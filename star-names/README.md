# Sanskrit Star Names — Source Database

Authentic references to star names in Sanskrit texts: the original shloka (copied verbatim from online e-texts), a published translation, and the modern identification of each star.

*Generated 2026-07-24. Machine-readable version: [`star-names.json`](star-names.json); per-source research files with full caveats: [`sources/`](sources/).*

**Method.** Compiled from primary Sanskrit e-texts (Sanskrit Wikisource, GRETIL) and public-domain translations (Burgess 1860, Iyer 1884, Keith 1914/1920, Eggeling 1882, Oldenberg 1886, Whitney 1905, Wilkinson & Sastri 1861, Tawney 1880). Devanagari copied verbatim from the cited e-texts; no verse was reconstructed from memory. Copyrighted translations (Bhat 1981, Arkasomayaji, Dumont 1954) are paraphrased and cited, never quoted.

**A note on what the texts actually say.** The Vedic texts name asterisms and deities but never coordinates; the siddhāntas give coordinates for a single junction star (yogatārā) per nakshatra. All modern equations therefore rest on the siddhāntic positions (chiefly as analysed by Burgess 1860) and on continuous tradition; the *confidence* column records where that chain is strong and where it is disputed.

## Summary table

| Sanskrit | IAST | Modern star | Bayer | Confidence | Attested in |
|---|---|---|---|---|---|
| [अश्विनी](#अश्विनी-aśvinī--sheratan) | Aśvinī | Sheratan | β Arietis | certain | Sūrya Siddhānta |
| [भरणी](#भरणी-bharaṇī--35-arietis-musca-borealis) | Bharaṇī | 35 Arietis (Musca Borealis) | 35 Arietis | disputed | Sūrya Siddhānta |
| [कृत्तिका](#कृत्तिका-kṛttikā--alcyone-pleiades) | Kṛttikā | Alcyone (Pleiades) | η Tauri | certain | Sūrya Siddhānta; Vedic corpus |
| [रोहिणी](#रोहिणी-rohiṇī--aldebaran) | Rohiṇī | Aldebaran | α Tauri | certain | Sūrya Siddhānta; Vedic corpus |
| [मृगशीर्ष](#मृगशीर्ष-mṛgaśīrṣa--meissa) | Mṛgaśīrṣa | Meissa | λ Orionis | certain | Sūrya Siddhānta; Vedic corpus |
| [आर्द्रा](#आर्द्रा-ārdrā--betelgeuse) | Ārdrā | Betelgeuse | α Orionis | disputed | Sūrya Siddhānta; Vedic corpus |
| [पुनर्वसु](#पुनर्वसु-punarvasu--pollux) | Punarvasu | Pollux | β Geminorum | certain | Sūrya Siddhānta |
| [पुष्य](#पुष्य-puṣya--asellus-australis) | Puṣya | Asellus Australis | δ Cancri | likely | Sūrya Siddhānta; Vedic corpus |
| [आश्लेषा](#आश्लेषा-āśleṣā--ashlesha) | Āśleṣā | Ashlesha | ε Hydrae | disputed | Sūrya Siddhānta |
| [मघा](#मघा-maghā--regulus) | Maghā | Regulus | α Leonis | certain | Sūrya Siddhānta |
| [पूर्वफल्गुनी](#पूर्वफल्गुनी-pūrva-phalgunī--zosma) | Pūrva-Phalgunī | Zosma | δ Leonis | likely | Sūrya Siddhānta |
| [उत्तरफल्गुनी](#उत्तरफल्गुनी-uttara-phalgunī--denebola) | Uttara-Phalgunī | Denebola | β Leonis | certain | Sūrya Siddhānta |
| [हस्त](#हस्त-hasta--gienah) | Hasta | Gienah | γ Corvi | disputed | Sūrya Siddhānta |
| [चित्रा](#चित्रा-citrā--spica) | Citrā | Spica | α Virginis | certain | Sūrya Siddhānta |
| [स्वाती](#स्वाती-svātī--arcturus) | Svātī | Arcturus | α Boötis | certain | Sūrya Siddhānta |
| [विशाखा](#विशाखा-viśākhā--ι-librae) | Viśākhā | ι Librae | ι Librae | disputed | Sūrya Siddhānta |
| [अनुराधा](#अनुराधा-anurādhā--dschubba) | Anurādhā | Dschubba | δ Scorpii | certain | Sūrya Siddhānta |
| [ज्येष्ठा](#ज्येष्ठा-jyeṣṭhā--antares) | Jyeṣṭhā | Antares | α Scorpii | certain | Sūrya Siddhānta |
| [मूल](#मूल-mūla--shaula) | Mūla | Shaula | λ Scorpii | likely | Sūrya Siddhānta |
| [पूर्वाषाढा](#पूर्वाषाढा-pūrvāṣāḍhā--kaus-media) | Pūrvāṣāḍhā | Kaus Media | δ Sagittarii | certain | Sūrya Siddhānta |
| [उत्तराषाढा](#उत्तराषाढा-uttarāṣāḍhā--nunki) | Uttarāṣāḍhā | Nunki | σ Sagittarii | likely | Sūrya Siddhānta |
| [अभिजित्](#अभिजित्-abhijit--vega) | Abhijit | Vega | α Lyrae | certain | Siddhānta Śiromaṇi; Sūrya Siddhānta |
| [श्रवण](#श्रवण-śravaṇa--altair) | Śravaṇa | Altair | α Aquilae | certain | Sūrya Siddhānta |
| [श्रविष्ठा](#श्रविष्ठा-śraviṣṭhā-dhaniṣṭhā--rotanev) | Śraviṣṭhā (Dhaniṣṭhā) | Rotanev | β Delphini | certain | Sūrya Siddhānta |
| [शतभिषज्](#शतभिषज्-śatabhiṣaj--hydor) | Śatabhiṣaj | Hydor | λ Aquarii | likely | Sūrya Siddhānta |
| [पूर्वभाद्रपदा](#पूर्वभाद्रपदा-pūrva-bhādrapadā--markab) | Pūrva-Bhādrapadā | Markab | α Pegasi | certain | Sūrya Siddhānta |
| [उत्तरभाद्रपदा](#उत्तरभाद्रपदा-uttara-bhādrapadā--algenib--alpheratz) | Uttara-Bhādrapadā | Algenib / Alpheratz | γ Pegasi / α Andromedae | disputed | Sūrya Siddhānta |
| [रेवती](#रेवती-revatī--revati) | Revatī | Revati | ζ Piscium | likely | Siddhānta Śiromaṇi; Sūrya Siddhānta |
| [अगस्त्य](#अगस्त्य-agastya--canopus) | Agastya | Canopus | α Carinae | certain | Bṛhat Saṃhitā; Siddhānta Śiromaṇi; Sūrya Siddhānta |
| [मृगव्याध](#मृगव्याध-mṛgavyādha--sirius) | Mṛgavyādha | Sirius | α Canis Majoris | likely | Sūrya Siddhānta; Vedic corpus |
| [लुब्धक](#लुब्धक-lubdhaka--sirius) | Lubdhaka | Sirius | α Canis Majoris | certain | Bṛhat Saṃhitā; Siddhānta Śiromaṇi |
| [अग्नि](#अग्नि-हुतभुज्-agni-hutabhuj--elnath) | Agni (Hutabhuj) | Elnath | β Tauri | certain | Sūrya Siddhānta |
| [ब्रह्महृदय](#ब्रह्महृदय-brahmahṛdaya--capella) | Brahmahṛdaya | Capella | α Aurigae | certain | Sūrya Siddhānta |
| [प्रजापति](#प्रजापति-prajāpati--prijipati) | Prajāpati | Prijipati | δ Aurigae | likely | Sūrya Siddhānta |
| [अपांवत्स](#अपांवत्स-apāṃvatsa--θ-virginis) | Apāṃvatsa | θ Virginis | θ Virginis | likely | Sūrya Siddhānta |
| [आपस्](#आपस्-आपः-āpas--minelauva-auva) | Āpas | Minelauva (Auva) | δ Virginis | certain | Sūrya Siddhānta |
| [ध्रुवः](#ध्रुवः-dhruva--polaris-the-pole-star) | Dhruva | Polaris (the pole star) | α Ursae Minoris | disputed | Vedic corpus |
| [सप्तर्षयः / ऋक्षाः](#सप्तर्षयः--ऋक्षाः-saptarṣayaḥ--ṛkṣāḥ--the-big-dipper---seven-bright-stars-of-ursa-major-dubhe-merak-phecda-megrez-alioth-mizar-alkaid) | Saptarṣayaḥ / Ṛkṣāḥ | the Big Dipper - seven bright stars of Ursa Major (Dubhe, Merak, Phecda, Megrez, Alioth, Mizar, Alkaid) | α, β, γ, δ, ε, ζ, η Ursae Majoris | certain | Vedic corpus |
| [मरीचि](#मरीचि-marīci--alkaid-benetnash) | Marīci | Alkaid (Benetnash) | η Ursae Majoris | likely | Bṛhat Saṃhitā |
| [वसिष्ठ](#वसिष्ठ-vasiṣṭha--mizar) | Vasiṣṭha | Mizar | ζ Ursae Majoris | certain | Bṛhat Saṃhitā |
| [अङ्गिरस्](#अङ्गिरस्-aṅgiras--alioth) | Aṅgiras | Alioth | ε Ursae Majoris | likely | Bṛhat Saṃhitā |
| [अत्रि](#अत्रि-atri--megrez) | Atri | Megrez | δ Ursae Majoris | likely | Bṛhat Saṃhitā |
| [पुलस्त्य](#पुलस्त्य-pulastya--phecda) | Pulastya | Phecda | γ Ursae Majoris | likely | Bṛhat Saṃhitā |
| [पुलह](#पुलह-pulaha--merak) | Pulaha | Merak | β Ursae Majoris | likely | Bṛhat Saṃhitā |
| [क्रतु](#क्रतु-kratu--dubhe) | Kratu | Dubhe | α Ursae Majoris | likely | Bṛhat Saṃhitā |
| [अरुन्धती](#अरुन्धती-arundhatī--alcor-the-faint-companion-of-mizar-in-the-big-dippers-handle) | Arundhatī | Alcor, the faint companion of Mizar in the Big Dipper's handle | 80 Ursae Majoris | certain | Bṛhat Saṃhitā; Vedic corpus |
| [अम्बा](#अम्बा-दुला-नितत्नी-अभ्रयन्ती-मेघयन्ती-वर्षयन्ती-चुपुणीका-ambā-dulā-nitatnī-abhrayantī-meghayantī-varṣayantī-cupuṇīkā--the-seven-individual-stars-of-the-pleiades) | Ambā, Dulā, Nitatnī, Abhrayantī, Meghayantī, Varṣayantī, Cupuṇīkā | the seven individual stars of the Pleiades | brightest members: η, 27, 17, 20, 23, 19, 28 Tauri (no secure one-to-one mapping) | likely | Vedic corpus |
| [रोहिणी](#रोहिणी-द्वितीया--ज्येष्ठा-rohiṇī-second--jyeṣṭhā--antares) | Rohiṇī (second; = Jyeṣṭhā) | Antares | α Scorpii | likely | Vedic corpus |
| [इन्वकाः](#इन्वकाः-इन्वगाः-invakāḥ-invagāḥ--alternative-taittirīya-name-of-mṛgaśīrṣa---the-stars-of-orions-head) | Invakāḥ (Invagāḥ) | alternative Taittirīya name of Mṛgaśīrṣa - the stars of Orion's head | λ, φ1, φ2 Orionis | likely | Vedic corpus |
| [बाहू](#बाहू-रुद्रस्य-bāhū-rudrasya--the-two-arms-of-the-deerorion-usually-taken-as-betelgeuse-and-bellatrix) | Bāhū (Rudrasya) | 'the two Arms' of the deer/Orion: usually taken as Betelgeuse and Bellatrix | α Orionis and γ Orionis | disputed | Vedic corpus |
| [तिष्यः](#तिष्यः-tiṣya--the-later-puṣya-the-asellus-stars-and-praesepe-region) | Tiṣya | the later Puṣya: the Asellus stars and Praesepe region | γ, δ, θ Cancri (δ Cancri = Asellus Australis nearest the ecliptic), with the Praesepe cluster M44 | likely | Vedic corpus |
| [मृगः](#मृगः-प्रजापतिः-mṛga-prajāpati--the-celestial-deer--orion) | Mṛga (Prajāpati) | the celestial deer = Orion | constellation Orion (head λ Ori; body the Belt region) | likely | Vedic corpus |
| [इषुस्त्रिकाण्डा](#इषुस्त्रिकाण्डा-iṣus-trikāṇḍā--orions-belt---mintaka-alnilam-alnitak---as-the-three-jointed-arrow) | Iṣus trikāṇḍā | Orion's Belt - Mintaka, Alnilam, Alnitak - as the 'three-jointed arrow' | δ, ε, ζ Orionis | likely | Vedic corpus |
| [अश्विन्यादीनां साभिजितां योगताराः](#अश्विन्यादीनां-साभिजितां-योगताराः-aśvinyādi-yogatārāḥ-sābhijit--collective-catalog-of-28-junction-stars) | Aśvinyādi yogatārāḥ (sābhijit) | collective catalog of 28 junction stars | various | likely | Siddhānta Śiromaṇi |

## A finding about the Āryabhaṭīya

The Āryabhaṭīya names NO individual stars. Evidence: (1) W.E. Clark's complete 1930 translation (full text fetched from https://archive.org/stream/in.ernet.dli.2015.61416/2015.61416.The-Aryabhatiya-Of-Aryabhata_djvu.txt) was searched for Agastya, Canopus, Sirius, Dhruva, 'pole star', and all 27 nakshatra names — zero hits; the index lists only generic 'Asterisms'. (2) The complete Sanskrit text of all four padas on sa.wikisource (https://sa.wikisource.org/wiki/गोल-पाद , /दश-गीतिका-पाद , /गणित-पाद , /काल-क्रिया-पाद) was searched for अगस्त्य, ध्रुव, सप्तर्षि and nakshatra names — zero hits. The Gola-pada speaks only generically of the asterisms: verse 4.9 'अचलानि भानि तद्-वत् सम-पश्चिम-गानि लङ्कायाम्' — Clark: 'just so at Lanka a man sees the stationary asterisms moving backward (westward) in a straight line'; 4.10 refers to the भ-पञ्जर ('cage of the asterisms'); Clark: 'the circle of the asterisms, together with the planets, driven by the provector wind, constantly moves straight westward at Lanka'. Gola 11-12 and 16-17 place the gods on Meru at the north pole (Clark: 'The gods, who dwell in the north on Meru, see the northern half of the sphere of the asterisms moving from left to right') but name no pole star — the word Dhruva does not occur anywhere in the text. There is no yogatārā catalog and no verse about any individual star; the Daśagītikā gives only revolution counts of 'the asterisms' as a whole.

## The 28 nakshatra junction stars (yogatārā)

Sūrya Siddhānta ch. 8 defines each nakshatra's junction star by polar coordinates and by rules (vv. 16–19) naming which member of the group is the yogatārā. Vedic attestations are added where found.

### अश्विनी (Aśvinī) — Sheratan

**Modern identification:** Sheratan — β Arietis, Aries (*certain*)

**Sūrya Siddhānta 8.16 (also 8.5, 8.9)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> फाल्गुन्योर् भाद्रपदयोस् तथैवाषाढयोर् द्वयोः / विशाखाश्विनिसौम्यानाम् योगतारोत्तरा स्मृता //
>
> — *16. Of the two Phalgunis, the two Bhadrapadas, and likewise the two Ashadhas, of Viçakha, Açvini, and Mrgaçirsha (saumya), the junction-star (yogatara) is stated to be the northern (uttara):*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: the northern of the pair β and γ Arietis; 'this is the star β Arietis (magn. 3.2), and not α Arietis (magn. 2), as assumed by Colebrooke', shown by comparison of longitudes.</sub>

### भरणी (Bharaṇī) — 35 Arietis (Musca Borealis)

**Modern identification:** 35 Arietis (Musca Borealis) — 35 Arietis, Aries (*disputed*)

**Sūrya Siddhānta 8.18** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> ज्येष्ठाश्रवणमैत्राणाम् बार्हस्पत्यस्य मध्यमा / भरण्याग्नेयपित्र्याणाम् रेवत्याश् चैव दक्षिणा //
>
> — *18. Of Jyeshtha, Çravana, Anuradha (maitra), and Pushya (barhaspatya), it is the middle star: of Bharani, Krttika (agneya), and Magha (pitrya), and likewise of Revati, it is the southern:*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Group = 35, 39, 41 Arietis (obsolete Musca Borealis). Burgess: the 'southern' designation is ambiguous; 41 Ari (brighter, nearer ecliptic) 'would seem more likely', but 'the defined position, however, agrees better with 35', which he adopts. Many modern lists prefer 41 Arietis.</sub>

### कृत्तिका (Kṛttikā) — Alcyone (Pleiades)

**Modern identification:** Alcyone (Pleiades) — η Tauri, Taurus (*certain*)

*See also:* `krittika-seven`

**Sūrya Siddhānta 8.18** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> ज्येष्ठाश्रवणमैत्राणाम् बार्हस्पत्यस्य मध्यमा / भरण्याग्नेयपित्र्याणाम् रेवत्याश् चैव दक्षिणा //
>
> — *18. Of Jyeshtha, Çravana, Anuradha (maitra), and Pushya (barhaspatya), it is the middle star: of Bharani, Krttika (agneya), and Magha (pitrya), and likewise of Revati, it is the southern:*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: if 'southern' (v. 18) were strict it would be Atlas (27 Tau) or Merope (23 Tau), but 'the defined position agrees best with Alcyone, nor can we hesitate to regard this as actually the junction-star'.</sub>

**Taittirīya Saṃhitā 4.4.10.1** — [Sanskrit e-text](https://sa.wikisource.org/wiki/तैत्तिरीयसंहिता(विस्वरः)

> कृत्तिका नक्षत्रम् अग्निर् देवताऽग्ने रुचः स्थ प्रजापतेर् धातुः सोमस्यर्चे त्वा रुचे त्वा द्युते त्वा भासे त्वा ज्योतिषे त्वा रोहिणी नक्षत्रम् प्रजापतिर् देवता मृगशीर्षं नक्षत्रꣳ सोमो देवताऽऽर्द्रा नक्षत्रꣳ रुद्रो देवता पुनर्वसू नक्षत्रम् अदितिर् देवता तिष्यो नक्षत्रम् बृहस्पतिर् देवताऽऽश्रेषा नक्षत्रꣳ सर्पा देवता मघा नक्षत्रम् पितरो देवता
>
> — *(Thou art) Krttikas, the Naksatra, Agni, the deity; ye are the radiances of Agni, of Prajapati, of the creator, of Soma; to the Re thee, to radiance thee, to the shining thee, to the blaze thee, to the light thee. (Thou art) Rohini the Naksatra, Prajapati the deity; Mrgaçirsa the Naksatra, Soma the deity; Ardra the Naksatra, Rudra the deity; the two Punarvasus the Naksatra, Aditi the deity; Tisya the Naksatra, Brhaspati the deity; the Açresas the Naksatra, the serpents the deity; the Maghas the Naksatra, the fathers the deity.*
> <br>— A.B. Keith, The Veda of the Black Yajus School (1914) ([source](https://www.sacred-texts.com/hin/yv/yv04.htm) · [mirror](https://web.archive.org/web/20210301091213/https://www.sacred-texts.com/hin/yv/yv04.htm))

<sub>**Identification notes (Vedic corpus):** Heads the oldest nakshatra list; deity Agni. Universally identified with the Pleiades. Eggeling and Whitney both gloss Krittikas = Pleiades. Also attested TB 1.5.1.1 ('agneḥ kṛttikāḥ'), TB 3.1.1.1, ŚB 2.1.2.1-5, AV 19.7.2.</sub>

**Śatapatha Brāhmaṇa 2.1.2.3** — [Sanskrit e-text](https://sa.wikisource.org/wiki/शतपथब्राह्मणम्/काण्डम्_२/अध्यायः_१/ब्राह्मण_२)

> एता ह वै प्राच्यै दिशो न च्यवन्ते । सर्वाणि ह वा अन्यानि नक्षत्राणि प्राच्यै दिशश्च्यवन्ते तत्प्राच्यामेवास्यैतद्दिश्याहितौ भवतस्तस्मात्कृत्तिकास्वादधीत - २.१.२.३
>
> — *And again, they do not move away from the eastern quarter, whilst the other asterisms do move from the eastern quarter. Thus his (two fires) are established in the eastern quarter: for this reason he may set up his fires under the Krittikas.*
> <br>— Julius Eggeling, SBE vol. 12 (1882) ([source](https://www.sacred-texts.com/hin/sbr/sbe12/sbe1241.htm) · [mirror](https://web.archive.org/web/20210506123309/https://www.sacred-texts.com/hin/sbr/sbe12/sbe1241.htm))

<sub>**Identification notes (Vedic corpus):** The famous archaeoastronomical passage: the Krittikas 'do not swerve from the eastern quarter'. The Pleiades rose due east (on the celestial equator) c. 3000-2500 BCE, which S.B. Dikshit (1895) used to date the ŚB; the dating argument (not the star identification) is disputed, since 'not swerving from the east' may be an approximation. ŚB 2.1.2.2 also notes they are the most numerous asterism (other nakshatras have 1-4 stars).</sub>

### रोहिणी (Rohiṇī) — Aldebaran

**Modern identification:** Aldebaran — α Tauri, Taurus (*certain*)

**Sūrya Siddhānta 8.19 (also 8.13)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> रोहिण्यादित्यमूलानाम् प्राची सार्पस्य चैव हि / यथा प्रत्यवशेषाणाम् स्थूला स्याद् योगतारका //
>
> — *19. Of Rohini, Punarvasu (aditya), and Mula, it is the eastern, and so also of Açlesha (sarpa): in the case of each of the others, the junction-star (yogataraka) is the great (sthula) one.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: the Hyades group (ε, δ, γ, ν, α Tauri); α 'the most easterly (v. 19) and the brightest of the group — being the brilliant star of the first magnitude known as Aldebaran — is the junction-star'. Verse 8.13 concerns splitting Rohiṇī's wain (śakaṭa).</sub>

**Śatapatha Brāhmaṇa 2.1.2.6** — [Sanskrit e-text](https://sa.wikisource.org/wiki/शतपथब्राह्मणम्/काण्डम्_२/अध्यायः_१/ब्राह्मण_२)

> रोहिण्यामग्नी आदधीत । रोहिण्यां ह वै प्रजापतिः प्रजाकामोऽग्नी आदधे स प्रजा असृजत ता अस्य प्रजाः सृष्टा एकरूपा उपस्तब्धास्तस्थू रोहिण्य इवैव तद्वै रोहिण्यै रोहिणीत्वं बहुर्हैव प्रजया पशुभिर्भवति य एवं विद्वान्रोहिण्यामाधत्ते - २.१.२.६
>
> — *He may also set up his fires under (the asterism of) Rohini. For under Rohini it was that Pragapati, when desirous of progeny (or creatures), set up his fires. He created beings, and the creatures produced by him remained invariable and constant, like (red) cows (rohini): hence the cow-like nature of Rohini. Rich in cattle and offspring therefore he becomes whosoever, knowing this, sets up his fires under Rohini.*
> <br>— Julius Eggeling, SBE vol. 12 (1882) ([source](https://www.sacred-texts.com/hin/sbr/sbe12/sbe1241.htm) · [mirror](https://web.archive.org/web/20210506123309/https://www.sacred-texts.com/hin/sbr/sbe12/sbe1241.htm))

<sub>**Identification notes (Vedic corpus):** 'The red one', deity Prajāpati; universally identified with the bright red star Aldebaran. Also TS 4.4.10.1, TB 1.5.1.1, TB 3.1.1.1-2 ('rohiṇī devy udagāt purastāt' - the goddess Rohini has risen in the east), AV 19.7.2, and AB 3.33 where the female deer (rohit) of the Prajāpati myth is Rohiṇī.</sub>

### मृगशीर्ष (Mṛgaśīrṣa) — Meissa

**Modern identification:** Meissa — λ Orionis, Orion (*certain*)

*See also:* `invaka`, `mriga`

**Sūrya Siddhānta 8.16** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> फाल्गुन्योर् भाद्रपदयोस् तथैवाषाढयोर् द्वयोः / विशाखाश्विनिसौम्यानाम् योगतारोत्तरा स्मृता //
>
> — *16. Of the two Phalgunis, the two Bhadrapadas, and likewise the two Ashadhas, of Viçakha, Açvini, and Mrgaçirsha (saumya), the junction-star (yogatara) is stated to be the northern (uttara):*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: the faint cluster in Orion's head, λ φ¹ φ² Orionis; the northern (v. 16), λ Orionis, is the junction-star, 'although the Hindu measurement... is far from accurate, especially as regards its latitude'.</sub>

**Śatapatha Brāhmaṇa 2.1.2.8-9** — [Sanskrit e-text](https://sa.wikisource.org/wiki/शतपथब्राह्मणम्/काण्डम्_२/अध्यायः_१/ब्राह्मण_२)

> मृगशीर्षेऽग्नी आदधीत । एतद्वै प्रजापतेः शिरो यन्मृगशीर्षं श्रीर्वै शिरः श्रीर्हि वै शिरस्तस्माद्योऽर्धस्य श्रेष्ठो भवत्यसावमुष्यार्धस्य शिर इत्याहुः श्रियं ह गच्छति य एवं विद्वान्मृगशीर्ष आधत्ते - २.१.२.८ अथ यस्मान्ना मृगशीर्ष आदधीत । प्रजापतेर्वा एतच्छरीरं यत्र वा एनं तदावेध्यंस्तदिषुणा त्रिकाण्डेनेत्याहुः स एतच्छरीरमजहाद्वास्तु वै शरीरमयज्ञियं निर्वीर्यं तस्मान्न मृगशीर्ष आदधीत - २.१.२.९
>
> — *He may also set up his fires under (the asterism of) Mrigasirsha. For Mrigasirsha, indeed, is the head of Pragapati; and the head (siras) means excellence (sri)... On the other hand (it is argued) why one should not set up his fire under Mrigasirsha. The latter, indeed, is Pragapati's body. Now, when they (the gods) on that occasion pierced him with what is called 'the three-knotted arrow,' he abandoned that body, for the body is a mere relic (or dwelling, vastu), unholy and sapless. He should therefore not set up his fires under Mrigasirsha.*
> <br>— Julius Eggeling, SBE vol. 12 (1882) ([source](https://www.sacred-texts.com/hin/sbr/sbe12/sbe1241.htm) · [mirror](https://web.archive.org/web/20210506123309/https://www.sacred-texts.com/hin/sbr/sbe12/sbe1241.htm))

<sub>**Identification notes (Vedic corpus):** 'The deer's head' = the compact triangle of faint stars forming Orion's head, chief star λ Orionis. The ŚB explicitly makes it 'the head of Prajapati', whose body (Orion) was pierced by the three-jointed arrow (Orion's belt) - see ŚB 2.1.2.9 and AB 3.33. Also TS 4.4.10.1 (deity Soma), AV 19.7.2 (mṛgaśiraḥ), TB 1.5.1.1 (called Invakā).</sub>

### आर्द्रा (Ārdrā) — Betelgeuse

**Modern identification:** Betelgeuse — α Orionis, Orion (*disputed*)

*See also:* `bahu`

**Sūrya Siddhānta 8.19 (positions 8.2, 8.6)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> रोहिण्यादित्यमूलानाम् प्राची सार्पस्य चैव हि / यथा प्रत्यवशेषाणाम् स्थूला स्याद् योगतारका //
>
> — *19. Of Rohini, Punarvasu (aditya), and Mula, it is the eastern, and so also of Açlesha (sarpa): in the case of each of the others, the junction-star (yogataraka) is the great (sthula) one.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Not individually named in ch. 8; single-star asterism covered by the position sequence (8.2, 8.6) and the sthūla rule (8.19). Burgess: 'impossible not to regard... α Orionis as the one here meant', despite 'very grave errors in the definition of its position'; the only star nearly matching the stated position is 135 Tauri (6th mag).</sub>

**Taittirīya Saṃhitā 4.4.10.1** — [Sanskrit e-text](https://sa.wikisource.org/wiki/तैत्तिरीयसंहिता(विस्वरः)

> मृगशीर्षं नक्षत्रꣳ सोमो देवताऽऽर्द्रा नक्षत्रꣳ रुद्रो देवता
>
> — *Mrgaçirsa the Naksatra, Soma the deity; Ardra the Naksatra, Rudra the deity.*
> <br>— A.B. Keith, The Veda of the Black Yajus School (1914) ([source](https://www.sacred-texts.com/hin/yv/yv04.htm) · [mirror](https://web.archive.org/web/20210301091213/https://www.sacred-texts.com/hin/yv/yv04.htm))

<sub>**Identification notes (Vedic corpus):** 'The moist one', deity Rudra. Standard identification is Betelgeuse (the bright reddish star adjoining Mṛgaśīrṣa in the ecliptic sequence); a minority of older scholars (e.g. Weber) proposed Sirius because of the Rudra connection. The Taittirīya Brāhmaṇa (1.5.1.1) substitutes the dual name Bāhū 'the two Arms (of Rudra)'. Also AV 19.7.2, TB 3.1.1.3 ('ārdrayā rudraḥ prathamānaḥ eti').</sub>

### पुनर्वसु (Punarvasu) — Pollux

**Modern identification:** Pollux — β Geminorum, Gemini (*certain*)

**Sūrya Siddhānta 8.19** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> रोहिण्यादित्यमूलानाम् प्राची सार्पस्य चैव हि / यथा प्रत्यवशेषाणाम् स्थूला स्याद् योगतारका //
>
> — *19. Of Rohini, Punarvasu (aditya), and Mula, it is the eastern, and so also of Açlesha (sarpa): in the case of each of the others, the junction-star (yogataraka) is the great (sthula) one.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'the two bright stars in the heads of the Twins, or α and β Geminorum, and the latter (1.2) is the junction-star' (the eastern, per v. 19).</sub>

### पुष्य (Puṣya) — Asellus Australis

**Modern identification:** Asellus Australis — δ Cancri, Cancer (*likely*)

*See also:* `tishya`

**Sūrya Siddhānta 8.18** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> ज्येष्ठाश्रवणमैत्राणाम् बार्हस्पत्यस्य मध्यमा / भरण्याग्नेयपित्र्याणाम् रेवत्याश् चैव दक्षिणा //
>
> — *18. Of Jyeshtha, Çravana, Anuradha (maitra), and Pushya (barhaspatya), it is the middle star: of Bharani, Krttika (agneya), and Magha (pitrya), and likewise of Revati, it is the southern:*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: the middle of three (with γ and θ Cancri) is the junction-star, 'shown by the position assigned to it to be δ Cancri (4)'; hypothetically, under the arrow figure alone, θ Cancri could be meant.</sub>

**Atharvaveda (Śaunaka) 19.7 (nakṣatra hymn, esp. v. 2)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अथर्ववेदः/काण्डं_१९/सूक्तम्_००७)

> चित्राणि साकं दिवि रोचनानि सरीसृपाणि भुवने जवानि । तुर्मिशं सुमतिमिच्छमानो अहानि गीर्भिः सपर्यामि नाकम् ॥१॥ सुहवमग्ने कृत्तिका रोहिणी चास्तु भद्रं मृगशिरः शमार्द्रा । पुनर्वसू सूनृता चारु पुष्यो भानुराश्लेषा अयनं मघा मे ॥२॥ पुण्यं पूर्वा फल्गुन्यौ चात्र हस्तश्चित्रा शिवा स्वाति सुखो मे अस्तु । राधे विशाखे सुहवानुराधा ज्येष्ठा सुनक्षत्रमरिष्ट मूलम् ॥३॥ अन्नं पूर्वा रासतां मे अषाढा ऊर्जं देव्युत्तरा आ वहन्तु । अभिजिन् मे रासतां पुण्यमेव श्रवणः श्रविष्ठाः कुर्वतां सुपुष्टिम् ॥४॥ आ मे महच्छतभिषग्वरीय आ मे द्वया प्रोष्ठपदा सुशर्म । आ रेवती चाश्वयुजौ भगं म आ मे रयिं भरण्य आ वहन्तु ॥५॥
>
> — *1. Seeking favor of the twenty-eight-fold (?) wondrous ones, shining in the sky together, ever-moving, hasting in the creation (bhuvana), I worship (sapary) with songs the days, the firmament (naka). 2. Easy of invocation for me [be] the Krittikas and Rohini; be Mriga-çiras excellent, [and] Ardra healthful (çam); be the two Punarvasus pleasantness, Pushya what is agreeable, the Açleshas light (bhanu), the Maghas progress (ayana) [for me]. ... 5. Let Çatabhishaj [bring] to me what is great widely; let the double Proshthapadas [bring] to me good protection (suçarman); let Revati and the two Açvayuj [bring] fortune to me; let the Bharanis bring to me wealth.*
> <br>— W.D. Whitney, Atharva-Veda Samhita, HOS 8 (1905), p. 907 ([source](https://archive.org/details/atharvavedasamhi02whituoft) · [mirror](https://archive.org/download/atharvavedasamhi02whituoft/atharvavedasamhi02whituoft_djvu.txt))

<sub>**Identification notes (Vedic corpus):** AV nakshatra hymn, verse 2; the AV series begins with the Krittikas (Pleiades) like the TS but comprises 28 asterisms including Abhijit (Vega). Whitney emends the corrupt turmiśaṁ of AV 19.7.1 to aṣṭāviṅśáṁ 'twenty-eight-fold'.</sub>

### आश्लेषा (Āśleṣā) — Ashlesha

**Modern identification:** Ashlesha — ε Hydrae, Hydra (*disputed*)

**Sūrya Siddhānta 8.19** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> रोहिण्यादित्यमूलानाम् प्राची सार्पस्य चैव हि / यथा प्रत्यवशेषाणाम् स्थूला स्याद् योगतारका //
>
> — *19. Of Rohini, Punarvasu (aditya), and Mula, it is the eastern, and so also of Açlesha (sarpa): in the case of each of the others, the junction-star (yogataraka) is the great (sthula) one.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Colebrooke pointed to α Cancri; Burgess rejects this ('α Cancri is not the eastern member of any group of five stars') and places the asterism in the circular group in Hydra's head, 'and ε Hydrae, its brightest star... is the junction-star', while conceding the latitude error is 'very considerable'.</sub>

### मघा (Maghā) — Regulus

**Modern identification:** Regulus — α Leonis, Leo (*certain*)

**Sūrya Siddhānta 8.18** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> ज्येष्ठाश्रवणमैत्राणाम् बार्हस्पत्यस्य मध्यमा / भरण्याग्नेयपित्र्याणाम् रेवत्याश् चैव दक्षिणा //
>
> — *18. Of Jyeshtha, Çravana, Anuradha (maitra), and Pushya (barhaspatya), it is the middle star: of Bharani, Krttika (agneya), and Magha (pitrya), and likewise of Revati, it is the southern:*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: of the Sickle group, 'the star α Leonis, or Regulus, the most brilliant of the group, is the junction-star, and its position is defined with unusual precision'.</sub>

### पूर्वफल्गुनी (Pūrva-Phalgunī) — Zosma

**Modern identification:** Zosma — δ Leonis, Leo (*likely*)

**Sūrya Siddhānta 8.16** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> फाल्गुन्योर् भाद्रपदयोस् तथैवाषाढयोर् द्वयोः / विशाखाश्विनिसौम्यानाम् योगतारोत्तरा स्मृता //
>
> — *16. Of the two Phalgunis, the two Bhadrapadas, and likewise the two Ashadhas, of Viçakha, Açvini, and Mrgaçirsha (saumya), the junction-star (yogatara) is stated to be the northern (uttara):*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: of the pair δ and θ Leonis, 'the first group is, then, clearly identifiable as δ and θ Leonis, the former and brighter being the distinctive star'; he notes the Siddhānta-Śiromaṇi and Graha-Lāghava data may instead point to θ Leonis (the southern).</sub>

### उत्तरफल्गुनी (Uttara-Phalgunī) — Denebola

**Modern identification:** Denebola — β Leonis, Leo (*certain*)

**Sūrya Siddhānta 8.16** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> फाल्गुन्योर् भाद्रपदयोस् तथैवाषाढयोर् द्वयोः / विशाखाश्विनिसौम्यानाम् योगतारोत्तरा स्मृता //
>
> — *16. Of the two Phalgunis, the two Bhadrapadas, and likewise the two Ashadhas, of Viçakha, Açvini, and Mrgaçirsha (saumya), the junction-star (yogatara) is stated to be the northern (uttara):*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'In the latter group, the junction-star is evidently β Leonis'; the text's calling it 'northern' he regards 'as simply an error' of the describers.</sub>

### हस्त (Hasta) — Gienah

**Modern identification:** Gienah — γ Corvi, Corvus (*disputed*)

**Sūrya Siddhānta 8.17** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> पश्चिमोत्तरताराया द्वितीया पश्चिमे स्थिता / हस्तस्य योगतारा सा श्रविष्ठायाश् च पश्चिमा //
>
> — *17. That which is the western northern star, being the second situated westward, that is the junction-star of Hasta; of Çravishtha it is the western:*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Five stars of Corvus. Burgess: v. 17's special description is 'quite hard to understand and apply: we regard it as most probable... that γ (3) is the star intended: the defined position... would point rather to δ (3)'. Colebrooke gave 'γ or δ Corvi'.</sub>

### चित्रा (Citrā) — Spica

**Modern identification:** Spica — α Virginis, Virgo (*certain*)

**Sūrya Siddhānta 8.19 (named in 8.21)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> अपाम्वत्सस् तु चित्राया उत्तरे +अम्शैस् तु पञ्चभिः / बृहत् किञ्चिद् अतो भागैर् आपः षड्भिस् तथोत्तरे //
>
> — *21. Apamvatsa is five degrees north from Citra: somewhat greater than it, as also six degrees to the north of it, is Apas.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'This is the beautiful star of the first magnitude α Virginis, or Spica, constituting an asterism by itself.' Named again in 8.21 as the reference star for Apāṃvatsa.</sub>

### स्वाती (Svātī) — Arcturus

**Modern identification:** Arcturus — α Boötis, Boötes (*certain*)

**Sūrya Siddhānta 8.19 (positions 8.2, 8.7)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> रोहिण्यादित्यमूलानाम् प्राची सार्पस्य चैव हि / यथा प्रत्यवशेषाणाम् स्थूला स्याद् योगतारका //
>
> — *19. Of Rohini, Punarvasu (aditya), and Mula, it is the eastern, and so also of Açlesha (sarpa): in the case of each of the others, the junction-star (yogataraka) is the great (sthula) one.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Not individually named in ch. 8 (single-star asterism; sthūla rule 8.19; positions 8.2/8.7). Burgess: 'The star intended is plainly α Bootis, or Arcturus'.</sub>

### विशाखा (Viśākhā) — ι Librae

**Modern identification:** ι Librae — ι Librae, Libra (*disputed*)

**Sūrya Siddhānta 8.16** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> फाल्गुन्योर् भाद्रपदयोस् तथैवाषाढयोर् द्वयोः / विशाखाश्विनिसौम्यानाम् योगतारोत्तरा स्मृता //
>
> — *16. Of the two Phalgunis, the two Bhadrapadas, and likewise the two Ashadhas, of Viçakha, Açvini, and Mrgaçirsha (saumya), the junction-star (yogatara) is stated to be the northern (uttara):*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'the identification of Viçakha [is] in some respects more doubtful than that of any other asterism in the series'; the defined position identifies the junction-star with faint ι Librae, though he believes the asterism 'was originally composed of the two stars α and β Librae'. Colebrooke suggested o or χ Librae; modern lists often use α Librae (Zubenelgenubi).</sub>

### अनुराधा (Anurādhā) — Dschubba

**Modern identification:** Dschubba — δ Scorpii, Scorpius (*certain*)

**Sūrya Siddhānta 8.18** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> ज्येष्ठाश्रवणमैत्राणाम् बार्हस्पत्यस्य मध्यमा / भरण्याग्नेयपित्र्याणाम् रेवत्याश् चैव दक्षिणा //
>
> — *18. Of Jyeshtha, Çravana, Anuradha (maitra), and Pushya (barhaspatya), it is the middle star: of Bharani, Krttika (agneya), and Magha (pitrya), and likewise of Revati, it is the southern:*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: the row β, δ, π Scorpionis, 'δ (2.3) being the junction-star' (the middle, per v. 18).</sub>

### ज्येष्ठा (Jyeṣṭhā) — Antares

**Modern identification:** Antares — α Scorpii, Scorpius (*certain*)

*See also:* `rohini-indra`

**Sūrya Siddhānta 8.18** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> ज्येष्ठाश्रवणमैत्राणाम् बार्हस्पत्यस्य मध्यमा / भरण्याग्नेयपित्र्याणाम् रेवत्याश् चैव दक्षिणा //
>
> — *18. Of Jyeshtha, Çravana, Anuradha (maitra), and Pushya (barhaspatya), it is the middle star: of Bharani, Krttika (agneya), and Magha (pitrya), and likewise of Revati, it is the southern:*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: the central of three (with σ and τ Scorpionis) is 'the brilliant star of the first magnitude α Scorpionis, or Antares'.</sub>

### मूल (Mūla) — Shaula

**Modern identification:** Shaula — λ Scorpii, Scorpius (*likely*)

**Sūrya Siddhānta 8.19** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> रोहिण्यादित्यमूलानाम् प्राची सार्पस्य चैव हि / यथा प्रत्यवशेषाणाम् स्थूला स्याद् योगतारका //
>
> — *19. Of Rohini, Punarvasu (aditya), and Mula, it is the eastern, and so also of Açlesha (sarpa): in the case of each of the others, the junction-star (yogataraka) is the great (sthula) one.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Stars of the Scorpion's tail. Burgess: 'if, as seems probable, λ is the star pointed out by the definition of position', the 'eastern' designation is strictly true only of the pair λ and ν (the Vedic vicṛtāu); ι, κ, and θ lie farther east.</sub>

### पूर्वाषाढा (Pūrvāṣāḍhā) — Kaus Media

**Modern identification:** Kaus Media — δ Sagittarii, Sagittarius (*certain*)

**Sūrya Siddhānta 8.16 (also 8.4)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> फाल्गुन्योर् भाद्रपदयोस् तथैवाषाढयोर् द्वयोः / विशाखाश्विनिसौम्यानाम् योगतारोत्तरा स्मृता //
>
> — *16. Of the two Phalgunis, the two Bhadrapadas, and likewise the two Ashadhas, of Viçakha, Açvini, and Mrgaçirsha (saumya), the junction-star (yogatara) is stated to be the northern (uttara):*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'The former group must comprise δ (3.4) and ε (3.2) Sagittarii, the former being the junction-star; this is shown by the... comparison of positions'. Called āpya (of the Waters) in 8.4.</sub>

### उत्तराषाढा (Uttarāṣāḍhā) — Nunki

**Modern identification:** Nunki — σ Sagittarii, Sagittarius (*likely*)

**Sūrya Siddhānta 8.16 (also 8.4)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> मनवो +अथ रसा वेदा वैश्वम् आप्यार्धभोगगम् / आप्यस्यैवाभिजित् प्रान्ते वैश्वान्ते श्रवणस्थितिः /
>
> — *4. Fourteen, six, four: Uttara-Ashadha (vaiçva) is at the middle of the portion (bhoga) of Purva-Ashadha (apya); Abhijit, likewise, is at the end of Purva-Ashadha; the position of Çravana is at the end of Uttara-Ashadha;*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'its northern and junction-star can be no other than σ (2.3)... notwithstanding the error in the Hindu determination of its latitude, which led Colebrooke to regard τ (4.3) as the star intended'. Called vaiśva (of the Viśve Devāḥ) in 8.4.</sub>

### अभिजित् (Abhijit) — Vega

**Modern identification:** Vega — α Lyrae, Lyra (*certain*)

**Sūrya Siddhānta 8.4** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> मनवो +अथ रसा वेदा वैश्वम् आप्यार्धभोगगम् / आप्यस्यैवाभिजित् प्रान्ते वैश्वान्ते श्रवणस्थितिः /
>
> — *4. Fourteen, six, four: Uttara-Ashadha (vaiçva) is at the middle of the portion (bhoga) of Purva-Ashadha (apya); Abhijit, likewise, is at the end of Purva-Ashadha; the position of Çravana is at the end of Uttara-Ashadha;*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'The position assigned to its junction-star, which is described as the brightest... in a group of three, identifies it with α Lyrae or Vega, a star which is exceeded in brilliancy by only one or two others in the heavens' (triangle with ε and ζ Lyrae).</sub>

**Siddhānta Śiromaṇi, Grahagaṇitādhyāya, Bhagrahayutyadhikāra vv.1-6 with Vāsanābhāṣya; Vāsanābhāṣya on v.16** — [Sanskrit e-text](https://sa.wikisource.org/wiki/पृष्ठम्:सिद्धान्तशिरोमणिः.djvu/351)

> यस्य स्फुटा क्रान्तिरुदक् च यत्र लम्बाधिका तत्र सदोदितं तत् । न दृश्यते तत् खलु यस्य याम्या भं लुब्धकः कुम्भभवो ग्रहो वा ।।१६।। — with Bhāskara's own bhāṣya: 'यत्र द्विपश्चाशदधिकाः पलांशास्तत्राभिजित् सदोदितमेव' [verbatim from unproofread OCR; द्विपञ्चाशद् expected]
>
> — *[own rendering, no PD translation exists] (v.16) A star whose true declination is north and exceeds the co-latitude is ever-visible there; one whose declination is south (by that amount) is never seen — be it Lubdhaka, the pot-born (Agastya), or even a planet. (Bhāṣya) Where the degrees of latitude exceed 52, Abhijit is ever-risen (circumpolar).*
> <br>— Own literal rendering (clearly marked), checked against Arkasomayaji's paraphrase ('where the latitude is greater than 52°, there Abhijit is always above the horizon'). ([source](https://archive.org/details/SiddhantaSiromaniGanitadhyaya))

<sub>**Identification notes (Siddhānta Śiromaṇi):** Included by Bhāskara among the 28 asterisms whose dhruvas he lists (Vāsanābhāṣya on vv.1-3: 'अष्टौ नखा इत्यादयोऽश्विन्यादीनां साभिजितां ध्रुवभागा वेदितव्याः' — the dhruvas of Aśvinī etc. together with Abhijit). Its śara is 62° north (largest in the list, per the Bhagrahayuti latitude table), matching Vega's ecliptic latitude of about +61.7°. Bhāskara's Vāsanābhāṣya on v.16 makes it circumpolar above latitude 52°. The 1861 PD volume identifies 'Abhijit (α Lyrae)' (pp.63, 68).</sub>

### श्रवण (Śravaṇa) — Altair

**Modern identification:** Altair — α Aquilae, Aquila (*certain*)

**Sūrya Siddhānta 8.18 (also 8.4)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> ज्येष्ठाश्रवणमैत्राणाम् बार्हस्पत्यस्य मध्यमा / भरण्याग्नेयपित्र्याणाम् रेवत्याश् चैव दक्षिणा //
>
> — *18. Of Jyeshtha, Çravana, Anuradha (maitra), and Pushya (barhaspatya), it is the middle star: of Bharani, Krttika (agneya), and Magha (pitrya), and likewise of Revati, it is the southern:*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: three stars 'in the back and neck of the Eagle, namely α, γ, and β Aquilae; α, the determinative [middle star, v. 18], is a star of the first to second magnitude'.</sub>

### श्रविष्ठा (Śraviṣṭhā (Dhaniṣṭhā)) — Rotanev

**Modern identification:** Rotanev — β Delphini, Delphinus (*certain*)

**Sūrya Siddhānta 8.17 (also 8.5)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> त्रिचतुः पादयोः सन्धौ श्रविष्ठा श्रवणस्य तु / स्वभोगतो वियन् नागाः षट्कृतिर् यमलाश्विनः //
>
> — *5. Çravishtha, on the other hand, is at the point of connection of the third and fourth quarters (pada) of Çravana: then, in their own portions, eighty, thirty-six, twenty-two,*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: the diamond in the Dolphin's head, β α γ δ Delphini; 'The junction-star, which is the western (v. 17), is β'.</sub>

### शतभिषज् (Śatabhiṣaj) — Hydor

**Modern identification:** Hydor — λ Aquarii, Aquarius (*likely*)

**Sūrya Siddhānta 8.19 (positions 8.3, 8.9)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> रोहिण्यादित्यमूलानाम् प्राची सार्पस्य चैव हि / यथा प्रत्यवशेषाणाम् स्थूला स्याद् योगतारका //
>
> — *19. Of Rohini, Punarvasu (aditya), and Mula, it is the eastern, and so also of Açlesha (sarpa): in the case of each of the others, the junction-star (yogataraka) is the great (sthula) one.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Not individually named in ch. 8; its junction-star is the brightest of its hundred (sthūla rule, 8.19). Burgess: 'This, from its defined position, can only be λ Aquarii (4)'. Some later scholars have proposed other Aquarii stars; al-Bīrūnī could not identify it.</sub>

### पूर्वभाद्रपदा (Pūrva-Bhādrapadā) — Markab

**Modern identification:** Markab — α Pegasi, Pegasus (*certain*)

**Sūrya Siddhānta 8.16** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> फाल्गुन्योर् भाद्रपदयोस् तथैवाषाढयोर् द्वयोः / विशाखाश्विनिसौम्यानाम् योगतारोत्तरा स्मृता //
>
> — *16. Of the two Phalgunis, the two Bhadrapadas, and likewise the two Ashadhas, of Viçakha, Açvini, and Mrgaçirsha (saumya), the junction-star (yogatara) is stated to be the northern (uttara):*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Part of the Square of Pegasus. Burgess: 'The junction-star of the former half-asterism is, by its defined position, clearly shown to be α Pegasi', though the 'northern' designation of v. 16 conflicts (α is the southern of the pair with β).</sub>

### उत्तरभाद्रपदा (Uttara-Bhādrapadā) — Algenib / Alpheratz

**Modern identification:** Algenib / Alpheratz — γ Pegasi / α Andromedae, Pegasus / Andromeda (*disputed*)

**Sūrya Siddhānta 8.16** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> फाल्गुन्योर् भाद्रपदयोस् तथैवाषाढयोर् द्वयोः / विशाखाश्विनिसौम्यानाम् योगतारोत्तरा स्मृता //
>
> — *16. Of the two Phalgunis, the two Bhadrapadas, and likewise the two Ashadhas, of Viçakha, Açvini, and Mrgaçirsha (saumya), the junction-star (yogatara) is stated to be the northern (uttara):*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: the text's position gives 'a longitude... of one member of the group [γ Pegasi], and a latitude which is that of the other [α Andromedae]'; 'There can be no doubt that the two stars recognized as composing the asterism are γ Pegasi and α Andromedae, but there has evidently been a blundering confusion of the two'. Modern lists usually take γ Pegasi.</sub>

### रेवती (Revatī) — Revati

**Modern identification:** Revati — ζ Piscium, Pisces (*likely*)

**Sūrya Siddhānta 8.18** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> ज्येष्ठाश्रवणमैत्राणाम् बार्हस्पत्यस्य मध्यमा / भरण्याग्नेयपित्र्याणाम् रेवत्याश् चैव दक्षिणा //
>
> — *18. Of Jyeshtha, Çravana, Anuradha (maitra), and Pushya (barhaspatya), it is the middle star: of Bharani, Krttika (agneya), and Magha (pitrya), and likewise of Revati, it is the southern:*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'The star intended is... the faint star ζ Piscium, of about the fifth magnitude, situated in the band which connects the two Fishes'; nearly all authorities make it mark the initial point of the sidereal sphere. It 'coincided in longitude with the vernal equinox in the year 572 of our era'.</sub>

**Siddhānta Śiromaṇi, Grahagaṇitādhyāya, Bhagrahayutyadhikāra, Vāsanābhāṣya (upapatti) on vv.4-6** — [Sanskrit e-text](https://sa.wikisource.org/wiki/पृष्ठम्:सिद्धान्तशिरोमणिः.djvu/349)

> …रात्रौ गोलमध्यगचिहुगतया दृष्ट्या रेवतो.तारां विलोक्य क्रान्तिवृत्ते यो मीनान्तस्तं रेवतीतारायां निवेश्य मध्यगतयैव दृष्टच्याश्चिन्यादेर्नक्षत्रस्य योगतारां विलोक्य तस्योपरिवेधवलयं निवेश्यम् । [prose bhāṣya, verbatim from unproofread OCR with visible OCR slips]
>
> — *[own rendering, no PD translation exists] At night, sighting through the mark at the centre of the sphere, one observes the star of Revatī and places upon it the end of Pisces on the ecliptic ring; then, sighting the yogatārā of Aśvinī and the other nakshatras, the sighting-ring is laid over each; the degrees from the end of Pisces to the intersection give that asterism's dhruva, and the degrees between the intersection and the yogatārā give its śara, north or south.*
> <br>— Own literal rendering (clearly marked) of Bhāskara's Vāsanābhāṣya. ([source](https://sa.wikisource.org/wiki/पृष्ठम्:सिद्धान्तशिरोमणिः.djvu/349))

<sub>**Identification notes (Siddhānta Śiromaṇi):** In the upapatti to Bhagrahayuti vv.4-6 Bhāskara himself describes the observational procedure: at night one sights the Revatī star through the armillary sphere and sets the end of Pisces (Mīnānta, i.e. longitude 360°) on it, then reads off each yogatārā's dhruva and śara on the sighting-ring. Bhāskara assigns Revatī dhruva 0 and śara 0. The traditional identification ζ Piscium is printed in the 1861 PD volume ('Revati (ζ Piscium)', p.63); some modern scholars debate whether the faint ζ Psc can be the intended zero star, hence 'likely' rather than 'certain'.</sub>

## Individually named stars

Stars outside the nakshatra series that the texts name in their own right.

### अगस्त्य (Agastya) — Canopus

**Modern identification:** Canopus — α Carinae, Carina (*certain*)

**Sūrya Siddhānta 8.10** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> अशीतिभागैर् याम्यायाम् अगस्त्यो मिथुनान्तगः / विम्शे च मिथुनस्याम्शे मृगव्याधो व्यवस्थितः //
>
> — *10. Agastya is at the end of Gemini, and eighty degrees south; and Mrgavyadha is situated in the twentieth degree of Gemini;*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'Agastya is α Navis, or Canopus, a star of the first magnitude, and one of the most brilliant in the southern heavens' (his 'α Argūs/α Navis' = modern α Carinae); identification 'correctly pointed out by Colebrooke'.</sub>

**Bṛhat Saṃhitā 12.7 (chapter title: अगस्त्यचाराध्यायः)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/बृहत्संहिता/अध्यायः_१२)

> उदये च मुनेरगस्त्यनाम्नः कुसमायोगमलप्रदूषितानि ।
> हृदयानि सतां इव स्वभावात्पुनरम्बूनि भवन्ति निर्मलानि ।। १२.०७ ।।
>
> — *When star Canopus reappears after its conjunction with the Sun, waters muddled by their contact with the earth will resume their original clearness just in the same way as the minds of the Sadhus naturally recover their original purity after contact with the wicked.*
> <br>— N. Chidambaram Iyer (1884), ch. XII v. 7, p. 77 ([source](https://archive.org/details/bihatsahitvarah00iyergoog))

<sub>**Identification notes (Bṛhat Saṃhitā):** Agastya = Canopus is universally accepted (Colebrooke, As. Res. IX; Burgess's Sūrya-siddhānta notes p. 245: 'Agastya is α Navis, or Canopus'). Bṛhat Saṃhitā ch. 12 (Agastyacārādhyāya) is devoted to its heliacal rising; Agastya is named in BS 12.7, 12.11, 12.12, 12.13, 12.19; BS 12.14 fixes its heliacal rising at Ujjayinī, and 12.21 its rising/setting against Hastā/Rohiṇī. Iyer translates the name throughout as 'Canopus'.</sub>

**Siddhānta Śiromaṇi, Grahagaṇitādhyāya, Bhagrahayutyadhikāra v.7 (also vv.8, 12, 16)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/पृष्ठम्:सिद्धान्तशिरोमणिः.djvu/349)

> अगस्त्यध्रुवः सप्तनागास्तु भागास्तुरखाद्यस्तस्य यम्यः शरांशः । षडष्टौ लवा लुब्धकस्य ध्रुवोऽयं नभोऽम्भोधिभागाः शरस्तस्य याम्यः ॥७॥ [verbatim from unproofread OCR; expected readings याम्यः for यम्यः, तुरगाद्रयस् for तुरखाद्यस्]
>
> — *[paraphrase] The polar longitude (dhruva) of Agastya is 87 degrees and its polar latitude (śara) 77 degrees south; the polar longitude of Lubdhaka is 86 degrees and its polar latitude 40 degrees south.*
> <br>— Paraphrased from D. Arkasomayaji, Siddhānta Śiromaṇi Gaṇitādhyāya (Kendriya Sanskrit Vidyapeetha, Tirupati; copyrighted, not quoted verbatim). No public-domain English translation of the Gaṇitādhyāya exists online. ([source](https://archive.org/details/SiddhantaSiromaniGanitadhyaya))

<sub>**Identification notes (Siddhānta Śiromaṇi):** Universal identification in the Siddhanta tradition. Bhāskara gives polar longitude 87° (sapta-nāga), polar latitude 77° south (turaga-adri); his Vāsanābhāṣya on v.16 adds that Agastya is invisible where the terrestrial latitude exceeds 37° ('यस्मिन् देशे सप्तत्रिशदधिकाः पलांशास्तत्रागस्त्यो न दृश्यते'). Verse 12 calls it 'muni' (the sage). The 1861 public-domain volume (Sūrya Siddhānta portion, same tradition) prints 'Agastya (Canopus)' explicitly (p.63, 68). D. Arkasomayaji's translation of this very verse also glosses 'Agastya (Canopus)'.</sub>

### मृगव्याध (Mṛgavyādha) — Sirius

**Modern identification:** Sirius — α Canis Majoris, Canis Major (*likely*)

*See also:* `lubdhaka`

**Sūrya Siddhānta 8.10–11** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> अशीतिभागैर् याम्यायाम् अगस्त्यो मिथुनान्तगः / विम्शे च मिथुनस्याम्शे मृगव्याधो व्यवस्थितः // विक्षेपो दक्षिणे भागैः खार्णवैः स्वाद् अपक्रमात् / हुतभुग्ब्रह्महृदयौ वृषे द्वाविम्शभागगौ //
>
> — *10. Agastya is at the end of Gemini, and eighty degrees south; and Mrgavyadha is situated in the twentieth degree of Gemini; 11. His latitude (vikshepa), reckoned from his point of declination (apakrama), is forty degrees south:*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'Mrgavyadha, "deer-hunter" — it is also called Lubdhaka, "hunter" — is α Canis Majoris, or Sirius, the brightest of the fixed stars'.</sub>

**Aitareya Brāhmaṇa 3.33** — [Sanskrit e-text](https://sa.wikisource.org/wiki/ऐतरेय_ब्राह्मणम्/पञ्चिका_३_(तृतीय_पञ्चिका)

> तमभ्यायत्याविध्यत्स विद्ध ऊर्ध्व उदप्रपतत्तमेतं मृग इत्याचक्षते य उ एव मृगव्याधः स उ एव स या रोहित्सा रोहिणी यो एवेषुस्त्रिकाण्डा सो एवेषुस्त्रिकाण्डा।
>
> — *Having aimed at him he pierced him; being pierced he flew upwards; him they call 'the deer'. The piercer of the deer is he of that name. The female deer is Rohini; the three-pointed arrow is the three-pointed arrow.*
> <br>— A.B. Keith, Rigveda Brahmanas, HOS 25 (1920), pp. 185-186 ([source](https://archive.org/details/rigvedabrahmana00keitgoog) · [mirror](https://archive.org/download/rigvedabrahmana00keitgoog/rigvedabrahmana00keitgoog_djvu.txt))

<sub>**Identification notes (Vedic corpus):** The piercer is the dread archer-god (Rudra/Bhūtapati). Identification with Sirius - the brilliant star 'aiming' along the line of Orion's belt - is the standard scholarly and later Indian tradition (Sirius = Lubdhaka 'the hunter' in classical astronomy); the AB itself does not name the star, hence 'likely'.</sub>

### लुब्धक (Lubdhaka) — Sirius

**Modern identification:** Sirius — α Canis Majoris, Canis Major (*certain*)

*See also:* `mrigavyadha`

**Not in Bṛhat Saṃhitā; Kathāsaritsāgara 6.2.88 (lubdhaka); Sūrya-siddhānta 8.10 (as Mṛgavyādha)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/कथासरित्सागरः/लम्बकः_६/तरङ्गः_२)

> Bṛhat Saṃhitā: shloka not found online (word absent from the text). Kathāsaritsāgara 6.2.88: दत्त्वायुषोऽर्धं मुनिना न भार्या रुरुणा कृता ।
> त्रिशङ्कुः किं न नीतो द्यां विश्वामित्रेण लुब्धकः ।। ८८
>
> — *Was not the Chandala Trisanku carried to heaven by Visvamitra?*
> <br>— C. H. Tawney (1880), Katha Sarit Sagara vol. 1, ch. XXVIII, p. 251; Sūrya-siddhānta rendering: E. Burgess (1860) ([source](https://archive.org/details/kathsaritsga01somauoft))

<sub>**Identification notes (Bṛhat Saṃhitā):** Lubdhaka ('the Hunter') = Sirius is standard in Sanskrit lexica (Monier-Williams, s.v. lubdhaka: 'the star Sirius', citing the Gaṇitādhyāya and Kathāsaritsāgara) — but the word does NOT occur in the Bṛhat Saṃhitā: a search of the complete GRETIL e-text (Yano–Sugita, Tripathi ed.) finds no lubdhaka and no mṛgavyādha as a star. Classical attestations verified online: (1) Sūrya-siddhānta 8.10 locates the star under its synonym Mṛgavyādha ('deer-hunter'): अशीतिभागैर् याम्यायाम् अगस्त्यो मिथुनान्तगः / विम्शे च मिथुनस्याम्शे मृगव्याधो व्यवस्थितः (https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः); Burgess: 'Mrgavyadha, deer-hunter — it is also called Lubdhaka, hunter — is α Canis Majoris, or Sirius, the brightest of the fixed stars' (pp. 245–246). (2) Kathāsaritsāgara 6.2.88 (= taraṅga 28.88) is MW's literary citation for lubdhaka = Sirius (Triśaṅku raised to the sky), but Tawney (1880, vol. 1 p. 251) translates 'Was not the Chandala Trisanku carried to heaven by Visvamitra?', taking lubdhaka as 'outcaste hunter' — so the star sense in KSS is a lexicographers' reading, not undisputed. No Kālidāsa attestation of Lubdhaka as Sirius was found online.</sub>

**Siddhānta Śiromaṇi, Grahagaṇitādhyāya, Bhagrahayutyadhikāra vv.7-8 (also vv.12, 16)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/पृष्ठम्:सिद्धान्तशिरोमणिः.djvu/349)

> अगस्त्यस्य नाडीद्वयं प्रोक्तमिष्टं सषड्भागनाडीद्वयं लुब्धकस्य । त्रिभागाधिकं स्थूलभानामणूना ततश्वाधिकं तारतम्येन कल्प्यम् ॥८॥ [verbatim from unproofread OCR]
>
> — *[paraphrase] The iṣṭa-nāḍīs (arc of visibility for heliacal rising) are two nāḍīs for Agastya, two nāḍīs and a sixth for Lubdhaka, a third more for the large stars, and progressively more for the fainter ones.*
> <br>— Paraphrased from D. Arkasomayaji (copyrighted); Bhāskara's own Vāsanābhāṣya glosses: Agastya 12 kālāṃśas, Lubdhaka 13, gross stars 14, faint ones 15-16. ([source](https://archive.org/details/SiddhantaSiromaniGanitadhyaya))

<sub>**Identification notes (Siddhānta Śiromaṇi):** Bhāskara's mūla uses 'Lubdhaka' (the Hunter) in vv.7-8 and 'mṛgaripu' (enemy of the deer) in v.12 ('भाना मुनेर्मृगरिपोरुदयास्तलग्ने'); the name Mṛgavyādha for the same star appears on the same page only in Nṛsiṃha Daivajña's Vārttika quoting Sūrya Siddhānta 9.12 ('स्वात्यगस्त्यमृगव्याधचित्राज्येष्ठाः पुनर्वसुः', sa.wikisource page 347). Values: polar longitude 86° (ṣaḍ-aṣṭau), polar latitude 40° south (nabho'mbhodhi). Iṣṭanāḍīs 2 1/6 nāḍī = 13 kālāṃśas per the Vāsanābhāṣya ('तत्र त्रयोदशा १३ कालांशाः'). 1861 PD volume: 'Mrigavyādha (Sirius)' (p.63).</sub>

### अग्नि (हुतभुज्) (Agni (Hutabhuj)) — Elnath

**Modern identification:** Elnath — β Tauri, Taurus (*certain*)

**Sūrya Siddhānta 8.11–12** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> विक्षेपो दक्षिणे भागैः खार्णवैः स्वाद् अपक्रमात् / हुतभुग्ब्रह्महृदयौ वृषे द्वाविम्शभागगौ // अष्टाभिस् त्रिम्शता चैव विक्षिप्ताव् उत्तरेण तौ / गोलम् लब्ध्वा परीक्षेत विक्षेपम् ध्रुवकम् स्फुटम् //
>
> — *11. ... Agni (hutabhuj) and Brahmahrdaya are in Taurus, the twenty-second degree; 12. And they are removed in latitude (vikshipta), northward, eight and thirty degrees respectively. . . .*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'The star named after the god of fire, Agni, and called in the text by one of his frequent epithets, hutabhuj, "devourer of the sacrifice," is the one which is situated at the extremity of the northern horn of the Bull, or β Tauri'; he notes 'the very gross error in the determination of the longitude of this star'.</sub>

### ब्रह्महृदय (Brahmahṛdaya) — Capella

**Modern identification:** Capella — α Aurigae, Auriga (*certain*)

**Sūrya Siddhānta 8.11–12** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> विक्षेपो दक्षिणे भागैः खार्णवैः स्वाद् अपक्रमात् / हुतभुग्ब्रह्महृदयौ वृषे द्वाविम्शभागगौ // अष्टाभिस् त्रिम्शता चैव विक्षिप्ताव् उत्तरेण तौ / गोलम् लब्ध्वा परीक्षेत विक्षेपम् ध्रुवकम् स्फुटम् //
>
> — *11. ... Agni (hutabhuj) and Brahmahrdaya are in Taurus, the twenty-second degree; 12. And they are removed in latitude (vikshipta), northward, eight and thirty degrees respectively. . . .*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'Brahmahrdaya, "Brahma's heart," is α Aurigae or Capella'.</sub>

### प्रजापति (Prajāpati) — Prijipati

**Modern identification:** Prijipati — δ Aurigae, Auriga (*likely*)

**Sūrya Siddhānta 8.20** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> पूर्वस्याम् ब्रह्महृदयाद् अम्शकैः पञ्चभिः स्थितः / प्रजापतिर् वृषान्ते +असौ सौम्ये +अष्टत्रिम्शदम्शकैः //
>
> — *20. Situated five degrees eastward from Brahmahrdaya is Prajapati: it is at the end of Taurus, and thirty-eight degrees north.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'The star referred to can hardly be any other than that in the head of the Wagoner, or δ Aurigae (4)', wondering 'why so faint and inconspicuous a star' was singled out. He also doubts the authenticity of vv. 20-21 and notes the two definitions of its longitude (v. 11 + v. 20 vs 'end of Taurus') do not quite agree.</sub>

### अपांवत्स (Apāṃvatsa) — θ Virginis

**Modern identification:** θ Virginis — θ Virginis, Virgo (*likely*)

**Sūrya Siddhānta 8.21** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> अपाम्वत्सस् तु चित्राया उत्तरे +अम्शैस् तु पञ्चभिः / बृहत् किञ्चिद् अतो भागैर् आपः षड्भिस् तथोत्तरे //
>
> — *21. Apamvatsa is five degrees north from Citra: somewhat greater than it, as also six degrees to the north of it, is Apas.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Colebrooke gave 'the nebulous stars marked b 1, 2, 3 in Virgo', which Burgess could find in no map or catalogue; Burgess: 'There is, on the other hand, a star, θ Virginis (4), situated directly between Spica and δ, and at such a distance from each as shows almost beyond question that it is the star intended' (so also his index: 'Apamvatsa, name of star (θ Virginis)').</sub>

### आपस् (आपः) (Āpas) — Minelauva (Auva)

**Modern identification:** Minelauva (Auva) — δ Virginis, Virgo (*certain*)

**Sūrya Siddhānta 8.21** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> अपाम्वत्सस् तु चित्राया उत्तरे +अम्शैस् तु पञ्चभिः / बृहत् किञ्चिद् अतो भागैर् आपः षड्भिस् तथोत्तरे //
>
> — *21. Apamvatsa is five degrees north from Citra: somewhat greater than it, as also six degrees to the north of it, is Apas.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'Apas, "Waters"... is put 6° north of Apamvatsa, or in lat. 9° N. It is identified by Colebrooke with δ Virginis (3), and doubtless correctly'. Noticed in the Sūrya-Siddhānta alone among his authorities.</sub>

### ध्रुवः (Dhruva) — Polaris (the pole star)

**Modern identification:** Polaris (the pole star) — α Ursae Minoris, Ursa Minor (*disputed*)

*See also:* `saptarshi`, `arundhati`

**Āśvalāyana Gṛhya Sūtra 1.7.22** — [Sanskrit e-text](https://sa.wikisource.org/wiki/आश्वलायनगृह्यसूत्रम्/अध्यायः_१)

> ध्रुवमरुन्धतीं सप्तऋषीनिति दृष्ट्वा वाचं विसृजेत जीवपत्नीं प्रजां विन्देयेति २२
>
> — *When she sees the polar-star, the star Arundhati, and the seven Rishis (ursa major), let her break the silence (and say), 'May my husband live and I get offspring.'*
> <br>— Hermann Oldenberg, SBE vol. 29 (1886) ([source](https://sacred-texts.com/hin/sbe29/sbe29.txt) · [mirror](https://web.archive.org/web/20080113225826/http://sacred-texts.com/hin/sbe29/sbe29.txt))

<sub>**Identification notes (Vedic corpus):** 'The fixed one', shown to the bride on the wedding night (dhruva-darśana) as an emblem of constancy. In the historical period Dhruva = Polaris, but scholars note that at plausible dates of the ritual's origin (2nd-1st millennium BCE) no bright star stood at the pole: α Draconis (Thuban) was pole star c. 2800 BCE, and Polaris only closed on the pole in the last ~1500 years. Dhruva may therefore be an idealized 'fixed point' of the sky, an earlier pole star remembered, or a faint near-polar star. Parallel rite with the mantra dhruvám asi: Śāṅkhāyana GS 1.17.2-4, tr. Oldenberg: 'Let them sit silent, when the sun has set, until the polar-star appears. He shows her the polar-star with the words, Firm be thou, thriving with me! Let her say, I see the polar-star; may I obtain offspring' (same source URL).</sub>

## The Saptarṣi (Ursa Major) and Arundhatī

Bṛhat Saṃhitā ch. 13 gives the east-to-west order of the seven rishis and places Arundhatī beside Vasiṣṭha; the star-by-star mapping below follows from that order once Vasiṣṭha is anchored to Mizar by Arundhatī = Alcor. Only the Mizar/Alcor pair is fixed by the text itself.

### सप्तर्षयः / ऋक्षाः (Saptarṣayaḥ / Ṛkṣāḥ) — the Big Dipper - seven bright stars of Ursa Major (Dubhe, Merak, Phecda, Megrez, Alioth, Mizar, Alkaid)

**Modern identification:** the Big Dipper - seven bright stars of Ursa Major (Dubhe, Merak, Phecda, Megrez, Alioth, Mizar, Alkaid) — α, β, γ, δ, ε, ζ, η Ursae Majoris, Ursa Major (*certain*)

*See also:* `marichi`, `vasishtha`, `angiras`, `atri`, `pulastya`, `pulaha`, `kratu`, `arundhati`

**Śatapatha Brāhmaṇa 2.1.2.4** — [Sanskrit e-text](https://sa.wikisource.org/wiki/शतपथब्राह्मणम्/काण्डम्_२/अध्यायः_१/ब्राह्मण_२)

> अथ यस्मान्न कृत्तिकास्वादधीत । ऋक्षाणां ह वा एता अग्रे पत्न्य आसुः सप्तर्षीनु ह स्म वै पुरर्क्षा इत्याचक्षते ता मिथुनेन व्यार्ध्यन्तामी ह्युत्तरा हि सप्तर्षय उद्यन्ति पुर एता अशमिव वै तद्यो मिथुनेन व्यृद्धः स नेन्मिथुनेन व्यृध्या इति तस्मान्न कृत्तिकास्वादधीत - २.१.२.४
>
> — *On the other hand (it is argued) why he should not set up the fires under the Krittikas. Originally, namely, the latter were the wives of the Bears (riksha); for the seven Rishis were in former times called the Rikshas (bears). They were, however, precluded from intercourse (with their husbands), for the latter, the seven Rishis, rise in the north, and they (the Krittikas) in the east. Now it is a misfortune for one to be precluded from intercourse (with his wife): he should therefore not set up his fires under the Krittikas, lest he should thereby be precluded from intercourse.*
> <br>— Julius Eggeling, SBE vol. 12 (1882), pp. 282-283 ([source](https://www.sacred-texts.com/hin/sbr/sbe12/sbe1241.htm) · [mirror](https://web.archive.org/web/20210506123309/https://www.sacred-texts.com/hin/sbr/sbe12/sbe1241.htm))

<sub>**Identification notes (Vedic corpus):** The ŚB states that the Seven Rishis 'were in former times called the Rkshas (bears)' - preserving the older name ṛkṣāḥ 'bears' (cf. RV 1.24.10) that matches the Greco-Roman Bear, and notes they rise in the north while the Krittikas rise in the east - exactly true of the circumpolar Dipper vs. the equatorial Pleiades. Also shown to the bride in ĀGS 1.7.22.</sub>

### मरीचि (Marīci) — Alkaid (Benetnash)

**Modern identification:** Alkaid (Benetnash) — η Ursae Majoris, Ursa Major (*likely*)

**Bṛhat Saṃhitā 13.5** — [Sanskrit e-text](https://sa.wikisource.org/wiki/बृहत्संहिता/अध्यायः_१३)

> पूर्वे भागे भगवान्मरीचिरपरे स्थितो वसिष्ठो +अस्मात् ।
> तस्याङ्गिरास्ततो +अत्रिस्तस्यासन्नः पुलस्त्यश्च ।। १३.०५ ।।
>
> — *The eastern-most of the group is Bhagavan Marichi; the next to him is Vasishtha; the next is Angirasa and the next two are Atri and Pulastya.*
> <br>— N. Chidambaram Iyer (1884), ch. XIII v. 5, p. 81 ([source](https://archive.org/details/bihatsahitvarah00iyergoog))

<sub>**Identification notes (Bṛhat Saṃhitā):** BS 13.5 makes Marīci the easternmost of the seven (pūrve bhāge bhagavān marīciḥ). The BS itself gives only this east-to-west ORDER, not star-by-star identifications; reading the order onto the Big Dipper (Alkaid is the easternmost star, and the next, Vasiṣṭha, is anchored to Mizar by Arundhatī = Alcor) yields Marīci = Alkaid. The Bayer assignment is thus conventional but consistent with the classical order.</sub>

### वसिष्ठ (Vasiṣṭha) — Mizar

**Modern identification:** Mizar — ζ Ursae Majoris, Ursa Major (*certain*)

*See also:* `arundhati`

**Bṛhat Saṃhitā 13.5–6** — [Sanskrit e-text](https://sa.wikisource.org/wiki/बृहत्संहिता/अध्यायः_१३)

> पूर्वे भागे भगवान्मरीचिरपरे स्थितो वसिष्ठो +अस्मात् ।
> तस्याङ्गिरास्ततो +अत्रिस्तस्यासन्नः पुलस्त्यश्च ।। १३.०५ ।।
> पुलहः क्रतुरिति भगानासन्ना अनुक्रमेण *पूर्वाद्यात्[क्.पूर्वाद्याः] ।
> तत्र वसिष्ठं मुनिवरं उपाश्रितारुन्धती साध्वी ।। १३.०६ ।।
>
> — *The eastern-most of the group is Bhagavan Marichi; the next to him is Vasishtha; ... The chaste Arundhati closely attends her husband the sage Vasishtha.*
> <br>— N. Chidambaram Iyer (1884), ch. XIII vv. 5–6, p. 81 ([source](https://archive.org/details/bihatsahitvarah00iyergoog))

<sub>**Identification notes (Bṛhat Saṃhitā):** Anchored by the text itself: BS 13.6 places the faithful Arundhatī right beside Vasiṣṭha, matching the naked-eye pair Mizar–Alcor; BS 13.5 places Vasiṣṭha second from the east, matching Mizar's position next to Alkaid. The Mizar/Alcor = Vasiṣṭha/Arundhatī pairing is the standard identification in Indian astronomy.</sub>

### अङ्गिरस् (Aṅgiras) — Alioth

**Modern identification:** Alioth — ε Ursae Majoris, Ursa Major (*likely*)

**Bṛhat Saṃhitā 13.5** — [Sanskrit e-text](https://sa.wikisource.org/wiki/बृहत्संहिता/अध्यायः_१३)

> पूर्वे भागे भगवान्मरीचिरपरे स्थितो वसिष्ठो +अस्मात् ।
> तस्याङ्गिरास्ततो +अत्रिस्तस्यासन्नः पुलस्त्यश्च ।। १३.०५ ।।
>
> — *The eastern-most of the group is Bhagavan Marichi; the next to him is Vasishtha; the next is Angirasa and the next two are Atri and Pulastya.*
> <br>— N. Chidambaram Iyer (1884), ch. XIII v. 5, p. 81 ([source](https://archive.org/details/bihatsahitvarah00iyergoog))

<sub>**Identification notes (Bṛhat Saṃhitā):** Third from the east in the order given by BS 13.5 (after Marīci and Vasiṣṭha); reading that order onto the Dipper with Mizar anchored by Arundhatī gives Alioth. Conventional assignment consistent with, but not explicitly stated in, the classical text.</sub>

### अत्रि (Atri) — Megrez

**Modern identification:** Megrez — δ Ursae Majoris, Ursa Major (*likely*)

**Bṛhat Saṃhitā 13.5** — [Sanskrit e-text](https://sa.wikisource.org/wiki/बृहत्संहिता/अध्यायः_१३)

> पूर्वे भागे भगवान्मरीचिरपरे स्थितो वसिष्ठो +अस्मात् ।
> तस्याङ्गिरास्ततो +अत्रिस्तस्यासन्नः पुलस्त्यश्च ।। १३.०५ ।।
>
> — *The eastern-most of the group is Bhagavan Marichi; the next to him is Vasishtha; the next is Angirasa and the next two are Atri and Pulastya.*
> <br>— N. Chidambaram Iyer (1884), ch. XIII v. 5, p. 81 ([source](https://archive.org/details/bihatsahitvarah00iyergoog))

<sub>**Identification notes (Bṛhat Saṃhitā):** Fourth from the east in the BS 13.5 order; conventional mapping onto the Dipper gives Megrez. Same caveat as the other rishis: BS gives the order, not the star-by-star assignment.</sub>

### पुलस्त्य (Pulastya) — Phecda

**Modern identification:** Phecda — γ Ursae Majoris, Ursa Major (*likely*)

**Bṛhat Saṃhitā 13.5** — [Sanskrit e-text](https://sa.wikisource.org/wiki/बृहत्संहिता/अध्यायः_१३)

> पूर्वे भागे भगवान्मरीचिरपरे स्थितो वसिष्ठो +अस्मात् ।
> तस्याङ्गिरास्ततो +अत्रिस्तस्यासन्नः पुलस्त्यश्च ।। १३.०५ ।।
>
> — *The eastern-most of the group is Bhagavan Marichi; the next to him is Vasishtha; the next is Angirasa and the next two are Atri and Pulastya.*
> <br>— N. Chidambaram Iyer (1884), ch. XIII v. 5, p. 81 ([source](https://archive.org/details/bihatsahitvarah00iyergoog))

<sub>**Identification notes (Bṛhat Saṃhitā):** Fifth from the east in the BS 13.5 order; conventional mapping gives Phecda. BS gives the order only.</sub>

### पुलह (Pulaha) — Merak

**Modern identification:** Merak — β Ursae Majoris, Ursa Major (*likely*)

**Bṛhat Saṃhitā 13.6** — [Sanskrit e-text](https://sa.wikisource.org/wiki/बृहत्संहिता/अध्यायः_१३)

> पुलहः क्रतुरिति भगानासन्ना अनुक्रमेण *पूर्वाद्यात्[क्.पूर्वाद्याः] ।
> तत्र वसिष्ठं मुनिवरं उपाश्रितारुन्धती साध्वी ।। १३.०६ ।।
>
> — *The next in order are the Rishis Pulaha and Kratu. The chaste Arundhati closely attends her husband the sage Vasishtha.*
> <br>— N. Chidambaram Iyer (1884), ch. XIII v. 6, p. 81 ([source](https://archive.org/details/bihatsahitvarah00iyergoog))

<sub>**Identification notes (Bṛhat Saṃhitā):** Sixth from the east in the BS 13.5–6 order; conventional mapping gives Merak. BS gives the order only.</sub>

### क्रतु (Kratu) — Dubhe

**Modern identification:** Dubhe — α Ursae Majoris, Ursa Major (*likely*)

**Bṛhat Saṃhitā 13.6** — [Sanskrit e-text](https://sa.wikisource.org/wiki/बृहत्संहिता/अध्यायः_१३)

> पुलहः क्रतुरिति भगानासन्ना अनुक्रमेण *पूर्वाद्यात्[क्.पूर्वाद्याः] ।
> तत्र वसिष्ठं मुनिवरं उपाश्रितारुन्धती साध्वी ।। १३.०६ ।।
>
> — *The next in order are the Rishis Pulaha and Kratu. The chaste Arundhati closely attends her husband the sage Vasishtha.*
> <br>— N. Chidambaram Iyer (1884), ch. XIII v. 6, p. 81 ([source](https://archive.org/details/bihatsahitvarah00iyergoog))

<sub>**Identification notes (Bṛhat Saṃhitā):** Last (westernmost) in the BS 13.5–6 east-to-west order; conventional mapping gives Dubhe, the western 'pointer'. BS gives the order only.</sub>

### अरुन्धती (Arundhatī) — Alcor, the faint companion of Mizar in the Big Dipper's handle

**Modern identification:** Alcor, the faint companion of Mizar in the Big Dipper's handle — 80 Ursae Majoris, Ursa Major (*certain*)

*See also:* `vasishtha`

**Āśvalāyana Gṛhya Sūtra 1.7.22** — [Sanskrit e-text](https://sa.wikisource.org/wiki/आश्वलायनगृह्यसूत्रम्/अध्यायः_१)

> ध्रुवमरुन्धतीं सप्तऋषीनिति दृष्ट्वा वाचं विसृजेत जीवपत्नीं प्रजां विन्देयेति २२
>
> — *When she sees the polar-star, the star Arundhati, and the seven Rishis (ursa major), let her break the silence (and say), 'May my husband live and I get offspring.'*
> <br>— Hermann Oldenberg, SBE vol. 29 (1886) ([source](https://sacred-texts.com/hin/sbe29/sbe29.txt) · [mirror](https://web.archive.org/web/20080113225826/http://sacred-texts.com/hin/sbe29/sbe29.txt))

<sub>**Identification notes (Vedic corpus):** Wife of the rishi Vasiṣṭha (= Mizar, ζ UMa), shown to the bride as the model of conjugal fidelity; the pan-Indian tradition of arundhatī-darśana fixes the identification with Alcor securely.</sub>

**Bṛhat Saṃhitā 13.6 (cf. 13.4, Kern's variant)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/बृहत्संहिता/अध्यायः_१३)

> पुलहः क्रतुरिति भगानासन्ना अनुक्रमेण *पूर्वाद्यात्[क्.पूर्वाद्याः] ।
> तत्र वसिष्ठं मुनिवरं उपाश्रितारुन्धती साध्वी ।। १३.०६ ।।
>
> — *They rise in the North-East and are accompanied by the chaste Arundhati, the consort of Vasishtha. ... The chaste Arundhati closely attends her husband the sage Vasishtha.*
> <br>— N. Chidambaram Iyer (1884), ch. XIII vv. 4 and 6, p. 81 ([source](https://archive.org/details/bihatsahitvarah00iyergoog))

<sub>**Identification notes (Bṛhat Saṃhitā):** BS 13.6 states that the chaste Arundhatī closely attends Vasiṣṭha, best of sages — exactly the naked-eye companion Alcor beside Mizar; the pair is the classic Indian eyesight test. Kern's variant of BS 13.4 (recorded in the e-text apparatus as क्. प्रागुत्तरतश्च एते सदा उदयन्ते ससाध्वीकाः) says the rishis rise in the north-east 'accompanied by the sādhvī', i.e. Arundhatī, which Iyer's v. 4 translates. Note: Utpala's tradition (Iyer p. 81 n.) holds the visible star is not the 'real' Arundhatī, said to be a sūkṣma-tārā (minute star) very close to Vasiṣṭha.</sub>

## Vedic asterisms and archaic names

Older names from the Saṃhitā/Brāhmaṇa layer: the individually named Kṛttikās, archaic nakshatra names, and the celestial Orion tableau of Aitareya Brāhmaṇa 3.33.

### अम्बा, दुला, नितत्नी, अभ्रयन्ती, मेघयन्ती, वर्षयन्ती, चुपुणीका (Ambā, Dulā, Nitatnī, Abhrayantī, Meghayantī, Varṣayantī, Cupuṇīkā) — the seven individual stars of the Pleiades

**Modern identification:** the seven individual stars of the Pleiades — brightest members: η, 27, 17, 20, 23, 19, 28 Tauri (no secure one-to-one mapping), Taurus (*likely*)

*See also:* `krittika`

**Taittirīya Brāhmaṇa 3.1.4.1** — [Sanskrit e-text](https://sa.wikisource.org/wiki/तैत्तिरीयब्राह्मणम्_(विस्वरपाठः)

> अग्निर्वा अकामयत । अन्नादो देवानाꣳ स्यामिति । स एतमग्नये कृत्तिकाभ्यः पुरोडाशमष्टाकपालं निरवपत् । ततो वै सोऽन्नादो देवानामभवत् । अग्निर्वै देवानामन्नादः । यथा ह वा अग्निर्देवनामन्नादः । एवꣳ ह वा एष मनुष्याणां भवति । य एतेन हविषा यजते । य उ चैनदेवं वेद । सोऽत्र जुहोति । अग्नये स्वाहा कृत्तिकाभ्यः स्वाहा । अम्बायै स्वाहा दुलायै स्वाहा । नितत्न्यै स्वाहाभ्रयन्त्यै स्वाहा । मेघयन्त्यै स्वाहा वर्षयन्त्यै स्वाहा । चुपुणीकायै स्वाहेति १
>
> — *[Paraphrase] Agni desired: 'May I be the eater of food of the gods.' He offered an eight-potsherd cake to Agni of the Krittikas, and thereby became the food-eater of the gods... He makes offering with: 'To Agni svaha! To the Krittikas svaha! To Amba svaha! To Dula svaha! To Nitatni svaha! To Abhrayanti svaha! To Meghayanti svaha! To Varshayanti svaha! To Cupunika svaha!' No public-domain English translation of the Taittiriya Brahmana exists; rendering above is the researcher's own paraphrase of the Sanskrit. Cf. P.-E. Dumont, 'The Ishtis to the Nakshatras (or Oblations to the Lunar Mansions) of the Taittiriya-Brahmana', Proceedings of the American Philosophical Society 98.3 (1954), pp. 204-223 (copyrighted, not quoted).*
> <br>— Researcher's paraphrase (no public-domain translation); cf. P.-E. Dumont (1954) ([source](https://www.jstor.org/stable/i344439))

<sub>**Identification notes (Vedic corpus):** The Taittirīya Brāhmaṇa names seven individual Kṛttikās in the svāhā-calls of the Agni-Kṛttikā offering; several names are rain/cloud words (Abhrayantī 'bringing clouds', Meghayantī 'making clouds', Varṣayantī 'raining'). The group = Pleiades is certain; which Vedic name maps to which star cannot be determined.</sub>

### रोहिणी (द्वितीया; = ज्येष्ठा) (Rohiṇī (second; = Jyeṣṭhā)) — Antares

**Modern identification:** Antares — α Scorpii, Scorpius (*likely*)

*See also:* `jyeshtha`, `rohini`

**Taittirīya Saṃhitā 4.4.10.2** — [Sanskrit e-text](https://sa.wikisource.org/wiki/तैत्तिरीयसंहिता(विस्वरः)

> अनूराधा नक्षत्रम् मित्रो देवता रोहिणी नक्षत्रम् इन्द्रो देवता विचृतौ नक्षत्रम् पितरो देवता
>
> — *Anruradha the Naksatra, Mitra the deity; Rohini the Naksatra, Indra the deity; the two Viçrts the Naksatra; the fathers the deity.*
> <br>— A.B. Keith, The Veda of the Black Yajus School (1914) ([source](https://www.sacred-texts.com/hin/yv/yv04.htm) · [mirror](https://web.archive.org/web/20210301091213/https://www.sacred-texts.com/hin/yv/yv04.htm))

<sub>**Identification notes (Vedic corpus):** TS 4.4.10 lists a SECOND Rohini with deity Indra, standing between Anuradha and Vicrtau (= Mula) - i.e. in the position of the later Jyestha. Antares, the other great red star of the zodiacal belt, evidently also bore the name 'the red one'; later lists rename it Jyeṣṭhā (so already TB 1.5.1 and AV 19.7.3).</sub>

### इन्वकाः (इन्वगाः) (Invakāḥ (Invagāḥ)) — alternative Taittirīya name of Mṛgaśīrṣa - the stars of Orion's head

**Modern identification:** alternative Taittirīya name of Mṛgaśīrṣa - the stars of Orion's head — λ, φ1, φ2 Orionis, Orion (*likely*)

*See also:* `mrigashirsha`

**Taittirīya Brāhmaṇa 1.5.1.1; 3.1.4.3** — [Sanskrit e-text](https://sa.wikisource.org/wiki/तैत्तिरीयब्राह्मणम्_(विस्वरपाठः) · [mirror](https://sa.wikisource.org/wiki/तैत्तिरीयब्राह्मणम्_(विस्वरपाठः)

> अग्नेः कृत्तिकाः । शुक्रं परस्ताज्ज्योतिरवस्तात् । प्रजापते रोहिणी ।आपः परस्तादोषधयोऽवस्तात् । सोमस्येन्वका । विततानि परस्ताद्वयन्तोऽवस्तात् । रुद्रस्य बाहू ।मृगयवः परस्ताद्विक्षारोऽवस्तात् । अदित्यै पुनर्वसू ।वातः परस्तादार्द्रमवस्तात् १ || सोमो वा अकामयत । ओषधीनाꣳ राज्यमभिजयेयमिति । स एतꣳ सोमाय मृगशीर्षाय श्यामाकं चरुं पयसि निरवपत् । ततो वै स ओषधीनाꣳ राज्यमभ्यजयत् । समानानाꣳ ह वै राज्यमभिजयति । य एतेन हविषा यजते । य उ चैनदेवं वेद । सोऽत्र जुहोति । सोमाय स्वाहा मृगशीर्षाय स्वाहा । इन्वकाभ्यः स्वाहौषधीभ्यः स्वाहा । राज्याय स्वाहाभिजित्यै स्वाहेति ३
>
> — *[Paraphrase of TB 1.5.1.1] The Krittikas are Agni's; brightness above, light below. Rohini is Prajapati's; the waters above, the plants below. The Invakas are Soma's; things spread out above, the weavers below. The Bahu (the two Arms) are Rudra's; hunters above, ... below. The two Punarvasus are Aditi's; wind above, moisture below. [TB 3.1.4.3] Soma desired: 'May I win the kingship of the plants'; he offered a caru of millet in milk to Soma of Mrgasirsha... 'To Soma svaha! To Mrgasirsha svaha! To the Invakas svaha! To the plants svaha!' No public-domain English translation of the Taittiriya Brahmana exists; rendering above is the researcher's own paraphrase of the Sanskrit. Cf. P.-E. Dumont (1954), copyrighted, not quoted.*
> <br>— Researcher's paraphrase (no public-domain translation); cf. P.-E. Dumont (1954) ([source](https://www.jstor.org/stable/i344439))

<sub>**Identification notes (Vedic corpus):** In the Taittirīya tradition Soma's nakshatra is called Invakā where other lists have Mṛgaśīrṣa: TB 1.5.1.1 'somasyenvakā', and TB 3.1.4.3 invokes Mṛgaśīrṣa and the Invakās side by side in the same offering, proving the equation.</sub>

### बाहू (रुद्रस्य) (Bāhū (Rudrasya)) — 'the two Arms' of the deer/Orion: usually taken as Betelgeuse and Bellatrix

**Modern identification:** 'the two Arms' of the deer/Orion: usually taken as Betelgeuse and Bellatrix — α Orionis and γ Orionis, Orion (*disputed*)

*See also:* `ardra`

**Taittirīya Brāhmaṇa 1.5.1.1** — [Sanskrit e-text](https://sa.wikisource.org/wiki/तैत्तिरीयब्राह्मणम्_(विस्वरपाठः)

> रुद्रस्य बाहू ।मृगयवः परस्ताद्विक्षारोऽवस्तात्
>
> — *[Paraphrase] Of Rudra are the two Arms (Bahu); the hunters above, ... below. No public-domain English translation of the Taittiriya Brahmana exists; rendering above is the researcher's own paraphrase of the Sanskrit. Cf. P.-E. Dumont (1954), copyrighted, not quoted.*
> <br>— Researcher's paraphrase (no public-domain translation); cf. P.-E. Dumont (1954) ([source](https://www.jstor.org/stable/i344439))

<sub>**Identification notes (Vedic corpus):** TB 1.5.1 gives Rudra's nakshatra as the dual Bāhū 'the two arms' in place of Ārdrā, fitting the picture of the celestial deer (Orion): the two bright shoulder stars Betelgeuse + Bellatrix. Which two stars are meant is not stated in the text; Betelgeuse-Bellatrix is the common scholarly reading, and the mention of 'hunters' (mṛgayavaḥ) alongside is part of the same Orion tableau.</sub>

### तिष्यः (Tiṣya) — the later Puṣya: the Asellus stars and Praesepe region

**Modern identification:** the later Puṣya: the Asellus stars and Praesepe region — γ, δ, θ Cancri (δ Cancri = Asellus Australis nearest the ecliptic), with the Praesepe cluster M44, Cancer (*likely*)

*See also:* `pushya`

**Taittirīya Saṃhitā 4.4.10.1** — [Sanskrit e-text](https://sa.wikisource.org/wiki/तैत्तिरीयसंहिता(विस्वरः)

> तिष्यो नक्षत्रम् बृहस्पतिर् देवता
>
> — *Tisya the Naksatra, Brhaspati the deity.*
> <br>— A.B. Keith, The Veda of the Black Yajus School (1914) ([source](https://www.sacred-texts.com/hin/yv/yv04.htm) · [mirror](https://web.archive.org/web/20210301091213/https://www.sacred-texts.com/hin/yv/yv04.htm))

<sub>**Identification notes (Vedic corpus):** Tiṣya, deity Bṛhaspati, is the archaic name that the AV (19.7.2) and all later lists call Puṣya; Whitney's note to AV 19.7 flags this TS/AV name difference explicitly. A faint asterism: identification rests on its fixed position between Punarvasū (Castor/Pollux) and Āśleṣā, hence 'likely' rather than 'certain'. Also TB 3.1.1.5, TB 3.1.4.6 (Bṛhaspati-Tiṣya offering).</sub>

### मृगः (प्रजापतिः) (Mṛga (Prajāpati)) — the celestial deer = Orion

**Modern identification:** the celestial deer = Orion — constellation Orion (head λ Ori; body the Belt region), Orion (*likely*)

*See also:* `mrigashirsha`, `mrigavyadha`, `ishus-trikanda`

**Aitareya Brāhmaṇa 3.33** — [Sanskrit e-text](https://sa.wikisource.org/wiki/ऐतरेय_ब्राह्मणम्/पञ्चिका_३_(तृतीय_पञ्चिका)

> प्रजापतिर्वै स्वां दुहितरमभ्यध्यायद्दिवमित्यन्य आहुरुषसमित्यन्ये तामृश्यो भूत्वा रोहितं भूतामभ्यैत् ... तमभ्यायत्याविध्यत्स विद्ध ऊर्ध्व उदप्रपतत्तमेतं मृग इत्याचक्षते य उ एव मृगव्याधः स उ एव स या रोहित्सा रोहिणी यो एवेषुस्त्रिकाण्डा सो एवेषुस्त्रिकाण्डा।
>
> — *Prajapati felt love towards his own daughter, the sky some say, Usas others. Having become a stag he approached her in the form of a deer. ... Having aimed at him he pierced him; being pierced he flew upwards; him they call 'the deer'. The piercer of the deer is he of that name. The female deer is Rohini; the three-pointed arrow is the three-pointed arrow.*
> <br>— A.B. Keith, Rigveda Brahmanas, HOS 25 (1920), pp. 185-186 ([source](https://archive.org/details/rigvedabrahmana00keitgoog) · [mirror](https://archive.org/download/rigvedabrahmana00keitgoog/rigvedabrahmana00keitgoog_djvu.txt))

<sub>**Identification notes (Vedic corpus):** The Prajapati-Rudra myth read astronomically: Prajapati, become a deer pursuing his daughter (Rohiṇī, the red doe = Aldebaran), is pierced and 'they call him the deer (mṛga)' in the sky. The astronomical reading (Orion) is standard scholarship since Weber; Keith's own footnote records that 'the astronomical data here given afford Tilak the source of his work Orion.' The text names the asterisms but not the modern stars, hence 'likely'. Cf. ŚB 2.1.2.8-9 where Mṛgaśīrṣa is the pierced Prajapati's head/body.</sub>

### इषुस्त्रिकाण्डा (Iṣus trikāṇḍā) — Orion's Belt - Mintaka, Alnilam, Alnitak - as the 'three-jointed arrow'

**Modern identification:** Orion's Belt - Mintaka, Alnilam, Alnitak - as the 'three-jointed arrow' — δ, ε, ζ Orionis, Orion (*likely*)

*See also:* `mriga`

**Aitareya Brāhmaṇa 3.33; cf. Śatapatha Brāhmaṇa 2.1.2.9** — [Sanskrit e-text](https://sa.wikisource.org/wiki/ऐतरेय_ब्राह्मणम्/पञ्चिका_३_(तृतीय_पञ्चिका)

> तमभ्यायत्याविध्यत्स विद्ध ऊर्ध्व उदप्रपतत्तमेतं मृग इत्याचक्षते य उ एव मृगव्याधः स उ एव स या रोहित्सा रोहिणी यो एवेषुस्त्रिकाण्डा सो एवेषुस्त्रिकाण्डा।
>
> — *The female deer is Rohini; the three-pointed arrow is the three-pointed arrow. [ŚB 2.1.2.9, tr. Eggeling: 'when they (the gods) on that occasion pierced him with what is called the three-knotted arrow, he abandoned that body'.]*
> <br>— A.B. Keith, Rigveda Brahmanas, HOS 25 (1920); Julius Eggeling, SBE 12 (1882) ([source](https://archive.org/details/rigvedabrahmana00keitgoog) · [mirror 1](https://archive.org/download/rigvedabrahmana00keitgoog/rigvedabrahmana00keitgoog_djvu.txt) · [mirror 2](https://www.sacred-texts.com/hin/sbr/sbe12/sbe1241.htm) · [mirror 3](https://web.archive.org/web/20210506123309/https://www.sacred-texts.com/hin/sbr/sbe12/sbe1241.htm))

<sub>**Identification notes (Vedic corpus):** The 'three-parted arrow' shot at Prajapati; the three aligned Belt stars piercing the deer's body. The same arrow appears in ŚB 2.1.2.9 ('iṣuṇā trikāṇḍena' - Eggeling: 'the three-knotted arrow') as the reason Prajapati abandoned the body that is Mṛgaśīrṣa's vicinity. Standard astronomical reading (Weber, Tilak); the text does not name the stars.</sub>

## Collective catalogs

Star-catalog passages that treat the yogatārās as a set.

### अश्विन्यादीनां साभिजितां योगताराः (Aśvinyādi yogatārāḥ (sābhijit)) — collective catalog of 28 junction stars

**Modern identification:** collective catalog of 28 junction stars — various, various (zodiacal belt and beyond) (*likely*)

**Siddhānta Śiromaṇi, Grahagaṇitādhyāya, Bhagrahayutyadhikāra vv.1-6; cf. Golādhyāya, Dṛkkarmavāsanā v.12** — [Sanskrit e-text](https://sa.wikisource.org/wiki/पृष्ठम्:सिद्धान्तशिरोमणिः.djvu/346) · [mirror](https://sa.wikisource.org/wiki/पृष्ठम्:सिद्धान्तशिरोमणिः.djvu/348)

> अष्टौ नखा गजगुणाः खशरास्त्रिषट्काः सप्तर्तवस्त्रिनव चाङ्गदशोऽष्टकाष्ठाः । गोऽकस्तथाद्रिमनवः शरबाणचन्द्राः खात्यष्टयस्त्रिधृतयो नवनन्दचन्द्राः ।।१।। अर्काधिनो जिनयमा नवबाहुदस्राः कब्ध्यश्चिनो जलधितत्त्वमिताश्च भागाः । षटयश्विनश्वपवनोत्कृतयोऽष्ट्रभानिखाडूश्विनी नखगुणा रसदन्तसंख्याः ॥२॥ सप्तामराः खमिति भध्रुवका निरुक्ता दृकर्मणायनभवेन सहाश्विधिष्ण्यात् । ब्रह्माग्निभधुवलवा रदलितिकोना मैत्रन्द्रयोद्वर्यधिपभस्य च सेषुलिसाः ॥३॥ [vv.1-3, dhruvakas; verbatim from unproofread OCR — several word-numerals visibly garbled] … दिशोऽकश्च सार्धाब्धयः सार्धवेदा दशेशा रसाः खं स्वराः खं च सूर्याः । त्रिचन्द्राः कुचन्द्रा विपादौ च दस्रौ तुरङ्गाग्नयः सत्रिभागं च रूपम् ॥४॥ विपादं द्वयं सार्थरामाश्च सार्धा गजाः सत्रिभागेषवो मार्गणाश्च । द्विषष्टिः खरामाश्च षड्वर्गसंख्यास्त्रिभागो जिना उत्कृतिः खं च भानाम् ॥५॥ निरुक्ताः स्फुटा योगताराशरांशास्त्रय ब्रह्मधिष्ण्याद्विशाखादिषट्कम् । करो वारुणं त्वाष्ट्रभं सार्पमेषां शरा दक्षिणा उत्तराः शेषभानाम् ।॥६॥ [vv.4-6, śaras]
>
> — *No public-domain translation of these Gaṇitādhyāya verses exists online. Bhāskara's own conception of this catalog is however translated in the public-domain 1861 rendering of Golādhyāya, Dṛkkarma-vāsanā v.12: '12. As the constellations are fixed their latitudes as given in the books of these curly [read: early] astronomers are the bpasuat-b'aras [read: spashta-śaras], i.e. tho reduced values of the latitudes so as to render them fit to be added to or subtracted from the declination; and tho dhkuvas [read: dhruvas] or longitude of these constellations are given, after being corrected by tho ayana drtkkakma [read: drikkarma] so as to suit those corrected latitudes that is, the star will appear to rise at the equator at the same time with longitude found by the correction.' [verbatim from OCR of the 1861 edition, bracketed restorations of obvious OCR errors added]*
> <br>— Lancelot Wilkinson, revised by Bapu Deva Sastri (1861), public domain (for Golādhyāya IX.12); Gaṇitādhyāya vv.1-6 values paraphrased from Arkasomayaji. ([source](https://archive.org/details/in.ernet.dli.2015.46927))

<sub>**Identification notes (Siddhānta Śiromaṇi):** Bhāskara gives the polar longitudes (vv.1-3) and rectified latitudes (vv.4-6) of all 28 yogatārās in bhūtasaṅkhyā word-numerals, stating (bhāṣya) that Kṛttikā and Rohiṇī are to be diminished by 32' and Viśākhā, Anurādhā, Jyeṣṭhā increased by 5': 'कृत्तिकारोहिणीनक्षत्रयोद्वत्रिशत्कलोनाः । विशाखानुराधाज्येष्ठानां कलापञ्चकेनाधिका ध्रुवकभागा वेदितव्याः' (sa.wikisource p.347). Per Arkasomayaji the base values are Brahmagupta's, copied also by Śrīpati. Standard traditional identifications for the brightest members, as printed in the public-domain 1861 volume (Sūrya Siddhānta portion, pp.63-68): Svātī = Arcturus, Citrā = Spica, Jyeṣṭhā = Antares, Punarvasu = β Geminorum, Rohiṇī = Aldebaran (α Tauri), Maghā = Regulus, Kṛttikā = Pleiades (η Tauri), Hasta = δ Corvi, Śravaṇa = α Aquilae, Dhaniṣṭhā = α Delphini, Viśākhā = α Librae, Aśvinī = α(β) Arietis, Revatī = ζ Piscium. Individual per-star numeric values in the online OCR tables are too corrupted to transcribe reliably.</sub>

## Caveats, per source

These are the working caveats recorded during compilation — read them before treating any entry as final.

### Sūrya Siddhānta

- Burgess's translation is NOT on sacred-texts.com; the public-domain translation was taken from two archive.org scans: the original JAOS vol. 6 printing (1860, item jstor-592174) and the 1935 Calcutta University reprint ed. Gangooly (item SuryaSiddhantaTranslation). Both full-text files were downloaded and read.
- Burgess quotations were transcribed from the archive.org OCR of the 1860 printing and cross-checked against the 1935 reprint's OCR; obvious OCR misreads were corrected, and Burgess's vowel diacritics (â, î, û, ç) are only partially reproduced because the OCR strips them inconsistently. Wording and word order are otherwise verbatim.
- The Devanagari e-text is the Sanskrit Wikisource page 'सूर्यसिद्धान्त भग्रहयुत्यधिकारः' (chapter 8, labelled [नक्षत्रग्रहयुति], verses ८.०१-८.२१). It follows GRETIL-style analytic conventions: spaces at pada boundaries, '+अ' marking a sandhi-elided initial vowel, and क/ख labels for verse halves. Verses were copied character-for-character; only the ka/kha half-verse labels and wiki markup were dropped and halves joined with the '/' and '//' dandas as printed.
- Chapter 8 does not list the 27 nakshatra names as a roll-call: vv. 2-9 give positions as bare number-words 'for Açvini (dasra), etc., in succession' (v. 9); individual names occur only in vv. 4-5 (Uttara/Purva-Ashadha, Abhijit, Çravana, Çravishtha, Açvini) and vv. 16-19 (junction-star rules). Ārdrā, Svātī, Citrā and Śatabhiṣaj are never named as junction-star rules' subjects; their entries cite the sthūla ('great/brightest') catch-all of 8.19, plus 8.21 for Citrā where it is named as a reference star.
- Disputed or qualified identifications per Burgess's own commentary: Bharaṇī (35 vs 41 Arietis), Ārdrā (α Orionis vs the position-matching 135 Tauri), Āśleṣā (ε Hydrae vs Colebrooke's α Cancri), P. Phalgunī (δ vs θ Leonis in other siddhāntas), Hasta (γ vs δ Corvi), Viśākhā ('more doubtful than any other asterism'; ι Librae vs original α+β Librae), Mūla (λ Scorpii), U. Āṣāḍhā (σ vs Colebrooke's τ Sagittarii), U. Bhādrapadā (longitude of γ Pegasi combined with latitude of α Andromedae), Prajāpati (δ Aurigae), Apāṃvatsa (θ Virginis vs Colebrooke's unidentifiable 'b 1,2,3 Virginis').
- Burgess considers vv. 16-21 possibly 'a later addition to its original content' and of 'inferior authority' compared with the polar-longitude/latitude determinations of vv. 1-12.
- Modern common names (Sheratan, Meissa, Zosma, Gienah, Dschubba, Kaus Media, Nunki, Rotanev, Hydor, Markab, Algenib, Alpheratz, Elnath, Minelauva) and the constellation 'Carina' for Burgess's 'α Argūs/α Navis' are modern conventions supplied by the researcher, not by Burgess.
- GRETIL's own URL for the Sūrya-Siddhānta e-text now returns 404 after the site reorganization, so only the Wikisource mirror of that e-text is cited.
- Burgess describes Abhijit's junction star as 'the brightest in a group of three', citing a verse reference '(v. 10)' that does not match ch. 8 v. 10 (which concerns Agastya); the brightest-star rule actually derives from the sthūla clause of v. 19.

### Vedic corpus

- Sanskrit passages are copied verbatim from the Sanskrit Wikisource e-texts listed in shloka_source_url (fetched 2026-07-24 via the MediaWiki raw API); only wiki markup and editor footnote tags were removed and whitespace collapsed. The e-texts carry their own quirks preserved here, e.g. the anusvara sign ꣳ and inconsistent danda spacing.
- AV 19.7.1 as transmitted reads 'turmiśaṁ', a corrupt word; Whitney emends to aṣṭāviṅśáṁ 'twenty-eight-fold'. The Wikisource text prints the transmitted reading.
- Translations quoted are public domain: A.B. Keith 1914 (TS), Julius Eggeling 1882 (ŚB, SBE 12), Hermann Oldenberg 1886 (ĀGS, SBE 29), W.D. Whitney 1905 (AV, HOS 8), A.B. Keith 1920 (AB, HOS 25). sacred-texts.com blocks automated fetching, so its pages were retrieved through Wayback Machine snapshots given in translation_source_url; Whitney and Keith 1920 were taken from archive.org scans. OCR artifacts and italic-markup splits were normalized without changing wording; diacritics are simplified.
- No complete public-domain English translation of the Taittirīya Brāhmaṇa exists. TB 1.5.1 and 3.1.x renderings here are the researcher's own paraphrases of the Sanskrit, with reference to P.-E. Dumont, 'The Ishtis to the Nakshatras of the Taittiriya-Brahmana', PAPS 98.3 (1954), pp. 204-223 (copyrighted, cited but not quoted). TB 3.1.1-2 contains full nakshatra mantras with presiding deities matching TS 4.4.10.
- Nakshatras are asterisms (star groups); the single 'junction star' (yogatārā) equations used in the modern_star fields come from later siddhantic astronomy and modern scholarship, not from the Vedic texts themselves, which never cite coordinates. Identifications are secure for bright unmistakable groups (Pleiades, Aldebaran, Big Dipper, Alcor), and inferential for faint ones (Tishya/Pushya) and for the Orion-Sirius reading of AB 3.33 (accepted since Weber and Tilak's 'Orion', noted in Keith's footnote, but the text names no stars).
- TS 4.4.10 contains two Rohinis: the Prajapati-Rohini (Aldebaran) and a second Indra-Rohini in the position of later Jyeshtha (Antares); TS also shows archaic names Tisya (= later Pushya), Vicrtau (= later Mula), Apabharani, and Srona (= later Sravana). TB 1.5.1 adds Invaka (= Mrgasirsha), Bahu (= Ardra) and Nishtya (= Svati). The AV 19.7 list has 28 nakshatras (including Abhijit = Vega); the TS list 27 with some names doubled.
- The Krittika east-rising statement (ŚB 2.1.2.3) and the Dhruva pole-star problem are both entangled in contested chronology: the Pleiades sat on the celestial equator c. 3000-2500 BCE (Dikshit's dating argument), and no bright pole star existed c. 1500 BCE (Thuban served c. 2800 BCE; Polaris only in recent centuries). Both facts are reported here descriptively; the entries take no position on text dating.
- ĀGS 1.7.22 numbering follows the Wikisource e-text and Oldenberg (Adhyaya 1, Kandika 7, sutra 22); the mantra 'dhruvam asi' cited in some secondary literature for the dhruva-darshana belongs to the parallel rite in other Grhya texts (e.g. Śāṅkhāyana GS 1.17.3, quoted under the Dhruva entry from the same Oldenberg volume).

### Bṛhat Saṃhitā

- All Devanagari was copied verbatim from the Sanskrit Wikisource e-texts fetched during this session (raw wikitext via action=raw). The Wikisource Bṛhat Saṃhitā derives from the Yano–Sugita digitization of A.V. Tripathi's edition and retains its editorial apparatus verbatim: '+' marks an editorially resolved avagraha/sandhi (e.g. वसिष्ठो +अस्मात् = वसिष्ठोऽस्मात्), and *reading[क्.variant] records H. Kern's edition's variant. These markers were preserved, not silently removed.
- Cross-check: BS 13.05 in the GRETIL e-text reads 'pūrve bhāge bhagavān marīcir apare sthito vasiṣṭho +asmāt', agreeing with the Wikisource Devanagari.
- The rishi→star mapping (Kratu=Dubhe … Marīci=Alkaid) is NOT stated star-by-star in the Bṛhat Saṃhitā or any classical text found; what BS 13.5–6 does give is the east-to-west order of the seven names plus Arundhatī's position beside Vasiṣṭha. The conventional Bayer assignments follow uniquely from that order once Vasiṣṭha is anchored to Mizar by Arundhatī = Alcor, hence 'certain' for Mizar/Alcor and 'likely' (conventional but well-founded) for the rest.
- Iyer's 1884 translation is public domain and quoted verbatim except for correction of obvious OCR errors in the archive.org text; hyphenation/line breaks joined. In Burgess's note, OCR 'a Cards Majoris' was restored to 'α Canis Majoris'. M.R. Bhat's 1981 translation was not used.
- Per Utpala's commentary as reported in Iyer's footnote (p. 81), the śāstras hold that the visible companion of Vasiṣṭha is not the 'real' Arundhatī, described as a sūkṣma-tārā (minute/telescopic star) very close to Vasiṣṭha — worth flagging in a scholarly database entry for Alcor.
- Kathāsaritsāgara verse numbering: Wikisource/GRETIL cite it as lambaka 6, taraṅga 2, v. 88 (sokss_6,2.88); Monier-Williams and Tawney cite the same verse by continuous taraṅga as 28.88.
- The Sūrya-siddhānta chapter containing 8.10 is titled Bhagrahayutyadhikāra on Wikisource; Burgess's translation (1860, public domain, pp. 245–246) numbers it chapter viii and identifies Agastya = 'α Navis, or Canopus' and Mṛgavyādha/Lubdhaka = Sirius, crediting Colebrooke's identifications.
- BS chapter 12 (Agastyacāra) names Agastya in vv. 7, 11, 12, 13, 19 and by implication throughout; v. 7 was chosen as the representative shloka. Iyer's chapter/verse numbering aligns with the Sanskrit for both chapters 12 and 13.
- Bṛhat Saṃhitā date: 6th century CE; the Saptarṣi-cāra chapter explicitly ascribes its doctrine to Vṛddha Garga (BS 13.2), so the star lore itself is older.

### Siddhānta Śiromaṇi

- All Devanagari shlokas are verbatim from UNPROOFREAD OCR pages (proofread level 1) on sa.wikisource, transcribing the Sampūrṇānand Sanskrit University 1981 edition of the Grahagaṇitādhyāya with Bhāskara's Vāsanābhāṣya and Nṛsiṃha Daivajña's Vāsanāvārttika (ed. Muralīdhara Chaturvedī). Obvious OCR slips remain (e.g. 'यम्यः' for 'याम्यः', 'तुरखाद्यस्' for 'तुरगाद्रयस्', 'रेवतो.तारां', 'द्विपश्चाशद्' for 'द्विपञ्चाशद्'); they were deliberately NOT silently corrected. Check against a printed edition before publication.
- There is NO public-domain English translation of the Gaṇitādhyāya online: the Wilkinson/Bapu Deva Sastri 1861 'Translation of the Siddhánta Śiromani' covers only the Golādhyāya (13 chapters; verified from its table of contents and general index — Agastya, Mṛgavyādha, Brahmahṛdaya, Yogatārā entries all point to pages of the Sūrya Siddhānta portion). English for the Bhagrahayuti verses is therefore paraphrase of D. Arkasomayaji's copyrighted translation (Tirupati ed., scan fetched from archive.org) or clearly-marked own renderings of the bhāṣya.
- Correction to the task premise: in the Bhagrahayutyadhikāra Bhāskara's own verses individually name ONLY Agastya and Lubdhaka (also 'muni' and 'mṛgaripu', v.12; 'kumbhabhava', v.16). Brahmahṛdaya, Agni, Prajāpati, Apāṃvatsa and Āpas do NOT occur in Bhāskara's mūla or his Vāsanābhāṣya there; Brahmahṛdaya and Mṛgavyādha appear on the same pages only inside Nṛsiṃha Daivajña's Vārttika (17th c.) quoting Sūrya Siddhānta 9.12-18 (footnoted as 'सू० सि० ९ अ०' in the edition, sa.wikisource p.347).
- Bhāskara's dhruva/śara values reproduce Brahmagupta's star table (so also Śrīpati), with Bhāskara's stated corrections of -32' for Kṛttikā and Rohiṇī and +5' for Viśākhā, Anurādhā, Jyeṣṭhā; his catalog is thus not an independent observation record (per Arkasomayaji's commentary, and Bhāskara's own bhāṣya on vv.1-3).
- Key numeric values were cross-confirmed between the Sanskrit OCR and Arkasomayaji: Agastya 87°, śara 77° S; Lubdhaka 86°, śara 40° S; kālāṃśas 12 (Agastya) and 13 (Lubdhaka); Agastya invisible above terrestrial latitude 37°; Abhijit circumpolar above 52°. The full 28-row dhruva/śara tables in both online OCRs are too corrupted for reliable transcription and were not included.
- The 1861 translation quote (Golādhyāya IX.12) is verbatim from the DLI scan's OCR (archive.org item in.ernet.dli.2015.46927), which is noisy; bracketed restorations are marked. The en.wikisource proofread project of the same book exists but its pages are still 'to be proofread'.
- Pañcasiddhāntikā ch. 14 was NOT examined (the two primary texts exhausted the time budget).
- Ecliptic vs polar coordinates: Bhāskara's dhruvas are POLAR longitudes (ayana-dṛkkarma applied) and his śaras 'sphuṭa' (pole-directed) latitudes, as he states in vv.17-21 and in Golādhyāya IX.12; they are not directly comparable to modern ecliptic coordinates without conversion.
