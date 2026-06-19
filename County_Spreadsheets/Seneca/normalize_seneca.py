#!/usr/bin/env python3
"""
Seneca County Normalization Script — Stage 3
Fills seneca_ohio_pipeline_config.json from seneca_ohio_raw_discovery.yaml.
Run from project root:
  python "County_Spreadsheets/Seneca/normalize_seneca.py"
"""
import sys, json, yaml, pathlib, re, ast
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

BASE        = pathlib.Path(r"D:\users\user1\Documents\CP Projects\Natural Areas Project v5")
YAML_PATH   = BASE / "County_Spreadsheets/Seneca/seneca_ohio_raw_discovery.yaml"
CONFIG_PATH = BASE / "County_Spreadsheets/Seneca/seneca_ohio_pipeline_config.json"

# ---------------------------------------------------------------------------
# FEATURE MAP  (canonical from na_feature_mapper_reference.md + Seneca additions)
# Declaration order = match priority. First match wins per IMP-026.
# ---------------------------------------------------------------------------
FEATURE_MAP = [
    # --- most-specific patterns first ---
    (r'outdoor classroom',                      "Outdoor Classroom"),
    (r'interpretive sign|interpretive signage|interpretive exhibit'
     r'|interpretive trail|self.guided interpretive',
                                                "Interpretive Exhibit"),
    (r'hiking trail|walking trail|walking path|winding trail|nature trail'
     r'|loop trail|trail system|woodland trail|foot trail'
     r'|paved trail|paved walk|paved path|brick.paved trail|stone walking trail'
     r'|exercise trail|walking loop',           "Hiking Trail"),
    (r'boardwalk',                              "Boardwalk"),
    (r'mountain bike trail',                    "Mountain Bike Trail"),
    (r'bridle trail|equestrian trail|equestrian',
                                                "Bridle Trail"),
    (r'wetland pond',                           "Pond"),
    (r'\bwetland\b',                            "Wetland"),
    (r'vernal pool',                            "Vernal Pool"),
    (r'\bfen\b',                                "Fen"),
    (r'\bmarsh\b',                              "Marsh"),
    (r'\bprairie\b',                            "Prairie"),
    (r'\bmeadow\b',                             "Meadow"),
    (r'\bgorge\b',                              "Gorge"),
    (r'\bbog\b|glacial bog',                    "Bog"),
    (r'\bpond\b',                               "Pond"),
    (r'boat ramp|launch ramp',                  "Boat Ramp"),
    (r'boat launch|watercraft|canoeing\b|kayak|paddle',
                                                "Watercraft Access"),
    (r'fishing pond|fishing lake|fishing pier|fishing dock',
                                                "Fishing Area"),
    (r'swimming beach|swim beach',              "Swimming Beach"),
    (r'swimming pool|city pool|\bpool\b',       "Swimming Pool"),
    (r'splash pad|spray pad|spray park',        "Spray Park"),
    (r'swimming\b',                             "Swimming Pool"),
    (r'\bbridge\b|footbridge|stream crossing',  "Bridge"),
    (r'\bfence\b|fenced',                       "Fence"),
    (r'pavilion|shelter house|open air pavilion'
     r'|rentable.shelter|covered seating',      "Pavilion"),
    (r'picnic area|picnic spot|picnic table',   "Picnic Area"),
    (r'gazebo',                                 "Gazebo"),
    (r'baseball|softball',                      "Ball Diamond"),
    (r'basketball court|\bbasketball\b',        "Basketball Court"),
    (r'tennis court|\btennis\b',                "Tennis Court"),
    (r'pickleball court|\bpickleball\b',        "Pickleball Court"),
    (r'volleyball court|sand volleyball|\bvolleyball\b',
                                                "Volleyball Court"),
    (r'soccer field|soccer complex|\bsoccer\b', "Soccer Pitch"),
    (r'football field|\bfootball\b',            "Football Field"),
    (r'disc golf',                              "Disc Golf Course"),
    (r'skate park|skate ramp',                  "Skate Park"),
    (r'miniature golf|mini.?golf',              "Mini Golf"),
    (r'bocce\b',                                "Bocce Court"),
    (r'horseshoe',                              "Horseshoe Pitch"),
    (r'playground|play equipment',              "Playground"),
    (r'sledding hill',                          "Sledding Hill"),
    (r'archery',                                "Archery Range"),
    (r'ropes course|high ropes',                "Ropes Course"),
    (r'shooting sports|shooting range',         "Shooting Range"),
    (r'dog park|off.leash.*dog|dog.*run',       "Dog Park"),
    (r'restroom|flush toilet|portable toilet'
     r'|bathroom|heated restroom',             "Restrooms"),
    (r'parking',                                "Parking Lot"),
    (r'bike rack',                              "Bike Rack"),
    (r'kiosk|information kiosk',                "Kiosk"),
    (r'camping|campsite',                       "Camping"),
    (r'cabin|camper cabin|yurt',                "Cabin Rentals"),
    (r'ADA.compliant|ADA accessible|wheelchair'
     r'|accessible playground',                "ADA Accessible"),
    (r'observation deck',                       "Observation Deck"),
    (r'hunting area|public hunting|waterfowl hunting',
                                                "Hunting Area"),
    (r'wildlife viewing|wildlife.*observation|wildlife.*view',
                                                "Wildlife Observation Area"),
    (r'bird.*watch|birding|bird.*view',         "Bird Viewing Area"),
    (r'golf course|18.hole|hole.*golf|driving range'
     r'|putting green|chipping',               "Golf Course"),
    (r'fire ring|fire circle|fire pit',         "Fire Ring"),
    (r'amphitheatre|amphitheater',              "Amphitheater"),
    (r'show cave|cave\b|cavern\b',              "Cave or Cavern"),
    (r'community garden|seeds of hope',         "Community Garden"),
    (r'fitness\b|health trail|exercise track'
     r'|fitness station',                      "Fitness Station"),
    (r'outdoor art|art installa|totem pole',    "Outdoor Art Installation"),
    (r'ohio hist.*marker|historical marker'
     r'|historic.*marker',                     "Historic Marker"),
    (r'historic.*house|historic.*church'
     r'|historic.*build|historic.*struct',     "Historic Structure"),
    (r'\boverlook\b',                           "Overlook (built)"),
    (r'\blodge\b',                              "Lodge"),
    (r'pollinator garden',                      "Pollinator Garden"),
    (r'prairie restoration|habitat restoration',"Habitat Restoration Area"),
    (r'historic.*ruin|building ruin',           "Building Ruins"),
    (r'historic.*depot|train depot|caboose'
     r'|railroad artifact',                    "Historic Structure"),
    (r'war memorial|memorial statue|monument'
     r'|WWI|military monument',               "Monument"),
    (r'nature center|nature lab',               "Nature Center"),
    (r'recreation center|community center'
     r'|community centre',                     "Community Center"),
    (r'guided.*tour|wagon tour|tractor.*tour',  "Guided Tours"),
]

# Named trail entities to strip from features (not infrastructure)
_NAMED_TRAIL_RE = re.compile(
    r'rock creek trail|tiffin storybook trail|wetland loop trail'
    r'|h2ohio loop trail|storybook trail|clary boulee'
    r'|sandusky.*scenic.*river trail',
    re.IGNORECASE
)


def map_features(features_raw_value):
    """Map features_raw list/str to sorted semicolon-delimited vocab string."""
    if not features_raw_value:
        return ""
    items = features_raw_value if isinstance(features_raw_value, list) else []
    if not items and isinstance(features_raw_value, str):
        try:
            items = ast.literal_eval(features_raw_value)
        except Exception:
            items = [features_raw_value]
    result = set()
    for item in items:
        if _NAMED_TRAIL_RE.search(item):
            continue  # named trail entity — omit from features
        il = item.lower()
        for pattern, vocab_term in FEATURE_MAP:
            if re.search(pattern, il, re.IGNORECASE):
                result.add(vocab_term)
                break  # first match wins
    return ";".join(sorted(result)) if result else ""


def parse_urls(urls_raw):
    """Return (url_primary, url_secondary_semicolon) from urls_raw."""
    if not urls_raw:
        return "", ""
    urls = urls_raw if isinstance(urls_raw, list) else [str(urls_raw)]
    urls = [u for u in urls if u]
    return (urls[0], ";".join(urls[1:])) if urls else ("", "")


def clean_desc(s):
    """Strip pipeline metadata markers from description_raw (IMP-053)."""
    if not s:
        return ""
    for p in (r'\[T\d\]\s*', r'IMP-\d+:?\s*',
              r'OBJECTID\s*=\s*[\d\.]+\s*', r'GPS pending[^.]*\.\s*'):
        s = re.sub(p, '', s, flags=re.IGNORECASE)
    return s.strip()


def parse_acres(val):
    if val is None:
        return None
    try:
        return float(val)
    except (TypeError, ValueError):
        return None


def parse_partners(val):
    if not val:
        return ""
    if isinstance(val, list):
        return ";".join(str(v) for v in val if v)
    return str(val)


# ---------------------------------------------------------------------------
# CEMETERY SUBTYPE INFERENCE (§7.4)
# ---------------------------------------------------------------------------
_CHURCH_OWN_KW = [
    "parish", "diocese", "church", "lutheran", "catholic", "methodist",
    "baptist", "mennonite", "dunkard", "brethren", "reformed", "episcopal",
    "evangelical", "presbyterian", "congregation",
]
_RELIGIOUS_NAMES = [
    "saint ", "st.", "saints ", "assumption", "holy ", "trinity",
    "resurrection", "zion ", "bethel", "shiloh", "ebenezer", "jerusalem",
    "methodist", "lutheran ", "dunkard", "mennonite ", "reformed ", "baptist",
    "caroline",   # Caroline Lutheran Cemetery
]
_GOV_KW = [
    "township", "municipality", "county", "village", "city", "state", "federal",
    "board of trustees", "trustee",
]


def infer_cemetery_subtype(name, own_raw, gov_raw):
    n = name.lower()
    o = (own_raw or "").lower()
    g = (gov_raw or "").lower()

    # Rule 1 — National Cemetery
    if "national cemetery" in n:
        return "Veterans Cemetery"
    # Rule 2 — Veterans / Soldiers / GAR
    if any(kw in n for kw in ("veteran", "soldier", " gar ", "g.a.r.")):
        return "Veterans Cemetery"
    # Rule 3 — Church governance or name
    # Guard: don't fire on 'congregation' in own_raw/gov_raw when those
    # strings also mention "township" (indicates uncertain/OR wording, not
    # actual church ownership — e.g. "Liberty Twp (presumed) OR congregation").
    church_in_own  = any(kw in o for kw in _CHURCH_OWN_KW) and "township" not in o
    church_in_gov  = any(kw in g for kw in _CHURCH_OWN_KW) and "township" not in g
    church_in_name = any(kw in n for kw in _RELIGIOUS_NAMES)
    if church_in_own or church_in_gov or church_in_name:
        return "Church Cemetery"
    # Rule 4 — Family Cemetery
    if "family cemetery" in n or "family burial" in n:
        return "Family Cemetery"
    # Rule 5 — Green Burial
    if "green burial" in n or "natural burial" in n:
        return "Green Burial Cemetery"
    # Rule 6 — Government entity
    if any(kw in o for kw in _GOV_KW) or any(kw in g for kw in _GOV_KW):
        return "Public Cemetery"
    # Rule 7 — Default
    return "Private Cemetery"


# ---------------------------------------------------------------------------
# GOVERNANCE HELPERS
# ---------------------------------------------------------------------------
def _township_governance(gov_raw):
    """Extract 'Foo Township Board of Trustees' from a raw governance string."""
    m = re.search(
        r'([A-Z][a-z]+(?:\s[A-Z][a-z]+)*\s*Township)',
        gov_raw
    )
    if m:
        return f"{m.group(1).strip()} Board of Trustees"
    return gov_raw


def _scpd_ownership(own_raw):
    o = own_raw.lower()
    if "ohio department of natural resources" in o or "odnr" in o:
        return "State of Ohio"
    if "tiffin university" in o:
        return "Tiffin University"
    if "mercy" in o:
        return "Mercy Tiffin Hospital; Seneca County Park District"
    if "seneca county commissioners" in o:
        return "Seneca County Commissioners"
    return "Seneca County Park District"


def _extract_village_gov(gov_raw, own_raw):
    """Return 'Village of Foo Parks and Recreation' or 'Village of Foo'."""
    for src in (gov_raw, own_raw):
        m = re.search(r'(Village of [\w\s]+?)(?:\s*Parks|\s*\(|$)', src, re.IGNORECASE)
        if m:
            vname = m.group(1).strip()
            if "parks" in src.lower() or "recreation" in src.lower():
                return vname + " Parks and Recreation"
            return vname
    return gov_raw


# ---------------------------------------------------------------------------
# PARK SUB-ASSIGNMENT HELPERS
# ---------------------------------------------------------------------------
_TIFFIN_GREENSPACE = frozenset([
    "schekelhoff", "nature trail", "nature trails", "junior home", "rotary"
])
_TIFFIN_BLANK = frozenset([
    "hedges-boyer", "highland", "kernan", "east green", "tiffin east"
])


def _tiffin_park_category(name_lower):
    if any(k in name_lower for k in _TIFFIN_GREENSPACE):
        return "Park", "Greenspace"
    if any(k in name_lower for k in _TIFFIN_BLANK):
        return "Park", ""
    return "Park", "Neighborhood Park"


_FOSTORIA_BLANK = frozenset(["foundation park", "iron triangle"])


def _fostoria_park_category(name_lower):
    if "veterans memorial reservoir" in name_lower:
        return "Water Site", "Reservoir"
    if any(k in name_lower for k in _FOSTORIA_BLANK):
        return "Park", ""
    return "Park", "Neighborhood Park"


# ---------------------------------------------------------------------------
# OGE CEMETERY GOVERNANCE
# Raw OGE values use em-dash (U+2014) as a prefix delimiter:
#   ownership_raw  = "Private — Lutheran congregation (presumed)"
#   governance_raw = "Unknown — Lutheran church congregation or church body (presumed)"
# Strip the prefix and use the remainder directly.
# ---------------------------------------------------------------------------
def _oge_strip(raw_val):
    """Strip 'Private — ' or 'Unknown — ' prefix from OGE raw cemetery values."""
    return re.sub(r'^(?:Private|Unknown)\s*—\s*', '', str(raw_val or '')).strip()


def _oge_cem_ownership(name, own_raw):
    """Return ownership string with prefix stripped."""
    stripped = _oge_strip(own_raw)
    return stripped if stripped else "Private (unknown owner)"


def _oge_cem_governance(name, gov_raw):
    """Return governance string with prefix stripped; insert county before (presumed)."""
    stripped = _oge_strip(gov_raw)
    if not stripped:
        return "Unknown, Seneca County, Ohio"
    # Insert ", Seneca County, Ohio" before trailing "(presumed)"
    return re.sub(r'\s*\(presumed\)\s*$', ', Seneca County, Ohio (presumed)', stripped)


# ---------------------------------------------------------------------------
# SITE NORMALIZATION
# ---------------------------------------------------------------------------
def normalize_site(raw, site, idx):
    """Fill all normalized fields in a pipeline config site dict."""
    name    = raw.get("name_raw", "")
    tier    = raw.get("discovery_tier", 0)
    own_raw = raw.get("ownership_raw") or ""
    gov_raw = raw.get("governance_raw") or ""
    idn_raw = raw.get("identity_notes_raw") or ""
    feat_r  = raw.get("features_raw")
    urls    = parse_urls(raw.get("urls_raw"))

    # ---- universal defaults ----
    site["status"]           = "Active"
    site["counties"]         = "Seneca"
    site["access"]           = "Public"
    site["features_raw"]     = str(feat_r) if feat_r else ""
    site["features"]         = map_features(feat_r)
    site["description"]      = clean_desc(raw.get("description_raw") or "")
    site["location"]         = raw.get("location_raw") or ""
    site["acres"]            = parse_acres(raw.get("acres_raw"))
    site["url_primary"]      = urls[0]
    site["url_secondary"]    = urls[1]
    site["identity_notes"]   = idn_raw
    site["partner_agencies"] = parse_partners(raw.get("partner_agencies_raw"))
    site["coordination"]     = raw.get("coordination_raw") or ""
    site["status_flag"]      = ""
    site["hold_detail"]      = ""
    site["notes"]            = ""
    site["temp_id"]          = f"T{tier}-{name[:28]}"

    # GPS from raw if explicitly provided
    if raw.get("gps_lat_raw") is not None:
        site["gps_lat"]        = raw["gps_lat_raw"]
        site["gps_lon"]        = raw["gps_lon_raw"]
        site["gps_confidence"] = "MED"

    # ---- category / subtype / designation / ownership / governance ----
    n = name.lower()
    o = own_raw.lower()
    g = gov_raw.lower()

    if tier == 2 and "division of natural areas" in g:
        site["category"]    = "Nature Preserve"
        site["subtype"]     = "State Nature Preserve"
        site["designation"] = "State Nature Preserve"
        site["ownership"]   = "State of Ohio"
        site["governance"]  = ("Ohio Department of Natural Resources, "
                                "Division of Natural Areas and Preserves")

    elif tier == 2 and "division of wildlife" in g:
        site["category"]    = "Wildlife Area"
        site["subtype"]     = "State Wildlife Area"
        site["designation"] = "State Wildlife Area"
        site["ownership"]   = "State of Ohio"
        site["governance"]  = ("Ohio Department of Natural Resources, "
                                "Division of Wildlife")

    elif tier == 3 and "eells" in n:
        # H.P. Eells Park — governance uncertain
        site["category"]    = "Park"
        site["subtype"]     = "Neighborhood Park"
        site["designation"] = ""
        site["ownership"]   = "Municipal"
        site["governance"]  = "Village of Bettsville"
        site["status_flag"] = "GOVERNANCE_UNCERTAIN"
        site["notes"]       = ("Bettsville Recreation Board last audited 2009 — "
                                "possibly dissolved; governance may be Village of Bettsville. "
                                "Verify before pipeline advance.")

    elif tier == 3 and "seneca county park" in g:
        # All SCPD-governed T3 sites
        if "preserve" in n or "wetland" in n:
            site["category"]  = "Nature Preserve"
            site["subtype"]   = "County Nature Preserve"
            site["designation"] = ""
        elif "river access" in n or "mill" in n:
            site["category"]  = "Park"
            site["subtype"]   = "Greenspace"
            site["designation"] = ""
        else:
            # Opportunity Park
            site["category"]  = "Park"
            site["subtype"]   = ""
            site["designation"] = ""
        site["ownership"]   = _scpd_ownership(own_raw)
        site["governance"]  = "Seneca County Park District"

    elif tier == 5:
        if "cemetery" in n:
            site["category"]    = "Cemetery"
            site["subtype"]     = infer_cemetery_subtype(name, own_raw, gov_raw)
            site["designation"] = ""
            site["ownership"]   = "Township"
            site["governance"]  = _township_governance(gov_raw)
        else:
            # Meadowbrook Park (only non-cemetery T5 entity)
            site["category"]    = "Park"
            site["subtype"]     = ""
            site["designation"] = ""
            site["ownership"]   = "Township"
            site["governance"]  = _township_governance(gov_raw)

    elif tier == 6 and "city of tiffin" in o:
        cat, sub = _tiffin_park_category(n)
        site["category"]    = cat
        site["subtype"]     = sub
        site["designation"] = ""
        site["ownership"]   = "Municipal"
        site["governance"]  = "City of Tiffin Parks and Recreation Department"

    elif tier == 6 and "city of fostoria" in o:
        cat, sub = _fostoria_park_category(n)
        site["category"]    = cat
        site["subtype"]     = sub
        site["designation"] = ""
        site["ownership"]   = "Municipal"
        site["governance"]  = "City of Fostoria Parks and Recreation"

    elif tier == 6 and ("village of" in o or "village of" in g):
        site["category"]    = "Park"
        site["subtype"]     = "Neighborhood Park"
        site["designation"] = ""
        site["ownership"]   = "Municipal"
        site["governance"]  = _extract_village_gov(gov_raw, own_raw)

    elif tier == 8 and any(kw in n for kw in ("golf", "country club")):
        site["category"]    = "Recreation Facility"
        site["subtype"]     = "Golf Course"
        site["designation"] = ""
        site["ownership"]   = "Private"
        site["governance"]  = _golf_gov(name)
        if any(kw in g for kw in ("members-only", "private country club",
                                   "private members", "member-owned")):
            site["access"] = "No Public Entry"

    elif tier == 8 and "cavern" in n:
        site["category"]    = "Natural Area"
        site["subtype"]     = ""
        site["designation"] = "State Natural Landmark"
        site["ownership"]   = "Private"
        site["governance"]  = "Seneca Caverns (private)"

    elif tier == 8 and ("pittenger" in n or "nwocyc" in n):
        site["category"]    = "Recreation Facility"
        site["subtype"]     = ""
        site["designation"] = ""
        site["ownership"]   = "Northwestern Ohio Christian Youth Camp, Inc. (NWOCYC)"
        site["governance"]  = "Northwestern Ohio Christian Youth Camp, Inc. (NWOCYC)"
        site["access"]      = "No Public Entry"

    elif tier == 8 and "franciscan" in n:
        site["category"]    = "Conservation Area"
        site["subtype"]     = "Stewardship Area"
        site["designation"] = ""
        site["ownership"]   = "Sisters of St. Francis of Tiffin"
        site["governance"]  = "Franciscan Earth Literacy Center"

    elif tier == 8 and "camp glen" in n:
        site["category"]    = "Recreation Facility"
        site["subtype"]     = ""
        site["designation"] = ""
        site["ownership"]   = "Camp Fire Sandusky County"
        site["governance"]  = "Camp Fire Sandusky County"

    elif tier == 8 and "greenlawn" in n:
        site["category"]    = "Cemetery"
        site["subtype"]     = "Private Cemetery"
        site["designation"] = ""
        site["ownership"]   = "Greenlawn Cemetery Association"
        site["governance"]  = "Greenlawn Cemetery Association"

    elif tier == 8 and "fairmont" in n:
        site["category"]    = "Cemetery"
        site["subtype"]     = "Private Cemetery"
        site["designation"] = ""
        site["ownership"]   = "Fairmont Cemetery Association"
        site["governance"]  = "Fairmont Cemetery Association"

    elif tier == 8 and "memory gardens" in n:
        site["category"]    = "Cemetery"
        site["subtype"]     = "Private Cemetery"
        site["designation"] = ""
        site["ownership"]   = "Private"
        site["governance"]  = "Seneca Memory Gardens (private partnership)"

    elif tier == 8 and "cemetery" in n:
        # OGE GNIS cemeteries
        site["category"]    = "Cemetery"
        site["subtype"]     = infer_cemetery_subtype(name, own_raw, gov_raw)
        site["designation"] = ""
        site["ownership"]   = _oge_cem_ownership(name, own_raw)
        site["governance"]  = _oge_cem_governance(name, gov_raw)

    else:
        site["category"]    = ""
        site["subtype"]     = ""
        site["designation"] = ""
        site["ownership"]   = own_raw
        site["governance"]  = gov_raw

    # ---- entity-specific overrides ----
    _apply_site_overrides(site)


def _golf_gov(name):
    n = name.lower()
    if "mohawk" in n:     return "Mohawk Golf and Country Club"
    if "loudon" in n:     return "Loudon Meadows Golf Club"
    if "clinton heights" in n: return "Clinton Heights Golf Course"
    if "lakeland" in n:   return "Lakeland Golf Course"
    if "seneca hills" in n: return "Seneca Hills Golf Course (private)"
    return "Private golf course"


def _apply_site_overrides(site):
    """Apply per-entity-ID overrides after general normalization."""
    sid = site["site_id"]

    # OH-SEN-S-069 — Seneca Hills GC: status conflict
    if sid == "OH-SEN-S-069":
        site["status"]      = "Closed"
        site["status_flag"] = "STATUS_CONFLICT"
        site["notes"]       = ("Golf Digest lists as permanently closed; "
                                "GolfNow still shows as active as of 2026. "
                                "Field verification required.")

    # OH-SEN-S-068 — Mohawk G&CC: members-only
    elif sid == "OH-SEN-S-068":
        site["access"] = "No Public Entry"

    # OH-SEN-S-067 — Loudon Meadows GC: members-only
    elif sid == "OH-SEN-S-067":
        site["access"] = "No Public Entry"

    # OH-SEN-S-098 — Zion Lutheran Cemetery: dedup candidate
    elif sid == "OH-SEN-S-098":
        site["status_flag"] = "DEDUP_CANDIDATE"
        site["notes"]       = ("May duplicate T5 Zion Cemetery (OH-SEN-S-023, "
                                "Jackson Township). Verify name, location, and "
                                "governance before pipeline advance.")

    # OH-SEN-S-100 — Attica Cemetery: dedup candidate
    elif sid == "OH-SEN-S-100":
        site["status_flag"] = "DEDUP_CANDIDATE"
        site["notes"]       = ("May duplicate T5 Attica-Venice Township Joint Cemetery "
                                "(OH-SEN-S-026). Verify name, location, and governance "
                                "before pipeline advance.")

    # OH-SEN-S-104 — Bloomville Cemetery: possible T6 governance
    elif sid == "OH-SEN-S-104":
        site["status_flag"] = "GOVERNANCE_FLAG"
        site["notes"]       = ("Name suggests possible Village of Bloomville governance "
                                "(T6 re-tier candidate). Verify with parcel data "
                                "before pipeline advance.")

    # OH-SEN-S-109 — County Home Cemetery: possible T4 governance
    elif sid == "OH-SEN-S-109":
        site["status_flag"] = "GOVERNANCE_FLAG"
        site["subtype"]     = "Public Cemetery"   # county ownership likely
        site["notes"]       = ("Possible T4 entity — historic Seneca County "
                                "infirmary/poorhouse cemetery. Verify ownership with "
                                "Seneca County parcel data before pipeline advance.")


# ---------------------------------------------------------------------------
# TRAIL NORMALIZATION
# ---------------------------------------------------------------------------
def normalize_trail(raw, trail, idx):
    """Fill all normalized fields in a pipeline config trail dict."""
    name    = raw.get("name_raw", "")
    tier    = raw.get("discovery_tier", 0)
    own_raw = raw.get("ownership_raw") or ""
    gov_raw = raw.get("governance_raw") or ""
    idn_raw = raw.get("identity_notes_raw") or ""
    urls    = parse_urls(raw.get("urls_raw"))

    # ---- universal defaults ----
    trail["status"]           = "Active"
    trail["counties"]         = "Seneca"
    trail["description"]      = clean_desc(raw.get("description_raw") or "")
    trail["url_primary"]      = urls[0]
    trail["maps"]             = urls[1]
    trail["identity_notes"]   = idn_raw
    trail["partner_agencies"] = parse_partners(raw.get("partner_agencies_raw"))
    trail["status_flag"]      = ""
    trail["hold_detail"]      = ""
    trail["notes"]            = ""
    trail["temp_id"]          = f"T{tier}-TRAIL-{name[:25]}"
    trail["accessibility"]    = raw.get("accessibility_raw") or ""
    trail["alternate_names"]  = ""
    trail["trail_history"]    = ""
    trail["difficulty"]       = ""
    trail["length_mi"]        = None
    trail["parent_site_id"]   = ""
    trail["network_ids"]      = ""
    trail["segment_ids"]      = ""
    trail["township"]         = ""
    trail["municipality"]     = ""
    trail["gps_lat"]          = None
    trail["gps_lon"]          = None
    trail["gps_confidence"]   = "NONE"

    n = name.lower()

    # T-001: Sandusky State Scenic River (cross-county Water trail)
    if "sandusky" in n and "scenic river" in n:
        trail["use_type"]     = "Water"
        trail["surface_type"] = "Water"
        trail["origin_type"]  = ""
        trail["length_mi"]    = 65.0
        trail["status"]       = "Active"
        trail["counties"]     = "Sandusky;Seneca;Wyandot"
        trail["ownership"]    = "Multiple"
        trail["governance"]   = ("Ohio Department of Natural Resources, "
                                  "Ohio Scenic Rivers Program")
        trail["status_flag"]  = "CROSS_COUNTY_CANDIDATE"
        trail["hold_detail"]  = ("Multi-county trail (Sandusky;Seneca;Wyandot): held "
                                  "pending cross-county resolution "
                                  "(Scenario A — partner counties not yet run)")
        trail["notes"]        = ("State Scenic River designation 1970. "
                                  "Designation: State Scenic River. "
                                  "Water trail / paddling corridor.")

    # T-002: Rock Creek Trail
    elif "rock creek trail" in n:
        trail["use_type"]     = "Hiking"
        trail["surface_type"] = "Paved"
        trail["origin_type"]  = "Purpose-Built"
        trail["length_mi"]    = 2.0
        trail["ownership"]    = "Municipal"
        trail["governance"]   = "City of Tiffin Parks and Recreation Department"
        trail["partner_agencies"] = "Heidelberg University"

    # T-003: Clary Boulee Wetland Loop Trail
    elif "wetland loop" in n:
        trail["use_type"]       = "Hiking"
        trail["surface_type"]   = "Natural Surface"
        trail["origin_type"]    = "Purpose-Built"
        trail["length_mi"]      = 1.0
        trail["ownership"]      = "Seneca County Park District"
        trail["governance"]     = "Seneca County Park District"
        trail["parent_site_id"] = "OH-SEN-S-060"
        trail["notes"]          = ("No official trail name; name is descriptive per "
                                    "discovery notes.")

    # T-004: Clary Boulee H2Ohio Loop Trail
    elif "h2ohio" in n:
        trail["use_type"]       = "Hiking"
        trail["surface_type"]   = "Natural Surface"
        trail["origin_type"]    = "Purpose-Built"
        trail["length_mi"]      = 0.4
        trail["ownership"]      = "Seneca County Park District"
        trail["governance"]     = "Seneca County Park District"
        trail["parent_site_id"] = "OH-SEN-S-060"
        trail["notes"]          = ("No official trail name; name is descriptive per "
                                    "discovery notes. H2Ohio water quality improvement "
                                    "program trail.")

    else:
        trail["use_type"]     = ""
        trail["surface_type"] = ""
        trail["origin_type"]  = ""
        trail["ownership"]    = own_raw
        trail["governance"]   = gov_raw


# ---------------------------------------------------------------------------
# GPS QUERIES
# ---------------------------------------------------------------------------
def populate_gps_queries(config, raw_sites, raw_trails):
    """Fill gps_queries with Nominatim-ready query strings where addresses exist."""
    gq = config.setdefault("gps_queries", {})

    for raw, site in zip(raw_sites, config["sites"]):
        sid  = site["site_id"]
        loc  = raw.get("location_raw") or ""
        name = raw.get("name_raw", "")
        # Use verbatim address if it starts with a number
        if re.match(r'\d+\s+\w', loc):
            gq[sid] = loc
        elif loc:
            gq[sid] = f"{name}, Seneca County, Ohio"
        else:
            gq[sid] = f"{name}, Seneca County, Ohio"

    for raw, trail in zip(raw_trails, config["trails"]):
        tid  = trail.get("trail_id", "")
        name = raw.get("name_raw", "")
        loc  = raw.get("location_raw") or ""
        n    = name.lower()
        if "sandusky" in n and "scenic river" in n:
            gq[tid] = ""  # water trail — GPS not applicable
        elif loc and re.match(r'\d+', loc):
            gq[tid] = loc
        else:
            gq[tid] = f"{name}, Seneca County, Ohio"

    config["gps_queries"] = gq


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    raw_data = yaml.safe_load(YAML_PATH.read_text(encoding='utf-8'))
    records  = raw_data['records']
    config   = json.loads(CONFIG_PATH.read_text(encoding='utf-8'))

    raw_sites  = [r for r in records if r['entity_type'] == 'Site']
    raw_trails = [r for r in records if r['entity_type'] == 'Trail']

    assert len(raw_sites)  == len(config['sites']), (
        f"Site count mismatch: {len(raw_sites)} raw vs {len(config['sites'])} config")
    assert len(raw_trails) == len(config['trails']), (
        f"Trail count mismatch: {len(raw_trails)} raw vs {len(config['trails'])} config")

    print(f"Normalizing {len(raw_sites)} sites and {len(raw_trails)} trails...")

    for i, (raw, site) in enumerate(zip(raw_sites, config['sites'])):
        normalize_site(raw, site, i)
        if (i + 1) % 25 == 0:
            print(f"  Sites: {i+1}/{len(raw_sites)} done")

    for j, (raw, trail) in enumerate(zip(raw_trails, config['trails'])):
        normalize_trail(raw, trail, j)

    populate_gps_queries(config, raw_sites, raw_trails)

    config['run_date']  = datetime.now().strftime('%Y-%m-%d')
    config['run_notes'] = (
        'Normalization pass complete 2026-05-28. '
        'GPS acquisition pending. '
        'Township/municipality GIS lookup pending.'
    )

    CONFIG_PATH.write_text(
        json.dumps(config, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )

    # Summary
    sites  = config['sites']
    trails = config['trails']
    cats   = {}
    for s in sites:
        c = s.get('category') or '(blank)'
        cats[c] = cats.get(c, 0) + 1
    held_trails = [t for t in trails if t.get('hold_detail')]
    flagged = [s for s in sites if s.get('status_flag')]

    print(f"\nDONE — {len(sites)} sites, {len(trails)} trails normalized.")
    print(f"\nCategory distribution:")
    for k, v in sorted(cats.items(), key=lambda x: -x[1]):
        print(f"  {k:<30} {v}")
    print(f"\nFlagged sites: {len(flagged)}")
    for s in flagged:
        print(f"  {s['site_id']}  {s['status_flag']:<26}  {s['name']}")
    print(f"\nHeld trails: {len(held_trails)}")
    for t in held_trails:
        print(f"  {t.get('trail_id','')}  {t['name']}")
    print(f"\nSaved → {CONFIG_PATH}")


if __name__ == "__main__":
    main()
