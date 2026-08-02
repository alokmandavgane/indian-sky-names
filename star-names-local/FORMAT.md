# How this database is built

`README.md` and `star-names-local.json` are **generated**. Do not edit them.

The originals are the seven per-language-group research files in **`sources/*.json`**.

```
sources/*.json ─── merge.py (+ canon.py) ──→ star-names-local.json
                                         └─→ README.md
```

Regenerate from `sources/`:

```bash
python3 merge.py
```

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

Of 522 names, 369 are not `sanskritic`. Filter on this before drawing any conclusion about what a
language "has" — and note that a `sanskritic` tag is a claim about the *name*, not about the
speakers: Malayalam's birth-star reckoning is entirely Sanskritic in vocabulary and entirely alive.

## A source entry

One entry is **one name, in one language, from one source**. The same object in nine languages is
nine entries.

| Field | Meaning |
|---|---|
| `sky_object` | free text — what the name denotes. Grouped by `canon.py`, not by string equality |
| `sanskrit_db_id` | id in `../star-names/star-names.json`, or `null`. Links on **referent identity**, not on borrowing: a Santali name for Orion links to the Sanskrit entry for the same stars without implying any relation between the names. 181 of 522 are null |
| `modern_star` | `{common_name, bayer, constellation}` |
| `language`, `iso639_3`, `region` | |
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
  writing. Where a source is in copyright — the 2013 and 2023 JAHH papers on Gondi and Bhil
  astronomy, Samsad 2000, Candrakanta 1962 — the finding is paraphrased and `quote` is `null`.
- **No back-transliteration.** If the source printed only roman, `name_native` is `null`.
- **Don't force an identification.** 12 entries are `unidentified` and one whole object group is
  *Figures with no secure modern identification*. A tribal figure described as a hunter and his dogs
  is worth more recorded honestly than pinned to a wrong Bayer designation.
- **Negative findings are recorded** in each file's `summary_findings` — no Bhili star name in any
  public-domain source; no Rajasthani; no Tamil name for Sirius; no Dravidian Ursa Major name in
  Telugu or Kannada; Radcliffe-Brown's statement that constellations are not recognised at all in
  the North Andaman.

## Grouping

`canon.py` maps 246 distinct `sky_object` strings onto 45 objects, longest-match-first, falling back
to the entry's `sanskrit_db_id` and finally to `unplaced-figure`. Objects are ordered in the README
by **how many languages name them**, which is itself a result: the Milky Way, Ursa Major, the
Pleiades, comets and Venus-at-dawn are what these languages actually bother to name.

## Adding a source

1. Write `sources/<name>.json` on the schema above.
2. Add the filename to `FILES` in `merge.py`.
3. If it introduces an object no rule matches, add a rule to `canon.py` — or leave it to fall
   through to `unplaced-figure`, which is a legitimate outcome.
4. `python3 merge.py`.
