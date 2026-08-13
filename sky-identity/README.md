# Sky identity

The two name databases say what a source *calls* a thing. The chart scripts say
where to *draw* it. Neither says **which star it is** in terms another catalogue
would recognise: `modern_star` carries prose — "β Arietis", "the Pleiades",
"Asellus Aus." — that a reader understands and a join cannot.

This is the missing layer. It resolves every object in both databases to a
Hipparcos number, and every language in the vernacular database to a slug.

```
star-names/sources/build_chart.py  ─┐
star-names-local/sources/build_chart.py ─┼─→ resolve.py  ──→ sky-identity.json
constellation-lines/sources/*      ─┘

star-names-local.json ──→ cultures.py ──→ cultures.json
```

Nothing here is authored by hand. Identity is resolved against the catalogues the
repo already vendors for the constellation-figure work, and every match is checked
against evidence the position could not have produced.

## Why HIP

HIP is the interlingua. Stellarium's skycultures key their names by it, SIMBAD
resolves it, `constellation-lines.json` already uses it for the figure work, and
the app's own `ChartStar.hipparcos` carries it. One number makes the vernacular
record joinable to every other star catalogue on earth — and makes the two
databases joinable to *each other*, which they were not: `arundhati` in the
Sanskrit compilation and `alcor` in the vernacular one are the same star, and
until now nothing said so in a form a program could read.

## How a match is believed

Three independent lines of evidence, and a match is reported with however many it
has rather than asserted:

| Evidence | Where it comes from |
|---|---|
| **position** | angular separation from the Hipparcos catalogue, within 0.1° |
| **magnitude** | the magnitude the Sanskrit table plots at, within 0.06 mag |
| **name** | the trailing `# Aldebaran` comment, `modern_star`, or the object key, against the IAU proper name, Bayer letter or Flamsteed number |

Position is the primary evidence; the others corroborate. The checker is
deliberately conservative — where a hint is prose that names no star at all
("the stars of Orion's head"), it reports *nothing to check* rather than inventing
agreement, and where a hint contradicts, it says so and asks for a human.

At the last run: **114 of 114 single stars resolve**, every one with at least two
independent lines except the aliases, whose evidence is their target's.

## Figures, clusters and roads

A figure is not one star, so it gets a list. There are three honest ways to fill
that list, and **no HIP is ever typed by hand**:

| How | Count | Where the members come from |
|---|---|---|
| `constellation` | 27 | the stars `constellation-lines.json` already draws lines through — not every star inside the boundary |
| `objects` | 11 | other objects in the same table, by key, so they cannot drift apart |
| `designations` | 8 | the compilation's own note, transcribed as *designations* — `"delta Leo"`, `"Bellatrix"` — and resolved to HIP against the catalogues |
| `cluster` | 2 | a cluster designation (M45, M44, Mel 25), plus the members the tradition counts individually |

The `objects` route is the one worth pointing at. `saptarshi` does not carry seven
numbers; it carries the seven ṛṣi keys the compilation already names — `marichi`,
`vasishtha`, `angiras`, `atri`, `pulastya`, `pulaha`, `kratu` — and their HIPs are
read from their own verified resolutions. The nine star-roads work the same way,
each drawn through its own three nakshatras. A road can never disagree with the
nakshatras it runs through, because it is not told them twice.

Where a note enumerates nothing, the figure is left **without** members and the
reason is recorded — `mulabarhana` is *"the Scorpion's tail as a whole"*, and no
source here draws that boundary. Inventing one is the single thing this database
has never done.

**48 figures, clusters and roads carry members; 295 distinct HIP numbers are
referenced in all.** Every designation token resolved; none were left dangling.

## What is deliberately not here

Of 65 vernacular objects, 25 have no identity record, and of 168 Sanskrit ids, 46
do not. That is correct, not a gap. They are the planets, the sun and moon, comets,
meteors, eclipses, the rainbow, the many names for the Milky Way — and the generic
words for *star*, *asterism*, *constellation* and *zodiac*. None of them is a
star, and the position tables do not place them either.

## What this found

Three coordinate errors, all the same shape: a right ascension borrowed from a
neighbouring row while the declination and magnitude stayed correct.

| Object | Was | Is | Evidence |
|---|---|---|---|
| `ashlesha`, `sarpa` | RA 130.80 | RA 131.69 | ε Hya, whose Dec and mag 3.38 already matched exactly — and whose IAU proper name is *Ashlesha* |
| `vishakha` | RA 222.72 | RA 228.06 | 222.72 is α² Librae's RA, copied from `radha`; ι Lib's own Dec and mag 4.54 were already right |
| `alcor` (local) | RA 200.98 | RA 201.31 | 200.98 is Mizar's RA; the Sanskrit table's `arundhati` had Alcor right all along |

Each plotted a name onto the wrong star, or onto empty sky. All three are fixed in
the chart tables.

## The culture unit

One culture is **one language**, as the compilation names it. `cultures.py` mints
the slug — `mizo`, `sema-naga`, `marathi` — and carries the ISO 639-3 code beside
it. The slug is the readable one because it has to serve as a URL; the code is one
field away for anything joining on it.

Two things it deliberately does not do:

- **Register does not split a culture.** Marathi-borrowed and Marathi-vernacular
  are one culture seen at two depths, and that they coexist is the database's
  central finding. Register is a stratum within a culture.
- **Community does not split a culture.** Of eleven distinct values, most are
  provenance prose rather than an identity — *"Hindu households of Sialkot
  district; Rose's informants are not further specified"*. Splitting on a field
  that is usually a footnote would mint a dozen near-empty cultures and bury the
  real ones. Community stays an annotation on the name, where the source put it.

58 cultures, no slug collisions. Three carry no single ISO 639-3 code, and are
recorded that way rather than resolved — inventing one would be a claim no source
made:

| Culture | Why |
|---|---|
| `nicobarese` | a cover term; Central Nicobarese, Chaura and Teressa are also here as languages in their own right |
| `andamanese` | a cover term for two distinct languages (`abj`, `akj`) that no source separates |
| `cholanaikkan` | no code in the sources |

## Running it

```bash
python3 resolve.py            # report only
python3 resolve.py --write    # also write sky-identity.json
python3 cultures.py --write   # also write cultures.json
```

Both read the chart scripts by parsing their syntax tree, never by importing them:
those modules load their databases at import time and are not safe to import from
anywhere but their own directory. The read is one-way. This layer sits beside the
existing pipeline and does not disturb it.

Four tables are read out of `star-names/sources/build_chart.py`, because the chart
builds its own at runtime and a literal read of `P` alone would miss most of them:

| Table | What it adds |
|---|---|
| `P` | the plotted points |
| `ALIAS_OF` | 28 names other texts give a star already in `P` — each re-resolved through the same verified path, then marked `alias_of`, so "another name for Aldebaran" is distinguishable from an independent identification of it |
| `ROADS` | the nine star-roads |
| `POS` (local) | the vernacular table, plus its `nak-` bridge into the Sanskrit one |
