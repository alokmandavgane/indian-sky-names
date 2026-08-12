# How this database is built

`README.md` and `star-names-local.json` are **generated**. Do not edit them.

The originals are the thirteen research files in **`sources/*.json`** — ten grouped by language, plus
`tribal_fieldwork.json`, which is grouped by *method* instead — the modern village-by-village field
surveys of Adivasi astronomy, whose reliability, copyright status and unit of observation are all
different from the lexicography — `maritime_peninsular.json`, grouped by *question* (what the seafaring and the
non-farming communities do with the sky), and `occupational.json`, grouped by *register*: sky-names
keyed to a trade or a caste rather than to a language.

```
sources/*.json ─── merge.py (+ canon.py) ──→ star-names-local.json
                                         └─→ README.md
                                              │
star-names-local.json ── build_chart.py ──────┼─→ sky-chart.html
                         (+ chart_template.html)
                      ── build_matrix.py ─────┴─→ coverage-matrix.html
```

Regenerate from `sources/`, in this order:

```bash
python3 merge.py && python3 build_chart.py && python3 build_matrix.py
```

`sky-chart.html` plots each object on an equirectangular RA/Dec grid, marker area ∝ the number of
languages naming it and colour = what kind of object it is. `coverage-matrix.html` is objects ×
languages, cells coloured by the least-Sanskritic register present. Both are self-contained.

Sky positions live in `build_chart.py`, not in the database — the research records what a source
says, and where to put that on a chart is a separate judgement. Objects with no fixed position
(comets, meteors, the planets, the word for "star") carry no coordinates and appear only in the
chart's index. `build_chart.py` reads the *Sanskrit* chart's position table for any object reached
through a `sanskrit_db_id`, so the two charts cannot drift apart.

This database is **separate from `docs/star-names/`**, which holds the Sanskrit compilation. The
relationship is one-way and read-only: `merge.py` reads `../star-names/star-names.json` to resolve
`sanskrit_db_id` values into names, and never writes to it. Nothing here feeds the app.

## Why the schema looks like this

Most Indian languages inherited the 27 Sanskrit nakshatra names and adapted them phonologically. A
table of those adaptations would be large, easy to compile, and nearly uninformative. So every name
carries a **`register`**, and that field is the point of the database:

| Register | Meaning |
|---|---|
| `vernacular` | formed in the language itself, not a Sanskrit loan |
| `folk` | rural or colloquial, from a dictionary's own usage note or from ethnography |
| `tribal` | from a distinct Adivasi tradition |
| `sanskritic` | the Sanskrit name in this language's script and phonology |

Of 777 names, 565 are not `sanskritic`. Filter on this before drawing any conclusion about what a
language "has" — and note that a `sanskritic` tag is a claim about the *name*, not about the
speakers: Malayalam's birth-star reckoning is entirely Sanskritic in vocabulary and entirely alive.

## A source entry

One entry is **one name, in one language, from one source**. The same object in nine languages is
nine entries.

| Field | Meaning |
|---|---|
| `sky_object` | free text — what the name denotes. Grouped by `canon.py`, not by string equality |
| `sanskrit_db_id` | id in `../star-names/star-names.json`, or `null`. Links on **referent identity**, not on borrowing: a Santali name for Orion links to the Sanskrit entry for the same stars without implying any relation between the names. 328 of 777 are null |
| `modern_star` | `{common_name, bayer, constellation}` |
| `language`, `iso639_3`, `region` | `iso639_3` is null where no code can be assigned with confidence — better than a wrong one |
| `community` | **optional.** The caste, occupational group or ethnonym the source names, in the source's own words. Absent on 767 of 777 entries, which is itself a finding — see `occupational.json`. Not a claim that the name belongs only to that group |
| `name_native` | native script **as the source prints it**, or `null`. Never back-transliterated — many 19th-century sources romanize only, and several scans have unreadable Indic OCR |
| `name_roman`, `literal_meaning` | |
| `register` | see above |
| `usage_note` | the season it marks, the work it governs, the story attached |
| `citation`, `source_type`, `source_date`, `source_url` | author, work, edition, headword, page |
| `quote` | verbatim from the fetched source. `null` **only** where the source is in copyright |
| `confidence` | `certain` · `likely` · `disputed` · `unidentified` |

## Editorial rules

- **Every name traces to a citable printed source** with a page reference and a URL. Wikipedia was
  not used as a source, only as a lead to chase to an original.
- **Verbatim or nothing.** Quotes are re-fetched and string-matched against the live source after
  writing. Where a source is in copyright — all five modern field surveys in `tribal_fieldwork.json`,
  Lalas 2013, Samsad 2000, Candrakanta 1962 — the finding is paraphrased and `quote` is `null`.
  Copyright is a reason not to *quote* a source, never a reason not to *read* one.
- **No back-transliteration.** If the source printed only roman, `name_native` is `null`. The one
  source that prints only *script* — Mewaram's Sindhi-English dictionary, which has no romanization
  at all — is romanized by the compiler off a pointed text, and its caveat says so.
- **Don't force an identification.** 30 entries are `unidentified`, 28 more `disputed`, and one whole object group is
  *Figures with no secure modern identification*. A tribal figure described as a hunter and his dogs
  is worth more recorded honestly than pinned to a wrong Bayer designation.
- **Negative findings are recorded** in each file's `summary_findings` — no Tamil name for Sirius in
  three separate dictionaries; no Dravidian Ursa Major name in Telugu or Kannada; no Gujarati name
  transcribable from any scan reached; Radcliffe-Brown's statement that constellations are not
  recognised at all in the North Andaman. Two such negatives have since been closed and the files
  say how: Rajasthani, by reading Macalister and Lalas, and Bhili, by reading the 2023 field survey.

## Grouping

`canon.py` maps 327 distinct `sky_object` strings onto 58 objects, longest-match-first, falling back
to the entry's `sanskrit_db_id` and finally to `unplaced-figure`. Objects are ordered in the README
by **how many languages name them**, which is itself a result: the Milky Way, Ursa Major, the
Pleiades, comets and Venus-at-dawn are what these languages actually bother to name.

## Adding a source

1. Write `sources/<name>.json` on the schema above.
2. Add the filename to `FILES` in `merge.py`.
3. If it introduces an object no rule matches, add a rule to `canon.py` — or leave it to fall
   through to `unplaced-figure`, which is a legitimate outcome.
4. If it introduces a language, add it to `FAMILY` in `build_matrix.py` — an unlisted language is a
   hard assertion failure, by design.
5. `python3 merge.py && python3 build_chart.py && python3 build_matrix.py`.
