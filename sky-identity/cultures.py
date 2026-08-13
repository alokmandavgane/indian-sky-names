#!/usr/bin/env python3
"""Give every sky culture in the vernacular database a stable slug.

The database groups names by LANGUAGE, in the compilation's own English form —
"Mizo (Lushai)", "Sema (Sumi) Naga". Those strings are right for a page of prose
and wrong for everything else: they cannot be a URL, a directory name, or a key
the app and the site agree on. This mints the slug that can be all three, and
carries the ISO 639-3 code beside it as the machine identity.

The slug is the readable one, not the code. `/culture/marathi/` is worth more to
a reader and to a search engine than `/culture/mar/`, and the code is one field
away for anything that needs to join on it.

WHY LANGUAGE AND NOT LANGUAGE x COMMUNITY. The database also carries a
`community` field, and it was tempting to make the culture the pair. The data
says otherwise: of eleven distinct values, most are provenance prose rather than
an identity — "Hindu households of Sialkot district; Rose's informants are not
further specified". Only a handful are ethnonyms. Splitting cultures on a field
that is usually a footnote would mint a dozen near-empty cultures and bury the
real ones, so community stays an annotation on the name, where the source put it.

REGISTER IS A STRATUM, NOT A BOUNDARY. Marathi-sanskritic and Marathi-vernacular
are one culture seen at two depths, and that they coexist is the database's whole
finding. Register stays a facet within a culture and never splits one.

    python3 cultures.py            # report to stdout
    python3 cultures.py --write    # also write cultures.json
"""
import argparse
import json
import os
import re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)
LOCAL_DB = os.path.join(DOCS, "star-names-local", "star-names-local.json")
SANSKRIT_DB = os.path.join(DOCS, "star-names", "star-names.json")

# Where the compilation's English name does not reduce cleanly, or reduces to
# something that misleads. Everything else is derived by rule.
SLUG_OVERRIDES = {
    # The parenthetical is the second half of a compound ethnonym, not a gloss to
    # be dropped: "Sumi" qualifies "Naga" and the tribe is Sema Naga.
    "Sema (Sumi) Naga": "sema-naga",
}

# Labels that name a family rather than a language. The database uses them where a
# source did, and they cannot be given one ISO code because they do not have one.
# Recorded rather than resolved: inventing a code would be a claim the source
# never made.
UMBRELLA = {
    "Nicobarese": "A cover term in the sources; the database also carries Central "
                  "Nicobarese, Chaura and Teressa as languages in their own right.",
    "Andamanese": "A cover term for two distinct languages (Aka-Bea, Aka-Jeru) that "
                  "no source here separates.",
}


def slugify(name):
    """"Mizo (Lushai)" -> "mizo". The parenthetical is a gloss for the reader."""
    if name in SLUG_OVERRIDES:
        return SLUG_OVERRIDES[name]
    base = re.sub(r"\s*\([^)]*\)", "", name).strip()
    return re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")


def build():
    db = json.load(open(LOCAL_DB, encoding="utf-8"))
    cultures = {}
    for obj in db["objects"]:
        for n in obj["names"]:
            lang = n["language"]
            c = cultures.setdefault(lang, {
                "slug": slugify(lang),
                "name": lang,
                "iso639_3": set(),
                "regions": set(),
                "registers": Counter(),
                "communities": set(),
                "objects": set(),
                "entries": 0,
            })
            c["entries"] += 1
            c["objects"].add(obj["key"])
            if n.get("iso639_3"):
                c["iso639_3"].add(n["iso639_3"])
            if n.get("region"):
                c["regions"].add(n["region"])
            if n.get("register"):
                c["registers"][n["register"]] += 1
            if n.get("community"):
                c["communities"].add(n["community"])

    out = {}
    for lang, c in cultures.items():
        iso = sorted(c["iso639_3"])
        rec = {
            "slug": c["slug"],
            "name": lang,
            "iso639_3": iso[0] if len(iso) == 1 else None,
            "entries": c["entries"],
            "objects": len(c["objects"]),
            "registers": dict(c["registers"].most_common()),
            "regions": sorted(c["regions"]),
            "source": "star-names-local",
        }
        if len(iso) > 1:
            rec["iso639_3_candidates"] = iso
        if lang in UMBRELLA:
            rec["umbrella"] = UMBRELLA[lang]
        if c["communities"]:
            rec["communities"] = sorted(c["communities"])
        out[c["slug"]] = rec

    # The classical tradition is a sky culture too, and the flagship one — but it
    # lives in the other database and is a textual corpus rather than a speech
    # community, so it is added explicitly and marked as such.
    sk = json.load(open(SANSKRIT_DB, encoding="utf-8"))
    out["sanskrit"] = {
        "slug": "sanskrit",
        "name": "Sanskrit",
        "iso639_3": "san",
        "entries": len(sk["stars"]),
        "objects": len(sk["stars"]),
        "registers": {"classical": len(sk["stars"])},
        "regions": [],
        "source": "star-names",
        "note": "The classical textual tradition, compiled from śloka attestations "
                "rather than from a living speech community's usage.",
    }
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="write cultures.json")
    args = ap.parse_args()

    cultures = build()

    collisions = Counter(c["slug"] for c in cultures.values())
    dupes = [s for s, n in collisions.items() if n > 1]

    print(f"{len(cultures)} cultures\n")
    print(f"{'slug':<22} {'iso':<6} {'entries':>7} {'objects':>7}  registers")
    print("-" * 78)
    for slug, c in sorted(cultures.items(), key=lambda kv: -kv[1]["entries"]):
        reg = " ".join(f"{k[:4]}:{v}" for k, v in c["registers"].items())
        iso = c["iso639_3"] or "--"
        print(f"{slug:<22} {iso:<6} {c['entries']:>7} {c['objects']:>7}  {reg}")

    print()
    if dupes:
        print(f"!! slug collisions: {dupes}")
    else:
        print("no slug collisions")

    noiso = [s for s, c in cultures.items() if not c["iso639_3"]]
    if noiso:
        print(f"\nno single ISO 639-3 code ({len(noiso)}) — these need a decision:")
        for s in noiso:
            c = cultures[s]
            why = c.get("umbrella") or "no code in the sources"
            cand = c.get("iso639_3_candidates")
            print(f"  {s:<20} {('candidates ' + ','.join(cand)) if cand else 'none'}"
                  f"\n      {why}")

    if args.write:
        path = os.path.join(HERE, "cultures.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump({
                "generated_by": "docs/sky-identity/cultures.py",
                "unit": "One culture is one language as the compilation names it. "
                        "Register is a stratum within a culture, never a boundary; "
                        "community is an annotation on the name.",
                "cultures": dict(sorted(cultures.items())),
            }, f, ensure_ascii=False, indent=1)
        print(f"\nwrote {path}")


if __name__ == "__main__":
    main()
