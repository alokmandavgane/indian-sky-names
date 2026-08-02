"""Build sky-chart.html for the vernacular database.

Sky positions live here, not in the database: the research records what a source
says a name means, and where to put that on a chart is a separate judgement.
Objects with no fixed position — comets, meteors, the planets, the word for
"star" — carry no coordinates and appear only in the chart's index, which is the
honest treatment rather than inventing a place for them.
"""
import json, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)

# key -> (RA, Dec, kind). J2000 degrees. Single stars take the star's own position;
# figures take a representative point inside the figure, which is all a label needs.
POS = {
    "pleiades":      (56.87, 24.11, "cluster"),
    "hyades":        (66.00, 15.90, "cluster"),
    "praesepe":      (130.10, 19.67, "cluster"),
    "castor-pollux": (114.83, 29.50, "cluster"),
    "ursa-major":    (165.50, 55.50, "figure"),
    "ursa-minor":    (240.00, 77.00, "figure"),
    "orion":         (83.00, 1.00, "figure"),
    "orions-belt":   (84.05, -1.20, "figure"),
    "scorpius":      (245.00, -26.00, "figure"),
    "pegasus":       (344.00, 20.00, "figure"),
    "auriga":        (85.00, 42.00, "figure"),
    "lupus":         (230.00, -45.00, "figure"),
    "cygnus":        (310.00, 42.00, "figure"),
    "centaurus":     (205.00, -50.00, "figure"),
    "corvus":        (183.95, -17.54, "figure"),
    "leo-virgo":     (180.00, 2.00, "figure"),
    "lyra":          (284.00, 37.00, "figure"),
    "aquila":        (297.00, 5.00, "figure"),
    "norma":         (245.00, -50.00, "figure"),
    "pole-star":     (37.95, 89.26, "star"),
    "alcor":         (200.98, 54.99, "star"),
    "canopus":       (95.99, -52.70, "star"),
    "sirius":        (101.29, -16.72, "star"),
    "aldebaran":     (68.98, 16.51, "star"),
    "betelgeuse":    (88.79, 7.41, "star"),
    "arcturus":      (213.92, 19.18, "star"),
    "antares":       (247.35, -26.43, "star"),
    "spica":         (201.30, -11.16, "star"),
    "vega":          (279.23, 38.78, "star"),
    "capella":       (79.17, 45.99, "star"),
    "altair":        (297.70, 8.87, "star"),
    "regulus":       (152.09, 11.97, "star"),
    "milky-way":     (None, None, "diffuse"),   # drawn as the galactic band
}
# Individual nakshatras reached through a sanskrit_db_id take their position from
# the Sanskrit chart's own table, so the two charts cannot drift apart.
NAK_FROM_SANSKRIT = True


def sanskrit_positions():
    import re
    src = open(os.path.join(OUT, "..", "star-names", "sources", "build_chart.py"), encoding="utf-8").read()
    P = {}
    for m in re.finditer(r'"([a-z0-9\-]+)"\s*:\s*\(\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)\s*,', src):
        P.setdefault(m.group(1), (float(m.group(2)), float(m.group(3))))
    return P


def main():
    with open(os.path.join(OUT, "star-names-local.json"), encoding="utf-8") as f:
        db = json.load(f)
    SP = sanskrit_positions()

    objects, placed, indexed = [], 0, 0
    for o in db["objects"]:
        key = o["key"]
        ra = dec = None
        kind = "figure"
        if key in POS:
            ra, dec, kind = POS[key]
        elif key.startswith("nak-") and NAK_FROM_SANSKRIT:
            sid = key[4:]
            if sid in SP:
                ra, dec = SP[sid]
                kind = "star"
        if ra is not None:
            placed += 1
        elif key != "milky-way":
            indexed += 1
        names = [{
            "language": n["language"], "region": n.get("region"),
            "name_native": n.get("name_native"), "name_roman": n["name_roman"],
            "literal_meaning": n.get("literal_meaning"), "register": n["register"],
            "confidence": n["confidence"], "usage_note": n.get("usage_note"),
            "quote": n.get("quote"), "citation": n["citation"],
            "source_url": n.get("source_url"), "notes": n.get("notes"),
        } for n in o["names"]]
        objects.append({
            "key": key, "title": o["title"], "kind": kind, "ra": ra, "dec": dec,
            "modern_star": o.get("modern_star"), "sanskrit_db_id": o.get("sanskrit_db_id"),
            "names": names,
        })

    c = db["counts"]
    about = (
        f"<p><b>{c['entries']} names for {c['objects']} sky objects, in {c['languages']} languages.</b> "
        "What speakers of the Indian languages call a star, an asterism or a constellation — each name "
        "quoted from the dictionary or ethnography it comes from, with the page cited.</p>"
        "<p><b>Marker area is the number of languages</b> that name the object, recomputed as you filter. "
        "Colour is what kind of thing it is, which does not change when you filter. The Milky Way is drawn "
        "as the galactic band rather than a point, because that is where it actually is.</p>"
        "<p><b>Register is the point of the database.</b> Most Indian languages took the 27 Sanskrit "
        "nakshatra names and adapted them; a table of those adaptations would be large and nearly "
        "uninformative. The tags separate that borrowed layer from names each language built itself — "
        f"{sum(v for k, v in c['by_register'].items() if k != 'sanskritic')} of {c['entries']} names are "
        "not Sanskritic. Filter to <i>tribal</i> alone to see a sky organised on entirely different "
        "principles.</p>"
        "<p><b>Sources</b> are public-domain lexicography and ethnography, chiefly the Digital Dictionaries "
        "of South Asia and archive.org — Molesworth 1857, Platts 1884, Kittel, Brown 1852, Gundert 1872, "
        "the Madras Tamil Lexicon, Praharaj, Maffei 1883, Hoffmann's Encyclopaedia Mundarica, Bodding, "
        "Rivers 1906 on the Toda, Man 1883 on the Andamans. Every quotation was re-fetched and matched "
        "against its source. Where a source is still in copyright the finding is paraphrased and no "
        "quotation is shown.</p>"
        "<p><b>Nothing was back-transliterated.</b> Where a source printed only a romanization, no script "
        "is given — much 19th-century Indic type survives in these scans only as unreadable OCR, and "
        "several entries were read off page images instead.</p>"
        "<p>Full database, with every caveat and the negative findings: <code>docs/star-names-local/</code> "
        "in the repository. The separate Sanskrit-text database is <code>docs/star-names/</code>.</p>"
    )

    data = {
        "objects": objects,
        "languages": list(db["counts"]["by_language"].items()),
        "about": about,
    }
    tpl = open(os.path.join(HERE, "chart_template.html"), encoding="utf-8").read()
    out = tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False))
    open(os.path.join(OUT, "sky-chart.html"), "w", encoding="utf-8").write(out)

    # Nothing may fall off the chart silently: every object is a point, the
    # galactic band, or explicitly index-only.
    stray = [o["key"] for o in objects
             if o["ra"] is None and o["key"] != "milky-way" and o["key"] in POS]
    assert not stray, f"positioned objects with no coordinates: {stray}"
    print(f"objects={len(objects)} plotted={placed} band=1 index-only={indexed} "
          f"names={sum(len(o['names']) for o in objects)}")


if __name__ == "__main__":
    main()
