"""Merge the seven per-language-group research files into the vernacular database.

Reads sources/*.json, writes ../star-names-local.json and ../README.md.
Grouping is by sky OBJECT (see canon.py), because the question is what the
different languages call one thing.

Read-only against docs/star-names/: the Sanskrit database is a separate
compilation and this script never writes to it.
"""
import json, os, glob, collections, unicodedata, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canon import canon, TITLES

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
SANSKRIT = os.path.join(OUT, "..", "star-names", "star-names.json")

FILES = ["hindi_urdu_punjabi", "marathi_gujarati", "bengali_assamese_odia",
         "tamil", "telugu_kannada", "malayalam_tulu_sinhala", "tribal"]

REGISTER_ORDER = ["vernacular", "folk", "tribal", "sanskritic"]
REGISTER_BLURB = {
    "vernacular": "formed in the language itself, not a Sanskrit loan",
    "folk": "rural or colloquial usage, from a dictionary's own usage note or from ethnography",
    "tribal": "from a distinct Adivasi tradition",
    "sanskritic": "the Sanskrit name in this language's script and phonology",
}
CONF_RANK = {"certain": 0, "likely": 1, "disputed": 2, "unidentified": 3}


def anchor(s):
    """GitHub's anchor algorithm: lowercase, keep letters/marks/numbers/-/_, spaces to hyphens."""
    out = []
    for ch in s.lower():
        if unicodedata.category(ch)[0] in "LMN" or ch in "-_":
            out.append(ch)
        elif ch == " ":
            out.append("-")
    return "".join(out)


def load_sanskrit():
    with open(SANSKRIT, encoding="utf-8") as f:
        db = json.load(f)
    return {s["id"]: s for s in db["stars"]}


def main():
    sk = load_sanskrit()
    sk_titles = {i: f"{s['name_iast']} ({s['modern_star']['common_name']})" for i, s in sk.items()}

    groups = collections.defaultdict(list)
    findings, caveats, langs_by_file = {}, {}, {}
    for name in FILES:
        with open(os.path.join(HERE, name + ".json"), encoding="utf-8") as f:
            src = json.load(f)
        findings[src["source_group"]] = src["summary_findings"]
        caveats[src["source_group"]] = src.get("caveats", [])
        langs_by_file[src["source_group"]] = src.get("languages", [])
        for e in src["entries"]:
            e = dict(e, _source_group=src["source_group"])
            groups[canon(e, sk_titles)].append(e)

    objects = []
    for key, entries in groups.items():
        entries.sort(key=lambda e: (REGISTER_ORDER.index(e["register"]) if e["register"] in REGISTER_ORDER else 9,
                                    e["language"], e["name_roman"]))
        ids = [e["sanskrit_db_id"] for e in entries if e["sanskrit_db_id"]]
        top_id = collections.Counter(ids).most_common(1)[0][0] if ids else None
        mods = [e["modern_star"] for e in entries if (e["modern_star"] or {}).get("common_name")]
        objects.append({
            "key": key,
            "title": TITLES.get(key, key),
            "sanskrit_db_id": top_id,
            "sanskrit_name": sk_titles.get(top_id) if top_id else None,
            "modern_star": mods[0] if mods else None,
            "languages": sorted({e["language"] for e in entries}),
            "n_names": len(entries),
            "names": entries,
        })
    # most widely named object first; that ordering is itself a finding
    objects.sort(key=lambda o: (-len(o["languages"]), -o["n_names"], o["title"]))

    all_entries = [e for o in objects for e in o["names"]]
    langs = collections.Counter(e["language"] for e in all_entries)
    regs = collections.Counter(e["register"] for e in all_entries)

    db = {
        "title": "Star names in the languages of India",
        "generated": "2026-08-02",
        "method": (
            "Compiled from public-domain lexicography and ethnography, chiefly the Digital Dictionaries of "
            "South Asia (dsal.uchicago.edu) and archive.org: Platts 1884, Fallon 1879 and Shakespear 1834 for "
            "Hindi/Urdu; Molesworth 1857 for Marathi; Maffei 1883 and Dalgado 1893 for Konkani; the Madras "
            "Tamil Lexicon 1924-39 and Winslow 1862 for Tamil; Brown 1852/1903 for Telugu; Kittel for Kannada; "
            "Gundert 1872 for Malayalam; Männer 1886 for Tulu; Carter and Clough for Sinhala; Praharaj and "
            "Jñānendramohana Dāsa for Odia and Bengali; and for the Adivasi languages Hoffmann's Encyclopaedia "
            "Mundarica, Bodding and Campbell on Santali, Grignard on Kurukh, Rivers 1906 on the Toda, Man 1883 "
            "and Radcliffe-Brown 1922 on the Andamans, and Russell & Hiralal 1916. Every name is quoted verbatim "
            "from a source that was actually fetched, with the page cited and the URL recorded; where a source "
            "printed only a romanization, no script is supplied and nothing was back-transliterated. Work still "
            "in copyright (notably the 2013 and 2023 JAHH papers on Gondi and Bhil astronomy, Samsad 2000 and "
            "Candrakanta 1962) is paraphrased and cited, never quoted. Wikipedia was not used as a source."
        ),
        "register_note": (
            "Every name is tagged by register. That is the point of the database rather than a detail: most "
            "Indian languages inherited the 27 Sanskrit nakshatra names and adapted them phonologically, and a "
            "table of those adaptations would be large and nearly uninformative. The tags separate that borrowed "
            "layer from names the languages made themselves. " +
            "; ".join(f"**{r}** — {REGISTER_BLURB[r]}" for r in REGISTER_ORDER) + "."
        ),
        "counts": {
            "entries": len(all_entries),
            "objects": len(objects),
            "languages": len(langs),
            "by_register": dict(regs),
            "by_language": dict(langs.most_common()),
            "linked_to_sanskrit_db": sum(1 for e in all_entries if e["sanskrit_db_id"]),
        },
        "language_groups": langs_by_file,
        "objects": objects,
        "summary_findings_by_source": findings,
        "caveats_by_source": caveats,
    }
    with open(os.path.join(OUT, "star-names-local.json"), "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=1)

    write_readme(db)
    print(f"{len(all_entries)} names, {len(objects)} sky objects, {len(langs)} languages")
    print("register:", dict(regs))


def write_readme(db):
    L = []
    A = L.append
    A("# Star names in the languages of India\n")
    A("What speakers of the different Indian languages call a star, an asterism or a constellation — "
      "with the dictionary or ethnography each name comes from, quoted and cited.\n")
    A(f"*Generated {db['generated']}. Machine-readable version: [`star-names-local.json`](star-names-local.json); "
      "per-language research files: [`sources/`](sources/).*\n")
    A("> **This file is generated — do not edit it.** The originals are the per-language-group research files in "
      "[`sources/`](sources/). See [`FORMAT.md`](FORMAT.md) for the schema and the editorial rules.\n")
    c = db["counts"]
    A(f"**{c['entries']} names** across **{c['languages']} languages** for **{c['objects']} sky objects**. "
      f"{c['linked_to_sanskrit_db']} link to an entry in the separate Sanskrit database at "
      f"[`../star-names/`](../star-names/); the rest have no Sanskrit counterpart, which is the interesting part.\n")
    A("**Register.** " + db["register_note"] + "\n")
    reg = c["by_register"]
    non = sum(v for k, v in reg.items() if k != "sanskritic")
    A(f"Of {c['entries']} names, **{non} are not Sanskrit** — "
      + ", ".join(f"{reg.get(r,0)} {r}" for r in REGISTER_ORDER) + ".\n")
    A("**Method.** " + db["method"] + "\n")

    A("## Languages\n")
    A("| Language | Names | Language | Names |")
    A("|---|--:|---|--:|")
    items = list(db["counts"]["by_language"].items())
    half = (len(items) + 1) // 2
    for i in range(half):
        a = items[i]
        b = items[i + half] if i + half < len(items) else ("", "")
        A(f"| {a[0]} | {a[1]} | {b[0]} | {b[1]} |")
    A("")

    A("## Sky objects, most widely named first\n")
    A("| Object | Languages | Names | Sanskrit counterpart |")
    A("|---|--:|--:|---|")
    for o in db["objects"]:
        sk = f"`{o['sanskrit_db_id']}`" if o["sanskrit_db_id"] else "—"
        A(f"| [{o['title']}](#{anchor(o['title'])}) | {len(o['languages'])} | {o['n_names']} | {sk} |")
    A("")

    for o in db["objects"]:
        A(f"## {o['title']}\n")
        if o["modern_star"] and o["modern_star"].get("common_name"):
            m = o["modern_star"]
            bits = [m.get("common_name"), m.get("bayer"), m.get("constellation")]
            A("**Modern:** " + " · ".join(b for b in bits if b and b != "—") + "  ")
        if o["sanskrit_db_id"]:
            A(f"**Sanskrit database:** `{o['sanskrit_db_id']}` — {o['sanskrit_name']} "
              f"([entry](../star-names/star-names.json))  ")
        A(f"**Named in {len(o['languages'])} languages:** " + ", ".join(o["languages"]) + "\n")
        A("| Language | Name | Romanized | Literally | Register |")
        A("|---|---|---|---|---|")
        for e in o["names"]:
            nat = e["name_native"] or "—"
            lit = (e["literal_meaning"] or "—").replace("|", "\\|")
            A(f"| {e['language']} | {nat} | *{e['name_roman']}* | {lit} | {e['register']} |")
        A("")
        for e in o["names"]:
            head = f"**{e['name_native'] + ' · ' if e['name_native'] else ''}{e['name_roman']}** "
            head += f"— {e['language']}"
            if e.get("region"):
                head += f" ({e['region']})"
            A(head + f" · *{e['register']}* · confidence: {e['confidence']}\n")
            if e.get("usage_note"):
                A(f"{e['usage_note']}\n")
            if e.get("quote"):
                A("> " + e["quote"].replace("\n", " ").strip())
                A(f"> <br>— {e['citation']}" + (f" ([source]({e['source_url']}))" if e.get("source_url") else "") + "\n")
            else:
                A(f"*No quotation: {e['citation']} is in copyright and is paraphrased only.*")
                A(f"> <br>— {e['citation']}" + (f" ([source]({e['source_url']}))" if e.get("source_url") else "") + "\n")
            if e.get("notes"):
                A(f"<sub>{e['notes']}</sub>\n")

    A("## Findings, per research file\n")
    for grp, text in db["summary_findings_by_source"].items():
        A(f"### {grp}\n")
        A(text + "\n")

    A("## Caveats, per research file\n")
    A("Read these before treating any entry as settled.\n")
    for grp, cs in db["caveats_by_source"].items():
        A(f"### {grp}\n")
        for x in cs:
            A(f"- {x}")
        A("")

    with open(os.path.join(OUT, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L))


if __name__ == "__main__":
    main()
