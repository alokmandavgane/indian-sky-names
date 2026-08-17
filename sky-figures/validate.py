#!/usr/bin/env python3
"""Check `figures.json` against the databases it makes claims about.

A figure is the strongest claim this research makes. A name says a language calls
these stars something; a figure says it joins them into a shape, and every star
assigned to a role asserts that the source put it there. So the invariants are
tighter than the name database's, and all of them are asserted rather than
trusted:

  * the culture exists, by slug, in `sky-identity/cultures.json`;
  * the object exists in `star-names-local.json`;
  * every HIP is a real star in the vendored Hipparcos catalogue, which is what
    catches the failure that actually happens — a mistyped number drawing a line
    across the sky to nowhere;
  * `spans` names every IAU constellation the figure's stars fall in, and the
    validator recomputes it. This is deliberately NOT a containment rule. The
    first draft required every star to belong to the object's own figure, and the
    material threw it out within a minute: the Bhili cot uses Alcor, which the
    IAU figure of Ursa Major does not draw a line through, and the Kolam Mahua
    tree stands in Crux with two women beside it in Centaurus. A culture's figure
    is under no obligation to use the IAU figure's vertices or to stop at its
    boundary — that is the whole reason figures need a record of their own. So
    crossing a boundary is not an error; failing to declare it is;
  * a part with stars is `attested: true` and one without is `attested: false`,
    so an unfilled role can never read as a filled one;
  * `quote`-style access discipline: `source_access` is one of the two values the
    name database uses, and the same rule applies — in-copyright material is
    paraphrased, never quoted.

    python3 validate.py

Exits non-zero on the first thing that does not hold.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)
FIGURES = os.path.join(HERE, "figures.json")
IDENTITY = os.path.join(DOCS, "sky-identity", "sky-identity.json")
CULTURES = os.path.join(DOCS, "sky-identity", "cultures.json")
LOCAL_DB = os.path.join(DOCS, "star-names-local", "star-names-local.json")
SANSKRIT_DB = os.path.join(DOCS, "star-names", "star-names.json")

ACCESS = {"public-domain", "in-copyright-paraphrased"}
CONFIDENCE = {"certain", "likely", "disputed", "unidentified"}

# The Sanskrit textual tradition draws figures too — the Purāṇic Śiśumāra is one —
# but it is not a language of the vernacular compilation: it has no entry in
# `cultures.json`, and its objects live in `star-names`, not `star-names-local`.
# So it is admitted by name, and its objects are checked against its own database.
TRADITIONS = {"sanskrit"}


def load_catalogue():
    """HIP -> IAU constellation, from the catalogues sky-identity already reads.

    Imported rather than re-read: `resolve.py` is the one place that knows how the
    vendored files are shaped, and a second reader of them would be a second thing
    to keep in step.
    """
    sys.path.insert(0, os.path.join(DOCS, "sky-identity"))
    import resolve

    hip_table = resolve.load_hipparcos()
    bayer = resolve.load_bayer()
    constellation = {h: b["constellation"] for h, b in bayer.items() if b["constellation"]}
    return hip_table, constellation


def main():
    figs = json.load(open(FIGURES, encoding="utf-8"))["figures"]
    cultures = json.load(open(CULTURES, encoding="utf-8"))["cultures"]
    objects = {o["key"] for o in json.load(open(LOCAL_DB, encoding="utf-8"))["objects"]}
    sanskrit_objects = {s["id"] for s in json.load(open(SANSKRIT_DB, encoding="utf-8"))["stars"]}
    hip_table, constellation_of = load_catalogue()

    errors, ids = [], set()
    n_parts = n_attested = n_stars = 0

    for f in figs:
        fid = f.get("id") or "<no id>"

        def bad(msg):
            errors.append(f"{fid}: {msg}")

        if fid in ids:
            bad("duplicate id")
        ids.add(fid)

        if f.get("culture") in TRADITIONS:
            if f.get("object") not in sanskrit_objects:
                bad(f"unknown object {f.get('object')!r} — not in the Sanskrit database")
        else:
            if f.get("culture") not in cultures:
                bad(f"unknown culture {f.get('culture')!r}")
            if f.get("object") not in objects:
                bad(f"unknown object {f.get('object')!r}")
        if f.get("source_access") not in ACCESS:
            bad(f"bad source_access {f.get('source_access')!r}")
        if f.get("confidence") not in CONFIDENCE:
            bad(f"bad confidence {f.get('confidence')!r}")
        if not (f.get("citation") or "").strip():
            bad("no citation — a figure without one is not evidence")
        if not (f.get("scene") or "").strip():
            bad("no scene — what the culture sees is the content of the record")

        parts = f.get("parts") or []
        if not parts:
            bad("no parts — a figure is its parts")
        touched = set()
        for p in parts:
            n_parts += 1
            role = (p.get("role") or "").strip()
            hips = p.get("hip")
            if not role:
                bad("a part with no role")
            if not isinstance(hips, list):
                bad(f"part {role!r}: `hip` must be a list, empty where unassigned")
                continue
            n_stars += len(hips)
            if p.get("attested") is not bool(hips):
                bad(f"part {role!r}: attested={p.get('attested')!r} contradicts "
                    f"{len(hips)} star(s) — a role with stars is attested, one "
                    f"without is not")
            if hips:
                n_attested += 1
            for h in hips:
                if h not in hip_table:
                    bad(f"part {role!r}: HIP {h} is not a star in the catalogue")
                elif h in constellation_of:
                    touched.add(constellation_of[h])

        declared = set(f.get("spans") or [])
        if declared != touched and touched:
            bad(f"spans {sorted(declared)} but the stars are in {sorted(touched)} — "
                f"a figure must say which constellations it stands in")

    print(f"{len(figs)} figures, {n_parts} parts ({n_attested} with stars, "
          f"{n_parts - n_attested} recorded as roles the source leaves unfilled), "
          f"{n_stars} star assignments")

    by_culture = {}
    for f in figs:
        by_culture.setdefault(f["culture"], []).append(f["object"])
    for c, objs in sorted(by_culture.items()):
        print(f"   {c:<12} {', '.join(sorted(objs))}")

    if errors:
        print(f"\n{len(errors)} problem(s):", file=sys.stderr)
        for e in errors:
            print(f"   {e}", file=sys.stderr)
        sys.exit(1)
    print("\nevery invariant holds")


if __name__ == "__main__":
    main()
