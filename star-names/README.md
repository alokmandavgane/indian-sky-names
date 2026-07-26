# Sanskrit Star Names — Source Database

Authentic references to star names in Sanskrit texts: the original shloka (copied verbatim from online e-texts), a published translation, and the modern identification of each star.

*Generated 2026-07-24. Machine-readable version: [`star-names.json`](star-names.json); per-source research files with full caveats: [`sources/`](sources/).*

**Method.** Compiled from primary Sanskrit e-texts (Sanskrit Wikisource, GRETIL) and public-domain translations (Burgess 1860, Iyer 1884, Keith 1914/1920, Eggeling 1882, Oldenberg 1886, Whitney 1905, Wilkinson & Sastri 1861, Tawney 1880). Devanagari copied verbatim from the cited e-texts; no verse was reconstructed from memory. Copyrighted translations (Bhat 1981, Arkasomayaji, Dumont 1954) are paraphrased and cited, never quoted.

**A note on what the texts actually say.** The Vedic texts name asterisms and deities but never coordinates; the siddhāntas give coordinates for a single junction star (yogatārā) per nakshatra. All modern equations therefore rest on the siddhāntic positions (chiefly as analysed by Burgess 1860) and on continuous tradition; the *confidence* column records where that chain is strong and where it is disputed.

## Summary table

| Sanskrit | IAST | Modern star | Bayer | Confidence | Attested in |
|---|---|---|---|---|---|
| [अश्विनी](#अश्विनी-aśvinī--sheratan) | Aśvinī | Sheratan | β Arietis | certain | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [भरणी](#भरणी-bharaṇī--35-arietis-musca-borealis) | Bharaṇī | 35 Arietis (Musca Borealis) | 35 Arietis | disputed | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [कृत्तिका](#कृत्तिका-kṛttikā--alcyone-pleiades) | Kṛttikā | Alcyone (Pleiades) | η Tauri | certain | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta; Vedic corpus |
| [रोहिणी](#रोहिणी-rohiṇī--aldebaran) | Rohiṇī | Aldebaran | α Tauri | certain | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta; Vedic corpus |
| [मृगशीर्ष](#मृगशीर्ष-mṛgaśīrṣa--meissa) | Mṛgaśīrṣa | Meissa | λ Orionis | certain | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta; Vedic corpus |
| [आर्द्रा](#आर्द्रा-ārdrā--betelgeuse) | Ārdrā | Betelgeuse | α Orionis | disputed | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta; Vedic corpus |
| [पुनर्वसु](#पुनर्वसु-punarvasu--pollux) | Punarvasu | Pollux | β Geminorum | certain | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [पुष्य](#पुष्य-puṣya--asellus-australis) | Puṣya | Asellus Australis | δ Cancri | likely | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta; Vedic corpus |
| [आश्लेषा](#आश्लेषा-āśleṣā--ashlesha) | Āśleṣā | Ashlesha | ε Hydrae | disputed | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [मघा](#मघा-maghā--regulus) | Maghā | Regulus | α Leonis | certain | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [पूर्वफल्गुनी](#पूर्वफल्गुनी-pūrva-phalgunī--zosma) | Pūrva-Phalgunī | Zosma | δ Leonis | likely | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [उत्तरफल्गुनी](#उत्तरफल्गुनी-uttara-phalgunī--denebola) | Uttara-Phalgunī | Denebola | β Leonis | certain | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [हस्त](#हस्त-hasta--gienah) | Hasta | Gienah | γ Corvi | disputed | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [चित्रा](#चित्रा-citrā--spica) | Citrā | Spica | α Virginis | certain | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [स्वाती](#स्वाती-svātī--arcturus) | Svātī | Arcturus | α Boötis | certain | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [विशाखा](#विशाखा-viśākhā--ι-librae) | Viśākhā | ι Librae | ι Librae | disputed | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [अनुराधा](#अनुराधा-anurādhā--dschubba) | Anurādhā | Dschubba | δ Scorpii | certain | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [ज्येष्ठा](#ज्येष्ठा-jyeṣṭhā--antares) | Jyeṣṭhā | Antares | α Scorpii | certain | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [मूल](#मूल-mūla--shaula) | Mūla | Shaula | λ Scorpii | likely | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [पूर्वाषाढा](#पूर्वाषाढा-pūrvāṣāḍhā--kaus-media) | Pūrvāṣāḍhā | Kaus Media | δ Sagittarii | certain | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [उत्तराषाढा](#उत्तराषाढा-uttarāṣāḍhā--nunki) | Uttarāṣāḍhā | Nunki | σ Sagittarii | likely | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [अभिजित्](#अभिजित्-abhijit--vega) | Abhijit | Vega | α Lyrae | certain | Later siddhāntas & al-Bīrūnī; Lexicons, Nirukta & Buddhist; Siddhānta Śiromaṇi; Sūrya Siddhānta |
| [श्रवण](#श्रवण-śravaṇa--altair) | Śravaṇa | Altair | α Aquilae | certain | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [श्रविष्ठा](#श्रविष्ठा-śraviṣṭhā-dhaniṣṭhā--rotanev) | Śraviṣṭhā (Dhaniṣṭhā) | Rotanev | β Delphini | certain | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [शतभिषज्](#शतभिषज्-śatabhiṣaj--hydor) | Śatabhiṣaj | Hydor | λ Aquarii | disputed | Later siddhāntas & al-Bīrūnī; Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [पूर्वभाद्रपदा](#पूर्वभाद्रपदा-pūrva-bhādrapadā--markab) | Pūrva-Bhādrapadā | Markab | α Pegasi | certain | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [उत्तरभाद्रपदा](#उत्तरभाद्रपदा-uttara-bhādrapadā--algenib--alpheratz) | Uttara-Bhādrapadā | Algenib / Alpheratz | γ Pegasi / α Andromedae | disputed | Lexicons, Nirukta & Buddhist; Sūrya Siddhānta |
| [रेवती](#रेवती-revatī--revati) | Revatī | Revati | ζ Piscium | likely | Lexicons, Nirukta & Buddhist; Siddhānta Śiromaṇi; Sūrya Siddhānta |
| [अघा](#अघा-aghā--regulus) | Aghā | Regulus | α Leonis | likely | Ṛgveda & Vedāṅga Jyotiṣa |
| [अर्जुन्यौ](#अर्जुन्यौ-arjunyau-arjunī--the-two-phalgunīs--zosmachertan-group-and-denebola) | Arjunyau (Arjunī) | the two Phalgunīs — Zosma/Chertan group and Denebola | δ & θ Leonis; β Leonis | likely | Ṛgveda & Vedāṅga Jyotiṣa |
| [निष्ट्यम् / निस्त्या](#निष्ट्यम्--निस्त्या-niṣṭya--nistyā--arcturus) | Niṣṭya / Nistyā | Arcturus | α Boötis | likely | Ṛgveda & Vedāṅga Jyotiṣa |
| [सार्प](#सार्प-sārpa--āśleṣā-head-of-hydra) | Sārpa | Āśleṣā (head of Hydra) | ε Hydrae (with δ, η, ρ, σ Hydrae) | likely | Later siddhāntas & al-Bīrūnī; Ṛgveda & Vedāṅga Jyotiṣa |
| [ज्येष्ठघ्नी](#ज्येष्ठघ्नी-jyeṣṭhaghnī--antares-cor-scorpionis) | Jyeṣṭhaghnī | Antares (Cor Scorpionis) | α Scorpii | certain | Ṛgveda & Vedāṅga Jyotiṣa |
| [मूलबर्हण](#मूलबर्हण-mūlabarhaṇa-fem-mūlabarhaṇī--the-scorpions-tail-mūla) | Mūlabarhaṇa (fem. Mūlabarhaṇī) | the Scorpion's tail (Mūla) | λ, υ and the chain ε–υ Scorpii | likely | Ṛgveda & Vedāṅga Jyotiṣa |
| [इन्वकाः](#इन्वकाः-इन्वगाः-invakāḥ-invagāḥ--alternative-taittirīya-name-of-mṛgaśīrṣa---the-stars-of-orions-head) | Invakāḥ (Invagāḥ) | alternative Taittirīya name of Mṛgaśīrṣa - the stars of Orion's head | λ, φ1, φ2 Orionis | likely | Vedic corpus; Ṛgveda & Vedāṅga Jyotiṣa |
| [इल्वलाः](#इल्वलाः-ilvalāḥ--the-stars-of-orions-head) | Ilvalāḥ | the stars of Orion's head | λ, φ¹, φ² Orionis | likely | Lexicons, Nirukta & Buddhist |
| [तिष्यः](#तिष्यः-tiṣya--the-later-puṣya-the-asellus-stars-and-praesepe-region) | Tiṣya | the later Puṣya: the Asellus stars and Praesepe region | γ, δ, θ Cancri (δ Cancri = Asellus Australis nearest the ecliptic), with the Praesepe cluster M44 | disputed | Later siddhāntas & al-Bīrūnī; Lexicons, Nirukta & Buddhist; Vedic corpus; Ṛgveda & Vedāṅga Jyotiṣa |
| [सिध्यः](#सिध्यः-sidhya--asellus-australis) | Sidhya | Asellus Australis | δ Cancri | certain | Lexicons, Nirukta & Buddhist |
| [बाहू](#बाहू-रुद्रस्य-bāhū-rudrasya--the-two-arms-of-the-deerorion-usually-taken-as-betelgeuse-and-bellatrix) | Bāhū (Rudrasya) | 'the two Arms' of the deer/Orion: usually taken as Betelgeuse and Bellatrix | α Orionis and γ Orionis | disputed | Vedic corpus |
| [रोहिणी](#रोहिणी-द्वितीया--ज्येष्ठा-rohiṇī-second--jyeṣṭhā--antares) | Rohiṇī (second; = Jyeṣṭhā) | Antares | α Scorpii | likely | Vedic corpus |
| [अश्वयुक्](#अश्वयुक्-aśvayuj--sheratan) | Aśvayuj | Sheratan | β Arietis | certain | Lexicons, Nirukta & Buddhist |
| [राधा](#राधा-rādhā--zubenelgenubi) | Rādhā | Zubenelgenubi | α Librae | certain | Lexicons, Nirukta & Buddhist |
| [श्रविष्ठा](#श्रविष्ठा-śraviṣṭhā--rotanev-dhaniṣṭhā) | Śraviṣṭhā | Rotanev (Dhaniṣṭhā) | β Delphini (with α–δ Delphini) | likely | Lexicons, Nirukta & Buddhist; Ṛgveda & Vedāṅga Jyotiṣa |
| [प्रोष्ठपदा](#प्रोष्ठपदा-proṣṭhapadā--markab--algenib) | Proṣṭhapadā | Markab / Algenib | α and γ Pegasi | certain | Lexicons, Nirukta & Buddhist |
| [आग्रहायणी](#आग्रहायणी-āgrahāyaṇī--meissa) | Āgrahāyaṇī | Meissa | λ Orionis | certain | Lexicons, Nirukta & Buddhist |
| [अश्वत्थ](#अश्वत्थ-aśvattha--altair-śravaṇaśroṇā) | Aśvattha | Altair (Śravaṇa/Śroṇā) | α Aquilae | disputed | Ṛgveda & Vedāṅga Jyotiṣa |
| [ब्राह्मण](#ब्राह्मण-brāhmaṇa--unidentified) | Brāhmaṇa | unidentified | — | disputed | Ṛgveda & Vedāṅga Jyotiṣa |
| [वैष्णव](#वैष्णव-vaiṣṇava--altair) | Vaiṣṇava | Altair | α Aquilae | certain | Later siddhāntas & al-Bīrūnī |
| [वासव](#वासव-vāsava--rotanev) | Vāsava | Rotanev | β Delphini | likely | Later siddhāntas & al-Bīrūnī |
| [अहिर्बुध्न्य](#अहिर्बुध्न्य-ahirbudhnya--algenib--alpheratz) | Ahirbudhnya | Algenib / Alpheratz | γ Pegasi / α Andromedae | certain | Later siddhāntas & al-Bīrūnī |
| [अश्विनिदैवत](#अश्विनिदैवत-aśvinidaivata--sheratan) | Aśvinidaivata | Sheratan | β Arietis | certain | Later siddhāntas & al-Bīrūnī |
| [मैत्र](#मैत्र-maitra--dschubba) | Maitra | Dschubba | δ Scorpii | certain | Later siddhāntas & al-Bīrūnī |
| [रौद्रर्क्ष](#रौद्रर्क्ष-raudrarkṣa--betelgeuse) | Raudrarkṣa | Betelgeuse | α Orionis | disputed | Later siddhāntas & al-Bīrūnī |
| [सौम्य](#सौम्य-saumya--meissa) | Saumya | Meissa | λ Orionis | certain | Later siddhāntas & al-Bīrūnī |
| [प्राजेश](#प्राजेश-prājeśa--aldebaran) | Prājeśa | Aldebaran | α Tauri | certain | Later siddhāntas & al-Bīrūnī |
| [आग्नेय](#आग्नेय-āgneya--alcyone) | Āgneya | Alcyone | η Tauri | certain | Later siddhāntas & al-Bīrūnī |
| [अगस्त्य](#अगस्त्य-agastya--canopus) | Agastya | Canopus | α Carinae | certain | Bṛhat Saṃhitā; Later siddhāntas & al-Bīrūnī; Lexicons, Nirukta & Buddhist; Purāṇas; Siddhānta Śiromaṇi; Sūrya Siddhānta |
| [मृगव्याध](#मृगव्याध-mṛgavyādha--sirius) | Mṛgavyādha | Sirius | α Canis Majoris | likely | Later siddhāntas & al-Bīrūnī; Sūrya Siddhānta; Vedic corpus |
| [लुब्धक](#लुब्धक-lubdhaka--sirius) | Lubdhaka | Sirius | α Canis Majoris | disputed | Bṛhat Saṃhitā; Later siddhāntas & al-Bīrūnī; Lexicons, Nirukta & Buddhist; Siddhānta Śiromaṇi |
| [अग्नि](#अग्नि-हुतभुज्-agni-hutabhuj--elnath) | Agni (Hutabhuj) | Elnath | β Tauri | certain | Sūrya Siddhānta |
| [ब्रह्महृदय](#ब्रह्महृदय-brahmahṛdaya--capella) | Brahmahṛdaya | Capella | α Aurigae | certain | Later siddhāntas & al-Bīrūnī; Sūrya Siddhānta |
| [प्रजापति](#प्रजापति-prajāpati--prijipati) | Prajāpati | Prijipati | δ Aurigae | likely | Sūrya Siddhānta |
| [अपांवत्स](#अपांवत्स-apāṃvatsa--θ-virginis) | Apāṃvatsa | θ Virginis | θ Virginis | likely | Sūrya Siddhānta |
| [आपस्](#आपस्-आपः-āpas--minelauva-auva) | Āpas | Minelauva (Auva) | δ Virginis | certain | Sūrya Siddhānta |
| [ध्रुवः](#ध्रुवः-dhruva--polaris-the-pole-star) | Dhruva | Polaris (the pole star) | α Ursae Minoris | disputed | Lexicons, Nirukta & Buddhist; Purāṇas; Vedic corpus |
| [कुम्भसम्भवः](#कुम्भसम्भवः-kumbhasambhava--canopus) | Kumbhasambhava | Canopus | α Carinae | certain | Lexicons, Nirukta & Buddhist |
| [मैत्रावरुणिः](#मैत्रावरुणिः-maitrāvaruṇi--canopus) | Maitrāvaruṇi | Canopus | α Carinae | certain | Lexicons, Nirukta & Buddhist |
| [मुनि](#मुनि-muni--canopus) | Muni | Canopus | α Carinae | certain | Later siddhāntas & al-Bīrūnī |
| [मृगहर्तृ](#मृगहर्तृ-mṛgahartṛ--sirius) | Mṛgahartṛ | Sirius | α Canis Majoris | certain | Later siddhāntas & al-Bīrūnī |
| [लोपामुद्रावल्लभ](#लोपामुद्रावल्लभ-lopāmudrāvallabha--canopus) | Lopāmudrāvallabha | Canopus | α Carinae | certain | Later siddhāntas & al-Bīrūnī |
| [औत्तानपादिः](#औत्तानपादिः-auttānapādi--pole-star) | Auttānapādi | Pole Star | α Ursae Minoris / the celestial pole | certain | Lexicons, Nirukta & Buddhist |
| [शूल](#शूल--śūla--unidentified-red-star-reported-south-of-canopus) | Śūla | unidentified red star reported south of Canopus | — | disputed | Later siddhāntas & al-Bīrūnī |
| [सप्तर्षयः / ऋक्षाः](#सप्तर्षयः--ऋक्षाः-saptarṣayaḥ--ṛkṣāḥ--the-big-dipper---seven-bright-stars-of-ursa-major-dubhe-merak-phecda-megrez-alioth-mizar-alkaid) | Saptarṣayaḥ / Ṛkṣāḥ | the Big Dipper - seven bright stars of Ursa Major (Dubhe, Merak, Phecda, Megrez, Alioth, Mizar, Alkaid) | α, β, γ, δ, ε, ζ, η Ursae Majoris | certain | Later siddhāntas & al-Bīrūnī; Lexicons, Nirukta & Buddhist; Purāṇas; Vedic corpus |
| [मरीचि](#मरीचि-marīci--alkaid-benetnash) | Marīci | Alkaid (Benetnash) | η Ursae Majoris | likely | Bṛhat Saṃhitā |
| [वसिष्ठ](#वसिष्ठ-vasiṣṭha--mizar) | Vasiṣṭha | Mizar | ζ Ursae Majoris | certain | Bṛhat Saṃhitā |
| [अङ्गिरस्](#अङ्गिरस्-aṅgiras--alioth) | Aṅgiras | Alioth | ε Ursae Majoris | likely | Bṛhat Saṃhitā |
| [अत्रि](#अत्रि-atri--megrez) | Atri | Megrez | δ Ursae Majoris | likely | Bṛhat Saṃhitā |
| [पुलस्त्य](#पुलस्त्य-pulastya--phecda) | Pulastya | Phecda | γ Ursae Majoris | likely | Bṛhat Saṃhitā |
| [पुलह](#पुलह-pulaha--merak) | Pulaha | Merak | β Ursae Majoris | likely | Bṛhat Saṃhitā |
| [क्रतु](#क्रतु-kratu--dubhe) | Kratu | Dubhe | α Ursae Majoris | likely | Bṛhat Saṃhitā |
| [अरुन्धती](#अरुन्धती-arundhatī--alcor-the-faint-companion-of-mizar-in-the-big-dippers-handle) | Arundhatī | Alcor, the faint companion of Mizar in the Big Dipper's handle | 80 Ursae Majoris | certain | Bṛhat Saṃhitā; Later siddhāntas & al-Bīrūnī; Vedic corpus |
| [ऋक्षाः](#ऋक्षाः-ṛkṣāḥ--ursa-major-the-seven-ṛṣis--big-dipper) | Ṛkṣāḥ | Ursa Major (the Seven Ṛṣis / Big Dipper) | α–η Ursae Majoris | disputed | Lexicons, Nirukta & Buddhist; Ṛgveda & Vedāṅga Jyotiṣa |
| [अम्बा](#अम्बा-दुला-नितत्नी-अभ्रयन्ती-मेघयन्ती-वर्षयन्ती-चुपुणीका-ambā-dulā-nitatnī-abhrayantī-meghayantī-varṣayantī-cupuṇīkā--the-seven-individual-stars-of-the-pleiades) | Ambā, Dulā, Nitatnī, Abhrayantī, Meghayantī, Varṣayantī, Cupuṇīkā | the seven individual stars of the Pleiades | brightest members: η, 27, 17, 20, 23, 19, 28 Tauri (no secure one-to-one mapping) | likely | Vedic corpus |
| [मृगः](#मृगः-प्रजापतिः-mṛga-prajāpati--the-celestial-deer--orion) | Mṛga (Prajāpati) | the celestial deer = Orion | constellation Orion (head λ Ori; body the Belt region) | likely | Vedic corpus |
| [इषुस्त्रिकाण्डा](#इषुस्त्रिकाण्डा-iṣus-trikāṇḍā--orions-belt---mintaka-alnilam-alnitak---as-the-three-jointed-arrow) | Iṣus trikāṇḍā | Orion's Belt - Mintaka, Alnilam, Alnitak - as the 'three-jointed arrow' | δ, ε, ζ Orionis | likely | Vedic corpus |
| [विचृतौ](#विचृतौ-vicṛtau--shaula-and-lesath-the-scorpions-sting) | Vicṛtau | Shaula and Lesath (the Scorpion's sting) | λ & υ Scorpii | certain | Ṛgveda & Vedāṅga Jyotiṣa |
| [शिशुमार](#शिशुमार-śiśumāra--the-celestial-porpoisedolphin--a-whole-star-figure-not-a-single-star) | Śiśumāra | the celestial porpoise/dolphin — a whole star-figure, not a single star | — | disputed | Purāṇas |
| [सक्वर](#सक्वर--sakvara--the-circumpolar-14-star-figure-a-second-name-for-the-śiśumāra) | Sakvara | the circumpolar 14-star figure (a second name for the Śiśumāra) | — | disputed | Later siddhāntas & al-Bīrūnī |
| [त्रिशङ्कु](#त्रिशङ्कु-triśaṅku--triśaṅku--a-king-fixed-head-downward-in-the-southern-sky) | Triśaṅku | Triśaṅku — a king fixed head-downward in the southern sky | — | disputed | Purāṇas |
| [धाता](#धाता-विधाता-dhātā-vidhātā--two-circumpolar-star-positions-at-the-root-of-the-śiśumāras-tail) | Dhātā, Vidhātā | two circumpolar star-positions at the root of the Śiśumāra's tail | — | disputed | Purāṇas |
| [इन्द्र / महेन्द्र](#इन्द्र--महेन्द्र-indra--mahendra--a-circumpolar-star-on-the-tail-of-the-śiśumāra) | Indra / Mahendra | a circumpolar star on the tail of the Śiśumāra | — | disputed | Purāṇas |
| [कश्यप](#कश्यप-kaśyapa--a-circumpolar-star-on-the-tail-of-the-śiśumāra-adjacent-to-dhruva) | Kaśyapa | a circumpolar star on the tail of the Śiśumāra, adjacent to Dhruva | — | disputed | Purāṇas |
| [मरीचि](#मरीचि-पुच्छे-marīci-in-the-tail--a-fifth-circumpolar-star-in-the-śiśumāras-tail) | Marīci (in the tail) | a fifth circumpolar star in the Śiśumāra's tail | — | disputed | Purāṇas |
| [उत्तानपाद](#उत्तानपाद-uttānapāda--the-upper-jaw-of-the-śiśumāra) | Uttānapāda | the upper jaw of the Śiśumāra | — | disputed | Purāṇas |
| [यज्ञ](#यज्ञ-धर्म-वरुण-अर्यमा-संवत्सर-मित्र-yajña-dharma-varuṇa-aryaman-saṃvatsara-mitra--six-further-body-positions-of-the-śiśumāra-lower-jaw-head-the-two-hind-thighs-the-sexual-organ-the-anus) | Yajña, Dharma, Varuṇa, Aryaman, Saṃvatsara, Mitra | six further body-positions of the Śiśumāra: lower jaw, head, the two hind thighs, the sexual organ, the anus | — | disputed | Purāṇas |
| [यम](#यम-अधराहनौ-yama-on-the-lower-jaw--a-star-on-the-lower-jaw-of-the-śiśumāra-opposite-agasti) | Yama (on the lower jaw) | a star on the lower jaw of the Śiśumāra, opposite Agasti | — | disputed | Purāṇas |
| [प्रजापति](#प्रजापति-पुच्छे-prajāpati-in-the-tail--a-circumpolar-star-on-the-śiśumāras-tail--not-the-ecliptic-prajāpati) | Prajāpati (in the tail) | a CIRCUMPOLAR star on the Śiśumāra's tail — not the ecliptic Prajāpati | — | disputed | Purāṇas |
| [सुनीति](#सुनीति-sunīti--a-star-beside-dhruva--dhruvas-mother-placed-as-a-star-near-the-pole) | Sunīti | a star beside Dhruva — Dhruva's mother, placed as a star near the pole | — | disputed | Purāṇas |
| [नागवीथी](#नागवीथी-nāgavīthī--the-serpent-road-northernmost-of-the-nine-star-roads) | Nāgavīthī | the Serpent-road, northernmost of the nine star-roads | — | likely | Purāṇas |
| [गजवीथी](#गजवीथी-gajavīthī--the-elephant-road) | Gajavīthī | the Elephant-road | — | likely | Purāṇas |
| [ऐरावती](#ऐरावती-airāvatī--the-road-of-airāvata) | Airāvatī | the road of Airāvata | — | likely | Purāṇas |
| [आर्षभी](#आर्षभी-ārṣabhī--the-bull-road) | Ārṣabhī | the Bull-road | — | likely | Purāṇas |
| [गोवीथी](#गोवीथी-govīthī--the-cow-road) | Govīthī | the Cow-road | — | disputed | Purāṇas |
| [जरद्गव / जारद्गवी](#जरद्गव--जारद्गवी-jaradgava--jāradgavī--the-old-ox-road) | Jaradgava / Jāradgavī | the Old-Ox road | — | disputed | Purāṇas |
| [अजवीथी](#अजवीथी-ajavīthī--the-goat-road--a-three-nakṣatra-segment-of-the-ecliptic-belt) | Ajavīthī | the Goat-road — a three-nakṣatra segment of the ecliptic belt | — | disputed | Purāṇas |
| [मृगवीथी](#मृगवीथी-mṛgavīthī--the-deer-road) | Mṛgavīthī | the Deer-road | — | likely | Purāṇas |
| [वैश्वानरी](#वैश्वानरी-vaiśvānarī--the-road-of-vaiśvānara-fire) | Vaiśvānarī | the road of Vaiśvānara (Fire) | — | disputed | Purāṇas |
| [ऐरावत / जरद्गव / वैश्वानर](#ऐरावत--जरद्गव--वैश्वानर-मार्गाः-airāvata--jaradgava--vaiśvānara-the-three-mārgas--the-three-great-celestial-belts--northern-middle-southern) | Airāvata / Jaradgava / Vaiśvānara (the three mārgas) | the three great celestial belts — northern, middle, southern | — | likely | Purāṇas |
| [पितृयाण / देवयान](#पितृयाण--देवयान-pitṛyāṇa--devayāna--the-road-of-the-fathers--the-road-of-the-gods--two-celestial-bands-defined-by-star-markers) | Pitṛyāṇa / Devayāna | the Road of the Fathers / the Road of the Gods — two celestial bands defined by star markers | — | likely | Purāṇas |
| [आकाशगङ्गा](#आकाशगङ्गा-ākāśagaṅgā--the-milky-way-lit-sky-ganges) | Ākāśagaṅgā | the Milky Way (lit. 'sky-Ganges') | — | likely | Purāṇas |
| [छायापथ](#छायापथ-chāyāpatha--the-milky-way-lit-the-shadow-path) | Chāyāpatha | the Milky Way (lit. 'the shadow-path') | — | certain | Purāṇas |
| [त्रिपथगा](#त्रिपथगा-tripathagā--the-milky-way-as-the-three-path-goer-the-gaṅgā-of-the-three-worlds) | Tripathagā | the Milky Way, as the 'three-path-goer' (the Gaṅgā of the three worlds) | — | certain | Purāṇas |
| [मन्दाकिनी](#मन्दाकिनी-mandākinī--milky-way) | Mandākinī | Milky Way | — | likely | Lexicons, Nirukta & Buddhist |
| [वियद्गङ्गा](#वियद्गङ्गा-viyadgaṅgā--milky-way) | Viyadgaṅgā | Milky Way | — | likely | Lexicons, Nirukta & Buddhist |
| [स्वर्णदी](#स्वर्णदी-svarnadī--milky-way) | Svarnadī | Milky Way | — | likely | Lexicons, Nirukta & Buddhist |
| [सुरदीर्घिका](#सुरदीर्घिका-suradīrghikā--milky-way) | Suradīrghikā | Milky Way | — | disputed | Lexicons, Nirukta & Buddhist |
| [विष्णुपद](#विष्णुपद-viṣṇupada--the-step-of-viṣṇu--the-third-and-highest-region-of-the-sky-where-dhruva-stands) | Viṣṇupada | 'the step of Viṣṇu' — the third and highest region of the sky, where Dhruva stands | — | disputed | Lexicons, Nirukta & Buddhist; Purāṇas |
| [मेढी / मेढीभूत](#मेढी--मेढीभूत-meḍhī--meḍhībhūta--the-threshing-post--the-celestial-pole-as-the-pivot-to-which-the-sky-is-tethered) | Meḍhī / Meḍhībhūta | 'the threshing-post' — the celestial pole as the pivot to which the sky is tethered | — | certain | Purāṇas |
| [प्रवह](#प्रवह-pravaha--the-wind-that-carries-the-stars-around-the-pole) | Pravaha | the wind that carries the stars around the pole | — | certain | Purāṇas |
| [तारापथः](#तारापथः-tārāpatha--the-firmament-star-road) | Tārāpatha | the firmament ('star-road') | — | certain | Lexicons, Nirukta & Buddhist |
| [नक्षत्रम्](#नक्षत्रम्-nakṣatra--star--asterism-generic) | Nakṣatra | star / asterism (generic) | — | certain | Lexicons, Nirukta & Buddhist |
| [भम्](#भम्-bha--star--asterism-generic) | Bha | star / asterism (generic) | — | certain | Lexicons, Nirukta & Buddhist |
| [तारा](#तारा-tārā--star-generic) | Tārā | star (generic) | — | certain | Lexicons, Nirukta & Buddhist |
| [तारका](#तारका-tārakā--star-generic) | Tārakā | star (generic) | — | certain | Lexicons, Nirukta & Buddhist |
| [उडु](#उडु-uḍu--star--lunar-mansion-generic) | Uḍu | star / lunar mansion (generic) | — | certain | Lexicons, Nirukta & Buddhist |
| [धिष्ण्यम्](#धिष्ण्यम्-dhiṣṇya--asterism--star-station-generic) | Dhiṣṇya | asterism / star-station (generic) | — | certain | Lexicons, Nirukta & Buddhist |
| [स्तृभिः](#स्तृभिः-stṛbhiḥ-stem-stṛ--the-stars-generic-vedic) | Stṛbhiḥ (stem stṛ) | the stars (generic, Vedic) | — | certain | Lexicons, Nirukta & Buddhist |
| [अश्विन्यादीनां साभिजितां योगताराः](#अश्विन्यादीनां-साभिजितां-योगताराः-aśvinyādi-yogatārāḥ-sābhijit--collective-catalog-of-28-junction-stars) | Aśvinyādi yogatārāḥ (sābhijit) | collective catalog of 28 junction stars | various | likely | Later siddhāntas & al-Bīrūnī; Siddhānta Śiromaṇi |
| [दाक्षायिण्यः](#दाक्षायिण्यः-dākṣāyaṇyaḥ--the-27-lunar-mansions-collectively) | Dākṣāyaṇyaḥ | the 27 lunar mansions collectively | — | certain | Lexicons, Nirukta & Buddhist |
| [चित्रशिखण्डिनः](#चित्रशिखण्डिनः-citraśikhaṇḍinaḥ--big-dipper--great-bear) | Citraśikhaṇḍinaḥ | Big Dipper / Great Bear | α–η Ursae Majoris | certain | Lexicons, Nirukta & Buddhist |
| [अष्टाविंशतिनक्षत्राणि](#अष्टाविंशतिनक्षत्राणि-aṣṭāviṃśati-nakṣatrāṇi--the-28-fold-nakshatra-circle-buddhist) | Aṣṭāviṃśati-nakṣatrāṇi | the 28-fold nakshatra circle (Buddhist) | — | certain | Lexicons, Nirukta & Buddhist |
| [चतुर्द्वारिकाणि नक्षत्राणि](#चतुर्द्वारिकाणि-नक्षत्राणि-catur-dvārikāṇi-nakṣatrāṇi--the-28-nakshatras-in-four-gate-groups-of-seven) | Catur-dvārikāṇi nakṣatrāṇi | the 28 nakshatras in four gate-groups of seven | — | certain | Lexicons, Nirukta & Buddhist |
| [ताराग्रहाः](#ताराग्रहाः-tārāgrahāḥ--the-five-star-planets) | Tārāgrahāḥ | the five star-planets | Mercury, Venus, Mars, Jupiter, Saturn | certain | Lexicons, Nirukta & Buddhist |

## What each source yielded

**Ṛgveda & Vedāṅga Jyotiṣa.** The Ṛgveda names almost no stars. An exhaustive search of the complete Aufrecht text (GRETIL) shows zero occurrences of Kṛttikā, Mṛgaśīrṣa, Viśākhā, Āśleṣā, Phalgunī, Anurādhā, Aṣāḍhā, Śatabhiṣaj, Proṣṭhapadā, Śraviṣṭhā, Abhijit, Invakā, Saptarṣi, Arundhatī, Mṛgavyādha or Lubdhaka; Agastya occurs six times but only as the ṛṣi, never as Canopus, and Rohiṇī only as 'red cows'. What the Ṛgveda does have is four star passages: ṛkṣāḥ (the Bears) at 1.24.10, the archaic pair Aghā/Arjunyau at 10.85.13, and Tiṣya at exactly two places, 5.54.13 and 10.64.8. The richest yield in this cluster is actually the Atharvaveda, which names two stars outright as tārake ('the two stars') — Vicṛtau, in four separate hymns — plus Jyeṣṭhaghnī and Mūlabarhaṇa in the Scorpius birth-charm AV 6.110. Taittirīya Āraṇyaka 1.11 supplies decisive context for ṛkṣāḥ by quoting the Ṛgvedic verse immediately after naming the Seven Ṛṣis and Agastya. Maitrāyaṇī Saṃhitā 2.13.20 yields Niṣṭya (for Svāti) and an anomalous 28th/29th name, Brāhmaṇa. The Vedāṅga Jyotiṣa names only Śraviṣṭhā and Sārpa, never Dhaniṣṭhā or Āśleṣā.

**Purāṇas.** Bhāgavata Purāṇa 5.23.4–8 yields the most complete Śiśumāra-cakra body-part↔star mapping in Sanskrit literature, recovered verbatim from two independent witnesses (GRETIL IAST and a Devanagari e-text of the mūla) that agree word-for-word. Its scheme is internally perfect: all 28 nakṣatras are placed exactly once — 14 uttarāyaṇa asterisms (Abhijit→Punarvasu) on the right side, 14 dakṣiṇāyana (Puṣya→Uttarāṣāḍhā) on the left — with no gaps or duplicates, which independently confirms the commentators' endpoints. A second, older and shorter Śiśumāra recension (Viṣṇu P. 2.12.31–34 = Vāyu 52.92–95 = Matsya 127.22–25 = Brahmāṇḍa 1,23.102–105) maps deities, not stars, onto a 14-star figure, and agrees on the crucial point: a circumpolar tail-group terminating in Dhruva, 'four stars that never set'. Beyond the Śiśumāra the harvest is large: the full nine-vīthī / three-mārga star-road system of Matsya 124, the pole-region names Viṣṇupada and meḍhī, and two genuine Milky Way terms — Ākāśagaṅgā and the chāyāpatha ('shadow-path') identified with Tripathagā. Also recovered: Triśaṅku as a sky-figure, and the Saptarṣi century-per-nakṣatra cycle in four recensions.

**Lexicons, Nirukta & Buddhist.** The Amarakośa is the richest yield: its Dig-varga (1.3) — not the Svarga-varga, as often assumed — supplies six generic star-words (nakṣatra, ṛkṣa, bha, tārā, tārakā, uḍu), the patronymic Auttānapādi for the pole star, two further names for Agastya/Canopus (Kumbhasambhava, Maitrāvaruṇi), the collective Dākṣāyaṇyaḥ for the 27 nakshatras, Citraśikhaṇḍinaḥ for the Seven Sages, archaic asterism names (Aśvayuj, Rādhā, Sidhya, Śraviṣṭhā, Proṣṭhapadā, Āgrahāyaṇī), and Ilvalāḥ defined by a relative clause as 'the stars that dwell in the head-region' of the Deer; the Svarga-varga (1.1.116) adds four Milky Way synonyms. Yāska's Nirukta 3.20 gives the oldest Indian etymologies of nakṣatra, ṛkṣa and stṛ. The Buddhist Śārdūlakarṇāvadāna is the single most valuable astronomical witness found: for all 28 nakshatras it gives an exact star-count, a figure, a muhūrta-value, a deity and a gotra — data that bears directly on which stars each asterism comprised. The Jain canon defeated the search: no fetchable Prakrit e-text of the Sūryaprajñapti or its relatives exists online. Arthaśāstra 2.20 turns out NOT to contain a nakshatra list at all.

**Later siddhāntas & al-Bīrūnī.** Sūrya Siddhānta ch. 9 (udayāstādhikāra) yielded the target verse 9.12 verbatim, naming Svātī, Agastya, Mṛgavyādha, Citrā, Jyeṣṭhā, Punarvasu, Abhijit and Brahmahṛdaya as the brightest class of stars, and 9.18, listing the six that never set heliacally; 9.13–15 add nine deity-epithet names for nakshatras. Chapter 10 contains NO star names at all (verified verse by verse); a bonus find is SS 13.8–9, naming Abhijit, the Saptarṣayaḥ and Agastya for the armillary sphere. The Pañcasiddhāntikā names exactly ONE non-nakshatra star — Agastya — and gives coordinates for only SEVEN yogatārās, with Varāhamihira's implied Canopus latitude (75°30' S) markedly better than the Sūrya Siddhānta's 80°. Brahmagupta's yogatārā table WAS located in the Bhagrahayutyadhikāra, with the edition's commentary stating explicitly that Bhāskara reproduced these same values; Brahmagupta names only two non-nakshatra stars, under four names, two of which are new here (muni, mṛgahartṛ). Colebrooke 1817 proves useless for stars — he translated only the mathematical chapters. Al-Bīrūnī is the richest single find: he independently confirms Brahmahṛdaya = Capella and Arundhatī = Alcor (by Ptolemaic catalogue number), reproduces visibility lists matching SS 9.12 and 9.18 almost star for star, glosses Śiśumāra by Persian susmār, fails to identify Śatabhiṣaj, and preserves two otherwise-unknown stars.

## A finding about the Āryabhaṭīya

The Āryabhaṭīya names NO individual stars. Evidence: (1) W.E. Clark's complete 1930 translation (full text fetched from https://archive.org/stream/in.ernet.dli.2015.61416/2015.61416.The-Aryabhatiya-Of-Aryabhata_djvu.txt) was searched for Agastya, Canopus, Sirius, Dhruva, 'pole star', and all 27 nakshatra names — zero hits; the index lists only generic 'Asterisms'. (2) The complete Sanskrit text of all four padas on sa.wikisource (https://sa.wikisource.org/wiki/गोल-पाद , /दश-गीतिका-पाद , /गणित-पाद , /काल-क्रिया-पाद) was searched for अगस्त्य, ध्रुव, सप्तर्षि and nakshatra names — zero hits. The Gola-pada speaks only generically of the asterisms: verse 4.9 'अचलानि भानि तद्-वत् सम-पश्चिम-गानि लङ्कायाम्' — Clark: 'just so at Lanka a man sees the stationary asterisms moving backward (westward) in a straight line'; 4.10 refers to the भ-पञ्जर ('cage of the asterisms'); Clark: 'the circle of the asterisms, together with the planets, driven by the provector wind, constantly moves straight westward at Lanka'. Gola 11-12 and 16-17 place the gods on Meru at the north pole (Clark: 'The gods, who dwell in the north on Meru, see the northern half of the sphere of the asterisms moving from left to right') but name no pole star — the word Dhruva does not occur anywhere in the text. There is no yogatārā catalog and no verse about any individual star; the Daśagītikā gives only revolution counts of 'the asterisms' as a whole.

## The Śiśumāra-cakra: the sky as a porpoise

Bhāgavata Purāṇa 5.23.4–8 lays the whole sky out as the body of a celestial porpoise, with Dhruva at the tail-tip and the 28 nakshatras ranged along its flanks. An older and shorter recension (Viṣṇu Purāṇa 2.12.31–34 = Vāyu 52.92–95 = Matsya 127.22–25 = Brahmāṇḍa 1,23.102–105) maps deities onto a fourteen-star figure instead. The two conflict — the upper jaw is Agasti in one and Uttānapāda in the other — so both are given here. *Stated* means the text says it; *inferred* means a commentator supplied it.

The Bhāgavata's scheme was checked arithmetically and is internally perfect: counting eight forward from Maghā and eight backward from Mṛgaśiras, plus the twelve individually named asterisms, places all 28 nakshatras exactly once — 14 per side. That independently confirms the commentators' endpoints.

| Recension | Body part | Sanskrit | IAST | Stated? | Modern |
|---|---|---|---|---|---|
| Bhāgavata 5.23.5 | tip of the tail (pucchāgra) | ध्रुव | Dhruva | stated | Polaris (α UMi) in the received tradition; α Draconis / Thuban for the older textual layer — disputed |
| Bhāgavata 5.23.5 | the tail (lāṅgūla) | प्रजापतिः, अग्निः, इन्द्रः, धर्मः | Prajāpati, Agni, Indra, Dharma | stated | unidentified circumpolar stars along Draco/Ursa Minor; no individual identifications in any Purāṇa |
| Bhāgavata 5.23.5 | root of the tail (puccha-mūla) | धाता, विधाता | Dhātā, Vidhātā | stated | unidentified; circumpolar |
| Bhāgavata 5.23.5 | waist / haunch (kaṭi) | सप्तर्षयः | Saptarṣayaḥ | stated | Ursa Major (the Big Dipper) — certain by universal tradition, though the Purāṇa does not say so |
| Bhāgavata 5.23.5 | the back (pṛṣṭha) | अजवीथी | Ajavīthī | stated | an ecliptic star-road; Mūla + both Aṣāḍhās per Brahmāṇḍa/Matsya 124.53, but Matsya 124.58 instead gives Hasta/Citrā/Svātī — the text is self-contradictory |
| Bhāgavata 5.23.5 | the belly (udara) | आकाशगङ्गा | Ākāśagaṅgā | stated | the Milky Way |
| Bhāgavata 5.23.6 | right and left hips (śroṇī) | पुनर्वसु, पुष्य | Punarvasu (R), Puṣya (L) | stated | Gemini (Castor/Pollux); Cancer (γ/δ/θ Cnc) |
| Bhāgavata 5.23.6 | right and left hind feet (paścimau pādau) | आर्द्रा, आश्लेषा | Ārdrā (R), Āśleṣā (L) | stated | Betelgeuse (α Ori); ε/δ/σ Hydrae. NOTE: Sanyal's printed translation wrongly puts these on the nostrils — see caveats |
| Bhāgavata 5.23.6 | right and left nostrils (nāsike) | अभिजित्, उत्तराषाढा | Abhijit (R), Uttarāṣāḍhā (L) | stated | Vega (α Lyrae); σ/ζ Sagittarii |
| Bhāgavata 5.23.6 | right and left eyes (locane) | श्रवण, पूर्वाषाढा | Śravaṇa (R), Pūrvāṣāḍhā (L) | stated | Altair (α Aquilae); δ/ε Sagittarii |
| Bhāgavata 5.23.6 | right and left ears (karṇau) | धनिष्ठा, मूल | Dhaniṣṭhā (R), Mūla (L) | stated | β Delphini group; λ/υ Scorpii |
| Bhāgavata 5.23.6 | left-side ribs (vāma-pārśva-vaṅkri) — eight dakṣiṇāyana asterisms | मघादीन्यष्ट नक्षत्राणि | the eight beginning with Maghā: Maghā, Pūrvaphalgunī, Uttaraphalgunī, Hasta, Citrā, Svāti, Viśākhā, Anurādhā | stated ('the eight beginning with Maghā'); the terminus Anurādhā is inferred, supplied by commentators and confirmed by counting | Leo through Scorpius, along the ecliptic |
| Bhāgavata 5.23.6 | right-side ribs (dakṣiṇa-pārśva-vaṅkri) — eight udagayana asterisms, in reverse order (prātilomyena) | मृगशीर्षादीन्युदगयनानि | the eight beginning with Mṛgaśīrṣa, counted backwards: Mṛgaśiras, Rohiṇī, Kṛttikā, Bharaṇī, Aśvinī, Revatī, Uttarabhādrapadā, Pūrvabhādrapadā | stated ('beginning with Mṛgaśīrṣa … in reverse order'); the terminus Pūrvabhādrapadā is inferred, and confirmed by counting | Orion/Taurus back through Aries and Pisces |
| Bhāgavata 5.23.6 | right and left shoulders (skandhau) | शतभिषा, ज्येष्ठा | Śatabhiṣā (R), Jyeṣṭhā (L) | stated | λ Aquarii; Antares (α Scorpii) |
| Bhāgavata 5.23.7 | upper jaw (uttarā-hanu) | अगस्ति | Agasti | stated | Canopus (α Carinae) — certain by universal tradition, not asserted by the text |
| Bhāgavata 5.23.7 | lower jaw (adharā-hanu) | यम | Yama | stated | unidentified |
| Bhāgavata 5.23.7 | the mouth (mukha) | अङ्गारक | Aṅgāraka | stated | Mars (planet, not a star) |
| Bhāgavata 5.23.7 | the genitals (upastha) | शनैश्चर | Śanaiścara | stated | Saturn |
| Bhāgavata 5.23.7 | the hump / nape (kakud) | बृहस्पति | Bṛhaspati | stated | Jupiter |
| Bhāgavata 5.23.7 | the chest (vakṣas) | आदित्य | Āditya | stated | the Sun |
| Bhāgavata 5.23.7 | the heart (hṛdaya) | नारायण | Nārāyaṇa | stated | not a celestial body — the deity upholding the figure |
| Bhāgavata 5.23.7 | the mind (manas) | चन्द्र | Candra | stated | the Moon |
| Bhāgavata 5.23.7 | the navel (nābhi) | उशना | Uśanā | stated | Venus (Śukra) |
| Bhāgavata 5.23.7 | the two breasts (stanau) | अश्विनौ | Aśvinau | stated | the Aśvins; cf. the nakṣatra Aśvinī (β/γ Arietis), but here the deities |
| Bhāgavata 5.23.7 | prāṇa and apāna (the vital airs) | बुध | Budha | stated | Mercury |
| Bhāgavata 5.23.7 | the throat (gala) | राहु | Rāhu | stated | the ascending lunar node |
| Bhāgavata 5.23.7 | all the limbs (sarvāṅgeṣu) | केतवः | Ketavaḥ | stated | comets / the descending node |
| Bhāgavata 5.23.7 | the body-hairs (romāṇi) | सर्वे तारागणाः | sarve tārā-gaṇāḥ | stated | all remaining stars — the general star-field |
| Viṣṇu 2.12.31 and parallels | upper jaw (uttaro hanuḥ) | उत्तानपाद | Uttānapāda | stated | unidentified. NOTE: conflicts with Bhāgavata 5.23.7, which puts Agasti on the upper jaw |
| Viṣṇu 2.12.31 and parallels | lower jaw (adharaḥ) | यज्ञ | Yajña | stated | unidentified |
| Viṣṇu 2.12.31 and parallels | the head / crown (mūrdhan) | धर्म | Dharma | stated | unidentified |
| Viṣṇu 2.12.32 and parallels | the heart (hṛd) | नारायण | Nārāyaṇa (Matsya/Vāyu add the Sādhyas) | stated | deity, not a star |
| Viṣṇu 2.12.32 and parallels | the two fore-feet (pūrvapādau) | अश्विनौ | Aśvinau | stated | unidentified |
| Viṣṇu 2.12.32 and parallels | the two hind thighs (paścime sakthinī) | वरुणः, अर्यमा | Varuṇa, Aryaman | stated | unidentified |
| Viṣṇu 2.12.33 and parallels | the sexual organ (śiśna) | संवत्सर | Saṃvatsara | stated | unidentified |
| Viṣṇu 2.12.33 and parallels | the organ of excretion (apāna) | मित्र | Mitra | stated | unidentified |
| Viṣṇu 2.12.34 and parallels | the tail (puccha), in sequence | अग्निः, महेन्द्रः, (मरीचिः), कश्यपः, ध्रुवः | Agni, Mahendra, (Marīci — Vāyu 52.95 and Brahmāṇḍa 1,23.104 only), Kaśyapa, Dhruva | stated — and the text itself asserts these are 'four stars that never set' (tārakā … nāstam eti catuṣṭayam), the only astronomical claim the older recension makes | circumpolar stars of Draco/Ursa Minor; individual identifications are all modern conjecture. Wilson's 'Kaśyapa ≈ Cassiopeia' is a 19th-c. sound-alike with no textual warrant |

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

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, p. 51** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> aśvinī-nakṣatraṃ dvitāraṃ turagaśīrṣa-saṃsthānaṃ triṃśan-muhūrta-yogaṃ madhu-pāyasabhojanaṃ gandharva-daivataṃ maitrāyāṇīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Aśvinī asterism has two stars, is shaped like a horse's head, has a thirty-muhūrta conjunction, honey and milk-rice for its food, Gandharva for its deity, Maitrāyāṇīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** TWO stars, HORSE'S-HEAD-shaped (turagaśīrṣa-saṃsthāna), deity Gandharva, gotra Maitrāyāṇīya. Two stars in a horse's head = β and γ Arietis, exactly the pair Burgess argued for against Colebrooke's α Arietis, and matching Colebrooke's own 'The head of Aries' for Amarakośa. NOTE the deity Gandharva where the Brahmanical lists have the Aśvins.</sub>

### भरणी (Bharaṇī) — 35 Arietis (Musca Borealis)

**Modern identification:** 35 Arietis (Musca Borealis) — 35 Arietis, Aries (*disputed*)

**Sūrya Siddhānta 8.18** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> ज्येष्ठाश्रवणमैत्राणाम् बार्हस्पत्यस्य मध्यमा / भरण्याग्नेयपित्र्याणाम् रेवत्याश् चैव दक्षिणा //
>
> — *18. Of Jyeshtha, Çravana, Anuradha (maitra), and Pushya (barhaspatya), it is the middle star: of Bharani, Krttika (agneya), and Magha (pitrya), and likewise of Revati, it is the southern:*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Group = 35, 39, 41 Arietis (obsolete Musca Borealis). Burgess: the 'southern' designation is ambiguous; 41 Ari (brighter, nearer ecliptic) 'would seem more likely', but 'the defined position, however, agrees better with 35', which he adopts. Many modern lists prefer 41 Arietis.</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, p. 51** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> bharaṇī-nakṣatraṃ tritāraṃ bhaga-saṃsthānaṃ triṃśan-muhūrta-yogaṃ tila-taṇḍūlāhāraṃ yamadaivataṃ bhārgavīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Bharaṇī asterism has three stars, is shaped like the bhaga, has a thirty-muhūrta conjunction, sesame and rice for its food, Yama for its deity, Bhārgavīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** THREE stars, bhaga-shaped (the female pudendum, i.e. a triangle), deity Yama, gotra Bhārgavīya. Three stars in a triangle = 35, 39, 41 Arietis — which settles that the asterism is the whole triad and makes Burgess's agonising over which one is the yogatārā a question about the junction-star only. The bhaga figure explains the alternative name Apabharaṇī and the Yama/death associations.</sub>

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

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, pp. 46–47; verse form p. 81** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> kṛttikā bhoḥ puṣkarasārin nakṣatraṃ ṣaṭtāraṃ kṣura-saṃsthānaṃ triṃśan-muhūrta-yogaṃ dadhyāhāram agnidaivataṃ vaiśyāyanīyaṃ gotreṇa/ ... ṣaṭtārāṃ kṛttikāṃ vidyād āśrayaṃ tāsu kārayet/
>
> — *Literal rendering: 'Kṛttikā, sir Puṣkarasārin, is a nakshatra of six stars, razor-shaped, with a thirty-muhūrta conjunction, curds for its food, Agni for its deity, Vaiśyāyanīya by gotra.' / 'One should know Kṛttikā as six-starred; under it one should build a dwelling.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** SIX stars, razor-shaped (kṣura-saṃsthāna), deity Agni, gotra Vaiśyāyanīya. The count of six bears directly on the seven individually-named Kṛttikās already on file: the Buddhist tradition counts six visible Pleiades, matching the widespread 'lost Pleiad' motif. The verse recension of the same chapter repeats it: ṣaṭtārāṃ kṛttikāṃ vidyāt.</sub>

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

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, pp. 46–47; cf. Amarakośa 1.3.227** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> rohiṇī-nakṣatraṃ pañca-tārakaṃ śakaṭākṛti-saṃsthānaṃ pañca-catvāriṃśan-muhūrta-yogaṃ mṛgamāṃsāhāraṃ prajāpati-daivataṃ bhāradvājaṃ gotreṇa/
>
> — *Literal rendering: 'The Rohiṇī asterism has five stars, is shaped like a wagon, has a forty-five-muhūrta conjunction, venison for its food, Prajāpati for its deity, Bhāradvāja by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** FIVE stars, wagon-shaped (śakaṭākṛti-saṃsthāna), deity Prajāpati, gotra Bhāradvāja. The five-star wagon is the Hyades V (α, θ¹, γ, δ, ε Tauri) — strong corroboration of the cluster reading, and of the śakaṭa ('wain') that Sūrya Siddhānta 8.13 speaks of splitting. Colebrooke independently glosses Amarakośa's rauhiṇeya = Mercury with 'Budha, son of Soma (or the moon) by Rohini (or the Hyades)', the earliest public-domain equation of Rohiṇī with the cluster rather than Aldebaran alone.</sub>

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

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, pp. 46–47; cf. Amarakośa 1.3.221** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> mṛgaśirā-nakṣatraṃ tritāraṃ mṛgaśīrṣa-saṃsthānaṃ triṃśan muhūrta-yogaṃ phalamūlāhāraṃ soma-daivataṃ mṛgāyaṇīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Mṛgaśirā asterism has three stars, is shaped like a deer's head, has a thirty-muhūrta conjunction, fruits and roots for its food, Soma for its deity, Mṛgāyaṇīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** THREE stars, deer's-head-shaped (mṛgaśīrṣa-saṃsthāna), deity Soma, gotra Mṛgāyaṇīya — i.e. exactly the group Amarakośa calls the Ilvalāḥ, λ/φ¹/φ² Orionis. The Amarakośa also records three name-forms (Mṛgaśīrṣa, Mṛgaśiras, Āgrahāyaṇī), which Colebrooke glosses simply 'Orion'.</sub>

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

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, pp. 46–47** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> ārdra-nakṣatram eka-tāraṃ tilaka-saṃsthānaṃ pañca-daśa-muhūrta-yogaṃ sarpirmaṇḍāhāraṃ sūrya-daivataṃ hārītītāyanīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Ārdrā asterism has one star, is shaped like a forehead-mark, has a fifteen-muhūrta conjunction, clarified-butter cream for its food, Sūrya for its deity, Hārītītāyanīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** ONE star, tilaka-shaped (a forehead-mark, i.e. a single point), deity Sūrya, gotra Hārītītāyanīya. The single-star count supports Betelgeuse over any multi-star reading. NOTE the deity: Sūrya, not the Rudra of the Brahmanical lists — a genuine Buddhist divergence, and one that weakens the Rudra-based argument sometimes used to identify Ārdrā with Sirius.</sub>

### पुनर्वसु (Punarvasu) — Pollux

**Modern identification:** Pollux — β Geminorum, Gemini (*certain*)

**Sūrya Siddhānta 8.19** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> रोहिण्यादित्यमूलानाम् प्राची सार्पस्य चैव हि / यथा प्रत्यवशेषाणाम् स्थूला स्याद् योगतारका //
>
> — *19. Of Rohini, Punarvasu (aditya), and Mula, it is the eastern, and so also of Açlesha (sarpa): in the case of each of the others, the junction-star (yogataraka) is the great (sthula) one.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'the two bright stars in the heads of the Twins, or α and β Geminorum, and the latter (1.2) is the junction-star' (the eastern, per v. 19).</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, pp. 46–47** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> punarvasu-nakṣatraṃ dvitāraṃ pada-saṃsthānaṃ pañca-catvāriṃśan-muhūrta-yogaṃ madh[u]āhāram aditidaivataṃ vāśiṣṭhaṃ gotreṇa/
>
> — *Literal rendering: 'The Punarvasu asterism has two stars, is foot-shaped, has a forty-five-muhūrta conjunction, honey for its food, Aditi for its deity, Vāśiṣṭha by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** TWO stars, foot-shaped (pada-saṃsthāna), deity Aditi, gotra Vāśiṣṭha. Two stars = Castor and Pollux, confirming both the dual name and the Aditi lordship of the Vedic lists on file.</sub>

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

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, pp. 46–47** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> puṣya-nakṣatraṃ tritāraṃ vardhamāna-saṃsthānaṃ triśan-muhūrta-yogaṃ madhu-maṇḍāhāraṃ bṛhaspati-daivatam aupamanyavīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Puṣya asterism has three stars, is shaped like a vardhamāna, has a thirty-muhūrta conjunction, honey-cream for its food, Bṛhaspati for its deity, Aupamanyavīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** THREE stars, vardhamāna-shaped (an auspicious 'growing' diagram), deity Bṛhaspati, gotra Aupamanyavīya. Three stars = δ, γ, θ Cancri; matches Colebrooke's 'Stars in Cancer' for the Amarakośa's Puṣya/Sidhya/Tiṣya trio.</sub>

### आश्लेषा (Āśleṣā) — Ashlesha

**Modern identification:** Ashlesha — ε Hydrae, Hydra (*disputed*)

*See also:* `sarpa`

**Sūrya Siddhānta 8.19** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> रोहिण्यादित्यमूलानाम् प्राची सार्पस्य चैव हि / यथा प्रत्यवशेषाणाम् स्थूला स्याद् योगतारका //
>
> — *19. Of Rohini, Punarvasu (aditya), and Mula, it is the eastern, and so also of Açlesha (sarpa): in the case of each of the others, the junction-star (yogataraka) is the great (sthula) one.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Colebrooke pointed to α Cancri; Burgess rejects this ('α Cancri is not the eastern member of any group of five stars') and places the asterism in the circular group in Hydra's head, 'and ε Hydrae, its brightest star... is the junction-star', while conceding the latitude error is 'very considerable'.</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, pp. 46–47** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> aśleṣā-nakṣatram eka-tāraṃ tilaka-saṃsthānaṃ pañca-daśa-muhūrta-yogaṃ pāyasa-bhojanaṃ sarpa-daivataṃ maitrāyaṇīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Aśleṣā asterism has one star, is shaped like a forehead-mark, has a fifteen-muhūrta conjunction, milk-rice for its food, Sarpa for its deity, Maitrāyaṇīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** ONE star, tilaka-shaped, deity Sarpa (the Serpent), gotra Maitrāyaṇīya. The single-star count conflicts with the later five- or six-star Āśleṣā of the siddhāntas and supports taking the yogatārā (ε Hydrae) as the whole asterism in the older reckoning — which is some support for Burgess against Colebrooke's α Cancri. The Sarpa deity matches Sārpa already on file.</sub>

### मघा (Maghā) — Regulus

**Modern identification:** Regulus — α Leonis, Leo (*certain*)

*See also:* `agha`

**Sūrya Siddhānta 8.18** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> ज्येष्ठाश्रवणमैत्राणाम् बार्हस्पत्यस्य मध्यमा / भरण्याग्नेयपित्र्याणाम् रेवत्याश् चैव दक्षिणा //
>
> — *18. Of Jyeshtha, Çravana, Anuradha (maitra), and Pushya (barhaspatya), it is the middle star: of Bharani, Krttika (agneya), and Magha (pitrya), and likewise of Revati, it is the southern:*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: of the Sickle group, 'the star α Leonis, or Regulus, the most brilliant of the group, is the junction-star, and its position is defined with unusual precision'.</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, pp. 47–48** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> maghā-nakṣatraṃ pañca-tāraṃ nadī-kubja-saṃsthānaṃ triśan-muhūrta-yogaṃ tila-kṛsarāhāraṃ pitṛdaivataṃ piṅgalāyanīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Maghā asterism has five stars, is shaped like the bend of a river, has a thirty-muhūrta conjunction, sesame-and-rice gruel for its food, the Fathers for its deity, Piṅgalāyanīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** FIVE stars, shaped like a river-bend (nadī-kubja-saṃsthāna), deity Pitṛ (the Fathers), gotra Piṅgalāyanīya. Five stars in a curve = the Sickle of Leo (α, η, γ, ζ, μ Leonis). The Pitṛ deity confirms the Aghā/Maghā-of-the-Fathers association on file.</sub>

### पूर्वफल्गुनी (Pūrva-Phalgunī) — Zosma

**Modern identification:** Zosma — δ Leonis, Leo (*likely*)

*See also:* `arjuni`

**Sūrya Siddhānta 8.16** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> फाल्गुन्योर् भाद्रपदयोस् तथैवाषाढयोर् द्वयोः / विशाखाश्विनिसौम्यानाम् योगतारोत्तरा स्मृता //
>
> — *16. Of the two Phalgunis, the two Bhadrapadas, and likewise the two Ashadhas, of Viçakha, Açvini, and Mrgaçirsha (saumya), the junction-star (yogatara) is stated to be the northern (uttara):*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: of the pair δ and θ Leonis, 'the first group is, then, clearly identifiable as δ and θ Leonis, the former and brighter being the distinctive star'; he notes the Siddhānta-Śiromaṇi and Graha-Lāghava data may instead point to θ Leonis (the southern).</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, pp. 47–48** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> pūrvaphalgunī-nakṣatraṃ dvitāraṃ padaka-saṃsthānaṃ triśan muhūrta-yogaṃ vilvabhojanaṃ bhavadevataṃ gautamīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Pūrvaphalgunī asterism has two stars, is padaka-shaped, has a thirty-muhūrta conjunction, bilva fruit for its food, Bhava for its deity, Gautamīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** TWO stars, padaka-shaped (like a small pendant), deity Bhava, gotra Gautamīya. Two stars = δ and θ Leonis, which supports Burgess's pair against the alternatives. NOTE the deity Bhava (a Rudra-name) where the Brahmanical lists have Bhaga.</sub>

### उत्तरफल्गुनी (Uttara-Phalgunī) — Denebola

**Modern identification:** Denebola — β Leonis, Leo (*certain*)

*See also:* `arjuni`

**Sūrya Siddhānta 8.16** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> फाल्गुन्योर् भाद्रपदयोस् तथैवाषाढयोर् द्वयोः / विशाखाश्विनिसौम्यानाम् योगतारोत्तरा स्मृता //
>
> — *16. Of the two Phalgunis, the two Bhadrapadas, and likewise the two Ashadhas, of Viçakha, Açvini, and Mrgaçirsha (saumya), the junction-star (yogatara) is stated to be the northern (uttara):*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'In the latter group, the junction-star is evidently β Leonis'; the text's calling it 'northern' he regards 'as simply an error' of the describers.</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, pp. 47–48** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> uttaraphalgunī-nakṣatraṃ dvitāraṃ padaka-saṃsthānaṃ pañca-catvāriṃśan-muhūrta-yogaṃ godhūmamatsyāhāram aryamādaivataṃ kauśikaṃ gotreṇa/
>
> — *Literal rendering: 'The Uttaraphalgunī asterism has two stars, is padaka-shaped, has a forty-five-muhūrta conjunction, wheat and fish for its food, Aryamā for its deity, Kauśika by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** TWO stars, padaka-shaped, deity Aryamā, gotra Kauśika. Two stars = β and 93 Leonis; the Aryamā lordship agrees with the Vedic lists.</sub>

### हस्त (Hasta) — Gienah

**Modern identification:** Gienah — γ Corvi, Corvus (*disputed*)

**Sūrya Siddhānta 8.17** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> पश्चिमोत्तरताराया द्वितीया पश्चिमे स्थिता / हस्तस्य योगतारा सा श्रविष्ठायाश् च पश्चिमा //
>
> — *17. That which is the western northern star, being the second situated westward, that is the junction-star of Hasta; of Çravishtha it is the western:*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Five stars of Corvus. Burgess: v. 17's special description is 'quite hard to understand and apply: we regard it as most probable... that γ (3) is the star intended: the defined position... would point rather to δ (3)'. Colebrooke gave 'γ or δ Corvi'.</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, pp. 47–48; cf. Amarakośa 3.3.464** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> hasta-nakṣatraṃ pañca-tāraṃ hasta-saṃsthānaṃ triṃśan-muhūrta-yogaṃ śyāmākabhojanaṃ sūrya-daivataṃ kāśyapaṃ gotreṇa/ — cf. अमरकोश ३.३.४६४: हस्तौ तु पाणिनक्षत्रे मरुतौ पवनामरौ ॥
>
> — *Literal rendering: 'The Hasta asterism has five stars, is hand-shaped, has a thirty-muhūrta conjunction, śyāmāka millet for its food, Sūrya for its deity, Kāśyapa by gotra.' — Amarakośa: 'Hasta [means] the hand and the asterism.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** FIVE stars, hand-shaped (hasta-saṃsthāna), deity Sūrya, gotra Kāśyapa — the clearest possible confirmation of the Corvus identification and of the name's literal sense, and it settles that the asterism is the whole five-star figure whatever the yogatārā. The Amarakośa's Nānārtha-varga separately records that hasta has exactly two senses, 'hand' and 'the asterism'.</sub>

### चित्रा (Citrā) — Spica

**Modern identification:** Spica — α Virginis, Virgo (*certain*)

**Sūrya Siddhānta 8.19 (named in 8.21)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> अपाम्वत्सस् तु चित्राया उत्तरे +अम्शैस् तु पञ्चभिः / बृहत् किञ्चिद् अतो भागैर् आपः षड्भिस् तथोत्तरे //
>
> — *21. Apamvatsa is five degrees north from Citra: somewhat greater than it, as also six degrees to the north of it, is Apas.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'This is the beautiful star of the first magnitude α Virginis, or Spica, constituting an asterism by itself.' Named again in 8.21 as the reference star for Apāṃvatsa.</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, pp. 47–48** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> citrā-nakṣatram eka-tāraṃ tilaka-saṃsthānaṃ triṃśan-muhūrta-yogaṃ mudgakṛsaraghṛta-pūpāhāraṃ tvaṣṭṛdaivataṃ kātyāyanīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Citrā asterism has one star, is shaped like a forehead-mark, has a thirty-muhūrta conjunction, mung-gruel and ghee-cakes for its food, Tvaṣṭṛ for its deity, Kātyāyanīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** ONE star, tilaka-shaped, deity Tvaṣṭṛ, gotra Kātyāyanīya. The single-star count is decisive for Spica; the Tvaṣṭṛ lordship agrees with the Vedic lists.</sub>

### स्वाती (Svātī) — Arcturus

**Modern identification:** Arcturus — α Boötis, Boötes (*certain*)

*See also:* `nishtya`

**Sūrya Siddhānta 8.19 (positions 8.2, 8.7)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> रोहिण्यादित्यमूलानाम् प्राची सार्पस्य चैव हि / यथा प्रत्यवशेषाणाम् स्थूला स्याद् योगतारका //
>
> — *19. Of Rohini, Punarvasu (aditya), and Mula, it is the eastern, and so also of Açlesha (sarpa): in the case of each of the others, the junction-star (yogataraka) is the great (sthula) one.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Not individually named in ch. 8 (single-star asterism; sthūla rule 8.19; positions 8.2/8.7). Burgess: 'The star intended is plainly α Bootis, or Arcturus'.</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, p. 48** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> svātī-nakṣatram eka-tāraṃ tilaka-saṃsthānaṃ pañca-daśa-muhūrta-yogaṃ mudgakṛsaraphalāhāraṃ vāyudaivataṃ kātyāyanīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Svātī asterism has one star, is shaped like a forehead-mark, has a fifteen-muhūrta conjunction, mung-gruel and fruit for its food, Vāyu for its deity, Kātyāyanīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** ONE star, tilaka-shaped, deity Vāyu, gotra Kātyāyanīya. Single-star count decisive for Arcturus; the Vāyu lordship agrees with the Vedic lists and with Niṣṭya already on file.</sub>

### विशाखा (Viśākhā) — ι Librae

**Modern identification:** ι Librae — ι Librae, Libra (*disputed*)

**Sūrya Siddhānta 8.16** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> फाल्गुन्योर् भाद्रपदयोस् तथैवाषाढयोर् द्वयोः / विशाखाश्विनिसौम्यानाम् योगतारोत्तरा स्मृता //
>
> — *16. Of the two Phalgunis, the two Bhadrapadas, and likewise the two Ashadhas, of Viçakha, Açvini, and Mrgaçirsha (saumya), the junction-star (yogatara) is stated to be the northern (uttara):*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'the identification of Viçakha [is] in some respects more doubtful than that of any other asterism in the series'; the defined position identifies the junction-star with faint ι Librae, though he believes the asterism 'was originally composed of the two stars α and β Librae'. Colebrooke suggested o or χ Librae; modern lists often use α Librae (Zubenelgenubi).</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, p. 48** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> viśākhā-nakṣatraṃ dvitāraṃ viṣāṇa-saṃsthānaṃ pañca-catvāriṃśan-muhūrta-yogaṃ tila-puṣpāhāram indrāgnidaivataṃ śāṃkhāyanīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Viśākhā asterism has two stars, is horn-shaped, has a forty-five-muhūrta conjunction, sesame and flowers for its food, Indra-and-Agni for its deity, Śāṃkhāyanīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** TWO stars, horn-shaped (viṣāṇa-saṃsthāna), deity Indrāgni, gotra Śāṃkhāyanīya. This bears directly on the most doubtful identification in the whole series: the two-star count sides with the 'ancient authors' whom Colebrooke cites against the later four-star reckoning, and the horn figure fits the two scale-stars α and β Librae — i.e. it supports Burgess's own belief that the asterism 'was originally composed of α and β Librae' rather than the faint ι Librae his coordinates forced on him.</sub>

### अनुराधा (Anurādhā) — Dschubba

**Modern identification:** Dschubba — δ Scorpii, Scorpius (*certain*)

**Sūrya Siddhānta 8.18** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> ज्येष्ठाश्रवणमैत्राणाम् बार्हस्पत्यस्य मध्यमा / भरण्याग्नेयपित्र्याणाम् रेवत्याश् चैव दक्षिणा //
>
> — *18. Of Jyeshtha, Çravana, Anuradha (maitra), and Pushya (barhaspatya), it is the middle star: of Bharani, Krttika (agneya), and Magha (pitrya), and likewise of Revati, it is the southern:*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: the row β, δ, π Scorpionis, 'δ (2.3) being the junction-star' (the middle, per v. 18).</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, p. 49** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> anurādhā-nakṣatraṃ catustāraṃ ratnābalī-saṃsthānaṃ triśan-muhūrta-yogaṃ surāmāṃsāhāraṃ mitradaivatam ālaṃbāyanīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Anurādhā asterism has four stars, is shaped like a string of jewels, has a thirty-muhūrta conjunction, liquor and meat for its food, Mitra for its deity, Ālaṃbāyanīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** FOUR stars, shaped like a string of jewels (ratnāvalī-saṃsthāna), deity Mitra, gotra Ālaṃbāyanīya. The jewel-string of four fits β, δ, π, ρ Scorpii. Mitra lordship agrees with the Vedic lists and with the siddhāntic epithet Maitra.</sub>

### ज्येष्ठा (Jyeṣṭhā) — Antares

**Modern identification:** Antares — α Scorpii, Scorpius (*certain*)

*See also:* `rohini-indra`

**Sūrya Siddhānta 8.18** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> ज्येष्ठाश्रवणमैत्राणाम् बार्हस्पत्यस्य मध्यमा / भरण्याग्नेयपित्र्याणाम् रेवत्याश् चैव दक्षिणा //
>
> — *18. Of Jyeshtha, Çravana, Anuradha (maitra), and Pushya (barhaspatya), it is the middle star: of Bharani, Krttika (agneya), and Magha (pitrya), and likewise of Revati, it is the southern:*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: the central of three (with σ and τ Scorpionis) is 'the brilliant star of the first magnitude α Scorpionis, or Antares'.</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, p. 49** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> jyeṣṭhā-nakṣatraṃ tritāraṃ yavamadhya-saṃsthānaṃ pañca-daśa-muhūrta-yogaṃ śāliyavāgubhojanam indradaivataṃ dīrghakātyāyanīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Jyeṣṭhā asterism has three stars, is shaped like the middle of a barleycorn, has a fifteen-muhūrta conjunction, rice gruel for its food, Indra for its deity, Dīrghakātyāyanīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** THREE stars, shaped like a barleycorn's middle (yavamadhya-saṃsthāna, a lens/fusiform figure), deity Indra, gotra Dīrghakātyāyanīya. Three stars in a fusiform = σ, α, τ Scorpii, exactly Burgess's group. Indra lordship agrees with the Vedic lists and with Jyeṣṭhaghnī already on file.</sub>

### मूल (Mūla) — Shaula

**Modern identification:** Shaula — λ Scorpii, Scorpius (*likely*)

*See also:* `vichritau`, `mulabarhana`

**Sūrya Siddhānta 8.19** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> रोहिण्यादित्यमूलानाम् प्राची सार्पस्य चैव हि / यथा प्रत्यवशेषाणाम् स्थूला स्याद् योगतारका //
>
> — *19. Of Rohini, Punarvasu (aditya), and Mula, it is the eastern, and so also of Açlesha (sarpa): in the case of each of the others, the junction-star (yogataraka) is the great (sthula) one.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Stars of the Scorpion's tail. Burgess: 'if, as seems probable, λ is the star pointed out by the definition of position', the 'eastern' designation is strictly true only of the pair λ and ν (the Vedic vicṛtāu); ι, κ, and θ lie farther east.</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, p. 49** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> mūla-nakṣatraṃ saptatāraṃ vṛścika-saṃsthānaṃ triśan-muhūrta-yogaṃ mūlaphalāhāraṃ nairṛtidaivataṃ kātyāyanīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Mūla asterism has seven stars, is shaped like a scorpion, has a thirty-muhūrta conjunction, roots and fruits for its food, Nairṛti for its deity, Kātyāyanīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** SEVEN stars, SCORPION-SHAPED (vṛścika-saṃsthāna), deity Nairṛti, gotra Kātyāyanīya. This is the strongest single confirmation in the whole chapter, because the text names the constellation-figure outright — seven stars in the Scorpion's sting-curve. It corroborates Vicṛtau and Mūlabarhaṇa already on file, and Colebrooke independently glosses Sanskrit mūla in the Nānārtha section as 'an asterism (the Scorpion's tail)'.</sub>

### पूर्वाषाढा (Pūrvāṣāḍhā) — Kaus Media

**Modern identification:** Kaus Media — δ Sagittarii, Sagittarius (*certain*)

**Sūrya Siddhānta 8.16 (also 8.4)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> फाल्गुन्योर् भाद्रपदयोस् तथैवाषाढयोर् द्वयोः / विशाखाश्विनिसौम्यानाम् योगतारोत्तरा स्मृता //
>
> — *16. Of the two Phalgunis, the two Bhadrapadas, and likewise the two Ashadhas, of Viçakha, Açvini, and Mrgaçirsha (saumya), the junction-star (yogatara) is stated to be the northern (uttara):*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'The former group must comprise δ (3.4) and ε (3.2) Sagittarii, the former being the junction-star; this is shown by the... comparison of positions'. Called āpya (of the Waters) in 8.4.</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, p. 49** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> pūrvāṣāḍhā-nakṣatraṃ catustāraṃ govikrama-saṃsthānaṃ triśan-muhūrta-yogaṃ nyagrodhakaṣāyāhāraṃ toyadaivataṃ darbhakātyāyanīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Pūrvāṣāḍhā asterism has four stars, is shaped like a cow's stride, has a thirty-muhūrta conjunction, banyan decoction for its food, the Waters for its deity, Darbhakātyāyanīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** FOUR stars, shaped like a cow's stride (govikrama-saṃsthāna), deity Toya ('the Waters' = Āpas), gotra Darbhakātyāyanīya. The Toya deity is the Buddhist form of the āpya lordship the Sūrya Siddhānta uses. The paired cow-stride/elephant-stride figures for the two Āṣāḍhās are a Buddhist speciality.</sub>

### उत्तराषाढा (Uttarāṣāḍhā) — Nunki

**Modern identification:** Nunki — σ Sagittarii, Sagittarius (*likely*)

**Sūrya Siddhānta 8.16 (also 8.4)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> मनवो +अथ रसा वेदा वैश्वम् आप्यार्धभोगगम् / आप्यस्यैवाभिजित् प्रान्ते वैश्वान्ते श्रवणस्थितिः /
>
> — *4. Fourteen, six, four: Uttara-Ashadha (vaiçva) is at the middle of the portion (bhoga) of Purva-Ashadha (apya); Abhijit, likewise, is at the end of Purva-Ashadha; the position of Çravana is at the end of Uttara-Ashadha;*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: 'its northern and junction-star can be no other than σ (2.3)... notwithstanding the error in the Hindu determination of its latitude, which led Colebrooke to regard τ (4.3) as the star intended'. Called vaiśva (of the Viśve Devāḥ) in 8.4.</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, p. 49** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> uttarāṣāḍhā-nakṣatraṃ catustāraṃ gajavikrama-saṃsthānaṃ pañca-catvāriṃśan-muhūrta-yogaṃ madhu-lājāhāraṃ viśva-daivataṃ maudgalāyanīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Uttarāṣāḍhā asterism has four stars, is shaped like an elephant's stride, has a forty-five-muhūrta conjunction, honey and parched grain for its food, the All-Gods for its deity, Maudgalāyanīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** FOUR stars, shaped like an elephant's stride (gajavikrama-saṃsthāna), deity Viśva (the Viśve Devāḥ), gotra Maudgalāyanīya. The Viśvadeva lordship agrees with the Vedic lists and with the Sūrya Siddhānta's vaiśva.</sub>

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

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, pp. 49–51; cf. Sūryaprajñapti as reported by Thibaut (1880), pp. 186–188** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> abhijin-nakṣatraṃ tritāraṃ gośīrsa-saṃsthānaṃ ṣaṇ-muhūrta-yogaṃ vāyuāhāraṃ brahma-daivataṃ brahmāvatīyaṃ gotreṇa/ ... eko +abhijit ṣaṇ-muhūrta-yogaḥ/
>
> — *Literal rendering: 'The Abhijit asterism has three stars, is shaped like a cow's head, has a six-muhūrta conjunction, air for its food, Brahmā for its deity, Brahmāvatīya by gotra.' ... 'One alone, Abhijit, has a six-muhūrta conjunction.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** THREE stars, cow's-head-shaped (gośīrṣa-saṃsthāna), deity Brahmā, gotra Brahmāvatīya — and uniquely a SIX-muhūrta conjunction where every other asterism has 15, 30 or 45. The text singles this out again a page later: 'one alone, Abhijit, has a six-muhūrta conjunction'. Three stars in a cow's-head = α, ε, ζ Lyrae, matching Burgess's triangle. The anomalously small extent is precisely the peculiarity behind Abhijit's later expulsion from the 27-fold scheme — and the Jain canon independently makes Abhijit a class of its own with a 9 4/67-muhūrta conjunction (Thibaut 1880: 'There is no special name for the extent of Abhijit').</sub>

**Sūrya Siddhānta 9.12, 9.18 and 13.8** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_उदयास्ताधिकारः)

> अभिजिद् ब्रह्महृदयम् स्वातीवैष्णववासवाः / अहिर्बुध्न्यम् उदक्स्थत्वान् न लुप्यन्ते ऽर्करश्मिभिः //
>
> — *18. Abhijit, Brahmahrdaya, Svati, Çravana (vāishnava), Çravishtha (vāsava), and Uttara-Bhādrapadā (ahirbudhnya), owing to their northern situation, are not extinguished by the sun's rays.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** Named at SS 9.12 (13° class) and heading the SS 9.18 list of stars never obscured by the sun; also at SS 13.8 among the stars needing day-circles on the armillary sphere. Al-Bīrūnī's independent lists give al-Nasr al-Wāqiʿ (Vega) in both positions, and his nakshatra table assigns Abhijit polar longitude 265° and 62° north latitude.</sub>

### श्रवण (Śravaṇa) — Altair

**Modern identification:** Altair — α Aquilae, Aquila (*certain*)

*See also:* `ashvattha`

**Sūrya Siddhānta 8.18 (also 8.4)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> ज्येष्ठाश्रवणमैत्राणाम् बार्हस्पत्यस्य मध्यमा / भरण्याग्नेयपित्र्याणाम् रेवत्याश् चैव दक्षिणा //
>
> — *18. Of Jyeshtha, Çravana, Anuradha (maitra), and Pushya (barhaspatya), it is the middle star: of Bharani, Krttika (agneya), and Magha (pitrya), and likewise of Revati, it is the southern:*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: three stars 'in the back and neck of the Eagle, namely α, γ, and β Aquilae; α, the determinative [middle star, v. 18], is a star of the first to second magnitude'.</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, p. 49** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> śravaṇā-nakṣatraṃ tritāraṃ yavamadhya-saṃsthānaṃ triṃśan-muhūrta-yogaṃ pakṣimāṃsāhāraṃ viṣṇudaivataṃ kātyāyanīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Śravaṇā asterism has three stars, is shaped like the middle of a barleycorn, has a thirty-muhūrta conjunction, birds' flesh for its food, Viṣṇu for its deity, Kātyāyanīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** THREE stars, barleycorn-middle-shaped (yavamadhya-saṃsthāna), deity Viṣṇu, gotra Kātyāyanīya. Three stars in a fusiform = β, α, γ Aquilae, exactly Burgess's group. Viṣṇu lordship agrees with the Vedic lists and with the siddhāntic epithet Vaiṣṇava.</sub>

### श्रविष्ठा (Śraviṣṭhā (Dhaniṣṭhā)) — Rotanev

**Modern identification:** Rotanev — β Delphini, Delphinus (*certain*)

**Sūrya Siddhānta 8.17 (also 8.5)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> त्रिचतुः पादयोः सन्धौ श्रविष्ठा श्रवणस्य तु / स्वभोगतो वियन् नागाः षट्कृतिर् यमलाश्विनः //
>
> — *5. Çravishtha, on the other hand, is at the point of connection of the third and fourth quarters (pada) of Çravana: then, in their own portions, eighty, thirty-six, twenty-two,*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: the diamond in the Dolphin's head, β α γ δ Delphini; 'The junction-star, which is the western (v. 17), is β'.</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, p. 50** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> dhaniṣṭhā-nakṣatraṃ catustāraṃ śakuna-saṃsthānaṃ triṃśan-muhūrta-yogaṃ kulatthapūpāhāraṃ vasudaivataṃ kauṇḍinyāyanīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Dhaniṣṭhā asterism has four stars, is shaped like a bird, has a thirty-muhūrta conjunction, horse-gram cakes for its food, the Vasus for its deity, Kauṇḍinyāyanīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** FOUR stars, BIRD-shaped (śakuna-saṃsthāna), deity Vasu, gotra Kauṇḍinyāyanīya. Four stars in a bird-figure = the Delphinus quadrilateral (α, β, γ, δ Del), agreeing exactly with Colebrooke's 'The Dolphin' for Śraviṣṭhā. Vasu lordship agrees with the Vedic lists and the siddhāntic epithet Vāsava.</sub>

### शतभिषज् (Śatabhiṣaj) — Hydor

**Modern identification:** Hydor — λ Aquarii, Aquarius (*disputed*)

**Sūrya Siddhānta 8.19 (positions 8.3, 8.9)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> रोहिण्यादित्यमूलानाम् प्राची सार्पस्य चैव हि / यथा प्रत्यवशेषाणाम् स्थूला स्याद् योगतारका //
>
> — *19. Of Rohini, Punarvasu (aditya), and Mula, it is the eastern, and so also of Açlesha (sarpa): in the case of each of the others, the junction-star (yogataraka) is the great (sthula) one.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Not individually named in ch. 8; its junction-star is the brightest of its hundred (sthūla rule, 8.19). Burgess: 'This, from its defined position, can only be λ Aquarii (4)'. Some later scholars have proposed other Aquarii stars; al-Bīrūnī could not identify it.</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, p. 50** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> śatabhiṣā-nakṣatram eka-tāraṃ tilaka-saṃsthānaṃ pañca-daśa-muhūrta-yogaṃ yavāgubhojanaṃ varuṇadaivataṃ tāṇḍyāyanīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Śatabhiṣā asterism has one star, is shaped like a forehead-mark, has a fifteen-muhūrta conjunction, barley gruel for its food, Varuṇa for its deity, Tāṇḍyāyanīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** ONE star, tilaka-shaped, deity Varuṇa, gotra Tāṇḍyāyanīya. The single-star count is striking against the 'hundred physicians/stars' the name suggests: the Buddhist tradition evidently took only the yogatārā. Varuṇa lordship agrees with the Vedic lists. Note the name-form Śatabhiṣā rather than Śatabhiṣaj, matched by the Pali Satabhisaja.</sub>

**Al-Bīrūnī, India ch. LV, table of the lunar stations (Sachau 1910, vol. 2)** — [Sanskrit e-text](https://archive.org/download/alberunisindia_201612/alberunisindia-color_002_djvu.txt)

> *No Sanskrit text: al-Bīrūnī wrote in Arabic, and the passage survives here only in Sachau's English.*
>
> — *24. Śatabhishaj ... Southern. Unknown. Most likely identical with the upper part of the hip-joint of Aquarius.*
> <br>— E. Sachau (1910) ([source](https://archive.org/download/alberunisindia_201612/alberunisindia-color_002_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** AL-BĪRŪNĪ COULD NOT IDENTIFY IT — independent evidence that the disputed status on file is not a modern artefact. His table leaves the note 'Unknown. Most likely identical with the upper part of the hip-joint of Aquarius', a guess that does not obviously land on λ Aquarii. He is equally defeated by Viśākhā, Pūrvabhādrapadā, Ārdrā, Āśleṣā and Dhaniṣṭhā, while being confident and correct wherever the Arabic manzil tradition gave him an anchor (Kṛttikā = al-Thurayyā, Rohiṇī = Aldabarān, Maghā = al-Jabha, Citrā = al-Simāk al-Aʿzal, Jyeṣṭhā = the Heart of Scorpio, Mūla = al-Shaula, and so on). Śatabhiṣaj sits precisely in the gap between the two systems, which is why it defeated him.</sub>

### पूर्वभाद्रपदा (Pūrva-Bhādrapadā) — Markab

**Modern identification:** Markab — α Pegasi, Pegasus (*certain*)

**Sūrya Siddhānta 8.16** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> फाल्गुन्योर् भाद्रपदयोस् तथैवाषाढयोर् द्वयोः / विशाखाश्विनिसौम्यानाम् योगतारोत्तरा स्मृता //
>
> — *16. Of the two Phalgunis, the two Bhadrapadas, and likewise the two Ashadhas, of Viçakha, Açvini, and Mrgaçirsha (saumya), the junction-star (yogatara) is stated to be the northern (uttara):*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Part of the Square of Pegasus. Burgess: 'The junction-star of the former half-asterism is, by its defined position, clearly shown to be α Pegasi', though the 'northern' designation of v. 16 conflicts (α is the southern of the pair with β).</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, p. 50** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> pūrvabhādrapadā-nakṣatraṃ dvitāraṃ padaka-saṃsthānaṃ triṃśan-muhūrta-yogaṃ māṃsa-rudhirāhāram ahirbudhnyadaivataṃ jātūkarṇyaṃ gotreṇa/
>
> — *Literal rendering: 'The Pūrvabhādrapadā asterism has two stars, is padaka-shaped, has a thirty-muhūrta conjunction, flesh and blood for its food, Ahirbudhnya for its deity, Jātūkarṇya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** TWO stars, padaka-shaped, deity Ahirbudhnya, gotra Jātūkarṇya. Two stars = α and β Pegasi; the Ahirbudhnya lordship agrees with the Vedic lists.</sub>

### उत्तरभाद्रपदा (Uttara-Bhādrapadā) — Algenib / Alpheratz

**Modern identification:** Algenib / Alpheratz — γ Pegasi / α Andromedae, Pegasus / Andromeda (*disputed*)

**Sūrya Siddhānta 8.16** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_भग्रहयुत्यधिकारः)

> फाल्गुन्योर् भाद्रपदयोस् तथैवाषाढयोर् द्वयोः / विशाखाश्विनिसौम्यानाम् योगतारोत्तरा स्मृता //
>
> — *16. Of the two Phalgunis, the two Bhadrapadas, and likewise the two Ashadhas, of Viçakha, Açvini, and Mrgaçirsha (saumya), the junction-star (yogatara) is stated to be the northern (uttara):*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Sūrya Siddhānta):** Burgess: the text's position gives 'a longitude... of one member of the group [γ Pegasi], and a latitude which is that of the other [α Andromedae]'; 'There can be no doubt that the two stars recognized as composing the asterism are γ Pegasi and α Andromedae, but there has evidently been a blundering confusion of the two'. Modern lists usually take γ Pegasi.</sub>

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, pp. 50–51** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> uttarabhādrapadā-nakṣatraṃ dvitāraṃ padaka-saṃsthānaṃ pañca-catvāriṃśan-muhūrta-yogaṃ māṃsāhāram aryamādaivataṃ dhyānadrāhyāyaṇīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Uttarabhādrapadā asterism has two stars, is padaka-shaped, has a forty-five-muhūrta conjunction, flesh for its food, Aryamā for its deity, Dhyānadrāhyāyaṇīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** TWO stars, padaka-shaped, deity Aryamā, gotra Dhyānadrāhyāyaṇīya. The two-star count supports the pair γ Pegasi + α Andromedae that Burgess said the text confuses — evidence the confusion is his sources', not the tradition's. NOTE the deity Aryamā where the Brahmanical lists have Ahirbudhnya, duplicating Uttaraphalgunī's deity.</sub>

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

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, p. 51** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> revatī-nakṣatram eka-tāraṃ tilaka-saṃsthānaṃ triśan-muhūrta-yogaṃ dadhyāhāraṃ pūṣadaivatam aṣṭabhaginīyaṃ gotreṇa/
>
> — *Literal rendering: 'The Revatī asterism has one star, is shaped like a forehead-mark, has a thirty-muhūrta conjunction, curds for its food, Pūṣan for its deity, Aṣṭabhaginīya by gotra.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** ONE star, tilaka-shaped, deity Pūṣa, gotra Aṣṭabhaginīya ('of the eight sisters'). The single-star count matches the siddhāntic use of Revatī's yogatārā as the zero-point of the sphere; Pūṣan lordship agrees with the Vedic lists.</sub>

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

**Bhāgavata Purāṇa 5.23.7; Viṣṇu Purāṇa 2.8.85; Vāyu Purāṇa 50.208; Matsya Purāṇa 124.97** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/3_purana/bhagp/bhp_05u.htm)

> उत्तराहनावगस्तिरधराहनौ यमो ... ॥ ७ ॥ — cf. विष्णुपुराण २.८.८५: उत्तरं [य]दगस्त्यस्य अजवीथ्याश्च दक्षिणम्।
>
> — *And on the upper jaw of the Sisumara is Agastya, and on its lower jaw is Yama. / On the north of Agastya, and south of the line of the Goat, exterior to the Vaiswánara path, lies the road of the Pitris.*
> <br>— J.M. Sanyal (1930s) and H.H. Wilson (1840); both public domain ([source](https://archive.org/details/in.ernet.dli.2015.187346))

<sub>**Identification notes (Purāṇas):** Two new Purāṇic attestations with distinct content: (a) Bhāgavata 5.23.7 places Agasti on the UPPER JAW of the Śiśumāra — a body-part assignment; (b) Viṣṇu P. 2.8.85 and Vāyu 50.208 use Agastya as the SOUTHERN LATITUDE MARKER bounding the Pitṛyāṇa, which is astronomically apt for Canopus, the brightest star of the far south. Neither text states the Canopus equation; it rests on universal later tradition.</sub>

**Amarakośa 1.3.215–216 (Dig-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> ध्रुव औत्तानपादिः स्यातगस्त्यः कुम्भसम्भवः ॥ १.३.२१५ ॥ मैत्रावरुणिरस्यैव लोपामुद्रा सधर्मिणी ॥ १.३.२१६ ॥
>
> — *Footnote: 'Agastya [is] regent of the star Canopus.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** The lexicon groups Agastya immediately after Dhruva, i.e. it treats the two as the paired southern and northern markers. Colebrooke's footnote calls Agastya 'regent of the star Canopus' — the earliest public-domain English statement of the identification.</sub>

**Sūrya Siddhānta 9.12; also Brāhmasphuṭasiddhānta, Bhagrahayutyadhikāra 35–37; Pañcasiddhāntikā XIV.39–41; Graha-Lāghava (per Burgess)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_उदयास्ताधिकारः)

> स्वात्यगस्त्यमृगव्याधचित्राज्येष्ठाः पुनर्वसुः / अभिजिद् ब्रह्महृदयम् त्रयोदशभिर् अम्शकैः //
>
> — *12. Svati, Agastya, Mrgavyadha, Citra, Jyeshtha, Punarvasu, Abhijit, and Brahmahrdaya rise and set at thirteen degrees.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** Listed among the stars needing only 13 kālāṃśas of distance from the sun to be visible — i.e. the brightest class. Burgess notes this class 'is, indeed, almost wholly composed of stars of the first magnitude'. Independently corroborated by al-Bīrūnī, who gives 13° for Suhail (Canopus) heading the identical list. THREE FURTHER WITNESSES with coordinates: Brahmagupta (Bhagrahayutyadhikāra 35–37) gives dhruva 27° Gemini = 87°, śara 77° S, arc 12° — far better than SS 8.11's 90°/80° S (true c. 85°04'/75°50' S); Varāhamihira's Pañcasiddhāntikā XIV.39–41 implies 75°30' S, which Thibaut reverse-engineered from the rule and which is the best ancient figure of all; and the Graha-Lāghava (1520) has 80°/76° S, correct in latitude but as wrong in longitude as the Sūrya Siddhānta, in the opposite direction. Burgess: 'The Siddhanta-Çiromani and (according to Colebrooke) the Brahma-Siddhanta give Agastya 87° of polar longitude, and 77° of latitude, which is a fair approximation to the truth.'</sub>

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

**Sūrya Siddhānta 9.12; Brāhmasphuṭasiddhānta, Bhagrahayutyadhikāra 40** — [Sanskrit e-text](https://archive.org/download/Brahmasphutasiddhanta/Brahmasphutasiddhanta_djvu.txt)

> षड्विंशे मिथुनांशेंऽशकचत्वारिंशच्छरदाता मृगव्याधः । तत्क्रान्तेर्दक्षिणतो विक्षिप्तोऽगस्त्यवच्छेषम् ॥ ४० ॥
>
> — *No public-domain translation of this chapter exists — Colebrooke (1817) rendered only BSS chs. 12 and 18, both purely mathematical. Sense: 'Mṛgavyādha stands in the twenty-sixth degree of Gemini, displaced forty degrees to the south of the declination-circle there; the rest (the finding of the suns of his rising and setting) is as for Agastya.'*
> <br>— Paraphrase by the compiler; Sanskrit normalised from the OCR of Ram Swarup Sharma's edition ([source](https://archive.org/download/Brahmasphutasiddhanta/Brahmasphutasiddhanta_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** Same 13° visibility class as Agastya at SS 9.12. Brahmagupta (Bhagrahayutyadhikāra 40) gives dhruva 26° Gemini = 86°, śara 40° S, arc 13°; his commentary notes the latitude matches the Sūrya Siddhānta's but the longitude differs (SS: 80°) 'and that difference is directly visible to the eye' — i.e. Brahmagupta corrected it by observation. Burgess agrees: 'while all authorities agree with the correct determination of the latitude of Sirius presented by our text, the Siddhanta-Çiromani etc. greatly reduce its error of longitude, by giving the star 86°, instead of 80°.' Al-Bīrūnī's quotation of Brahmagupta's Uttara-Khaṇḍakhādyaka matches exactly: '26° Orion, its southern latitude 40 parts... 13' for the heliacal-rising arc.</sub>

### लुब्धक (Lubdhaka) — Sirius

**Modern identification:** Sirius — α Canis Majoris, Canis Major (*disputed*)

*See also:* `mrigavyadha`

**Not in Bṛhat Saṃhitā; Kathāsaritsāgara 6.2.88 (lubdhaka); Sūrya-siddhānta 8.10 (as Mṛgavyādha)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/कथासरित्सागरः/लम्बकः_६/तरङ्गः_२)

> दत्त्वायुषोऽर्धं मुनिना न भार्या रुरुणा कृता ।
> त्रिशङ्कुः किं न नीतो द्यां विश्वामित्रेण लुब्धकः ।। ८८
>
> *The word is absent from the Bṛhat Saṃhitā itself; the verse quoted is the Kathāsaritsāgara's, which the citation names.*
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

**Amarakośa 2.10.1437 (Śūdra-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/द्वितीयकाण्डम्)

> व्याधो मृगवधाजीवो मृगयुर्लुब्धकोऽपि सः ।। २.१०.१४३७ ।।
>
> — *Literal rendering: 'A hunter (vyādha) — one who lives by killing deer, mṛgayu, and lubdhaka likewise.'*
> <br>— Literal rendering by the compiler ([source](https://sa.wikisource.org/wiki/अमरकोशः/द्वितीयकाण्डम्))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** IMPORTANT NEGATIVE RESULT: the Amarakośa does NOT list Lubdhaka or Mṛgavyādha among stars. Its only entry for lubdhaka is in the Śūdra-varga, where it is one of four synonyms for 'hunter' (vyādha, mṛgavadhājīva, mṛgayu, lubdhaka). The classical thesaurus therefore supplies the lexical basis of the Sirius-name — hunter of the Deer — but does not itself attest the astronomical use, which comes instead from the siddhāntas.</sub>

**Brāhmasphuṭasiddhānta, Bhagrahayutyadhikāra 40 with Pṛthūdakasvāmin's commentary** — [Sanskrit e-text](https://archive.org/download/Brahmasphutasiddhanta/Brahmasphutasiddhanta_djvu.txt)

> भानां ग्रहस्य लुब्धकस्य मुनेरगस्त्यस्य चोदयास्तादिसाधनम् ।
>
> — *No public-domain translation exists. Sense: 'the determination of the risings, settings and so forth of the asterisms, of a planet, of Lubdhaka, and of the sage Agastya.'*
> <br>— Paraphrase by the compiler ([source](https://archive.org/download/Brahmasphutasiddhanta/Brahmasphutasiddhanta_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** Lubdhaka and Mṛgavyādha are strictly synonymous in Brahmagupta's tradition: the heading of the verse in this edition reads 'idānīṃ lubdhakasya dhruvaśarāṃśān āha' — 'now he states the polar longitude and latitude degrees OF LUBDHAKA' — introducing the verse whose subject-word is mṛgavyādhaḥ. Pṛthūdaka's gloss on the chapter-scope verse likewise lists 'the risings and settings of the asterisms, of a planet, of Lubdhaka, and of the sage Agastya'. Śrīpati's Siddhāntaśekhara also uses Lubdhaka. This is the astronomical attestation the Amarakośa conspicuously lacks.</sub>

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

**Sūrya Siddhānta 9.12 and 9.18; al-Bīrūnī, India ch. LVI** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_उदयास्ताधिकारः)

> अभिजिद् ब्रह्महृदयम् स्वातीवैष्णववासवाः / अहिर्बुध्न्यम् उदक्स्थत्वान् न लुप्यन्ते ऽर्करश्मिभिः //
>
> — *18. Abhijit, Brahmahrdaya, Svati, Çravana (vāishnava), Çravishtha (vāsava), and Uttara-Bhādrapadā (ahirbudhnya), owing to their northern situation, are not extinguished by the sun's rays. — Al-Bīrūnī (Sachau): 'They are, according to the author of the Ghurrat-alzījāt, the following:—13° for Suhail, Alyamāniya, Alwāki', Alayyūk, Alsimākān, Kalb-al-akrab...' and, from Vijayanandin: 'Some stars are not covered by the rays nor impaired in their shining by the sun, viz. Alayyūk, Alsimāk, Alrāmiḥ, the two Eagles, Dhanishtha, and Uttarabhādrapadā, because they have so much northern latitude.'*
> <br>— E. Burgess (1860); E. Sachau (1910) for al-Bīrūnī ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** Named twice in SS ch. 9: at 9.12 among the 13°-visibility stars, and at 9.18 among the six never extinguished by the sun's rays 'owing to their northern situation'. Burgess adds that Prajāpati (δ Aurigae) is not counted here 'since it is 8° north of Brahmahrdaya, and consequently can not become invisible where the latter does not'. DECISIVE INDEPENDENT CONFIRMATION: al-Bīrūnī reproduces both lists in Arabic star names, and al-Ayyūq is unambiguously Capella in Arabic astronomy — so the identification is settled without relying on the Hindu coordinate data at all. The same passage settles Svātī = Arcturus (al-Simāk al-Rāmiḥ) the same way.</sub>

### प्रजापति (Prajāpati) — Prijipati

**Modern identification:** Prijipati — δ Aurigae, Auriga (*likely*)

*See also:* `prajapati-circumpolar`

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

*See also:* `saptarshi`, `arundhati`, `shishumara`, `medhi`, `suniti`, `vishnupada`

**Āśvalāyana Gṛhya Sūtra 1.7.22** — [Sanskrit e-text](https://sa.wikisource.org/wiki/आश्वलायनगृह्यसूत्रम्/अध्यायः_१)

> ध्रुवमरुन्धतीं सप्तऋषीनिति दृष्ट्वा वाचं विसृजेत जीवपत्नीं प्रजां विन्देयेति २२
>
> — *When she sees the polar-star, the star Arundhati, and the seven Rishis (ursa major), let her break the silence (and say), 'May my husband live and I get offspring.'*
> <br>— Hermann Oldenberg, SBE vol. 29 (1886) ([source](https://sacred-texts.com/hin/sbe29/sbe29.txt) · [mirror](https://web.archive.org/web/20080113225826/http://sacred-texts.com/hin/sbe29/sbe29.txt))

<sub>**Identification notes (Vedic corpus):** 'The fixed one', shown to the bride on the wedding night (dhruva-darśana) as an emblem of constancy. In the historical period Dhruva = Polaris, but scholars note that at plausible dates of the ritual's origin (2nd-1st millennium BCE) no bright star stood at the pole: α Draconis (Thuban) was pole star c. 2800 BCE, and Polaris only closed on the pole in the last ~1500 years. Dhruva may therefore be an idealized 'fixed point' of the sky, an earlier pole star remembered, or a faint near-polar star. Parallel rite with the mantra dhruvám asi: Śāṅkhāyana GS 1.17.2-4, tr. Oldenberg: 'Let them sit silent, when the sun has set, until the polar-star appears. He shows her the polar-star with the words, Firm be thou, thriving with me! Let her say, I see the polar-star; may I obtain offspring' (same source URL).</sub>

**Viṣṇu Purāṇa 1.12.90-92; Bhāgavata Purāṇa 5.23.1 and 5.23.5; Viṣṇu Purāṇa 2.7.10, 2.9.1** — [Sanskrit e-text](https://sa.wikisource.org/wiki/विष्णुपुराणम्/प्रथमांशः/अध्यायः_१२)

> त्रैलोक्यादधिके स्थाने सर्वताराग्रहाश्रयः । भविष्यति न संदेहो मत्प्रसादाद्भावन्ध्रुव ॥ १,१२.९० ॥ सूर्यात्सोमात्तथा भौमात्सोमपुत्राद्बृहस्पतेः । सितार्कतनयादीनां सर्वर्क्षाणां तथा ध्रुवः ॥ १,१२.९१ ॥
>
> — *A station shall be assigned to thee, Dhruva, above the three worlds; one in which thou shalt sustain the stars and the planets; a station above those of the sun, the moon, Mars, the son of Soma (Mercury), Venus, the son of Súrya (Saturn), and all the other constellations; above the regions of the seven Rishis, and the divinities who traverse the atmosphere.*
> <br>— H.H. Wilson (1840; public domain) ([source](https://www.sacred-texts.com/hin/vp/vp047.htm))

<sub>**Identification notes (Purāṇas):** New Purāṇic attestations, each adding something: (a) BP 5.23.1 places Dhruva 1.3 million yojanas above Saturn's region, circled by five star-deities — the fullest positional statement; (b) BP 5.23.5 fixes him at the tail-TIP (pucchāgra) of the Śiśumāra, more precise than Viṣṇu P. 2.9's 'in the tail'; (c) VP 1.12.90-92 grants him a station above Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn, all asterisms and the Saptarṣis. On identification, note honestly that Polaris was NOT at the pole when these texts were composed — precession puts Thuban near the pole c. 3000-2500 BCE and Polaris only in the last few centuries; R.N. Iyengar and R.S. Hariharan argue the figure preserves a memory of Thuban, which remains a reconstruction.</sub>

**Amarakośa 1.3.215 (Dig-varga); second sense at 3.3.792 (Nānārtha-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> ध्रुव औत्तानपादिः स्यातगस्त्यः कुम्भसम्भवः ॥ १.३.२१५ ॥ — cf. ध्रुवो भभेदे क्लीबे तु निश्चिते शाश्वते त्रिषु ॥ ३.३.७९२ ॥
>
> — *'The pole.' Footnote: 'Or the north pole itself. In mythology, Dhruva is son of Uttānapāda, and consequently grandson of the first Manu. In Astronomy, Uttānapāda is Ursa minor.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** Amarakośa gives Dhruva one synonym, the patronymic Auttānapādi. Colebrooke's gloss is 'The pole', and his footnote is explicit that it may mean 'the north pole itself', distinguishing the mythological Dhruva son of Uttānapāda from the astronomical usage in which 'Uttānapāda is Ursa minor' — which is direct support for the caveat already on file that Dhruva may name the pole rather than a star. Separately, the Nānārtha-varga (3.3.792) records a second technical sense: dhruva also denotes a class of asterism (bha-bheda), the dhruva/sthira group used in muhūrta.</sub>

### कुम्भसम्भवः (Kumbhasambhava) — Canopus

**Modern identification:** Canopus — α Carinae, Carina (*certain*)

*See also:* `agastya`, `maitravaruni`

**Amarakośa 1.3.215 (Dig-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> ध्रुव औत्तानपादिः स्यातगस्त्यः कुम्भसम्भवः ॥ १.३.२१५ ॥
>
> — *Colebrooke glosses the group as 'regent of the star Canopus'.*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** 'Jar-born' — synonym of Agastya in the same lexical entry, from the legend of the sage's birth in a water-jar. A name of the sage transferred to the star by the lexicon's own equation of the two. Note that Sūrya Siddhānta 9.16 independently uses kumbhabhava ('pot-born') for the same star.</sub>

### मैत्रावरुणिः (Maitrāvaruṇi) — Canopus

**Modern identification:** Canopus — α Carinae, Carina (*certain*)

*See also:* `agastya`, `kumbhasambhava`

**Amarakośa 1.3.216 (Dig-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> मैत्रावरुणिरस्यैव लोपामुद्रा सधर्मिणी ॥ १.३.२१६ ॥
>
> — *'His consort' [Lopāmudrā] follows; Colebrooke glosses the preceding names as 'regent of the star Canopus'.*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** 'Son of Mitra and Varuṇa' — third synonym of Agastya/Canopus in the lexicon's entry, an old Vedic patronymic of the sage. NOTE: Lopāmudrā, named in the same verse, is EXCLUDED from this database as a star name — Colebrooke glosses her only as 'His consort', and the lexicon does not treat her as a star.</sub>

### मुनि (Muni) — Canopus

**Modern identification:** Canopus — α Carinae, Carina (*certain*)

*See also:* `agastya`, `lopamudravallabha`

**Brāhmasphuṭasiddhānta, Bhagrahayutyadhikāra 13–14 (also 41)** — [Sanskrit e-text](https://archive.org/download/Brahmasphutasiddhanta/Brahmasphutasiddhanta_djvu.txt)

> कृत्वापि दृष्टिकर्म श्रीषेणार्यभटविष्णुचन्द्रोक्तम् । प्रतिदिनमुदयेऽस्ते वा न भवति दृग्गणितयोरैक्यम् ॥१३॥ भमुनिमृगव्याधानां यतस्ततो दृष्टिकर्म वक्ष्यामि । दृग्गणितसमं देयं शिष्याय चिरोषितायेदम् ॥१४॥
>
> — *No public-domain translation exists. Sense: 'Even after performing the visibility-correction stated by Śrīṣeṇa, Āryabhaṭa and Viṣṇucandra, there is daily no agreement between observation and computation, at rising or at setting. Therefore I shall state a visibility-correction for the asterisms, the Sage and the Deer-hunter; this, being in accord with observation, is to be given to a long-tested pupil.'*
> <br>— Paraphrase by the compiler ([source](https://archive.org/download/Brahmasphutasiddhanta/Brahmasphutasiddhanta_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** 'The Sage' used absolutely as a name for Canopus. At Bhagrahayutyadhikāra 13–14 Brahmagupta writes of the dṛkkarma 'of the asterisms, the Sage, and the Deer-hunter' (bha-muni-mṛgavyādhānām), and the commentary glosses the compound word for word as nakṣatra-agastya-lubdhakānām. Bhāskara II inherits the usage — 'bhānāṃ muner mṛgaripor udayāstalagne'. The verses are also notable for naming the predecessors whose dṛkkarma Brahmagupta rejects: Śrīṣeṇa, Āryabhaṭa and Viṣṇucandra.</sub>

### मृगहर्तृ (Mṛgahartṛ) — Sirius

**Modern identification:** Sirius — α Canis Majoris, Canis Major (*certain*)

*See also:* `mrigavyadha`, `lubdhaka`

**Brāhmasphuṭasiddhānta, Bhagrahayutyadhikāra 37** — [Sanskrit e-text](https://archive.org/download/Brahmasphutasiddhanta/Brahmasphutasiddhanta_djvu.txt)

> षड्भयुतमूनमुदयैः षड्राशियुतं तदस्तमयसूर्यः । घटिकाद्वितयेनैवं षड्भागयुतेन मृगहर्तुः ॥ ३७ ॥
>
> — *No public-domain translation exists. Sense: '...that, increased by six signs and diminished by the oblique ascensions, is the sun of his setting; and in the same way, by two ghaṭikās increased by a sixth, for the Deer-snatcher (Sirius).'*
> <br>— Paraphrase by the compiler ([source](https://archive.org/download/Brahmasphutasiddhanta/Brahmasphutasiddhanta_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** 'The deer-snatcher' — a fourth Sanskrit name for Sirius, alongside Mṛgavyādha ('deer-hunter'), Lubdhaka ('hunter') and Bhāskara's Mṛgaripu ('the deer's enemy'). It occurs in the closing pāda of Bhagrahayutyadhikāra 37, and the edition's commentary glosses it in parentheses as (vyādhasya) and quotes the phrase back as Brahmagupta's own wording: 'ghaṭikādvitayenaiva ṣaḍbhāgayutena mṛgahartuḥ' — 'for the Deer-snatcher, by the same two ghaṭikās increased by a sixth' (= 13 kālāṃśas, versus 12 for Agastya).</sub>

### लोपामुद्रावल्लभ (Lopāmudrāvallabha) — Canopus

**Modern identification:** Canopus — α Carinae, Carina (*certain*)

*See also:* `agastya`, `muni`

**Siddhāntaśekhara of Śrīpati, as quoted in the commentary on Brāhmasphuṭasiddhānta, Bhagrahayutyadhikāra 35–37** — [Sanskrit e-text](https://archive.org/download/Brahmasphutasiddhanta/Brahmasphutasiddhanta_djvu.txt)

> नक्षत्रांशः संयुतं राशियुगमं ८७ लोपामुद्रावल्लभस्य ध्रुवः स्यात् । ... विक्षिप्तोऽयं दक्षिणे स्वापमाग्रात् ।
>
> — *No public-domain translation exists. Sense: 'Two signs plus the degrees of a nakshatra (= 87°) would be the dhruva of Lopāmudrā's beloved; ... he is displaced to the south of his own declination-limit by seventy-seven degrees.'*
> <br>— Paraphrase by the compiler ([source](https://archive.org/download/Brahmasphutasiddhanta/Brahmasphutasiddhanta_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** 'The beloved of Lopāmudrā' — Śrīpati's kenning for Agastya/Canopus, Lopāmudrā being the sage's wife. Śrīpati gives the star dhruva 87° and śara 77° S, identical to Brahmagupta's figures; the commentary concludes 'Śrīpati's statement conforms exactly to Brahmagupta's'. Recovered at second hand — these Siddhāntaśekhara verses are quoted inside the modern commentary on the Brāhmasphuṭasiddhānta and their OCR is poor, so the NAME is unambiguous but the verse wording needs checking against a published Siddhāntaśekhara edition.</sub>

### औत्तानपादिः (Auttānapādi) — Pole Star

**Modern identification:** Pole Star — α Ursae Minoris / the celestial pole, Ursa Minor (*certain*)

*See also:* `dhruva`, `uttanapada`

**Amarakośa 1.3.215 (Dig-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> ध्रुव औत्तानपादिः स्यातगस्त्यः कुम्भसम्भवः ॥ १.३.२१५ ॥
>
> — *'The pole.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** Distinct from the Purāṇic Uttānapāda already on file (a position on the Śiśumāra's upper jaw): this is the patronymic 'son of Uttānapāda' used by the lexicon as a full synonym of the pole star itself.</sub>

### शूल (?) (Śūla) — unidentified red star reported south of Canopus

**Modern identification:** unidentified red star reported south of Canopus — —, far southern sky (*disputed*)

**Al-Bīrūnī, India ch. XXII (Sachau 1910, vol. 1, p. 240; note at vol. 2, p. 309)** — [Sanskrit e-text](https://archive.org/download/alberunisindiaac01biru/alberunisindiaac01biru_djvu.txt)

> *No Sanskrit text: al-Bīrūnī wrote in Arabic, and the passage survives here only in Sachau's English.*
>
> — *So Śrīpāla says that the people of Multan see in summer time a red star a little below the meridian of Canopus, which they call Sūla, i.e. the beam of crucifixion, and that the Hindus consider it as unlucky. Therefore, when the moon stands in the station Pūrvabhādrapada, the Hindus do not travel towards the south, because this star stands in the south.*
> <br>— E. Sachau (1910) ([source](https://archive.org/download/alberunisindiaac01biru/alberunisindiaac01biru_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** A star otherwise unrecorded in the Sanskrit tradition, preserved only because al-Bīrūnī heard of it from Śrīpāla, a scholar of Multan contemporary with him. Data: red; seen in summer; a little BELOW the meridian of Canopus; considered unlucky; standing in the south when the moon is in Pūrvabhādrapadā, on which account Hindus avoided southward travel then. Sachau translates the name as 'the beam of crucifixion', pointing to Sanskrit śūla ('stake, impaling-post') — but the Devanagari above is a reconstruction from Sachau's transliteration of an Arabic-script word and is NOT attested in any Sanskrit source; Sachau himself declines to identify the star. The identification is genuinely open: nothing prominent, red and south of Canopus is visible from Multan (30°12'N), so either the report is garbled, or 'below the meridian of Canopus' means something other than 'further south', or the object was transient.</sub>

## The Saptarṣi (Ursa Major) and Arundhatī

Bṛhat Saṃhitā ch. 13 gives the east-to-west order of the seven rishis and places Arundhatī beside Vasiṣṭha; the star-by-star mapping below follows from that order once Vasiṣṭha is anchored to Mizar by Arundhatī = Alcor. Only the Mizar/Alcor pair is fixed by the text itself.

### सप्तर्षयः / ऋक्षाः (Saptarṣayaḥ / Ṛkṣāḥ) — the Big Dipper - seven bright stars of Ursa Major (Dubhe, Merak, Phecda, Megrez, Alioth, Mizar, Alkaid)

**Modern identification:** the Big Dipper - seven bright stars of Ursa Major (Dubhe, Merak, Phecda, Megrez, Alioth, Mizar, Alkaid) — α, β, γ, δ, ε, ζ, η Ursae Majoris, Ursa Major (*certain*)

*See also:* `marichi`, `vasishtha`, `angiras`, `atri`, `pulastya`, `pulaha`, `kratu`, `arundhati`, `rksha`

**Śatapatha Brāhmaṇa 2.1.2.4** — [Sanskrit e-text](https://sa.wikisource.org/wiki/शतपथब्राह्मणम्/काण्डम्_२/अध्यायः_१/ब्राह्मण_२)

> अथ यस्मान्न कृत्तिकास्वादधीत । ऋक्षाणां ह वा एता अग्रे पत्न्य आसुः सप्तर्षीनु ह स्म वै पुरर्क्षा इत्याचक्षते ता मिथुनेन व्यार्ध्यन्तामी ह्युत्तरा हि सप्तर्षय उद्यन्ति पुर एता अशमिव वै तद्यो मिथुनेन व्यृद्धः स नेन्मिथुनेन व्यृध्या इति तस्मान्न कृत्तिकास्वादधीत - २.१.२.४
>
> — *On the other hand (it is argued) why he should not set up the fires under the Krittikas. Originally, namely, the latter were the wives of the Bears (riksha); for the seven Rishis were in former times called the Rikshas (bears). They were, however, precluded from intercourse (with their husbands), for the latter, the seven Rishis, rise in the north, and they (the Krittikas) in the east. Now it is a misfortune for one to be precluded from intercourse (with his wife): he should therefore not set up his fires under the Krittikas, lest he should thereby be precluded from intercourse.*
> <br>— Julius Eggeling, SBE vol. 12 (1882), pp. 282-283 ([source](https://www.sacred-texts.com/hin/sbr/sbe12/sbe1241.htm) · [mirror](https://web.archive.org/web/20210506123309/https://www.sacred-texts.com/hin/sbr/sbe12/sbe1241.htm))

<sub>**Identification notes (Vedic corpus):** The ŚB states that the Seven Rishis 'were in former times called the Rkshas (bears)' - preserving the older name ṛkṣāḥ 'bears' (cf. RV 1.24.10) that matches the Greco-Roman Bear, and notes they rise in the north while the Krittikas rise in the east - exactly true of the circumpolar Dipper vs. the equatorial Pleiades. Also shown to the bride in ĀGS 1.7.22.</sub>

**Viṣṇu Purāṇa 4.24.105-106 (vulgate; = 4.24.25-26 in Pathak's critical ed.); Bhāgavata Purāṇa 12.2.27-28; Matsya Purāṇa 273.39-43; Vāyu Purāṇa uttarārdha 37.413-417; Brahmāṇḍa Purāṇa 2,74.230-235** — [Sanskrit e-text](https://sa.wikisource.org/wiki/विष्णुपुराणम्/चतुर्थांशः/अध्यायः_२४)

> सप्तर्षीणां तु यौ पूर्वौ दृश्येते ह्युदितौ दिवि ।
> तयोस्तु मध्ये नक्षत्रं दृश्यते यत्समं निशि १०५ ।
> तेन सप्तर्षयो युक्तास्तिष्ठंत्यब्दशतं नृणाम् ।
> ते तु पारीक्षिते काले मघास्वासन्द्विजोत्तम १०६ ।
>
> — *When the two first stars of the seven Rishis (the great Bear) rise in the heavens, and some lunar asterism is seen at night at an equal distance between them, then the seven Rishis continue stationary in that conjunction for a hundred years of men. At the birth of Paríkshit they were in Maghá...*
> <br>— H.H. Wilson (1840; public domain), Viṣṇu Purāṇa Book IV ch. XXIV, pp. 484-486 ([source](https://www.sacred-texts.com/hin/vp/vp117.htm))

<sub>**Identification notes (Purāṇas):** New attestation carrying a distinct astronomical doctrine: the SAPTARṢI CYCLE, in which the seven sages occupy each nakṣatra for 100 human years, completing 27 × 100 = 2700 years. The method is observational and stated: take the two leading ṛṣis visible in the north, and the asterism seen midway between them on the meridian is the one they 'occupy'. Attested in four recensions. Śrīdhara Svāmī's commentary maps the sages onto Ursa Major and notes that the two that rise first are Pulaha and Kratu — i.e. the Pointers, Merak and Dubhe. Whether the cycle tracks any real motion is disputed; the 1916 Matsya editor calls it 'a contrivance of historians', and the sages' proper motion is far too small to produce it.</sub>

**Matsya Purāṇa 273.39-43 (Wikisource numbering; = 40-44 in Taluqdar/Pargiter)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/मत्स्यपुराणम्/अध्यायः_२७३)

> सप्तर्षयस्तु वर्त्तन्ते यत्र नक्षत्रमण्डले।
> सप्तर्षयस्तु तिष्ठन्ति पर्य्यायेण शतं शतम्।।  २७३.३९
> सप्तर्षीणाञ्च यौ पूर्वौ दृश्येते ह्युदितौ निशि ।।  २७३.४१
> तयोर्मध्ये तु नक्षत्रं दृश्यते यत्समं दिवि।
> तेन सप्तर्षयो ज्ञेया युक्ता व्योम्नि शतं समाः ।।  २७३.४२
> नक्षत्राणामृषीणाञ्च योगस्यैतन्निदर्शनम्।
> सप्तर्षयो मघायुक्ताः काले पारिक्षिते शतम् ।।  २७३.४३
>
> — *"In the circle of the lunar constellations, wherein the Great Bear revolves, and which contains 27 constellations in its circumstance, the Great Bear remains 100 years in (conjoined with) each in turn." ... The two front stars of the Great Bear, which are seen when risen at night, the lunar constellation which is seen situated equally between them in the sky, the Great Bear is to be known as conjoined with that constellation 100 years in the sky. ... This is the exposition of the conjunction of the lunar constellations and the Great Bear. The Great Bear was conjoined with the Maghâs in Parikṣit's time 100 years.*
> <br>— 'A Taluqdar of Oudh', The Matsya Puranam Part II (Sacred Books of the Hindus, Allahabad, 1917), p. 344, rendering Pargiter's emended text; public domain. Transcribed from the page images, the archive.org OCR of these pages being badly garbled. ([source](https://archive.org/details/in.ernet.dli.2015.283501))

<sub>**Identification notes (Purāṇas):** The Matsya recension of the Saptarṣi cycle, independently verified. Its text is corrupt at 273.38-39 (the vulgate repeats सप्तर्षयस्तु where the Brahmāṇḍa/Vāyu have सप्तविंशतिपर्यन्ते कृत्स्ने नक्षत्रमण्डले); both Wilson (1840) and the 1917 Taluqdar edition flag this, and Pargiter emended the passage. NOTE the verse-number offset: the Taluqdar/Pargiter numbering runs one higher than the Wikisource text (Taluqdar 44 = Wikisource 273.43). Wilson's note 81 records the manuscript spread for the Parīkṣit-to-Nanda interval: 1015 years in all his Viṣṇu copies, 1050 in three Vāyu copies and five Matsya copies, 1500 in one Matsya copy — and the Viṣṇu critical edition indeed reads pañcadaśottaram (1015) where the vulgate has pañcāśaduttaram (1050).</sub>

**Amarakośa 1.3.229 (Dig-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> सप्तर्षयो मरीच्यत्रिमुखाश्चित्रशिखण्डिनः ॥ १.३.२२९ ॥
>
> — *'Ursa major.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** Lexicon attestation adding Colebrooke's explicit roll-call of the seven stars as the seven sages, and the alternative collective Citraśikhaṇḍinaḥ. Note Amarakośa's ordering 'headed by Marīci and Atri' (marīcy-atri-mukhāḥ).</sub>

**Sūrya Siddhānta 13.8–9; cf. al-Bīrūnī, India ch. XLV** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_ज्यौतिषोपनिषदध्यायः)

> याम्योदग्गोलसम्स्थानाम् भानाम् अभिजितस् तथा // सप्तर्षीणाम् अगस्त्यस्य ब्रह्मादीनाम् च कल्पयेत् /
>
> — *8. ... Those likewise of the asterisms (bha) situated in the southern and northern hemispheres, of Abhijit, 9. Of the Seven Sages (saptarshayas), of Agastya, of Brahma etc., are to be fixed ....*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** SS 13.8–9 (the armillary-sphere chapter) directs that day-circles be fixed for the asterisms of both hemispheres, for Abhijit, for the Seven Sages, for Agastya, and for 'Brahmā etc.' — confirming that the treatise treats the Saptarṣayaḥ as observable stars with definite declinations, not merely as myth. Burgess computes this would burden the instrument with forty-two extra circles and remarks that 'such impracticable directions... cannot but inspire the suspicion that the instrument may never have been constructed except upon paper.' Al-Bīrūnī separately gives Ptolemaic Ursa Major catalogue numbers for the seven rishis (Marīci 27th, Vasiṣṭha 26th, Aṅgiras 25th, Atri 18th, Kratu 16th, Pulaha 17th, Pulastya 19th), broadly consistent with the east-to-west mapping on file, and demolishes the Saptarṣi-cycle chronology: 'The words of Garga are without any foundation.'</sub>

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

**Al-Bīrūnī, India ch. XLV, 'On the constellation of the Great Bear' (Sachau 1910, vol. 1, pp. 389–391)** — [Sanskrit e-text](https://archive.org/download/alberunisindiaac01biru/alberunisindiaac01biru_djvu.txt)

> *No Sanskrit text: al-Bīrūnī wrote in Arabic, and the passage survives here only in Sachau's English.*
>
> — *The Great Bear is in the Indian language called Saptarshayas, i.e. the Seven Rishis. They are said to have been anchorites who nourished themselves only with what it is allowable to eat, and with them there was a pious woman, Al-suhā (Ursa Major, star 80 by Ptolemy). ... Marici is the 27th star of this constellation. Vasishtha, 26th; Angiras, 25th; Atri, 18th; Kratu, 16th; Pulaha, 17th; Pulastya, 19th.*
> <br>— E. Sachau (1910) ([source](https://archive.org/download/alberunisindiaac01biru/alberunisindiaac01biru_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** A DECISIVE INDEPENDENT CROSS-CHECK. Al-Bīrūnī equates Arundhatī with al-Suhā and pins it by Ptolemaic catalogue number: 'a pious woman, Al-suhā (Ursa Major, star 80 by [Ptolemy])'. Al-Suhā is the standard Arabic name for Alcor and 80 UMa is Alcor's designation — so an eleventh-century Central Asian observer independently arrives at the identification on file, without recourse to the Indian coordinate tradition.</sub>

## Vedic asterisms and archaic names

Older names from the Saṃhitā/Brāhmaṇa layer: the individually named Kṛttikās, the celestial Orion tableau of Aitareya Brāhmaṇa 3.33, and the archaic names that the Ṛgveda, Atharvaveda, Maitrāyaṇī/Kāṭhaka Saṃhitās and Vedāṅga Jyotiṣa use where later lists have the familiar ones — Aghā for Maghā, Arjunī for the Phalgunīs, Niṣṭya for Svāti, Sārpa for Āśleṣā, Jyeṣṭhaghnī for Jyeṣṭhā. Vicṛtau is the earliest Indian passage to name individual stars *as stars* (tārake, 'the two stars').

### ऋक्षाः (Ṛkṣāḥ) — Ursa Major (the Seven Ṛṣis / Big Dipper)

**Modern identification:** Ursa Major (the Seven Ṛṣis / Big Dipper) — α–η Ursae Majoris, Ursa Major (*disputed*)

*See also:* `saptarshi`

**Ṛgveda 1.24.10** — [Sanskrit e-text](https://sa.wikisource.org/wiki/ऋग्वेदः_सूक्तं_१.२४)

> अमी य ऋक्षा निहितास उच्चा नक्तं ददृश्रे कुह चिद्दिवेयुः ।
> अदब्धानि वरुणस्य व्रतानि विचाकशच्चन्द्रमा नक्तमेति ॥१०॥
>
> — *Whither by day depart the constellations that shine at night, set high in heaven above us? Varuna's holy laws remain unweakened, and through the night the Moon moves on in splendor*
> <br>— R.T.H. Griffith (1896) ([source](https://en.wikisource.org/wiki/The_Hymns_of_the_Rigveda/Book_1/Hymn_24))

<sub>**Identification notes (Ṛgveda & Vedāṅga Jyotiṣa):** The oldest Indian reference to Ursa Major, and the only plural ṛkṣāḥ in the Ṛgveda (verified by exhaustive search of the Aufrecht text). Griffith renders it generically as 'constellations' and does NOT translate 'Bears' — the identification rests on etymology (ṛkṣa cognate with Greek ἄρκτος, Latin ursa) and on Macdonell & Keith, Vedic Index (1912) i.114: 'Rksa, "bear," is found only once in the Rigveda... Not more frequent is the use of the word in the plural to denote the "seven bears," later called the "seven Rsis," the constellation of the "Great Bear"', citing precisely RV 1.24.10, Śatapatha Brāhmaṇa 2.1.2.4, and Taittirīya Āraṇyaka 1.11.2.</sub>

**Taittirīya Āraṇyaka 1.11.2** — [Sanskrit e-text](https://sa.wikisource.org/wiki/तैत्तिरीयारण्यकम्(विस्वर)

> ऋषयः सप्तात्रिश्च यत् । सर्वेऽत्रयो अगस्त्यश्च । नक्षत्रैः शंकृतोऽवसन्, इति । अथ सवितुः श्यावाश्वस्यावर्तिकामस्य, इति । अमी य ऋक्षा निहितास उच्चा । नक्तं ददृश्रे कुहचिद्दिवेयुः । अदब्धानि वरुणस्य व्रतानि । विचाकशच्चन्द्रमा नक्षत्रमेति, इति ।
>
> — *The seven Ṛṣis and Atri; all the Atris and Agastya; they dwelt blessed among the asterisms. — Then, of Savitṛ, of Śyāvāśva who desires... — Those Bears that are set on high, seen at night: whither by day have they gone? Unimpaired are Varuṇa's ordinances; surveying all, the moon goes to the asterism.*
> <br>— No public-domain English translation of the Taittirīya Āraṇyaka located; literal rendering supplied by the compiler ([source](https://sa.wikisource.org/wiki/तैत्तिरीयारण्यकम्(विस्वर))

<sub>**Identification notes (Ṛgveda & Vedāṅga Jyotiṣa):** This is the passage that makes the Bear identification defensible. TĀ 1.11 names the Seven Ṛṣis, Atri and Agastya as dwelling 'with/among the nakṣatras' and then, in the very next breath, quotes the Ṛgvedic ṛkṣāḥ verse. It also transmits a significant variant: where RV 1.24.10 ends नक्तमेति ('goes by night'), the Āraṇyaka reads नक्षत्रमेति ('goes to the asterism'). Macdonell & Keith cite exactly this passage under their 'Rksa = Great Bear' entry.</sub>

**Nirukta 3.20; Amarakośa 1.3.217 (Dig-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/निरुक्तशास्त्रम्/तृतीयोध्यायः)

> ऋक्षा उदीर्णानीव ख्यायन्ते । स्तृभिस्तीर्णानीव ख्यायन्ते । अमी य ऋक्षा निहितास उच्चा । पश्यन्तो द्यामिव स्तृभिः । इत्यपि निगमौ भवतः ।
>
> — *'Rkṣāh (stars) appear to be raised up. Strbhih (stars) appear to be scattered (in the sky). "These stars which are placed on high." "Looking at the sky with stars, as it were." These are two Vedic quotations.'*
> <br>— Lakshman Sarup (1921) ([source](https://archive.org/download/nighantuniruktao00yaskuoft/nighantuniruktao00yaskuoft_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** DECISIVE FOR THE BEAR CONTROVERSY, and against it. Yāska explains ṛkṣāḥ NOT from ṛkṣa 'bear' but as 'they appear as if raised up' (udīrṇāni iva khyāyante), and quotes exactly the verse RV 1.24.10 already on file. So the oldest Indian etymologist reads ṛkṣa as a general word for star, derived from height, and knows nothing of the Bear — a point directly against the Indo-European ṛkṣa/ἄρκτος/ursa equation. The Amarakośa confirms the flattening: by the 6th century ṛkṣa is a plain neuter synonym of nakṣatra, 'a star'.</sub>

### अम्बा, दुला, नितत्नी, अभ्रयन्ती, मेघयन्ती, वर्षयन्ती, चुपुणीका (Ambā, Dulā, Nitatnī, Abhrayantī, Meghayantī, Varṣayantī, Cupuṇīkā) — the seven individual stars of the Pleiades

**Modern identification:** the seven individual stars of the Pleiades — brightest members: η, 27, 17, 20, 23, 19, 28 Tauri (no secure one-to-one mapping), Taurus (*likely*)

*See also:* `krittika`

**Taittirīya Brāhmaṇa 3.1.4.1** — [Sanskrit e-text](https://sa.wikisource.org/wiki/तैत्तिरीयब्राह्मणम्_(विस्वरपाठः)

> अग्निर्वा अकामयत । अन्नादो देवानाꣳ स्यामिति । स एतमग्नये कृत्तिकाभ्यः पुरोडाशमष्टाकपालं निरवपत् । ततो वै सोऽन्नादो देवानामभवत् । अग्निर्वै देवानामन्नादः । यथा ह वा अग्निर्देवनामन्नादः । एवꣳ ह वा एष मनुष्याणां भवति । य एतेन हविषा यजते । य उ चैनदेवं वेद । सोऽत्र जुहोति । अग्नये स्वाहा कृत्तिकाभ्यः स्वाहा । अम्बायै स्वाहा दुलायै स्वाहा । नितत्न्यै स्वाहाभ्रयन्त्यै स्वाहा । मेघयन्त्यै स्वाहा वर्षयन्त्यै स्वाहा । चुपुणीकायै स्वाहेति १
>
> — *[Paraphrase] Agni desired: 'May I be the eater of food of the gods.' He offered an eight-potsherd cake to Agni of the Krittikas, and thereby became the food-eater of the gods... He makes offering with: 'To Agni svaha! To the Krittikas svaha! To Amba svaha! To Dula svaha! To Nitatni svaha! To Abhrayanti svaha! To Meghayanti svaha! To Varshayanti svaha! To Cupunika svaha!' No public-domain English translation of the Taittiriya Brahmana exists; rendering above is the researcher's own paraphrase of the Sanskrit. Cf. P.-E. Dumont, 'The Ishtis to the Nakshatras (or Oblations to the Lunar Mansions) of the Taittiriya-Brahmana', Proceedings of the American Philosophical Society 98.3 (1954), pp. 204-223 (copyrighted, not quoted).*
> <br>— Researcher's paraphrase (no public-domain translation); cf. P.-E. Dumont (1954) ([source](https://www.jstor.org/stable/i344439))

<sub>**Identification notes (Vedic corpus):** The Taittirīya Brāhmaṇa names seven individual Kṛttikās in the svāhā-calls of the Agni-Kṛttikā offering; several names are rain/cloud words (Abhrayantī 'bringing clouds', Meghayantī 'making clouds', Varṣayantī 'raining'). The group = Pleiades is certain; which Vedic name maps to which star cannot be determined.</sub>

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

### विचृतौ (Vicṛtau) — Shaula and Lesath (the Scorpion's sting)

**Modern identification:** Shaula and Lesath (the Scorpion's sting) — λ & υ Scorpii, Scorpius (*certain*)

*See also:* `mula`, `mulabarhana`

**Atharvaveda (Śaunaka) 2.8.1** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अथर्ववेदः/काण्डं_२/सूक्तम्_०८)

> उदगातां भगवती विचृतौ नाम तारके ।
> वि क्षेत्रियस्य मुञ्चतामधमं पाशमुत्तमम् ॥१॥
>
> — *Arisen are the (two) blessed stars called the Unfasteners (vicṛ́t); let them unfasten (vi-muc) of the kṣetriyá the lowest, the highest fetter.*
> <br>— W.D. Whitney, rev. C.R. Lanman (1905) ([source](https://en.wikisource.org/wiki/Atharva-Veda_Samhita/Book_II/Hymn_8))

<sub>**Identification notes (Ṛgveda & Vedāṅga Jyotiṣa):** 'The two Unfasteners.' The single most important find in this cluster: unlike the nakshatra lists, which name asterisms, the Atharvaveda here calls Vicṛtau explicitly तारके — 'the two stars' — the earliest Indian passage to name individual stars as stars. It occurs in four separate AV hymns (2.8.1, 3.7.4, 6.110.2, 6.121.3); in AV 3.7 and 6.121 the Wikisource sūkta headers give the deity of the verse as तारके. Macdonell & Keith, Vedic Index (1912) ii.295: 'Vicṛtau, "the two releasers"; Mula, "root"; or Mulabarhani, "uprooting," denote primarily λ and υ at the extremity of the tail of the Scorpion.' Sāyaṇa's bhāṣya on this verse glosses एतन्नाम्न्यौ तारके मूलनक्षत्रम्. Note that Vicṛtau also stands in the Mūla slot of the Taittirīya Saṃhitā 4.4.10 list itself.</sub>

**Atharvaveda (Śaunaka) 3.7.4** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अथर्ववेदः/काण्डं_३/सूक्तम्_०७)

> अमू ये दिवि सुभगे विचृतौ नाम तारके ।
> वि क्षेत्रियस्य मुञ्चतामधमं पाशमुत्तमम् ॥४॥
>
> — *The two blessed stars named Unfasteners (vicṛ́t), that are yonder in the sky—let them unfasten of the kṣetriyá the lowest, the highest fetter.*
> <br>— W.D. Whitney, rev. C.R. Lanman (1905) ([source](https://en.wikisource.org/wiki/Atharva-Veda_Samhita/Book_III/Hymn_7))

<sub>**Identification notes (Ṛgveda & Vedāṅga Jyotiṣa):** The Sanskrit Wikisource sūkta header for AV 3.7 assigns the deity of verse 4 literally as तारके ('the two stars') — 'दे. १-३ हरिणः, ४ तारके, ५ आपः'. Whitney's note on the passage discusses the identification with the Scorpion's sting.</sub>

**Taittirīya Āraṇyaka 2.6** — [Sanskrit e-text](https://sa.wikisource.org/wiki/तैत्तिरीयारण्यकम्(विस्वर)

> अमी ये सुभगे दिवि विचृतौ नाम तारके । प्रेहामृतस्य यच्छतामेतद्बद्धकमोचनम, इति ।
>
> — *Those two blessed stars in the sky named the Unfasteners — may they come forth and grant immortality; this is the loosing of the bound one.*
> <br>— No public-domain English translation of the Taittirīya Āraṇyaka located; literal rendering supplied by the compiler (cf. Whitney's rendering of the near-identical AV 6.121.3) ([source](https://sa.wikisource.org/wiki/तैत्तिरीयारण्यकम्(विस्वर))

<sub>**Identification notes (Ṛgveda & Vedāṅga Jyotiṣa):** The āraṇyaka attestation, in the Yajurvedic tradition rather than the Atharvavedic. Sāyaṇa quotes this exact verse (as तैआ २,६,१) in his commentary on AV 2.8.1 to prove that vicṛt is a synonym of the Mūla nakshatra. The same verse also stands at AV 6.121.3, and in the Paippalāda Saṃhitā kāṇḍas 1, 3 and 16.</sub>

## Other names for the nakshatras

Every one of these is a real attested name for an asterism that also appears above under its familiar title — archaic Vedic forms (Aghā, Arjunī, Niṣṭya, Jyeṣṭhaghnī), lexicon variants (Aśvayuj, Rādhā, Śraviṣṭhā, Proṣṭhapadā, Āgrahāyaṇī, Ilvalāḥ), and the siddhāntic habit of naming a nakshatra by its presiding deity (Vaiṣṇava for Śravaṇa, Vāsava for Dhaniṣṭhā, Raudrarkṣa for Ārdrā). They are kept as separate entries so it stays visible which text calls it what. **Two are traps:** Brahmagupta's Prājeśa means Rohiṇī and his Āgneya means Kṛttikā — not the distinct fixed stars Prajāpati (δ Aurigae) and Agni (β Tauri) listed further down.

### अघा (Aghā) — Regulus

**Modern identification:** Regulus — α Leonis, Leo (*likely*)

*See also:* `magha`

**Ṛgveda 10.85.13** — [Sanskrit e-text](https://sa.wikisource.org/wiki/ऋग्वेदः_सूक्तं_१०.८५)

> सूर्याया वहतुः प्रागात्सविता यमवासृजत्।
> अघासु हन्यन्ते गावोऽर्जुन्योः पर्युह्यते ॥१३॥
>
> — *The bridal pomp of Surya, which Savitar started, moved along. In Magha days are oxen slain, in Arjuris they wed the bride.*
> <br>— R.T.H. Griffith (1896) ([source](https://en.wikisource.org/wiki/The_Hymns_of_the_Rigveda/Book_10/Hymn_85))

<sub>**Identification notes (Ṛgveda & Vedāṅga Jyotiṣa):** The archaic Ṛgvedic form of Maghā, occurring exactly once in the Ṛgveda. Griffith silently normalises it to 'Magha'. Macdonell & Keith, Vedic Index (1912) i.10: 'In the wedding hymn of the Rigveda it is said that cows are slain in the Aghas, and the wedding takes place at the Arjunis (dual). The Atharvaveda has the ordinary Maghas instead. It is impossible to resist the conclusion that the reading of the Rigveda was deliberately altered because of the connection of the slaughter of kine with sin (agha).' The parallel Atharvaveda recension of the same hymn (AV 14.1.13) reads Maghā.</sub>

### अर्जुन्यौ (Arjunyau (Arjunī)) — the two Phalgunīs — Zosma/Chertan group and Denebola

**Modern identification:** the two Phalgunīs — Zosma/Chertan group and Denebola — δ & θ Leonis; β Leonis, Leo (*likely*)

*See also:* `purva-phalguni`, `uttara-phalguni`

**Ṛgveda 10.85.13** — [Sanskrit e-text](https://sa.wikisource.org/wiki/ऋग्वेदः_सूक्तं_१०.८५)

> सूर्याया वहतुः प्रागात्सविता यमवासृजत्।
> अघासु हन्यन्ते गावोऽर्जुन्योः पर्युह्यते ॥१३॥
>
> — *The bridal pomp of Surya, which Savitar started, moved along. In Magha days are oxen slain, in Arjuris they wed the bride.*
> <br>— R.T.H. Griffith (1896) ([source](https://en.wikisource.org/wiki/The_Hymns_of_the_Rigveda/Book_10/Hymn_85))

<sub>**Identification notes (Ṛgveda & Vedāṅga Jyotiṣa):** The archaic Ṛgvedic dual for the two Phalgunīs. The dual arjunyoḥ occurs only here in the Ṛgveda (other forms of arjuna in the RV are the ordinary adjective 'bright/white'). Macdonell & Keith, Vedic Index (1912) i.36: 'Arjuni is, in the Rigveda, the name of the Naksatra ("lunar mansion"), elsewhere called Phalguni. It occurs in the marriage hymn, with Agha for Magha, and, like that word, is apparently a deliberate modification.' AV 14.1.13 has the normalised Phalgunī.</sub>

### निष्ट्यम् / निस्त्या (Niṣṭya / Nistyā) — Arcturus

**Modern identification:** Arcturus — α Boötis, Boötes (*likely*)

*See also:* `svati`

**Maitrāyaṇī Saṃhitā 2.13.20 (also Kāṭhaka Saṃhitā 39.13)** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/1_veda/1_sam/maitrs_pu.htm)

> *(IAST — the e-text carries no Devanagari copy)*
>
> ... hasto nakṣatraṃ savitā devatā citrā nakṣatraṃ tvaṣṭā devatā niṣṭyaṃ nakṣatraṃ vāyur devatā viśākhaṃ nakṣatram indrāgnī devatānūrādhā nakṣatraṃ mitro devatā jyeṣṭhā nakṣatraṃ varuṇo devatā mūlaṃ nakṣatraṃ nirṛtir devatā ... //MS_2,13.20//
>
> — *Niṣṭya is the asterism, Vāyu the deity.*
> <br>— No public-domain English translation of the Maitrāyaṇī Saṃhitā located; literal rendering supplied by the compiler (name forms corroborated by Macdonell & Keith, Vedic Index, 1912, i.413) ([source](https://archive.org/stream/vedicindexofname01macduoft/vedicindexofname01macduoft_djvu.txt))

<sub>**Identification notes (Ṛgveda & Vedāṅga Jyotiṣa):** The Maitrāyaṇī and Kāṭhaka name for the asterism the Taittirīya Saṃhitā calls Svāti — the most substantive divergence between the Yajurveda nakshatra lists. Note the neuter gender (निष्ट्यं नक्षत्रं) and the deity Vāyu, matching TS's Svāti. Macdonell & Keith, Vedic Index (1912) i.417: 'Svati or Nistya is later clearly the brilliant star Arcturus or α Bootis, its place in the north being assured by the notice in the Santikalpa'; their comparative table gives slot 13 as 'Svati | Nistya (neut.) | Nistya' for TS | MS | KS. The same form Nistyā stands in the Taittirīya Brāhmaṇa 1.5.1 list. SCRIPT NOTE: the GRETIL Maitrāyaṇī e-text is romanised IAST, not Devanagari; the Devanagari headword is supplied by the compiler and is NOT copied from an e-text.</sub>

### सार्प (Sārpa) — Āśleṣā (head of Hydra)

**Modern identification:** Āśleṣā (head of Hydra) — ε Hydrae (with δ, η, ρ, σ Hydrae), Hydra (*likely*)

*See also:* `ashlesha`

**Vedāṅga Jyotiṣa, Ārca-jyotiṣa 6 (= Yājuṣa-jyotiṣa 7)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/ऋग्वेदाङ्गज्योतिषं_सुधाकरभाष्यसहितम्)

> प्रपद्येते श्रविष्ठादौ सूर्याचन्द्रमसावुदक्।
> सार्पार्धे दक्षिणाऽर्कस्य माघश्रावणयोः सदा॥६॥
>
> — *The sun and moon turn towards the north at the beginning of 'Sravish'ṭhā: but the sun turns towards the south in the middle of the constellation over which the serpents preside; and this [his turn towards the south, and towards the north], always [happens] in [the months of] Mág'ha and 'Srávaṇa.*
> <br>— H.T. Colebrooke (1805; repr. Essays on the Religion and Philosophy of the Hindus, 1858, p. 66) ([source](https://archive.org/details/essaysonreligion00coleiala))

<sub>**Identification notes (Ṛgveda & Vedāṅga Jyotiṣa):** The Vedāṅga Jyotiṣa never uses the name Āśleṣā. It marks the summer solstice as falling in 'the middle of Sārpa' — the asterism of the Serpents — identifying the nakshatra only by its presiding deity. The equation Sārpa = Āśleṣā comes from the text's own deity list (Ārca 25 / Yājuṣa 32, where Sarpāḥ presides over the 7th asterism) and is made explicit by Colebrooke. This verse, paired with Śraviṣṭhā for the winter solstice, is the basis for dating the text's astronomical epoch to roughly the 14th–12th century BCE.</sub>

**Sūrya Siddhānta 9.14** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_उदयास्ताधिकारः)

> कृत्तिकामैत्रमूलानि सार्पम् रौद्रर्क्षम् एव च / दृश्यन्ते पञ्चदशभिर् आषाढाद् द्वितयम् तथा //
>
> — *14. Krttikā, Anurādhā (māitra), and Mūla, and likewise Açleshā and Ārdrā (rāudrarksha), are seen at fifteen degrees; so, too, the pair of Āshādhās.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** Already on file from the Vedāṅga Jyotiṣa; this is a siddhāntic re-attestation, used in place of Āśleṣā at SS 9.14 (the nakshatra's divinities being the Sarpas). Al-Bīrūnī could not identify this asterism: his table notes 'Unknown, Most likely identical with two stars of Cancer and four stars outside of it' — independent evidence that the disputed status recorded here is not a modern artefact.</sub>

### ज्येष्ठघ्नी (Jyeṣṭhaghnī) — Antares (Cor Scorpionis)

**Modern identification:** Antares (Cor Scorpionis) — α Scorpii, Scorpius (*certain*)

*See also:* `jyeshtha`

**Atharvaveda (Śaunaka) 6.110.2** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अथर्ववेदः/काण्डं_६/सूक्तम्_११०)

> ज्येष्ठघ्न्यां जातो विचृतोर्यमस्य मूलबर्हणात्परि पाह्येनम् ।
> अत्येनं नेषद्दुरितानि विश्वा दीर्घायुत्वाय शतशारदाय ॥२॥
>
> — *Born in jyeṣṭhaghnī́, in Yama's two Unfasteners (vicṛ́t)—do thou protect him from the Uprooter (mūlabárhaṇa); may he conduct him across all difficulties unto long life, of a hundred autumns.*
> <br>— W.D. Whitney, rev. C.R. Lanman (1905) ([source](https://en.wikisource.org/wiki/Atharva-Veda_Samhita/Book_VI/Hymn_110))

<sub>**Identification notes (Ṛgveda & Vedāṅga Jyotiṣa):** 'She that slays the eldest' — the archaic, ill-omened name of Jyeṣṭhā, occurring exactly once in the Atharvaveda. AV 6.110 is a birth-star charm: a rite for a child born under a malevolent asterism. Whitney's note: 'Antares or Cor Scorpionis (either alone or with σ, τ) is usually called jyeṣṭhā "oldest," but also (more anciently?), as an asterism of ill omen, jyeṣṭhaghnī "she that slays the oldest"'. Note the hymn does NOT mention Tiṣya, contrary to a common secondary-literature claim — the three asterisms named are all in Scorpius.</sub>

### मूलबर्हण (Mūlabarhaṇa (fem. Mūlabarhaṇī)) — the Scorpion's tail (Mūla)

**Modern identification:** the Scorpion's tail (Mūla) — λ, υ and the chain ε–υ Scorpii, Scorpius (*likely*)

*See also:* `mula`, `vichritau`

**Atharvaveda (Śaunaka) 6.110.2** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अथर्ववेदः/काण्डं_६/सूक्तम्_११०)

> ज्येष्ठघ्न्यां जातो विचृतोर्यमस्य मूलबर्हणात्परि पाह्येनम् ।
> अत्येनं नेषद्दुरितानि विश्वा दीर्घायुत्वाय शतशारदाय ॥२॥
>
> — *Born in jyeṣṭhaghnī́, in Yama's two Unfasteners (vicṛ́t)—do thou protect him from the Uprooter (mūlabárhaṇa); may he conduct him across all difficulties unto long life, of a hundred autumns.*
> <br>— W.D. Whitney, rev. C.R. Lanman (1905) ([source](https://en.wikisource.org/wiki/Atharva-Veda_Samhita/Book_VI/Hymn_110))

<sub>**Identification notes (Ṛgveda & Vedāṅga Jyotiṣa):** 'The Uprooter' / 'root-wrencher' — an archaic name for Mūla, distinguished from Vicṛtau in the same verse: Macdonell & Keith, Vedic Index (1912) i.416 treat 'Vicṛtau', 'Mula' and 'Mulabarhani' as three names for the same region, with Vicṛtau denoting the two sting-stars specifically and Mūla/Mūlabarhaṇī the tail as a whole. The name also occurs at AV 6.112.1 and AV 12.5.33, and stands in the Mūla slot of the Taittirīya Brāhmaṇa 1.5.1 nakshatra list.</sub>

### इन्वकाः (इन्वगाः) (Invakāḥ (Invagāḥ)) — alternative Taittirīya name of Mṛgaśīrṣa - the stars of Orion's head

**Modern identification:** alternative Taittirīya name of Mṛgaśīrṣa - the stars of Orion's head — λ, φ1, φ2 Orionis, Orion (*likely*)

*See also:* `mrigashirsha`

**Taittirīya Brāhmaṇa 1.5.1.1; 3.1.4.3** — [Sanskrit e-text](https://sa.wikisource.org/wiki/तैत्तिरीयब्राह्मणम्_(विस्वरपाठः) · [mirror](https://sa.wikisource.org/wiki/तैत्तिरीयब्राह्मणम्_(विस्वरपाठः)

> अग्नेः कृत्तिकाः । शुक्रं परस्ताज्ज्योतिरवस्तात् । प्रजापते रोहिणी ।आपः परस्तादोषधयोऽवस्तात् । सोमस्येन्वका । विततानि परस्ताद्वयन्तोऽवस्तात् । रुद्रस्य बाहू ।मृगयवः परस्ताद्विक्षारोऽवस्तात् । अदित्यै पुनर्वसू ।वातः परस्तादार्द्रमवस्तात् १ || सोमो वा अकामयत । ओषधीनाꣳ राज्यमभिजयेयमिति । स एतꣳ सोमाय मृगशीर्षाय श्यामाकं चरुं पयसि निरवपत् । ततो वै स ओषधीनाꣳ राज्यमभ्यजयत् । समानानाꣳ ह वै राज्यमभिजयति । य एतेन हविषा यजते । य उ चैनदेवं वेद । सोऽत्र जुहोति । सोमाय स्वाहा मृगशीर्षाय स्वाहा । इन्वकाभ्यः स्वाहौषधीभ्यः स्वाहा । राज्याय स्वाहाभिजित्यै स्वाहेति ३
>
> — *[Paraphrase of TB 1.5.1.1] The Krittikas are Agni's; brightness above, light below. Rohini is Prajapati's; the waters above, the plants below. The Invakas are Soma's; things spread out above, the weavers below. The Bahu (the two Arms) are Rudra's; hunters above, ... below. The two Punarvasus are Aditi's; wind above, moisture below. [TB 3.1.4.3] Soma desired: 'May I win the kingship of the plants'; he offered a caru of millet in milk to Soma of Mrgasirsha... 'To Soma svaha! To Mrgasirsha svaha! To the Invakas svaha! To the plants svaha!' No public-domain English translation of the Taittiriya Brahmana exists; rendering above is the researcher's own paraphrase of the Sanskrit. Cf. P.-E. Dumont (1954), copyrighted, not quoted.*
> <br>— Researcher's paraphrase (no public-domain translation); cf. P.-E. Dumont (1954) ([source](https://www.jstor.org/stable/i344439))

<sub>**Identification notes (Vedic corpus):** In the Taittirīya tradition Soma's nakshatra is called Invakā where other lists have Mṛgaśīrṣa: TB 1.5.1.1 'somasyenvakā', and TB 3.1.4.3 invokes Mṛgaśīrṣa and the Invakās side by side in the same offering, proving the equation.</sub>

**Maitrāyaṇī Saṃhitā 2.13.20** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/1_veda/1_sam/maitrs_pu.htm)

> *(IAST — the e-text carries no Devanagari copy)*
>
> kṛttikā nakṣatram agnir devatā ... rohiṇī nakṣatraṃ prajāpatir devatā invagā nakṣatraṃ maruto devatā bāhur nakṣatraṃ rudro devatā punarvasur nakṣatram aditir devatā tiṣyo nakṣatraṃ bṛhaspatir devatā ... //MS_2,13.20//
>
> — *Invagā is the asterism, the Maruts the deity; Bāhu is the asterism, Rudra the deity.*
> <br>— No public-domain English translation of the Maitrāyaṇī Saṃhitā located; literal rendering supplied by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/1_veda/1_sam/maitrs_pu.htm))

<sub>**Identification notes (Ṛgveda & Vedāṅga Jyotiṣa):** The Maitrāyaṇī spelling of Invakā, with the deity Maruts, standing where the Taittirīya list has Mṛgaśīrṣa. Macdonell & Keith's comparative table gives slot 3 as 'Mrgasirsa (neut.) | Invaga | Invaka' for TS | MS | KS — the g/k variation is a real recensional difference, not an e-text error. Invakā also survives into the Atharvaveda Nakṣatra Kalpa (avparis_1,6.5, 'invakāsu'). SCRIPT NOTE: source e-text is romanised IAST; the Devanagari headword is supplied by the compiler.</sub>

### इल्वलाः (Ilvalāḥ) — the stars of Orion's head

**Modern identification:** the stars of Orion's head — λ, φ¹, φ² Orionis, Orion (*likely*)

*See also:* `mrigashirsha`, `invaka`, `agrahayani`

**Amarakośa 1.3.222 (Dig-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> इल्वलास्तच्छिरोदेशे तारका निवसन्ति याः ॥ १.३.२२२ ॥
>
> — *'Stars in his head.' (Literally: 'The stars which dwell in the head-region of that [deer] are the Ilvalās.')*
> <br>— H.T. Colebrooke (1808), with a literal rendering of the relative clause added ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** One of the most valuable lexicon finds: Amarakośa defines Ilvalāḥ by a relative clause — 'the stars which dwell in the head-region of that [Deer]' — so the anatomy is stated by the lexicon itself, not inferred. Colebrooke glosses 'Stars in his head', following directly on 'Orion'. Cognate/variant of Invakā already on file (the Vedic Invakā/Ilvalā alternation); this is the classical form with an explicit definition attached, and the Śārdūlakarṇāvadāna's 'three stars, deer's-head-shaped' independently confirms the group.</sub>

### तिष्यः (Tiṣya) — the later Puṣya: the Asellus stars and Praesepe region

**Modern identification:** the later Puṣya: the Asellus stars and Praesepe region — γ, δ, θ Cancri (δ Cancri = Asellus Australis nearest the ecliptic), with the Praesepe cluster M44, Cancer (*disputed*)

*See also:* `pushya`

**Taittirīya Saṃhitā 4.4.10.1** — [Sanskrit e-text](https://sa.wikisource.org/wiki/तैत्तिरीयसंहिता(विस्वरः)

> तिष्यो नक्षत्रम् बृहस्पतिर् देवता
>
> — *Tisya the Naksatra, Brhaspati the deity.*
> <br>— A.B. Keith, The Veda of the Black Yajus School (1914) ([source](https://www.sacred-texts.com/hin/yv/yv04.htm) · [mirror](https://web.archive.org/web/20210301091213/https://www.sacred-texts.com/hin/yv/yv04.htm))

<sub>**Identification notes (Vedic corpus):** Tiṣya, deity Bṛhaspati, is the archaic name that the AV (19.7.2) and all later lists call Puṣya; Whitney's note to AV 19.7 flags this TS/AV name difference explicitly. A faint asterism: identification rests on its fixed position between Punarvasū (Castor/Pollux) and Āśleṣā, hence 'likely' rather than 'certain'. Also TB 3.1.1.5, TB 3.1.4.6 (Bṛhaspati-Tiṣya offering).</sub>

**Ṛgveda 5.54.13** — [Sanskrit e-text](https://sa.wikisource.org/wiki/ऋग्वेदः_सूक्तं_५.५४)

> युष्माद्त्तस्य मरुतो विचेतसो रायः स्याम रथ्यो वयस्वतः।
> न यो युच्छति तिष्यो यथा दिवोऽस्मे रारन्त मरुतः सहस्रिणम् ॥१३॥
>
> — *Sage Maruts, may we be the drivers of the car of riches full of life that have been given by you. O Maruts, let that wealth in thousands dwell with us which never vanishes like Tisya from the sky.*
> <br>— R.T.H. Griffith (1896) ([source](https://en.wikisource.org/wiki/The_Hymns_of_the_Rigveda/Book_5/Hymn_54))

<sub>**Identification notes (Ṛgveda & Vedāṅga Jyotiṣa):** One of only two occurrences of tiṣya in the whole Ṛgveda. Macdonell & Keith, Vedic Index (1912) i.312: 'Tisya occurs twice in the Rigveda, apparently as the name of a star, though Sayana takes it to mean the sun. It is doubtless identical with the Avestan Tistrya. Later it is the name of a lunar mansion', citing 5.54.13 and 10.64.8. Here Tiṣya is a byword for a star that never fails to appear — an observational, not a calendrical, use.</sub>

**Ṛgveda 10.64.8** — [Sanskrit e-text](https://sa.wikisource.org/wiki/ऋग्वेदः_सूक्तं_१०.६४)

> त्रिः सप्त सस्रा नद्यो महीरपो वनस्पतीन्पर्वताँ अग्निमूतये।
> कृशानुमस्तॄन्तिष्यं सधस्थ आ रुद्रं रुद्रेषु रुद्रियं हवामहे ॥८॥
>
> — *The thrice-seven wandering Rivers, yea, the mighty floods, the forest trees, the mountains, Agni to our aid, Krsanu, Tisya, archers to our gathering-place, and Rudra strong amid the Rudras we invoke.*
> <br>— R.T.H. Griffith (1896) ([source](https://en.wikisource.org/wiki/The_Hymns_of_the_Rigveda/Book_10/Hymn_64))

<sub>**Identification notes (Ṛgveda & Vedāṅga Jyotiṣa):** The second and last Ṛgvedic occurrence. Notable because Tiṣya is invoked here alongside Kṛśānu the archer (कृशानु, astṛ 'archer'), which Macdonell & Keith flag explicitly: '5.54.13; 10.64.8 (with Krsanu as an archer)'. Kṛśānu is the celestial bowman who shoots at the soma-eagle in RV 4.27.3; Tilak and others connected this archer-and-target tableau with the Orion/Sirius myth complex (Mṛgavyādha), but NO Vedic text calls Kṛśānu a star, so that link is speculation, not attestation.</sub>

**Amarakośa 1.3.219 (Dig-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> राधाविशाखा पुष्ये तु सिध्यतिष्यौ श्रविष्ठया ॥ १.३.२१९ ॥
>
> — *'Stars in Cancer.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** The classical lexicon still preserves the Vedic Tiṣya as a live synonym of Puṣya, some 1500 years after the Ṛgvedic attestation on file — and Colebrooke's gloss 'Stars in Cancer' fixes it in Cancer, not (as sometimes proposed for the Vedic form) at Sirius.</sub>

**Sūrya Siddhānta 9.15** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_उदयास्ताधिकारः)

> भरणीतिष्यसौम्यानि सौक्ष्म्यात् त्रिःसप्तकाम्शकैः / शेषाणि सप्तदशभिर् दृश्यादृश्यानि भानि तु //
>
> — *15. Bharani, Pushya, and Mrgaçirsha, owing to their faintness, are seen at twenty-one degrees; the rest of the asterisms become visible and invisible at seventeen degrees.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** Already on file from the Ṛgveda and the Amarakośa; SS 9.15 shows the archaic name surviving in a siddhānta, placed in the faintest class (21°) 'owing to their faintness' (saukṣmyāt). Al-Bīrūnī's parallel list likewise puts Alnathra (the Praesepe region of Cancer) in his faintest 20° class.</sub>

### सिध्यः (Sidhya) — Asellus Australis

**Modern identification:** Asellus Australis — δ Cancri, Cancer (*certain*)

*See also:* `pushya`, `tishya`

**Amarakośa 1.3.219 (Dig-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> राधाविशाखा पुष्ये तु सिध्यतिष्यौ श्रविष्ठया ॥ १.३.२१९ ॥
>
> — *'Stars in Cancer.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** Third name of Puṣya alongside Tiṣya, 'the auspicious/successful one'. Colebrooke glosses the trio 'Stars in Cancer'. The Śārdūlakarṇāvadāna gives Puṣya three stars in a vardhamāna (auspicious-mark) figure, matching δ, γ and θ Cancri.</sub>

### बाहू (रुद्रस्य) (Bāhū (Rudrasya)) — 'the two Arms' of the deer/Orion: usually taken as Betelgeuse and Bellatrix

**Modern identification:** 'the two Arms' of the deer/Orion: usually taken as Betelgeuse and Bellatrix — α Orionis and γ Orionis, Orion (*disputed*)

*See also:* `ardra`

**Taittirīya Brāhmaṇa 1.5.1.1** — [Sanskrit e-text](https://sa.wikisource.org/wiki/तैत्तिरीयब्राह्मणम्_(विस्वरपाठः)

> रुद्रस्य बाहू ।मृगयवः परस्ताद्विक्षारोऽवस्तात्
>
> — *[Paraphrase] Of Rudra are the two Arms (Bahu); the hunters above, ... below. No public-domain English translation of the Taittiriya Brahmana exists; rendering above is the researcher's own paraphrase of the Sanskrit. Cf. P.-E. Dumont (1954), copyrighted, not quoted.*
> <br>— Researcher's paraphrase (no public-domain translation); cf. P.-E. Dumont (1954) ([source](https://www.jstor.org/stable/i344439))

<sub>**Identification notes (Vedic corpus):** TB 1.5.1 gives Rudra's nakshatra as the dual Bāhū 'the two arms' in place of Ārdrā, fitting the picture of the celestial deer (Orion): the two bright shoulder stars Betelgeuse + Bellatrix. Which two stars are meant is not stated in the text; Betelgeuse-Bellatrix is the common scholarly reading, and the mention of 'hunters' (mṛgayavaḥ) alongside is part of the same Orion tableau.</sub>

### रोहिणी (द्वितीया; = ज्येष्ठा) (Rohiṇī (second; = Jyeṣṭhā)) — Antares

**Modern identification:** Antares — α Scorpii, Scorpius (*likely*)

*See also:* `jyeshtha`, `rohini`

**Taittirīya Saṃhitā 4.4.10.2** — [Sanskrit e-text](https://sa.wikisource.org/wiki/तैत्तिरीयसंहिता(विस्वरः)

> अनूराधा नक्षत्रम् मित्रो देवता रोहिणी नक्षत्रम् इन्द्रो देवता विचृतौ नक्षत्रम् पितरो देवता
>
> — *Anruradha the Naksatra, Mitra the deity; Rohini the Naksatra, Indra the deity; the two Viçrts the Naksatra; the fathers the deity.*
> <br>— A.B. Keith, The Veda of the Black Yajus School (1914) ([source](https://www.sacred-texts.com/hin/yv/yv04.htm) · [mirror](https://web.archive.org/web/20210301091213/https://www.sacred-texts.com/hin/yv/yv04.htm))

<sub>**Identification notes (Vedic corpus):** TS 4.4.10 lists a SECOND Rohini with deity Indra, standing between Anuradha and Vicrtau (= Mula) - i.e. in the position of the later Jyestha. Antares, the other great red star of the zodiacal belt, evidently also bore the name 'the red one'; later lists rename it Jyeṣṭhā (so already TB 1.5.1 and AV 19.7.3).</sub>

### अश्वयुक् (Aśvayuj) — Sheratan

**Modern identification:** Sheratan — β Arietis, Aries (*certain*)

*See also:* `ashvini`

**Amarakośa 1.3.218 (Dig-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> दाक्षायिण्योऽश्विनीत्यादितारा अश्वयुगश्विनी ॥ १.३.२१८ ॥
>
> — *'The head of Aries.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** Alternative name of Aśvinī, 'the horse-yoker'. Colebrooke glosses the pair as 'The head of Aries'. The form survives in the Arthaśāstra's month-name Āśvayuja and in the Pali Assayuja — a genuinely pan-Indic variant.</sub>

### राधा (Rādhā) — Zubenelgenubi

**Modern identification:** Zubenelgenubi — α Librae, Libra (*certain*)

*See also:* `vishakha`

**Amarakośa 1.3.219 (Dig-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> राधाविशाखा पुष्ये तु सिध्यतिष्यौ श्रविष्ठया ॥ १.३.२१९ ॥
>
> — *'Stars in the Southern scale.' Footnote: 'Properly dual, as indicating two stars, which compose this constellation according to ancient authors. But astronomers now recken [sic] four.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** Amarakośa's synonym for Viśākhā. Colebrooke glosses it 'Stars in the Southern scale' — α Librae — and his footnote records exactly the dispute this database tracks: 'Properly dual, as indicating two stars, which compose this constellation according to ancient authors. But astronomers now reckon four.' The Buddhist Śārdūlakarṇāvadāna independently gives Viśākhā two stars, siding with the 'ancient authors' — and against the faint ι Librae that Burgess derived from the Sūrya Siddhānta's coordinates.</sub>

### श्रविष्ठा (Śraviṣṭhā) — Rotanev (Dhaniṣṭhā)

**Modern identification:** Rotanev (Dhaniṣṭhā) — β Delphini (with α–δ Delphini), Delphinus (*likely*)

*See also:* `dhanishtha`, `vasava`

**Vedāṅga Jyotiṣa, Ārca-jyotiṣa 6 (= Yājuṣa-jyotiṣa 7); also Ārca 5, 19, 34** — [Sanskrit e-text](https://sa.wikisource.org/wiki/ऋग्वेदाङ्गज्योतिषं_सुधाकरभाष्यसहितम्)

> प्रपद्येते श्रविष्ठादौ सूर्याचन्द्रमसावुदक्।
> सार्पार्धे दक्षिणाऽर्कस्य माघश्रावणयोः सदा॥६॥
>
> — *The sun and moon turn towards the north at the beginning of 'Sravish'ṭhā: but the sun turns towards the south in the middle of the constellation over which the serpents preside; and this [his turn towards the south, and towards the north], always [happens] in [the months of] Mág'ha and 'Srávaṇa.*
> <br>— H.T. Colebrooke (1805; repr. Essays on the Religion and Philosophy of the Hindus, 1858, p. 66) ([source](https://archive.org/details/essaysonreligion00coleiala))

<sub>**Identification notes (Ṛgveda & Vedāṅga Jyotiṣa):** The asterism at which the Vedāṅga Jyotiṣa begins the year and places the winter solstice — the oldest datable astronomical statement in Indian literature. Verified in two independent e-texts: the Sudhākara Dvivedī recension on Sanskrit Wikisource (Devanagari, cited here) and GRETIL's romanised Lagadha text, which reads 'prapadyete śraviṣṭhādau sūryācandramasāv udak / sārpārdhe dakṣiṇārkas tu māghaśrāvaṇayoḥ sadā // 6'. Colebrooke, Essays (1858) pp. 66–67: 'Sravish'ṭhā is given, in all the dictionaries of the Sanscrit language, as another name of D'haniṣh'ṭhā... Hence it is clear, that D'haniṣh'ṭhā and Aslesha are the constellations meant; and that when this Hindu calendar was regulated, the solstitial points were reckoned to be at the beginning of the one, and in the middle of the other: and such was the situation of those cardinal points, in the fourteenth century before the Christian era.' IMPORTANT: the name धनिष्ठा never appears in the Vedāṅga Jyotiṣa itself — only श्रविष्ठा; Dhaniṣṭhā enters solely through Sudhākara's 19th-century gloss.</sub>

**Amarakośa 1.3.219–220 (Dig-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> राधाविशाखा पुष्ये तु सिध्यतिष्यौ श्रविष्ठया ॥ १.३.२१९ ॥ समा धनिष्ठाः स्युः प्रोष्ठपदा भाद्रपदाः स्त्रियः ॥ १.३.२२० ॥
>
> — *'The Dolphin.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** The older name of Dhaniṣṭhā, expressly equated with it by the lexicon ('Dhaniṣṭhāḥ are the same as Śraviṣṭhā'). Colebrooke's gloss 'The Dolphin' is decisive for Delphinus, and the Śārdūlakarṇāvadāna's four stars in a śakuna (bird) figure agrees with the Delphinus quadrilateral. This is the name the Vedāṅga Jyotiṣa uses for the asterism that begins its year — Dhaniṣṭhā never appears in that text at all.</sub>

### प्रोष्ठपदा (Proṣṭhapadā) — Markab / Algenib

**Modern identification:** Markab / Algenib — α and γ Pegasi, Pegasus (*certain*)

*See also:* `purva-bhadrapada`, `uttara-bhadrapada`

**Amarakośa 1.3.220 (Dig-varga); Arthaśāstra 2.20.55** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> समा धनिष्ठाः स्युः प्रोष्ठपदा भाद्रपदाः स्त्रियः ॥ १.३.२२० ॥ — cf. (IAST) śrāvaṇaḥ prauṣṭhapadaś ca varṣāḥ // kaz02.20.55
>
> — *'The wing of Pegasus.' — Arthaśāstra: 'Śrāvaṇa and Prauṣṭhapada are the rains.'*
> <br>— H.T. Colebrooke (1808); the Arthaśāstra line rendered literally by the compiler ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** Older feminine form of Bhādrapadā, expressly equated with it. Colebrooke's gloss 'The wing of Pegasus' fixes the asterism on the Pegasus square. The archaic form underlies Kauṭilya's month-name Prauṣṭhapada (Arthaśāstra 2.20.55), confirming it was still standard when the Arthaśāstra's calendar was compiled; the Atharvaveda Nakṣatra Kalpa also uses Proṣṭhapadā rather than Bhādrapadā.</sub>

### आग्रहायणी (Āgrahāyaṇī) — Meissa

**Modern identification:** Meissa — λ Orionis, Orion (*certain*)

*See also:* `mrigashirsha`, `ilvala`

**Amarakośa 1.3.221 (Dig-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> मृगशीर्षं मृगशिरस्तस्मिन्नेवाग्रहायणी ॥ १.३.२२१ ॥
>
> — *'Orion.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** Third name of Mṛgaśiras, 'she who begins the year' — a fossil of the era when the year opened at the Mṛgaśiras full moon, and so a chronological datum in its own right. Amarakośa's tasminn eva ('in that very asterism') makes the equation explicit. Source of the month-name Mārgaśīrṣa/Agrahāyaṇa.</sub>

### अश्वत्थ (Aśvattha) — Altair (Śravaṇa/Śroṇā)

**Modern identification:** Altair (Śravaṇa/Śroṇā) — α Aquilae, Aquila (*disputed*)

*See also:* `shravana`

**Kāṭhaka Saṃhitā 39.13** — [Sanskrit e-text](https://archive.org/stream/vedicindexofname01macduoft/vedicindexofname01macduoft_djvu.txt)

> *No e-text of the Kāṭhaka Saṃhitā is online; the name is attested here through Macdonell & Keith's comparative table of the nakṣatra lists.*
>
> — *[Attested only via the secondary comparative table] '21. Srona .. Srona. .. Asvattha'*
> <br>— A.A. Macdonell & A.B. Keith, Vedic Index of Names and Subjects (1912), i.413 ([source](https://archive.org/stream/vedicindexofname01macduoft/vedicindexofname01macduoft_djvu.txt))

<sub>**Identification notes (Ṛgveda & Vedāṅga Jyotiṣa):** A name unique to the Kāṭhaka Saṃhitā, standing in slot 21 where the Taittirīya and Maitrāyaṇī lists both read Śroṇā. Attested in Macdonell & Keith's comparative table of the three Yajurveda lists, Vedic Index (1912) i.413: '21. Srona .. Srona. .. Asvattha' for TS | MS | KS. The word otherwise means the pipal tree (Ficus religiosa). NOT verified against a primary Kāṭhaka e-text — GRETIL does not host it and the TITUS URL returned only a frame stub — so confidence is marked disputed on that ground alone, not because the scholarly attestation is weak.</sub>

### ब्राह्मण (Brāhmaṇa) — unidentified

**Modern identification:** unidentified — —, — (*disputed*)

**Maitrāyaṇī Saṃhitā 2.13.20** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/1_veda/1_sam/maitrs_pu.htm)

> *(IAST — the e-text carries no Devanagari copy)*
>
> ... revatī nakṣatraṃ pūṣā devatāśvayujau nakṣatram aśvinau devatā bharaṇīr nakṣatraṃ yamo devatā brāhmaṇo nakṣatraṃ somo devatā ... //MS_2,13.20//
>
> — *Bharaṇī is the asterism, Yama the deity; Brāhmaṇa is the asterism, Soma the deity.*
> <br>— No public-domain English translation of the Maitrāyaṇī Saṃhitā located; literal rendering supplied by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/1_veda/1_sam/maitrs_pu.htm))

<sub>**Identification notes (Ṛgveda & Vedāṅga Jyotiṣa):** An anomalous extra nakshatra appended after Bharaṇī at the very end of the Maitrāyaṇī list, with Soma as its deity — 'brāhmaṇo nakṣatraṃ somo devatā'. The MS list already contains 28 including Abhijit, so Brāhmaṇa is a 29th. Macdonell & Keith, Vedic Index (1912) i.414 confirm: 'the list in the Maitrayani Samhita contains 28 Naksatras, including Abhijit, and adds Brahmana at the end as another', noting that Taittirīya Brāhmaṇa 3.1.4 likewise 'mentions Brahmana as the 28th Naksatra' — a point Weber used to argue Abhijit was an interpolation. Almost certainly a ritual or classificatory category rather than an observed asterism; recorded because it is a genuine textual name, not because it is identifiable in the sky. SCRIPT NOTE: source e-text is romanised IAST.</sub>

### वैष्णव (Vaiṣṇava) — Altair

**Modern identification:** Altair — α Aquilae, Aquila (*certain*)

*See also:* `shravana`

**Sūrya Siddhānta 9.18** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_उदयास्ताधिकारः)

> अभिजिद् ब्रह्महृदयम् स्वातीवैष्णववासवाः / अहिर्बुध्न्यम् उदक्स्थत्वान् न लुप्यन्ते ऽर्करश्मिभिः //
>
> — *18. Abhijit, Brahmahrdaya, Svati, Çravana (vāishnava), Çravishtha (vāsava), and Uttara-Bhādrapadā (ahirbudhnya), owing to their northern situation, are not extinguished by the sun's rays.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** Deity-epithet name for Śravaṇa, whose presiding divinity is Viṣṇu, used in place of the ordinary name at SS 9.18. Corroborated by al-Bīrūnī, whose never-setting list includes 'the two Eagles' — al-Nasr al-Ṭāʾir (Altair) and al-Nasr al-Wāqiʿ (Vega) — matching Vaiṣṇava and Abhijit exactly. The Buddhist Śārdūlakarṇāvadāna independently gives Śravaṇā the deity Viṣṇu.</sub>

### वासव (Vāsava) — Rotanev

**Modern identification:** Rotanev — β Delphini, Delphinus (*likely*)

*See also:* `dhanishtha`, `shravishtha`

**Sūrya Siddhānta 9.18** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_उदयास्ताधिकारः)

> अभिजिद् ब्रह्महृदयम् स्वातीवैष्णववासवाः / अहिर्बुध्न्यम् उदक्स्थत्वान् न लुप्यन्ते ऽर्करश्मिभिः //
>
> — *18. ... Çravishtha (vāsava) ... owing to their northern situation, are not extinguished by the sun's rays.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** Deity-epithet name for Śraviṣṭhā/Dhaniṣṭhā, whose divinities are the Vasus, used at SS 9.18. Al-Bīrūnī's independent never-setting list also has Dhaniṣṭhā, and his nakshatra table remarks of it: 'Unknown. Most likely it is the Dolphin' — an independent arrival at Delphinus, matching Colebrooke's gloss on the Amarakośa.</sub>

### अहिर्बुध्न्य (Ahirbudhnya) — Algenib / Alpheratz

**Modern identification:** Algenib / Alpheratz — γ Pegasi / α Andromedae, Pegasus / Andromeda (*certain*)

*See also:* `uttara-bhadrapada`

**Sūrya Siddhānta 9.18** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_उदयास्ताधिकारः)

> अभिजिद् ब्रह्महृदयम् स्वातीवैष्णववासवाः / अहिर्बुध्न्यम् उदक्स्थत्वान् न लुप्यन्ते ऽर्करश्मिभिः //
>
> — *18. ... and Uttara-Bhādrapadā (ahirbudhnya), owing to their northern situation, are not extinguished by the sun's rays.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** Deity-epithet name for Uttara-Bhādrapadā, whose divinity is Ahir Budhnya, 'the serpent of the deep', used at SS 9.18. Burgess notes the internal tension that this star, of the second magnitude, is left in the unspecified 17° class at 9.15 yet appears here among those never obscured. Al-Bīrūnī's never-setting list likewise ends with Uttarabhādrapadā.</sub>

### अश्विनिदैवत (Aśvinidaivata) — Sheratan

**Modern identification:** Sheratan — β Arietis, Aries (*certain*)

*See also:* `ashvini`

**Sūrya Siddhānta 9.13** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_उदयास्ताधिकारः)

> हस्तश्रवणफाल्गुन्यः श्रविष्टा रोहिणीमघाः / चतुर्दशाम्शकैर् दृश्या विशाखाश्विनिदैवतम् //
>
> — *13. Hasta, Çravana, the Phalgunis, Çravishthā, Rohini, and Maghā become visible at fourteen degrees; also Viçākhā and Açvini.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** Periphrastic name for Aśvinī at SS 9.13 — literally 'that whose deity is the Aśvins'. Burgess renders the compound simply as 'Açvini'. Note that the Buddhist tradition gives this asterism the deity Gandharva instead.</sub>

### मैत्र (Maitra) — Dschubba

**Modern identification:** Dschubba — δ Scorpii, Scorpius (*certain*)

*See also:* `anuradha`

**Sūrya Siddhānta 9.14; Brāhmasphuṭasiddhānta, Bhagrahayutyadhikāra 9** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_उदयास्ताधिकारः)

> कृत्तिकामैत्रमूलानि सार्पम् रौद्रर्क्षम् एव च / दृश्यन्ते पञ्चदशभिर् आषाढाद् द्वितयम् तथा //
>
> — *14. Krttikā, Anurādhā (māitra), and Mūla, and likewise Açleshā and Ārdrā (rāudrarksha), are seen at fifteen degrees; so, too, the pair of Āshādhās.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** Deity-epithet name for Anurādhā, whose divinity is Mitra. Used at SS 9.14 and also by Brahmagupta at Bhagrahayutyadhikāra 9 (maitrasya) in the yogatārā table, so the usage is standard across the siddhāntas rather than peculiar to one text. The Buddhist Śārdūlakarṇāvadāna independently gives Anurādhā the deity Mitra.</sub>

### रौद्रर्क्ष (Raudrarkṣa) — Betelgeuse

**Modern identification:** Betelgeuse — α Orionis, Orion (*disputed*)

*See also:* `ardra`

**Sūrya Siddhānta 9.14; cf. al-Bīrūnī, India ch. LV** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_उदयास्ताधिकारः)

> कृत्तिकामैत्रमूलानि सार्पम् रौद्रर्क्षम् एव च / दृश्यन्ते पञ्चदशभिर् आषाढाद् द्वितयम् तथा //
>
> — *14. ... and likewise Açleshā and Ārdrā (rāudrarksha), are seen at fifteen degrees. — Al-Bīrūnī, quoting Mārkaṇḍeya via Varāhamihira: 'Abhijit, the Falling Eagle; Ārdrā, the Sirius Yemenicus; Rohiṇī, or Aldabarān; Punarvasu, i.e. the Two Heads of the Twins; Puṣya, Revatī, Agastya or Canopus, the Great Bear, the master of Vāyu, the master of Ahirbudhnya, and the master of Śraviṣṭhā, each of these stars has a circumference of five yojanas.'*
> <br>— E. Burgess (1860); E. Sachau (1910) for al-Bīrūnī ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** 'The asterism of Rudra' = Ārdrā, whose divinity is Rudra. Burgess flags the classification as anomalous: α Orionis 'though a variable star, does not fall below the first to second magnitude', yet is ranked with six third-magnitude stars in the 15° class. Al-Bīrūnī dissents twice over: his nakshatra table says 'Unknown. Most likely identical with Canis Minor' (Procyon), while his rendering of Varāhamihira's Saṃhitā ch. 4 glosses 'Ārdrā, the Sirius Yemenicus' (Sirius). The two Arabic names differ only in epithet (al-yamāniyya = Sirius, al-shāmiyya = Procyon), so the likeliest reading is that the Saṃhitā gloss is corrupt and Procyon was his settled view — but as the text stands he assigns Sirius twice, since he uses 'Sirius Yemenicus' for Mṛgavyādha too. An independent ancient dissent from Ārdrā = Betelgeuse, worth recording.</sub>

### सौम्य (Saumya) — Meissa

**Modern identification:** Meissa — λ Orionis, Orion (*certain*)

*See also:* `mrigashirsha`

**Sūrya Siddhānta 9.15** — [Sanskrit e-text](https://sa.wikisource.org/wiki/सूर्यसिद्धान्त_उदयास्ताधिकारः)

> भरणीतिष्यसौम्यानि सौक्ष्म्यात् त्रिःसप्तकाम्शकैः / शेषाणि सप्तदशभिर् दृश्यादृश्यानि भानि तु //
>
> — *15. Bharani, Pushya, and Mrgaçirsha, owing to their faintness, are seen at twenty-one degrees; the rest of the asterisms become visible and invisible at seventeen degrees.*
> <br>— E. Burgess (1860) ([source](https://archive.org/download/jstor-592174/592174_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** Deity-epithet name for Mṛgaśīrṣa, whose divinity is Soma; the same epithet is used at SS 8.16. Al-Bīrūnī's parallel faint-class list gives Alhakʿa (al-Haqʿa, the head of Orion, λ/φ¹/φ² Orionis), an exact independent match — and the Buddhist tradition also gives Mṛgaśirā the deity Soma and three head-stars.</sub>

### प्राजेश (Prājeśa) — Aldebaran

**Modern identification:** Aldebaran — α Tauri, Taurus (*certain*)

*See also:* `rohini`, `prajapati`

**Brāhmasphuṭasiddhānta, Bhagrahayutyadhikāra 8** — [Sanskrit e-text](https://archive.org/download/Brahmasphutasiddhanta/Brahmasphutasiddhanta_djvu.txt)

> प्राजेशयोगतारा विक्षेपाः कला त्रिघनहीनः । आग्नेयस्य कलानामेकोनत्रिंशता हीनैः ॥ ८ ॥
>
> — *No public-domain translation exists. Sense: 'The junction-star of Prājeśa (Rohiṇī) stands with its latitudes diminished by twenty-seven minutes; that of Āgneya (Kṛttikā), by twenty-nine minutes.'*
> <br>— Paraphrase by the compiler ([source](https://archive.org/download/Brahmasphutasiddhanta/Brahmasphutasiddhanta_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** 'That of the Lord of Creatures' — Brahmagupta's name for ROHIṆĪ, whose divinity is Prajāpati, in the yogatārā table; its latitude is to be reduced by 27 minutes. NAME-COLLISION WARNING: Prājeśa/Prajāpati here denotes Rohiṇī = α Tauri, NOT the separate fixed star Prajāpati = δ Aurigae of Sūrya Siddhānta 8.20–21 already on file. The two must not be merged.</sub>

### आग्नेय (Āgneya) — Alcyone

**Modern identification:** Alcyone — η Tauri, Taurus (*certain*)

*See also:* `krittika`, `agni`

**Brāhmasphuṭasiddhānta, Bhagrahayutyadhikāra 8–9** — [Sanskrit e-text](https://archive.org/download/Brahmasphutasiddhanta/Brahmasphutasiddhanta_djvu.txt)

> पञ्चदशकलाहीनैश्चित्रायाः सप्तभिर्विशाखायाः । षट्सप्तत्या मैत्रस्यैन्द्रस्य त्रिंशता हीनैः ॥ ९ ॥
>
> — *No public-domain translation exists. Sense: '(the junction-star) of Citrā with fifteen minutes deducted, of Viśākhā with seven, of Maitra (Anurādhā) with seventy-six, of Aindra (Jyeṣṭhā) with thirty deducted.'*
> <br>— Paraphrase by the compiler ([source](https://archive.org/download/Brahmasphutasiddhanta/Brahmasphutasiddhanta_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** 'That of Agni' — Brahmagupta's name for KṚTTIKĀ, whose divinity is Agni, in the yogatārā table; its polar latitude is reduced by 29 minutes. Cited together with Aindra (Jyeṣṭhā, reduced by 30') and Maitra (Anurādhā, by 76'). NAME-COLLISION WARNING: Āgneya here is Kṛttikā = η Tauri, NOT the separate fixed star Agni/Hutabhuj = β Tauri of Sūrya Siddhānta 8.20 already on file.</sub>

## The vocabulary of 'star' itself

Not names of stars but the words for them, with the oldest Indian etymologies. Yāska derives ṛkṣa from height and stṛ from scattering; the Amarakośa treats nakṣatra, ṛkṣa, bha, tārā, tārakā and uḍu as interchangeable. *tārā* is the element in *yoga-tārā*, 'junction star', on which every identification in this database depends.

### नक्षत्रम् (Nakṣatra) — star / asterism (generic)

**Modern identification:** star / asterism (generic) — —, — (*certain*)

*See also:* `bha`, `tara`, `taraka`, `udu`, `dhishnya`, `str`, `rksha`

**Amarakośa 1.3.217 (Dig-varga); Nirukta 3.20** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> नक्षत्रमृक्षं भं तारा तारकाप्युडु वा स्त्रियाम् ॥ १.३.२१७ ॥ — cf. निरुक्त ३.२०: नक्षत्राणि नक्षतेर्गतिकर्मणः । नेमानि क्षत्राणि इति च ब्राह्मणम् ।
>
> — *'A star.' — Nirukta: 'Naksatra (stars) is derived from (the root) nakṣ, meaning to go. There is also a Brahmana passage: These are not gold (na-kṣatrāṇi).'*
> <br>— H.T. Colebrooke (1808); Lakshman Sarup (1921) for the Nirukta ([source](https://archive.org/download/nighantuniruktao00yaskuoft/nighantuniruktao00yaskuoft_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** Head-word of the six-fold synonym set for 'star'. The lexicon treats nakṣatra, ṛkṣa, bha, tārā, tārakā and uḍu as fully interchangeable — which is why the separate entries for Ṛkṣāḥ and the rest form one lexical family. Yāska's Nirukta 3.20 supplies the oldest etymology: from the root nakṣ 'to go', with the alternative Brāhmaṇa pun na imāni kṣatrāṇi.</sub>

### भम् (Bha) — star / asterism (generic)

**Modern identification:** star / asterism (generic) — —, — (*certain*)

*See also:* `nakshatra-generic`

**Amarakośa 1.3.217 (Dig-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> नक्षत्रमृक्षं भं तारा तारकाप्युडु वा स्त्रियाम् ॥ १.३.२१७ ॥
>
> — *'A star.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** The technical monosyllable used throughout siddhāntic astronomy for a nakshatra — bha-gaṇa (the asterism-circle), bha-cakra, bha-bheda, and the bhagrahayuti chapter-titles of Brahmagupta and Bhāskara. Amarakośa records it twice: as a synonym of 'star' here, and in the Nānārtha-varga among the senses of dhiṣṇya and of dhruva.</sub>

### तारा (Tārā) — star (generic)

**Modern identification:** star (generic) — —, — (*certain*)

*See also:* `nakshatra-generic`, `taraka`

**Amarakośa 1.3.217 (Dig-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> नक्षत्रमृक्षं भं तारा तारकाप्युडु वा स्त्रियाम् ॥ १.३.२१७ ॥
>
> — *'A star.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** The commonest classical word for a single star, and the element in the compound yoga-tārā ('junction star') on which the whole nakshatra-identification enterprise rests.</sub>

### तारका (Tārakā) — star (generic)

**Modern identification:** star (generic) — —, — (*certain*)

*See also:* `nakshatra-generic`, `tara`

**Amarakośa 1.3.217 (Dig-varga); Arthaśāstra 9.4.26** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> नक्षत्रमृक्षं भं तारा तारकाप्युडु वा स्त्रियाम् ॥ १.३.२१७ ॥ — cf. (IAST) nakṣatram ati pṛcchantaṃ bālam artho 'tivartate / artho hy arthasya nakṣatraṃ kiṃ kariṣyanti tārakāḥ // kaz09.4.26
>
> — *'A star.' — Arthaśāstra: 'Wealth passes by the childish man who keeps asking about the asterism; for wealth is the asterism of wealth — what will the stars do?'*
> <br>— H.T. Colebrooke (1808); the Arthaśāstra line rendered literally by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_kauTilya-arthazAstra.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** Diminutive of tārā, and the word the Atharvaveda uses of Vicṛtau (tārake, 'the two stars') and Amarakośa of the Ilvalāḥ. Kauṭilya uses it in the sharpest ancient Indian statement against astral determinism, Arthaśāstra 9.4.26: 'wealth is the asterism of wealth — what will the stars do?' (kiṃ kariṣyanti tārakāḥ).</sub>

### उडु (Uḍu) — star / lunar mansion (generic)

**Modern identification:** star / lunar mansion (generic) — —, — (*certain*)

*See also:* `nakshatra-generic`

**Amarakośa 1.3.217 (Dig-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> नक्षत्रमृक्षं भं तारा तारकाप्युडु वा स्त्रियाम् ॥ १.३.२१७ ॥
>
> — *'A star.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** Sixth member of the synonym set; Amarakośa notes it is optionally feminine (vā striyām). The base of uḍu-pati and uḍu-rāja, 'lord of the asterisms' = the moon. Distinct from uḍupa 'raft', which the same lexicon records separately.</sub>

### धिष्ण्यम् (Dhiṣṇya) — asterism / star-station (generic)

**Modern identification:** asterism / star-station (generic) — —, — (*certain*)

*See also:* `nakshatra-generic`

**Amarakośa 3.3.671 (Nānārtha-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/तृतीयकाण्डम्)

> धिष्ण्यं स्थाने गृहे भेऽग्नौ भाग्यं कर्म शुभाशुभम् ॥ ३.३.६७१ ॥
>
> — *Literal rendering: 'Dhiṣṇya [means] a place, a house, an asterism (bha), fire; bhāgya [means] deed, good or ill.'*
> <br>— Literal rendering by the compiler (Colebrooke's Nānārtha page is illegible in the available scan) ([source](https://sa.wikisource.org/wiki/अमरकोशः/तृतीयकाण्डम्))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** The Nānārtha-varga lists four senses: 'place', 'house', bha (= asterism), 'fire'. The semantic chain place > station > asterism is the Vedic dhiṣṇya (fire-hearth) applied to the lunar mansions, and is the lexicographical warrant for reading dhiṣṇya as a star-word in kāvya.</sub>

### स्तृभिः (Stṛbhiḥ (stem stṛ)) — the stars (generic, Vedic)

**Modern identification:** the stars (generic, Vedic) — —, — (*certain*)

*See also:* `nakshatra-generic`, `rksha`

**Nirukta 3.20 (on Nighaṇṭu 3)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/निरुक्तशास्त्रम्/तृतीयोध्यायः)

> ऋक्षाः स्तृभिरिति नक्षत्राणाम् । ... स्तृभिस्तीर्णानीव ख्यायन्ते । ... पश्यन्तो द्यामिव स्तृभिः ।
>
> — *'Rksāh and strbhih are (synonyms) of stars.' ... 'Strbhih (stars) appear to be scattered (in the sky).' ... 'Looking at the sky with stars, as it were.'*
> <br>— Lakshman Sarup (1921) ([source](https://archive.org/download/nighantuniruktao00yaskuoft/nighantuniruktao00yaskuoft_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** The oldest Sanskrit word for 'stars', and the one the Nighaṇṭu pairs with ṛkṣāḥ. Yāska derives it from stṛ 'to scatter/strew' — 'they appear as if strewn'. Cognate with Greek astēr, Latin stella, English star. Attested at RV 4.7.3, quoted by Yāska.</sub>

## Sky-figures

Whole figures drawn in the stars, rather than single points.

### शिशुमार (Śiśumāra) — the celestial porpoise/dolphin — a whole star-figure, not a single star

**Modern identification:** the celestial porpoise/dolphin — a whole star-figure, not a single star — —, Draco (+ Ursa Minor) on the dominant reading; the Bhāgavata's expanded version spans the entire sky (*disputed*)

*See also:* `dhruva`, `dhata-vidhata`, `indra-mahendra`, `kashyapa`, `marichi-tail`, `uttanapada`, `yajna-group`, `yama-shishumara`, `prajapati-circumpolar`, `akashaganga`

**Bhāgavata Purāṇa 5.23.4 (also 5.23.5); parallels Viṣṇu P. 2.9.1, 2.9.5; Vāyu P. 52.90-95; Matsya P. 125.5, 127.19-25; Brahmāṇḍa P. 1,23.99-105** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/3_purana/bhagp/bhp_05u.htm)

> केचनैतज्ज्योतिरनीकं शिशुमारसंस्थानेन भगवतो वासुदेवस्य योगधारणायामनुवर्णयन्ति ॥ ४ ॥
>
> — *According to the doctrine of some, the celestial system, assuming the shape of a porpoise (Sisumara) is stationed [in] the Reverend Vasudeva's region of contemplation (Dhyana).*
> <br>— J.M. Sanyal (Srimad-Bhagabatam vol. II, 1930s; public domain) ([source](https://archive.org/details/in.ernet.dli.2015.187346))

<sub>**Identification notes (Purāṇas):** Two quite different figures share the name. (a) The older, compact Śiśumāra of Viṣṇu P. 2.9/2.12, Vāyu 52, Matsya 125/127 and Brahmāṇḍa 1,23 is explicitly a FOURTEEN-star figure (Matsya 125.5 caturdaśarkṣeṣu) with Dhruva in the tail; R.N. Iyengar and R.S. Hariharan identify it with Draco, and al-Bīrūnī (c. 1030 CE) independently reports that Hindus placed the pole star in a four-footed aquatic animal called Śiśumāra, glossing it with Persian susumār, the Great Lizard = Draco. (b) The Bhāgavata's Śiśumāra (5.23.4-7) carries all 28 nakṣatras and all the planets along its flanks, so it cannot be a compact circumpolar constellation — it is the whole celestial sphere given porpoise shape. Interpreters who identify it with Ursa Minor alone are reading (a) into (b). The one structural fact both share, and the strongest argument for the Draco/Ursa Minor core, is the run from the tail-tip inward: Dhruva → Agni/Indra/Prajāpati/Dharma → Dhātā/Vidhātā → Saptarṣi (Ursa Major), which traces exactly the path from the pole down the Draco/UMi tail to the Big Dipper.</sub>

### सक्वर (?) (Sakvara) — the circumpolar 14-star figure (a second name for the Śiśumāra)

**Modern identification:** the circumpolar 14-star figure (a second name for the Śiśumāra) — —, Ursa Minor / Draco (*disputed*)

*See also:* `shishumara`

**Al-Bīrūnī, India ch. XXII (Sachau 1910, vol. 1, pp. 241–242)** — [Sanskrit e-text](https://archive.org/download/alberunisindiaac01biru/alberunisindiaac01biru_djvu.txt)

> *No Sanskrit text: al-Bīrūnī wrote in Arabic, and the passage survives here only in Sachau's English.*
>
> — *The Hindus tell rather ludicrous tales when speaking of the figure in which they represent this group of stars, viz. the figure of a four-footed aquatic animal, which they call Sakvara, and also Śiśumāra. I suppose that the latter animal is the great lizard, for in Persia it is called Susmār, which sounds much like the Indian Śiśumāra. ... The Vishnu-Dharma says: 'Fourteen of these stars he placed round the pole in the shape of a śiśumāra, which drive the other stars round the pole. One of them, north of the pole, on the uppermost chin, is Uttānapāda, on the lowest chin Yajña, on the head Dharma, on the breast Nārāyaṇa, on the two hands towards the east the two stars Aśvinī the physicians, on the two feet Varuṇa, and Aryaman towards the west, on the penis Saṃwatsara, on the back Mitra, on the tail Agni, Mahendra, Marīci, and Kaśyapa.'*
> <br>— E. Sachau (1910) ([source](https://archive.org/download/alberunisindiaac01biru/alberunisindiaac01biru_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** Al-Bīrūnī records TWO Sanskrit names for the circumpolar aquatic figure: 'a four-footed aquatic animal, which they call Sakvara, and also Śiśumāra.' Sakvara is otherwise unattested and no Sanskrit source for it could be found; the underlying form may be śākvara ('bull-like, mighty') or a corruption of śiśumāra itself — treat as unverified. The Devanagari above is a transliteration of Sachau's Latin-script form, marked (?) like Śūla's, and is NOT an attested spelling. His etymological note is the prize: 'I suppose that the latter animal is the great lizard, for in Persia it is called Susmār, which sounds much like the Indian Śiśumāra' — independent support for the Draco reading already on file. He then gives the Viṣṇu-Dharma's fourteen-star roster, which differs from the Purāṇic versions on file by putting NĀRĀYAṆA ON THE BREAST and the two Aśvins on the hands. He closes with a jab — 'How simple those people are! Among us there are scholars who know between 1020 to 1030 stars' — and a methodological admission that explains why his own nakshatra guesses are weak: 'If I had found a Hindu able to point out to me with his finger the single stars, I should have been able to identify them with the star-figures known among Greeks and Arabs.'</sub>

### त्रिशङ्कु (Triśaṅku) — Triśaṅku — a king fixed head-downward in the southern sky

**Modern identification:** Triśaṅku — a king fixed head-downward in the southern sky — —, Crux (the Southern Cross) on the usual modern gloss (*disputed*)

**Bhāgavata Purāṇa 9.7.5-6** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/3_purana/bhagp/bhp_09u.htm)

> तस्य सत्यव्रत: पुत्रस्त्रिशङ्कुरिति विश्रुत: । प्राप्तश्चाण्डालतां शापाद् गुरो: कौशिकतेजसा ॥ ५ ॥ सशरीरो गत: स्वर्गमद्यापि दिवि द‍ृश्यते । पातितोऽवाक् शिरा देवैस्तेनैव स्तम्भितो बलात् ॥ ६ ॥
>
> — *His son was known as Trishanku, and he was truthful. He became a Chandala by the curse of [his] preceptor, but was transmitted to Heaven with his whole body by virtue of the powers of Kausika, and is still seen in the firmament. He was going to be thrown headlong down by the gods, but was forcibly resisted by Viswamitra's great power of asceticism.*
> <br>— J.M. Sanyal (Srimad-Bhagabatam vol. III; public domain). OCR lightly cleaned; sense unaffected. ([source](https://archive.org/details/in.ernet.dli.2015.186141))

<sub>**Identification notes (Purāṇas):** A Purāṇic sky-figure. The Bhāgavata makes an explicit observational claim: adyāpi divi dṛśyate, 'even today he is seen in the sky', hanging avākśirāḥ, head-downward — the very phrase used of the Śiśumāra at 5.23.5. The Crux/Southern Cross identification comes from later lexicography (Kittel's Kannada-English dictionary: 'a small southern constellation near the celestial pole containing Coalsack; the Southern Cross') and is not stated in any Purāṇa; treat as disputed. Other Purāṇic loci: Brahmāṇḍa 3.63.108, Vāyu 88.108-113, Viṣṇu Purāṇa 4.3.21.</sub>

## Positions on the Śiśumāra

Names the Purāṇas place on the body of the celestial porpoise. These are genuine textual sky-positions, but no Purāṇa equates any of them with a visible star, so none is plotted on the chart — every limb-to-star chart in circulation is modern reconstruction. See the mapping table below.

### धाता, विधाता (Dhātā, Vidhātā) — two circumpolar star-positions at the root of the Śiśumāra's tail

**Modern identification:** two circumpolar star-positions at the root of the Śiśumāra's tail — —, Draco / Ursa Minor region (*disputed*)

*See also:* `shishumara`

**Bhāgavata Purāṇa 5.23.5** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/3_purana/bhagp/bhp_05u.htm)

> यस्य पुच्छाग्रेऽवाक्‌शिरस: कुण्डलीभूतदेहस्य ध्रुव उपकल्पितस्तस्य लाङ्गूले प्रजापतिरग्निरिन्द्रो धर्म इति पुच्छमूले धाता विधाता च कट्यां सप्तर्षय: ॥ ५ ॥
>
> — *At the tail of this Sisumara resting with its head lowered, and its body coiled up, is Dhruva. Under the ends of the Sisumara's tail are Prajapati, Agni, Indra and Dharma; at the root of its tail are Dhata and Vidhata; and about its waist are the Saptarshis (the seven saints).*
> <br>— J.M. Sanyal (1930s; public domain) ([source](https://archive.org/details/in.ernet.dli.2015.187346))

<sub>**Identification notes (Purāṇas):** Unique to the Bhāgavata's expanded recension — the older Viṣṇu/Vāyu/Matsya/Brahmāṇḍa version does not have them. Positionally they fall between the tail-group (Prajāpati, Agni, Indra, Dharma) and the Saptarṣi at the waist, so they should lie along the Draco tail toward Ursa Major. No Purāṇa identifies them with visible stars and no defensible modern equation was found.</sub>

### इन्द्र / महेन्द्र (Indra / Mahendra) — a circumpolar star on the tail of the Śiśumāra

**Modern identification:** a circumpolar star on the tail of the Śiśumāra — —, Draco / Ursa Minor region (*disputed*)

*See also:* `shishumara`, `kashyapa`

**Viṣṇu Purāṇa 2.12.34; Bhāgavata Purāṇa 5.23.5 (and 5.23.1); Vāyu Purāṇa 52.95; Matsya Purāṇa 127.25; Brahmāṇḍa Purāṇa 1,23.104** — [Sanskrit e-text](https://sa.wikisource.org/wiki/विष्णुपुराणम्/द्वितीयांशः/अध्यायः_१२)

> पुच्छेग्निश्च महेन्द्र श्च कश्यपोथ ततो ध्रुवः । तारका शिशुमारस्य नास्तमेति चतुष्टयम् ॥ ३४ ॥
>
> — *Agni, Mahendra, Kaśyapa, and Dhruva, in succession, are placed in its tail; which four stars in this constellation never set.*
> <br>— H.H. Wilson (1840; public domain) ([source](https://www.sacred-texts.com/hin/vp/vp070.htm))

<sub>**Identification notes (Purāṇas):** One of the most stable elements in the whole tradition: Indra appears in the tail-group in every recension (Bhāgavata 5.23.1 and 5.23.5; Viṣṇu P. 2.12.34 and Vāyu/Matsya/Brahmāṇḍa as Mahendra), and Viṣṇu P. 2.12.34 explicitly states that the four tail-figures are stars that NEVER SET — i.e. circumpolar. That is a real, falsifiable astronomical claim in the text. Which visible star is meant is nowhere stated; proposals that make Indra a former pole star are modern reconstruction.</sub>

### कश्यप (Kaśyapa) — a circumpolar star on the tail of the Śiśumāra, adjacent to Dhruva

**Modern identification:** a circumpolar star on the tail of the Śiśumāra, adjacent to Dhruva — —, Draco / Ursa Minor region (*disputed*)

*See also:* `shishumara`, `indra-mahendra`

**Viṣṇu Purāṇa 2.12.34; Bhāgavata Purāṇa 5.23.1; Vāyu Purāṇa 52.95; Matsya Purāṇa 127.25; Brahmāṇḍa Purāṇa 1,23.104** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/3_purana/bhagp/bhp_05u.htm)

> अथ तस्मात्परतस्त्रयोदशलक्षयोजनान्तरतो यत्तद्विष्णो: परमं पदमभिवदन्ति यत्र ह महाभागवतो ध्रुव औत्तानपादिरग्निनेन्द्रेण प्रजापतिना कश्यपेन धर्मेण च समकालयुग्भि: सबहुमानं दक्षिणत: क्रियमाण ... ॥ १ ॥
>
> — *That auspicious devotee of the Lord exists there ever reverentially circled by Agni, Indra, Prajapati, Kasyapa and Dharma, all simultaneously converted into stars; and attaining equal longevity with the beings living for a Kalpa.*
> <br>— J.M. Sanyal (1930s; public domain) ([source](https://archive.org/details/in.ernet.dli.2015.187346))

<sub>**Identification notes (Purāṇas):** Distinct from Kaśyapa as a member of the Saptarṣi: here he is one of the four never-setting tail stars immediately preceding Dhruva (Viṣṇu P. 2.12.34), and one of the five who circumambulate Dhruva in Bhāgavata 5.23.1. His position next to Dhruva has led several modern writers to propose him as a former pole star. WARNING: Wilson's note 7 to VP 2.12 suggests 'in Kaśyapa we have a verbal affinity to Cassiopeia' — this is 19th-century sound-alike speculation with no textual or commentarial basis and should not be recorded as an identification.</sub>

### मरीचि (पुच्छे) (Marīci (in the tail)) — a fifth circumpolar star in the Śiśumāra's tail

**Modern identification:** a fifth circumpolar star in the Śiśumāra's tail — —, Draco / Ursa Minor region (*disputed*)

*See also:* `shishumara`, `marichi`

**Vāyu Purāṇa 52.95; Brahmāṇḍa Purāṇa 1,23.104 (absent from Viṣṇu Purāṇa 2.12.34)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/वायुपुराणम्/पूर्वार्धम्/अध्यायः_५२)

> पुच्छेऽग्निश्च महेन्द्रश्च मरीचिः कश्यपो ध्रुवः। तारकाः शिशुमारश्च नास्तमेति चतुष्टयम् ।। ५२.९५ ।।
>
> — *In the tail are Agni and Mahendra and Marīci, Kaśyapa, Dhruva; four of the Śiśumāra's stars do not set.*
> <br>— Literal rendering by the compiler ([source](https://sa.wikisource.org/wiki/वायुपुराणम्/पूर्वार्धम्/अध्यायः_५२))

<sub>**Identification notes (Purāṇas):** A recension-specific addition worth recording: Vāyu 52.95 and Brahmāṇḍa 1,23.104 insert Marīci into the tail-list (Agni, Mahendra, Marīci, Kaśyapa, Dhruva) where Viṣṇu P. 2.12.34 has only four names. Since the very next line still says only FOUR stars never set, the five-name list is in tension with its own following verse — evidence of textual growth. Distinct from Marīci as a Saptarṣi (Alkaid).</sub>

### उत्तानपाद (Uttānapāda) — the upper jaw of the Śiśumāra

**Modern identification:** the upper jaw of the Śiśumāra — —, Draco (head region) on the Draco identification (*disputed*)

*See also:* `shishumara`, `agastya`

**Viṣṇu Purāṇa 2.12.31; Vāyu Purāṇa 52.92; Matsya Purāṇa 127.22; Brahmāṇḍa Purāṇa 1,23.102** — [Sanskrit e-text](https://sa.wikisource.org/wiki/विष्णुपुराणम्/द्वितीयांशः/अध्यायः_१२)

> उत्तानपादस्तस्याधो विज्ञेयो ह्युत्तरो हनुः । यज्ञोऽधरश्च विज्ञेयो धर्मो मूर्द्धानमाश्रितः ॥ ३१ ॥
>
> — *Uttánapáda is to be considered as its upper jaw; Sacrifice as its lower. Dharma is situated on its brow; Náráyańa in its heart.*
> <br>— H.H. Wilson (1840; public domain) ([source](https://www.sacred-texts.com/hin/vp/vp070.htm))

<sub>**Identification notes (Purāṇas):** A genuine sky-position term, distinct from Uttānapāda as Dhruva's father in the narrative. NOTE THE CONFLICT: the older recension puts Uttānapāda on the upper jaw, whereas Bhāgavata 5.23.7 puts Agasti (Canopus) there — the two Śiśumāra traditions are not reconcilable at this point, which is itself evidence that the Bhāgavata reworked an inherited figure.</sub>

### यज्ञ, धर्म, वरुण, अर्यमा, संवत्सर, मित्र (Yajña, Dharma, Varuṇa, Aryaman, Saṃvatsara, Mitra) — six further body-positions of the Śiśumāra: lower jaw, head, the two hind thighs, the sexual organ, the anus

**Modern identification:** six further body-positions of the Śiśumāra: lower jaw, head, the two hind thighs, the sexual organ, the anus — —, Draco / Ursa Minor region on the Draco identification (*disputed*)

*See also:* `shishumara`

**Viṣṇu Purāṇa 2.12.31-33; Vāyu Purāṇa 52.92-94; Matsya Purāṇa 127.22-24; Brahmāṇḍa Purāṇa 1,23.102-104** — [Sanskrit e-text](https://sa.wikisource.org/wiki/विष्णुपुराणम्/द्वितीयांशः/अध्यायः_१२)

> हृदि नारायणश्चास्ते अश्विनौ पूर्वपादयोः । वरुणश्चार्यमा चैव पश्चिमे तस्य सक्थिनी ॥ ३२ ॥ शिश्नः संवत्सरस्तस्य मित्रोऽपानं समाश्रितः ॥ ३३ ॥
>
> — *The Áswins are its two fore feet; and Varuńa and Áryamat its two hinder legs. Samvatsara is its sexual organ; Mitra its organ of excretion.*
> <br>— H.H. Wilson (1840; public domain) ([source](https://www.sacred-texts.com/hin/vp/vp070.htm))

<sub>**Identification notes (Purāṇas):** Grouped because they share a single source-passage and an identical evidential status: each is a NAMED position on the star-figure, but no Purāṇa assigns any of them a visible star, and the older recension's figure has only fourteen stars for far more than fourteen named positions. Dharma also appears independently in the Bhāgavata's tail-group (5.23.5), where it is a different position on a different version of the figure. Any star-by-star mapping of these is reconstruction, not text.</sub>

### यम (अधराहनौ) (Yama (on the lower jaw)) — a star on the lower jaw of the Śiśumāra, opposite Agasti

**Modern identification:** a star on the lower jaw of the Śiśumāra, opposite Agasti — —, far southern sky, if paired with Canopus (*disputed*)

*See also:* `shishumara`, `agastya`

**Bhāgavata Purāṇa 5.23.7** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/3_purana/bhagp/bhp_05u.htm)

> उत्तराहनावगस्तिरधराहनौ यमो मुखेषु चाङ्गारक: शनैश्चर उपस्थे बृहस्पति: ककुदि वक्षस्यादित्यो हृदये नारायणो मनसि चन्द्रो नाभ्यामुशना स्तनयोरश्विनौ बुध: प्राणापानयो राहुर्गले केतव: सर्वाङ्गेषु रोमसु सर्वे तारागणा: ॥ ७ ॥
>
> — *And on the upper jaw of the Sisumara is Agastya, and on its lower jaw is Yama.*
> <br>— J.M. Sanyal (1930s; public domain) ([source](https://archive.org/details/in.ernet.dli.2015.187346))

<sub>**Identification notes (Purāṇas):** Bhāgavata 5.23.7 pairs Yama on the lower jaw directly against Agasti (Canopus) on the upper. Since Agastya is securely Canopus and the two jaws are adjacent, a southern-sky star is implied, but the text names none and no reliable identification was found. Yama as an asterism-deity (of Bharaṇī) is a separate usage; this is a distinct sky-position.</sub>

### प्रजापति (पुच्छे) (Prajāpati (in the tail)) — a CIRCUMPOLAR star on the Śiśumāra's tail — not the ecliptic Prajāpati

**Modern identification:** a CIRCUMPOLAR star on the Śiśumāra's tail — not the ecliptic Prajāpati — —, Draco / Ursa Minor region (*disputed*)

*See also:* `shishumara`, `prajapati`

**Bhāgavata Purāṇa 5.23.5 (and 5.23.1)** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/3_purana/bhagp/bhp_05u.htm)

> यस्य पुच्छाग्रेऽवाक्‌शिरस: कुण्डलीभूतदेहस्य ध्रुव उपकल्पितस्तस्य लाङ्गूले प्रजापतिरग्निरिन्द्रो धर्म इति ... ॥ ५ ॥
>
> — *Under the ends of the Sisumara's tail are Prajapati, Agni, Indra and Dharma.*
> <br>— J.M. Sanyal (1930s; public domain) ([source](https://archive.org/details/in.ernet.dli.2015.187346))

<sub>**Identification notes (Purāṇas):** Flagged because the referent differs from the Sūrya Siddhānta's Prajāpati already in this database. That one is the Rohiṇī-pursuer near Orion/Auriga (δ Aurigae per Burgess). The Prajāpati of Bhāgavata 5.23.1 and 5.23.5 is one of the five stars circumambulating Dhruva and sits on the tail of the Śiśumāra — necessarily circumpolar, hence a different star. Some modern writers make it a former pole star. Kept as a distinct sense rather than merged.</sub>

### सुनीति (Sunīti) — a star beside Dhruva — Dhruva's mother, placed as a star near the pole

**Modern identification:** a star beside Dhruva — Dhruva's mother, placed as a star near the pole — —, Ursa Minor / circumpolar (*disputed*)

*See also:* `dhruva`, `arundhati`

**Viṣṇu Purāṇa 1.12.94** — [Sanskrit e-text](https://sa.wikisource.org/wiki/विष्णुपुराणम्/प्रथमांशः/अध्यायः_१२)

> सुनीतिरपि ते माता त्वदासन्नातिनिर्मला । विमाने तारका भूत्वा तावत्कालं निवत्स्यति ॥ १,१२.९४ ॥
>
> — *Thy mother Suníti, in the orb of a bright star, shall abide near thee for a similar term.*
> <br>— H.H. Wilson (1840; public domain) ([source](https://www.sacred-texts.com/hin/vp/vp047.htm))

<sub>**Identification notes (Purāṇas):** An obscure but real Purāṇic star: the mūla says only that Sunīti 'shall become a star (tārakā) in a vimāna and dwell near thee' — a stellar apotheosis exactly parallel to Arundhatī's beside Vasiṣṭha. Wilson's note 8 to VP 1.12 records the commentator's identification of her with a specific star at the pole, but the mūla itself names none. A companion of Polaris is structurally attractive but this is inference; the name is recorded, not an identification.</sub>

## Star-roads (vīthī) and belts (mārga)

The Purāṇic road-system: three great belts (Airāvata, Jaradgava, Vaiśvānara), each holding three vīthīs of three nakshatras — 27 in all. On the chart each road is drawn as a dashed line through its own nakshatras. Matsya 124 is the only full source and it contradicts itself twice, which the entries record.

### नागवीथी (Nāgavīthī) — the Serpent-road, northernmost of the nine star-roads

**Modern identification:** the Serpent-road, northernmost of the nine star-roads — —, Aries and Taurus (Aśvinī, Bharaṇī, Kṛttikā) (*likely*)

*See also:* `margas`, `pitryana-devayana`

**Viṣṇu Purāṇa 2.8.90; Matsya Purāṇa 124.54; Vāyu Purāṇa 50.130; Brahmāṇḍa Purāṇa 1,21.77** — [Sanskrit e-text](https://sa.wikisource.org/wiki/विष्णुपुराणम्/द्वितीयांशः/अध्यायः_८)

> नागावीथ्युत्तरं यच्च सप्तर्षिभ्यश्च दक्षिणम् । उत्तरः सवितुः पंथा देवयानश्च स स्मृतः ॥ ९० ॥ — cf. मत्स्य १२४.५४: अश्विनीकृत्तिकायाम्या नागवीथ्यस्त्रयः स्मृताः।
>
> — *The path of the gods lies to the north of the solar sphere, north of the Nágavithi, and south of the seven Rishis.*
> <br>— H.H. Wilson (1840; public domain) ([source](https://www.sacred-texts.com/hin/vp/vp066.htm))

<sub>**Identification notes (Purāṇas):** Matsya 124.54 states its three asterisms: Aśvinī, Kṛttikā, and yāmyā (= Bharaṇī, whose deity is Yama). Wilson's note 23 to VP 2.8 gives the same: 'The stars of the Nágavíthi are those of Aries and Taurus.' In Viṣṇu P. 2.8.90 it is a latitude marker: the Devayāna lies north of Nāgavīthī and south of the Saptarṣis. Homonym caution: Nāgavīthī is also a woman in the genealogies (daughter of Yāmī) at VP 1.15.107 — the star-road personified.</sub>

### गजवीथी (Gajavīthī) — the Elephant-road

**Modern identification:** the Elephant-road — —, Taurus/Orion (Rohiṇī, Ārdrā, Mṛgaśiras) (*likely*)

*See also:* `margas`

**Matsya Purāṇa 124.55 (transmitted as nāgavīthī, emend to gajavīthī); named in Wilson's note 21 to Viṣṇu Purāṇa 2.8** — [Sanskrit e-text](https://sa.wikisource.org/wiki/मत्स्यपुराणम्/अध्यायः_१२४)

> रोहिण्यार्द्रा मृगशिरो नागवीथिरिति स्मृता। [transmitted reading; emend नागवीथिः → गजवीथिः]
>
> — *...those of the northern portion are termed Nágavithi, Gajavíthi, and Airávati...*
> <br>— H.H. Wilson (1840; public domain), note 21 to VP 2.8 ([source](https://www.sacred-texts.com/hin/vp/vp066.htm))

<sub>**Identification notes (Purāṇas):** The second vīthī of the northern (Airāvata) mārga. TEXTUAL PROBLEM: Matsya 124.55 as transmitted reads nāgavīthī for this road, repeating the previous name — certainly corrupt for Gajavīthī. Both witnesses checked (GRETIL's Chaukhamba text and sa.wikisource) share the error, so it is old; the 1916 translator flags it, noting the text Wilson quoted should read Gajavīthī. Wilson's own note 21 to VP 2.8 lists Gajavíthi among the nine.</sub>

### ऐरावती (Airāvatī) — the road of Airāvata

**Modern identification:** the road of Airāvata — —, Cancer/Gemini (Puṣya, Āśleṣā, Punarvasu) (*likely*)

*See also:* `margas`

**Matsya Purāṇa 124.55** — [Sanskrit e-text](https://sa.wikisource.org/wiki/मत्स्यपुराणम्/अध्यायः_१२४)

> पुष्याश्लेषा पुनर्वस्वोर्वीथी चैरावती स्मृता।। १२४.५४ ।।
>
> — *Puṣya, Āśleṣā and Punarvasu — that road is remembered as Airāvatī.*
> <br>— Literal rendering by the compiler (the 1916 public-domain Matsya OCR is too corrupt to quote here) ([source](https://archive.org/details/in.ernet.dli.2015.274264))

<sub>**Identification notes (Purāṇas):** Third vīthī of the northern mārga. Matsya 124.55 states the three asterisms explicitly. Homonym caution: Airāvatī is also a river name in Matsya 114.21 and 115.19, and Airāvata elsewhere is Indra's elephant.</sub>

### आर्षभी (Ārṣabhī) — the Bull-road

**Modern identification:** the Bull-road — —, Leo (Pūrva- and Uttara-phalgunī, Maghā) (*likely*)

*See also:* `margas`

**Matsya Purāṇa 124.56** — [Sanskrit e-text](https://sa.wikisource.org/wiki/मत्स्यपुराणम्/अध्यायः_१२४)

> पूर्वउत्तरफल्गुन्यौ मघा चैवार्षभी भवेत्।। १२४.५५ ।।
>
> — *Pūrva- and Uttara-phalgunī and Maghā — that would be Ārṣabhī.*
> <br>— Literal rendering by the compiler ([source](https://archive.org/details/in.ernet.dli.2015.274264))

<sub>**Identification notes (Purāṇas):** First vīthī of the middle (Jaradgava) mārga, per Matsya 124.56.</sub>

### गोवीथी (Govīthī) — the Cow-road

**Modern identification:** the Cow-road — —, Pegasus/Pisces (Pūrva- and Uttara-proṣṭhapadā, Revatī) (*disputed*)

*See also:* `margas`

**Matsya Purāṇa 124.57** — [Sanskrit e-text](https://sa.wikisource.org/wiki/मत्स्यपुराणम्/अध्यायः_१२४)

> पूर्वोत्तरप्रोष्ठपदौ गोवीथी रेवती स्मृता।। १२४.५६ ।।
>
> — *Pūrva- and Uttara-proṣṭhapadā and Revatī are remembered as Govīthī.*
> <br>— Literal rendering by the compiler ([source](https://archive.org/details/in.ernet.dli.2015.274264))

<sub>**Identification notes (Purāṇas):** Matsya 124.57 assigns it Pūrva/Uttara-proṣṭhapadā and Revatī. But Varāhamihira's Bṛhat Saṃhitā 9 makes Govīthī = Hasta, Citrā, Svāti — a substantive Purāṇa-vs-Siddhānta divergence, not a scribal one. Both readings recorded.</sub>

### जरद्गव / जारद्गवी (Jaradgava / Jāradgavī) — the Old-Ox road

**Modern identification:** the Old-Ox road — —, Aquila/Delphinus/Aquarius (Śravaṇa, Dhaniṣṭhā, Vāruṇa = Śatabhiṣaj) (*disputed*)

*See also:* `margas`

**Matsya Purāṇa 124.52 (as mārga) and 124.57 (as vīthī)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/मत्स्यपुराणम्/अध्यायः_१२४)

> श्रवणञ्च धनिष्ठा च वारुणञ्च जरद्‌गवम्।। १२४.५६ ।।
>
> — *Śravaṇa and Dhaniṣṭhā and Vāruṇa — that is Jaradgava.*
> <br>— Literal rendering by the compiler ([source](https://archive.org/details/in.ernet.dli.2015.274264))

<sub>**Identification notes (Purāṇas):** The name does double duty: Jaradgava is both the MIDDLE of the three great mārgas and the third vīthī within it (Matsya 124.57). Bṛhat Saṃhitā 9 instead makes Jāradgavī = Viśākhā, Anurādhā, Jyeṣṭhā. Note vāruṇa here is the asterism whose deity is Varuṇa, i.e. Śatabhiṣaj.</sub>

### अजवीथी (Ajavīthī) — the Goat-road — a three-nakṣatra segment of the ecliptic belt

**Modern identification:** the Goat-road — a three-nakṣatra segment of the ecliptic belt — —, Scorpius–Sagittarius (Mūla + both Aṣāḍhās) on one reading; Corvus–Virgo–Boötes (Hasta, Citrā, Svāti) on the other (*disputed*)

*See also:* `vaishvanari`, `margas`, `pitryana-devayana`

**Bhāgavata Purāṇa 5.23.5; Viṣṇu Purāṇa 2.8.85; Matsya Purāṇa 124.53 and 124.58; Vāyu Purāṇa 50.130; Brahmāṇḍa Purāṇa 1,21.76** — [Sanskrit e-text](https://sa.wikisource.org/wiki/विष्णुपुराणम्/द्वितीयांशः/अध्यायः_८)

> उत्तरं [य]दगस्त्यस्य अजवीथ्याश्च दक्षिणम् । पितृयानः स वै पन्था वैश्वानरपथाद्बहिः ॥ ८५ ॥ — cf. मत्स्य १२४.५८: हस्त चित्रा तथा स्वाती ह्यजवीथिरितिस्मृता।
>
> — *On the north of Agastya, and south of the line of the Goat, exterior to the Vaiswánara path, lies the road of the Pitris.*
> <br>— H.H. Wilson (1840; public domain) ([source](https://www.sacred-texts.com/hin/vp/vp066.htm))

<sub>**Identification notes (Purāṇas):** A star-road, not a star. Brahmāṇḍa 2.21.76 & 159, Matsya 124.53 and Viṣṇu P. 2.8.85 make it Mūla, Pūrvāṣāḍhā, Uttarāṣāḍhā — part of the Pitṛyāṇa. But Matsya 124.58, in the SAME chapter, makes it Hasta, Citrā, Svāti and reassigns Mūla + Aṣāḍhās to Vaiśvānarī. The 1916 translator flags 124.53/58 as corrupt and his rendering as 'tentative only'. Varāhamihira's Bṛhat Saṃhitā 9 gives yet another arrangement — a genuine Purāṇa-vs-Siddhānta divergence, not a copying slip. In Bhāgavata 5.23.5 it is placed on the back (pṛṣṭha) of the Śiśumāra.</sub>

### मृगवीथी (Mṛgavīthī) — the Deer-road

**Modern identification:** the Deer-road — —, Libra/Scorpius (Jyeṣṭhā, Viśākhā, Maitra = Anurādhā) (*likely*)

*See also:* `margas`

**Matsya Purāṇa 124.59** — [Sanskrit e-text](https://sa.wikisource.org/wiki/मत्स्यपुराणम्/अध्यायः_१२४)

> ज्येष्ठा विशाखा मैत्रञ्च मृगवीथी तथोच्यते।। १२४.५८ ।।
>
> — *Jyeṣṭhā, Viśākhā and Maitra — that is called Mṛgavīthī.*
> <br>— Literal rendering by the compiler ([source](https://archive.org/details/in.ernet.dli.2015.274264))

<sub>**Identification notes (Purāṇas):** Second vīthī of the southern (Vaiśvānara) mārga, Matsya 124.59. maitra = the asterism of Mitra, i.e. Anurādhā.</sub>

### वैश्वानरी (Vaiśvānarī) — the road of Vaiśvānara (Fire)

**Modern identification:** the road of Vaiśvānara (Fire) — —, Scorpius/Sagittarius (Mūla, Pūrva- and Uttara-āṣāḍhā) (*disputed*)

*See also:* `ajavithi`, `margas`

**Matsya Purāṇa 124.59** — [Sanskrit e-text](https://sa.wikisource.org/wiki/मत्स्यपुराणम्/अध्यायः_१२४)

> मूलं पूर्वोत्तराषाढ़े वीथी वैश्वानरी भवेत्।। १२४.५८ ।।
>
> — *Mūla and the two Aṣāḍhās — that road would be Vaiśvānarī.*
> <br>— Literal rendering by the compiler ([source](https://archive.org/details/in.ernet.dli.2015.274264))

<sub>**Identification notes (Purāṇas):** Southernmost vīthī, Matsya 124.59. Directly contradicts Matsya 124.53, which gives the same three asterisms to Ajavīthī. The 1916 translator marks both verses corrupt and his rendering 'tentative only'.</sub>

### ऐरावत / जरद्गव / वैश्वानर (मार्गाः) (Airāvata / Jaradgava / Vaiśvānara (the three mārgas)) — the three great celestial belts — northern, middle, southern

**Modern identification:** the three great celestial belts — northern, middle, southern — —, the three latitude-bands of the ecliptic, each subdivided into three vīthīs (*likely*)

*See also:* `nagavithi`, `gajavithi`, `airavati`, `arshabhi`, `govithi`, `jaradgava`, `ajavithi`, `mrigavithi`, `vaishvanari`

**Matsya Purāṇa 124.52; Vaiśvānara-patha also at Viṣṇu Purāṇa 2.8.85 and Vāyu Purāṇa 50.208** — [Sanskrit e-text](https://sa.wikisource.org/wiki/मत्स्यपुराणम्/अध्यायः_१२४)

> स्थानं जरद्‌गवं मध्ये तथैरावतमुत्तरम्। वैश्वानरं दक्षिणतो निर्दिष्टमिह तत्त्वतः।। १२४.५१ ।।
>
> — *...the path (Márga) of the sun and other planets amongst the lunar asterisms is divided into three portions or Avasht́hánas, northern, southern, and central, called severally Airávata, Járadgava (Ajagava, Matsya P.), and Vaiswánara.*
> <br>— H.H. Wilson (1840; public domain), note 21 to VP 2.8 ([source](https://www.sacred-texts.com/hin/vp/vp066.htm))

<sub>**Identification notes (Purāṇas):** The framing structure of the whole system: Airāvata = the northern belt, Jaradgava = the middle, Vaiśvānara = the southern; each contains three vīthīs, three nakṣatras apiece, 27 in all. This is what makes Viṣṇu P. 2.8.85 coherent — the Pitṛyāṇa can be both 'south of Ajavīthī' and 'outside the Vaiśvānara path' because Ajavīthī is a sub-road of the Vaiśvānara belt. Vaiśvānara-patha is thus a real, textually attested Purāṇic sky-region name.</sub>

### पितृयाण / देवयान (Pitṛyāṇa / Devayāna) — the Road of the Fathers / the Road of the Gods — two celestial bands defined by star markers

**Modern identification:** the Road of the Fathers / the Road of the Gods — two celestial bands defined by star markers — —, Pitṛyāṇa: north of Canopus and south of Ajavīthī. Devayāna: north of Nāgavīthī (Aries/Taurus) and south of Ursa Major (*likely*)

*See also:* `agastya`, `ajavithi`, `nagavithi`, `saptarshi`

**Viṣṇu Purāṇa 2.8.85 and 2.8.90; Vāyu Purāṇa 50.208 and 50.216; Matsya Purāṇa 124.97; Brahmāṇḍa Purāṇa 1,21.168-169** — [Sanskrit e-text](https://sa.wikisource.org/wiki/विष्णुपुराणम्/द्वितीयांशः/अध्यायः_८)

> उत्तरं [य]दगस्त्यस्य अजवीथ्याश्च दक्षिणम् । पितृयानः स वै पन्था वैश्वानरपथाद्बहिः ॥ ८५ ॥
>
> — *On the north of Agastya, and south of the line of the Goat, exterior to the Vaiswánara path, lies the road of the Pitris. / The path of the gods lies to the north of the solar sphere, north of the Nágavithi, and south of the seven Rishis.*
> <br>— H.H. Wilson (1840; public domain) ([source](https://www.sacred-texts.com/hin/vp/vp066.htm))

<sub>**Identification notes (Purāṇas):** Valuable for a star database because these are defined ASTRONOMICALLY, by named stellar boundary markers rather than by myth: Agastya (Canopus) and Ajavīthī bound the Pitṛyāṇa; Nāgavīthī and the Saptarṣis bound the Devayāna. Attested identically in three recensions.</sub>

## The Milky Way

Three Purāṇic names for the galactic band. On the chart they are attached to the galactic equator, computed from the J2000 galactic pole.

### आकाशगङ्गा (Ākāśagaṅgā) — the Milky Way (lit. 'sky-Ganges')

**Modern identification:** the Milky Way (lit. 'sky-Ganges') — —, the galactic band (*likely*)

*See also:* `chayapatha`, `tripathaga`, `shishumara`

**Bhāgavata Purāṇa 5.23.5 (Milky Way sense); contrast Viṣṇu Purāṇa 2.9.12, 2.9.14, 2.9.17 (celestial rain-water sense)** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/3_purana/bhagp/bhp_05u.htm)

> पृष्ठे त्वजवीथी आकाशगङ्गा चोदरत: ॥ ५ ॥
>
> — *...and on the back of the Sisumara is the fore part of its right side, and in its womb is the celestial Ganges.*
> <br>— J.M. Sanyal (1930s; public domain). Note that Sanyal renders udarataḥ 'in its womb' and does not recognise Ajavīthī as a name. ([source](https://archive.org/details/in.ernet.dli.2015.187346))

<sub>**Identification notes (Purāṇas):** In Bhāgavata 5.23.5 it lies on the belly (udara) of the Śiśumāra, placed among star-positions alongside Ajavīthī — that context makes the Milky Way reading secure. IMPORTANT CONTRAST: in Viṣṇu P. 2.9.12, 2.9.14 and 2.9.17 the same word means something else entirely — the celestial water that falls from a cloudless sky, a bath in which is 'divya snāna'. So the Milky-Way sense is specifically the Bhāgavata's. The Vāyu/Brahmāṇḍa/Matsya group does not use the word for the sky at all; its Milky Way term is chāyāpatha.</sub>

### छायापथ (Chāyāpatha) — the Milky Way (lit. 'the shadow-path')

**Modern identification:** the Milky Way (lit. 'the shadow-path') — —, the galactic band (*certain*)

*See also:* `akashaganga`, `tripathaga`

**Vāyu Purāṇa 47.28; Brahmāṇḍa Purāṇa 1,18.29; Matsya Purāṇa 121.29** — [Sanskrit e-text](https://sa.wikisource.org/wiki/वायुपुराणम्/पूर्वार्धम्/अध्यायः_४७)

> दिविच्छायापथो यस्तु अनुनक्षत्रमण्डलम् । दृश्यते भास्वरो रात्रौ देवी त्रिपथगा तु सा ।। ४७.२८ ।।
>
> — *The shadow-path in the sky that runs along the circle of the nakṣatras, seen shining at night — she is the goddess Tripathagā.*
> <br>— Literal rendering by the compiler; no public-domain published translation of this verse was located ([source](https://sa.wikisource.org/wiki/वायुपुराणम्/पूर्वार्धम्/अध्यायः_४७))

<sub>**Identification notes (Purāṇas):** The clearest, least ambiguous Milky Way attestation in the whole Purāṇic corpus, and the term the Vāyu/Brahmāṇḍa/Matsya group actually uses: 'the shadow-path in the sky that runs ALONG THE CIRCLE OF THE NAKṢATRAS, seen shining at night — that is the goddess Tripathagā.' Three independent witnesses. The description (a luminous band following the asterism-circle, visible at night) admits no other referent.</sub>

### त्रिपथगा (Tripathagā) — the Milky Way, as the 'three-path-goer' (the Gaṅgā of the three worlds)

**Modern identification:** the Milky Way, as the 'three-path-goer' (the Gaṅgā of the three worlds) — —, the galactic band (*certain*)

*See also:* `akashaganga`, `chayapatha`

**Vāyu Purāṇa 47.28; Brahmāṇḍa Purāṇa 1,18.29; Matsya Purāṇa 121.29-30** — [Sanskrit e-text](https://sa.wikisource.org/wiki/वायुपुराणम्/पूर्वार्धम्/अध्यायः_४७)

> दिविच्छायापथो यस्तु अनुनक्षत्रमण्डलम् । दृश्यते भास्वरो रात्रौ देवी त्रिपथगा तु सा ।। ४७.२८ ।।
>
> — *...seen shining at night — she is the goddess Tripathagā.*
> <br>— Literal rendering by the compiler ([source](https://sa.wikisource.org/wiki/वायुपुराणम्/पूर्वार्धम्/अध्यायः_४७))

<sub>**Identification notes (Purāṇas):** Not a separate object but the identification supplied by the same verse: the chāyāpatha IS Tripathagā, i.e. the celestial Gaṅgā. This is the Purāṇic equation of the Milky Way with the sky-river, stated rather than inferred. Distinct from Mandākinī, which in these same texts is always a terrestrial Himalayan river and never a sky-object.</sub>

### मन्दाकिनी (Mandākinī) — Milky Way

**Modern identification:** Milky Way — —, — (*likely*)

*See also:* `akashaganga`, `chayapatha`, `tripathaga`, `viyadganga`, `svarnadi`, `suradirghika`

**Amarakośa 1.1.116 (Svarga-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> मन्दाकिनी वियद्गङ्गा स्वर्णदी सुरदीर्घिका ॥ १.१.११६ ॥
>
> — *'The river of heaven.' Footnote: 'The Ganges of the sky, suggested probably by the milky-way.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** First of four synonyms Amarasiṃha gives for the celestial river. Colebrooke's own footnote reads that this is 'The Ganges of the sky, suggested probably by the milky-way' — the equation is explicit in the earliest public-domain scholarship on the text. NOTE the contrast with the Purāṇic layer already on file, where Mandākinī is always a terrestrial Himalayan river and the Milky Way word is chāyāpatha.</sub>

### वियद्गङ्गा (Viyadgaṅgā) — Milky Way

**Modern identification:** Milky Way — —, — (*likely*)

*See also:* `mandakini`, `akashaganga`

**Amarakośa 1.1.116 (Svarga-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> मन्दाकिनी वियद्गङ्गा स्वर्णदी सुरदीर्घिका ॥ १.१.११६ ॥
>
> — *'The river of heaven.' Footnote: 'The Ganges of the sky, suggested probably by the milky-way.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** 'Ganges of the firmament' (viyat). Second synonym in the same verse. Note the form is viyad-, not the vyoma- that secondary literature often reports.</sub>

### स्वर्णदी (Svarnadī) — Milky Way

**Modern identification:** Milky Way — —, — (*likely*)

*See also:* `mandakini`, `akashaganga`

**Amarakośa 1.1.116 (Svarga-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> मन्दाकिनी वियद्गङ्गा स्वर्णदी सुरदीर्घिका ॥ १.१.११६ ॥
>
> — *'The river of heaven.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** 'River of heaven'. Third synonym in the same verse. The correct segmentation is svar+nadī ('heaven-river'), not svarṇa+dī ('gold-').</sub>

### सुरदीर्घिका (Suradīrghikā) — Milky Way

**Modern identification:** Milky Way — —, — (*disputed*)

*See also:* `mandakini`, `akashaganga`

**Amarakośa 1.1.116 (Svarga-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> मन्दाकिनी वियद्गङ्गा स्वर्णदी सुरदीर्घिका ॥ १.१.११६ ॥
>
> — *'The river of heaven.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** 'The gods' long water-course'. Fourth synonym in the same verse, and the one whose astronomical reference is weakest — it need mean no more than a celestial watercourse in the abstract.</sub>

## Sky-regions and mechanisms

Named zones and the machinery of rotation — not stars, and not plottable as points.

### विष्णुपद (Viṣṇupada) — 'the step of Viṣṇu' — the third and highest region of the sky, where Dhruva stands

**Modern identification:** 'the step of Viṣṇu' — the third and highest region of the sky, where Dhruva stands — —, the circumpolar region (*disputed*)

*See also:* `dhruva`, `saptarshi`

**Viṣṇu Purāṇa 2.8.98; Matsya Purāṇa 124.112; Brahmāṇḍa Purāṇa 1,21.176; Vāyu Purāṇa 50.221** — [Sanskrit e-text](https://sa.wikisource.org/wiki/विष्णुपुराणम्/द्वितीयांशः/अध्यायः_८)

> ऊर्ध्वोत्तरमृषिभ्यस्तु ध्रुवो यत्र व्यवस्थितः । एतद्विष्णुपदं दिव्यं तृतीयं व्योम्नि भासुरम् ॥ ९८ ॥
>
> — *The space between the seven Rishis and Dhruva, the third region of the sky, is the splendid celestial path of Vishńu (Vishńupada).*
> <br>— H.H. Wilson (1840; public domain) ([source](https://www.sacred-texts.com/hin/vp/vp066.htm))

<sub>**Identification notes (Purāṇas):** A named sky-REGION rather than a star: the zone above the Saptarṣis (Ursa Major) containing the pole. Attested in four recensions in near-identical wording. Homonym caution: Viṣṇupada is also a lake on Mt. Niṣadha (Matsya 121, Brahmāṇḍa 1,18.67).</sub>

**Amarakośa 1.2.169 (Vyoma-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> वियद्विष्णुपदं वा तु पुंस्याकाशविहायसी ॥ १.२.१६९ ॥
>
> — *Listed by Colebrooke under 'The sky'.*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** IMPORTANT CORRECTIVE to the Purāṇic entry already on file: in the classical thesaurus viṣṇupada is simply a synonym of vyoman / ākāśa, 'the sky', not the circumpolar station the Purāṇas make of it. The lexicon therefore does NOT support treating Viṣṇupada as a star or a specific sky-region.</sub>

### मेढी / मेढीभूत (Meḍhī / Meḍhībhūta) — 'the threshing-post' — the celestial pole as the pivot to which the sky is tethered

**Modern identification:** 'the threshing-post' — the celestial pole as the pivot to which the sky is tethered — —, the north celestial pole (*certain*)

*See also:* `dhruva`

**Bhāgavata Purāṇa 5.23.3; Matsya Purāṇa 125.5 and 127.27; Brahmāṇḍa Purāṇa 1,22.6 and 1,23.106; Vāyu Purāṇa 52.97; cf. Viṣṇu Purāṇa 2.7.10** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/3_purana/bhagp/bhp_05u.htm)

> यथा मेढीस्तम्भ आक्रमणपशव: संयोजितास्त्रिभिस्त्रिभि: सवनैर्यथास्थानं मण्डलानि चरन्त्येवं भगणा ग्रहादय एतस्मिन्नन्तर्बहिर्योगेन कालचक्र आयोजिता ध्रुवमेवावलम्ब्य ... ॥ ३ ॥
>
> — *Just as oxes, fastened to a post fixed in the centre of a threshing floor, leaving their own station, go round at shorter, middle or longer distances, — similarly fixed on the inside and outside of the circle of time, stars and planets exist, supporting themselves, on Dhruva.*
> <br>— J.M. Sanyal (1930s; public domain); cf. Wilson on VP 2.7.10: 'Dhruva (the pole-star), the pivot or axis of the whole planetary circle.' ([source](https://archive.org/details/in.ernet.dli.2015.187346))

<sub>**Identification notes (Purāṇas):** A technical term for the pole, built on a vivid agricultural image: as oxen tied to a central post tread out grain in circles, so the stars circle Dhruva. Bhāgavata 5.23.3 develops the simile at length (meḍhīstambha, 'the post', with the ākramaṇa-paśavaḥ, treading cattle); the Matsya/Brahmāṇḍa/Vāyu group uses meḍhībhūta as an epithet of Dhruva directly.</sub>

### प्रवह (Pravaha) — the wind that carries the stars around the pole

**Modern identification:** the wind that carries the stars around the pole — —, — (*certain*)

**Viṣṇu Purāṇa 2.12.28; Matsya Purāṇa 127.18; Brahmāṇḍa Purāṇa 1,23.98; Vāyu Purāṇa 52.89; Kūrma Purāṇa 1,41.27** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/3_purana/vipce_pu.htm)

> *(IAST — the e-text carries no Devanagari copy)*
>
> yasmāj jyotīṃṣi vahati pravahas tena sa smṛtaḥ // ViP_2,12.28 //
>
> — *The air, which is called Pravaha, is so termed because it bears along the planets, which turn round, like a disc of fire, driven by the aerial wheel.*
> <br>— H.H. Wilson (1840; public domain) ([source](https://www.sacred-texts.com/hin/vp/vp070.htm))

<sub>**Identification notes (Purāṇas):** Not a star but the named mechanism of diurnal rotation, and the text supplies its own etymology: 'because it bears (vahati) the lights, it is called Pravaha.' Included because it is the Purāṇic term for what modern astronomy calls the apparent rotation of the celestial sphere.</sub>

### तारापथः (Tārāpatha) — the firmament ('star-road')

**Modern identification:** the firmament ('star-road') — —, — (*certain*)

*See also:* `chayapatha`

**Amarakośa 1.2.171 (Vyoma-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> तारापथोऽन्तरिक्षं च मेघाध्वा च महाबिलम् ॥ १.२.१७१ ॥
>
> — *Listed by Colebrooke under 'The sky' (Book I, Ch. I, Sect. II).*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** NOT a star: the Vyoma-varga lists tārāpatha among synonyms of the sky, alongside antarikṣa, meghādhvan and mahābila. Recorded because it is the lexicon's own term for the star-bearing region, and because it is easily confused with the Milky-Way words Chāyāpatha and Tripathagā already on file.</sub>

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

**Brāhmasphuṭasiddhānta, Bhagrahayutyadhikāra 3–9; Pañcasiddhāntikā XIV.34–38** — [Sanskrit e-text](https://archive.org/download/Brahmasphutasiddhanta/Brahmasphutasiddhanta_djvu.txt)

> सौम्या दशकं विषया याम्याः शरदशभवा रसाः सौम्याः । खं सप्तदक्षिणाः खं सौम्याः सूर्यत्रयोदशकाः ॥ ५ ॥ दक्षिणतो भवयमलाः सप्तत्रिंशदुदगंशका याम्याम् । अध्यर्धत्रिचतुष्कार्धनवमसप्त्यंशविषयशराः ॥ ६ ॥
>
> — *No public-domain translation of the BSS chapter exists; these verses encode the polar latitudes of the 27 junction-stars in bhūtasaṅkhyā word-numerals with the direction attached (saumya = north, yāmya = south). For the Pañcasiddhāntikā, Thibaut renders XIV.34–37: '34. (The junction-star) of krittika is at the end of the sixth degree (of the nakshatra), and three and a half hastas to the north of the ecliptic; that of Rohiṇī is at the end of the eighth degree, and five and a half hastas to the south... 37. Of Chitrā (the yogatara is) at seven and a half degrees, three hastas to the south.'*
> <br>— Paraphrase by the compiler for the BSS; G. Thibaut & Sudhakara Dvivedi (1889) for the Pañcasiddhāntikā ([source](https://archive.org/download/wg1078/WG1078-1889%20-The%20Panchasiddhantika%20-%20The%20Astronomical%20Work%20Of%20Varaha%20Mihira_djvu.txt))

<sub>**Identification notes (Later siddhāntas & al-Bīrūnī):** THIS IS THE TABLE BHĀSKARA COPIED — and the edition's commentary says so outright: 'these very dhruvāṃśas of Aśvinī and the rest were read out by Bhāskara too, in his own Bhagrahayutyadhikāra.' BSS 10.3–4 give the polar longitudes as degrees within a sign (Aśvinī 8° Aries, Bharaṇī 20° Aries, Kṛttikā 8° Taurus less 32', Rohiṇī 20° Taurus less 32', Mṛgaśīrṣa 13° Gemini, Ārdrā 7° Gemini, Punarvasu 3° Cancer, Puṣya 16° Cancer, Āśleṣā 18° Cancer, Maghā 9° Leo, P. Phalgunī 27° Leo, U. Phalgunī 5° Virgo, Hasta 20° Virgo, Citrā 3° Libra, Svātī 19° Libra…); 10.5–7 give the latitudes and 10.8–9 the minute-corrections. Only 27 are tabulated. Burgess: 'With it, so far as the longitude is concerned, exactly accord the Brahma-Siddhanta, as reported by Colebrooke, and the Khanda-Kataka, as reported by al-Biruni... but the latitudes of the Khanda-Kataka often vary considerably from both.' SEPARATELY, the Pañcasiddhāntikā gives coordinates for only SEVEN yogatārās (XIV.34–37: Kṛttikā, Rohiṇī, Punarvasu, Puṣya, Āśleṣā, Maghā, Citrā), in hastas rather than degrees, and they diverge widely from the Sūrya Siddhānta's; Thibaut: 'Why Varāha Mihira should have confined himself to stating the longitudes and latitudes of seven junction stars only, remains unaccounted for. Possibly the Manuscripts are defective just at that place.'</sub>

### दाक्षायिण्यः (Dākṣāyaṇyaḥ) — the 27 lunar mansions collectively

**Modern identification:** the 27 lunar mansions collectively — —, — (*certain*)

*See also:* `nakshatra-generic`

**Amarakośa 1.3.218 (Dig-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> दाक्षायिण्योऽश्विनीत्यादितारा अश्वयुगश्विनी ॥ १.३.२१८ ॥
>
> — *'Asterisms.' Footnote: 'Aśvinī and others, the longitude of which regulates the divisions of the zodiac. In mythology, they are nymphs, and daughters of Daksha.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** Collective proper name for the whole set of nakshatras — 'the daughters of Dakṣa'. Colebrooke's note ties it directly to the coordinate framework: these are the asterisms 'the longitude of which regulates the divisions of the zodiac'.</sub>

### चित्रशिखण्डिनः (Citraśikhaṇḍinaḥ) — Big Dipper / Great Bear

**Modern identification:** Big Dipper / Great Bear — α–η Ursae Majoris, Ursa Major (*certain*)

*See also:* `saptarshi`, `rksha`

**Amarakośa 1.3.229 (Dig-varga)** — [Sanskrit e-text](https://sa.wikisource.org/wiki/अमरकोशः/प्रथमकाण्डम्)

> सप्तर्षयो मरीच्यत्रिमुखाश्चित्रशिखण्डिनः ॥ १.३.२२९ ॥
>
> — *'Ursa major.' Footnote: 'The seven principal stars in Ursa major are the seven sages; Marichi, Atri, Angiras, Pulastya, Pulaha, Kratu and Vasishthá.'*
> <br>— H.T. Colebrooke (1808) ([source](https://archive.org/download/AmaraKosha/amara_english_colebrook_djvu.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** Second collective name for the Seven Sages, 'the bright-crested ones', given as a straight synonym of Saptarṣayaḥ. Colebrooke glosses the verse 'Ursa major' and names the seven in a footnote. Cross-confirmed internally: six verses earlier the Amarakośa calls Bṛhaspati citraśikhaṇḍija, 'son of a Citraśikhaṇḍin' (i.e. of Aṅgiras, one of the seven).</sub>

### अष्टाविंशतिनक्षत्राणि (Aṣṭāviṃśati-nakṣatrāṇi) — the 28-fold nakshatra circle (Buddhist)

**Modern identification:** the 28-fold nakshatra circle (Buddhist) — —, — (*certain*)

*See also:* `nakshatra-catur-dvarika`

**Śārdūlakarṇāvadāna (Divyāvadāna 33), nakṣatra-vaṃśa, p. 46 (Mukhopadhyaya ed.)** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> kṛttikā rohiṇī mṛgaśirā ārdrā punarvasuḥ puṣyaḥ aśleṣā maghā pūrvaphalgunī uttaraphalgunī hastā citrā svātī viśākhā anurādhā jyeṣṭhā mūlā pūrvāṣāḍhā uttarāṣāḍhā abhijit śravaṇā dhaniṣṭhā śatabhiṣā pūrvabhādrapadā uttarabhādrapadā revatī aśvinī bharaṇī / ity etāni bhoḥ puṣkarasārinn aṣṭāviṃśati-nakṣatrāṇi/
>
> — *Literal rendering: 'Kṛttikā, Rohiṇī, Mṛgaśirā, Ārdrā, Punarvasu, Puṣya, Aśleṣā, Maghā, Pūrvaphalgunī, Uttaraphalgunī, Hastā, Citrā, Svātī, Viśākhā, Anurādhā, Jyeṣṭhā, Mūlā, Pūrvāṣāḍhā, Uttarāṣāḍhā, Abhijit, Śravaṇā, Dhaniṣṭhā, Śatabhiṣā, Pūrvabhādrapadā, Uttarabhādrapadā, Revatī, Aśvinī, Bharaṇī — these, sir Puṣkarasārin, are the twenty-eight nakshatras.'*
> <br>— Literal rendering by the compiler (no public-domain translation of this chapter exists; Cowell & Neil 1886 is an edition without translation) ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_zArdUlakarNAvadAna.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** The Buddhist canonical list, enumerated from Kṛttikā (not Aśvinī) and explicitly counted as 28 with Abhijit included — the same archaic starting-point as the Vedic lists on file. This is the frame for the star-count and figure data that the same chapter supplies for every asterism, and which is recorded on each nakshatra's own entry.</sub>

### चतुर्द्वारिकाणि नक्षत्राणि (Catur-dvārikāṇi nakṣatrāṇi) — the 28 nakshatras in four gate-groups of seven

**Modern identification:** the 28 nakshatras in four gate-groups of seven — —, — (*certain*)

*See also:* `ashtavimshati-nakshatrani`

**Śārdūlakarṇāvadāna (Divyāvadāna 33), pp. 47–52; Mahāmāyūrī-vidyārājñī (Takubo ed. pp. 50–52)** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_mahAmAyUrIvidyArAjJI.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> amīṣāṃ bhoḥ puṣkarasārin saptānāṃ nakṣatrāṇāṃ pūrva-dvārikāṇāṃ kṛttikā prathamā nāmāśleṣā paścimā nāma/ ... dakṣiṇa-dvārikāṇāṃ maghā prathamā nāma viśākhā paścimā nāma/ ... paścimadvārikāṇāṃ ... anurādhā prathamā nāma śravaṇā paścimā nāma/ ... uttara-dvārikāṇāṃ dhaniṣṭhā prathamā nāma bharaṇī paścimā nāma/
>
> — *Literal rendering (Mahāmāyūrī): 'Kṛttikā and Rohiṇī, Mṛgaśiras, Ārdrā, Punarvasu, Puṣya endowed with good fortune, and Aśleṣā is the seventh. These seven asterisms are stationed at the eastern gate; they guard and protect the eastern quarter.' ... 'The twenty-eight asterisms stand seven by seven in the [four] directions.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_mahAmAyUrIvidyArAjJI.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** A structural scheme attested independently in two Buddhist texts: the 28 are divided into four sevens 'stationed at the gates' of the four directions — Kṛttikā–Aśleṣā (east), Maghā–Viśākhā (south), Anurādhā–Śravaṇā (west), Dhaniṣṭhā–Bharaṇī (north). The Mahāmāyūrī makes each seven the guardian of its quarter. Note the boundaries fall between Aśleṣā/Maghā and between Śravaṇā/Dhaniṣṭhā, i.e. near the old solstitial colures — the same division the Vedāṅga Jyotiṣa's Śraviṣṭhā/Sārpa solstices imply.</sub>

### ताराग्रहाः (Tārāgrahāḥ) — the five star-planets

**Modern identification:** the five star-planets — Mercury, Venus, Mars, Jupiter, Saturn, — (*certain*)

*See also:* `tara`

**Mahāmāyūrī-vidyārājñī (Takubo ed. p. 52)** — [Sanskrit e-text](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_mahAmAyUrIvidyArAjJI.txt)

> *(IAST — the e-text carries no Devanagari copy)*
>
> aṣṭāviṃśati nakṣatrāḥ saptasapta diśi sthitāḥ. tārāgrahās tathā pañca rāhuketuś ca saptamaḥ, mahātejo mahābalo maharddhikā mahātapāḥ. sūryacandramasau caiva saptatriṃśad anūnakāḥ,
>
> — *Literal rendering: 'The twenty-eight asterisms stand seven by seven in the directions; likewise the five star-planets, and Rāhu-Ketu as the seventh — of great splendour, great strength, great power, great austerity; and the sun and moon: thirty-seven, none lacking.'*
> <br>— Literal rendering by the compiler ([source](https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_mahAmAyUrIvidyArAjJI.txt))

<sub>**Identification notes (Lexicons, Nirukta & Buddhist):** 'The star-seizers' — the technical term distinguishing the five planets from the luminaries. Recorded because it shows tārā being used of planets as well as fixed stars, a distinction this database should keep explicit. The same passage counts thirty-seven bodies in all: 28 nakshatras + 5 tārāgrahas + Rāhu + Ketu + sun + moon.</sub>

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

### Ṛgveda & Vedāṅga Jyotiṣa

- NEGATIVE FINDING (Ṛgveda, high confidence): an exhaustive programmatic search of the complete Aufrecht Ṛgveda (GRETIL plaintext) returned ZERO occurrences of mṛgaśīrṣa, kṛttikā, viśākhā, āśleṣā, phalgunī, anurādhā, aṣāḍhā, śatabhiṣaj, proṣṭhapadā/bhādrapadā, śraviṣṭhā, abhijit, invakā, nistya, sārpa, saptarṣi, arundhatī, mṛgavyādha, lubdhaka, brahmahṛdaya, and apāṃvatsa. The Ṛgveda names no asterism as Mṛgaśīrṣa or Mṛga.
- NEGATIVE FINDING: Agastya occurs 6 times in the Ṛgveda but ALWAYS as the ṛṣi, never as the star Canopus. Rohiṇī occurs 3 times, always meaning 'red cow(s)'. dhaniṣṭhā occurs once (RV 10.73.1) as the superlative 'most bountiful', not the asterism. The RV's 11 occurrences of nakṣatra are all generic 'stars/constellations' with no individual name.
- NEGATIVE FINDING: RV 10.19.1 (agnīṣomā punarvasū ... revatīḥ) is NOT an asterism reference. Macdonell & Keith: 'Nor do the adjectives revati ("rich") and punarvasu ("bringing wealth again") in another hymn appear to refer to the Naksatras.' Similarly RV 8.101.13 rohiṇyā means 'of ruddy hue'.
- NEGATIVE FINDING: Atharvaveda 19.8 invokes the nakṣatras collectively and gives their number as twenty-eight (अष्टाविंशानि, verse 2) but names no individual asterism. AV 19.9 likewise names none. AV 19.49.2 contains śraviṣṭhāḥ, but Whitney treats it as the superlative adjective, the line is textually corrupt, and it should NOT be recorded as an attestation of the asterism.
- NEGATIVE FINDING: the Vājasaneyi Saṃhitā has no nakshatra list comparable to TS 4.4.10 / MS 2.13.20 / KS 39.13. VS references to nakṣatra (e.g. 18.40) are generic, and the Śukla Yajurveda's asterism list sits in Śatapatha Brāhmaṇa 2.1.2, already on file.
- The Atharvaveda Nakṣatra Kalpa IS findable online — Pariśiṣṭa 1 of the Atharvaveda Pariśiṣṭas (ed. Bolling & von Negelein 1909–10, public domain) on GRETIL. Its names are the standard 28 (Śraviṣṭhā not Dhaniṣṭhā, Proṣṭhapadā not Bhādrapadā, Aśvayujau not Aśvinī), so no new name is reported. It does contain a valuable STAR-COUNT list at avparis_1,2.1 giving the number of stars in each asterism — directly useful for confirming yogatārā identifications.
- VERIFICATION GAP: no primary e-text of the Kāṭhaka Saṃhitā could be obtained. The Aśvattha entry rests solely on Macdonell & Keith's comparative table and should be re-verified against Schroeder's edition before being treated as firm.
- SCRIPT NOTE: the Maitrāyaṇī Saṃhitā evidence is from a romanised IAST e-text (GRETIL), not Devanagari. Devanagari headwords for Niṣṭya, Invagā and Brāhmaṇa were transliterated by the compiler and are NOT copied verbatim from an e-text; the IAST passages quoted in the shloka fields ARE verbatim.
- Verse-numbering correction for the Vedāṅga Jyotiṣa: the Śraviṣṭhā/Sārpa solstice verse is Ārca 6 = Yājuṣa 7, NOT Ārca 5. T.S. Kuppanna Sastry's copyrighted 1985 translation was deliberately not quoted anywhere.
- web.archive.org was blocked and sacred-texts.com returned HTTP 403 for this research pass; Griffith and Whitney were therefore taken from en.wikisource.org, and all Devanagari from sa.wikisource.org raw wikitext (?action=raw). One textual divergence found this way: RV 1.24.10 reads निहितास उच्चा in the raw Wikisource/Aufrecht text, where a rendered-page fetch gave निहिता उच्चा.

### Purāṇas

- SANYAL'S PRINTED TRANSLATION OF BP 5.23.6 IS DEFECTIVE — do not rely on it. The printed text drops the hind-feet clause and the Abhijit/Uttarāṣāḍhā clause entirely, and misassigns Ārdrā and Āśleṣā to the nostrils. The mūla is unambiguous: ārdrāśleṣe ca dakṣiṇa-vāmayoḥ paścimayoḥ pādayoḥ (hind feet), abhijid-uttarāṣāḍhe … nāsikayoḥ (nostrils). The mapping table follows the Sanskrit, not Sanyal. Sanyal also fails to render Ajavīthī as a proper name at 5.23.5.
- INDEPENDENTLY VERIFIED: the BP 5.23 scheme is arithmetically perfect. Counting eight forward from Maghā and eight backward from Mṛgaśiras (as prātilomyena requires), plus the twelve individually named asterisms, places all 28 nakṣatras exactly once, with no gaps and no duplicates — and yields exactly 14 per side, Abhijit→Punarvasu on the right and Puṣya→Uttarāṣāḍhā on the left, which is precisely what the commentator-derived endpoints state. The endpoints Anurādhā and Pūrvabhādrapadā are therefore inferred but confirmed, not guessed.
- TWO DIFFERENT ŚIŚUMĀRAS. The Bhāgavata's figure and the Viṣṇu/Vāyu/Matsya/Brahmāṇḍa figure conflict directly — e.g. the upper jaw is Agasti in the former and Uttānapāda in the latter, and the older version has only fourteen stars while the Bhāgavata carries all 28 nakṣatras plus every planet. They are recorded as two recensions of one name, not merged into a single mapping.
- MODERN CONSTELLATION IDENTIFICATION OF THE ŚIŚUMĀRA IS GENUINELY DISPUTED AND THE TEXTS DO NOT SETTLE IT. Draco is the strongest reading for the older 14-star figure (R.N. Iyengar; R.S. Hariharan; and al-Bīrūnī's independent gloss of Śiśumāra by Persian susumār, the Great Lizard = Draco). Ursa Minor is proposed by others. Neither can be right for the Bhāgavata's version, which is a whole-sky figure. No Purāṇa assigns a single named star to a single limb, so every limb-to-star chart in circulation is reconstruction.
- THE NINE-VĪTHĪ LIST IS INTERNALLY CONTRADICTORY IN ITS ONLY FULL SOURCE. Matsya 124.53 and 124.58 assign the same three asterisms (Mūla + both Aṣāḍhās) to two different vīthīs; and 124.55 repeats the name nāgavīthī where Gajavīthī is required. Both errors are shared by the GRETIL and Wikisource witnesses, so they are old, and the 1916 translator flags both. The Matsya scheme also diverges substantively from Varāhamihira's Bṛhat Saṃhitā 9 — a real Purāṇa-vs-Siddhānta difference, not a copying slip.
- CORRECTIONS TO EARLIER ASSUMPTIONS: (a) in BP 5.23.5 the Ākāśagaṅgā is on the BELLY (udarataḥ), not the back — only Ajavīthī is on the back (pṛṣṭhe); (b) the Viṣṇu Purāṇa's Śiśumāra body-part mapping is at 2.12.31-34, NOT 2.9, which gives only the bare figure; (c) the vīthīs are at VP 2.8.85/2.8.90 and Matsya 124, not VP 2.9/2.12 or Matsya 127 — Matsya 127 is the Dhruva/Śiśumāra chapter; (d) the Viṣṇu Purāṇa names only TWO vīthīs and gives constituent nakṣatras for neither.
- NEGATIVE FINDINGS, CHECKED DIRECTLY: Kāladaṇḍa does not occur as a sky-object in Brahmāṇḍa, Matsya, Mārkaṇḍeya, Kūrma, Liṅga or the Vāyu chapters examined — every occurrence is Yama's staff or a weapon-simile. Ākāśagaṅgā and Svargagaṅgā are absent as sky-names from that whole group (their term is chāyāpatha); Mandākinī there is always a terrestrial river. Liṅga, Kūrma and Mārkaṇḍeya contain neither the ninefold vīthī list nor the Śiśumāra sky-figure and added no distinct star names — the Mārkaṇḍeya's Agastya references are to the sage, not the star.
- SOURCE-ACCESS NOTES: sacred-texts.com blocked direct requests, so Wilson's text was read through the Wayback Machine mirror of the canonical URLs cited (the same text with identical footnotes is also mirrored at wisdomlib.org). GRETIL has NO full Vāyu Purāṇa — only the Revākhaṇḍa — so all Vāyu Sanskrit comes from sa.wikisource and is unchecked against a critical edition; GRETIL's Matsya stops at adhyāya 176, so Matsya 273 likewise.
- DEVANAGARI COVERAGE IS UNEVEN. Bhāgavata Devanagari was taken from an e-text of the mūla only (never a copyrighted translation) and cross-checked word-for-word against GRETIL's independent IAST — those two agree exactly. Viṣṇu Purāṇa Devanagari comes from sa.wikisource, whose text carries minor slips against the Pathak critical edition (e.g. पदगस्त्यस्य for यदगस्त्यस्य at 2.8.85, तस्याधो for तस्यातो at 2.12.31); IAST from GRETIL's critical edition is the more reliable witness. Brahmāṇḍa is available in IAST only. Prabhupāda's and Tagare's translations were consulted only for orientation and are nowhere quoted.
- The 1916/1917 Matsya Purāṇa translation ('A Taluqdar of Oudh', ed. B.D. Basu) is public domain but its OCR on archive.org is badly degraded; where it could not be quoted cleanly a literal rendering was supplied and labelled as such. Page images are at archive.org/details/in.ernet.dli.2015.283501 (Part II) and in.ernet.dli.2015.274264 if exact quotation is needed.
- Viṣṇu Purāṇa verse numbering differs by edition: vulgate 4.24.104-112 vs Pathak critical edition 4.24.24-31 for the Saptarṣi-cycle passage. The citation in this database follows the vulgate/Wikisource text quoted.

### Lexicons, Nirukta & Buddhist

- VERSE NUMBERING: sa.wikisource and GRETIL both number the Amarakośa by half-verse continuously within each kāṇḍa, so the star passage falls at 1.3.215–229 in their reckoning. Editions numbering by full śloka give the same passage as roughly 1.3.22–29. Colebrooke prints it as Book I, Chapter I, Section II, verses 21–28, merging the Vyoma-varga and Dig-varga into one section. Two independent e-texts (sa.wikisource wikitext and GRETIL) were compared and agree letter-for-letter on every Amarakośa line quoted.
- The Amarakośa star material is in the DIG-VARGA (1.3), not the Svarga-varga as commonly assumed; only the Milky-Way synonyms are in the Svarga-varga (1.1.116).
- NOT FOUND in the Amarakośa, contrary to expectation: Nabhogaṅgā, Haritsarit, Vyomagaṅgā, Ākāśagaṅgā (its four Milky-Way words are only Mandākinī, Viyadgaṅgā, Svarnadī, Suradīrghikā); Mṛgavyādha; jyotis as a star-synonym; and any synonym-set for the Pleiades — Kṛttikā gets no synonyms at all.
- Lopāmudrā (Amarakośa 1.3.216) is EXCLUDED as a star name. Colebrooke glosses her only as 'His consort'; the lexicon does not treat her as a star, notwithstanding a modern editorial section-heading in the GRETIL file that says 'agastya's wife (also star names)'.
- The Buddhist nakshatra DEITIES are deities, not star names, and are recorded only in the notes. Several diverge from the Brahmanical lists — Ārdrā's deity is Sūrya (not Rudra), Hasta's Sūrya (not Savitṛ), Pūrvaphalgunī's Bhava (not Bhaga), Aśvinī's Gandharva (not the Aśvins), Uttarabhādrapadā's Aryamā — which is itself evidence of an independent transmission.
- The Mahāmāyūrī's maṅgalasaṃpanna (of Puṣya), amitramarthanī (of Maghā) and mahātejā (of Anurādhā) are metrical EPITHETS filling out the verse, not additional names, and are deliberately given no entries.
- Triśaṅku appears in the Śārdūlakarṇāvadāna as the mātaṅga (outcaste) king who recites the astronomy to the brahmin Puṣkarasārin — a person, not the star already on file. No star-sense of Triśaṅku occurs in this text.
- NO PUBLIC-DOMAIN ENGLISH TRANSLATION exists for the Śārdūlakarṇāvadāna or the Mahāmāyūrī: Cowell & Neil (1886) is a Sanskrit edition without translation, and Mukhopadhyaya (1954) and Takubo (1972) are copyrighted. All renderings of those two texts are the compiler's own literal versions, flagged as such; nothing is quoted from a copyrighted translation.
- SCRIPT NOTE: the GRETIL e-texts of the Śārdūlakarṇāvadāna, Mahāmāyūrī and Arthaśāstra are in IAST transliteration only, so the shloka fields for those entries hold verbatim IAST, not Devanagari, and are marked '[IAST, GRETIL]'. Devanagari WAS obtained for Nirukta 3.20 (sa.wikisource) and for every Amarakośa line.
- ARTHAŚĀSTRA 2.20 DOES NOT CONTAIN A NAKSHATRA LIST. The whole of 2.20 (Kangle 2.20.1–66) was read: it gives linear measures, time units, shadow-lengths, the six seasons and the nakshatra-derived month names, and defines the 27-day nākṣatra month, but never enumerates the 28. Grepping the entire Arthaśāstra for nakshatra names turns up only those month-names and the sceptical maxim at 9.4.26.
- JAIN CANON — NOT RECOVERED. No fetchable Ardhamāgadhī Prakrit e-text was found for the Sūryaprajñapti, Candraprajñapti, Jambūdvīpaprajñapti or Sthānāṅga-sūtra. GRETIL's Prakrit holdings contain no Jain astronomy; the archive.org scans have unusable Devanagari OCR; jainqq.org serves page images with Hindi commentary rather than the Prakrit. Thibaut's public-domain 1880 study is the best available witness and yields the doctrine in English (28 unequal nakshatras; Abhijit a class of its own at 9 4/67 muhūrtas) but no quotable Prakrit. The Jain star-counts and shapes therefore remain UNVERIFIED. Recommended follow-up: Weber's 'Die vedischen Nachrichten von den Naxatra' (1860–62, public-domain German, quotes the Jain Prakrit).
- OTHER KOŚAS ALL FAILED. Hemacandra's Abhidhānacintāmaṇi is not on GRETIL and the archive.org 1877 Calcutta edition has unusable Devanagari OCR, so no verbatim quotation is offered. Vaijayantī, Trikāṇḍaśeṣa, Medinīkośa and Śabdakalpadruma: no usable e-text located. Böhtlingk & Rieu's public-domain 1847 edition of Hemacandra with German translation is the right source and is worth a dedicated follow-up.
- One Amarakośa datum could not be attributed safely: Colebrooke's Nānārtha section glosses a headword as 'An asterism (the Scorpion's tail)', which can only be मूलम्, but the Devanagari headword is illegible in the scan and the matching half-verse could not be located with confidence. It is cited in the Mūlā notes as Colebrooke's identification, without a verse number.

### Later siddhāntas & al-Bīrūnī

- OCR RELIABILITY IS THE MAIN RISK IN THE BRĀHMASPHUṬASIDDHĀNTA ENTRIES. The only complete Sanskrit BSS with a usable text layer is the archive.org item 'Brahmasphutasiddhanta' (Ram Swarup Sharma's edition), whose OCR garbles conjuncts and numerals badly. Every Devanagari verse given for the BSS has been normalised from that OCR against the edition's own word-by-word Sanskrit and Hindi commentary, which restates each figure in plain words — so the NUMBERS (87/77, 86/40, 12 and 13 kālāṃśas) and the NAMES (muni, mṛgahartṛ, prājeśa, āgneya, maitra, aindra) are secure, while the exact orthography of the verses is not. A page-image check against Dvivedi 1902 or Sharma 1966 is advisable before these verses are quoted as text.
- COLEBROOKE 1817 IS A DEAD END FOR STARS — a settled negative. He translated only BSS ch. 12 (arithmetic) and ch. 18 (algebra). GRETIL's BSS file is likewise mathematics only and contains zero hits for agastya, mṛgavyādha, brahmahṛdaya, lubdhaka, yogatārā or even nakṣatra. Burgess's remark about 'the Brahma-Siddhanta... according to Colebrooke' comes from Colebrooke's separate Asiatic Researches papers, not the 1817 volume.
- BRAHMAGUPTA NAMES ONLY TWO NON-NAKSHATRA STARS. Burgess states it flatly: 'The Siddhanta-Çiromani and Brahma-Siddhanta omit all notice of any of the fixed stars excepting Canopus and Sirius.' Greps of the full Sanskrit BSS confirm it — no brahmahṛdaya, prajāpati, apāṃvatsa, āpas or hutabhuj anywhere in the mūla (brahmahṛdaya occurs twice, both inside the commentary). So the Sūrya Siddhānta's seven-star roster is NOT the common siddhāntic inheritance: Brahmagupta and Bhāskara carry only two of them, and Varāhamihira only one.
- PAÑCASIDDHĀNTIKĀ SANSKRIT COULD NOT BE OBTAINED — a real gap. Neither the Thibaut/Dvivedi 1889 scan nor Kuppanna Sastry's 1993 edition has any Devanagari in its text layer, and the text is on neither GRETIL nor sa.wikisource. The findings rest on Thibaut's public-domain English and on the printed tables. Kuppanna Sastry notes that PS XIV.39–40 are quoted by Utpala on Bṛhat Saṃhitā 12.21, so a Bṛhat Saṃhitā edition WITH Utpala is the most promising route to the Sanskrit. Thibaut also cautions that his emended text 'exhibits considerable deviation from the text of the Manuscripts' at exactly the Agastya rule.
- ŚRĪPATI IS RECOVERED ONLY AT SECOND HAND, from quotations inside the modern BSS commentary rather than a Siddhāntaśekhara edition; Babuaji Misra's edition was not located online. The name Lopāmudrāvallabha and the figures 87°/77° are certain; the verse wording is not.
- VAṬEŚVARA-SIDDHĀNTA IS ONLY PARTLY ONLINE and the relevant chapters are the missing ones. sa.wikisource has three chapters (madhyamādhikāra, spaṣṭādhikāra, triprasnādhikāra), none of which names an individual star; the two hits for yogatārā are false positives about the 27 soli-lunar YOGAS. The udayāsta and bhagrahayuti chapters are not online.
- FOUR TARGETS REMAIN OPEN, and their absence here is 'not searched', not a negative finding: Lalla's Śiṣyadhīvṛddhida; the Siddhāntaśekhara as a text in its own right; the Bṛhat Jātaka (N.C. Iyer's 1885 public-domain translation, and GRETIL's sa_varAhamihira-bRhajjAtaka.txt, which exists); and the Bṛhat Parāśara Horā Śāstra.
- SŪRYA SIDDHĀNTA CH. 10 CONTAINS NO STAR NAMES — verified verse by verse. It is entirely on the moon's phases and the computation of eclipse-like phenomena.
- AL-BĪRŪNĪ'S NAKSHATRA COORDINATE TABLE WAS NOT FULLY TRANSCRIBED. Its OCR is heavily damaged; only the identification column was extracted reliably, plus two coordinate rows (Abhijit 265°/62°N — note this differs from the Sūrya Siddhānta value; Śatabhiṣaj 10s 20°). Recovering the full numeric column requires the page images and would be worth doing, since Burgess says the Khaṇḍakhādyaka latitudes 'often vary considerably' from both the Sūrya Siddhānta and the Siddhānta Śiromaṇi, and al-Bīrūnī is our only witness for them.
- TWO AL-BĪRŪNĪ OBJECTS ARE NOTED BUT GIVEN NO ENTRY, because he supplies no Sanskrit name. (1) A 'fever-star' seen from Langabalus, 'composed of the tail of the Small Bear and his back, and of some small stars situated there; it is called the axe of the mill' — and, crucially, 'BRAHMAGUPTA MENTIONS IT IN CONNECTION WITH THE FISH', i.e. Brahmagupta treated this Ursa Minor group as part of the Śiśumāra, a datum about the figure's extent worth chasing in the BSS Golādhyāya. (2) The Pauliśa Siddhānta's rule for Agastya's heliacal setting, with the observational note that 'They observe it first when the sun enters the station Hasta, and they lose it out of sight when he enters the station Rohiṇī.'
- NAME-COLLISION WARNING. Brahmagupta's yogatārā table uses deity-epithets that collide with existing entries for entirely different stars: Prājeśa/Prajāpati means ROHIṆĪ (α Tauri), whereas the Prajāpati on file is δ Aurigae; and Āgneya means KṚTTIKĀ (η Tauri), whereas the Agni/Hutabhuj on file is β Tauri. Sūrya Siddhānta 9.13–15 uses the same style of epithet (maitra, sārpa, raudrarkṣa, tiṣya, saumya, aśvinidaivata, vaiṣṇava, vāsava, ahirbudhnya). These are recorded as alternative names of the nakshatras, deliberately NOT merged with the same-named fixed stars.
