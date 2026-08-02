#!/usr/bin/env python3
"""Merge the four per-source research JSONs into the final star-name database
(JSON + Markdown). Grouping unit = the Sanskrit name; synonyms are cross-linked
rather than collapsed, so every attested name keeps its own entry."""
import json
import os
import re
import unicodedata

URL_RE = re.compile(r"https?://[^\s)]+")

def links(field, label):
    """Render a source field as markdown link(s). Fields may carry annotations
    ('fetched via …', page numbers) around one or more URLs; the full text is
    preserved in the JSON, the markdown just links the URLs."""
    urls = [u.rstrip(".,;") for u in URL_RE.findall(field)]
    if not urls:
        return field
    parts = [f"[{label}]({urls[0]})"]
    for i, u in enumerate(urls[1:], 1):
        name = "mirror" if len(urls) == 2 else f"mirror {i}"
        parts.append(f"[{name}]({u})")
    return " · ".join(parts)

SCRATCH = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = "/Users/alokm/dev/bhagol/docs/star-names"

SOURCES = {
    "surya_siddhanta": "Sūrya Siddhānta",
    "vedic_corpus": "Vedic corpus",
    "brihat_samhita": "Bṛhat Saṃhitā",
    "siddhanta_shiromani": "Siddhānta Śiromaṇi",
    "vedic_expansion": "Ṛgveda & Vedāṅga Jyotiṣa",
    "puranas": "Purāṇas",
    "lexicons_buddhist": "Lexicons, Nirukta & Buddhist",
    "later_siddhantas": "Later siddhāntas & al-Bīrūnī",
    "utpala": "Utpala's commentary",
    "panini": "Pāṇini & Patañjali",
    "vatesvara_samanta": "Vaṭeśvara & Sāmanta",
    "kerala": "Āryabhaṭīya commentaries",
    "xiuyao": "Chinese Buddhist witnesses",
    "epics": "Mahābhārata & Rāmāyaṇa",
    "kavya": "Classical kāvya",
}

# (source_key, name_iast) -> canonical entry id.  Entries sharing an id merge
# (their references are concatenated); the first-listed source is the primary
# whose name/modern-star/notes seed the canonical entry.
CANON = {
    # --- Surya Siddhanta: 28 yogataras + 7 individual stars (primary) ---
    ("surya_siddhanta", "Aśvinī"): "ashvini",
    ("surya_siddhanta", "Bharaṇī"): "bharani",
    ("surya_siddhanta", "Kṛttikā"): "krittika",
    ("surya_siddhanta", "Rohiṇī"): "rohini",
    ("surya_siddhanta", "Mṛgaśīrṣa"): "mrigashirsha",
    ("surya_siddhanta", "Ārdrā"): "ardra",
    ("surya_siddhanta", "Punarvasu"): "punarvasu",
    ("surya_siddhanta", "Puṣya"): "pushya",
    ("surya_siddhanta", "Āśleṣā"): "ashlesha",
    ("surya_siddhanta", "Maghā"): "magha",
    ("surya_siddhanta", "Pūrva-Phalgunī"): "purva-phalguni",
    ("surya_siddhanta", "Uttara-Phalgunī"): "uttara-phalguni",
    ("surya_siddhanta", "Hasta"): "hasta",
    ("surya_siddhanta", "Citrā"): "chitra",
    ("surya_siddhanta", "Svātī"): "svati",
    ("surya_siddhanta", "Viśākhā"): "vishakha",
    ("surya_siddhanta", "Anurādhā"): "anuradha",
    ("surya_siddhanta", "Jyeṣṭhā"): "jyeshtha",
    ("surya_siddhanta", "Mūla"): "mula",
    ("surya_siddhanta", "Pūrvāṣāḍhā"): "purva-ashadha",
    ("surya_siddhanta", "Uttarāṣāḍhā"): "uttara-ashadha",
    ("surya_siddhanta", "Abhijit"): "abhijit",
    ("surya_siddhanta", "Śravaṇa"): "shravana",
    ("surya_siddhanta", "Śraviṣṭhā (Dhaniṣṭhā)"): "dhanishtha",
    ("surya_siddhanta", "Śatabhiṣaj"): "shatabhishaj",
    ("surya_siddhanta", "Pūrva-Bhādrapadā"): "purva-bhadrapada",
    ("surya_siddhanta", "Uttara-Bhādrapadā"): "uttara-bhadrapada",
    ("surya_siddhanta", "Revatī"): "revati",
    ("surya_siddhanta", "Agastya"): "agastya",
    ("surya_siddhanta", "Mṛgavyādha"): "mrigavyadha",
    ("surya_siddhanta", "Agni (Hutabhuj)"): "agni",
    ("surya_siddhanta", "Brahmahṛdaya"): "brahmahridaya",
    ("surya_siddhanta", "Prajāpati"): "prajapati",
    ("surya_siddhanta", "Apāṃvatsa"): "apamvatsa",
    ("surya_siddhanta", "Āpas"): "apas",
    # --- Vedic corpus ---
    ("vedic_corpus", "Kṛttikāḥ"): "krittika",             # both TS and SB entries
    ("vedic_corpus", "Ambā, Dulā, Nitatnī, Abhrayantī, Meghayantī, Varṣayantī, Cupuṇīkā"): "krittika-seven",
    ("vedic_corpus", "Rohiṇī"): "rohini",
    ("vedic_corpus", "Rohiṇī (second; = Jyeṣṭhā)"): "rohini-indra",
    ("vedic_corpus", "Mṛgaśīrṣa"): "mrigashirsha",
    ("vedic_corpus", "Invakāḥ (Invagāḥ)"): "invaka",
    ("vedic_corpus", "Ārdrā"): "ardra",
    ("vedic_corpus", "Bāhū (Rudrasya)"): "bahu",
    ("vedic_corpus", "Tiṣya"): "tishya",
    ("vedic_corpus", "Puṣya"): "pushya",
    ("vedic_corpus", "Saptarṣayaḥ / Ṛkṣāḥ"): "saptarshi",
    ("vedic_corpus", "Dhruva"): "dhruva",
    ("vedic_corpus", "Arundhatī"): "arundhati",
    ("vedic_corpus", "Mṛga (Prajāpati)"): "mriga",
    ("vedic_corpus", "Mṛgavyādha"): "mrigavyadha",
    ("vedic_corpus", "Iṣus trikāṇḍā"): "ishus-trikanda",
    # --- Brihat Samhita ---
    ("brihat_samhita", "Agastya"): "agastya",
    ("brihat_samhita", "Marīci"): "marichi",
    ("brihat_samhita", "Vasiṣṭha"): "vasishtha",
    ("brihat_samhita", "Aṅgiras"): "angiras",
    ("brihat_samhita", "Atri"): "atri",
    ("brihat_samhita", "Pulastya"): "pulastya",
    ("brihat_samhita", "Pulaha"): "pulaha",
    ("brihat_samhita", "Kratu"): "kratu",
    ("brihat_samhita", "Arundhatī"): "arundhati",
    ("brihat_samhita", "Lubdhaka"): "lubdhaka",
    # --- Siddhanta Shiromani ---
    ("siddhanta_shiromani", "Agastya"): "agastya",
    ("siddhanta_shiromani", "Lubdhaka (Mṛgaripu / Mṛgavyādha)"): "lubdhaka",
    ("siddhanta_shiromani", "Abhijit"): "abhijit",
    ("siddhanta_shiromani", "Revatī-tārā (junction star of Revatī, the zero point)"): "revati",
    ("siddhanta_shiromani", "Aśvinyādi yogatārāḥ (sābhijit)"): "yogatara-catalog",
}

# Sources whose entries carry an explicit "db_id" (newer research files); the
# older four are mapped through CANON above.
DB_ID_SOURCES = {"vedic_expansion", "puranas", "lexicons_buddhist", "later_siddhantas",
                 "utpala", "panini", "vatesvara_samanta", "kerala", "xiuyao",
                 "epics", "kavya"}

NAKSHATRAS = [
    "ashvini", "bharani", "krittika", "rohini", "mrigashirsha", "ardra",
    "punarvasu", "pushya", "ashlesha", "magha", "purva-phalguni",
    "uttara-phalguni", "hasta", "chitra", "svati", "vishakha", "anuradha",
    "jyeshtha", "mula", "purva-ashadha", "uttara-ashadha", "abhijit",
    "shravana", "dhanishtha", "shatabhishaj", "purva-bhadrapada",
    "uttara-bhadrapada", "revati",
]
INDIVIDUAL = ["agastya", "mrigavyadha", "lubdhaka", "agni", "brahmahridaya",
              "prajapati", "apamvatsa", "apas", "dhruva",
              # further names for the same few bright stars, plus one unidentified
              "kumbhasambhava", "maitravaruni", "muni", "mrigahartri",
              "lopamudravallabha", "auttanapadi", "shula", "kumbhayoni", "yama-samanta"]
SAPTARSHI = ["saptarshi", "marichi", "vasishtha", "angiras", "atri",
             "pulastya", "pulaha", "kratu", "arundhati"]
# Asterisms of the Vedic star-lore proper (the Orion tableau, the Bears)
VEDIC_EXTRA = ["rksha", "krittika-seven", "mriga", "ishus-trikanda", "vichritau"]

# Alternative, archaic and deity-epithet names for the 28 nakshatras. These are
# real attested names, kept separate from the nakshatra they denote so the reader
# can see which text calls it what.
NAKSHATRA_ALIAS = [
    "agha", "arjuni", "nishtya", "sarpa", "jyeshthaghni", "mulabarhana",
    "invaka", "ilvala", "tishya", "sidhya", "bahu", "rohini-indra",
    "ashvayuj", "radha", "shravishtha", "proshthapada", "agrahayani",
    "ashvattha", "brahmana-nakshatra",
    # siddhāntic deity-epithets
    "vaishnava", "vasava", "ahirbudhnya", "ashvinidaivata", "maitra",
    "raudrarksha", "saumya", "prajesha", "agneya",
    # Pāṇini's archaic stratum, and the Middle-Indic form behind the Chinese
    "bahula", "kattika-karttika",
    # deity-epithets from Utpala, the epics, Vaṭeśvara and Sāmanta
    "paitamaha", "svayambhuva", "prajapatya", "anala-krittika", "yamya-bharani",
    "paushna", "bhagya", "pavana-svati", "tvashtra", "varuna-shatabhishaj",
    "pracetas-shatabhishaj", "maindra-jyeshtha", "aindra-nakshatra", "ekapada",
    "aditya-punarvasu", "aditidaivatya", "devamatri", "vishnubha",
    "govinda-shravana", "brahma-nakshatra", "nairrita", "jiva-pushya",
    "vitta-dhanishtha",
]

# The generic vocabulary of "star" itself
STAR_WORD = ["nakshatra-generic", "bha", "tara", "taraka", "udu", "dhishnya", "str"]
SKY_FIGURE = ["shishumara", "sakvara", "trishanku"]
SHISHUMARA_POS = ["dhata-vidhata", "indra-mahendra", "kashyapa", "marichi-tail",
                  "uttanapada", "yajna-group", "yama-shishumara",
                  "prajapati-circumpolar", "suniti"]
STAR_ROAD = ["nagavithi", "gajavithi", "airavati", "arshabhi", "govithi",
             "jaradgava", "ajavithi", "mrigavithi", "vaishvanari",
             "margas", "pitryana-devayana", "suravithi", "shukra-shanmandala"]
MILKY_WAY = ["akashaganga", "chayapatha", "tripathaga",
             "mandakini", "viyadganga", "svarnadi", "suradirghika",
             "vyomaganga", "nabhonadi"]
SKY_REGION = ["vishnupada", "medhi", "pravaha", "tarapatha"]
COLLECTIVE = ["yogatara-catalog", "dakshayanyah", "citrashikhandin",
              "ashtavimshati-nakshatrani", "nakshatra-catur-dvarika", "taragraha",
              "rohini-shakata", "brahmarashi", "nakshatramala", "dakshina-saptarshi"]

CATEGORY = {}
for i in NAKSHATRAS: CATEGORY[i] = "nakshatra"
for i in INDIVIDUAL: CATEGORY[i] = "individual-star"
for i in SAPTARSHI: CATEGORY[i] = "saptarshi"
for i in VEDIC_EXTRA: CATEGORY[i] = "vedic-asterism"
for i in NAKSHATRA_ALIAS: CATEGORY[i] = "nakshatra-alias"
for i in STAR_WORD: CATEGORY[i] = "star-word"
for i in SKY_FIGURE: CATEGORY[i] = "sky-figure"
for i in SHISHUMARA_POS: CATEGORY[i] = "shishumara-position"
for i in STAR_ROAD: CATEGORY[i] = "star-road"
for i in MILKY_WAY: CATEGORY[i] = "milky-way"
for i in SKY_REGION: CATEGORY[i] = "sky-region"
for i in COLLECTIVE: CATEGORY[i] = "collective"

SEE_ALSO = {
    "bahula": ["krittika", "anala-krittika", "kattika-karttika", "krittika-seven"],
    "kattika-karttika": ["krittika", "bahula"],
    "anala-krittika": ["krittika", "agni", "bahula"],
    "paitamaha": ["rohini", "svayambhuva", "prajapatya", "prajesha", "prajapati", "rohini-shakata"],
    "svayambhuva": ["rohini", "paitamaha", "prajapati"],
    "prajapatya": ["rohini", "paitamaha", "prajapati", "prajesha"],
    "rohini-shakata": ["rohini", "krittika-seven", "ilvala", "ishus-trikanda"],
    "brahma-nakshatra": ["abhijit", "brahmana-nakshatra", "brahmarashi"],
    "brahmarashi": ["brahma-nakshatra", "dhruva", "saptarshi"],
    "kumbhayoni": ["agastya", "kumbhasambhava", "maitravaruni", "muni"],
    "vyomaganga": ["akashaganga", "nabhonadi", "mandakini", "viyadganga"],
    "nabhonadi": ["akashaganga", "vyomaganga", "svarnadi"],
    "suravithi": ["margas", "pitryana-devayana", "shukra-shanmandala"],
    "shukra-shanmandala": ["margas", "suravithi"],
    "nakshatramala": ["dakshina-saptarshi", "trishanku"],
    "dakshina-saptarshi": ["saptarshi", "nakshatramala", "trishanku"],
    "yama-samanta": ["agastya", "shula"],

    "mrigavyadha": ["lubdhaka"],
    "lubdhaka": ["mrigavyadha"],
    "tishya": ["pushya"],
    "pushya": ["tishya"],
    "invaka": ["mrigashirsha"],
    "mrigashirsha": ["invaka", "mriga"],
    "bahu": ["ardra"],
    "ardra": ["bahu"],
    "rohini-indra": ["jyeshtha", "rohini"],
    "jyeshtha": ["rohini-indra"],
    "krittika-seven": ["krittika"],
    "krittika": ["krittika-seven"],
    "arundhati": ["vasishtha"],
    "vasishtha": ["arundhati"],
    "mriga": ["mrigashirsha", "mrigavyadha", "ishus-trikanda"],
    "ishus-trikanda": ["mriga"],
    "dhruva": ["saptarshi", "arundhati", "shishumara", "medhi", "suniti",
               "vishnupada"],
    "saptarshi": ["marichi", "vasishtha", "angiras", "atri", "pulastya",
                   "pulaha", "kratu", "arundhati", "rksha"],
    # --- expansion cross-links ---
    "rksha": ["saptarshi"],
    "agha": ["magha"],
    "magha": ["agha"],
    "arjuni": ["purva-phalguni", "uttara-phalguni"],
    "purva-phalguni": ["arjuni"],
    "uttara-phalguni": ["arjuni"],
    "vichritau": ["mula", "mulabarhana"],
    "mulabarhana": ["mula", "vichritau"],
    "mula": ["vichritau", "mulabarhana"],
    "jyeshthaghni": ["jyeshtha"],
    "nishtya": ["svati"],
    "svati": ["nishtya"],
    "ashvattha": ["shravana"],
    "shravana": ["ashvattha"],
    "sarpa": ["ashlesha"],
    "ashlesha": ["sarpa"],
    "shishumara": ["dhruva", "dhata-vidhata", "indra-mahendra", "kashyapa",
                   "marichi-tail", "uttanapada", "yajna-group",
                   "yama-shishumara", "prajapati-circumpolar", "akashaganga"],
    "dhata-vidhata": ["shishumara"],
    "indra-mahendra": ["shishumara", "kashyapa"],
    "kashyapa": ["shishumara", "indra-mahendra"],
    "marichi-tail": ["shishumara", "marichi"],
    "uttanapada": ["shishumara", "agastya"],
    "yajna-group": ["shishumara"],
    "yama-shishumara": ["shishumara", "agastya"],
    "prajapati-circumpolar": ["shishumara", "prajapati"],
    "prajapati": ["prajapati-circumpolar"],
    "suniti": ["dhruva", "arundhati"],
    "akashaganga": ["chayapatha", "tripathaga", "shishumara"],
    "chayapatha": ["akashaganga", "tripathaga"],
    "tripathaga": ["akashaganga", "chayapatha"],
    "ajavithi": ["vaishvanari", "margas", "pitryana-devayana"],
    "vaishvanari": ["ajavithi", "margas"],
    "nagavithi": ["margas", "pitryana-devayana"],
    "gajavithi": ["margas"],
    "airavati": ["margas"],
    "arshabhi": ["margas"],
    "govithi": ["margas"],
    "jaradgava": ["margas"],
    "mrigavithi": ["margas"],
    "margas": ["nagavithi", "gajavithi", "airavati", "arshabhi", "govithi",
               "jaradgava", "ajavithi", "mrigavithi", "vaishvanari"],
    "pitryana-devayana": ["agastya", "ajavithi", "nagavithi", "saptarshi"],
    "vishnupada": ["dhruva", "saptarshi"],
    "medhi": ["dhruva"],
    "trishanku": [],
    # --- lexicon / Buddhist / later-siddhānta cross-links ---
    "mandakini": ["akashaganga", "chayapatha", "tripathaga", "viyadganga", "svarnadi", "suradirghika"],
    "viyadganga": ["mandakini", "akashaganga"],
    "svarnadi": ["mandakini", "akashaganga"],
    "suradirghika": ["mandakini", "akashaganga"],
    "auttanapadi": ["dhruva", "uttanapada"],
    "kumbhasambhava": ["agastya", "maitravaruni"],
    "maitravaruni": ["agastya", "kumbhasambhava"],
    "muni": ["agastya", "lopamudravallabha"],
    "lopamudravallabha": ["agastya", "muni"],
    "mrigahartri": ["mrigavyadha", "lubdhaka"],
    "nakshatra-generic": ["bha", "tara", "taraka", "udu", "dhishnya", "str", "rksha"],
    "bha": ["nakshatra-generic"], "tara": ["nakshatra-generic", "taraka"],
    "taraka": ["nakshatra-generic", "tara"], "udu": ["nakshatra-generic"],
    "dhishnya": ["nakshatra-generic"], "str": ["nakshatra-generic", "rksha"],
    "dakshayanyah": ["nakshatra-generic"],
    "citrashikhandin": ["saptarshi", "rksha"],
    "ashvayuj": ["ashvini"], "radha": ["vishakha"], "sidhya": ["pushya", "tishya"],
    "shravishtha": ["dhanishtha", "vasava"], "proshthapada": ["purva-bhadrapada", "uttara-bhadrapada"],
    "agrahayani": ["mrigashirsha", "ilvala"], "ilvala": ["mrigashirsha", "invaka", "agrahayani"],
    "vaishnava": ["shravana"], "vasava": ["dhanishtha", "shravishtha"],
    "ahirbudhnya": ["uttara-bhadrapada"], "ashvinidaivata": ["ashvini"],
    "maitra": ["anuradha"], "raudrarksha": ["ardra"], "saumya": ["mrigashirsha"],
    "prajesha": ["rohini", "prajapati"], "agneya": ["krittika", "agni"],
    "sakvara": ["shishumara"], "shula": [],
    "ashtavimshati-nakshatrani": ["nakshatra-catur-dvarika"],
    "nakshatra-catur-dvarika": ["ashtavimshati-nakshatrani"],
    "taragraha": ["tara"],
    "tarapatha": ["chayapatha"],
}

CONF_RANK = {"certain": 0, "likely": 1, "disputed": 2, "unidentified": 3}

def load(name):
    with open(os.path.join(SCRATCH, name + ".json")) as f:
        return json.load(f)

def main():
    data = {k: load(k) for k in SOURCES}
    stars = {}
    order = []
    for src_key, src in data.items():
        for e in src["entries"]:
            cid = e["db_id"] if src_key in DB_ID_SOURCES else CANON[(src_key, e["name_iast"])]
            ref = {
                "text": SOURCES[src_key],
                "citation": e["citation"],
                "text_date": e.get("text_date"),
                "name_status": e.get("name_status"),
                "shloka_devanagari": e["shloka_devanagari"],
                # Devanagari unless the only e-text is romanized (the Buddhist
                # Sanskrit is edited in IAST); empty verse carries a note saying why.
                "shloka_script": e.get("shloka_script", "devanagari"),
                "shloka_note": e.get("shloka_note"),
                "shloka_source_url": e["shloka_source_url"],
                "translation_en": e["translation_en"],
                "translator": e["translator"],
                "translation_source_url": e["translation_source_url"],
                "source_notes": e["identification_notes"],
            }
            if cid not in stars:
                stars[cid] = {
                    "id": cid,
                    "category": CATEGORY[cid],
                    "name_devanagari": e["name_devanagari"],
                    "name_iast": e["name_iast"],
                    "modern_star": e["modern_star"],
                    "identification_confidence": e["identification_confidence"],
                    "see_also": SEE_ALSO.get(cid, []),
                    "references": [ref],
                }
                order.append(cid)
            else:
                s = stars[cid]
                s["references"].append(ref)
                # keep the most cautious confidence label
                if CONF_RANK[e["identification_confidence"]] > CONF_RANK[s["identification_confidence"]]:
                    s["identification_confidence"] = e["identification_confidence"]

    # deterministic order: category blocks, then first-seen within each
    block = (NAKSHATRAS + NAKSHATRA_ALIAS + INDIVIDUAL + SAPTARSHI + VEDIC_EXTRA
             + SKY_FIGURE + SHISHUMARA_POS + STAR_ROAD + MILKY_WAY + SKY_REGION
             + STAR_WORD + COLLECTIVE)
    ordered = [stars[i] for i in block if i in stars]
    missing = set(stars) - set(block)
    assert not missing, f"ids not placed in any category block: {sorted(missing)}"
    assert len(ordered) == len(stars), (len(ordered), len(stars))

    db = {
        "title": "Sanskrit star names: an annotated source database",
        "generated": "2026-08-02",
        "method": "Compiled from primary e-texts — Sanskrit Wikisource and GRETIL for Sanskrit, CBETA for the Chinese Buddhist canon — and, where no keyed e-text exists (Utpala, Vaṭeśvara, Sāmanta, every Kerala work), from archive.org page facsimiles read directly, the Devanagari OCR of those scans being unusable. Devanagari is copied verbatim from the cited source; no verse was reconstructed from memory, and a verse that could not be fetched is recorded as absent rather than supplied. Public-domain translations (Burgess 1860, Iyer 1884, Keith 1914/1920, Eggeling 1882, Oldenberg 1886, Whitney 1905, Wilson 1840, Colebrooke 1805/1808, Ganguli 1883-96, Dutt 1892-94, Cowell, Vasu 1891, Wilkinson & Sastri 1861, Tawney 1880) are quoted verbatim with a URL; copyrighted work (Bhat 1981, Arkasomayaji, Dumont 1954, Kuppanna Sastry, Shukla, K.V. Sarma, Pingree, Ramasubramanian, Goldman) is paraphrased and cited, never quoted. Where no published translation exists the rendering is labelled as the compiler's own. Negative findings — texts searched that yielded no star name — are recorded per source rather than omitted. See FORMAT.md for the schema and the full editorial rules.",
        "unit": "One entry per attested Sanskrit name (synonyms cross-linked via see_also), grouped: 28 nakshatra junction stars (yogatārā), individually named stars, the Saptarṣi and Arundhatī, Vedic asterisms of the Orion tableau and archaic names, and Bhāskara's collective catalog.",
        "aryabhatiya_finding": data["siddhanta_shiromani"]["aryabhatiya_finding"],
        "summary_findings_by_source": {
            SOURCES[k]: data[k]["summary_findings"]
            for k in data if "summary_findings" in data[k]
        },
        "shishumara_mapping": data["puranas"]["shishumara_mapping"],
        "stars": ordered,
        "caveats_by_source": {SOURCES[k]: data[k]["caveats"] for k in data},
    }
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "star-names.json"), "w") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    write_markdown(db)
    print(f"{len(ordered)} entries, {sum(len(s['references']) for s in ordered)} references")

def anchor(s):
    # GitHub anchor algorithm: lowercase; keep word chars (letters, marks,
    # numbers, underscore) and hyphens; spaces become hyphens; drop the rest.
    out = []
    for c in s.lower():
        if unicodedata.category(c)[0] in "LMN" or c in "-_":
            out.append(c)
        elif c == " ":
            out.append("-")
    return "".join(out)

def write_markdown(db):
    L = []
    A = L.append
    A("# Sanskrit Star Names — Source Database\n")
    A("Authentic references to star names in Sanskrit texts: the original shloka "
      "(copied verbatim from online e-texts), a published translation, and the modern "
      "identification of each star.\n")
    A(f"*Generated {db['generated']}. Machine-readable version: [`star-names.json`](star-names.json); "
      "per-source research files with full caveats: [`sources/`](sources/).*\n")
    A("> **This file is generated — do not edit it.** The originals are the per-text research files in "
      "[`sources/`](sources/); this page, `star-names.json` and `sky-chart.html` are all rebuilt from them "
      "by `sources/merge.py` and `sources/build_chart.py`. See [`FORMAT.md`](FORMAT.md) for the schema, the "
      "editorial rules, and how to add a source.\n")
    A("**Method.** " + db["method"] + "\n")
    A("**A note on what the texts actually say.** The Vedic texts name asterisms and deities but never "
      "coordinates; the siddhāntas give coordinates for a single junction star (yogatārā) per nakshatra. "
      "All modern equations therefore rest on the siddhāntic positions (chiefly as analysed by Burgess 1860) "
      "and on continuous tradition; the *confidence* column records where that chain is strong and where it is disputed.\n")

    cats = [
        ("nakshatra", "The 28 nakshatra junction stars (yogatārā)",
         "Sūrya Siddhānta ch. 8 defines each nakshatra's junction star by polar coordinates and by rules "
         "(vv. 16–19) naming which member of the group is the yogatārā. Vedic attestations are added where found."),
        ("individual-star", "Individually named stars",
         "Stars outside the nakshatra series that the texts name in their own right."),
        ("saptarshi", "The Saptarṣi (Ursa Major) and Arundhatī",
         "Bṛhat Saṃhitā ch. 13 gives the east-to-west order of the seven rishis and places Arundhatī beside "
         "Vasiṣṭha; the star-by-star mapping below follows from that order once Vasiṣṭha is anchored to Mizar "
         "by Arundhatī = Alcor. Only the Mizar/Alcor pair is fixed by the text itself."),
        ("vedic-asterism", "Vedic asterisms and archaic names",
         "Older names from the Saṃhitā/Brāhmaṇa layer: the individually named Kṛttikās, the celestial Orion tableau "
         "of Aitareya Brāhmaṇa 3.33, and the archaic names that the Ṛgveda, Atharvaveda, Maitrāyaṇī/Kāṭhaka "
         "Saṃhitās and Vedāṅga Jyotiṣa use where later lists have the familiar ones — Aghā for Maghā, Arjunī for "
         "the Phalgunīs, Niṣṭya for Svāti, Sārpa for Āśleṣā, Jyeṣṭhaghnī for Jyeṣṭhā. Vicṛtau is the earliest "
         "Indian passage to name individual stars *as stars* (tārake, 'the two stars')."),
        ("nakshatra-alias", "Other names for the nakshatras",
         "Every one of these is a real attested name for an asterism that also appears above under its "
         "familiar title — archaic Vedic forms (Aghā, Arjunī, Niṣṭya, Jyeṣṭhaghnī), lexicon variants "
         "(Aśvayuj, Rādhā, Śraviṣṭhā, Proṣṭhapadā, Āgrahāyaṇī, Ilvalāḥ), and the siddhāntic habit of naming a "
         "nakshatra by its presiding deity (Vaiṣṇava for Śravaṇa, Vāsava for Dhaniṣṭhā, Raudrarkṣa for Ārdrā). "
         "They are kept as separate entries so it stays visible which text calls it what. **Two are traps:** "
         "Brahmagupta's Prājeśa means Rohiṇī and his Āgneya means Kṛttikā — not the distinct fixed stars "
         "Prajāpati (δ Aurigae) and Agni (β Tauri) listed further down."),
        ("star-word", "The vocabulary of 'star' itself",
         "Not names of stars but the words for them, with the oldest Indian etymologies. Yāska derives ṛkṣa from "
         "height and stṛ from scattering; the Amarakośa treats nakṣatra, ṛkṣa, bha, tārā, tārakā and uḍu as "
         "interchangeable. *tārā* is the element in *yoga-tārā*, 'junction star', on which every identification "
         "in this database depends."),
        ("sky-figure", "Sky-figures",
         "Whole figures drawn in the stars, rather than single points."),
        ("shishumara-position", "Positions on the Śiśumāra",
         "Names the Purāṇas place on the body of the celestial porpoise. These are genuine textual sky-positions, "
         "but no Purāṇa equates any of them with a visible star, so none is plotted on the chart — every "
         "limb-to-star chart in circulation is modern reconstruction. See the mapping table below."),
        ("star-road", "Star-roads (vīthī) and belts (mārga)",
         "The Purāṇic road-system: three great belts (Airāvata, Jaradgava, Vaiśvānara), each holding three "
         "vīthīs of three nakshatras — 27 in all. On the chart each road is drawn as a dashed line through its "
         "own nakshatras. Matsya 124 is the only full source and it contradicts itself twice, which the entries record."),
        ("milky-way", "The Milky Way",
         "Three Purāṇic names for the galactic band. On the chart they are attached to the galactic equator, "
         "computed from the J2000 galactic pole."),
        ("sky-region", "Sky-regions and mechanisms",
         "Named zones and the machinery of rotation — not stars, and not plottable as points."),
        ("collective", "Collective catalogs",
         "Star-catalog passages that treat the yogatārās as a set."),
    ]

    # summary table
    A("## Summary table\n")
    A("| Sanskrit | IAST | Modern star | Bayer | Confidence | Attested in |")
    A("|---|---|---|---|---|---|")
    for s in db["stars"]:
        texts = sorted({r["text"] for r in s["references"]})
        nm = s["name_devanagari"].split(",")[0].split(" (")[0]
        link_text = f"[{nm}](#{anchor(header_line(s))})"
        A(f"| {link_text} | {s['name_iast']} | {s['modern_star']['common_name']} | "
          f"{s['modern_star']['bayer']} | {s['identification_confidence']} | {'; '.join(texts)} |")
    A("")

    A("## What each source yielded\n")
    for src, s in db["summary_findings_by_source"].items():
        A(f"**{src}.** {s}\n")

    A("## A finding about the Āryabhaṭīya\n")
    A(db["aryabhatiya_finding"] + "\n")

    A("## The Śiśumāra-cakra: the sky as a porpoise\n")
    A("Bhāgavata Purāṇa 5.23.4–8 lays the whole sky out as the body of a celestial porpoise, with Dhruva at the "
      "tail-tip and the 28 nakshatras ranged along its flanks. An older and shorter recension (Viṣṇu Purāṇa "
      "2.12.31–34 = Vāyu 52.92–95 = Matsya 127.22–25 = Brahmāṇḍa 1,23.102–105) maps deities onto a fourteen-star "
      "figure instead. The two conflict — the upper jaw is Agasti in one and Uttānapāda in the other — so both are "
      "given here. *Stated* means the text says it; *inferred* means a commentator supplied it.\n")
    A("The Bhāgavata's scheme was checked arithmetically and is internally perfect: counting eight forward from "
      "Maghā and eight backward from Mṛgaśiras, plus the twelve individually named asterisms, places all 28 "
      "nakshatras exactly once — 14 per side. That independently confirms the commentators' endpoints.\n")
    A("| Recension | Body part | Sanskrit | IAST | Stated? | Modern |")
    A("|---|---|---|---|---|---|")
    for m in db["shishumara_mapping"]:
        A(f"| {m['recension']} | {m['body_part']} | {m['name_devanagari']} | {m['name_iast']} | "
          f"{m['stated_or_inferred']} | {m['modern']} |")
    A("")

    for cat, title, blurb in cats:
        entries = [s for s in db["stars"] if s["category"] == cat]
        if not entries:
            continue
        A(f"## {title}\n")
        A(blurb + "\n")
        for s in entries:
            A(f"### {header_line(s)}\n")
            m = s["modern_star"]
            A(f"**Modern identification:** {m['common_name']} — {m['bayer']}, {m['constellation']} "
              f"(*{s['identification_confidence']}*)\n")
            if s["see_also"]:
                A("*See also:* " + ", ".join(f"`{x}`" for x in s["see_also"]) + "\n")
            for r in s["references"]:
                A(f"**{r['citation']}** — {links(r['shloka_source_url'], 'Sanskrit e-text')}\n")
                if r["shloka_devanagari"]:
                    if r["shloka_script"] == "iast":
                        A("> *(IAST — the e-text carries no Devanagari copy)*")
                        A(">")
                    for line in r["shloka_devanagari"].split("\n"):
                        A(f"> {line}")
                    if r["shloka_note"]:
                        A(">")
                        A(f"> *{r['shloka_note']}*")
                else:
                    # No verse to quote; say why in its place rather than leaving a blank quote.
                    A(f"> *{r['shloka_note']}*")
                A(">")
                A(f"> — *{r['translation_en']}*")
                A(f"> <br>— {r['translator']} ({links(r['translation_source_url'], 'source')})\n")
                A(f"<sub>**Identification notes ({r['text']}):** {r['source_notes']}</sub>\n")

    A("## Caveats, per source\n")
    A("These are the working caveats recorded during compilation — read them before treating any entry as final.\n")
    for src, caveats in db["caveats_by_source"].items():
        A(f"### {src}\n")
        for c in caveats:
            A(f"- {c}")
        A("")

    with open(os.path.join(OUT_DIR, "README.md"), "w") as f:
        f.write("\n".join(L))

def header_line(s):
    return f"{s['name_devanagari']} ({s['name_iast']}) — {s['modern_star']['common_name']}"

if __name__ == "__main__":
    main()
