# Indian Sky Names

What the languages and traditions of South Asia call the sky — and what they draw in it.

**[Browse the record as tables →](https://alokmandavgane.github.io/indian-sky-names/)**
— every name, filterable by language and register, straight from the JSON.

Four research databases, built to be checked: every name carries its source cited to the
page, every Sanskrit attestation reproduces its śloka verbatim with a translation credited
to its translator, and every editorial judgment is written down next to the data it judges.

| Database | What it holds |
|---|---|
| [`star-names/`](star-names/) | The Sanskrit record: 168 entries — nakshatras, stars, asterisms — attested by 448 references across 19 source texts, from the Ṛgveda to the Siddhānta Darpaṇa (1869). Each reference carries the śloka in Devanagari, an English translation, and identification notes. |
| [`star-names-local/`](star-names-local/) | The vernacular record: 975 names for 65 sky objects in 57 languages — from Marathi and Tamil lexicography to Kolami, Korku and Pardhi fieldwork — each tagged by register (vernacular, folk, tribal, borrowed) and cited to the page. |
| [`sky-identity/`](sky-identity/) | The join layer: which star each name means, in HIP numbers — the shared key that lets a Sanskrit attestation and an Adivasi field record agree they are about the same star — plus the culture slugs the atlas publishes. |
| [`sky-figures/`](sky-figures/) | What cultures *draw*, as against what they name: constellation figures as the parts their sources actually describe. |

Each directory has its own `FORMAT.md` (the schema and the rules), its `sources/` (the
research files, which are the originals), and a generated `README.md` that renders the
whole record readable. The generated files say so at the top; edit the sources and re-run
the directory's build script.

## Where this is used

- **[sky.alokm.com](https://sky.alokm.com)** — the atlas: every object, culture and star as
  a page, with essays reading across the record.
- **भगोल Bhagol** — the planetarium app for
  [Android](https://play.google.com/store/apps/details?id=com.alokm.android.stardroid) and
  [iPhone](https://apps.apple.com/app/id6797572192), which letters its live sky from these
  databases.

## Contributing

The unit of contribution is a sourced name: the name as the source prints it, the source
cited to the page, and — for anything in copyright — a paraphrase rather than the text.
Each database's `FORMAT.md` states its rules; the merge scripts validate what they can.
Corrections with citations are as welcome as additions.

## Licensing

- **Data and prose** (the JSON databases, `sources/`, the generated READMEs, `FORMAT.md`,
  charts' content): [CC BY 4.0](LICENSE) — reuse freely, credit the compilation.
- **Code** (`merge.py`, `canon.py`, `cultures.py`, `validate.py`, chart templates):
  [MIT](LICENSE-CODE).

The śloka texts are public domain; translations are used from public-domain editions
(credited inline, e.g. Burgess 1860, Eggeling 1882, Wilson 1840) or are this compilation's
own literal renderings. Names from in-copyright field studies are paraphrased, never
quoted, and marked as such in the record.
