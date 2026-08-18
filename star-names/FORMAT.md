# How this database is built

`README.md`, `star-names.json` and `sky-chart.html` in this directory are **generated**. Do not
edit them; the next regeneration overwrites them.

The originals are the per-text research files in **`sources/*.json`** — one per source text,
hand-authored, 15 of them. They are the only irreplaceable thing here.

```
sources/*.json ─── merge.py ──→ star-names.json     (merged, machine-readable)
                            └─→ README.md           (human-readable, per-entry)
                                    │
star-names.json ── build_chart.py ──┴─→ sky-chart.html
   │              (+ chart_template.html)
   │
   └── tools/build.gradle.kts reads it straight from docs/ ──→ catalogs/starinfo.pb
```

Regenerate, from this directory:

```bash
cd sources && python3 merge.py && python3 build_chart.py
```

Then, if the app should pick up the change, from the repo root:

```bash
./gradlew :tools:generateCatalogs
```

`catalogs/starinfo.pb` is committed, so it goes stale silently if you skip that step. There is no
copy of `star-names.json` under `tools/` — `processResources` puts this file on the generator's
classpath from where it sits, and `StarInfoGenerator` navigates it as a JSON tree rather than
mapping it to DTOs, so adding fields here will not break the build.

## A source file

```jsonc
{
  "source_text": "Utpala's commentary",   // short label; also add it to SOURCES in merge.py
  "summary_findings": "…",                // one dense paragraph, incl. what was NOT found
  "entries": [ … ],
  "caveats": ["…"]                        // limits of this research pass
}
```

Each entry is **one attestation** — one name in one passage. The same name in three texts is three
entries in three files sharing a `db_id`; `merge.py` folds them into a single database entry with
three references.

| Field | Meaning |
|---|---|
| `db_id` | kebab-case join key. **Reuse an existing id** to attach to a known name; a new id creates a new entry and must be placed in a category list in `merge.py`. |
| `name_devanagari`, `name_iast` | the name as this text gives it |
| `name_status` | `new` or `additional-attestation` |
| `modern_star` | `{common_name, bayer, constellation}` |
| `identification_confidence` | `certain` · `likely` · `disputed` · `unidentified` — the merged entry takes the **least** confident value across its sources |
| `identification_notes` | reasoning, conflicts, homonym warnings. Becomes `source_notes` in the merged file. |
| `content_note` | optional, rare: why this reference's prose should be chosen rather than landed on (frank sexual/marital content). Presence is the flag the app reads — it keeps the card shut by default, never hidden. The text stays here so the judgment sits next to the passage it judges. |
| `citation` | work + chapter.verse |
| `text_date` | date of the text, not the manuscript |
| `shloka_devanagari` | **verbatim from a fetched e-text.** `null` if unobtainable — never reconstructed |
| `shloka_script` | `devanagari` · `iast` · `chinese` |
| `shloka_note` | textual problems: OCR quality, variant readings, emendations, edition numbering |
| `shloka_source_url` | the exact URL fetched |
| `translation_en`, `translator`, `translation_source_url` | see the rules below |

## Editorial rules

These are what make the database worth citing, and they are not enforced by any script:

- **Verbatim or nothing.** A `shloka_devanagari` must come from a text actually fetched. If it
  can't be found, the field is `null` and `identification_notes` says so. No verse is ever
  reconstructed from memory.
- **Public-domain translations quoted, modern ones paraphrased.** Quote Burgess, Iyer, Keith,
  Eggeling, Whitney, Oldenberg, Wilson, Ganguli, Dutt, Cowell, Vasu verbatim with a URL. Bhat 1981,
  Shukla, Sarma, Pingree, Ramasubramanian, Goldman and other in-copyright work: paraphrase and cite,
  never quote. Own renderings are labelled `"Literal rendering by the compiler"`.
- **Negative findings are entries in `summary_findings`, not omissions.** That the Āryabhaṭīya names
  no individual star, and that Agastya is never the star in either epic, are among the more useful
  things here.
- **Grade your readings.** A clean hit, an expansion from sandhi, and an emendation are three
  different things; say which in `shloka_note`. Several sources exist only as bad OCR, quoted as
  scanned with the normalised reading marked editorial.
- **Flag homonyms.** Prājeśa is Rohiṇī, not the star Prajāpati; Āgneya is Kṛttikā, not the star Agni.
  These stay separate entries with warnings on both.

## The merged file

`star-names.json` is `{title, generated, method, unit, aryabhatiya_finding,
summary_findings_by_source, shishumara_mapping, stars[], caveats_by_source}`. Each star is
`{id, category, name_devanagari, name_iast, modern_star, identification_confidence, see_also[],
references[]}` — the identity fields come from the first source to mention the name, and every
source contributes a reference.

Categories, set by the id lists at the top of `merge.py`: `nakshatra`, `nakshatra-alias`,
`individual-star`, `saptarshi`, `vedic-asterism`, `sky-figure`, `shishumara-position`, `star-road`,
`milky-way`, `sky-region`, `star-word`, `collective`. Every id must appear in exactly one list —
`merge.py` asserts this, so a new name fails the build until it is placed.

## The chart

`build_chart.py` holds the sky positions, which are deliberately **not** in the database: the
research records what a text says, and where a name sits on the sky is a separate judgement.

- `P` — id → `(RA, Dec, magnitude, kind, label override, note)`, J2000 degrees
- `ALIAS_OF` — an alias plots on the star it names, by id, so the two cannot drift apart
- `ROADS` — a vīthī drawn as a dashed line through its own nakshatras
- `GALACTIC` — Milky Way names pinned to the galactic equator by galactic longitude
- `UNPLOTTED_NOTE` — why an entry has no position, shown in the chart

Assertions at the end require every id to be a point, a road, on the galaxy, in a non-plottable
category, or explicitly noted as unplotted. Nothing falls off the chart silently.

## Adding a source

1. Write `sources/<name>.json` on the schema above.
2. Add it to `SOURCES` and `DB_ID_SOURCES` in `merge.py`.
3. Put any new `db_id` in a category list.
4. Give plottable new ids coordinates in `build_chart.py`, or an `UNPLOTTED_NOTE`.
5. `python3 merge.py && python3 build_chart.py`, then `./gradlew :tools:generateCatalogs`.
