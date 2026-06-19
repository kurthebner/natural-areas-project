#!/usr/bin/env python3
"""
normalize_hardin.py — Hardin County OH pipeline: Stages 2–5
Natural Areas Project v6 | Run: 2026-06-01 | IMP-017 validation run

Reads hardin_ohio_raw_discovery.yaml, performs resolution and normalization
for all four entity types, and writes the normalized entity lists into
hardin_config.json. Run na_run_county.py afterward for GPS gate, TSV output,
and upsert.

Usage:
    python County_Spreadsheets/Hardin/normalize_hardin.py
"""

import copy
import json
import os
import re
import sys
from datetime import datetime, timezone

import yaml

# ── Paths ────────────────────────────────────────────────────────────────────
COUNTY_DIR = os.path.dirname(os.path.abspath(__file__))
V6_ROOT    = os.path.abspath(os.path.join(COUNTY_DIR, "..", ".."))
YAML_FILE  = os.path.join(COUNTY_DIR, "hardin_ohio_raw_discovery.yaml")
CONFIG_FILE = os.path.join(COUNTY_DIR, "hardin_config.json")
UTILITIES  = os.path.join(V6_ROOT, "utilities")
sys.path.insert(0, UTILITIES)

try:
    from na_yaml_preprocess import preprocess_yaml
except ImportError:
    preprocess_yaml = None

PREFIX  = "OH-HAR"
COUNTY  = "Hardin"
RUN_ID  = "hardin_ohio_2026_06_01"
TODAY   = "2026-06-01"

# ── Vocabulary constants ─────────────────────────────────────────────────────
SITE_CATEGORIES = {
    "Campground", "Cemetery", "Community Garden", "Conservation Area",
    "Cultural Facility", "Curated Biological Site", "Fishing Area",
    "Historic Site", "Hunting Area", "Memorial", "Museum", "Natural Area",
    "Nature Preserve", "Open Space", "Park", "Recreation Facility",
    "Water Site", "Wildlife Area",
}
SITE_STATUS_VALUES = {
    "Active", "Seasonal", "Access Permit Required", "No Public Entry",
    "Under Development", "Proposed", "Abandoned", "Closed", "Defunct", "Unknown",
}
TRAILTHING_USE_TYPES  = {
    "Multi-Use", "Hiking", "Bridle", "Water", "Bicycling", "Mountain Bike",
    "BMX", "Pump Track", "Snowmobile", "Cross Country Ski", "Other",
}
TRAILTHING_SURFACES   = {
    "Paved", "Crushed Stone", "Gravel", "Natural Surface",
    "Boardwalk", "Water", "Mixed", "Other",
}
TRAILTHING_ORIGINS    = {
    "Rail Trail", "Canal Towpath", "Historic Route", "Greenway Corridor",
    "Purpose-Built", "Utility Corridor", "Roadside Corridor", "Waterway", "Other",
}
TRAILTHING_ORG_TYPES  = {
    "Federal Agency", "State Agency", "Regional Authority", "County Authority",
    "Municipal Department", "Land Trust", "Nonprofit Conservancy",
    "Trail Association", "Coordinating Body", "Other",
}
TRAILTHING_STATUSES   = {
    "Active", "Planned", "Under Construction", "Gap", "Closed",
    "Under Development", "Partially Open",
}
SN_NETWORK_TYPES = {
    "National Heritage Area", "Scenic River Corridor", "Heritage Corridor",
    "Historic Corridor", "Conservation Corridor", "Ecological Corridor",
    "Cultural Landscape Network", "Watershed Network", "Greenway Network",
    "Local Historic District", "Park District System", "Municipal Recreation System",
    "State Program Portfolio", "Federal Program Portfolio", "Land Trust Portfolio",
    "Conservation Authority Portfolio", "Nonprofit Conservation Portfolio", "Other",
}
SN_ORG_TYPES = {
    "Federal Agency", "State Agency", "Regional Authority", "County Authority",
    "Municipal Department", "Land Trust", "Nonprofit Conservancy",
    "Trail Association", "Coordinating Body", "Other",
}
SN_STATUSES = {"Active", "Inactive", "Proposed", "Discontinued"}
AP_TYPES = {
    "Trailhead", "Parking Area", "Boat Ramp", "Boat Launch",
    "Watercraft Access Point", "River Access", "Fishing Access", "Hazard Portage",
    "Bicycle Access", "Snowmobile Access", "Cross Country Ski Access",
    "Equestrian Access", "Roadside Pull-Off", "Pedestrian Entrance",
    "Vehicle Entrance", "Transit Access", "Ferry Access", "Shuttle Access",
    "Administrative Access", "Other",
}
AP_STATUSES = {"Active", "Seasonal", "Closed", "Restricted"}

# ── Feature map (canonical) ───────────────────────────────────────────────────
FEATURE_MAP = [
    (r'hiking trail|walking trail|walking path|winding trail|nature trail|loop trail|trail system|woodland trail|foot trail', "Hiking Trail"),
    (r'boardwalk',                   "Boardwalk"),
    (r'mountain bike trail',         "Mountain Bike Trail"),
    (r'bridle trail|equestrian',     "Bridle Trail"),
    (r'interpretive sign|interpretive signage|interpretive exhibit|interpretive trail|self.guided interpretive', "Interpretive Exhibit"),
    (r'wetland pond',                "Pond"),
    (r'\bwetland\b',                 "Wetland"),
    (r'\bpond\b',                    "Pond"),
    (r'\bbog\b|glacial bog',         "Bog"),
    (r'vernal pool',                 "Vernal Pool"),
    (r'boat ramp|launch ramp',       "Boat Ramp"),
    (r'boat launch|watercraft|canoe|kayak', "Watercraft Access"),
    (r'fishing pond|fishing lake|fishing pier|fishing dock', "Fishing Area"),
    (r'swimming beach|swim beach',   "Swimming Beach"),
    (r'swimming pool|city pool|\bpool\b', "Swimming Pool"),
    (r'splash pad|spray pad',        "Spray Park"),
    (r'\bbridge\b|stream crossing',  "Bridge"),
    (r'\bfence\b|fenced',            "Fence"),
    (r'pavilion|shelter house|open air pavilion|rentable.*shelter|covered seating', "Pavilion"),
    (r'picnic area|picnic spot|picnic table', "Picnic Area"),
    (r'gazebo',                      "Gazebo"),
    (r'baseball|softball',           "Ball Diamond"),
    (r'basketball court',            "Basketball Court"),
    (r'tennis court',                "Tennis Court"),
    (r'pickleball court',            "Pickleball Court"),
    (r'volleyball court|sand volleyball', "Volleyball Court"),
    (r'soccer field|soccer complex', "Soccer Pitch"),
    (r'football field',              "Football Field"),
    (r'disc golf',                   "Disc Golf Course"),
    (r'skate park|skate ramp',       "Skate Park"),
    (r'miniature golf',              "Mini Golf"),
    (r'playground|play equipment',   "Playground"),
    (r'sledding hill',               "Sledding Hill"),
    (r'horseshoe',                   "Horseshoe Pitch"),
    (r'archery',                     "Archery Range"),
    (r'ropes course|high ropes',     "Ropes Course"),
    (r'shooting sports|shooting range', "Shooting Range"),
    (r'dog park|off-leash.*dog|dog.*run', "Dog Park"),
    (r'restroom|flush toilet|portable toilet|bathroom', "Restrooms"),
    (r'parking',                     "Parking Lot"),
    (r'bike rack',                   "Bike Rack"),
    (r'kiosk|information kiosk',     "Kiosk"),
    (r'camping|campsite',            "Camping"),
    (r'cabin|camper cabin|yurt',     "Cabin Rentals"),
    (r'ADA.compliant|ADA accessible|wheelchair|handicap accessible', "ADA Accessible"),
    (r'observation deck',            "Observation Deck"),
    (r'hunting area|public hunting', "Hunting Area"),
    (r'wildlife viewing|wildlife.*observation', "Wildlife Observation Area"),
    (r'prairie restoration|habitat restoration', "Habitat Restoration Area"),
    (r'historic.*ruin|building ruin', "Building Ruins"),
    (r'historic.*depot|train depot|caboose|railroad artifact|memorial cannon|cannon', "Historic Structure"),
    (r'war memorial|memorial statue|monument|WWI|military monument|mural', "Monument"),
    (r'nature center|nature lab',    "Nature Center"),
    (r'recreation center|community center|community centre', "Community Center"),
    (r'guided.*tour|wagon tour|tractor.*tour', "Guided Tours"),
    (r'farm store|bison.*store',     "Farm Store"),
    (r'pollinator garden',           "Pollinator Garden"),
    (r'log cabin|historic cabin|cabin museum', "Historic Structure"),
    (r'stocked.*pond|stocked.*lake', "Fishing Area"),
    (r'fitness station|fitness.*bench',  "Fitness Station"),
    (r'dirt bike|bmx',               "Pump Track"),
    (r'batting cage',                "Athletic Field"),
    (r'concession',                  "Pavilion"),
    (r'bleacher',                    "Athletic Field"),
]

FEATURES_ALLOWED = {
    "ADA Accessible", "AED", "Alvar", "Amphibian Area", "Amphitheater",
    "Apiary", "Arboretum", "Archery Range", "Art Gallery", "Art Installation",
    "Athletic Field", "Ball Diamond", "Basketball Court", "Beach",
    "Bike Rack", "Bike Repair Station", "Bird Viewing Area", "Boardwalk",
    "Boat Dock", "Boat Ramp", "Bocce Court", "Bog", "Bluff", "Boathouse",
    "Bridge", "Bridle Trail", "Building Ruins", "Butterfly or Pollinator Garden",
    "Camping", "Cabin Rentals", "Canal Structure", "Cave or Cavern",
    "Cemetery Section", "Chapel", "Cliff", "Climbing Structure",
    "Community Center", "Community Garden", "Composting Station",
    "Conservatory", "Covered Shelter", "Cricket Pitch", "Culvert",
    "Dam", "Dance Floor", "Dance Performance Space", "Demonstration Farm Plot",
    "Demonstration Garden", "Disc Golf Course", "Dog Park", "Drainage Ditch",
    "Dune", "Educational Pavilion", "Electric Vehicle Charging",
    "Equestrian Arena", "Farm Store", "Fence", "Fen", "Fieldhouse",
    "Fire Ring", "Fire Tower", "Fishing Area", "Fitness Station",
    "Football Field", "Football Stadium", "Fountain", "Garage", "Garden",
    "Gate", "Gatehouse", "Gazebo", "Glacial Erratic", "Golf Course",
    "Gorge", "Greenhouse", "Grill", "Guided Tours", "Habitat Restoration Area",
    "Handball Court", "Hiking Trail", "Hilltop", "Historic Bridge",
    "Historic Canal Segment", "Historic Cemetery Section", "Historic Fence Line",
    "Historic Foundation", "Historic Lock", "Historic Marker",
    "Historic Marker Cluster", "Historic Millrace", "Historic Road Trace",
    "Historic Ruins", "Historic Structure", "Historic Well", "Horseshoe Pitch",
    "Hunting Area", "Ice Rink", "Information Board", "Insectarium",
    "Interpretive Exhibit", "Interpretive Garden", "Interpretive Sign",
    "Island", "Kiosk", "Kite Flying", "Lacrosse Field", "Lake",
    "Landmark Tree", "Levee", "Lodge", "Lookout Cabin",
    "Maintenance Building", "Marina", "Marsh", "Meadow",
    "Model Airplane Field", "Model Rocketry Field", "Mini Golf",
    "Monitoring Station", "Monument", "Mountain Bike Trail", "Multi-use Trail",
    "Museum Building", "Musical Instruments", "Musical Performance Space",
    "Native American Artifacts", "Native American Cultural Site",
    "Native American Earthwork", "Natural Arch", "Nature Center",
    "Nature Play Area", "Observation Deck", "Observation Tower",
    "Observatory", "Old-Growth Stand", "Orchard", "Outdoor Art Installation",
    "Outdoor Classroom", "Overflow Parking", "Overlook (built)",
    "Overlook (natural)", "Parking Lot", "Pavilion", "Peninsula",
    "Pickleball Court", "Picnic Area", "Picnic Shelter", "Picnic Table Cluster",
    "Pipeline Corridor", "Pioneer Historic Site", "Pioneer Re-creation",
    "Planetarium", "Playground", "Pollinator Garden", "Pond",
    "Powerline Corridor", "Prairie", "Prairie Restoration",
    "Public Art Installation", "Pump Station", "Pump Track", "Rain Garden",
    "Ravine", "Reforestation Area", "Reptile House", "Research Plot",
    "Restrooms", "Ropes Course", "Retaining Wall", "Retention Basin",
    "Ridge", "Rock Outcrop", "Scenic View", "Sculpture", "Sedge Meadow",
    "Shooting Range", "Shotgun Range", "Shuffleboard Court", "Silo",
    "Sinkhole", "Ski Slopes", "Skate Park", "Sledding Hill", "Slide",
    "Soccer Pitch", "Spillway", "Spray Park", "Spring", "Stable",
    "Stage", "Stormwater Basin", "Stream Segment", "Swimming Beach",
    "Swimming Pool", "Swing Set", "Tennis Court", "Theatre", "Topiary",
    "Trapping Area", "Transit Stop", "Trolley", "Tropical Garden",
    "Utility Corridor", "Valley", "Vegetable Garden", "Vernal Pool",
    "Via Ferrata", "Viewing Platform", "Vineyard", "Visitor Center",
    "Volleyball Court", "Wall", "Water Park", "Water Tower",
    "Watercraft Access", "Waterfall (built)", "Waterfall (natural)",
    "Waterslide", "Weather Station", "Weir", "Wetland",
    "Wetland Restoration", "Wilderness Area", "Wild Animal Rehabilitation",
    "Wildlife Observation Area", "Working Railway", "Zoo",
}

# ── Helpers ───────────────────────────────────────────────────────────────────

def map_features(features_raw: str) -> str:
    """Map features_raw to semicolon-delimited controlled vocabulary, alphabetized."""
    if not features_raw:
        return ""
    found = set()
    raw_lower = features_raw.lower()
    for pattern, canonical in FEATURE_MAP:
        if re.search(pattern, raw_lower, re.IGNORECASE):
            if canonical in FEATURES_ALLOWED:
                found.add(canonical)
    return ";".join(sorted(found))

def clean_str(val) -> str:
    if val is None:
        return ""
    return str(val).strip()

def first_url(urls_raw) -> str:
    if isinstance(urls_raw, list) and urls_raw:
        return str(urls_raw[0]).strip()
    if isinstance(urls_raw, str) and urls_raw:
        return urls_raw.strip()
    return ""

def all_urls(urls_raw) -> str:
    if isinstance(urls_raw, list):
        return ";".join(str(u).strip() for u in urls_raw if u)
    if isinstance(urls_raw, str) and urls_raw:
        return urls_raw.strip()
    return ""

def normalize_counties(counties_raw) -> str:
    if isinstance(counties_raw, list):
        return ";".join(sorted(str(c).strip() for c in counties_raw if c))
    if isinstance(counties_raw, str) and counties_raw:
        return counties_raw.strip()
    return COUNTY

def safe_float(val):
    try:
        return float(val)
    except (TypeError, ValueError):
        return None

def safe_acres(val):
    if val is None:
        return None
    s = str(val).replace("+", "").replace("~", "").replace(",", "").strip()
    try:
        return float(s.split()[0])
    except (ValueError, IndexError):
        return None

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

# ── Site normalization map ────────────────────────────────────────────────────

def normalize_site_category(raw: dict) -> tuple:
    """Returns (category, subtype, designation) based on governance/name/raw."""
    name = clean_str(raw.get("name_raw", "")).lower()
    gov  = clean_str(raw.get("governance_raw", "")).lower()
    own  = clean_str(raw.get("ownership_raw", "")).lower()
    ident = clean_str(raw.get("identity_notes_raw", "")).lower()
    tier = raw.get("discovery_tier", 0)

    # Cemetery (T5 + T8 cemeteries)
    if raw.get("entity_type") == "Site" and (tier == 5 or tier == 8):
        if "cemetery" in name or "burial" in name or "mausoleum" in name:
            # Determine subtype
            ident_str = clean_str(raw.get("identity_notes_raw", ""))
            if "archaeological" in ident_str.lower() or "burial grounds" in name.lower():
                return ("Historic Site", "Archaeological Site", "")
            if "amish" in ident_str.lower() or "church cemetery" in ident_str.lower():
                return ("Cemetery", "Church Cemetery", "")
            if "family cemetery" in ident_str.lower():
                return ("Cemetery", "Family Cemetery", "")
            if "private cemetery" in ident_str.lower():
                return ("Cemetery", "Private Cemetery", "")
            if "county home" in name.lower():
                return ("Cemetery", "Private Cemetery", "")
            if "veterans" in name.lower() or "national" in name.lower():
                return ("Cemetery", "Veterans Cemetery", "")
            # Township-owned (T5)
            if tier == 5:
                return ("Cemetery", "Public Cemetery", "Registered Cemetery")
            return ("Cemetery", "Public Cemetery", "")

    # T2 State nature preserve
    if "state nature preserve" in name.lower() or "nature preserve" in gov:
        return ("Nature Preserve", "State Nature Preserve", "State Nature Preserve")

    # T2 Wildlife areas
    if "wildlife area" in name.lower() or "division of wildlife" in gov:
        return ("Wildlife Area", "State Wildlife Area", "State Wildlife Area")

    # T3 SWCD natural area
    if "silver creek" in name.lower():
        return ("Natural Area", "", "")

    # T3 Veterans Memorial Park (park district)
    if "veterans memorial park" in name.lower() and "golf" not in name.lower():
        return ("Park", "Waterfront Park", "")

    # T3 Boy Scout Lake (child site)
    if "boy scout lake" in name.lower():
        return ("Water Site", "Pond", "")

    # T6 Campgrounds
    if "saulisberry" in name.lower():
        return ("Campground", "RV Campground", "")

    # T6 France Lake (child water site)
    if "france lake" in name.lower():
        return ("Water Site", "Lake", "")

    # T6 Recreation Facilities
    if any(x in name.lower() for x in ["home run memorial park", "ranger sports complex"]):
        return ("Recreation Facility", "Sports Complex", "")

    if "golf" in name.lower() and "club" in name.lower() or "memorial park golf" in name.lower():
        return ("Recreation Facility", "Golf Course", "")

    # T6 Memorials
    if any(x in name.lower() for x in ["gene autry", "ray brown memorial park"]):
        return ("Memorial", "Civic Memorial", "")

    if "ada railroad park" in name.lower() and "path" not in name.lower():
        return ("Historic Site", "Historic Landmark", "National Register of Historic Places (NRHP)")

    if "ada war memorial" in name.lower() or "ada memorial park" in name.lower():
        return ("Park", "Historic Park", "")

    if "gormley park" in name.lower():
        return ("Park", "Waterfront Park", "")

    if "c.e. wharton" in name.lower() or "wharton" in name.lower():
        return ("Park", "Sports Park", "")

    if any(x in name.lower() for x in ["pioneer park", "murray park"]):
        return ("Park", "Greenspace", "")

    if "village park" in name.lower() or any(x in name.lower() for x in [
        "dunkirk community park", "mcguffey village park", "mount victory village park",
        "gormley park"]):
        return ("Park", "Neighborhood Park", "")

    if "dunkirk community park" in name.lower():
        return ("Park", "Neighborhood Park", "")

    if "alger" in name.lower() and "park" in name.lower():
        return ("Memorial", "Civic Memorial", "")

    # Generic park fallback
    if "park" in name.lower() and "golf" not in name.lower():
        return ("Park", "Neighborhood Park", "")

    # Roundhead community park (unconfirmed)
    if "roundhead" in name.lower() and "unconfirmed" in name.lower():
        return ("Park", "", "")

    return ("", "", "")


def normalize_site_status(raw: dict) -> str:
    status_raw = clean_str(raw.get("status_raw", raw.get("access_notes_raw", "")))
    name = clean_str(raw.get("name_raw", "")).lower()
    tier = raw.get("discovery_tier", 0)

    if "historical" in status_raw.lower() or "historical" in name:
        return "Closed"
    if "abandoned" in status_raw.lower():
        return "Abandoned"
    if "closed" in status_raw.lower():
        return "Closed"
    if "planned" in status_raw.lower() or "proposed" in status_raw.lower():
        return "Proposed"
    if "restricted" in status_raw.lower() or "no public" in status_raw.lower():
        return "No Public Entry"
    if "permit required" in status_raw.lower():
        return "Access Permit Required"
    if "seasonal" in status_raw.lower():
        return "Seasonal"
    if tier == 8 and "gnis-only" in clean_str(raw.get("identity_notes_raw", "")).lower():
        return "Unknown"
    return "Active"


def should_hold_gps(raw: dict) -> str:
    """Returns hold/unresolvable state: 'hold', 'unresolvable', or '' (has GPS)."""
    lat = safe_float(raw.get("gps_lat_raw"))
    lon = safe_float(raw.get("gps_lon_raw"))
    if lat and lon:
        return ""  # has GPS
    tier = raw.get("discovery_tier", 0)
    name = clean_str(raw.get("name_raw", "")).lower()
    # Cemeteries without GPS: declare gps_unresolvable (rural road descriptions only)
    if tier in (5, 8) and "cemetery" in name.lower():
        return "unresolvable"
    if tier == 8 and "burial grounds" in name.lower():
        return "unresolvable"
    # Cross-county held entities: don't gate on GPS (entity is held for other reason)
    if "CROSS_COUNTY_CANDIDATE" in clean_str(raw.get("identity_notes_raw", "")):
        return "held_cc"
    # Sites with stated address but no GPS: need acquisition
    if raw.get("location_raw"):
        return "needs_acquisition"
    return "unresolvable"


# ── ID counters ───────────────────────────────────────────────────────────────
_id_counters = {"S": 0, "TT": 0, "SN": 0, "AP": 0}

def next_id(type_code: str) -> str:
    _id_counters[type_code] += 1
    n = _id_counters[type_code]
    if type_code == "S":
        return f"{PREFIX}-S-{n:03d}"
    elif type_code == "TT":
        return f"{PREFIX}-TT-{n:03d}"
    elif type_code == "SN":
        return f"{PREFIX}-SN-{n:03d}"
    elif type_code == "AP":
        return f"{PREFIX}-AP-{n:03d}"


# ── Main normalization ─────────────────────────────────────────────────────────

def load_yaml() -> list:
    """Load raw discovery YAML and return only entity records (skip result blocks)."""
    text = open(YAML_FILE, encoding="utf-8").read()
    if preprocess_yaml:
        text = preprocess_yaml(text)
    data = yaml.safe_load(text)
    records = data.get("records", [])
    # Filter to entity records only (skip null-evidence blocks)
    entities = [r for r in records if isinstance(r, dict) and "entity_type" in r
                and r["entity_type"] in ("Site", "Trailthing", "Site Network", "Access Point")]
    print(f"Loaded {len(entities)} entity records from {len(records)} total records")
    return entities


def normalize_sites(raw_sites: list) -> tuple:
    """Normalize site records. Returns (sites_out, held_out)."""
    sites_out = []
    held_out  = []

    for i, raw in enumerate(raw_sites, start=1):
        entity_id = next_id("S")
        name      = clean_str(raw.get("name_raw", ""))
        counties  = normalize_counties(raw.get("counties_raw"))
        ident_notes = clean_str(raw.get("identity_notes_raw", ""))

        # Cross-county entities → hold
        is_cc = "CROSS_COUNTY_CANDIDATE" in ident_notes
        is_unconfirmed = "IDENTITY_UNCONFIRMED" in ident_notes

        cat, subtype, designation = normalize_site_category(raw)
        status = normalize_site_status(raw)

        lat = safe_float(raw.get("gps_lat_raw"))
        lon = safe_float(raw.get("gps_lon_raw"))
        gps_state = should_hold_gps(raw)

        # Build site dict (matches config format)
        site = {
            "site_id":             entity_id,
            "name":                name,
            "category":            cat,
            "subtype":             subtype,
            "designation":         designation,
            "status":              status if status in SITE_STATUS_VALUES else "Active",
            "ownership":           clean_str(raw.get("ownership_raw", "")),
            "governance":          clean_str(raw.get("governance_raw", "")),
            "partner_agencies":    clean_str(raw.get("partner_agencies_raw") or ""),
            "coordination":        clean_str(raw.get("coordination_raw") or ""),
            "description":         clean_str(raw.get("description_raw", "")),
            "habitat_type":        clean_str(raw.get("habitat_type_raw") or ""),
            "features_raw":        clean_str(raw.get("features_raw", "")),
            "features":            map_features(clean_str(raw.get("features_raw", ""))),
            "access_notes":        clean_str(raw.get("access_notes_raw") or ""),
            "location":            clean_str(raw.get("location_raw", "")),
            "acres":               safe_acres(raw.get("acres_raw")),
            "counties":            counties,
            "township":            "",
            "municipality":        "",
            "gps_lat":             lat,
            "gps_lon":             lon,
            "gps_confidence":      "HIGH" if lat and lon else "NONE",
            "gps_unresolvable":    gps_state == "unresolvable",
            "plus_code":           "",
            "notes":               "",
            "url_primary":         first_url(raw.get("urls_raw")),
            "urls":                all_urls(raw.get("urls_raw")),
            "last_verified_date":  clean_str(raw.get("last_verified_date", TODAY)),
            "field_verified":      bool(raw.get("field_verified", False)),
            "parent_site_id":      "",
            "parent_site_name":    "",
            "ebird_hotspot_id":    clean_str(raw.get("ebird_hotspot_id") or ""),
            "identity_notes":      ident_notes,
            "status_flag":         "",
            "hold_detail":         "",
            "discovery_tier":      raw.get("discovery_tier", 0),
            "seeded_from_baseline": bool(raw.get("seeded_from_baseline", False)),
            "baseline_id":         clean_str(raw.get("baseline_id") or ""),
        }

        # Determine hold status
        hold_reason = ""
        hold_detail = ""

        if is_cc:
            hold_reason = "cross_county_held"
            hold_detail = f"{name}: cross-county entity spanning Hardin and Wyandot counties. Wyandot County not yet run under v6. Hold pending Wyandot County pipeline run (Scenario A)."

        elif is_unconfirmed:
            hold_reason = "identity_uncertain"
            hold_detail = f"{name}: identity unconfirmed — insufficient authoritative source information. Flag for field verification."

        elif not lat and not lon and gps_state == "needs_acquisition":
            # Will be handled by GPS acquisition pass; flag for it
            site["status_flag"] = "GPS_NEEDED"

        elif not lat and not lon and gps_state == "unresolvable":
            site["gps_unresolvable"] = True
            # gps_unresolvable entities PASS the GPS gate

        elif not lat and not lon and not site["gps_unresolvable"]:
            hold_reason = "gps_missing"
            hold_detail = f"{name}: GPS null and gps_unresolvable not set."

        if hold_reason:
            site["status_flag"]  = hold_reason
            site["hold_detail"]  = hold_detail
            held_out.append({
                "entity_id":   entity_id,
                "entity_type": "Site",
                "name":        name,
                "county":      COUNTY,
                "hold_reason": hold_reason,
                "hold_detail": hold_detail,
                "run_id":      RUN_ID,
            })
        else:
            sites_out.append(site)

    return sites_out, held_out


def normalize_trailthings(raw_tts: list, site_map: dict) -> tuple:
    """Normalize Trailthing records. site_map maps name→id for parent lookup."""
    tts_out  = []
    held_out = []

    for raw in raw_tts:
        entity_id = next_id("TT")
        name      = clean_str(raw.get("name_raw", ""))

        # Source term is verbatim — NEVER normalize
        source_term = clean_str(raw.get("source_term_raw", ""))
        src_hier    = clean_str(raw.get("source_hierarchy_context_raw", ""))

        # Use type normalization
        use_raw = clean_str(raw.get("use_type_raw", "")).lower()
        use_type = ""
        if "multi" in use_raw: use_type = "Multi-Use"
        elif "hiking" in use_raw or "walking" in use_raw: use_type = "Hiking"
        elif "mountain bike" in use_raw: use_type = "Mountain Bike"
        elif "bicycle" in use_raw or "bike" in use_raw: use_type = "Bicycling"
        elif "water" in use_raw or "paddling" in use_raw: use_type = "Water"
        elif "bridle" in use_raw or "equestrian" in use_raw: use_type = "Bridle"
        if use_type not in TRAILTHING_USE_TYPES:
            use_type = ""

        # Surface type
        surf_raw = clean_str(raw.get("surface_type_raw", "")).lower()
        surface = ""
        if "boardwalk" in surf_raw: surface = "Boardwalk"
        elif "paved" in surf_raw or "asphalt" in surf_raw or "concrete" in surf_raw: surface = "Paved"
        elif "crushed" in surf_raw or "limestone" in surf_raw: surface = "Crushed Stone"
        elif "gravel" in surf_raw: surface = "Gravel"
        elif "natural" in surf_raw or "dirt" in surf_raw: surface = "Natural Surface"
        elif "mowed" in surf_raw: surface = "Natural Surface"
        elif "water" in surf_raw: surface = "Water"
        elif "mixed" in surf_raw: surface = "Mixed"
        if surface not in TRAILTHING_SURFACES:
            surface = ""

        # Origin type
        origin_raw = clean_str(raw.get("origin_type_raw", "")).lower()
        origin = ""
        if "rail" in origin_raw: origin = "Rail Trail"
        elif "canal" in origin_raw: origin = "Canal Towpath"
        elif "purpose" in origin_raw or "village-built" in origin_raw: origin = "Purpose-Built"
        elif "utility" in origin_raw or "powerline" in origin_raw: origin = "Utility Corridor"
        elif "road" in origin_raw: origin = "Roadside Corridor"
        elif "greenway" in origin_raw: origin = "Greenway Corridor"
        elif "waterway" in origin_raw: origin = "Waterway"
        # Infer purpose-built for parks/cities
        if not origin:
            gov = clean_str(raw.get("governance_raw", "")).lower()
            if any(x in gov for x in ["village of", "city of", "township", "district", "university"]):
                origin = "Purpose-Built"
        if origin not in TRAILTHING_ORIGINS:
            origin = ""

        # Org type
        gov_raw = clean_str(raw.get("governance_raw", "")).lower()
        org_type = ""
        if "odnr" in gov_raw or "division of" in gov_raw: org_type = "State Agency"
        elif "county" in gov_raw and "university" not in gov_raw: org_type = "County Authority"
        elif any(x in gov_raw for x in ["village of", "city of"]): org_type = "Municipal Department"
        elif "university" in gov_raw: org_type = "Nonprofit Conservancy"
        elif "swcd" in gov_raw or "soil and water" in gov_raw: org_type = "County Authority"
        if org_type not in TRAILTHING_ORG_TYPES:
            org_type = ""

        # Status
        status_raw = clean_str(raw.get("status_raw", "")).lower()
        status = ""
        if "open" in status_raw or "active" in status_raw: status = "Active"
        elif "planned" in status_raw: status = "Planned"
        elif "closed" in status_raw: status = "Closed"
        elif "under construction" in status_raw: status = "Under Construction"
        if status not in TRAILTHING_STATUSES:
            status = "Active"

        # Parent Site lookup
        site_parent_raw  = clean_str(raw.get("site_parent_raw", ""))
        site_parent_id   = site_map.get(site_parent_raw, "")
        site_parent_name = site_parent_raw if site_parent_id else ""

        counties = normalize_counties(raw.get("counties_raw"))

        # Length
        length_raw = clean_str(raw.get("total_length_raw", ""))
        length_val = None
        m = re.search(r"([\d.]+)\s*mile", length_raw, re.IGNORECASE)
        if m:
            try: length_val = float(m.group(1))
            except ValueError: pass

        tt = {
            "trailthing_id":            entity_id,
            "name":                     name,
            "alternate_names":          "",
            "source_term":              source_term,
            "source_hierarchy_context": src_hier,
            "parent_id":                "",
            "parent_name":              "",
            "site_parent_id":           site_parent_id,
            "site_parent_name":         site_parent_name,
            "parent_site_network_id":   "",
            "parent_site_network_name": "",
            "use_type":                 use_type,
            "surface_type":             surface,
            "origin_type":              origin,
            "org_type":                 org_type,
            "status":                   status,
            "difficulty":               "",
            "accessibility":            clean_str(raw.get("accessibility_raw") or ""),
            "ownership":                clean_str(raw.get("ownership_raw", "")),
            "governance":               clean_str(raw.get("governance_raw", "")),
            "partner_agencies":         clean_str(raw.get("partner_agencies_raw") or ""),
            "coordination":             clean_str(raw.get("coordination_raw") or ""),
            "counties":                 counties,
            "states_included":          "",
            "total_length":             length_val,
            "description":              clean_str(raw.get("description_raw", "")),
            "trail_history":            "",
            "identity_notes":           clean_str(raw.get("identity_notes_raw") or ""),
            "notes":                    "",
            "url":                      first_url(raw.get("urls_raw")),
            "maps":                     ";".join(raw.get("maps_raw", [])) if isinstance(raw.get("maps_raw"), list) else "",
            "status_flag":              "",
            "hold_detail":              "",
            "discovery_tier":           raw.get("discovery_tier", 0),
            "seeded_from_baseline":     bool(raw.get("seeded_from_baseline", False)),
            "baseline_id":              clean_str(raw.get("baseline_id") or ""),
            # Trailthings are not gated — GPS is gps_unresolvable for all
            "gps_unresolvable":         True,
        }

        # Check if parent site is held
        if site_parent_id == "" and site_parent_raw:
            tt["status_flag"] = "parent_site_not_found"
            tt["hold_detail"] = f"Parent site '{site_parent_raw}' not resolved."

        tts_out.append(tt)

    return tts_out, held_out


def normalize_site_networks(raw_sns: list, site_map: dict) -> list:
    """Normalize Site Network records."""
    sns_out = []
    for raw in raw_sns:
        entity_id = next_id("SN")
        name = clean_str(raw.get("network_name_raw", raw.get("name_raw", "")))

        network_type_raw = clean_str(raw.get("network_type_raw", "")).lower()
        network_type = ""
        if "municipal recreation" in network_type_raw: network_type = "Municipal Recreation System"
        elif "park district" in network_type_raw: network_type = "Park District System"
        elif "state program" in network_type_raw: network_type = "State Program Portfolio"
        elif "land trust" in network_type_raw: network_type = "Land Trust Portfolio"
        elif "conservation authority" in network_type_raw: network_type = "Conservation Authority Portfolio"
        elif "nonprofit" in network_type_raw: network_type = "Nonprofit Conservation Portfolio"
        elif "heritage area" in network_type_raw: network_type = "National Heritage Area"
        elif "scenic" in network_type_raw: network_type = "Scenic River Corridor"
        if network_type not in SN_NETWORK_TYPES:
            network_type = ""

        org_type_raw = clean_str(raw.get("org_type_raw", "")).lower()
        org_type = ""
        if "municipal" in org_type_raw: org_type = "Municipal Department"
        elif "state" in org_type_raw: org_type = "State Agency"
        elif "federal" in org_type_raw: org_type = "Federal Agency"
        elif "county" in org_type_raw: org_type = "County Authority"
        elif "land trust" in org_type_raw: org_type = "Land Trust"
        elif "nonprofit" in org_type_raw: org_type = "Nonprofit Conservancy"
        elif "coordinating" in org_type_raw: org_type = "Coordinating Body"
        elif "regional" in org_type_raw: org_type = "Regional Authority"
        if org_type not in SN_ORG_TYPES:
            org_type = ""

        status_raw = clean_str(raw.get("status_raw", "")).lower()
        status = "Active"
        if "inactive" in status_raw: status = "Inactive"
        if status not in SN_STATUSES:
            status = "Active"

        # Member sites — resolve names to IDs
        member_names_raw = clean_str(raw.get("member_site_names_raw", ""))
        member_ids   = []
        member_names = []
        for mn in member_names_raw.split(";"):
            mn = mn.strip()
            if not mn: continue
            mid = site_map.get(mn, "")
            if mid:
                member_ids.append(mid)
                member_names.append(mn)
            else:
                member_names.append(mn)

        ident = clean_str(raw.get("identity_notes_raw") or "")

        sn = {
            "network_id":        entity_id,
            "name":              name,
            "network_type":      network_type,
            "org_type":          org_type,
            "status":            status,
            "ownership":         clean_str(raw.get("ownership_raw") or ""),
            "governance":        clean_str(raw.get("governance_raw", "")),
            "partner_agencies":  clean_str(raw.get("partner_agencies_raw") or ""),
            "coordination":      clean_str(raw.get("coordination_raw") or ""),
            "counties":          normalize_counties(raw.get("counties_raw")),
            "states_included":   "",
            "member_count":      len(member_ids) or None,
            "member_site_ids":   ";".join(member_ids),
            "member_site_names": ";".join(member_names),
            "description":       clean_str(raw.get("description_raw", "")),
            "identity_notes":    ident,
            "notes":             "",
            "url":               first_url(raw.get("urls_raw")),
            "status_flag":       "",
            "hold_detail":       "",
            "discovery_tier":    raw.get("discovery_tier", 0),
            "seeded_from_baseline": bool(raw.get("seeded_from_baseline", False)),
        }
        sns_out.append(sn)

    return sns_out


def normalize_access_points(raw_aps: list, site_map: dict, tt_map: dict) -> tuple:
    """Normalize Access Point records. Returns (aps_out, held_out)."""
    aps_out  = []
    held_out = []

    for raw in raw_aps:
        entity_id = next_id("AP")
        name = clean_str(raw.get("name_raw", raw.get("access_point_name", "")))

        # Determine parent entity (prefer Site over Trailthing)
        parent_sites = raw.get("parent_sites_raw", []) or []
        parent_tts   = raw.get("parent_trailthings_raw", []) or []
        if isinstance(parent_sites, str): parent_sites = [parent_sites] if parent_sites else []
        if isinstance(parent_tts, str):   parent_tts   = [parent_tts]   if parent_tts   else []

        parent_id   = ""
        parent_name = ""
        parent_type = ""

        for ps in parent_sites:
            if ps and ps in site_map:
                parent_id   = site_map[ps]
                parent_name = ps
                parent_type = "Site"
                break

        if not parent_id:
            for pt in parent_tts:
                if pt and pt in tt_map:
                    parent_id   = tt_map[pt]
                    parent_name = pt
                    parent_type = "Trailthing"
                    break

        # AP type — check primary access pattern first
        ap_type = "Trailhead"  # default for park/preserve entrances
        feat_raw = clean_str(raw.get("features_raw", "")).lower()
        name_lower = name.lower()
        if "boat" in feat_raw or "kayak" in feat_raw or "watercraft" in feat_raw:
            ap_type = "Watercraft Access Point"
        elif "parking" in feat_raw and "trail" not in feat_raw and "trailhead" not in feat_raw:
            ap_type = "Parking Area"
        # Note: "fishing" alone does NOT override Trailhead when the AP serves
        # a multi-amenity park entrance. Only use Fishing Access when fishing
        # is the primary documented function.

        lat = safe_float(raw.get("gps_lat_raw"))
        lon = safe_float(raw.get("gps_lon_raw"))

        ident = clean_str(raw.get("identity_notes_raw") or "")
        is_cc = "CROSS_COUNTY_CANDIDATE" in ident

        ap = {
            "access_point_id":           entity_id,
            "name":                      name,
            "ap_type":                   ap_type if ap_type in AP_TYPES else "Trailhead",
            "status":                    "Active",
            "identity_parent_entity_type": parent_type,
            "identity_parent_entity_id":  parent_id,
            "identity_parent_entity_name": parent_name,
            "county":                    COUNTY,
            "township":                  "",
            "municipality":              "",
            "address":                   clean_str(raw.get("location_raw", "")),
            "gps_lat":                   lat,
            "gps_lon":                   lon,
            "gps_confidence":            "HIGH" if lat and lon else "NONE",
            "gps_unresolvable":          False,
            "plus_code":                 "",
            "features":                  map_features(clean_str(raw.get("features_raw", ""))),
            "identity_notes":            ident,
            "notes":                     "",
            "url":                       first_url(raw.get("urls_raw")),
            "last_verified_date":        clean_str(raw.get("last_verified_date", TODAY)),
            "field_verified":            bool(raw.get("field_verified", False)),
            "status_flag":               "",
            "hold_detail":               "",
            "discovery_tier":            raw.get("discovery_tier", 0),
        }

        # If we had requested parents but found none, entity should be held
        requested_parents = [p for p in (list(parent_sites) + list(parent_tts)) if p]
        parent_missing = (parent_id == "" and len(requested_parents) > 0)
        attempted_parent = requested_parents[0] if requested_parents else ""

        # Hold if parent is held (cross-county) or if no parent found
        if parent_missing:
            ap["status_flag"] = "parent_held"
            ap["hold_detail"] = f"Parent entity '{attempted_parent}' not in normalized entity maps (likely held cross-county or unresolved)."
            held_out.append({
                "entity_id":   entity_id,
                "entity_type": "Access Point",
                "name":        name,
                "county":      COUNTY,
                "hold_reason": "parent_held",
                "hold_detail": ap["hold_detail"],
                "run_id":      RUN_ID,
            })
        elif not lat and not lon:
            ap["gps_unresolvable"] = False
            ap["status_flag"] = "GPS_NEEDED"
            aps_out.append(ap)
        else:
            aps_out.append(ap)

    return aps_out, held_out


# ── GPS acquisition pass (Nominatim) ─────────────────────────────────────────

def build_gps_queries(sites: list, aps: list) -> dict:
    """Build Nominatim query strings for entities needing GPS."""
    queries = {}
    for s in sites:
        if s.get("status_flag") == "GPS_NEEDED" and s.get("location"):
            loc = s["location"].split(";")[0].strip()  # use first location
            queries[s["site_id"]] = loc
    for ap in aps:
        if ap.get("status_flag") == "GPS_NEEDED" and ap.get("address"):
            queries[ap["access_point_id"]] = ap["address"].split(";")[0].strip()
    return queries


def build_fallback_gps(entities: list) -> dict:
    """Extract stated GPS as fallback for entities that have it."""
    fallback = {}
    for e in entities:
        eid = e.get("site_id") or e.get("access_point_id", "")
        lat = e.get("gps_lat")
        lon = e.get("gps_lon")
        if lat and lon and eid:
            fallback[eid] = [lat, lon]
    return fallback


# ── Config writer ─────────────────────────────────────────────────────────────

def write_config(sites: list, tts: list, sns: list, aps: list,
                 held: list, gps_queries: dict, fallback_gps: dict):
    with open(CONFIG_FILE, encoding="utf-8") as f:
        config = json.load(f)

    config["records_input"] = 144
    config["sites"]         = sites
    config["trailthings"]   = tts
    config["site_networks"] = sns
    config["access_points"] = aps
    config["held_entities"] = held
    config["gps_queries"]   = gps_queries
    config["fallback_gps"]  = fallback_gps
    config["fallback_conf"] = {k: "HIGH" for k in fallback_gps}

    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False, default=str)
    print(f"Config written: {CONFIG_FILE}")


# ── Unconfirmed baseline seeds ────────────────────────────────────────────────

UNCONFIRMED_SEEDS = [
    "Ada Trail Spur (Unmarked)",
    "Simon Kenton Trail (Planned Extension)",
    "Kenton Greenbelt Parcel",
    "Ada Reservoir",
    "Ada Reservoir Woodlot Buffer",
    "Kenton Water Treatment Plant Buffer",
    "McGuffey Reservoir",
    "Pleasant Township Green Parcel",
    # Scioto Marsh entries — all unconfirmed/out of scope
    "Scioto Marsh Drainage Canals",
    "Scioto Marsh Drainage District Parcels",
    "Scioto Marsh Drainage Ditch Access",
    "Scioto Marsh Edge Parcels",
    "Scioto Marsh Prairie Remnants",
    "Scioto Marsh Remnants",
    "Scioto Marsh Complex",
    "Scioto Marsh (historical)",
    "Scioto River Corridor",
    "Hog Creek Corridor",
    "Blanchard River Corridor",
    "Hog Creek Marsh (historical)",
    "Hog Creek Marsh Remnant",
    "AEP Transmission Corridor — Ada Segment",
    "Lawrence Woods Prairie Restoration",
    "Lawrence Woods Buffer Parcel",
    "Veterans Park North Buffer",
    "Ada Reservoir Woodlot Buffer",
    "Kenton Water Treatment Plant Buffer",
    "Kenton Greenbelt Parcel",
]

HOLD_DETAILS_SEEDS = {
    "Ada Trail Spur (Unmarked)": "Baseline: short paved segment from Ada Railroad Park, no signage. No authoritative source confirms distinct trail entity separate from Ada Railroad Park Path. Unconfirmed pending field verification.",
    "Simon Kenton Trail (Planned Extension)": "Baseline: proposed trail extension into Hardin County. Trail currently ends in Logan/Champaign Counties. Not yet constructed. Unconfirmed until construction begins.",
    "Kenton Greenbelt Parcel": "Baseline: wooded parcel along river near Kenton, unknown ownership. No authoritative source confirms public ownership or managed identity. Likely informal/private.",
    "Ada Reservoir": "Baseline GPS matches Ada War Memorial Park stocked pond. If the reservoir is the pond inside Ada Memorial Park, it is captured as a park feature, not a separate entity. Unconfirmed pending field verification.",
    "McGuffey Reservoir": "Baseline: small reservoir near McGuffey, unknown ownership. Not confirmed as public recreation area during T4/T6 discovery.",
    "Pleasant Township Green Parcel": "Baseline: informal open space in Pleasant Township. Township has no parks. No authoritative source confirms managed natural area identity.",
}


def build_unconfirmed_held(seeds: list = UNCONFIRMED_SEEDS) -> list:
    held = []
    for seed_name in seeds:
        detail = HOLD_DETAILS_SEEDS.get(seed_name,
            f"Baseline seed '{seed_name}' not confirmed by any authoritative source during T1–T8 discovery. "
            f"May be informal, private, out of scope, or historical only.")
        held.append({
            "entity_id":   f"SEED-{seed_name[:40].replace(' ', '_')}",
            "entity_type": "Site",
            "name":        seed_name,
            "county":      COUNTY,
            "hold_reason": "unconfirmed_baseline_seed",
            "hold_detail": detail,
            "run_id":      RUN_ID,
        })
    return held


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    # Reset ID counters for fresh run
    global _id_counters
    _id_counters = {"S": 0, "TT": 0, "SN": 0, "AP": 0}

    print(f"\n{'='*60}")
    print(f"Hardin County OH normalization — {TODAY}")
    print(f"{'='*60}\n")

    # Load records
    entities = load_yaml()

    # Partition by type
    raw_sites = [r for r in entities if r.get("entity_type") == "Site"]
    raw_tts   = [r for r in entities if r.get("entity_type") == "Trailthing"]
    raw_sns   = [r for r in entities if r.get("entity_type") == "Site Network"]
    raw_aps   = [r for r in entities if r.get("entity_type") == "Access Point"]

    print(f"Input: {len(raw_sites)} Sites, {len(raw_tts)} Trailthings, "
          f"{len(raw_sns)} Site Networks, {len(raw_aps)} Access Points\n")

    # Normalize
    sites_out, sites_held = normalize_sites(raw_sites)
    print(f"Sites: {len(sites_out)} normalized, {len(sites_held)} held")

    # Build lookup maps for parent resolution
    site_map = {s["name"]: s["site_id"] for s in sites_out}

    tts_out, tts_held = normalize_trailthings(raw_tts, site_map)
    print(f"Trailthings: {len(tts_out)} normalized, {len(tts_held)} held")

    tt_map = {t["name"]: t["trailthing_id"] for t in tts_out}

    sns_out = normalize_site_networks(raw_sns, site_map)
    print(f"Site Networks: {len(sns_out)} normalized")

    aps_out, aps_held = normalize_access_points(raw_aps, site_map, tt_map)
    print(f"Access Points: {len(aps_out)} normalized, {len(aps_held)} held")

    # Unconfirmed baseline seeds
    seed_held = build_unconfirmed_held()
    print(f"Unconfirmed baseline seeds: {len(seed_held)}")

    all_held = sites_held + tts_held + aps_held + seed_held
    print(f"\nTotal held: {len(all_held)}")

    # GPS queries and fallbacks
    gps_queries  = build_gps_queries(sites_out, aps_out)
    fallback_gps = build_fallback_gps(sites_out + aps_out)
    print(f"GPS queries needed: {len(gps_queries)}")
    print(f"GPS from source:    {len(fallback_gps)}")

    # Write config
    write_config(sites_out, tts_out, sns_out, aps_out,
                 all_held, gps_queries, fallback_gps)

    # Summary
    print(f"\n{'='*60}")
    print("NORMALIZATION COMPLETE")
    print(f"  Sites:         {len(sites_out)} normalized, {len(sites_held)} held")
    print(f"  Trailthings:   {len(tts_out)} normalized")
    print(f"  Site Networks: {len(sns_out)} normalized")
    print(f"  Access Points: {len(aps_out)} normalized, {len(aps_held)} held")
    print(f"  Total held:    {len(all_held)}")
    print(f"\nNext: review hardin_config.json, then run:")
    print(f"  python utilities/na_run_county.py --county-dir County_Spreadsheets/Hardin")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
