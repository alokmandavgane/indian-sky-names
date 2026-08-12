# Expanding the local star-name database

A plan for taking `docs/star-names-local/` from nine literary languages to the tribal, regional and
occupational sky-lore of India. It began as a *search* plan — which resources exist, where they
are, what state they are in, and in what order to work them — and it has since been rewritten wave
by wave into the record of what each one found. **Every wave and sub-wave in it is now done.**

Read `FORMAT.md` first; every rule there still binds. Nothing below relaxes *verbatim or nothing*,
*no back-transliteration*, *negative findings are recorded*, or *don't force an identification*.

---

## 1. Where the database stands

**928 entries · 64 objects · 57 languages · 525 linked to the Sanskrit database.**
Thirteen source files. **All waves of this plan are done, including the five sub-waves.**
*(At the time this plan was first written: 522 / 46 / 26, seven files.)*

| Register | Entries | After wave 6 | At plan start |
|---|---|---|---|
| vernacular | 220 | 209 | 177 |
| folk | 106 | 106 | 101 |
| tribal | **387** | 250 | 91 |
| sanskritic | 215 | 212 | 153 |

The shape of the coverage, still lopsided but much less so:

- **Deep**: Marathi (64), Tamil (62), Telugu (57), Kannada (41), Mizo (38), Malayalam (36),
  Sindhi (34), Pardhi (33), Korku (32), Odia (31), Hindi (31).
- **Adequate**: Mundari (26), Bengali (24), Sinhala (24), Kolami (21), Urdu (20), Gondi (20),
  Kashmiri (18), Garo (18), Mara (18), Chhattisgarhi (18), Santali (17), Rengma (16), Nepali (14).
- **Thin but real**: Lambadi (12), Divehi (12), Punjabi (12), Assamese (11), Rajasthani (11),
  Angami (10), Chowra (10), Sema (10), Bhili (9), Camorta (9), Kurukh (9), Sora (9), Newar (9),
  Tulu (8), Teressa (8), Meitei (7), Toda (7).
- **Token**: Konkani (5), Cholanaikkan (5), Khasi (5), Kokna (4), Mavchi (4), Nicobarese (4),
  Ao (4), Andamanese (3), Kui (3), Kodava (3), Pawra (3), Tibetan (2), Ho (2), Kumaoni (2),
  Gujarati (2), Vasavi (1). *(Divehi's are deliberately a sample of 27 — see §7.)*
- **Still absent entirely**: Garhwali, Ladakhi, Spiti, Bhutia, Monpa, Sherpa and Lahuli — the
  Buddhist Himalaya is now *reached* and still unread, for the reason given in §8b — and Bodo,
  Sylheti, and the Naga languages other than the four here.

The register tags remain the honest measure. `tribal` now covers **twenty-eight** communities rather
than five — but India has several hundred Scheduled Tribes and around 120 languages with more than
10,000 speakers. This is a good start, not a survey.

### What the existing files say is missing

These are recorded negatives, not oversights, and each is a work item:

| Gap | What the file says | Status |
|---|---|---|
| Rajasthani | "NO RAJASTHANI ENTRY IS CLAIMED" — Lalas in copyright, no PD source reached | **Closed in Wave 0**, see §2 |
| Gujarati | "DSAL has no Gujarati dictionary"; scans OCR to noise | Claim **upheld** in Wave 0, see §2 |
| Bhili | Nothing in PD; JAHH 26(2) 2023 unobtainable | **Closed in Wave 1**, see §3 |
| Naga | Hodson 1911 grepped, zero star names | Still zero; sources 503'd in Wave 3, see §5 |
| Andamanese | Radcliffe-Brown: constellations not recognised in North Andaman | Genuine result, leave |
| Bodding vols 1–4 | Not findable online; would deepen Santali | Retry, §11 |
| Encyclopaedia Mundarica vols I, IV, VIII, IX, XI, XIV–XVI | Missing | Retry, §11 |
| JASB | "not searched, worth a later pass" | §11 |
| Bhaduri, *Astronomy of the Mundas*, Man in India | Lead identified, not followed | §11 |
| Vahia/Halkare series beyond Gond | Korku, Kolam, Banjara, Pardhi noted as out of scope | **Four of seven done in Wave 1**, §3 |

---

## 2. Wave 0 — the correction pass. **Done, 2026-08-12.**

### What the re-check actually found

The DSAL holdings page lists dictionaries it does not host. Several entries carry
*"License agreements for Web use need to be negotiated"* or *"We are currently building a searchable
database out of this data"* and have **no link** — announced, not available. The listing must be read
by its links, not its bibliography. Doing that gives the real inventory:

| Language | Live on DSAL | Listed but NOT hosted |
|---|---|---|
| Rajasthani | `macalister` (1898, PD), `lalasa-2nd` (2013) | — |
| Tamil | `fabricius`, `winslow`, `tamil-lex`, `kadirvelu`, `crea`, `mcalpin`, `tamil-idioms` | — |
| Kashmiri | `grierson` (1932, PD), `hassan` | Shauq 2024, Tośah Khānī |
| Sindhi | `mewaram` (1910, PD), `baloch` | — |
| Lushai (Mizo) | `lorrain` (1940) | — |
| Nepali | `turner` (1931), `schmidt` | — |
| Newar | `jorgensen` (1936), `malla`, `manandhar` | — |
| Manipuri | `sharma` | — |
| Sylheti | `gwynn-sylheti` | — |
| Comparative | `burrow` (DEDR), `soas` (CDIAL) | — |
| **Gujarati** | **nothing** | Śāstrī, *Bṛhad Gujarātī Kośa* |
| **Konkani** | **nothing** | Thali 1999–2001, Ghanekar 2009 |
| **Tibetan** | **nothing** | Jäschke 1881, Das 1902 ("building") |
| **Mundari** | **nothing** | *Encyclopaedia Mundarica* — "copyright approval is pending" |
| Sinhala | `carter` | Jayatilaka 1935 |

So of the three corrections this plan originally proposed, **two held and one was wrong**:

1. ~~DSAL hosts a Gujarati dictionary~~ — **it does not.** `marathi_gujarati.json` was right. Its
   wording has been tightened to "no *searchable* Gujarati dictionary", with the reason recorded so
   nobody chases it again. The same applies to modern Konkani and to Tibetan.
2. **DSAL hosts Rajasthani** — confirmed, and both dictionaries were worked. See below.
3. **DSAL hosts Fabricius** — confirmed, and it was searched.

### What changed in the database

**529 names · 46 objects · 27 languages** (was 522 / 46 / 26).

**Rajasthani, 7 entries, gap closed.** The old caveat said Lalas "is in copyright and was not
consulted" — treating copyright as a reason not to *read* a source, where the rest of this database
treats it only as a reason not to *quote* one. Both dictionaries were read on this pass:

- **सातरसा *sātarasā*** "the Pleiades" — Macalister 1898 p. 30, public domain, quoted verbatim. Not
  a reflex of Kṛttikā. Macalister has no word for "star" at all, and only one other celestial
  headword in the whole book (आंमर *āmmara* "the sky"), so the dictionary is thin, not silent.
- **किरति / किरतियाँ / किरती / किरतीयु** for Kṛttikā and **आदरा *ādarā*** for Ārdrā — Lalas,
  paraphrased. Both are tadbhavas, but what hangs on them is not: six stars counted in Kṛttikā, a
  lightning proverb, and five rain-couplets under Ārdrā, three of them invoking **Bhaḍḍaḷī** by
  name — the female counterpart of the Ghāgh already quoted in this file for Bihar.
- **The find: Rajasthani orients itself by where Ursa Major sets.** **रिसिअस्त *risiasta***, "the
  setting of the ṛṣis", is a *point of the compass* — the quarter between north and north-west — and
  three winds are named off it: **ओकड़ *ōkaṛa*** and **दावौ *dāvau***, which damage the standing
  crop, and **सूरयौ *sūrayau***, which blowing in Śrāvaṇa is read as a sign of rain. No other
  language in this database names a direction or a wind after a constellation. The Great Bear here
  is not a figure to be named but a bearing to steer weather by.

Still not found for Rajasthani at the end of this wave: Orion, the Milky Way, the pole star, comets,
meteors, and any independent word for "star". **Wave 2 finished the list — see §4.**

**Tamil: Fabricius adds no name and strengthens the negatives.** Full-text search returns *nothing*
for Sirius, Antares, Arcturus and Canopus, so the absence of Tamil names for those four now rests on
three independent dictionaries instead of two. Its one novelty is **rejected**: Fabricius glosses
நட்சத்திரமாலை *naṭcattira-mālai* as "the galaxy or milky way" (p. 584), where the Madras Tamil
Lexicon (p. 2135) gives only "cluster of stars", "the lunar zodiac", "= நட்சத்திரவீதி, the moon's
path", and "a treatise" — no Milky Way sense anywhere. Recorded as a disagreement, not entered.

### One method finding, and it bites everything downstream

**DSAL's search-results view silently drops words; its page view does not.** The Lalas entry for
ध्रुव returns `दिशा की ओर स्थित एक प्रसिद्ध तारा` from a search but `उत्तर दिशा की ओर स्थित एक
प्रसिद्ध तारा` from `…_query.py?page=1968`. Macalister's search view strips diacritics *and* full
stops — `सातरसा satarasa m The Pleiades` against the page view's `सातरसा sātarasā , m. The Pleiades.`

Every quote and gloss in this Wave was re-read on the page view, and `source_url` now points at the
page rather than at a query. **All later waves must do the same**, and any existing entry quoted
from a `?qs=` URL is worth re-checking against its page.

---

## 3. Wave 1 — the modern field surveys. **Done, 2026-08-12.**

**642 names · 51 objects · 38 languages** (was 529 / 46 / 27). The `tribal` register went from
**91 entries to 202** — from five communities to sixteen. New file: `sources/tribal_fieldwork.json`,
113 entries, grouped by *method* rather than by language because these surveys differ from the
lexicography in reliability, in copyright status and in unit of observation.

Communities added: **Banjara, Kolam, Korku, Camorta / Chowra / Teressa Nicobarese, Bhil, Mavchi
Bhil, Vasave Bhil, Pawra, Kokna.** All five papers are in copyright, so all 113 entries are
paraphrased with `quote: null` — the footing tribal.json already set for its Gondi entries.

### The four cross-family threads all held, and two got sharper

- **The cot.** Kolami *Mandater* a cot; Lambadi *Jamakhat* the cot of the **dead** (from Yama);
  Chowra *Lonob* a hen-basket; Teressa *Rohiung* a **coffin**; Bhil, Pawra and Kokna the cot with a
  leg pulled crooked. The death sense, which tribal.json found only in the Mundari bier, now turns
  up three more times in unrelated languages.
- **The three thieves — but *who* they are is local politics.** Korku numbers them (*Pahila*,
  *Dusara*, *Tisara chor*). The Kolams make them a Kolam, a Gond and a Pardhan — one man of each
  community sharing the landscape. The Bhils make them the village elder, the chief, the sheriff and
  the revenue collector: the men who actually come to take things.
- **Orion is an implement, never a hunter.** Kolam *Tipan* and Bhil *Pambar*, both seed drills; Korku
  lays out the whole scene star by star — *Harnangar* the plough (the Belt), *Doba 1* and *Doba 2*
  the two bullocks (Rigel, Saiph), *Nangarnara manus* the ploughman (Betelgeuse). The one exception
  is the Banjaras, a trading people, who keep the mainstream deer.
- **The Milky Way is a road with animals on it** — Kolam *Margam*, Banjara *Mardaar wat*, Bhil "the
  path of cows" — except in the Nicobars, where it is a spring of water, exactly as tribal.json
  predicted from Whitehead a century earlier.

### Two results that are new

**The bird and its eggs is the most productive figure in the material.** Kolam *Kovela Kor* (the
Pleiades as one large bird and several small), Kolam *Bhori* (Aldebaran, a bird with two eggs),
Korku *Pankheru* (Sirius) with *Bhori Aakom* its eggs — the same word *Bhori* in a Dravidian and a
Munda language — and among the Bhil, Pawra and Kokna a single bird named *hulgi* whose eggs are
Orion's Belt in one village, the Pleiades in another and a triangle of Auriga in a third. The figure
is stable; the stars it lands on are not.

**The Bhil Milky Way is a kinship rule drawn on the sky.** At Varpada the band forks because a woman
walking the road meets her husband's elder brother and must turn aside — an avoidance that is a real
rule of conduct in these communities. Elsewhere it forks into the gods' path and the
daughter-in-law's, or the father-in-law's ghost path and the daughter-in-law's.

Also: Kolam *Irukmara*, the Mahua tree at Crux with an old woman and a young woman gathering its
flowers beneath, is almost certainly the same word as Gondi *Irukna Mara*, which tribal.json had to
grade `unidentified`. That entry is deliberately **not** altered — a cognate's identification in
another community is evidence, not proof — but the two now cross-reference each other.

### What Wave 1 did not get

Three papers of the same programme were not obtained and **no entry is offered from them**: the
Pardhi study, the Cholanaikkan study, and the Warli / Dhodia / Katkari / Kokna study. The
second-hand Nicobarese lists quoted inside the 2018 paper from Rajamanickam (1997) and Justine
(2013) are recorded as leads but not entered — this database does not rest an entry on a
transcription at second hand.

### Two source-handling problems worth knowing before Wave 1b

- **The Korku paper's Greek letters are gone.** The ADS scan renders every Greek glyph as a solid
  black box *in the page image as well as the text*. Where the paper also prints a proper name the
  designation is unambiguous and was restored; where it prints only the letter, nothing was — hence
  *Bharada*, *Pati* and *Patni* graded `unidentified` and *Miryan* `likely`.
- **The Bhil paper cannot be extracted as text at all.** Its font subsets carry no ToUnicode map, so
  extraction yields a monoalphabetic substitution cipher — a *different* one per font. Every Bhil,
  Pawra, Mavchi, Vasave and Kokna reading was read off a rendered page image at 150 dpi. Solving the
  cipher against English prose was rejected: it is not evidence for the spelling of a Bhili word.

**Getting the papers:** ADS serves JAHH full-text scans free at
`articles.adsabs.harvard.edu/pdf/<bibcode>` (e.g. `2016JAHH...19..216V`, `2023JAHH...26..441S`) —
SciEngine returns HTTP 418 to scripted requests. Banjara/Kolam is `arXiv:1406.3044`; the Nicobarese
paper is an open PDF on heritageuniversityofkerala.com.

---

## 3b. The field-survey programme, for reference

Mayank Vahia, Ganesh Halkare and colleagues have been doing exactly this work as fieldwork since
~2010, community by community. The existing `tribal.json` uses **one** paper of the series and flags
the rest as out of scope. Bringing in the whole programme is the highest-yield move available.

Communities covered by the series, as far as can be traced:

| Community | Where | Publication |
|---|---|---|
| Gond | Vidarbha / Adilabad | JAHH 16(1), 2013 — in `tribal.json` |
| Banjara, Kolam | Vidarbha | JAHH 17(1), 65–84, 2014; `arXiv:1406.3044` — **done, Wave 1** |
| Korku | Melghat, Satpuras | JAHH 19(2), 216–232, 2016 — **done, Wave 1** |
| Pardhi | Vidarbha | JAHH — **not obtained** |
| Nicobarese | Nicobar Islands | *Heritage Journal* 6, 1014–1039, 2018 — **done, Wave 1** |
| Cholanaikkan | Nilambur, Kerala | JAHH — **not obtained** |
| Warli, Dhodia, Katkari, Kokna | Thane/Palghar, Gujarat border | JAHH — **not obtained** |
| Bhil, Pawra, Kokna | Khandesh / N. Maharashtra | JAHH 26(2), 441–468, 2023 — **done, Wave 1** |

All are in copyright. The established convention applies unchanged: **paraphrase, cite, `quote:
null`**, exactly as the twenty Gondi entries already do. The arXiv preprints and the open Heritage
PDF mean several are obtainable in full text without a library.

Expected yield: 100–200 entries across 12+ communities, all genuinely `tribal` register, and — this
is the point — they will test the three cross-family figures the existing file identified (the cot
with thieves, the plough/yoke that is never a hunter, the cattle-road Milky Way) against a dozen
independent traditions. That test is a result whichever way it comes out.

**Adjacent**: check whether the same group or others have published on Irula, Kurumba, Paniya,
Chenchu, Koya, Savara/Sora, Juang, Bonda, Saharia, Baiga, Muria. Search JAHH, *Current Science*,
*Indian Journal of History of Science*, and the ICOA proceedings.

---

## 4. Wave 2 — the north-west. **Done, 2026-08-12.**

**687 names · 51 objects · 40 languages** (was 642 / 51 / 38). New file:
`sources/northwest.json`, 41 entries — Sindhi 23, Kashmiri 18 — plus 4 more Rajasthani appended to
`hindi_urdu_punjabi.json`, which finishes the pass Wave 0 left half-done.

### Sindhi has a sky of its own under the loans; Kashmiri has almost none

That contrast is the wave's result, and it is not what two neighbouring Indo-Aryan languages with
the same two learned traditions behind them would predict.

**Sindhi** (Mewaram 1910, public domain, quoted verbatim) yields three names that belong to neither
tradition:

- **ٽيڙۇ *ṭīṛū*** for **Orion's Belt** — not Sanskrit *ishus-trikāṇḍā* or *mṛgaśiras*, not Arabic
  *jauzā* or *an-niẓām*. Mewaram gives no derivation and none is claimed.
- **ڊۇهُ *ḍūhu*** for the **pole star**, whose second sense at the same entry is the adjective
  *"motionless, stationary, stable"*. Every other north-western name for Polaris imports that idea
  with a foreign word — Sanskrit *dhruva*, Arabic *quṭb*, Arabic *jadī* — and Sindhi reaches it in
  its own vocabulary.
- **چوٽيٴ تارو *choṭīa tāro***, the comet as a woman's braided **topknot**, beside the ordinary
  *puchiru tāro* "tailed star". The Sanskrit comet is smoke and the Munda comet is a broom; the
  topknot is Sindhi's alone.

The rest is the three-layer stack `hindi_urdu_punjabi.json` found for Hindustani, and single
headwords make the layers visible: **جَديِ *jadī*** is Arabic *al-jady*, Capricorn **and** the pole
star at one entry, with **قُطِبنُما *quṭub-numā***, the mariner's compass, beside it — the only
navigational word the whole north-west produced.

**Kashmiri** (Grierson 1932, public domain) gives the nakshatras in Kashmiri phonology — *kraʦh*,
*mag* with its five Leonis stars named by Grierson himself, *hostu* in Corvus, *shrawun* of three
stars, *abizĕth* — plus Persian *sitāra*, Arabic *suraiya*, *ulkā* for a meteor and *ketu* for a
comet. And that is all. **No Kashmiri name for Orion exists anywhere in the 1,200 pages**, none for
Sirius, none for Canopus, none for the evening star, none for the Milky Way that is not the Sanskrit
compound. The single Kashmiri formation in the whole sky is **क्रच़ि-कूरू॒ *kraʦi-kūrü***, "a
daughter of Kṛttikā", for any one of the six Pleiades, with the plural *kraʦi-kōrĕ* for the cluster:
*kūrü* is the ordinary Kashmiri word for a daughter, and the compound gives the group a singular and
a plural the bare loan does not have.

### Rajasthani, finished — and the answer is a negative

Outside the Saptarṣi wind cluster Wave 0 found, **Rajasthani names the sky in Sanskrit.** Orion is
only *mrigasirā* in five variants; the Milky Way is five tatsama compounds; the comet is the whole
Bṛhat-Saṃhitā catalogue of *ketu*s; the meteor is *ulkā*. The word for star, **तारौ *tārau***, has
as its most specific sense not a star at all but **the season in which Jupiter and Venus are
invisible and no wedding may be held** — the Rajasthani counterpart of the Telugu *kārte* and the
Tamil *nāḷ*. One survival earns its entry: **गजबीथी *gajabīthī***, and the *nakṣatravīthi* scheme of
nine star-roads set out at its own headword **with Devala and Kāśyapa named as differing
authorities** — the vīthī material of Bṛhat Saṃhitā 9 and Utpala, alive in a dictionary of 2013, and
the first entry here from the Sanskrit compilation's `star-road` category.

### Negatives and what was not reached

No Sindhi or Kashmiri name for Canopus, the Hyades, Antares, or the Great Bear as a figure — though
**both languages name Alcor**, the faintest thing in it, and nothing else in the constellation. No
Sindhi word for a meteor.

**Rose's *Glossary of the Tribes and Castes of the Punjab and NWFP* is a near-total negative and an
unfinished search.** Only volume 3 could be downloaded (archive.org returned HTTP 503 for volumes 1
and 2); searched for nine sky terms it produced exactly one hit — a Lahauli funeral rite governed by
the *pañcaka* — and no star name at all. Consistent with the pattern already seen: caste-and-tribe
compendia are dry, and when they yield they yield one community in four volumes.

**Not searched:** `baloch`'s *Jāmiʻ Sindhī lughāt* and the modern Kashmiri dictionaries. Both are
monolingual, so the English-gloss method used throughout this wave does not reach them; a proper
pass needs the questions asked in the language.

### Method note

Mewaram prints **no romanization at all** — Sindhi script to English throughout. The roman here is
therefore the compiler's, the one place in this database where that is true of a public-domain
source. It is a reading of a *pointed* text (Mewaram marks the short vowels), and `name_native` is
the script exactly as the page image shows it. Grierson is the opposite and needs no warning: roman,
Devanagari and a Sanskrit gloss for every headword.

---

## 5. Wave 3 — the north-east. **Done, 2026-08-12.**

**731 names · 58 objects · 43 languages** (was 687 / 51 / 40). New file `sources/northeast.json`,
44 entries — Mizo 36, Meitei 7, Mara 1.

### This wave was predicted to be thin. It is the richest single pass in the database.

The prediction was reasonable: `tribal.json` had grepped Hodson's *Naga Tribes of Manipur* for six
sky terms and got zero hits, and Gurdon's *The Khasis* yielded only the sun and the moon. But nobody
had opened **Lorrain's *Dictionary of the Lushai Language* (1940)** — and Lorrain is the best single
source in this whole compilation.

**Twenty-two star and constellation headwords**, and for most of them he says *which Western stars
they are*: Capella and three others in Auriga; a group in Taurus near Aldebaran; two close stars in
Monoceros; Castor, Pollux, Procyon and Sirius; three small stars in Orion; Rigel; four stars in
Delphinus; three in Aquila and four in Delphinus. **No other source here maps an indigenous sky onto
the modern one star by star.** Shakespear (1912) independently confirms the system is live: *"Many
of the stars and constellations have received names; most of them have some story attached to
them."*

### The figures are not the mainland's

- **No cot in Ursa Major and no thieves at it.** The Mizo name *Zâng-khua* is not glossed at all.
  What Lorrain records instead is **Zângkhua bung-bu**, a *verb* — "to be upside down, as the Great
  Bear when high in the heavens" — used metaphorically for the tables being turned. The only place
  in this database where a constellation's changing orientation has become an idiom, and a precise
  observation as well as a proverb.
- **No plough in Orion and no deer.** *Si-mei-talh* is "three small stars in Orion", *Si-va-hluk* is
  Rigel, neither glossed.
- **The best-drawn figure here: Dingdi-puan-tah.** Capella at the apex of an isosceles triangle in
  Auriga is a young woman named Dingdi weaving, and **the cloth she is weaving is pinned to the wall
  at the two base stars**. A named character, an action, and two stars serving as nails.

### Two threads from the earlier files cross the mountains

**Star-dung.** Mizo has the compound **arsi êk** — Lorrain's own entry for *êk* glosses it
"excrement, dung" and cross-refers here — but attaches it to the rosette markings on maturing
bamboo, not to a meteor (which is *arsi thlâwk*). **Meitei puts it back where the Munda and
Dravidian languages have it**: *thawānmicāk mathi*, and Sharma prints the morphology himself,
`[star + faeces]`. The idea now spans Munda, Dravidian and Tibeto-Burman.

**The Pleiades run the farming year.** **Siruk la** is the last and greatest nor'wester of spring,
named because it coincides with the *heliacal setting* of the Pleiades, and the Lushais reckon the
rice must be sown before it comes. That is Santali *ruhni*, the Telugu *kārte* and the Rajasthani
Bhaḍḍaḷī couplets again — and it also names a wind from a constellation, as Rajasthani *okaṛa*,
*dāvau* and *sūrayau* do from Ursa Major.

### Two new kinds of thing enter the database

- **suk-chen**, "a pestle's length" — the unit in which the Lushai measure the height of the sun,
  moon or stars above the horizon. The **first native angular measure** recorded here, and the
  inland counterpart of the west-coast fist-and-finger measures (*kai kanakku*, *viral kanakku*,
  *dhru*) that Wave 5 will reach. It creates the object *Measuring the sky*.
- **Āwk**, the fabulous creature that swallows the sun or moon, said by some to be the spirit of a
  Pawi chieftain — an eclipse-swallower who is not Rāhu. Creates the object *Eclipses*.

### A three-language meteor belief, compared by the ethnographer himself

Shakespear in 1912 records the Lushai **Chawifa**, a meteor that flies blazing through the village
and kills the householder it lands on; gives the Lakher **Thla-shi-pu** for the same thing with the
*opposite* omen — where it falls is where to cut next year's jhum, and the crop will be good; and
compares the Manipuri **Sangaisel**. Sharma's Manipuri dictionary of 2006 has *sanggāisen*
independently. **Chawifa is not in Lorrain** under that or any adjacent spelling — for once the
ethnographer has what the lexicographer lacks.

### Negatives and what was not reached

Meitei has no name for Orion, the Great Bear, Venus or a comet in Sharma, and its only pole star is
the Sanskrit *dhrubatarā* — the Manipur valley looks far more Sanskritised than the hills around it,
which is what its history predicts.

**No Naga, Garo, Bodo or Khasi material was added.** Playfair's *The Garos*, Hutton's *The Angami
Nagas*, Mills' *The Ao Nagas* and Endle's *The Kacharis* all returned HTTP 503 from archive.org
across repeated attempts and were not read; the mission dictionaries for those languages are on
neither DSAL nor any route reached here. Sylheti was not searched. Khasi still rests on five words.
**The stories Shakespear says attach to most Lushai constellations are in neither source** and are
the obvious next thing to chase.

Ten of the 36 Mizo entries are graded `unidentified`, which is the honest shape of the source:
Lorrain names a figure and then, about a third of the time, says nothing beyond "the name of a
Lushai constellation". They are kept — an unidentified indigenous figure is a result, and their
number *is* the finding.

---

## 6. Wave 4 — the Himalaya. **Done, 2026-08-12.**

**756 names · 58 objects · 46 languages** (was 731 / 58 / 43). New file `sources/himalaya.json`,
25 entries — Nepali 14, Newar 9, Kumaoni 2.

### Nepali builds its whole sky by compounding on one noun

Turner's entry for **तारो *tāro*** is the Nepali heaven in miniature: *dhrub-tāro* the polestar,
*puchre tāro* "the tailed star" a comet, *phuṭne tāro* "the bursting star" a meteor, *tārā-maṇḍal* a
constellation, and — at the same headword, without ceremony — **सात् तारा *sāt tārā*, "the seven
stars", the Great Bear.**

That last is the finding. Every mainland community in this database sees furniture in those seven
stars and somebody stealing it; **Nepali just counts them.** The learned calque *sapta-rikhi* stands
elsewhere in the dictionary, made (Turner says) "on the model of" Sanskrit *saptarṣi* — so Nepali has
both, and only the count is ordinary speech.

The other real Nepali figure is **तिन्-तारे *tin-tāre***, "the three stars", which Turner defines as
three particular stars that always appear in a straight line — Orion's Belt, named for what it looks
like, as Sindhi *ṭīṛū* and Mizo *Si-mei-talh* are.

For the **Pleiades** Nepali has three words at once: its own *gujmuji tārā* "the bunched, clustered
stars"; the Hindi loan *kacpaciyā*, the same crowding image travelling up from the plains; and
*kirkiṭi*, which Turner marks "popular" and derives from the loan *kṛttikā* with an audible shrug —
"after what?" He compares Nepali *kirkaũlā*, "small bits of rice grains", which is probably the
answer he would not commit to.

And **मुल् *mul***, the eleven-star asterism reckoned unlucky, has a derivative **मुल्याहा
*mulyāhā*** — "born under *mul*", and as a noun "an unfortunate person, an orphan". Elsewhere here
the asterisms govern the farming year; this is the only one that names a social condition.

### Newar is the opposite shape: borrowed asterisms, home-made meteors

Every Newar asterism is Sanskrit and the Milky Way is *ākāśa gaṅgā*. What Newar made itself is the
*transient*: **ताहाव नगतिं *tāhāva nagatiṃ***, "the long star", for a comet or shooting star, with
the modern reflex *tāhāhnagu* and the modern paraphrase *mhepwanā tahā̃ nagu*, "the star with a
drawn-out tail".

**And Newar can be dated.** Malla's *Dictionary of Classical Newari* is compiled from manuscripts and
cites the Nepal Saṃvat of each attestation, so this file carries **the only dated vernacular
star-words in the database**: *ādra* in NS 509 (1389 CE), *ulaka* and *tāhāva nagatiṃ* in NS 811
(1691), *dhurmmaketu* in NS 883 (1763).

### The Indian Himalaya is essentially unreached — the honest headline

Grierson's Pahārī volume (LSI IX.4) was downloaded in full and searched. The comparative word-list
gives only a reflex of *tārā* for "star", and the Kumauni-English vocabulary yields **exactly one
sky name**: *lampuchhā tāro*, "the long-tailed star", a comet. Nothing for the Pleiades, Orion, the
Great Bear, the Milky Way or the pole star in Kumaoni or any other Pahārī dialect in the volume —
and the Devanagari in that scan is OCR noise, so nothing could be transcribed in script.

**Tibetan and Ladakhi were not reached at all.** DSAL lists Jäschke (1881) and Das (1902) but hosts
neither ("we are currently building a searchable database out of this data"), and both — with
Atkinson's *Himalayan Gazetteer* — returned HTTP 503 from archive.org on every attempt. So there is
no Ladakhi, Spiti, Bhutia, Monpa, Sherpa or Garhwali material here, and **the Buddhist Himalaya,
which has a fully developed astronomy of its own, is absent from this database entirely.** That
absence is a gap in the search, not a finding about the region.

### Method note: copyright runs a long way

All but two entries here are paraphrased. Turner 1931, Jørgensen 1936, Manandhar 1986, Malla 2000
and Schmidt 1993 are every one of them still in copyright — Turner died in 1983 and Jørgensen in
1974, so their dictionaries of 1931 and 1936 run to 2053 and 2044. The two exceptions are the
Kumaoni entries from Grierson (1916), quoted verbatim including the OCR's own errors, with the
readings marked editorial and graded `likely`.

---

## 7. Wave 5 — the maritime calendar and the peninsular forest. **Done, 2026-08-12.**

**774 names · 58 objects · 48 languages** (was 756 / 58 / 46). New file
`sources/maritime_peninsular.json`, 18 entries — Divehi 13, Cholanaikkan 5, Tamil 1.

### The Maldive and Minicoy sky is the same twenty-seven asterisms, re-indexed against the monsoon

Maniku's Dhivehi vocabulary gives every one of the twenty-seven a headword with its stars in Bayer
designations — and defines each **not by its place in the moon's circuit but by its number within a
monsoon**: eighteen *nakaiy* of the *hulhangu* or south-west monsoon, from *Assidha* (Aśvinī) to
*Dhosha* (Jyeṣṭhā), then nine of the *iruvai* or north-east, from *Mula* (Mūla) to *Reyva* (Revatī),
"the ninth and the last".

Every other language here that has the twenty-seven has them as the moon's stations counted once
round. **Divehi keeps the names and re-hangs them on the sun and the wind.** That is a sailor's
calendar — it answers when the season turns, not where the moon is — and it is why *Mūla*, an
unremarkable nineteenth in the Sanskrit list, is here **the hinge of the year**.

Two details complete it. The system was *administered*: **ނަކަތްޗާ *nakaiychaa***, "the nakaiy man",
was an office at the Sultan's palace — which is why a vernacular vocabulary can print Bayer
designations for all twenty-seven. And it was kept true to the sun by a twenty-eighth, **އަވިހި
*avihi***, a variable intercalary asterism now disused — **the only place in this database where a
vernacular calendar's leap mechanism is recorded.**

Minicoy (Maliku), Indian territory in Lakshadweep, speaks this language and uses this calendar.

### The Cholanaikkans have no constellations — and this is the control case for the whole database

The recorders say why in their first sentence: *"absence of farming activities made sky-watching a
never compelling affair"*. They are forest foragers of fewer than two hundred people in the Nilambur
reserves. They have two words for "star", *Koram* and *Udumbam*, and identify no star and no pattern
whatever — **shown the night sky in the Kozhikode planetarium, the party smiled and walked out.**
They do not know that the sun rises at different points through the year, and so do not connect it
with the seasons.

`tribal.json` already had Radcliffe-Brown's flat statement that constellations are not recognised in
the North Andaman, recorded as a result rather than a gap. Here the same result comes **with a cause
attached**, and it is the cause the rest of this compilation would predict: every figure in this
database that carries a story belongs to a community that plants something — the cot and the three
thieves, the plough with its two bullocks and its ploughman, the sowing-star, the threshing floor,
the seed drill, the Pleiades that say when to sow.

What they *do* have is a meteor, *Katui*, "embers of the fire sent by the gods" — and a meteor needs
no calendar.

### The fishermen's measures were not found, and that is the wave's real failure

The plan aimed at the fist-and-finger star-altitude systems reported for the Indian Ocean — *kai
kanakku* in Lakshadweep and Malabar, *viral kanakku* in Tamil Nadu, *dhru* in Gujarat. **The
lexicographic route does not reach them.** The Tamil Lexicon has கைக்கணக்கு only as a memorandum of
accounts and has no விரற்கணக்கு at all; its navigational vocabulary is generic (*mālumi* "pilot",
from the same Arabic *muʿallim* that names the Kutchi *mālam* manuals; *cukkāni* "helmsman";
*kānta-p-peṭṭi* "magnet box", the mariner's compass).

The one real find is **சங்கு *caṅku***, the gnomon that measures the sun's altitude by its shadow —
the classical instrument, not a rule of thumb, and the second entry in the *Measuring the sky*
object after Mizo *suk-chen*. The two are opposite methods: the Mizo hold a pestle up against the
sky and count its lengths; the Tamil plant a post and read its shadow.

A proper pass at the fist-measures needs the maritime literature — Tibbetts on Arab navigation, the
Kutchi *mālam* manuscripts — all of it in copyright and none of it reached.

### Peninsular tribal, largely dry again

Thurston's volume II was downloaded and searched for nine sky terms: **one hit, on "constellation",
with no star name** — confirming from a second volume what `tamil.json` found in the other six. No
Sora, Savara, Kui, Irula, Kurumba, Chenchu or Koya source could be obtained; the identifiers tried
on archive.org returned empty metadata and none of those languages is on DSAL.

### An editorial decision worth flagging

**Only seven of the twenty-seven *nakaiy* are entered.** Maniku gives all twenty-seven and this file
could have listed them — but `FORMAT.md`'s opening argument is that a table of the inherited asterism
names in one more language would be "large, easy to compile, and nearly uninformative". What is
informative is the *system*, and the members whose position in it is structurally interesting. The
other twenty are named in the *nakaiy* entry's usage note.

---

## 8. Wave 6 — the occupational and caste register. **Done, 2026-08-12.**

**777 names · 58 objects · 48 languages** (was 774 / 58 / 48). New file `sources/occupational.json`,
3 entries — and the `community` field, which is what this wave was really for.

### The occupational axis is almost unrecorded, and that is the result

The wave aimed at sky-names keyed to what people *do* rather than to what they speak —
pastoralists (Dhangar, Kuruba, Gujjar, Rabari, Bharvad, Golla), fishing castes, the Banjara outside
Vidarbha. I downloaded three of the largest folklore compendia of colonial India in full —
Enthoven's *Folklore of Bombay* (1924) and both volumes of Crooke's *Popular Religion and Folk-lore
of Northern India* (1896) — extracted every line containing a sky word with four lines of context
either side, and tested each against twenty occupational and caste terms.

**One line matched in three volumes, and it was a false positive.**

That is the same shape this database has met four times already: Russell & Hiralal yielded one
community with named figures in four volumes (the Dhuri), Thurston almost nothing in seven, Rose's
*Glossary* nothing in the volume obtained. **The colonial compendia record sky-lore by language and
by tribe, and essentially never by trade.** That is a fact about what folklorists collected, not a
claim that pastoralists and fishermen have no sky.

### And what the compendia do have had mostly been taken already

Enthoven's chapter on stars and planets was worked in an earlier pass — eight entries in
`marathi_gujarati.json` come from it, including the two best occupational items in the whole
database: **Gadli**, Rohiṇī and Kṛttikā together, "supposed to indicate the rise and fall in the
cotton-market" — the only commodity omen here — and the Konkan death-divination in which a man who
cannot make out the pole star, or in the other version Arundhatī, has six months to live.

Re-reading the chapter yielded three things it had missed:

- **The four maṇḍalas.** A meteor is read by which quarter of the sky it falls from: *Vāyu-maṇḍal*
  portends an epidemic, *Varuṇa-maṇḍal* is favourable to human happiness, *Indra-maṇḍal* threatens
  kings, *Agni-maṇḍal* threatens war between nations. A partition of the sky this database did not
  have — the vīthīs divide by the planets' road, the maṇḍalas by presiding deity, and they exist
  only to answer where a meteor came from. In the same passage is **the sharpest occupational split
  recorded anywhere here**: a meteor falling into the sea forebodes evil to the dwellers on earth
  generally, but *in the Kanara District* the same fall is held to promise rain. A coast that wants
  rain reads the omen the other way up.
- **Tārā-bāras**, the name of the rite of showing the pole star to a couple as soon as the marriage
  knot is tied — **the only name for a sky-*rite* in this database**, everything else here naming a
  star, a figure, a wind or a season.
- **Crooke on Mūla**, which corroborates a Wave 4 finding from 900 km away and 35 years earlier.
  Turner's Nepali has *mulyāhā*, "born under *mul*", meaning as a noun "an unfortunate person, an
  orphan". Crooke gives the social fact behind the word: the twenty-seven asterisms serve only to
  cast a marriage horoscope, and the one an ordinary cultivator must reckon with is the unlucky
  Mūla, because a son born under it needs an elaborate purification. An asterism that matters as a
  **social category** rather than as a season or a shape.

### The schema change (plan §11, item a)

This database is keyed on language while the question is partly about communities, and the mismatch
had already bitten: the Chhattisgarhi Dhuri entries in `tribal.json` had to be argued into a caveat
because the Dhuri are a caste, not a language. An **optional `community` field** is now part of the
schema — carried by the three new entries and back-filled onto the seven earlier ones that had a
community buried in their `region` string: the Dhuri rice-parchers of Chhattisgarh (3), the Deshasth
Brahmans of Dharwar, the Konda Dora of the Vizagapatam Agency, the Uppu Yerukala of the Telugu
country, and the Lingāyat cultivators of Bellary whose *kārte* rain-calendar Thurston recorded.

**Ten entries out of 777 carry a community, and that ratio is the finding restated.**

*(Item b of that section, `source_access`, is still open — see §12.)*

---

## 8b. The sub-waves — 1b, 2b, 3b, 4b, 5b. **Done, 2026-08-12.**

All five were blocked on getting hold of things rather than on reading them, and four of the five
came unblocked at once when the archive.org route found in Wave 4 was applied systematically: fetch
`archive.org/metadata/<id>` for the item's real server and directory, then request
`https://<server><dir>/<filename>` directly. **Every book this plan recorded as returning HTTP 503
was obtained this way.** The pass added 151 entries and nine languages, and the database now stands
at **928 names · 64 objects · 57 languages · 525 linked to the Sanskrit database**.

### 3b is the largest single pass in the database, and it should have been done first

Seventy-seven entries from six monographs that were sitting behind a redirect layer. Playfair on the
Garos, Hutton on the Angamis and the Semas, Mills on the Aos and the Rengmas, Parry on the Lakhers.
Four findings that only appear once the region is read together:

- **Orion's Belt is a carried load, and the carriers are always ambushed.** Sema
  *Phoghwosülesipfemi* three men carrying a roof-beam, Angami *Thepeko* three men carrying a
  house-post, Lakher *Vothawlapiapa* two men carrying a pig, Garo *Wak-ripe* the pig itself on a
  pole. In every case but the Garo the stars of the Sword are the enemies who ambushed them. The
  mainland's Orion is a plough or a yoke; the north-east's is a killing on a path. The Rengmas
  reverse the roles — the Belt is the ambush party and the Sword the travellers walking into it —
  which is the exception that shows the figure is understood and not merely inherited.
- **The Milky Way is a seasonal boundary, not a cattle road.** Ao *'cold-weather rains-divider'*,
  Lakher *Sonatachhiarari* 'rains and dry weather boundary', Mizo *Thlasik Kong* 'the cold weather
  road' — and the Lakhers say how it is read: by which side of the band has the larger expanse of
  empty sky. The exceptions all make it water — the Angami name it after the Barak river, the
  Rengmas after the Diyung and the Tulo, the Semas call it the river of souls.
- **No cot and no thieves.** The mainland's commonest figure does not cross the hills. In its place
  Ursa Major is a corpse: Lakher *Keulachongpa* is a man killed in a raid whose head and left leg his
  slayers carried off, and the Lusheis tell the same of *Zangkhua*. The Lakhers then explain the
  circumpolar circuit by a rule of funeral law — a man killed in war cannot cross the Kolodyne, so
  his stars turn back instead of completing their round. It is the only place in this database where
  an observed astronomical fact is explained by a point of ritual law.
- **The Garo sky is one story.** Fourteen names, and all but the two Venus names are episodes of a
  single funeral — the cremation of the moon's mother. Cassiopeia is the bearing of the body, Sirius
  the star that lit the pyre, the Pleiades the sacrificial cock, the Square of Pegasus the four posts
  of the pyre, Orion's Belt the pig brought as food, the Milky Way the hoofprints of the buffalo that
  bolted. No other tradition here organises its whole sky as one event.

The negatives are as sharp. **Mills says of the Aos that stars 'are too small and remote to interest
the Ao much, and none of the constellations seem to have names'** — the same author who recorded
twenty Rengma names in the next valley. His *Lhota Nagas* has no star vocabulary at all. Gurdon's
*The Khasis*, read end to end, has none either, so Khasi still rests on five words; and Endle's *The
Kacharis* has not one sky word, so **Bodo remains unattested**.

### 1b: the Pardhi are the exception to this database's rule about Orion

Thirty-three entries. The Pardhi paper (JAHH 22(1), 2019) was on ADS all along. What it gives is the
one community in the compilation still living by hunting and scavenging, and **the one Orion that is
a hunt** — three deer in the Belt, two hunting dogs in the Nebula, a Pardhi man at Rigel. Everywhere
else Orion is a plough, a yoke, a beam or a bedstead. The figure follows the economy and not the
language: Pardhi is Indo-Aryan and close to Bhili, and the Bhils, who farm, do not see this.
Alongside it: the Hyades as *Mangari*, a triangular bird-net whose design the authors say was
inspired by the star pattern — the only such case in their whole programme; the three trailing stars
of Ursa Major named twice over, once as three birds the tribe eats and once as three men identified
by surname and by the goddess each family worships; and a compass in which east and west come from
the sun, north from the hills and south from *rakshasbaku*, the demon's mouth.

**The Warli / Dhodia / Katkari / Kokna study appears never to have been published.** A public talk
abstract summarises it in English and gives one vernacular word; a web summary of a talk is not a
citable transcription and no entry rests on it. That is the whole of the remaining gap in the
programme, and it is recorded in `tribal_fieldwork.json`.

### 2b: Baloch answers when you ask in Sindhi, and Hassan does not answer at all

Eleven Sindhi entries. The *Jāmiʻ Sindhī lughāt* is monolingual, which is why Wave 2 got nothing out
of it: it was queried in English. Queried in Sindhi it gives the **northern cot** *autirīṅ khaṭ* for
Ursa Major — the westernmost attestation of the cot in the database, and one Mewaram does not have —
a named Sirius (*labhadhak*, Sanskrit Lubdhaka, which Wave 2 had recorded as absent), five names for
the Milky Way and not one of them a road, and the **Katī-and-Scorpion proverb**: the Pleiades are the
Scorpion's betrothed, and that is why the two are never in the sky together. An observational fact
about right ascension, carried as an engagement.

And a **third kind of DSAL gap**, to set beside the two this database already documents. Hassan's *A
Pronouncing Dictionary of Kashmiri Language* is listed *and linked*, and its search form is live —
and the database behind it is empty. Every query in Devanagari, Perso-Arabic and roman returns 'No
results', and `hassan_query.py?page=N` returns an empty frame for pages 1, 5, 50, 200 and 500.
Kashmiri still rests on Grierson 1932 alone.

Rose's *Glossary* volumes I and II were obtained and are all but dry, which settles the whole work.
Volume I yields one Punjabi Venus name, *wautián dá tára*, 'the wives' star' — a star that decides
when a bride may travel between her father's house and her husband's. Its comet name is **not**
entered: two independent scans of the same printing render it two different ways and neither is
legible.

### 4b: the Buddhist Himalaya is reachable and still unreadable

Jäschke 1881, Das 1902 and Atkinson's *Himalayan Gazetteer* were all obtained. The obstacle turns
out not to be access but OCR: the transliterated Tibetan is set with diacritics that both scans
destroy, so Jäschke's twenty-eight lunar mansions at *rgyu-skar* come out as an unreadable string,
and Das's Tibetan-script column is recognised into the wrong letters — *smin* is rendered *yin* at
the very entry that defines it. Two names survive because they recur identically across both
dictionaries and are entered; the rest is left unread rather than reconstructed, which is the
decision this database already made about the Korku paper's Greek letters and the Bhil paper's
cipher. Atkinson has no Kumaoni or Garhwali star-name in three volumes. **Garhwali, Ladakhi, Spiti,
Bhutia, Monpa, Sherpa and Lahuli remain entirely unattested.**

### 5b: the measures are still unreached, but Sora and Kui were not

*kai kanakku*, *viral kanakku* and *dhru* are where Wave 5 left them, and for the same reason. What
did open were two dictionaries this plan had assumed did not exist. **Sora** — the one Munda language
the database had nothing for — turns out to have a sixteen-name star list at Ramamurti's headword
*tuj-ən*, of which nine are glossed elsewhere in the book and are entered: the Pleiades as a crowd,
the fifth lunar mansion built on the verb *to plough*, both appearances of Venus, Jupiter twice over
with the lexicographer's own note that one of the two is 'due to the influence of the Oriya
astrologers', and Mars. **Kui** has exactly three sky words in Winfield's vocabulary and no
constellation at all.

### Two loose ends closed, and one correction

*Encyclopaedia Mundarica* and Bodding were re-fetched and turn out to add nothing: the *ipil* essay in
volume 7 and Bodding's Pleiades entries are already in `tribal.json` in full. What volume 6 does add
is Mundari using **Orion as a clock in ordinary speech** — *araṛ ipilko hāṛeṇnate*, 'the marriage
guests arrived about two hours after Orion had crossed the meridian'. **Elwin was misfiled as in
copyright by this plan and is not**: he died in February 1964, so the Indian term expired on 1
January 2025, and *The Baiga* is quoted verbatim. It yields fifteen figures, of which Elwin locates
almost none — eleven entries are `unidentified`, the largest such block in the database — including
the best-explained death-cot anywhere in it: Ursa Major is the bier, the Baiga smash the bier with
axes after a burial, and the splinters are the rest of the stars.

---

## 9. Resource classes to sweep

### A. Lexicography
DSAL (inventory in §2) is the spine. Beyond it:
- **CDIAL** and **DEDR** to trace whether a vernacular name is inherited or coined.
- Missing families have no DSAL dictionary at all — Munda, Kurukh, Gondi, Bhili, Khasi, Andamanese,
  most Tibeto-Burman. For these go to the individual works: Hoffmann's *Encyclopaedia Mundarica*,
  Bodding's *Santal Dictionary*, Grignard's *Kurukh*, Burrows' *Ho*, Nissor Singh's *Khasi*,
  Lorrain & Savidge, Whitehead's *Car-Nicobarese*, Man's *Andamanese*, plus mission dictionaries for
  Garo (Mason/Ramkhe), Bodo (Endle), Ao (Clark), Angami (McCabe), Mizo (Lorrain).

### B. Colonial ethnography — greppable full text on archive.org
- **Sarat Chandra Roy**: *The Oraons*, *The Mundas and their Country*, *The Birhors*, *The Kharias*,
  *The Hill Bhuiyas*. Roy is the most likely PD source of substantial Adivasi sky material not yet
  read, and he founded *Man in India*.
- Dalton, *Descriptive Ethnology of Bengal* (1872).
- Crooke, *Tribes and Castes of the NWP & Oudh* (4 vols) and *Popular Religion and Folklore of
  Northern India* — the latter is organised by belief and is the right shape for this.
- Enthoven, *Tribes and Castes of Bombay* (3 vols), *Folklore of Bombay*.
- Risley, *Tribes and Castes of Bengal*.
- Ananthakrishna Iyer, *Cochin Tribes and Castes*, *Mysore Tribes and Castes*.
- Rose, *Glossary of the Tribes and Castes of the Punjab and NWFP* (3 vols) — the north-west gap.
- Thurston (already grepped, dry for Tamil vernacular names, but re-check for Telugu/Kannada tribes).
- North-east: Hutton (*Angami*, *Sema*), Mills (*Ao*, *Lotha*, *Rengma*), Playfair (*The Garos*),
  J. Shakespear (*Lushei-Kuki Clans*), Endle (*The Kacharis*), Gurdon (*The Khasis*, already dry).
- Himalaya: Atkinson, *Himalayan Gazetteer*; Traill's Kumaon reports; Sherring, *Western Tibet*.

Note the pattern from the work already done: caste-and-tribe compendia are mostly dry, and when they
yield, they yield one community in four volumes (the Dhuri). Budget accordingly — these are grep
targets, not read targets.

### C. Serials
*Man in India* (1921– ; the Bhaduri Munda star-name paper), *Indian Antiquary* (1872–1933, PD),
*Journal of the Asiatic Society of Bengal* (flagged unsearched), *Folklore*, *Journal of the Bombay
Natural History Society* (seasonal notes), *Bulletin of the Anthropological Survey of India*,
*Indian Journal of History of Science*, state Tribal Research Institute bulletins (MP, Jharkhand,
Odisha, Chhattisgarh, Maharashtra).

### D. Agricultural and calendrical
This is where vernacular star names actually live — the existing files found Telugu *kārte*, Tamil
*nāḷ*, Hindi *Hathiyā rāni*, Malayalam *ñēṅṅōl* all through farming use, not astronomy.
- Ghāgh & Bhaḍḍarī weather proverbs (printed collections; Grierson's *Bihar Peasant Life* used).
- Provincial and district gazetteers — Bombay, Central Provinces, Madras, Punjab, NWFP series.
  (Bengal and Assam were downloaded and grepped: one astronomical sentence in 22 volumes. Do not
  repeat that experiment blind — sample two volumes before committing to a series.)
- Regional almanacs/pañcāṅgs, whose seasonal tables often print folk names beside the Sanskrit.

### E. Maritime and navigational — completely untouched
The existing Kerala file records a flat negative: no navigational star name in any PD Kerala source.
That negative is probably about the *sources*, not the practice.
- The fist-and-finger altitude systems: *kai kanakku* (Lakshadweep, Malabar), *viral kanakku* (Tamil
  Nadu), *dhru* (Gujarat/Kutch); working units *pidi*, *kōl*, *tāmbu/kayiru*.
- Kutchi *mālam* navigation manuals; the Arab-Indian Ocean tradition via Ibn Mājid and
  Sulaymān al-Mahrī (Tibbetts' edition is in copyright — paraphrase).
- Divehi (Maniku 2000) as the Lakshadweep-adjacent lexicon.
- Fisher-community lore: Konkan, Malabar, Coromandel, Odisha, Sundarbans.

### F. Repositories
DSAL · archive.org full-text · Digital Library of India · Panjab Digital Library ·
**Shodhganga** (Indian PhD theses — the largest untapped body of folklore fieldwork, much of it on
single communities) · SOAS/ELAR and DoBeS endangered-language archives · Anthropological Survey of
India *People of India* (43 vols, copyright — use as an index of communities to chase, not a quote
source) · IGRMS publications.

---

## 10. Waves

Each wave produces one or two new `sources/*.json`, added to `FILES` in `merge.py`, with new sky
objects given rules in `canon.py` and positions in `build_chart.py`.

| Wave | Scope | Chief resources | Rough yield |
|---|---|---|---|
| ~~**0**~~ | ~~Correction pass~~ | **Done 2026-08-12** — see §2 | +7 Rajasthani; 1 claim retracted, 2 upheld, Tamil negatives strengthened |
| ~~**1**~~ | ~~Central & Western Adivasi~~ | **Done 2026-08-12** — see §3 | +113 entries, 11 new communities, all `tribal` |
| ~~**1b**~~ | ~~The rest of the field-survey programme~~ | **Done 2026-08-12** — see §8b | +33 Pardhi. Cholanaikkan was closed in Wave 5; the Warli study appears never to have been published |
| ~~**2**~~ | ~~North-west~~ | **Done 2026-08-12** — see §4 | +45 entries: Sindhi 23, Kashmiri 18, Rajasthani finished with 4 |
| ~~**2b**~~ | ~~North-west, unfinished~~ | **Done 2026-08-12** — see §8b | +11 Sindhi, +1 Punjabi. Baloch answers when asked in Sindhi; Hassan's Kashmiri is a live search form over an empty database; Rose I–II are dry |
| ~~**3**~~ | ~~North-east~~ | **Done 2026-08-12** — see §5 | +44 entries: Mizo 36, Meitei 7, Mara 1. Not thin — the richest single pass yet |
| ~~**3b**~~ | ~~North-east, unfinished~~ | **Done 2026-08-12** — see §8b | **+77, the largest single pass in the database.** Garo 18, Mara 18, Rengma 16, Angami 10, Sema 10, Ao 4, Mizo 2. Lhota, Khasi and Bodo are dry and now demonstrably so |
| ~~**4**~~ | ~~Himalaya~~ | **Done 2026-08-12** — see §6 | +25 entries: Nepali 14, Newar 9, Kumaoni 2 |
| ~~**4b**~~ | ~~The Buddhist Himalaya, unreached~~ | **Done 2026-08-12** — see §8b | +2 Tibetan, and a negative with a new cause: the books were obtained and their transliteration does not survive OCR. Atkinson is dry |
| ~~**5**~~ | ~~Peninsular tribal & maritime~~ | **Done 2026-08-12** — see §7 | +18 entries: Divehi 13, Cholanaikkan 5 (one being the wave's best result), Tamil 1 |
| ~~**5b**~~ | ~~The fishermen's measures~~ | **Partly done 2026-08-12** — see §8b | +9 Sora, +3 Kui, from dictionaries that turned out to exist. The measures themselves are still unreached and the reason has not changed |
| ~~**6**~~ | ~~Occupational & caste registers~~ | **Done 2026-08-12** — see §8 | +3 entries, and the `community` field added to the schema. The wave's result is a **negative**: the colonial compendia record sky-lore by language and by tribe, essentially never by trade |

Order is deliberate. Wave 0 is nearly free. Wave 1 has the best yield-per-hour and the material is
already digitised. Waves 3–4 are the ones most likely to come back thin, and thin is a publishable
result here, but do them after the wins are banked.

---

## 11. Loose ends already flagged, folded in

**Mostly closed, 2026-08-12.** *Encyclopaedia Mundarica* volumes 1, 2, 4, 6, 7, 8 and 10 and
Bodding volume 5 were obtained and add nothing the database did not already have from them, except
one Mundari idiom recorded in §8b. **Elwin's *Baiga* is done and quoted** — he was misfiled here as
in copyright and is not; his *Muria and their Ghotul* was read and has no star vocabulary beyond one
reference to the twenty-seven nakshatras.

Still open, and now the whole of §11: Bodding's *Santal Dictionary* vols 1–4, which archive.org does
not appear to hold under any identifier that resolves; *Encyclopaedia Mundarica* vols 3, 5, 9 and
11–16; the *Journal of the Asiatic Society of Bengal*; Bhaduri's Munda star-names paper in *Man in
India*; and Date's `(कुण.)` abbreviation, which still needs the un-OCRed front matter of the
*Mahārāṣṭra Śabdakośa*.

---

## 12. Two schema changes this needs

**a. `community` alongside `language`. — DONE in Wave 6, see §8.** The database is keyed on language, but the user's question
is about cultures. These are not the same axis and the mismatch already bit once: the Chhattisgarhi
Dhuri entries had to be argued into a caveat because the Dhuri are a caste, not a language. Waves 1,
5 and 6 are all community-keyed. Add an optional `community` field (ethnonym as the source gives it)
and let `language` mean only the language of the name.

**b. `source_access`. — DONE, 2026-08-12.** Added to all 928 entries: `public-domain` (693) ·
`in-copyright-paraphrased` (235) · `not-obtained` (0). The premise turned out to be half wrong, and
the half that was wrong is the more interesting one. `quote: null` never did mean 'could not be
obtained', because **nothing is ever entered from a source that was not read** — an unobtained source
produces a line in `summary_findings`, not a row with an empty quote. So `not-obtained` is defined
in order to stay empty, and `merge.py` now *asserts* the whole invariant: a quote exists if and only
if `source_access` is `public-domain`. What was a convention maintained by care is now a build
failure if it is broken.

**c. A fifth `register` value — decided against, 2026-08-12.** Wave 5 was to force the question and
did not: the Divehi monsoon calendar sits under the existing values without strain. `tribal` is now
carrying 387 of 928 names across Munda, Dravidian, Tibeto-Burman, Austroasiatic and Indo-Aryan
traditions, which is a lot of weight — but splitting it by family would duplicate `language`, and
splitting it by mode of life would make the register a claim about the speakers rather than about
the name, which is exactly what the field is documented not to be. The 387 are separable already, by
family through `build_matrix.py` and by community through `community`. Left as it stands.

---

## 13. Two decisions still open

**Scope. — SETTLED IN PRACTICE, 2026-08-12; still worth stating explicitly in `FORMAT.md`.** The
sub-waves settled this by acting on the recommendation rather than by arguing it. The database now
carries Tibetan, whose only use is to speak for Ladakh, Spiti and Sikkim, which have no lexicography
of their own; Mara and Mizo, whose sources are as much about the Chin Hills as about Mizoram; and
Divehi, which reaches India through Minicoy. Every one of them earns its place by illuminating an
Indian community that cannot be reached directly. **The database is South Asian; the app, if it ever
consumes this, should filter.** What remains is to say so in `FORMAT.md`, which still does not.

**Whether any of this reaches the app.** Today it does not: `FORMAT.md` states plainly that nothing
under `star-names-local/` feeds the app, which reads `docs/star-names/star-names.json` into
`catalogs/starinfo.pb`. A survey this size changes the argument. Options, in ascending cost:
show local names on the star detail sheet when the device locale matches; a "local names" toggle
listing every recorded name for a star; or a full second name layer. This plan does not assume any
of them — but the schema decisions in §7 are cheaper to make now than after 500 more entries.

---

## 14. What "done" looks like

Not "all cultures of India" — that is not reachable and claiming it would be the one thing this
database has so far avoided. Done is:

- every language family of South Asia represented or explicitly recorded as dry,
- every community for which a citable star-name source exists in a searched resource, entered,
- `coverage-matrix.html` readable as a map of *the literature*, with the empty cells honestly
  meaning "no source found" and each backed by a named search in `summary_findings`.

The negative findings are half the value. A file that says *Radcliffe-Brown found no constellations
in the North Andaman, and here is where he says it* is worth more than one that quietly omits the
Andamans.

### Where that stands, 2026-08-12

The first test is now met for every family the plan set out to reach. **Indo-Aryan, Dravidian,
Munda, Tibeto-Burman, Austroasiatic, Andamanese and the Maldivian branch are all represented**, and
the four languages that were read and found dry — Lhota, Khasi beyond five words, Bodo, Kumaoni past
two entries — each say so in a `summary_findings` with the book and the search named. The second is
met for every source this plan named. The third is what `coverage-matrix.html` now is.

**What is left is not a wave.** It is the next order of work, and it is a different kind of thing:

1. **The measures.** *kai kanakku*, *viral kanakku*, *dhru*, and the Mizo *suk-chen* that stands
   alone in the database as a native angular unit. Not lexicographic; they need the maritime
   literature and the Kutchi *mālam* manuscripts, and none of it is digitised.
2. **The Buddhist Himalaya, again, from clean text.** The books are in hand and the OCR defeats
   them. This wants a modern digital Jäschke or a Ladakhi dictionary, not another download.
3. **Fieldwork that exists but is not published.** The Warli / Dhodia / Katkari / Kokna survey is
   the clear case: it was done, it was presented, and there is nothing citable. Writing to the
   authors would close it, which no amount of searching will.
4. **The rest of the Naga languages, and Bodo, from mission dictionaries** that are on neither DSAL
   nor archive.org, and which exist chiefly in Shillong and Guwahati.

None of these is reachable the way the first eleven waves were reachable — by finding the right
book and reading it carefully. That, rather than any count, is the sense in which this plan is
finished.
