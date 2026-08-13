#!/usr/bin/env python3
"""Build the full-screen sky chart: merge J2000 coordinates + magnitudes with the
shloka/translation references from star-names.json, inject as __DATA__."""
import json, re, html

DB = json.load(open("/Users/alokm/dev/bhagol/docs/star-names/star-names.json"))
TPL = open("chart_template.html").read()
URL_RE = re.compile(r"https?://[^\s)]+")

def urls(s):
    return [u.rstrip(".,;") for u in URL_RE.findall(s or "")]

# id -> (RA deg J2000, Dec deg, apparent mag, kind, dev_short, plotnote)
#   kind: "star" = point star, "figure" = asterism/group (dashed ring)
#   dev_short/plotnote: None keeps the default (first Devanagari token)
P = {
    # ---- 28 nakshatra junction stars (yogatārā) ----
    "ashvini":          (28.66,  20.81, 2.64, "star", None, None),
    "bharani":          (40.86,  27.71, 4.66, "star", None, None),
    "krittika":         (56.87,  24.11, 2.87, "star", None, None),  # Alcyone
    "rohini":           (68.98,  16.51, 0.85, "star", None, None),  # Aldebaran
    "mrigashirsha":     (83.78,   9.93, 3.39, "star", None, None),  # Meissa
    "ardra":            (88.79,   7.41, 0.45, "star", None, None),  # Betelgeuse
    "punarvasu":        (116.33, 28.03, 1.14, "star", None, None),  # Pollux
    "pushya":           (131.17, 18.15, 3.94, "star", None, None),  # Asellus Aus.
    "ashlesha":         (131.69,  6.42, 3.38, "star", None, None),  # eps Hya
    "magha":            (152.09, 11.97, 1.36, "star", None, None),  # Regulus
    "purva-phalguni":   (168.53, 20.52, 2.56, "star", None, None),  # Zosma
    "uttara-phalguni":  (177.26, 14.57, 2.11, "star", None, None),  # Denebola
    "hasta":            (183.95,-17.54, 2.59, "star", None, None),  # Gienah
    "chitra":           (201.30,-11.16, 0.98, "star", None, None),  # Spica
    "svati":            (213.92, 19.18,-0.05, "star", None, None),  # Arcturus
    "vishakha":         (228.06,-19.79, 4.54, "star", None,  # iota Lib
                         "Contested. Plotted at ι Librae, where Sāmanta's 1899 re-observation puts it to 32'. "
                         "But the Śārdūlakarṇāvadāna and both early Chinese witnesses make Viśākhā TWO stars, "
                         "horn-shaped — which can only be the bright scale-pair α/β Librae, as Burgess himself "
                         "believed. The asterism and the computed junction-star may simply have parted company."),
    "anuradha":         (240.08,-22.62, 2.29, "star", None, None),  # Dschubba
    "jyeshtha":         (247.35,-26.43, 1.06, "star", None, None),  # Antares
    "mula":             (263.40,-37.10, 1.62, "star", None, None),  # Shaula
    "purva-ashadha":    (275.25,-29.83, 2.70, "star", None, None),  # Kaus Media
    "uttara-ashadha":   (283.82,-26.30, 2.05, "star", None, None),  # Nunki
    "abhijit":          (279.23, 38.78, 0.03, "star", None, None),  # Vega
    "shravana":         (297.70,  8.87, 0.76, "star", None, None),  # Altair
    "dhanishtha":       (309.40, 14.60, 3.63, "star", None, None),  # Rotanev
    "shatabhishaj":     (343.15, -7.58, 3.74, "star", None, None),  # lambda Aqr
    "purva-bhadrapada": (346.19, 15.21, 2.49, "star", None, None),  # Markab
    "uttara-bhadrapada":(3.31,   15.18, 2.83, "star", None,
                         "Disputed: the text mixes γ Pegasi (Algenib, plotted here) with α Andromedae; see notes."),
    "revati":           (18.44,   7.57, 5.21, "star", None, None),  # zeta Psc
    # ---- individually named stars ----
    "agastya":          (95.99, -52.70,-0.74, "star", None,
                         "Deep-south star; lies low on the horizon from India — the theme of Bṛhat Saṃhitā ch. 12."),
    "mrigavyadha":      (101.29,-16.72,-1.46, "star", None, None),  # Sirius
    "lubdhaka":         (101.29,-16.72,-1.46, "star", None,
                         "Same star as Mṛgavyādha (Sirius): the classical 'hunter' synonym."),
    "agni":             (81.57,  28.61, 1.65, "star", "अग्नि", None),   # Elnath
    "brahmahridaya":    (79.17,  46.00, 0.08, "star", None, None),      # Capella
    "prajapati":        (89.88,  54.28, 3.72, "star", None, None),      # delta Aur
    "apamvatsa":        (197.49, -5.54, 4.38, "star", None, None),      # theta Vir
    "apas":             (193.90,  3.40, 3.39, "star", "आपः", None),     # delta Vir
    "dhruva":           (37.95,  89.26, 1.98, "star", None,
                         "The pole star sits at the very top of any RA/Dec chart (Dec +89°); RA is nearly meaningless there."),
    # ---- Saptarṣi (Ursa Major) & Arundhatī ----
    "saptarshi":        (185.0,  56.0,  2.0, "figure", "सप्तर्षयः",
                         "The whole Big Dipper; plotted at the group's centre, with its seven rishi-stars around it."),
    "marichi":          (206.89, 49.31, 1.85, "star", None, None),  # Alkaid
    "vasishtha":        (200.98, 54.93, 2.23, "star", None, None),  # Mizar
    "angiras":          (193.51, 55.96, 1.76, "star", None, None),  # Alioth
    "atri":             (183.86, 57.03, 3.31, "star", None, None),  # Megrez
    "pulastya":         (178.46, 53.69, 2.44, "star", None, None),  # Phecda
    "pulaha":           (165.46, 56.38, 2.37, "star", None, None),  # Merak
    "kratu":            (165.93, 61.75, 1.79, "star", None, None),  # Dubhe
    "arundhati":        (201.31, 54.99, 3.99, "star", None,
                         "Alcor, the naked-eye companion of Mizar (Vasiṣṭha) — the classic eyesight test."),
    # ---- Vedic asterisms & archaic names ----
    "krittika-seven":   (56.75, 24.12, 1.6, "figure", "सप्त कृत्तिकाः",
                         "The seven individually-named Kṛttikās = the stars of the Pleiades cluster."),
    "rohini-indra":     (247.35,-26.43, 1.06, "star", "रोहिणी (इन्द्र)",
                         "The archaic second 'Rohiṇī' of the Taittirīya Saṃhitā = Antares, later renamed Jyeṣṭhā."),
    "invaka":           (83.78,  9.93, 3.39, "star", "इन्वकाः",
                         "Taittirīya name for the stars of Orion's head = Mṛgaśīrṣa (λ Orionis)."),
    "bahu":             (85.0,   6.9,  1.6, "figure", "बाहू",
                         "'The two Arms' of the celestial deer: usually Betelgeuse + Bellatrix; plotted between them."),
    "tishya":           (131.17, 18.15, 3.94, "star", "तिष्यः",
                         "Archaic name for the later Puṣya (δ Cancri region)."),
    "mriga":            (83.0,   1.0,  1.7, "figure", "मृगः",
                         "The celestial deer = the whole figure of Orion (Aitareya Brāhmaṇa 3.33); plotted at its centre."),
    "ishus-trikanda":   (84.05, -1.20, 1.69, "figure", "इषुस्त्रिकाण्डा",
                         "The 'three-jointed arrow' = Orion's Belt (Mintaka, Alnilam, Alnitak); plotted at Alnilam."),
    # ---- Ṛgveda / Atharvaveda / Vedāṅga Jyotiṣa expansion ----
    "rksha":            (185.0,  56.0,  2.0, "figure", "ऋक्षाः",
                         "The Ṛgvedic 'Bears' = the same seven stars as the Saptarṣi; plotted at the group's centre."),
    "agha":             (152.09, 11.97, 1.36, "star", "अघा",
                         "The archaic Ṛgvedic form of Maghā, at Regulus."),
    "arjuni":           (172.90, 17.50, 2.30, "figure", "अर्जुन्यौ",
                         "A dual: both Phalgunīs (δ/θ Leonis and β Leonis); plotted between them."),
    "vichritau":        (263.05,-37.20, 1.60, "figure", "विचृतौ",
                         "'The two Unfasteners' = Shaula (λ Sco) and Lesath (υ Sco); plotted between the pair."),
    "jyeshthaghni":     (247.35,-26.43, 1.06, "star", "ज्येष्ठघ्नी",
                         "The archaic ill-omened name of Jyeṣṭhā, at Antares."),
    "mulabarhana":      (263.40,-37.10, 1.62, "figure", "मूलबर्हण",
                         "'The Uprooter' = the Scorpion's tail as a whole; plotted at λ Scorpii."),
    "nishtya":          (213.92, 19.18,-0.05, "star", "निष्ट्य",
                         "The Maitrāyaṇī/Kāṭhaka name for Svāti, at Arcturus."),
    "ashvattha":        (297.70,  8.87, 0.76, "star", "अश्वत्थ",
                         "The Kāṭhaka name in the Śravaṇa slot, at Altair. The verse itself could not be found "
                         "online — this rests on Macdonell & Keith's comparative table alone."),
    "sarpa":            (131.69,  6.42, 3.38, "star", "सार्प",
                         "The Vedāṅga Jyotiṣa names this nakshatra only by its deity (the Serpents) = Āśleṣā."),
    # ---- Purāṇic sky-figures ----
    "shishumara":       (262.50, 62.00, 2.20, "figure", "शिशुमार",
                         "The celestial porpoise. Plotted over Draco, which is the strongest reading of the older "
                         "14-star figure (and al-Bīrūnī's own gloss). The Bhāgavata's expanded version is a "
                         "whole-sky figure and cannot be placed at one point at all."),
    "trishanku":        (188.00,-60.00, 1.30, "figure", "त्रिशङ्कु",
                         "Plotted at Crux, the usual modern gloss — but no Purāṇa says so; the identification "
                         "comes from later lexicography."),
    "sakvara":          (262.50, 62.00, 2.20, "figure", "शाक्वर",
                         "Al-Bīrūnī's second name for the Śiśumāra, plotted with it over Draco — the reading his "
                         "own Persian gloss (susmār, 'great lizard') supports."),
    # ---- other names for nakshatras: plotted on the same star, so one click
    #      reveals every Sanskrit name for that point ----
    "ilvala":           (83.78,   9.93, 3.39, "figure", "इल्वलाः",
                         "The Amarakośa defines these as 'the stars that dwell in the head-region' of the Deer — "
                         "so the group, λ/φ¹/φ² Orionis, is stated by the lexicon itself."),
    "sidhya":           (131.17, 18.15, 3.94, "star", "सिध्यः", None),
    "ashvayuj":         (28.66,  20.81, 2.64, "star", "अश्वयुक्", None),
    "radha":            (222.72,-16.04, 2.75, "star", "राधा",
                         "Plotted at α Librae (Zubenelgenubi), the star Colebrooke's 'Southern scale' gloss and "
                         "the Buddhist two-star count both point to — not at the faint ι Librae that the Sūrya "
                         "Siddhānta's coordinates forced on Burgess for Viśākhā."),
    "shravishtha":      (309.40, 14.60, 3.63, "star", "श्रविष्ठा", None),
    "proshthapada":     (346.19, 15.21, 2.49, "figure", "प्रोष्ठपदा",
                         "A dual covering both Bhādrapadās (α Pegasi and γ Pegasi); plotted at α Pegasi, since "
                         "the pair straddles 0h and cannot share one point on this projection."),
    "agrahayani":       (83.78,   9.93, 3.39, "star", "आग्रहायणी", None),
    "vaishnava":        (297.70,  8.87, 0.76, "star", "वैष्णव", None),
    "vasava":           (309.40, 14.60, 3.63, "star", "वासव", None),
    "ahirbudhnya":      (3.31,   15.18, 2.83, "star", "अहिर्बुध्न्य", None),
    "ashvinidaivata":   (28.66,  20.81, 2.64, "star", "अश्विनिदैवत", None),
    "maitra":           (240.08,-22.62, 2.29, "star", "मैत्र", None),
    "raudrarksha":      (88.79,   7.41, 0.45, "star", "रौद्रर्क्ष",
                         "Plotted at Betelgeuse with the tradition — but al-Bīrūnī twice dissents, offering "
                         "Procyon in one place and Sirius in another."),
    "saumya":           (83.78,   9.93, 3.39, "star", "सौम्य", None),
    "prajesha":         (68.98,  16.51, 0.85, "star", "प्राजेश",
                         "Brahmagupta's name for ROHIṆĪ (Aldebaran) — not for the fixed star Prajāpati "
                         "(δ Aurigae), which is a different point on this chart."),
    "agneya":           (56.87,  24.11, 2.87, "star", "आग्नेय",
                         "Brahmagupta's name for KṚTTIKĀ (Alcyone) — not for the fixed star Agni "
                         "(β Tauri, Elnath), which is a different point on this chart."),
    # ---- further names for the same bright stars ----
    "kumbhasambhava":   (95.99, -52.70,-0.74, "star", "कुम्भसम्भवः", None),
    "maitravaruni":     (95.99, -52.70,-0.74, "star", "मैत्रावरुणिः", None),
    "muni":             (95.99, -52.70,-0.74, "star", "मुनि", None),
    "lopamudravallabha":(95.99, -52.70,-0.74, "star", "लोपामुद्रावल्लभ", None),
    "mrigahartri":      (101.29,-16.72,-1.46, "star", "मृगहर्तृ", None),
    "auttanapadi":      (37.95,  89.26, 1.98, "star", "औत्तानपादिः", None),
}

# Alias names plot on the very star they denote, so clicking a point stacks every
# name any text gives it. Target ids, not coordinates, so the two stay in step.
ALIAS_OF = {
    "bahula": "krittika", "kattika-karttika": "krittika", "anala-krittika": "krittika",
    "paitamaha": "rohini", "svayambhuva": "rohini", "prajapatya": "rohini",
    "yamya-bharani": "bharani", "paushna": "revati", "bhagya": "purva-phalguni",
    "pavana-svati": "svati", "tvashtra": "chitra",
    "varuna-shatabhishaj": "shatabhishaj", "pracetas-shatabhishaj": "shatabhishaj",
    "maindra-jyeshtha": "jyeshtha", "aindra-nakshatra": "jyeshtha",
    "ekapada": "purva-bhadrapada", "aditya-punarvasu": "punarvasu",
    "aditidaivatya": "punarvasu", "devamatri": "punarvasu",
    "vishnubha": "shravana", "govinda-shravana": "shravana",
    "brahma-nakshatra": "abhijit", "nairrita": "mula", "jiva-pushya": "pushya",
    "vitta-dhanishtha": "dhanishtha", "kumbhayoni": "agastya",
}
ALIAS_NOTE = {
    "paitamaha": "A name for ROHIṆĪ (Aldebaran) — not for the fixed star Prajāpati "
                 "(δ Aurigae), which is a different point on this chart.",
    "svayambhuva": "A name for ROHIṆĪ (Aldebaran) — not for the fixed star Prajāpati "
                   "(δ Aurigae), which is a different point on this chart.",
    "prajapatya": "The Rāmāyaṇa's name for ROHIṆĪ (Aldebaran) — not for the fixed star "
                  "Prajāpati (δ Aurigae), which is a different point on this chart.",
    "anala-krittika": "Utpala's name for KṚTTIKĀ (Alcyone) — not for the fixed star Agni "
                      "(β Tauri, Elnath), which is a different point on this chart.",
    "brahma-nakshatra": "Utpala's name for ABHIJIT (Vega). Distinct from the Vedic Brāhmaṇa "
                        "nakshatra, whose deity is Soma, and from the circumpolar Brahmarāśi.",
}
for _a, _t in ALIAS_OF.items():
    _ra, _dec, _mag, _kind, _ov, _n = P[_t]
    P[_a] = (_ra, _dec, _mag, "star", None, ALIAS_NOTE.get(_a))


# Star-roads: drawn as a dashed line through the road's own nakshatras.
ROADS = {
    "nagavithi":  ["ashvini", "bharani", "krittika"],
    "gajavithi":  ["rohini", "ardra", "mrigashirsha"],
    "airavati":   ["pushya", "ashlesha", "punarvasu"],
    "arshabhi":   ["purva-phalguni", "uttara-phalguni", "magha"],
    "govithi":    ["purva-bhadrapada", "uttara-bhadrapada", "revati"],
    "jaradgava":  ["shravana", "dhanishtha", "shatabhishaj"],
    "ajavithi":   ["mula", "purva-ashadha", "uttara-ashadha"],
    "mrigavithi": ["jyeshtha", "vishakha", "anuradha"],
    "vaishvanari": ["mula", "purva-ashadha", "uttara-ashadha"],
}
ROAD_NOTE = {
    "gajavithi": "Matsya 124.55 as transmitted repeats the name नागवीथी here; Gajavīthī is the required reading.",
    "ajavithi": "Drawn on the Matsya 124.53 / Viṣṇu 2.8.85 reading (Mūla + both Aṣāḍhās). Matsya 124.58, in the "
                "same chapter, instead gives Hasta, Citrā and Svātī — the text contradicts itself.",
    "vaishvanari": "Matsya 124.59 gives Vaiśvānarī the same three asterisms that 124.53 gives Ajavīthī, so the two "
                   "roads are drawn on top of each other here. The contradiction is the text's, not the chart's.",
    "govithi": "Drawn on the Matsya reading. Bṛhat Saṃhitā 9.2cd gives Govīthī = Aśvinī, Revatī and the two "
               "Bhādrapadās — close to the Matsya, adding only Aśvinī. The Hasta/Citrā/Svāti version belongs to the "
               "sequential scheme at BS 9.1, which Varāhamihira attributes to others.",
    "jaradgava": "Drawn on the Matsya reading (vāruṇa = Śatabhiṣaj), which Bṛhat Saṃhitā 9.3ab confirms exactly: "
                 "the triad beginning at Śravaṇa.",
}

# Milky Way names, pinned to the galactic equator at these galactic longitudes
# (chosen so the three labels sit apart along the band).
GALACTIC = {"akashaganga": 35.0, "mandakini": 80.0, "viyadganga": 135.0,
            "chayapatha": 195.0, "svarnadi": 250.0, "tripathaga": 300.0,
            "suradirghika": 340.0, "vyomaganga": 60.0, "nabhonadi": 220.0}

def short_dev(name):
    """First name only — chart labels take the head of a synonym list."""
    return re.split(r"[,(（/]", name)[0].strip()

UNPLOTTED_NOTE = {
    "yama-samanta": "Sāmanta gives this southern star coordinates (dhruva 66°, 22° south) but no identification "
                    "has been made; recorded unemended rather than guessed at.",
    "suravithi": "A road of the gods named at Mahābhārata 3.44.12 with no asterisms attached — it does not belong "
                 "to the nine-vīthī set and cannot be traced on the sky.",
    "shukra-shanmandala": "Six named blocks of consecutive nakshatras spanning the whole ecliptic. The names survive "
                          "only in the Parāśara passage Utpala quotes; Varāhamihira describes the six but names none.",
    "rohini-shakata": "The Wain of Rohiṇī — the Hyades cluster, a V-shaped group rather than a single point. "
                      "Utpala calls it six stars, the Śārdūlakarṇāvadāna five.",
    "brahmarashi": "A circumpolar group named between Dhruva and the Saptarṣis in both Utpala and the epics, "
                   "never identified; three translators give three different renderings.",
    "nakshatramala": "A second 'garland of asterisms' placed in the southern sky at Rāmāyaṇa 1.59.20-22, unidentified.",
    "dakshina-saptarshi": "A southern counterpart of the Great Bear, named in the Rāmāyaṇa and never identified.",
    "yogatara-catalog": "A catalog of all 28 junction stars as a set (Bhāskara's dhruva/śara table) — not a single point.",
    "brahmana-nakshatra": "An extra nakshatra name with no identified star; almost certainly a ritual category "
                          "rather than an observed asterism.",
    "margas": "Three latitude belts, each holding three vīthīs — a framing structure rather than a place. "
              "The nine roads themselves are drawn on the chart.",
    "pitryana-devayana": "Two bands defined by their boundary markers (Agastya and Ajavīthī; Nāgavīthī and the "
                         "Saptarṣi) rather than by stars of their own.",
    "vishnupada": "The zone above the Saptarṣi containing the pole — a region, not a star.",
    "medhi": "The pole itself, as the post the sky is tethered to — a concept, not a separate star.",
    "pravaha": "The wind that turns the sky: the Purāṇic name for diurnal rotation, not an object in it.",
    "tarapatha": "The Amarakośa's word for the sky as the star-bearing region — a place, not a thing in it.",
    "shula": "A red star south of Canopus, reported to al-Bīrūnī from Multan and identified with nothing since. "
             "Left off the chart because no position can honestly be assigned: nothing prominent, red and "
             "south of Canopus is visible from Multan's latitude.",
    "dakshayanyah": "A collective name for all 27 nakshatras — 'the daughters of Dakṣa'.",
    "citrashikhandin": "A collective name for the Seven Sages; the seven stars themselves are plotted.",
    "ashtavimshati-nakshatrani": "The Buddhist 28-fold list as a set; its per-asterism star-counts and figures "
                                 "are recorded on each nakshatra's own entry.",
    "nakshatra-catur-dvarika": "A structural scheme — the 28 asterisms in four gate-groups of seven, one per "
                               "direction — rather than a place in the sky.",
    "taragraha": "'The star-seizers': the five planets, which move and so cannot be charted at fixed points.",
}
STAR_WORD_NOTE = ("A word for 'star' rather than the name of one. Kept in the database because the vocabulary is "
                  "itself evidence — tārā is the element in yoga-tārā, 'junction star', on which every "
                  "identification here depends.")
SHISHUMARA_NOTE = ("A named position on the body of the Śiśumāra. No Purāṇa equates it with a visible star, so it "
                   "is deliberately left off the chart rather than pinned to a guess — every limb-to-star chart in "
                   "circulation is modern reconstruction.")

items = []
for s in DB["stars"]:
    sid = s["id"]
    road = ROADS.get(sid)
    gal = GALACTIC.get(sid)
    if sid in P:
        ra, dec, mag, kind, ov, plotnote = P[sid]
        dev_short = ov or short_dev(s["name_devanagari"])
    else:
        ra = dec = mag = None
        kind = "road" if road else ("galactic" if gal is not None else "figure")
        dev_short = short_dev(s["name_devanagari"])
        if road:
            plotnote = ROAD_NOTE.get(sid)
        elif gal is not None:
            plotnote = ("Pinned to the galactic equator, computed from the J2000 galactic pole. The band is where "
                        "the Milky Way actually runs; the exact point along it is chosen only to place the label.")
        elif s["category"] == "shishumara-position":
            plotnote = SHISHUMARA_NOTE
        elif s["category"] == "star-word":
            plotnote = STAR_WORD_NOTE
        else:
            plotnote = UNPLOTTED_NOTE.get(sid)
    refs = [{
        "text": r["text"],
        "citation": r["citation"],
        "shloka": html.escape(r["shloka_devanagari"]),
        "shloka_script": r["shloka_script"],
        "shloka_note": html.escape(r["shloka_note"]) if r["shloka_note"] else None,
        "shloka_links": urls(r["shloka_source_url"]),
        "translation": html.escape(r["translation_en"]),
        "translator": html.escape(r["translator"]),
        "trans_links": urls(r["translation_source_url"]),
        "notes": html.escape(r["source_notes"]),
    } for r in s["references"]]
    items.append({
        "id": sid, "cat": s["category"],
        "dev": s["name_devanagari"], "dev_short": dev_short,
        "iast": s["name_iast"], "modern": s["modern_star"],
        "conf": s["identification_confidence"], "see_also": s["see_also"],
        "label": dev_short, "kind": kind,
        "ra": ra, "dec": dec, "mag": mag,
        "road": road, "galacticL": gal,
        "plotnote": html.escape(plotnote) if plotnote else None,
        "refs": refs,
    })

# Sanity: everything is either a point, a road, on the galaxy, or an explicitly
# non-plottable category — nothing falls through silently.
NON_PLOT_CATS = {"collective", "shishumara-position", "sky-region", "star-road", "star-word"}
stray = [s["id"] for s in DB["stars"]
         if s["id"] not in P and s["id"] not in ROADS and s["id"] not in GALACTIC
         and s["category"] not in NON_PLOT_CATS and s["id"] not in UNPLOTTED_NOTE]
assert not stray, f"no plotting rule for: {stray}"
# Roads must point at ids that exist and have coordinates
for rid, stops in ROADS.items():
    for st in stops:
        assert st in P, f"road {rid} references unplotted {st}"

about = (
    "<p>Every mark on this chart is an entry in a hand-built database of star names drawn from primary Sanskrit "
    "texts, spanning roughly 1500 BCE to 1150 CE. Positions are modern J2000 coordinates for the star each verse "
    "is understood to name; marker size grows with apparent brightness.</p>"
    "<p><b>How to read the marks.</b> Filled circles and diamonds are single stars. Dashed rings are asterisms — "
    "groups of stars, plotted at the group's position. Dashed gold lines are the Purāṇic <i>star-roads</i> "
    "(vīthī), each drawn through its own three nakshatras. The soft band is the Milky Way, computed as the "
    "galactic equator from the J2000 galactic pole; the three Sanskrit names for it sit on that band.</p>"
    "<p><b>What is deliberately not plotted.</b> The Purāṇas name many positions on the body of the Śiśumāra, the "
    "celestial porpoise, but never say which visible star any of them is. Those names are in the Index rather "
    "than pinned to a guess — every limb-to-star chart in circulation is modern reconstruction. The same goes for "
    "named sky-regions (Viṣṇupada, the mārgas) and for Bhāskara's collective star-catalog.</p>"
    "<p><b>What the texts actually give.</b> The Vedic texts name asterisms and deities but never coordinates; "
    "the siddhāntas give a position for one junction star (yogatārā) per nakshatra. Modern equations rest on those "
    "siddhāntic positions — chiefly Burgess's 1860 analysis of the Sūrya Siddhānta — and on continuous tradition. "
    "The <i>confidence</i> badge on each entry records where that chain is firm and where scholars disagree.</p>"
    "<p><b>Two findings worth stating plainly.</b> The Āryabhaṭīya names no individual stars at all — verified "
    "against both W.E. Clark's 1930 translation and the full Sanskrit text — so it contributes nothing here. And "
    "the Ṛgveda names almost none: an exhaustive search of the Aufrecht text yields only the Bears (ṛkṣāḥ), the "
    "archaic Aghā and Arjunī of the wedding hymn, and Tiṣya twice. Its Agastya is always the sage, never Canopus.</p>"
    "<p><b>Sources.</b> Sanskrit copied verbatim from Sanskrit Wikisource and GRETIL; translations are "
    "public-domain (Burgess 1860, Iyer 1884, Keith 1914/1920, Eggeling 1882, Whitney 1905, Griffith 1896, "
    "Oldenberg 1886, Wilson 1840, Colebrooke 1805, Sanyal 1930s, Wilkinson &amp; Sastri 1861). Copyrighted "
    "translations are paraphrased and cited, never quoted. Where no published translation exists, the rendering "
    "is labelled as the compiler's own.</p>"
    "<p>Full database with every caveat, and the Śiśumāra mapping table: <code>docs/star-names/</code> in the "
    "repository (README.md and star-names.json).</p>"
)

DATA = {"items": items, "about": about}
out = TPL.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
open("/Users/alokm/dev/bhagol/docs/star-names/sky-chart.html", "w").write(out)
print(f"points={sum(1 for i in items if i['ra'] is not None)} "
      f"roads={sum(1 for i in items if i['road'])} "
      f"galactic={sum(1 for i in items if i['galacticL'] is not None)} "
      f"index-only={sum(1 for i in items if i['ra'] is None and not i['road'] and i['galacticL'] is None)} "
      f"total={len(items)}")
