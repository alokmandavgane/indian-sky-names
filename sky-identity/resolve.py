#!/usr/bin/env python3
"""Resolve every sky object in the two name databases to a catalog identity.

The databases say what a source calls a thing. The chart scripts say where to draw
it. Neither says *which star it is* in terms any other catalogue would recognise —
`modern_star` carries prose ("β Arietis", "the Pleiades") that a human reads and a
join cannot. This builds the missing layer: db-id → HIP.

HIP is the interlingua. It is what Stellarium's skycultures key their names by,
what SIMBAD resolves, and what `constellation-lines.json` already uses for the
figure work — so one number makes the vernacular record joinable to every other
star catalogue, and to the app's own chart stars, which carry `hipparcos` already.

Nothing here is typed from memory. Identity is resolved against the catalogues
this repo already vendors for the figure work, and every match is checked three
ways — angular separation, Bayer designation, IAU proper name — so that a wrong
identification is a reported disagreement rather than a silent one.

    python3 resolve.py            # report to stdout
    python3 resolve.py --write    # also write sky-identity.json

Positions are read out of the two `build_chart.py` files by parsing their syntax
tree, never by importing or executing them: those modules read their databases at
import time and are not safe to import from anywhere but their own directory.
This is a deliberate one-way read. Phase 0 adds an identity layer beside the
existing pipeline without disturbing it.
"""
import argparse
import ast
import csv
import json
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)
CL_SOURCES = os.path.join(DOCS, "constellation-lines", "sources")

SANSKRIT_CHART = os.path.join(DOCS, "star-names", "sources", "build_chart.py")
LOCAL_CHART = os.path.join(DOCS, "star-names-local", "sources", "build_chart.py")
SANSKRIT_DB = os.path.join(DOCS, "star-names", "star-names.json")
LOCAL_DB = os.path.join(DOCS, "star-names-local", "star-names-local.json")
FIGURES = os.path.join(DOCS, "constellation-lines", "constellation-lines.json")

# How close a catalogue star must sit to a plotted position to be believed. The
# tables round to two decimals (~36"), and the nearest naked-eye star to any given
# bright star is far further off than this, so a tenth of a degree separates a
# match from a coincidence without being so tight that rounding breaks it.
MATCH_TOLERANCE_DEG = 0.10

# Where a second star falls inside this, a position match alone is not evidence:
# the report says so and asks for the designation to settle it.
CROWDING_DEG = 0.50


# ---------------------------------------------------------------- catalogues


def load_hipparcos():
    """HIP -> position and magnitude, from the mag-7 Hipparcos snapshot.

    Public-domain ESA data, vendored for the constellation-figure work; RA is
    stored as sexagesimal strings there, so it is converted once here.
    """
    out = {}
    path = os.path.join(CL_SOURCES, "hipparcos-mag7.csv")
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                hip = int(row["HIP"])
                h, m, s = (float(x) for x in row["RAhms"].split())
                d, dm, ds = row["DEdms"].split()
                vmag = float(row["Vmag"])
            except (TypeError, ValueError):
                continue
            sign = -1 if d.startswith("-") else 1
            out[hip] = {
                "ra": (h + m / 60 + s / 3600) * 15,
                "dec": sign * (abs(float(d)) + float(dm) / 60 + float(ds) / 3600),
                "vmag": vmag,
                "spectral": (row.get("SpType") or "").strip(),
            }
    return out


# Bayer letters are stored as three-letter abbreviations ("alf", "tet01"); the
# chart tables and `modern_star` write them as Greek. Only what is needed to
# compare the two is mapped.
BAYER_GREEK = {
    # Theta appears as both "the" and "tet": the Bayer cross-index uses the first,
    # the IAU catalogue the second. Both are mapped, because a letter missing here
    # silently costs a star its designation rather than raising anything.
    "the": "θ",
    "alf": "α", "bet": "β", "gam": "γ", "del": "δ", "eps": "ε", "zet": "ζ",
    "eta": "η", "tet": "θ", "iot": "ι", "kap": "κ", "lam": "λ", "mu.": "μ",
    "nu.": "ν", "ksi": "ξ", "omi": "ο", "pi.": "π", "rho": "ρ", "sig": "σ",
    "tau": "τ", "ups": "υ", "phi": "φ", "chi": "χ", "psi": "ψ", "ome": "ω",
}


def load_bayer():
    """HIP -> Bayer letter, Flamsteed number and constellation."""
    out = {}
    path = os.path.join(CL_SOURCES, "bayer-flamsteed-crossindex.csv")
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                hip = int(row["HIP"])
            except (TypeError, ValueError):
                continue
            raw = (row.get("Bayer") or "").strip()
            # "tet01" is θ¹: the letter is the first three characters, the rest a
            # superscript index distinguishing members of a lettered pair.
            letter = BAYER_GREEK.get(raw[:3].lower(), "") if raw else ""
            index = raw[3:].lstrip("0") if len(raw) > 3 else ""
            out[hip] = {
                "bayer": letter,
                "bayer_index": index,
                "flamsteed": (row.get("Fl") or "").strip(),
                "constellation": (row.get("Cst") or "").strip(),
            }
    return out


# The catalogue's tail is regular where its middle is not: HIP, HD, RA, Dec and a
# date, with "_" standing in wherever a star has no such designation. Anchoring on
# that tail reads the file without depending on column offsets holding, which they
# do not — the diacritic and Bayer columns carry characters of differing width.
CSN_TAIL = re.compile(
    r"\s(\d+|_)\s+(\d+|_)\s+(-?[\d.]+)\s+(-?[\d.]+)\s+\d{4}-\d{2}-\d{2}"
)


def load_iau_names(hip_table=None):
    """HIP -> IAU-approved proper name, from the WGSN catalogue.

    Where `hip_table` is given, every parse is confirmed against it: the name's own
    RA/Dec must land on the Hipparcos position for the HIP it claims. That makes a
    misparsed row an error here rather than a wrong star downstream.
    """
    path = os.path.join(CL_SOURCES, "iau-csn.txt")
    out, checked, rejected = {}, 0, 0
    for ln in open(path, encoding="utf-8").read().splitlines():
        if ln.startswith("#") or not ln.strip():
            continue
        m = CSN_TAIL.search(ln)
        if not m or not m.group(1).isdigit():
            continue  # exoplanet hosts and the like carry "_" for HIP
        hip = int(m.group(1))
        ra, dec = float(m.group(3)), float(m.group(4))
        if hip_table and hip in hip_table:
            s = hip_table[hip]
            if separation(ra, dec, s["ra"], s["dec"]) > 0.05:
                rejected += 1
                continue
            checked += 1
        # A star can be named twice (components A and B); the first wins, which is
        # the primary in every case the databases here reach.
        out.setdefault(hip, ln[:18].strip())
    if hip_table:
        print(f"  IAU names: {len(out)} parsed, {checked} position-confirmed, "
              f"{rejected} rejected on position")
    return out


def load_figure_constellations():
    """IAU abbreviation -> the HIPs the figure work draws, for constellation-shaped objects.

    Only stars the figure actually runs through: `constellation-lines.json` charts
    field stars too, and a culture that names "Orion" means the shape, not every
    star inside its boundary.
    """
    data = json.load(open(FIGURES, encoding="utf-8"))
    out = {}
    for c in data["constellations"]:
        abbr = c.get("abbr") or ""
        hips = [int(s["hip"]) for s in c.get("stars", []) if s.get("hip") and s.get("figure")]
        if abbr:
            out[abbr] = {"id": c.get("id"), "hips": sorted(hips)}
    return out


# ------------------------------------------------------- the position tables


def position_table(path, varname):
    """The `P` / `POS` dict out of a chart script, without importing it."""
    tree = ast.parse(open(path, encoding="utf-8").read())
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(isinstance(t, ast.Name) and t.id == varname for t in node.targets):
            return ast.literal_eval(node.value)
    raise SystemExit(f"{os.path.basename(path)}: no `{varname} = {{...}}` found")


def trailing_comments(path):
    """key -> the `# Aldebaran` a table row was annotated with.

    These are the compiler's own identifications, written beside the coordinates,
    and they are the best independent check that a position match found the star
    that was meant rather than a neighbour.
    """
    out = {}
    for line in open(path, encoding="utf-8").read().splitlines():
        m = re.match(r'\s*"([a-z0-9\-]+)"\s*:\s*\(.*?#\s*(.+?)\s*$', line)
        if m:
            out[m.group(1)] = m.group(2)
    return out


def modern_stars():
    """db-id / object-key -> the `modern_star` prose both databases carry."""
    out = {}
    sk = json.load(open(SANSKRIT_DB, encoding="utf-8"))
    for s in sk["stars"]:
        ms = s.get("modern_star") or {}
        out[s["id"]] = {
            "common_name": ms.get("common_name") or "",
            "bayer": ms.get("bayer") or "",
            "constellation": ms.get("constellation") or "",
        }
    lo = json.load(open(LOCAL_DB, encoding="utf-8"))
    for o in lo["objects"]:
        ms = o.get("modern_star") or {}
        out.setdefault("local:" + o["key"], {
            "common_name": ms.get("common_name") or "",
            "bayer": ms.get("bayer") or "",
            "constellation": ms.get("constellation") or "",
        })
    return out


# -------------------------------------------------------------- the matching


def separation(ra1, dec1, ra2, dec2):
    """Angular separation in degrees."""
    p1, p2 = math.radians(dec1), math.radians(dec2)
    dl = math.radians(ra1 - ra2)
    v = math.sin(p1) * math.sin(p2) + math.cos(p1) * math.cos(p2) * math.cos(dl)
    return math.degrees(math.acos(max(-1.0, min(1.0, v))))


def nearest(hip_table, ra, dec, limit=CROWDING_DEG):
    """Catalogue stars within `limit` of a position, closest first."""
    near = []
    for hip, s in hip_table.items():
        if abs(s["dec"] - dec) > limit:
            continue  # cheap reject before the trigonometry
        d = separation(ra, dec, s["ra"], s["dec"])
        if d <= limit:
            near.append((d, hip))
    near.sort()
    return near


def designation_of(hip, bayer, hip_table):
    """'η Tau' — the Bayer designation, where the cross-index has one."""
    b = bayer.get(hip)
    if not b or not b["bayer"]:
        return ""
    return f"{b['bayer']}{b['bayer_index']} {b['constellation']}".replace(" ", " ").strip()


GREEK_BY_NAME = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ε",
    "zeta": "ζ", "eta": "η", "theta": "θ", "iota": "ι", "kappa": "κ",
    "lambda": "λ", "mu": "μ", "nu": "ν", "xi": "ξ", "omicron": "ο", "pi": "π",
    "rho": "ρ", "sigma": "σ", "tau": "τ", "upsilon": "υ", "phi": "φ",
    "chi": "χ", "psi": "ψ", "omega": "ω",
}
GREEK_SPELLED = {v: k for k, v in GREEK_BY_NAME.items()}


def name_agrees(hint, proper_name, designation, flamsteed):
    """Does an identification written by hand corroborate the catalogue's?

    `hint` is a trailing comment or a `modern_star` string — free prose, sometimes
    naming the star ("Aldebaran", "theta Vir", "35 Arietis") and sometimes only
    describing it ("the stars of Orion's head"). Position is the primary evidence;
    this is corroboration, so the constellation is not required to agree — a Greek
    letter or Flamsteed number landing on a star already matched to arcseconds is
    confirmation enough, and demanding more only manufactures false disagreements.

    Returns True on agreement, False on a name that contradicts, None where the
    hint names no star at all and there is nothing to check.
    """
    if not hint:
        return None
    h = hint.lower()
    if proper_name:
        if proper_name.lower() in h:
            return True
        # "Asellus Aus." for "Asellus Australis": the catalogue's first word is
        # distinctive enough on its own once it is longer than a Greek letter.
        first = proper_name.split()[0].lower()
        if len(first) > 3 and first in h:
            return True
    if designation:
        letter = designation.split()[0][0]  # strip any superscript index
        spelled = GREEK_SPELLED.get(letter)
        if letter in hint or (spelled and re.search(rf"\b{spelled}\b", h)):
            return True
    if flamsteed and re.search(rf"\b{flamsteed}\b", h):
        return True
    return False if _names_a_star(hint) else None


def _names_a_star(hint):
    """Does this hint identify a star at all, or only describe one?

    A hint that names nothing cannot disagree with anything, and reporting it as a
    contradiction would bury the real ones. Prose like "the stars of Orion's head"
    carries no designation; "Alcyone" and "lambda Aqr" both do.
    """
    h = hint.lower()
    if re.search(r"\b\d+\s+[A-Z][a-z]+", hint):        # Flamsteed: "35 Arietis"
        return True
    if any(re.search(rf"\b{g}\b", h) for g in GREEK_SPELLED.values()):
        return True
    if any(ch in hint for ch in GREEK_SPELLED):
        return True
    # A capitalised word reads as a proper name — but not the first word, which is
    # as likely to be a sentence opener as a designation.
    return bool(re.search(r"\S+\s+.*?\b[A-Z][a-z]{3,}", hint))


def resolve(entries, hip_table, bayer, iau, source):
    """Resolve one position table. `entries` is key -> (ra, dec, kind, mag or None)."""
    results = {}
    for key, (ra, dec, kind, mag) in sorted(entries.items()):
        rec = {"source": source, "kind": kind}
        if ra is None or kind not in ("star",):
            # Figures, clusters and the unplaced are not one star and must not be
            # given one. They are carried through unresolved, for the phase that
            # gives figures their member lists.
            rec["resolution"] = "not-a-single-star"
            results[key] = rec
            continue

        near = nearest(hip_table, ra, dec)
        if not near:
            rec["resolution"] = "unresolved"
            results[key] = rec
            continue

        dist, hip = near[0]
        star = hip_table[hip]
        b = bayer.get(hip, {})
        rec.update({
            "hip": hip,
            "separation_arcsec": round(dist * 3600, 1),
            "vmag": star["vmag"],
            "designation": designation_of(hip, bayer, hip_table),
            "flamsteed": b.get("flamsteed", ""),
            "proper_name": iau.get(hip, ""),
            "spectral": star["spectral"],
        })
        rec["resolution"] = "position" if dist <= MATCH_TOLERANCE_DEG else "far"
        # The Sanskrit table carries the magnitude it plotted at. Agreement with
        # the catalogue's is evidence entirely independent of position and of the
        # hand-written name — the check that settles the prose-only hints.
        if mag is not None:
            rec["plotted_vmag"] = mag
            rec["vmag_agrees"] = abs(mag - star["vmag"]) <= 0.06
        contenders = [h for d, h in near[1:] if d <= CROWDING_DEG]
        if contenders:
            rec["crowded_by"] = contenders[:4]
        results[key] = rec
    return results


# ------------------------------------------------------------------ figures
#
# A figure is not one star, so it gets a list. There are exactly two honest ways
# to fill that list, and both are used below; neither types a HIP by hand.
#
#   1. The figure IS a constellation. Its members are the stars the figure work
#      already draws lines through, pulled from constellation-lines.json.
#   2. The compilation's own note enumerates the stars. Those enumerations are
#      transcribed here AS DESIGNATIONS — "delta Leo", "Bellatrix" — and resolved
#      to HIP against the catalogues, so a typo becomes an unresolved token rather
#      than a wrong star.
#
# Where a note enumerates nothing ("the Scorpion's tail as a whole"), the figure
# is left without members. Inventing a boundary the source did not draw would be
# the one thing this database has never done.

FIGURE_CONSTELLATIONS = {
    # Sanskrit
    "mriga": ["Ori"],            # "the whole figure of Orion (Aitareya Brāhmaṇa 3.33)"
    "shishumara": ["Dra"],       # "Plotted over Draco, the strongest reading of the older figure"
    "sakvara": ["Dra"],          # al-Bīrūnī's second name for the Śiśumāra, plotted with it
    "trishanku": ["Cru"],        # "the usual modern gloss — but no Purāṇa says so"
    # Vernacular
    "local:ursa-major": ["UMa"], "local:ursa-minor": ["UMi"],
    "local:orion": ["Ori"], "local:scorpius": ["Sco"], "local:pegasus": ["Peg"],
    "local:taurus": ["Tau"], "local:crux": ["Cru"], "local:canis-major": ["CMa"],
    "local:corona-australis": ["CrA"], "local:delphinus": ["Del"],
    "local:monoceros": ["Mon"], "local:auriga": ["Aur"], "local:lupus": ["Lup"],
    "local:cygnus": ["Cyg"], "local:centaurus": ["Cen"], "local:corvus": ["Crv"],
    "local:lyra": ["Lyr"], "local:aquila": ["Aql"], "local:norma": ["Nor"],
    "local:cassiopeia": ["Cas"], "local:grus": ["Gru"], "local:pisces": ["Psc"],
    "local:leo-virgo": ["Leo", "Vir"],   # one object spanning two constellations
}

FIGURE_MEMBERS = {
    # Each list is what the object's own plotnote or title states, nothing more.
    "ishus-trikanda": ["Mintaka", "Alnilam", "Alnitak"],   # "Orion's Belt (Mintaka, Alnilam, Alnitak)"
    "ilvala": ["lambda Ori", "phi1 Ori", "phi2 Ori"],      # "the group, λ/φ¹/φ² Orionis, is stated by the lexicon itself"
    "bahu": ["Betelgeuse", "Bellatrix"],                   # "usually Betelgeuse + Bellatrix"
    "arjuni": ["delta Leo", "theta Leo", "beta Leo"],      # "both Phalgunīs (δ/θ Leonis and β Leonis)"
    "vichritau": ["Shaula", "Lesath"],                     # "Shaula (λ Sco) and Lesath (υ Sco)"
    "proshthapada": ["Markab", "Algenib"],                 # "both Bhādrapadās (α Pegasi and γ Pegasi)"
    "local:orions-belt": ["Mintaka", "Alnilam", "Alnitak"],
    "local:castor-pollux": ["Castor", "Pollux"],           # a pair, not a cluster
}

# Figures whose members are other objects in the same table — so the two can never
# drift apart, and the seven ṛṣis stay the seven stars the compilation names.
FIGURE_ALIAS_OF = {
    "saptarshi": ["marichi", "vasishtha", "angiras", "atri",
                  "pulastya", "pulaha", "kratu"],
    "rksha": ["marichi", "vasishtha", "angiras", "atri",
              "pulastya", "pulaha", "kratu"],   # "the same seven stars as the Saptarṣi"
}

# Clusters are identified by their cluster designation, which is what they are;
# the bright members are listed where the tradition counts them individually.
CLUSTERS = {
    "krittika-seven": ("M45", ["Alcyone", "Atlas", "Electra", "Maia", "Merope",
                               "Taygeta", "Pleione", "Asterope", "Celaeno"]),
    "local:pleiades": ("M45", ["Alcyone", "Atlas", "Electra", "Maia", "Merope",
                               "Taygeta", "Pleione", "Asterope", "Celaeno"]),
    "local:praesepe": ("M44", []),
    "local:hyades": ("Mel 25", []),
}

# Notes on figures deliberately left without members.
NO_MEMBERS = {
    "mulabarhana": "'the Scorpion's tail as a whole' — the note draws no boundary, "
                   "and the tail's extent is not stated by any source here.",
    "local:milky-way": "The galactic band; drawn as a band, not as member stars.",
}

SUPERSCRIPT = {"¹": "1", "²": "2", "³": "3"}


def resolve_token(token, iau_inverse, bayer_index):
    """'Bellatrix' or 'phi1 Ori' -> HIP, or None if the catalogues do not know it."""
    t = token.strip()
    if t in iau_inverse:
        return iau_inverse[t]
    for uni, ascii_digit in SUPERSCRIPT.items():
        t = t.replace(uni, ascii_digit)
    parts = t.split()
    if len(parts) != 2:
        return None
    letter, cst = parts
    m = re.match(r"([A-Za-z]+)(\d*)$", letter)
    if not m:
        return None
    greek = GREEK_BY_NAME.get(m.group(1).lower())
    if not greek:
        return None
    return bayer_index.get((greek, m.group(2), cst))


def resolve_figures(results, hip_table, bayer, iau):
    """Fill in member HIPs for every figure and cluster. Returns unresolved tokens."""
    constellations = load_figure_constellations()
    iau_inverse = {v: k for k, v in iau.items()}
    bayer_index = {}
    for hip, b in bayer.items():
        if b["bayer"]:
            bayer_index[(b["bayer"], b["bayer_index"], b["constellation"])] = hip

    unresolved = []
    for key, rec in results.items():
        if rec["kind"] == "star":
            continue
        members, how = [], None

        if key in FIGURE_ALIAS_OF:
            how = "objects"
            for other in FIGURE_ALIAS_OF[key]:
                hip = (results.get(other) or {}).get("hip")
                if hip:
                    members.append(hip)
                else:
                    unresolved.append((key, other))
            rec["member_objects"] = FIGURE_ALIAS_OF[key]

        elif key in FIGURE_MEMBERS:
            how = "designations"
            for token in FIGURE_MEMBERS[key]:
                hip = resolve_token(token, iau_inverse, bayer_index)
                if hip:
                    members.append(hip)
                else:
                    unresolved.append((key, token))

        elif key in CLUSTERS:
            how = "cluster"
            catalog_id, names = CLUSTERS[key]
            rec["catalog_id"] = catalog_id
            for token in names:
                hip = resolve_token(token, iau_inverse, bayer_index)
                if hip:
                    members.append(hip)
                else:
                    unresolved.append((key, token))

        elif key in FIGURE_CONSTELLATIONS:
            how = "constellation"
            abbrs = FIGURE_CONSTELLATIONS[key]
            rec["iau_constellations"] = abbrs
            for a in abbrs:
                c = constellations.get(a)
                if c:
                    members.extend(c["hips"])
                else:
                    unresolved.append((key, a))

        elif key in NO_MEMBERS:
            rec["members_note"] = NO_MEMBERS[key]
            continue
        else:
            continue  # genuinely unplaced: planets, the word for "star", weather

        if members:
            rec["member_hips"] = sorted(set(members))
            rec["members_from"] = how
            rec["resolution"] = "figure"
    return unresolved


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="write sky-identity.json")
    args = ap.parse_args()

    hip_table = load_hipparcos()
    bayer = load_bayer()
    print(f"catalogues: {len(hip_table)} Hipparcos stars, {len(bayer)} Bayer rows")
    iau = load_iau_names(hip_table)
    ms = modern_stars()

    # The Sanskrit table's tuples are (ra, dec, mag, kind, dev_short, note).
    sanskrit_raw = position_table(SANSKRIT_CHART, "P")
    sanskrit = {k: (v[0], v[1], v[3], v[2]) for k, v in sanskrit_raw.items()}
    sanskrit_hints = trailing_comments(SANSKRIT_CHART)

    # The chart script expands `P` at runtime with ALIAS_OF: names that different
    # texts give the same star, plotted on the very point they denote. A literal
    # read of the table misses all of them, so the same expansion is applied here —
    # and each alias resolves through the same verified path as its target rather
    # than inheriting a HIP unchecked.
    aliases = position_table(SANSKRIT_CHART, "ALIAS_OF")
    for alias, target in aliases.items():
        if target in sanskrit:
            sanskrit[alias] = sanskrit[target]

    # The local table's are (ra, dec, kind), with no magnitude to check against.
    local_raw = position_table(LOCAL_CHART, "POS")
    local = {k: (v[0], v[1], v[2], None) for k, v in local_raw.items()}

    # Local objects keyed `nak-<sanskrit id>` take their position from the Sanskrit
    # table — the bridge the local chart calls NAK_FROM_SANSKRIT, which is what
    # keeps the two charts from drifting. Identity has to cross it too.
    local_db = json.load(open(LOCAL_DB, encoding="utf-8"))
    for obj in local_db["objects"]:
        key = obj["key"]
        if key.startswith("nak-") and key not in local:
            sid = key[4:]
            if sid in sanskrit:
                local[key] = sanskrit[sid]

    res_s = resolve(sanskrit, hip_table, bayer, iau, "sanskrit")
    res_l = resolve(local, hip_table, bayer, iau, "local")

    # Check each resolution against what the compiler wrote by hand.
    for key, rec in res_s.items():
        hint = sanskrit_hints.get(key) or ms.get(key, {}).get("common_name", "")
        rec["hint"] = hint
        rec["agrees"] = name_agrees(hint, rec.get("proper_name", ""),
                                    rec.get("designation", ""), rec.get("flamsteed", ""))
    for key, rec in res_l.items():
        m = ms.get("local:" + key, {})
        # The local keys are themselves star names ("alcor", "betelgeuse"), assigned
        # by canon.py from the sources' prose — an input independent of the position
        # table, so agreement between the two corroborates as much as a comment does.
        hint = " ".join(x for x in (m.get("common_name"), m.get("bayer")) if x) \
            or key.replace("-", " ").title()
        rec["hint"] = hint
        rec["agrees"] = name_agrees(hint, rec.get("proper_name", ""),
                                    rec.get("designation", ""), rec.get("flamsteed", ""))

    # Figures are resolved over both tables at once: the vernacular objects are
    # prefixed, the Sanskrit ones are not, and `saptarshi` reaches its seven ṛṣis
    # by object key. The records are shared, so filling them here fills them in
    # the per-source views too.
    # Star-roads are figures made of nakshatras: the chart draws each as a dashed
    # line through its own three. They are not in `P` — they have no point of their
    # own — so their records are minted here, with members by object key so a road
    # can never disagree with the nakshatras it runs through.
    roads = position_table(SANSKRIT_CHART, "ROADS")
    for road, members in roads.items():
        res_s.setdefault(road, {
            "source": "sanskrit",
            "kind": "road",
            "resolution": "not-a-single-star",
            "member_objects": list(members),
        })

    combined = {**res_s, **{"local:" + k: v for k, v in res_l.items()}}
    for road, members in roads.items():
        hips = [combined[m]["hip"] for m in members
                if m in combined and combined[m].get("hip")]
        if hips:
            combined[road]["member_hips"] = sorted(set(hips))
            combined[road]["members_from"] = "objects"
            combined[road]["resolution"] = "figure"

    unresolved_tokens = resolve_figures(combined, hip_table, bayer, iau)

    # Record which entries are aliases, so a consumer can tell "another text's name
    # for Aldebaran" from an independent identification of it.
    for alias, target in aliases.items():
        if alias in combined and target in combined:
            combined[alias]["alias_of"] = target

    report(res_s, "SANSKRIT  (docs/star-names)")
    report(res_l, "LOCAL     (docs/star-names-local)")
    report_figures(combined, unresolved_tokens)

    if args.write:
        out = {
            "generated_by": "docs/sky-identity/resolve.py",
            "catalogues": {
                "hipparcos": "constellation-lines/sources/hipparcos-mag7.csv",
                "bayer": "constellation-lines/sources/bayer-flamsteed-crossindex.csv",
                "iau_names": "constellation-lines/sources/iau-csn.txt",
                "figures": "constellation-lines/constellation-lines.json",
            },
            "objects": combined,
        }
        path = os.path.join(HERE, "sky-identity.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=1)
        print(f"\nwrote {path}")


def report_figures(combined, unresolved_tokens):
    figures = {k: v for k, v in combined.items() if v["kind"] != "star"}
    filled = {k: v for k, v in figures.items() if v.get("member_hips")}
    noted = {k: v for k, v in figures.items() if v.get("members_note")}
    empty = {k: v for k, v in figures.items()
             if not v.get("member_hips") and not v.get("members_note")}

    print(f"\n{'=' * 78}\nFIGURES AND CLUSTERS\n{'=' * 78}")
    print(f"{len(figures)} objects that are not a single star")
    by_how = {}
    for k, v in filled.items():
        by_how.setdefault(v["members_from"], []).append(k)
    for how in sorted(by_how):
        n = sum(len(filled[k]["member_hips"]) for k in by_how[how])
        print(f"  {len(by_how[how]):>3} given members from {how:<14} ({n} stars)")
    print(f"  {len(noted):>3} deliberately without members (note recorded)")
    print(f"  {len(empty):>3} unplaced — planets, weather, the word for 'star'")

    if filled:
        print("\n  -- members --")
        for k, v in sorted(filled.items()):
            hips = v["member_hips"]
            shown = ", ".join(str(h) for h in hips[:6])
            more = f" +{len(hips) - 6}" if len(hips) > 6 else ""
            src = v.get("catalog_id") or ",".join(v.get("iau_constellations", [])) or v["members_from"]
            print(f"     {k:<26} {len(hips):>2} stars  [{src}]  {shown}{more}")
    if unresolved_tokens:
        print("\n  !! tokens the catalogues could not resolve --")
        for key, token in unresolved_tokens:
            print(f"     {key:<26} {token!r}")


def evidence(rec):
    """The independent lines of evidence backing one resolution."""
    got = []
    if rec.get("resolution") == "position":
        got.append("position")
    if rec.get("vmag_agrees"):
        got.append("magnitude")
    if rec.get("agrees"):
        got.append("name")
    return got


def report(results, title):
    stars = {k: v for k, v in results.items() if v["kind"] == "star"}
    other = {k: v for k, v in results.items() if v["kind"] != "star"}
    placed = {k: v for k, v in stars.items() if v.get("resolution") == "position"}
    bad = {k: v for k, v in stars.items() if v.get("resolution") != "position"}
    # A name that fails to match is only a contradiction when nothing else
    # corroborates. Where position AND magnitude both agree, the star is settled
    # and the mismatch is orthography — "Pole Star" for Polaris, "Āśleṣā" for the
    # IAU's Ashlesha. Calling that a contradiction would cry wolf on every run.
    contradicted = {k: v for k, v in placed.items()
                    if v.get("agrees") is False and not v.get("vmag_agrees")}
    spelling = {k: v for k, v in placed.items()
                if v.get("agrees") is False and v.get("vmag_agrees")}
    # An alias is another text's name for a star already identified; its evidence
    # is its target's, so it is not weak for lacking its own.
    weak = {k: v for k, v in placed.items()
            if len(evidence(v)) < 2 and not v.get("alias_of")}

    print(f"\n{'=' * 78}\n{title}\n{'=' * 78}")
    print(f"{len(stars)} single stars, {len(other)} figures/clusters/unplaced")
    by_strength = {}
    for k, v in placed.items():
        by_strength.setdefault(len(evidence(v)), []).append(k)
    for n in sorted(by_strength, reverse=True):
        lines = "+".join(sorted({"/".join(evidence(placed[k])) for k in by_strength[n]}))
        print(f"  {len(by_strength[n]):>3} confirmed by {n} independent line(s): {lines}")
    if bad:
        print(f"  {len(bad):>3} unresolved or beyond tolerance")

    if contradicted:
        print("\n  -- the hand-written name CONTRADICTS the catalogue (needs a human) --")
        for k, v in contradicted.items():
            print(f"     {k:<22} HIP {v.get('hip'):<7} "
                  f"{v.get('proper_name') or v.get('designation') or '?':<18} "
                  f"({v.get('separation_arcsec')}\")  hint: {v.get('hint')!r}")
    if spelling:
        print(f"\n  -- {len(spelling)} settled by position+magnitude; the name is "
              f"spelled differently --")
        for k, v in spelling.items():
            print(f"     {k:<22} HIP {v.get('hip'):<7} "
                  f"{v.get('proper_name') or v.get('designation') or '?':<18} "
                  f"hint: {v.get('hint')!r}")
    if weak:
        print("\n  -- position only, nothing to corroborate it --")
        for k, v in weak.items():
            print(f"     {k:<22} HIP {v.get('hip'):<7} "
                  f"{v.get('proper_name') or v.get('designation') or '?':<18} "
                  f"hint: {v.get('hint')!r}")
    if bad:
        print("\n  -- unresolved --")
        for k, v in bad.items():
            print(f"     {k:<22} {v.get('resolution')}  "
                  f"nearest HIP {v.get('hip')} at {v.get('separation_arcsec')}\"")
    crowded = {k: v for k, v in stars.items() if v.get("crowded_by")}
    if crowded:
        print(f"\n  -- {len(crowded)} in crowded fields (position alone is weak evidence) --")
        for k, v in list(crowded.items()):
            print(f"     {k:<22} HIP {v.get('hip')} {v.get('proper_name', ''):<14} "
                  f"also within 0.5°: {v['crowded_by']}")


if __name__ == "__main__":
    main()
