"""Canonical sky-objects for the vernacular database.

The seven research files were written independently and name the same object 246
different ways ("the Pleiades", "Pleiades", "The Pleiades", "Krittika / the
Pleiades"). Grouping is by OBJECT, because the question this database answers is
what the different languages call one thing — so the object, not the Sanskrit
name, is the primary key. `sanskrit_db_id` is carried along where a source
supplied one, but it cannot be the key: 181 of 522 entries have none, which is
the whole point of the tribal and vernacular material.
"""
import re

# Longest match wins, so order matters: "orion's belt" must be tested before "orion".
RULES = [
    ("orions-belt",   r"orion'?s? belt|belt of orion|three kings"),
    ("orion",         r"\borion\b|mrigashirsha|mriga[sś]iras|kalpurush|k[aā]lapuru[sṣ]a"),
    ("pleiades",      r"pleiad|krittika|k[rṛ]ttik[aā]|kārttikai"),
    ("ursa-major",    r"ursa major|great bear|big dipper|charles'?s? wain|saptar[sṣ]|seven sages|seven brothers|plough \(constellation\)"),
    ("alcor",         r"alcor|arundhat"),
    # Before ursa-minor: nearly every entry here is about the pole star itself, and
    # carries "Ursa Minor" only in its modern_star.constellation field. Tested the
    # other way round, the constellation swallows the star and the label lies.
    ("pole-star",     r"pole ?star|polar ?star|north ?star|dhruva|pole of the sky"),
    ("ursa-minor",    r"ursa minor|little bear"),
    ("milky-way",     r"milky ?way|galaxy|ak[aā][sś]agang|via lactea"),
    ("venus-morning", r"morning ?star|venus as (the )?morning|dawn ?star"),
    ("venus-evening", r"evening ?star|venus as (the )?evening"),
    ("venus",         r"\bvenus\b|shukra|[sś]ukra"),
    ("canopus",       r"canopus|agastya|agasti"),
    ("sirius",        r"sirius|dog ?star|lubdhaka|mrigavyadha"),
    ("arcturus",      r"arcturus|sv[aā]t[iī]"),
    ("antares",       r"antares|jyeshtha|jye[sṣ][tṭ]h"),
    # Before aldebaran: the Hyades entries name Aldebaran among their stars, and
    # tested the other way round the brightest member swallows the cluster.
    ("hyades",        r"hyades"),
    ("aldebaran",     r"aldebaran|rohini|rohi[nṇ][iī]"),
    ("betelgeuse",    r"betelgeuse|ardra|[aā]rdr[aā]"),
    # After both, so a Hyades or Aldebaran entry is not swallowed by its constellation.
    # \b on both sides of "tauri" — without the leading one it also eats "Centauri".
    ("taurus",        r"\btaurus\b|\btauri\b"),
    ("crux",          r"\bcrux\b|southern cross"),
    ("canis-major",   r"canis major"),
    ("corona-australis", r"corona austral"),
    ("direction",     r"quarter of the horizon|cardinal direction"),
    ("sky-motion",    r"turning of the stars|rotation of the stars"),
    ("rainbow",       r"rainbow"),
    ("comet",         r"comet"),
    ("eclipse",       r"eclipse"),
    ("sky-measure",   r"unit of measure|altitude of the sun|measuring the sky"),
    ("meteor",        r"meteor|shooting ?star|falling ?star"),
    ("saturn",        r"saturn|shani|[sś]ani"),
    ("jupiter",       r"jupiter|brihaspati|b[rṛ]haspati"),
    ("mars",          r"\bmars\b|mangala|[aā][nṅ]g[aā]raka"),
    ("mercury",       r"mercury|budha"),
    ("moon",          r"\bmoon\b|chandra|candra"),
    ("sun",           r"\bsun\b(?! *dial)|surya|s[uū]rya"),
    ("zodiac",        r"zodiac|rashi|r[aā][sś]i"),
    ("lunar-mansion", r"lunar mansion|naksh?atra|nak[sṣ]atra|asterism \(generic|the 27|twenty-seven"),
    ("constellation", r"constellation \(generic|constellation$|generic word for constellation"),
    ("star-generic",  r"star \(generic|generic word for star|star$|stars$"),
    ("sky",           r"\bsky\b|firmament|heavens"),
    ("planet",        r"planet"),
    ("season-marker", r"rain[- ]?asterism|agricultural|sowing|monsoon|season"),
]
COMPILED = [(k, re.compile(p, re.I)) for k, p in RULES]

TITLES = {
    "orions-belt": "Orion's Belt", "orion": "Orion", "pleiades": "The Pleiades",
    "ursa-major": "Ursa Major (the Big Dipper)", "ursa-minor": "Ursa Minor",
    "alcor": "Alcor (and Mizar)", "pole-star": "The pole star",
    "milky-way": "The Milky Way", "venus-morning": "Venus as morning star",
    "venus-evening": "Venus as evening star", "venus": "Venus",
    "canopus": "Canopus", "sirius": "Sirius", "arcturus": "Arcturus",
    "antares": "Antares", "aldebaran": "Aldebaran", "betelgeuse": "Betelgeuse",
    "hyades": "The Hyades", "taurus": "Taurus", "crux": "Crux (the Southern Cross)",
    "canis-major": "Canis Major", "corona-australis": "Corona Australis",
    "eclipse": "Eclipses", "sky-measure": "Measuring the sky",
    "comet": "Comets", "meteor": "Meteors and shooting stars",
    "saturn": "Saturn", "jupiter": "Jupiter", "mars": "Mars", "mercury": "Mercury",
    "moon": "The Moon", "sun": "The Sun", "zodiac": "The zodiac",
    "lunar-mansion": "The lunar mansions as a system", "constellation": "'Constellation' as a word",
    "star-generic": "'Star' as a word", "sky": "'Sky' as a word", "planet": "'Planet' as a word",
    "season-marker": "Seasonal and agricultural star-markers",
    "direction": "Directions taken from the sky",
    "sky-motion": "The turning of the sky", "rainbow": "The rainbow",
    "other": "Other and unclassified",
}

# Individual stars and constellations that the rules above don't reach. Tested
# only after them, so "Vega / the constellation Lyra" lands on vega, not lyra.
EXTRA = [
    ("vega", r"\bvega\b|abhijit"), ("capella", r"capella|brahmahridaya|brahmah[rṛ]daya"),
    ("altair", r"altair|shravana|[sś]rava[nṇ]a"), ("spica", r"spica|chitra|citr[aā]"),
    ("corvus", r"corvus|hasta"), ("regulus", r"regulus|magha|magh[aā]"),
    ("castor-pollux", r"castor|pollux|punarvasu|gemini"), ("praesepe", r"praesepe|pushya|pu[sṣ]ya|cancer"),
    ("scorpius", r"scorpi"), ("lyra", r"\blyra\b"), ("aquila", r"aquila"),
    ("pegasus", r"pegasus|alpheratz"), ("auriga", r"auriga"), ("lupus", r"lupus"),
    ("delphinus", r"delphin"), ("monoceros", r"monoceros|the unicorn constellation"),
    ("cygnus", r"cygnus"), ("centaurus", r"centaur"), ("norma", r"norma"),
    ("cassiopeia", r"cassiopei"), ("grus", r"\bgrus\b"), ("pisces", r"\bpisces\b"),
    ("leo-virgo", r"\bleo\b|\bvirgo\b"),
]
COMPILED_EXTRA = [(k, re.compile(p, re.I)) for k, p in EXTRA]
TITLES.update({
    "vega": "Vega", "capella": "Capella", "altair": "Altair", "spica": "Spica",
    "corvus": "Corvus", "regulus": "Regulus", "castor-pollux": "Castor and Pollux",
    "praesepe": "Praesepe and Cancer", "scorpius": "Scorpius", "lyra": "Lyra",
    "aquila": "Aquila", "pegasus": "Pegasus", "auriga": "Auriga", "lupus": "Lupus",
    "cygnus": "Cygnus", "centaurus": "Centaurus", "norma": "Norma",
    "delphinus": "Delphinus", "monoceros": "Monoceros",
    "cassiopeia": "Cassiopeia", "grus": "Grus", "pisces": "Pisces",
    "leo-virgo": "Leo and Virgo",
    "unplaced-figure": "Figures with no secure modern identification",
})

def canon(entry, sanskrit_names=None):
    """Canonical object key for one source entry.

    Falls back to the entry's own `sanskrit_db_id` before giving up, so an
    individual nakshatra that no rule names still groups with its fellows
    rather than landing in a bucket called 'other'.
    """
    hay = " ".join(str(entry.get(k) or "") for k in ("sky_object", "literal_meaning"))
    mod = entry.get("modern_star") or {}
    hay += " " + " ".join(str(mod.get(k) or "") for k in ("common_name", "bayer", "constellation"))
    for key, rx in COMPILED:
        if rx.search(hay):
            return key
    for key, rx in COMPILED_EXTRA:
        if rx.search(hay):
            return key
    sid = entry.get("sanskrit_db_id")
    if sid:
        if sanskrit_names is not None:
            TITLES.setdefault("nak-" + sid, sanskrit_names.get(sid, sid))
        return "nak-" + sid
    return "unplaced-figure"
