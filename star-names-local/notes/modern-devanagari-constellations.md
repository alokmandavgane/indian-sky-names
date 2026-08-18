# The Devanagari names of the modern constellations

*Research note, 2026-08-18. This documents the sources behind the Devanagari constellation
names the Bhagol app adopted on this date. The full per-name entries now exist:
17 Marathi entries (Dikshit, quoted against the page images) in `marathi_gujarati.json`
and 56 Hindi entries (Muley, paraphrased) in `hindi_urdu_punjabi.json`.*

## The chain of authority

1. **Bal Shastri Jambhekar (before 1846)** coined Sanskrit names for the Western
   constellations that had none in the Indian tradition. We know this from Dikshit (below),
   who reports the names as *current in Marathi* by 1892 and names their author:

   > पाश्चात्य ज्योतिष्यांनीं आकाशांतील तारकांचे सुमारें १०२ राशि म्हणजे पुंज कल्पिले
   > आहेत. त्यांपैकीं ४८ प्राचीन आहेत. … पाश्चात्यांनीं कल्पिलेल्या बाकीच्या राशींस
   > संस्कृत संज्ञा शास्त्री जांभेकर यांनीं दिल्या आहेत. त्याच हल्लीं मराठींत येतात.
   > — Jyotirvilas, pp. 35–36 (transcribed from the scan, leaves 60–61)

2. **S. B. Dikshit, ज्योतिर्विलास, 2nd ed. (Bombay, 1893; 1st ed. 1892).** Marathi,
   public domain. Scan: archive.org/details/india.history.resource.92658 (leaf = printed
   page + 25). Uses the Jambhekar set throughout and adds two coinages of his own, with
   the reasoning stated (the southern Saptarshi theory):

   > स्वस्तिक आणि नरतुरंग ह्या दोन पुंजांस अनुक्रमें त्रिशंकु आणि दक्षिणर्क्ष अशीं नांवें
   > मीं योजिलीं आहेत. — p. 36

   On Cygnus he is explicit that the name is a translation, defended from kāvya:
   > हंस हें नांव आमच्या ज्योतिषग्रंथांत नाहीं, पाश्चात्यांच्या नांवावरून भाषांतर करून
   > घेतलें आहे, हें खरें. तरी आमच्या इतर ग्रंथांत तें आहे असें मला वाटतें. — p. 38

3. **Gunakar Muley, आकाश दर्शन (New Delhi: Rajkamal Prakashan, first ed. February 1993).**
   Hindi, IN COPYRIGHT — cite and paraphrase only, never quote. Serialized in Navbharat
   Times (1988–89) and Saptahik Hindustan (1991–92) before book publication, so the names
   reached a national Hindi readership. Scan: archive.org/details/akash-gunakar.
   A Marathi native (preface, p. 7), Muley carries the Jambhekar–Dikshit Marathi set into
   Hindi and completes it: his परिशिष्ट 4, "तारा-मंडल सूची" (pp. 344–347, read from scan
   leaves 172–173) tables all 88 IAU constellations with a भारतीय नाम column. For
   Centaurus his prose (p. ~89) states the names are received usage: "सेंटौरस् मंडल को
   भारत में कभी किन्नर, तो कभी नरतुरंग कहा जाता है"; likewise Pegasus (p. ~241 "अब
   महाश्व या हयशिर के नाम से भी जाना जाता है"), Crux (p. ~132 "त्रिशंकु या स्वस्तिक के
   नाम से भी जाना जाता है"), Boötes (p. ~159 "भारतीय ज्योतिष में … प्रायः ईश (भूतेश)"),
   Ursa Minor (p. ~141 "लघु सप्तर्षि"), Perseus (p. ~311 "इस मंडल को अब हम ययाति कहते
   हैं"). His own framing (p. ~16): uniform Indian names across languages are still to be
   settled — i.e. part proposal, part report.

## The concordance (what the app adopted, and why)

| IAU | Adopted (hi / en) | Authority | Notes |
|---|---|---|---|
| Aquila | गरुड / Garuda | AD 344 (also index p. 236f) | |
| Auriga | सारथी / Sarathi | JV 183; AD 344 (प्रजापति primary, सारथी attested) | प्रजापति avoided: collides with Uranus (Modak's coinage, JV pp. 154ff) and the star Prajāpati (δ Aur) |
| Boötes | भूतेश / Bhutesh | AD ~159 (ईश, भूतेश, भूतप) | |
| Canis Major | बृहद् श्वान / Brihad Shwan | AD ~72, 344 | replaces unattested app coinage ब्रहलुब्धक |
| Canis Minor | लघु श्वान / Laghu Shwan | AD ~72, 344 | |
| Carina | नौतल / Nautal | AD ~97, 345 | JV's नौका = whole Argo (नौकापुंज, pp. 36, 181) |
| Centaurus | नरतुरंग / Narturang | Jambhekar apud JV 36; AD ~89, 345 | AD also किन्नर; JV's own दक्षिणर्क्ष (p. 36, 184) recorded as alternative |
| Cetus | तिमिंगल / Timingal | JV 181; AD 345 | AD also केतु — avoided (node collision) |
| Coma Berenices | केश (hi only) | AD 346 | |
| Corona Australis | दक्षिणी किरीट / Dakshini Kirit | AD 346 | |
| Corona Borealis | उत्तरी किरीट / Uttari Kirit | AD 346 | JV's उत्तरमुकुट (p. 181, 1866 nova) is the older Devanagari name |
| Corvus | काक / Kak | AD ~130, 346 | |
| Crater | चषक / Chashak | AD 346 | |
| Crux | त्रिशंकु / Trishanku | Dikshit's coinage, JV 36; AD ~132 | Jambhekar's स्वस्तिक (JV 34, 36; AD 346) the alternative; matches Kannada ತ್ರಿಶಂಕು (Jyotirvinodini 1931) |
| Cygnus | हंस (kept) | JV 38, 181; AD 346 | |
| Draco | शिशुमार (kept) | traditional; JV/AD use कालिय (JV ~41; AD ~145, 346) | कालिय recorded as alternative |
| Equuleus | लघु अश्व / Laghu Ashva | AD 346 | |
| Eridanus | वैतरणी / Vaitarani | AD ~305, 346 | JV's यमुना/यमुनानदी (pp. 39; index "यमुना तारकापुंज ३९") the older name |
| Grus | सारस / Saras | AD 346 | |
| Hercules | शौरि / Shauri | JV 184 (solar apex "शौरिनामक पुंज") | AD never Indianizes Hercules — JV is the sole authority |
| Hydra | महासर्प / Mahasarp | AD ~134, 346 | |
| Hydrus | जलसर्प / Jalsarp | AD 346 | |
| Leo Minor | लघु सिंह / Laghu Simha | AD 346 | |
| Lepus | शशक / Shashak | AD 346 | |
| Lupus | वृक / Vrika | AD 346 | matches Kannada ವೃಕ (Jyotirvinodini 1931) |
| Lynx | बिडाल / Bidal | AD 346 | |
| Lyra | वीणा / Veena | AD ~241, 346 | |
| Monoceros | एकशृंग / Ekashring | AD 346 | |
| Ophiuchus | सर्पधर / Sarpdhar | AD ~192, 347 | JV's भुजगधारी (p. 181, Kepler's nova) the older name |
| Pavo | मयूर / Mayur | AD 347 | |
| Pegasus | हयशिर / Hayashir | AD ~241, 347 | also महाश्व |
| Perseus | ययाति (kept) | JV 181, 184; AD 347 | |
| Phoenix | अमरपक्षी / Amarpakshi | AD 347 | |
| Piscis Austrinus | दक्षिण मीन / Dakshin Meen | AD ~249, 347 | JV's याम्यमत्स्य (p. 39) the older name |
| Puppis | पिच्छल / Pichchhal | AD 347 | |
| Sagitta | वाण / Vaan | AD 347 | |
| Sextans | षडंश / Shadansh | AD 347 | |
| Triangulum | त्रिभुज / Tribhuj | AD ~283, 347 | |
| Triangulum Australe | दक्षिणी त्रिभुज / Dakshini Tribhuj | AD 347 | |
| Tucana | कारंडव / Karandav | AD 347 | |
| Ursa Minor | लघु सप्तर्षि / Laghu Saptarshi | AD ~141, 347 | JV's ध्रुवमत्स्य (p. 20; also Maharashtra Sabdakosa, already in DB) the older name |
| Vela | पाल / Pal | AD 347 | |
| Vulpecula | शृगाल / Shrigal | AD 347 | |
| Ara, Octans, Antlia, Caelum | वेदी, अष्टक, वाताकर्ष, तक्षणी | AD 344–347 | |
| hi-only (en keeps Latin) | जाल, शिल्पकार, चित्रफलक, दिक्सूचक, सूक्ष्मदर्शी, दूरदर्शी, केश | AD 344–347 | Sanskrit-compound translations; Devanagari display only |
| Record-only (pulled from the base display 2026-08-18 evening) | जिराफ़, घड़ी, गुनिया, परकार, भट्ठी, पठार, ढाल, उड़न-मीन | AD 344–347 | Hindi-register translations (five merely repeat Muley's gloss column); they letter the opt-in Hindi culture layer, where the Muley citation shows, but not the base "Sanskrit" display |
| Serpens Caput/Cauda | — | AD gives only सर्प (347) | the app briefly showed सर्पशीर्ष/सर्पपुच्छ, the compiler's own construction; withdrawn the same day — the halves stay Latin in the base display |
| Not adopted | Apus, Lacerta (blank in AD), Dorado, Indus, Delphinus, Canes Venatici (transliterations only) | | |

## Named stars the sources add (not yet entries)

JV: ब्रह्महृदय = Capella (p. 34); आप + अपांवत्स near Hasta/Chitrā (p. 35, θ Vir region);
अग्नि = β Tau; मिरा glossed अद्भुत(?) p. 182; अलगोल p. 181. AD (with index pages):
नदीमुख = Achernar (305–308), मत्स्यमुख = Fomalhaut (249–254), अग्नि = अल्-नाथ/β Tau,
and the सप्तर्षि star-by-star set (क्रतु=Dubhe, पुलह=Merak, पुलस्त्य=Phecda, अत्रि=Megrez,
अंगिरस=Alioth, वसिष्ठ=Mizar, मरीचि=Alkaid).

## Traps recorded

- **प्रजापति** is three things: Uranus (Modak's planet coinage, used by JV), the star near
  Orion's head (JV p. 32 "प्रजापति तारा"), and Auriga (AD). Never map it bare.
- **केतु** for Cetus (AD) collides with the node; never adopt.
- **शिशुमार** is claimed for Draco (tradition; the app), for Delphinus (AD ~213), and
  शिशुमार चक्र for Ursa Minor (AD ~141). The app keeps it on Draco.
- JV's index and OCR page numbers drop digits; page numbers above marked ~ are from the
  book's own index as OCR'd and should be verified against the scan when entries are written.
