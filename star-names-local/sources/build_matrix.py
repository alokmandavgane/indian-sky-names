"""Build coverage-matrix.html — which languages have a term for which sky object.

A presence matrix, objects x languages. Cells are coloured by the LEAST Sanskritic
register present, so the eye picks up where a language built its own word rather
than taking the Sanskrit one. Languages are grouped by family, because the
cross-family repetitions (the cot, the plough, the road) are the point.
"""
import json, os, html, collections

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)

FAMILY = {
    "Indo-Aryan": ["Hindi", "Urdu", "Punjabi", "Rajasthani", "Sindhi", "Kashmiri",
                   "Chhattisgarhi", "Marathi",
                   "Konkani", "Gujarati", "Bengali", "Assamese", "Odia", "Sinhala",
                   "Lambadi (Banjara)", "Bhili", "Mavchi", "Vasavi (Vasave Bhil)",
                   "Pauri Bareli (Pawra)", "Kukna (Kokna)", "Nepali", "Kumaoni", "Divehi (Mahl)",
                   "Pardhi"],
    "Dravidian": ["Tamil", "Telugu", "Kannada", "Malayalam", "Tulu", "Kodava",
                  "Gondi", "Kolami", "Kurukh", "Toda", "Cholanaikkan", "Kui"],
    "Munda": ["Santali", "Mundari", "Ho", "Korku", "Sora"],
    "Austroasiatic": ["Khasi", "Nicobarese", "Central Nicobarese (Camorta)",
                      "Chaura (Chowra)", "Teressa"],
    "Tibeto-Burman": ["Mizo (Lushai)", "Mara (Lakher)", "Meitei (Manipuri)",
                      "Newar (Nepal Bhasa)", "Garo", "Angami Naga", "Sema (Sumi) Naga",
                      "Rengma Naga", "Ao Naga", "Tibetan"],
    "Andamanese": ["Andamanese"],
}
# Least-Sanskritic wins the cell; a language that has both a loan and its own word
# is more interesting for the word it made itself.
PRIORITY = ["tribal", "folk", "vernacular", "sanskritic"]
REG_HEX = {"tribal": "#d55181", "folk": "#c98500", "vernacular": "#3987e5", "sanskritic": "#008300"}
REG_LABEL = {
    "tribal": "a distinct Adivasi tradition",
    "folk": "rural or colloquial usage",
    "vernacular": "formed in the language itself",
    "sanskritic": "the Sanskrit name, adapted",
}


def local_name(o):
    """The Indian name for a row, and whose word it is.

    Same rule as the sky chart, minus the language filter this table does not
    have: the pan-Indian form the object carries in the Sanskrit database if it
    has one, else the first name in the database's own order — which puts the
    least Sanskritic first. Returns (name, language-or-None); the language is
    given only when the name is one language's rather than the shared form, so
    that nobody's word is passed off as everyone's.
    """
    sk = (o.get("sanskrit_name") or "").split(" (")[0].strip()
    if sk:
        return sk, None
    n = o["names"][0] if o["names"] else None
    if not n:
        return "", None
    return (n.get("name_native") or n["name_roman"]), n["language"]


def main():
    with open(os.path.join(OUT, "star-names-local.json"), encoding="utf-8") as f:
        db = json.load(f)

    langs = [l for fam in FAMILY.values() for l in fam]
    seen = {n["language"] for o in db["objects"] for n in o["names"]}
    assert not (seen - set(langs)), f"language missing from FAMILY: {seen - set(langs)}"

    # cell[(object_key, language)] = (register, [names])
    cell = {}
    for o in db["objects"]:
        for n in o["names"]:
            k = (o["key"], n["language"])
            cur = cell.get(k)
            reg = n["register"]
            if cur is None or PRIORITY.index(reg) < PRIORITY.index(cur[0]):
                cell[k] = (reg, cur[1] + [n] if cur else [n])
            else:
                cur[1].append(n)

    objects = sorted(db["objects"], key=lambda o: (-len(o["languages"]), o["title"]))
    filled = len(cell)
    total = len(objects) * len(langs)

    css = """
    :root{color-scheme:dark;--bg:#0a0f1e;--panel:#121a30;--ink:#e9eef8;--ink-2:#9aa6c0;
      --ink-3:#5d6a88;--line:#232f4d;--grid:#161f38;
      --serif:"Iowan Old Style",Palatino,Georgia,serif;
      --indic:"Noto Sans Devanagari","Noto Sans Tamil","Noto Sans Telugu","Noto Sans Kannada",
        "Noto Sans Malayalam","Noto Sans Bengali","Noto Sans Gujarati","Noto Sans Oriya",
        "Noto Sans Gurmukhi","Noto Sans Sinhala","Noto Nastaliq Urdu",-apple-system,sans-serif;
      --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif}
    *{box-sizing:border-box;margin:0}
    body{background:var(--bg);color:var(--ink);font-family:var(--sans);padding:22px 20px 60px}
    h1{font-family:var(--serif);font-size:22px;font-weight:600}
    .sub{color:var(--ink-2);font-size:13px;margin-top:6px;max-width:74ch;line-height:1.6}
    .legend{display:flex;flex-wrap:wrap;gap:14px;margin:16px 0 6px;align-items:center}
    .lg{display:inline-flex;align-items:center;gap:7px;font-size:12px;color:var(--ink-2)}
    .lg i{width:12px;height:12px;border-radius:3px;display:inline-block}
    .note{font-size:11.5px;color:var(--ink-3);margin-top:4px}
    .wrap{overflow:auto;margin-top:18px;border:1px solid var(--line);border-radius:10px;max-height:78vh}
    table{border-collapse:separate;border-spacing:0;font-size:12px}
    th,td{padding:0;white-space:nowrap}
    thead th{position:sticky;top:0;z-index:3;background:var(--panel);border-bottom:1px solid var(--line)}
    thead th.fam{font-size:10.5px;letter-spacing:.07em;text-transform:uppercase;color:var(--ink-3);
      padding:7px 8px;text-align:left;border-left:1px solid var(--line)}
    thead tr.langs th{height:118px;vertical-align:bottom;padding:0 0 7px}
    thead tr.langs th div{writing-mode:vertical-rl;transform:rotate(180deg);
      font-weight:500;color:var(--ink-2);font-size:11.5px;padding-left:3px}
    th.obj{position:sticky;left:0;z-index:2;background:var(--panel);text-align:left;
      font-weight:400;color:var(--ink);padding:0 12px 0 10px;border-right:1px solid var(--line);
      max-width:270px;overflow:hidden;text-overflow:ellipsis}
    th.obj .loc{font-family:var(--indic);color:var(--ink)}
    th.obj .eng{color:var(--ink-3)}
    tbody tr:hover th.obj .eng{color:var(--ink-2)}
    thead th.corner{left:0;z-index:4}
    td.c{width:19px;height:19px;border-right:1px solid var(--grid);border-bottom:1px solid var(--grid)}
    td.c.on{cursor:pointer}
    td.c.on:hover{outline:2px solid var(--ink);outline-offset:-2px}
    td.famgap,th.famgap{border-left:1px solid var(--line)}
    tbody tr:hover th.obj{color:#fff;background:#18213c}
    td.n{color:var(--ink-3);font-variant-numeric:tabular-nums;padding:0 8px;text-align:right}
    tfoot td{position:sticky;bottom:0;background:var(--panel);border-top:1px solid var(--line);
      color:var(--ink-3);font-size:11px;font-variant-numeric:tabular-nums;text-align:center;padding:5px 0}
    #tip{position:fixed;z-index:20;pointer-events:none;opacity:0;transition:opacity 90ms;
      background:rgba(16,23,43,.96);border:1px solid var(--line);border-radius:8px;padding:9px 12px;
      max-width:330px;box-shadow:0 8px 28px rgba(0,0,0,.55)}
    #tip.show{opacity:1}
    #tip .h{font-family:var(--serif);font-size:13.5px}
    #tip .l{font-size:11px;color:var(--ink-3);letter-spacing:.05em;text-transform:uppercase;margin-top:2px}
    #tip .nm{margin-top:7px;font-size:13px;line-height:1.5}
    #tip .nm b{font-weight:600}
    #tip .nm span{color:var(--ink-2);font-style:italic}
    """

    rows = []
    for o in objects:
        tds = []
        for fam, fl in FAMILY.items():
            for i, lg in enumerate(fl):
                got = cell.get((o["key"], lg))
                cls = "c" + (" on" if got else "") + (" famgap" if i == 0 else "")
                if got:
                    reg, names = got
                    bits = []
                    for n in names[:4]:
                        # A few entries record a figure whose name the source never gives —
                        # Elwin's Baiga Great Bear, Mills's Rengma eclipse. They are real
                        # findings and belong in the matrix, labelled for what they are.
                        nm = n["name_native"] or n["name_roman"] or "(figure recorded, name not)"
                        lit = f" <span>‘{html.escape(n['literal_meaning'])}’</span>" if n.get("literal_meaning") else ""
                        bits.append(f"<b>{html.escape(nm)}</b>{lit}")
                    if len(names) > 4:
                        bits.append(f"<span>+{len(names)-4} more</span>")
                    payload = html.escape("<br>".join(bits), quote=True)
                    tds.append(f'<td class="{cls}" style="background:{REG_HEX[reg]}" '
                               f'data-o="{html.escape(o["title"], quote=True)}" data-l="{lg}" '
                               f'data-r="{reg}" data-n="{payload}"></td>')
                else:
                    tds.append(f'<td class="{cls}"></td>')
        loc, loc_lang = local_name(o)
        # Inline here, not stacked as on the chart: the constraint in a matrix is
        # row height, and these rows are 19px. Width is what there is plenty of.
        if loc and not o["title"].lower().startswith(loc.lower()):
            head = (f'<span class="loc">{html.escape(loc)}</span>'
                    f'<span class="eng"> · {html.escape(o["title"])}</span>')
            tt = f'{loc} · {o["title"]}' + (f' — {loc_lang}' if loc_lang else "")
        else:
            head = f'<span class="loc">{html.escape(o["title"])}</span>'
            tt = o["title"]
        rows.append(f'<tr><th class="obj" title="{html.escape(tt, quote=True)}">'
                    f'{head}</th>{"".join(tds)}'
                    f'<td class="n">{len(o["languages"])}</td></tr>')

    fam_hdr, lang_hdr, foot = [], [], []
    for fam, fl in FAMILY.items():
        fam_hdr.append(f'<th class="fam" colspan="{len(fl)}">{fam}</th>')
        for i, lg in enumerate(fl):
            lang_hdr.append(f'<th class="{"famgap" if i==0 else ""}"><div>{lg}</div></th>')
            n = sum(1 for (ok, l) in cell if l == lg)
            foot.append(f'<td>{n}</td>')

    doc = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Which languages name which stars</title>
<style>{css}</style>
<h1>Which languages name which stars</h1>
<div class="sub">Every sky object in the database against every language that has a word for it —
{filled} filled cells of {total}. The gaps carry as much as the marks: a blank is a language for which
no citable source gives a name, not a language that has none. Objects are ordered by how many
languages name them; languages are grouped by family, because the repetitions across families
— the cot, the plough, the road — are what the database is for.</div>
<div class="legend">
  {"".join(f'<span class="lg"><i style="background:{REG_HEX[r]}"></i>{r} — {REG_LABEL[r]}</span>' for r in PRIORITY)}
</div>
<div class="note">Where a language has more than one name for an object, the cell takes the least
Sanskritic — a language that has both a loan and a word of its own is more interesting for the one it made.
Hover any cell for the names.
Each row is labelled with the Indian name first and the English one after it. That name is the
pan-Indian form the object carries in the Sanskrit database where it has one; where it has none —
comets, both appearances of Venus, and the unplaced figures — the label falls back to the first name
in the database\'s own order, which is one language\'s word and not everyone\'s. Hover the row label
and it tells you whose.</div>
<div class="wrap">
<table>
<thead>
  <tr><th class="obj corner"></th>{"".join(fam_hdr)}<th></th></tr>
  <tr class="langs"><th class="obj corner"></th>{"".join(lang_hdr)}<th></th></tr>
</thead>
<tbody>{"".join(rows)}</tbody>
<tfoot><tr><td></td>{"".join(foot)}<td></td></tr></tfoot>
</table>
</div>
<div id="tip"></div>
<script>
const tip = document.getElementById('tip');
document.querySelectorAll('td.c.on').forEach(td => {{
  td.addEventListener('mouseenter', e => {{
    tip.innerHTML = '<div class="h">' + td.dataset.o + '</div>' +
      '<div class="l">' + td.dataset.l + ' · ' + td.dataset.r + '</div>' +
      '<div class="nm">' + td.dataset.n + '</div>';
    tip.classList.add('show');
  }});
  td.addEventListener('mousemove', e => {{
    const r = tip.getBoundingClientRect();
    tip.style.left = Math.min(e.clientX + 14, innerWidth - r.width - 12) + 'px';
    tip.style.top = Math.min(e.clientY + 14, innerHeight - r.height - 12) + 'px';
  }});
  td.addEventListener('mouseleave', () => tip.classList.remove('show'));
}});
</script>
"""
    with open(os.path.join(OUT, "coverage-matrix.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"matrix: {len(objects)} objects x {len(langs)} languages, {filled}/{total} cells filled "
          f"({100*filled/total:.0f}%)")
    by_fam = collections.Counter()
    for (ok, lg), (reg, _) in cell.items():
        for fam, fl in FAMILY.items():
            if lg in fl:
                by_fam[(fam, reg)] += 1
    return by_fam


if __name__ == "__main__":
    main()
