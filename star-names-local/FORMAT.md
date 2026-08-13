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
languages, cells coloured by the least-borrowed register present. Both are self-contained.

Sky positions live in `build_chart.py`, not in the database — the research records what a source
says, and where to put that on a chart is a separate judgement. Objects with no fixed position
(comets, meteors, the planets, the word for "star") carry no coordinates and appear only in the
chart's index. `build_chart.py` reads the *Sanskrit* chart's position table for any object reached
through a `sanskrit_db_id`, so the two charts cannot drift apart.

**Scope is South Asian, not Indian.** The app is *Indian Sky Map*; this database is deliberately
wider, and every language that reaches past the border is here to speak for a community inside it
that has no lexicography of its own — Tibetan for Ladakh, Spiti and Sikkim; Mara and Mizo from
sources as much about the Chin Hills as about Mizoram; Divehi through Minicoy, which speaks it;
Nepali and Newar for the Indian Himalaya; Sinhala for the Dravidian south. The research is worth
more undivided, and the rule for anything that consumes it is that **the consumer filters, not the
database**.

This database is **separate from `docs/star-names/`**, which holds the Sanskrit compilation. The
relationship is one-way and read-only: `merge.py` reads `../star-names/star-names.json` to resolve
`sanskrit_db_id` values into names, and never writes to it.

**Three things now consume this database**, where once nothing did:

| Consumer | Reads | Via |
|---|---|---|
| the app | `star-names-local.json` → `catalogs/localnames.pb` | `tools/` `LocalNamesGenerator` |
| the atlas at `sky.alokm.com` | `star-names-local.json` | `docs/site/build_site.py` |
| `docs/sky-identity` | the chart's position tables | `resolve.py`, `cultures.py` |

None of them writes back, and the scope rule above binds all three.

## Why the schema looks like this

Most Indian languages inherited the 27 Sanskrit nakshatra names and adapted them phonologically. A
table of those adaptations would be large, easy to compile, and nearly uninformative. So every name
carries a **`register`**, and that field is the point of the database:

| Register | Meaning |
|---|---|
| `vernacular` | formed in the language itself, not a loan from the prestige tradition |
| `folk` | rural or colloquial, from a dictionary's own usage note or from ethnography |
| `tribal` | from a distinct Adivasi tradition |
| `borrowed` | the prestige tradition's name in this language's script and phonology |

A `borrowed` name also carries **`borrowed_from`**, naming the tradition it came from. Every one of
the 221 says `sanskrit`, and the field exists precisely so that the register need not: the question
*did this language form this name or take it* is the same question outside South Asia, and only the
answer's source changes. `register` was `sanskritic` until 2026-08-13, which made the whole
vocabulary Sanskrit-relative — `vernacular` was defined as "not a Sanskrit loan" — and could not
have described a Vietnamese name formed against literary Chinese. `merge.py` asserts the pair:
`borrowed_from` is present if and only if the register is `borrowed`, and its value must be a known
tradition.

Of 975 names, 754 are not `borrowed`. Filter on this before drawing any conclusion about what a
language "has" — and note that a `borrowed` tag is a claim about the *name*, not about the
speakers: Malayalam's birth-star reckoning is entirely Sanskritic in vocabulary and entirely alive.

## A source entry

One entry is **one name, in one language, from one source**. The same object in nine languages is
nine entries.

| Field | Meaning |
|---|---|
| `sky_object` | free text — what the name denotes. Grouped by `canon.py`, not by string equality |
| `sanskrit_db_id` | id in `../star-names/star-names.json`, or `null`. Links on **referent identity**, not on borrowing: a Santali name for Orion links to the Sanskrit entry for the same stars without implying any relation between the names. 444 of 975 are null |
| `modern_star` | `{common_name, bayer, constellation}` |
| `language`, `iso639_3`, `region` | `iso639_3` is null where no code can be assigned with confidence — better than a wrong one |
| `community` | **optional.** The caste, occupational group or ethnonym the source names, in the source's own words. Absent on 916 of 975 entries, which is itself a finding — see `occupational.json`. Not a claim that the name belongs only to that group |
| `name_native` | native script **as the source prints it**, or `null`. Never back-transliterated — many 19th-century sources romanize only, and several scans have unreadable Indic OCR |
| `name_roman`, `literal_meaning` | `name_roman` is null on 4 entries, where the source records the figure and never gives the word — Elwin's Baiga Great Bear, Mills's Rengma eclipse. They read as *(figure recorded, name not)* in the README and the matrix |
| `register` | see above |
| `borrowed_from` | the tradition a `borrowed` name came from — `sanskrit` on all 221. Present if and only if `register` is `borrowed`, which `merge.py` asserts |
| `usage_note` | the season it marks, the work it governs, the story attached |
| `citation`, `source_type`, `source_date`, `source_url` | author, work, edition, headword, page |
| `quote` | verbatim from the fetched source. `null` **only** where the source is in copyright |
| `source_access` | `public-domain` · `in-copyright-paraphrased` · `not-obtained`. 693 and 282; the third value is empty and must stay empty — see below |
| `confidence` | `certain` · `likely` · `disputed` · `unidentified` |

## Editorial rules

- **Every name traces to a citable printed source** with a page reference and a URL. Wikipedia was
  not used as a source, only as a lead to chase to an original.
- **Verbatim or nothing.** Quotes are re-fetched and string-matched against the live source after
  writing. Where a source is in copyright — the six field surveys, Turner 1931, Jørgensen, Malla,
  Manandhar, Maniku 2000, Sharma 2006, Baloch, Grignard, Lalas 2013, Samsad 2000, Candrakanta 1962 —
  the finding is paraphrased and `quote` is `null`, which `source_access` now states rather than
  implies. Copyright is a reason not to *quote* a source, never a reason not to *read* one.
- **OCR damage is bracketed, never mended silently.** Where an archive.org scan has broken an
  *English* word inside a quote and the printed reading is not in doubt, the restoration is marked
  `[like this]`. No vernacular name is ever restored: where two scans of one printing disagree on a
  name, both readings are recorded and neither is preferred.
- **No back-transliteration.** If the source printed only roman, `name_native` is `null`. The one
  source that prints only *script* — Mewaram's Sindhi-English dictionary, which has no romanization
  at all — is romanized by the compiler off a pointed text, and its caveat says so.
- **Don't force an identification.** 51 entries are `unidentified`, 43 more `disputed`, and one whole object group is
  *Figures with no secure modern identification*. A tribal figure described as a hunter and his dogs
  is worth more recorded honestly than pinned to a wrong Bayer designation.
- **`source_access` is an invariant, not a label.** `merge.py` asserts that a `quote` exists if and
  only if `source_access` is `public-domain`, so the convention above cannot drift. The third value,
  `not-obtained`, exists to be *unused*: nothing is entered from a source that was not read, so a
  `not-obtained` entry would be a bug. Sources that could not be obtained are recorded in
  `summary_findings` and `caveats`, where they belong, and never as a row with an empty quote.
- **Negative findings are recorded** in each file's `summary_findings` — no Tamil name for Sirius in
  three separate dictionaries; no Dravidian Ursa Major name in Telugu or Kannada; no Gujarati name
  transcribable from any scan reached; Radcliffe-Brown's statement that constellations are not
  recognised at all in the North Andaman. Two such negatives have since been closed and the files
  say how: Rajasthani, by reading Macalister and Lalas, and Bhili, by reading the 2023 field survey.

## Grouping

`canon.py` maps 411 distinct `sky_object` strings onto 65 objects, longest-match-first, falling back
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
