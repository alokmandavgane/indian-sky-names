"""Merge the nine research files into the vernacular database.

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

FILES = ["hindi_urdu_punjabi", "northwest", "marathi_gujarati", "bengali_assamese_odia",
         "tamil", "telugu_kannada", "malayalam_tulu_sinhala", "northeast", "himalaya", "maritime_peninsular", "occupational", "tribal",
         "tribal_fieldwork"]

REGISTER_ORDER = ["vernacular", "folk", "tribal", "borrowed"]
REGISTER_BLURB = {
    "vernacular": "formed in the language itself, not a loan from the prestige tradition",
    "folk": "rural or colloquial usage, from a dictionary's own usage note or from ethnography",
    "tribal": "from a distinct Adivasi tradition",
    "borrowed": "the prestige tradition's name in this language's script and phonology — "
                "in every entry here, Sanskrit's",
}
# Which tradition a `borrowed` name was borrowed from. One value so far, and the
# field exists because the register must not name it: `sanskritic` described the
# only prestige tradition this database has met, and a database of the world's sky
# cultures meets others. `register` says whether a language formed a name or took
# it; `borrowed_from` says where from. Splitting those two questions is what lets
# the same four registers describe a Vietnamese name against literary Chinese.
TRADITIONS = ["sanskrit"]
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


ACCESS = ("public-domain", "in-copyright-paraphrased")


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
            # `source_access` is an invariant, not a comment: a quote may exist only
            # where the source is out of copyright, and `not-obtained` may never
            # reach an entry at all, because nothing is entered from a source that
            # was not read.
            acc = e.get("source_access")
            assert acc in ACCESS, f"{name}: bad source_access {acc!r} on {e.get('name_roman')!r}"
            assert (acc == "public-domain") == (e.get("quote") is not None), (
                f"{name}: source_access {acc!r} contradicts quote on {e.get('name_roman')!r}")
            # `borrowed_from` is the same kind of invariant: a name says where it was
            # borrowed from if and only if it says it was borrowed. Asserted rather
            # than trusted, so the pair cannot drift apart the way a convention would.
            reg, bf = e.get("register"), e.get("borrowed_from")
            assert reg in REGISTER_ORDER, f"{name}: bad register {reg!r} on {e.get('name_roman')!r}"
            assert (reg == "borrowed") == (bf is not None), (
                f"{name}: register {reg!r} contradicts borrowed_from {bf!r} "
                f"on {e.get('name_roman')!r}")
            assert bf is None or bf in TRADITIONS, (
                f"{name}: unknown tradition {bf!r} on {e.get('name_roman')!r}")
            e = dict(e, _source_group=src["source_group"])
            groups[canon(e, sk_titles)].append(e)

    objects = []
    for key, entries in groups.items():
        entries.sort(key=lambda e: (REGISTER_ORDER.index(e["register"]) if e["register"] in REGISTER_ORDER else 9,
                                    e["language"], e["name_roman"] or ""))
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
    trads = collections.Counter(e["borrowed_from"] for e in all_entries
                                if e.get("borrowed_from"))

    db = {
        "title": "Star names in the languages of India",
        "generated": "2026-08-12",
        "method": (
            "Compiled from public-domain lexicography and ethnography, chiefly the Digital Dictionaries of "
            "South Asia (dsal.uchicago.edu) and archive.org: Platts 1884, Fallon 1879 and Shakespear 1834 for "
            "Hindi/Urdu; Molesworth 1857 for Marathi; Maffei 1883 and Dalgado 1893 for Konkani; the Madras "
            "Tamil Lexicon 1924-39 and Winslow 1862 for Tamil; Brown 1852/1903 for Telugu; Kittel for Kannada; "
            "Gundert 1872 for Malayalam; Männer 1886 for Tulu; Carter and Clough for Sinhala; Praharaj and "
            "Jñānendramohana Dāsa for Odia and Bengali; and for the Adivasi languages Hoffmann's Encyclopaedia "
            "Mundarica, Bodding and Campbell on Santali, Grignard on Kurukh, Rivers 1906 on the Toda, Man 1883 "
            "and Radcliffe-Brown 1922 on the Andamans, Ramamurti 1938 on Sora and Winfield 1929 on Kui; "
            "for the north-east, Lorrain 1940 on Mizo and the colonial monographs — Playfair 1909 on the "
            "Garos, Hutton 1921 on the Angamis and the Semas, Mills 1926 and 1937 on the Aos and the "
            "Rengmas, Parry 1932 on the Lakhers; Elwin 1939 on the Baiga, and Russell & Hiralal 1916; Macalister 1898 and Lalas "
            "2013 for Rajasthani. A second layer, kept in its own source file, comes from MODERN FIELD SURVEYS "
            "that have no counterpart in the printed record: Vahia, Halkare and colleagues on the Gonds (2013), "
            "the Banjaras and Kolams (2014), the Korku (2016) and the Nicobarese (2018), and Shetye, Halkare "
            "and Sule on the Bhil, Pawra and Kokna (2023). Every name from a public-domain source is quoted "
            "verbatim from a source that was actually fetched, with the page cited and the URL recorded; where "
            "a source printed only a romanization, no script is supplied and nothing was back-transliterated. "
            "Work still in copyright — the six field surveys, Turner 1931, Jorgensen, Malla, Manandhar, "
            "Maniku 2000, Sharma 2006, Baloch, Grignard, Samsad 2000, Candrakanta 1962 and Lalas 2013 — is "
            "paraphrased and cited, never quoted, and every entry now says which it is in `source_access`. Wikipedia was not used as a source."
        ),
        "register_note": (
            "Every name is tagged by register. That is the point of the database rather than a detail: most "
            "Indian languages inherited the 27 Sanskrit nakshatra names and adapted them phonologically, and a "
            "table of those adaptations would be large and nearly uninformative. The tags separate that borrowed "
            "layer from names the languages made themselves. " +
            "; ".join(f"**{r}** — {REGISTER_BLURB[r]}" for r in REGISTER_ORDER) + ". "
            "A `borrowed` name also carries `borrowed_from`, naming the tradition it came from. "
            "Every one of them here says `sanskrit`; the field exists so that the register need "
            "not, because the question *did this language form this name or take it* is the same "
            "question outside South Asia, and only the answer's source changes."
        ),
        "counts": {
            "entries": len(all_entries),
            "objects": len(objects),
            "languages": len(langs),
            "by_register": dict(regs),
            "by_tradition": dict(trads),
            "by_language": dict(langs.most_common()),
            "linked_to_sanskrit_db": sum(1 for e in all_entries if e["sanskrit_db_id"]),
            "by_source_access": dict(collections.Counter(e["source_access"] for e in all_entries)),
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
      "research files: [`sources/`](sources/).*\n")
    A("> **This file is generated — do not edit it.** The originals are the research files in "
      "[`sources/`](sources/). See [`FORMAT.md`](FORMAT.md) for the schema and the editorial rules.\n")
    c = db["counts"]
    A(f"**{c['entries']} names** across **{c['languages']} languages** for **{c['objects']} sky objects**. "
      f"{c['linked_to_sanskrit_db']} link to an entry in the separate Sanskrit database at "
      f"[`../star-names/`](../star-names/); the rest have no Sanskrit counterpart, which is the interesting part.\n")
    A("**Register.** " + db["register_note"] + "\n")
    reg = c["by_register"]
    non = sum(v for k, v in reg.items() if k != "borrowed")
    A(f"Of {c['entries']} names, **{non} are not borrowed** — "
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
            rom = e["name_roman"] or "(figure recorded, name not)"
            lit = (e["literal_meaning"] or "—").replace("|", "\\|")
            A(f"| {e['language']} | {nat} | *{rom}* | {lit} | {e['register']} |")
        A("")
        for e in o["names"]:
            head = f"**{e['name_native'] + ' · ' if e['name_native'] else ''}"
            head += f"{e['name_roman'] or '(figure recorded, name not)'}** "
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
