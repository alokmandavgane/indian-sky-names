# Sky figures

A name says a language *calls* these stars something. A figure says it *joins* them
into a shape — and every line drawn between two stars asserts that a source saw one
there. That is a much stronger claim, so this is a separate record with tighter
rules than the name database, and it is small on purpose.

```
star-names-local.json ─┐
cultures.json          │
star-names.json        ├─→ validate.py ──→ (exit 0 or the reason why not)
sky-identity.json      │
hipparcos-mag7.csv    ─┘        ▲
                          figures.json  (authored, not generated)
```

`figures.json` is **research, hand-written like `star-names-local/sources/*.json`** —
not derived from anything. `validate.py` is what keeps it honest.

## The finding that determined the schema

The obvious design is a polyline per culture: a list of star pairs to draw. Reading
the material first is what stopped that.

**The sources almost never assign stars to parts.** They say *"the seven stars are a
cot"*, not *"Dubhe and Merak are the head-posts"*. Of 975 names, 136 describe a
shape at all, and only ~31 name both a part of a figure and an identifiable star.
Authoring polylines from the rest would have meant inventing the vertex assignments
— which is precisely the thing this research has never done.

So a figure is recorded as **parts**: the roles the source names, and the stars it
gives them.

```json
{
  "role": "the mourners walking away from the grave",
  "hip": [62956, 65378],
  "attested": true,
  "note": "Alioth and Mizar, both named in the source."
}
```

A role the source names but does not fill is still recorded, with an empty list and
`attested: false` — Lorrain says Dingdi's cloth is pinned to the wall at two stars
and never says which two, and that gap is part of the record rather than something
to paper over. **Lines are derived at export time from parts, never authored here.**

## What the validator enforces

| Invariant | Why |
|---|---|
| culture exists in `cultures.json`, object in `star-names-local.json` — or the culture is a named tradition (`sanskrit`) and the object an id in `star-names` | a figure cannot be about a culture or a thing that isn't there; the Sanskrit tradition is not a language of the vernacular compilation, so its objects are checked against its own database |
| every HIP is a real star in the vendored Hipparcos catalogue | catches the failure that actually happens — a mistyped number drawing a line to nowhere |
| `spans` names every IAU constellation the stars fall in, recomputed | see below |
| a part with stars is `attested: true`, one without is `attested: false` | an unfilled role must never read as a filled one |
| citation present; `source_access` from the name database's vocabulary | in-copyright material is paraphrased, never quoted — the same rule as everywhere else |

All five are negative-tested.

### `spans` is not a containment rule, and that is the point

The first draft required every star to belong to its object's own IAU figure. The
material threw that out within a minute of writing it:

- the **Bhili cot** uses Alcor for the middle thief's child — and the IAU figure of
  Ursa Major draws no line through Alcor;
- the **Kolam Mahua tree** stands in Crux with two women beside it who are α and β
  Centauri — one figure across two constellations;
- α Centauri turns out to be charted with `figure: false` in the vendored
  constellation lines, so even the brightest star in Centaurus fails a
  figure-membership test.

A culture's figure is under no obligation to use the IAU figure's vertices, or to
stop at its boundary. That is the whole reason figures need a record of their own.
So crossing a boundary is not an error — **failing to declare it is**, and the
validator recomputes `spans` from the catalogue and insists the record agrees.

## What is in it

Ten figures, 41 parts, 98 star assignments. Deliberately the ones the sources
actually draw:

| Figure | Culture | What is attested |
|---|---|---|
| the bier | Mundari | the four bowl stars as the broken frame; Alioth and Mizar as the mourners walking away |
| the cot | Bhili | four bowl stars as the legs, three handle stars as the thieves, Alcor as the middle thief's child |
| the Mahua tree | Kolami | Crux as the tree; α and β Centauri as the old lady and the young one gathering flowers |
| Dingdi's cloth-stretching | Mizo | Capella as Dingdi at the loom's apex; the two stars pinning the cloth left unassigned |
| the ladle | Odia | all seven joined, which Praharaj states — a figure that agrees with the received one is still a figure |
| the Śiśumāra | Sanskrit | the Bhāgavata's whole-sky body-map (5.23.5-7): Dhruva at the tail-tip, the Seven Sages at the waist, nakshatras for hips, feet, nostrils, eyes, ears, shoulders and sixteen ribs, Agasti on the upper jaw — 17 parts placed, 5 named and left unfilled |
| Rohiṇī's cart | Sanskrit | the Śārdūlakarṇāvadāna's census: five stars, wagon-shaped — the V of the Hyades the omen books watch for śakaṭa-bheda |
| the pierced deer | Sanskrit | Aitareya-brāhmaṇa 3.33: the deer's head at Mṛgaśiras, the Belt as the three-jointed arrow, Mṛgavyādha the hunter at Sirius, the doe at Rohiṇī — one hunt across three constellations |
| the Seven Sages | Sanskrit | Bṛhat-saṃhitā 13.5-6: the seven named in order as one set, and Arundhatī — the text's one per-star claim — beside Vasiṣṭha at Alcor |
| the seven Kṛttikās | Sanskrit | Taittirīya-brāhmaṇa 3.1.4.1: Ambā, Dulā, Nitatnī and the four rain-names, one set over the Pleiades — six charted, Pleione below the chart's field limit |

Alkaid is unassigned in the Mundari bier because Hoffmann assigns it nothing. That
is the shape of most records here. The Śiśumāra is the one figure the Sanskrit
tradition itself draws star by star: the older recension (Viṣṇu-purāṇa 2.12 and
parallels) seats deities on the limbs and identifies almost nothing, so it is the
Bhāgavata's expansion — nakshatras for limbs — that can be drawn at all. Its
planets, Nārāyaṇa at the heart, and the star-field as body-hair stay in the scene:
they are not fixed stars, and a HIP number would be a false claim. The Seven Sages
are one part, not seven: Varāhamihira assigns the set and the order, not star to
name, and the record claims no more than the text.

## Running it

```bash
python3 validate.py
```

## Where this goes

This is the record Phase 3's Stellarium exporter and Phase 4's per-culture figure
layer both read. Stellarium wants lines; parts are what the sources give, so the
exporter derives lines from parts and must mark that derivation as its own — a
figure whose vertex order was chosen by a program is not a figure a source drew.
A culture with names and no lines is a perfectly legitimate skyculture, and most
of the 58 will be exactly that.
