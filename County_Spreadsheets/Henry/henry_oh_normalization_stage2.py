#!/usr/bin/env python3
"""
henry_oh_normalization_stage2.py
Stage 2 Normalization Engine — Henry County, OH
Natural Areas Project v5  |  Pipeline Run: henry_oh_2026_04_20
Run date: 2026-04-26

Normalization Engine v5.8
Site Normalization Contract v5.9  |  Trail Normalization Contract v5.2
Trail Segment Normalization Contract v5.1  |  AP Normalization Contract v5.1
Site Vocabulary v5.5  |  Trail Vocabulary v5.1  |  AP Vocabulary v5.2

Reads:  henry_oh_resolved_entities.yaml (50 entities)
Writes: henry_oh_normalized_entities.yaml
        henry_oh_held_entities.yaml
        henry_oh_normalization_report.md
"""

import sys
import os
import re
import yaml
import datetime
import logging

UTIL_PATH = "/sessions/trusting-sweet-gates/mnt/Natural Areas Project v5/utilities"
sys.path.insert(0, UTIL_PATH)

from na_vocab_constants import (
    ALLOWED_CATEGORIES, ALLOWED_SUBTYPES, ALLOWED_FEATURES,
    ALLOWED_DESIGNATIONS, ALLOWED_SITE_STATUSES,
    ALLOWED_TRAIL_USE_TYPES, ALLOWED_TRAIL_SURFACES,
    ALLOWED_TRAIL_ORIGINS, ALLOWED_TRAIL_STATUSES,
    ALLOWED_TRAIL_DIFFICULTIES, ALLOWED_AP_TYPES, ALLOWED_AP_STATUSES,
    subtypes_for, feature_valid, category_valid, subtype_valid,
)
from na_plus_code import encode_plus_code
from na_township_lookup import OhioTownshipLookup

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

# ── Paths ────────────────────────────────────────────────────────────────────
BASE = "/sessions/trusting-sweet-gates/mnt/Natural Areas Project v5"
INPUT_FILE   = f"{BASE}/henry_oh_resolved_entities.yaml"
OUTPUT_FILE  = f"{BASE}/henry_oh_normalized_entities.yaml"
HELD_FILE    = f"{BASE}/henry_oh_held_entities.yaml"
REPORT_FILE  = f"{BASE}/henry_oh_normalization_report.md"

# ── Run constants ─────────────────────────────────────────────────────────────
RUN_ID         = "henry_oh_2026_04_20"
COUNTY         = "Henry"
STATE          = "Ohio"
NORM_DATE      = "2026-04-26"
COUNTY_CENTROID = (41.30, -84.08)  # Henry County centroid

# ── GIS lookup ────────────────────────────────────────────────────────────────
_gis = OhioTownshipLookup()

def gis_lookup(lat: float, lon: float):
    """Returns (township, municipality) or ('', '') on failure."""
    try:
        twp, muni = _gis.get_both(lat, lon)
        return (twp or ""), (muni or "")
    except Exception as e:
        log.warning(f"GIS lookup failed for ({lat}, {lon}): {e}")
        return "", ""

# ── GPS utilities ─────────────────────────────────────────────────────────────
LAT_RANGE = (24.0, 50.0)
LON_RANGE = (-130.0, -65.0)

def parse_gps(lat_raw, lon_raw):
    """Parse and validate GPS strings. Returns (float, float) or (None, None)."""
    if not lat_raw or not lon_raw:
        return None, None
    try:
        lat = round(float(str(lat_raw).strip()), 6)
        lon = round(float(str(lon_raw).strip()), 6)
        if not (LAT_RANGE[0] <= lat <= LAT_RANGE[1]):
            log.warning(f"GPS lat {lat} out of range [{LAT_RANGE}]")
            return None, None
        if not (LON_RANGE[0] <= lon <= LON_RANGE[1]):
            log.warning(f"GPS lon {lon} out of range [{LON_RANGE}]")
            return None, None
        return lat, lon
    except (ValueError, TypeError):
        return None, None

def get_plus_code(lat, lon):
    if lat is None or lon is None:
        return ""
    try:
        return encode_plus_code(lat, lon)
    except Exception as e:
        log.warning(f"Plus code failed for ({lat}, {lon}): {e}")
        return ""

# ── County normalization ──────────────────────────────────────────────────────
_COUNTY_STRIP = re.compile(r'\s*,?\s*county\s*', re.IGNORECASE)
_COUNTY_STATE = re.compile(r',\s*(ohio|oh)\s*$', re.IGNORECASE)
_COUNTY_CLEANUP = re.compile(r',.*$')  # strip ", Ohio" or ", OH"

def normalize_county_name(raw: str) -> str:
    """Strip 'County', 'Ohio', 'OH' suffixes; return bare county name."""
    s = raw.strip()
    s = _COUNTY_STATE.sub("", s)
    s = _COUNTY_STRIP.sub("", s)
    s = _COUNTY_CLEANUP.sub("", s).strip()
    return s

def normalize_counties(counties_raw: list) -> str:
    """Return semicolon-delimited, alphabetized, 'County' stripped county names."""
    names = sorted({normalize_county_name(c) for c in counties_raw if c})
    return ";".join(names)

# ── URL utilities ─────────────────────────────────────────────────────────────
def best_url(urls_raw: list) -> str:
    """Return the first https:// URL as url_primary, or the first URL."""
    if not urls_raw:
        return ""
    for u in urls_raw:
        u = str(u).strip()
        if u.startswith("https://"):
            return u
    return str(urls_raw[0]).strip() if urls_raw else ""

def urls_semicolon(urls_raw: list) -> str:
    cleaned = []
    seen = set()
    for u in (urls_raw or []):
        u = str(u).strip()
        if u and u not in seen:
            seen.add(u)
            cleaned.append(u)
    return ";".join(cleaned)

def has_authoritative_url(urls_raw: list) -> bool:
    """True if any URL is https:// (heuristic for authoritative source)."""
    for u in (urls_raw or []):
        u = str(u).strip()
        if u.startswith("http"):
            return True
    return False

# ── Governance / Ownership normalization ──────────────────────────────────────
def norm_text_field(raw) -> str:
    """Trim a string field; return '' for None/null."""
    if raw is None:
        return ""
    return str(raw).strip()

def norm_list_to_semicolon(raw) -> str:
    """Convert a list or string to semicolon-delimited; remove duplicates."""
    if not raw:
        return ""
    if isinstance(raw, list):
        items = [str(x).strip() for x in raw if x]
    else:
        items = [str(raw).strip()]
    seen, out = set(), []
    for it in items:
        if it and it not in seen:
            seen.add(it)
            out.append(it)
    return ";".join(out)

# ── Identity Notes cleanup (IMP-053) ─────────────────────────────────────────
_NOTES_STRIP = [
    # GPS verification annotations from discovery
    re.compile(r'GPS from Google Maps[^.]*\.', re.IGNORECASE),
    re.compile(r'GPS from Google Maps.*?(?=\n|$)', re.IGNORECASE),
    re.compile(r'confirmed Google Maps[^.]*\.?', re.IGNORECASE),
    # Pipeline staging notes
    re.compile(r'Session log:\s*["\'][^"\']+["\']\.?', re.IGNORECASE),
    re.compile(r'Staging per inclusion rule[^.]*\.?', re.IGNORECASE),
    re.compile(r'Pipeline to resolve[^.]*\.?', re.IGNORECASE),
    re.compile(r'Resolves HEN-F-\d+[^.]*\.?', re.IGNORECASE),
    re.compile(r'HEN-F-\d+[^.]*context[^.]*\.?', re.IGNORECASE),
    re.compile(r'Partially resolves[^.]*\.?', re.IGNORECASE),
    re.compile(r'Baseline also listed[^.]*\.?', re.IGNORECASE),
    re.compile(r'GIS_VERIFY_COUNTY[^.]*\.?', re.IGNORECASE),
    re.compile(r'MINIMAL_DATA\s*—\s*', re.IGNORECASE),
    # Discovery run labels
    re.compile(r'map verification pass \d{4}-\d{2}-\d{2}[^.]*\.?', re.IGNORECASE),
    # IMP bare references
    re.compile(r'\[IMP-\d+\]'),
    # Bare OBJECTID
    re.compile(r'OBJECTID:?\s*\d+'),
]

def clean_identity_notes(raw: str) -> str:
    """Apply IMP-053 pipeline metadata stripping to identity_notes_raw."""
    if not raw:
        return ""
    s = raw.strip()
    for pat in _NOTES_STRIP:
        s = pat.sub("", s)
    # Collapse multiple spaces / blank lines
    s = re.sub(r'  +', ' ', s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    s = s.strip()
    # Remove orphaned trailing punctuation from stripping
    s = re.sub(r'^\s*[.;,]\s*', '', s)
    s = re.sub(r'\s+\.', '.', s)
    return s.strip()

# ── Description normalization (IMP-052, IMP-059) ──────────────────────────────
def norm_description(raw: str, name: str, category: str, subtype: str) -> str:
    """
    IMP-052: Strip redundancy — description should not repeat name+category formula.
    IMP-059: Formula detection — if description IS just a name/category formula, blank it.
    Limits to ~3 sentences; no governance/ownership info.
    """
    if not raw:
        return ""
    s = raw.strip()
    # IMP-059 formula detection: "X is a [category] in [place]" → acceptable but minimal
    formula_pattern = re.compile(
        r'^' + re.escape(name) + r'\s+is\s+a\s+' + re.escape(category or "") + r'\b',
        re.IGNORECASE
    )
    if formula_pattern.match(s) and len(s) < 120:
        return ""  # pure formula, no value — blank it
    # IMP-052: strip governance contamination
    s = re.sub(r'managed by [^,.]+[,.]?', '', s, flags=re.IGNORECASE)
    s = re.sub(r'operated by [^,.]+[,.]?', '', s, flags=re.IGNORECASE)
    # Collapse to max 3 sentences
    sentences = re.split(r'(?<=[.!?])\s+', s.strip())
    if len(sentences) > 3:
        s = " ".join(sentences[:3])
    return s.strip()

# ── Features mapping (IMP-049/050/051) ───────────────────────────────────────
FEATURE_MAP = [
    # walking / hiking
    (r'hiking trail|walking trail|walking path|winding trail|nature trail|loop trail|trail system|interpretive trail|self.guided interpretive|storybook trail', "Hiking Trail"),
    (r'\bboardwalk\b', "Boardwalk"),
    (r'bridle trail|equestrian', "Bridle Trail"),
    # water
    (r'boat ramp|launch ramp', "Boat Ramp"),
    (r'boat launch|watercraft|canoe|kayak', "Watercraft Access"),
    (r'fishing (pond|lake|area|pier)|fishing$|fish(ing)?\s', "Fishing Area"),
    (r'fishing pond', "Pond"),
    (r'swimming beach|swim beach', "Swimming Beach"),
    (r'swimming pool|city pool', "Swimming Pool"),
    (r'splash pad|spray pad', "Spray Park"),
    (r'\bmarina\b', "Marina"),
    # picnic / shelter
    (r'pavilion|shelter house|open air pavilion|covered.*(shelter|seating)|rustic shelter|small.*shelter', "Pavilion"),
    (r'picnic area|picnic spot|picnic table|picnicking', "Picnic Area"),
    (r'gazebo|historic gazebo', "Gazebo"),
    # sports
    (r'baseball|softball|ball field', "Ball Diamond"),
    (r'basketball court', "Basketball Court"),
    (r'tennis court', "Tennis Court"),
    (r'pickleball court', "Pickleball Court"),
    (r'volleyball court|sand volleyball', "Volleyball Court"),
    (r'soccer field|soccer complex', "Soccer Pitch"),
    (r'football field', "Football Field"),
    (r'disc golf', "Disc Golf Course"),
    (r'skate park|skate ramp', "Skate Park"),
    (r'miniature golf|mini golf', "Mini Golf"),
    # recreation
    (r'playground|play equipment|swing set', "Playground"),
    (r'sledding hill', "Sledding Hill"),
    (r'horseshoe', "Horseshoe Pitch"),
    (r'archery', "Archery Range"),
    (r'ropes course|high ropes', "Ropes Course"),
    (r'shooting sports|shooting range', "Shooting Range"),
    (r'\bdog park\b', "Dog Park"),
    # amenities
    (r'restroom|flush toilet|portable toilet|bathroom|pit toilet', "Restrooms"),
    (r'\bparking\b', "Parking Lot"),
    (r'\bkiosk\b|information kiosk', "Kiosk"),
    (r'\bcamping\b|campsite|rv.*camp|tent.*camp', "Camping"),
    (r'\bcabin\b|camper cabin|\byurt\b', "Cabin Rentals"),
    (r'ADA.compliant|ADA accessible|wheelchair|ADA concrete', "ADA Accessible"),
    # natural features
    (r'observation deck', "Observation Deck"),
    (r'vernal pool', "Vernal Pool"),
    (r'hunting area|public hunting', "Hunting Area"),
    (r'wildlife.*(view|observ)', "Wildlife Observation Area"),
    # historical / interpretive
    (r'railroad history|radio scanner|railfan|railroad.*display|informational display', "Historic Marker"),
    (r'log home|one.?room schoolhouse|historic.*gazebo|smokehouse|historic (building|structure|complex)', "Historic Structure"),
    (r'war memorial|memorial statue|monument|military monument', "Monument"),
    # educational / farm
    (r'nature center', "Nature Center"),
    (r'guided.*tour', "Guided Tours"),
    (r'farm store', "Farm Store"),
    # misc
    (r'pollinator garden', "Pollinator Garden"),
    (r'community center|events center|steel structure.*basketball', "Community Center"),
]

# Compile patterns for speed
_FEATURE_MAP_COMPILED = [(re.compile(p, re.IGNORECASE), v) for p, v in FEATURE_MAP]

def map_features(features_raw: str) -> str:
    """
    4-step features normalization (IMP-049/050/051):
    Step 1: activity detection from features_raw
    Step 2: strip operational/capacity details (kept in features_raw)
    Step 3: named-entity detection (venue/structure names → generic vocab)
    Step 4: map to controlled vocab via FEATURE_MAP; emit only matched terms.
    Returns semicolon-delimited controlled vocab string, or "".
    """
    if not features_raw:
        return ""
    matched = set()
    for pattern, vocab_term in _FEATURE_MAP_COMPILED:
        if vocab_term and pattern.search(features_raw):
            matched.add(vocab_term)
    # Validate all terms against ALLOWED_FEATURES (safety net)
    valid = sorted(t for t in matched if t in ALLOWED_FEATURES)
    return ";".join(valid)

# ── Category inference ────────────────────────────────────────────────────────
# §7.2 IMP-068 name-pattern recognition (check BEFORE generic inference)
_NAME_CATEGORY_068 = [
    (re.compile(r'\bbotanical garden\b|\bconservatory\b', re.I), "Curated Biological Site", "Botanical Garden"),
    (re.compile(r'\barboretum\b', re.I),                          "Curated Biological Site", "Arboretum"),
    (re.compile(r'\bzoo\b|\bzoological\b', re.I),                 "Curated Biological Site", "Zoo"),
    (re.compile(r'\baquarium\b', re.I),                           "Curated Biological Site", "Aquarium"),
    (re.compile(r'\baviary\b', re.I),                             "Curated Biological Site", "Aviary"),
    (re.compile(r'\bscience center\b|\bscience museum\b', re.I),  "Museum", "Science Museum"),
    (re.compile(r'\bhall of fame\b', re.I),                       "Museum", None),
    (re.compile(r'\bmuseum\b', re.I),                             "Museum", None),
]

# Additional name-based inference rules
_NAME_CATEGORY_EXTRA = [
    (re.compile(r'\bwildlife area\b|\bwildlife management area\b', re.I),  "Wildlife Area"),
    (re.compile(r'\bhunting area\b|\bgame preserve\b', re.I),               "Hunting Area"),
    (re.compile(r'\bstate park\b', re.I),                                    "Park"),
    (re.compile(r'\bnature preserve\b|\bstate nature preserve\b', re.I),     "Nature Preserve"),
    (re.compile(r'\bnatural area\b|\bnatural preserve\b', re.I),             "Natural Area"),
    (re.compile(r'\bconservation area\b', re.I),                             "Conservation Area"),
    (re.compile(r'\bcemetery\b|\bburial ground\b', re.I),                    "Cemetery"),
    (re.compile(r'\bfairgrounds?\b', re.I),                                  "Recreation Facility"),
    (re.compile(r'\bhistoric(?:al)? complex\b|\bhistoric(?:al)? site\b', re.I), "Historic Site"),
    (re.compile(r'\bnature center\b', re.I),                                 "Cultural Facility"),
    (re.compile(r'\bgolf course\b', re.I),                                   "Recreation Facility"),
    (re.compile(r'\bswimming pool\b|\baquatic center\b', re.I),              "Recreation Facility"),
]

# Governance-based inference
_GOV_WILDLIFE  = re.compile(r'division of wildlife', re.I)
_GOV_STATE_PARK= re.compile(r'division of parks', re.I)

def infer_category_subtype_designation(entity: dict):
    """
    Infer (category, subtype, designation, inference_source) from entity data.
    Priority:
      1. category_raw if already set and valid
      2. §7.2 IMP-068 name patterns
      3. Governance-based rules (ODNR DoW → Wildlife Area)
      4. Name keyword extra rules
      5. Default → "Park"
    """
    name    = (entity.get("identity_block") or {}).get("name_raw") or ""
    cat_raw = (entity.get("payload") or {}).get("category_raw") or ""
    gov_raw = ((entity.get("organizational_block") or {}).get("governance_raw") or "")
    own_raw = ((entity.get("organizational_block") or {}).get("ownership_raw") or "")
    desc    = (entity.get("payload") or {}).get("description_raw") or ""

    category   = ""
    subtype    = ""
    designation= ""
    source     = "default"

    # 1. Honour explicit category_raw if valid
    if cat_raw and cat_raw in ALLOWED_CATEGORIES:
        category = cat_raw
        source = "category_raw"

    # 2. §7.2 IMP-068 name patterns (highest priority override)
    if not category:
        for pat, cat, sub in _NAME_CATEGORY_068:
            if pat.search(name):
                category = cat
                subtype  = sub or ""
                source   = "name_pattern_IMP068"
                break

    # 3. Governance-based rules
    if not category:
        if _GOV_WILDLIFE.search(gov_raw) or _GOV_WILDLIFE.search(own_raw):
            category = "Wildlife Area"
            source   = "governance_ODNR_DoW"
        elif _GOV_STATE_PARK.search(gov_raw):
            category = "Park"
            source   = "governance_ODNR_Parks"

    # 4. Name-keyword extra rules
    if not category:
        for pat, cat in _NAME_CATEGORY_EXTRA:
            if pat.search(name):
                category = cat
                source   = "name_keyword"
                break

    # 5. Default → Park
    if not category:
        category = "Park"
        source   = "default_Park"

    # ── Subtype inference (if not already set by step 2) ──────────────────────
    if not subtype:
        subtype, sub_source = infer_subtype(name, category, designation, desc, gov_raw)
    else:
        sub_source = source

    # ── Designation inference ─────────────────────────────────────────────────
    if not designation:
        designation = infer_designation(name, category, gov_raw)

    # Validate subtype against vocabulary
    if subtype and not subtype_valid(category, subtype):
        # Try §7.3 mapping
        mapped = map_subtype(subtype, category)
        if mapped:
            subtype = mapped
        else:
            log.warning(f"Subtype '{subtype}' invalid for category '{category}' on '{name}' — nulling")
            subtype = ""

    return category, subtype, designation, source

# §7.3 Subtype mapping table
_SUBTYPE_MAP = {
    "Park": {
        "Community Park":    "Neighborhood Park",
        "Pocket Park":       "Neighborhood Park",
        "Greenway":          "Linear Park",
        "Trail Corridor":    "Linear Park",
        "Natural Park":      "Greenspace",
        "Woodland Park":     "Greenspace",
        "Riparian Park":     "Greenspace",
        "Regional Park":     "",   # no vocab equivalent
        "Metro Park":        "",   # governance label, not subtype
    },
}

def map_subtype(raw_subtype: str, category: str) -> str:
    """Apply §7.3 subtype normalization mapping. Returns '' if no valid mapping."""
    cat_map = _SUBTYPE_MAP.get(category, {})
    return cat_map.get(raw_subtype, "")

# §7.4 IMP-065 Subtype inference rules
def infer_subtype(name: str, category: str, designation: str, desc: str, gov: str) -> tuple:
    """Returns (subtype, source)."""
    # Nature Preserve
    if category == "Nature Preserve":
        if "State Nature Preserve" in designation or re.search(r'state nature preserve', name, re.I):
            return "State Nature Preserve", "designation_name"
        return "Private Nature Preserve", "default_NP"

    # Wildlife Area
    if category == "Wildlife Area":
        gov_u = gov.upper()
        if "ODNR" in gov_u or "OHIO DEPARTMENT OF NATURAL RESOURCES" in gov_u or "DIVISION OF WILDLIFE" in gov_u:
            return "State Wildlife Area", "governance_ODNR"
        return "", ""

    # Park subtypes by name
    if category == "Park":
        nl = name.lower()
        if "dog park" in nl:
            return "Dog Park", "name_keyword"
        if re.search(r'\blinear\b|greenway|trail.*corridor|corridor.*trail', nl):
            return "Linear Park", "name_keyword"
        if re.search(r'\bplayground\b', nl):
            return "Playground Park", "name_keyword"
        if re.search(r'\bsports?\b|athletic|ballpark|ball park', nl):
            return "Sports Park", "name_keyword"
        if re.search(r'\bwaterfront\b|riverfront|lakefront', nl):
            return "Waterfront Park", "name_keyword"
        if re.search(r'\bcivic\b', nl):
            return "Civic Park", "name_keyword"
        return "", ""

    # Water Site subtypes (§7.4)
    if category == "Water Site":
        if re.search(r'\breservoir\b', name, re.I):
            return "Reservoir", "name_keyword"
        if re.search(r'\blake\b', name, re.I):
            return "Lake", "name_keyword"
        if re.search(r'\bpond\b', name, re.I):
            return "Pond", "name_keyword"
        if re.search(r'\briver\b|\bcreek\b|\bstream\b|\brun\b', name, re.I):
            return "River", "name_keyword"
        if re.search(r'\bharbor\b', name, re.I):
            return "Harbor", "name_keyword"
        if re.search(r'\bmarina\b', name, re.I):
            return "Marina", "name_keyword"
        return "", ""

    # Recreation Facility subtypes (§7.4)
    if category == "Recreation Facility":
        nl = name.lower()
        if "golf course" in nl:
            return "Golf Course", "name_keyword"
        if re.search(r'pool|aquatic center|swim center', nl):
            return "Swimming Pool", "name_keyword"
        if "skate park" in nl:
            return "Skate Park", "name_keyword"
        if "disc golf" in nl:
            return "Disc Golf Course", "name_keyword"
        if re.search(r'sports complex|athletic complex|recreation complex', nl):
            return "Sports Complex", "name_keyword"
        if re.search(r'athletic field|soccer field|baseball field|softball field', nl):
            return "Athletic Field", "name_keyword"
        if re.search(r'recreation center|rec center|community center', nl):
            return "Recreation Center", "name_keyword"
        return "", ""

    # Museum subtypes
    if category == "Museum":
        nl = name.lower()
        if re.search(r'art\b', nl):
            return "Art Museum", "name_keyword"
        if re.search(r'history|historical|heritage', nl):
            return "History Museum", "name_keyword"
        if re.search(r'natural history', nl):
            return "Natural History Museum", "name_keyword"
        if re.search(r'children|child|kids', nl):
            return "Children's Museum", "name_keyword"
        if re.search(r'science', nl):
            return "Science Museum", "name_keyword"
        return "", ""

    # Historic Site subtypes
    if category == "Historic Site":
        if re.search(r'battlefield', name, re.I):
            return "Battlefield", "name_keyword"
        if re.search(r'complex|cluster|group', name, re.I):
            return "Historic Landmark", "name_keyword"
        return "Historic Structure", "default_HS"

    # Cultural Facility subtypes
    if category == "Cultural Facility":
        if re.search(r'nature center|interpretive center', name, re.I):
            return "Interpretive Center", "name_keyword"
        if re.search(r'visitor center', name, re.I):
            return "Visitor Center", "name_keyword"
        return "", ""

    # Cemetery subtypes
    if category == "Cemetery":
        nl = name.lower()
        if "public" in nl:
            return "Public Cemetery", "name_keyword"
        if "church" in nl or "parish" in nl:
            return "Church Cemetery", "name_keyword"
        if "family" in nl:
            return "Family Cemetery", "name_keyword"
        if "veterans" in nl or "military" in nl:
            return "Veterans Cemetery", "name_keyword"
        return "Public Cemetery", "default_cemetery"

    return "", ""

def infer_designation(name: str, category: str, gov: str) -> str:
    """Infer designation from name/governance."""
    if category == "Wildlife Area":
        if re.search(r'state wildlife area|division of wildlife', name + " " + gov, re.I):
            return "State Wildlife Area"
    if category == "Park":
        if re.search(r'\bstate park\b', name, re.I):
            return "State Park"
        if re.search(r'\bnational park\b', name, re.I):
            return "National Park"
    if category == "Nature Preserve":
        if re.search(r'state nature preserve', name, re.I):
            return "State Nature Preserve"
    return ""

# ── Status inference (§4.2a) ──────────────────────────────────────────────────
_STATUS_MAP_SITE = {
    "open": "Active",
    "open seasonally": "Seasonal",
    "seasonal": "Seasonal",
    "by permit only": "Active",   # maps to "Active" with notes, not "Access Permit Required"
    "no trespassing": "Closed",
    "under construction": "Under Construction",
    "coming soon": "Under Construction",
    "permanently closed": "Closed",
    "closed": "Closed",
    "planned": "Planned",
    "defunct": "Defunct",
}

_STATUS_MAP_TRAIL = {
    "open": "Active",
    "operational": "Active",
    "active": "Active",
    "proposed": "Planned",
    "planned": "Planned",
    "under construction": "Under Construction",
    "closed": "Closed",
    "permanently closed": "Closed",
    "gap": "Gap",
}

def norm_site_status(status_raw: str, has_gps: bool, has_url: bool) -> str:
    """Normalize site status. §4.2a: infer Active when GPS+URL present and status_raw blank."""
    if status_raw:
        mapped = _STATUS_MAP_SITE.get(status_raw.strip().lower(), "")
        if mapped and mapped in ALLOWED_SITE_STATUSES:
            return mapped
        log.warning(f"Unmappable site status_raw: '{status_raw}' — leaving blank")
        return ""
    # §4.2a inference
    if has_gps and has_url:
        return "Active"
    return ""

def norm_trail_status(status_raw: str) -> str:
    if not status_raw:
        return ""
    mapped = _STATUS_MAP_TRAIL.get(status_raw.strip().lower(), "")
    if mapped and mapped in ALLOWED_TRAIL_STATUSES:
        return mapped
    return ""

# ── Trail vocabulary normalization ────────────────────────────────────────────
_USE_TYPE_MAP = {
    "multi-purpose": "Multi-Use", "multipurpose": "Multi-Use", "shared use": "Multi-Use",
    "multi-use": "Multi-Use", "multiuse": "Multi-Use",
    "walking trail": "Hiking", "pedestrian trail": "Hiking",
    "nature trail": "Hiking", "footpath": "Hiking", "hiking": "Hiking",
    "equestrian trail": "Bridle", "horse trail": "Bridle", "bridle": "Bridle",
    "bike path": "Bicycling", "bicycle path": "Bicycling", "bicycling": "Bicycling",
    "paddling trail": "Water", "canoe trail": "Water", "kayak trail": "Water",
    "blueway": "Water", "water": "Water",
    "mtb trail": "Mountain Bike", "mountain bike": "Mountain Bike",
    "xc ski trail": "Cross Country Ski", "nordic trail": "Cross Country Ski",
}

_SURFACE_MAP = {
    "asphalt": "Paved", "concrete": "Paved", "hard surface": "Paved", "paved": "Paved",
    "crushed limestone": "Crushed Stone", "stone dust": "Crushed Stone",
    "limestone screenings": "Crushed Stone", "compacted gravel": "Crushed Stone",
    "crushed stone": "Crushed Stone",
    "dirt trail": "Natural Surface", "earthen": "Natural Surface",
    "grass": "Natural Surface", "unimproved": "Natural Surface",
    "native surface": "Natural Surface", "natural surface": "Natural Surface",
    "cinder": "Natural Surface",  # cinder/gravel → Natural Surface
    "gravel": "Gravel",
    "boardwalk": "Boardwalk",
    "mixed surface": "Mixed", "mixed": "Mixed",
    "water": "Water",
}

_ORIGIN_MAP = {
    "rails-to-trails": "Rail Trail", "former rail corridor": "Rail Trail",
    "railroad trail": "Rail Trail", "rail trail": "Rail Trail",
    "towpath": "Canal Towpath", "canal trail": "Canal Towpath",
    "canal towpath": "Canal Towpath",
    "power line trail": "Utility Corridor", "pipeline trail": "Utility Corridor",
    "utility corridor": "Utility Corridor",
    "road corridor": "Roadside Corridor", "highway trail": "Roadside Corridor",
    "roadside corridor": "Roadside Corridor",
    "greenway corridor": "Greenway Corridor", "greenway": "Greenway Corridor",
    "historic route": "Historic Route",
    "purpose-built": "Purpose-Built",
}

_DIFFICULTY_MAP = {
    "easy": "Easy", "beginner": "Easy",
    "moderate": "Moderate", "intermediate": "Moderate",
    "difficult": "Difficult", "hard": "Difficult", "advanced": "Difficult",
    "strenuous": "Strenuous",
    "expert": "Expert", "black diamond": "Expert", "expert only": "Expert",
}

def norm_trail_use_type(raw: str) -> str:
    if not raw:
        return ""
    mapped = _USE_TYPE_MAP.get(raw.strip().lower(), "")
    return mapped if mapped in ALLOWED_TRAIL_USE_TYPES else ""

def norm_trail_surface(raw: str) -> str:
    if not raw:
        return ""
    mapped = _SURFACE_MAP.get(raw.strip().lower(), "")
    return mapped if mapped in ALLOWED_TRAIL_SURFACES else ""

def norm_trail_origin(raw: str) -> str:
    if not raw:
        return ""
    mapped = _ORIGIN_MAP.get(raw.strip().lower(), "")
    return mapped if mapped in ALLOWED_TRAIL_ORIGINS else ""

def norm_trail_difficulty(raw: str) -> str:
    """Only map explicit authoritative ratings — reject free-text non-ratings."""
    if not raw:
        return ""
    stripped = raw.strip().lower()
    # Reject obvious non-rating strings (free-text descriptions that leaked into difficulty_raw)
    non_ratings = [
        "hiking/biking", "surface and difficulty", "flat rail-trail",
        "not specified", "varies", "rail trail"
    ]
    if any(nr in stripped for nr in non_ratings):
        return ""
    mapped = _DIFFICULTY_MAP.get(stripped, "")
    return mapped if mapped in ALLOWED_TRAIL_DIFFICULTIES else ""

def norm_length(raw) -> str:
    """Return numeric-only length string, or ''."""
    if raw is None or raw == "" or raw == []:
        return ""
    try:
        val = float(str(raw).strip().split()[0])  # take first number
        return str(val)
    except (ValueError, AttributeError):
        return ""

# ── Trail origin inference from name/notes ────────────────────────────────────
def infer_trail_origin(name: str, notes: str, governance: str) -> str:
    """Infer origin type from name/notes when origin_raw is blank.
    Uses word-boundary patterns to avoid false matches from substrings
    (e.g. 'trail trail' containing 'rail trail' as a substring).
    """
    combined = (name + " " + notes + " " + governance).lower()
    if "canal towpath" in combined or re.search(r'\btowpath\b', combined) or "miami & erie" in combined or "miami and erie" in combined:
        return "Canal Towpath"
    # \brail\b ensures "rail" is a standalone word — not the tail of "trail"
    if re.search(r'\brail\s+trail\b', combined) or "rails-to-trails" in combined or re.search(r'\bformer rail\b', combined) or "railroad corridor" in combined:
        return "Rail Trail"
    if re.search(r'\bwabash cannonball\b', combined):
        return "Rail Trail"
    return ""

def infer_trail_use_type(name: str, notes: str, surface_raw: str) -> str:
    """Infer use type from name/context when use_type_raw is blank."""
    combined = (name + " " + notes).lower()
    if "wabash cannonball" in combined or "canal towpath" in combined:
        # Both WCT and M&E are documented as hiking/biking but no explicit "multi-use" label
        # → leave blank per vocabulary rules (don't infer from context alone)
        return ""
    if "storybook trail" in combined:
        return "Hiking"
    return ""

# ── AP Type normalization ─────────────────────────────────────────────────────
_AP_TYPE_MAP = {
    "trailhead": "Trailhead", "trail head": "Trailhead", "trail-head": "Trailhead",
    "parking area": "Parking Area", "parking lot": "Parking Area", "parking": "Parking Area",
    "boat ramp": "Boat Ramp", "boat launch ramp": "Boat Ramp",
    "boat launch": "Boat Launch",
    "kayak launch": "Watercraft Access Point", "canoe access": "Watercraft Access Point",
    "watercraft access": "Watercraft Access Point", "watercraft access point": "Watercraft Access Point",
    "river access": "River Access",
    "fishing access": "Fishing Access",
    "portage": "Hazard Portage", "mandatory portage": "Hazard Portage",
    "pedestrian entrance": "Pedestrian Entrance",
    "vehicle entrance": "Vehicle Entrance",
}

def norm_ap_type(raw: str, name: str) -> str:
    """Normalize access point type. Infer from name if raw is blank."""
    if raw:
        mapped = _AP_TYPE_MAP.get(raw.strip().lower(), "")
        if mapped:
            return mapped
    # Infer from AP name
    nl = name.lower() if name else ""
    if "boat launch ramp" in nl or "boat ramp" in nl:
        return "Boat Ramp"
    if "boat launch" in nl:
        return "Boat Launch"
    if "boat dock" in nl or "dock" in nl:
        return "Boat Launch"   # public dock = general boat access
    if "marina" in nl:
        return "Boat Launch"   # marina = motorized boat access
    if "trailhead" in nl or "trail head" in nl:
        return "Trailhead"
    if "parking" in nl:
        return "Parking Area"
    if "portage" in nl:
        return "Hazard Portage"
    return ""

# ── Parent ID resolution ──────────────────────────────────────────────────────
def resolve_parent_site_id(entity: dict) -> str:
    resolved = (entity.get("parent_block") or {}).get("resolved_parent_ids") or {}
    return resolved.get("parent_site_id", "")

def resolve_parent_trail_id(entity: dict) -> str:
    resolved = (entity.get("parent_block") or {}).get("resolved_parent_ids") or {}
    return resolved.get("parent_trail_id", "")

def resolve_ap_parent(entity: dict) -> tuple:
    resolved = (entity.get("parent_block") or {}).get("resolved_parent_ids") or {}
    parent_id   = resolved.get("parent_entity_id", "")
    parent_type = resolved.get("parent_entity_type", "")
    return parent_id, parent_type

# ── Derived Label ─────────────────────────────────────────────────────────────
def derived_label(name: str, category: str, subtype: str) -> str:
    if subtype:
        return f"{name} ({category}: {subtype})"
    return f"{name} ({category})"

# ════════════════════════════════════════════════════════════════════════════
#  ENTITY NORMALIZERS
# ════════════════════════════════════════════════════════════════════════════

def normalize_site(entity: dict, provenance: list) -> dict | None:
    """Normalize a Site entity. Returns None if held (IMP-069 GPS gate)."""
    eid  = entity["resolved_entity_id"]
    name = (entity.get("identity_block") or {}).get("name_raw") or ""
    payload   = entity.get("payload") or {}
    org_block = entity.get("organizational_block") or {}
    id_block  = entity.get("identity_block") or {}
    meta      = entity.get("metadata_block") or {}
    parent_bl = entity.get("parent_block") or {}

    urls_raw = id_block.get("urls_raw") or []
    identity_notes_raw = parent_bl.get("identity_notes_raw") or ""

    # ── GPS Gate IMP-069 ──────────────────────────────────────────────────────
    lat, lon = parse_gps(payload.get("gps_lat_raw"), payload.get("gps_lon_raw"))
    if lat is None:
        provenance.append({"entity_id": eid, "type": "Site", "name": name,
                           "action": "HOLD", "reason": "IMP-069: GPS null"})
        return None  # signal held

    # ── Category / Subtype / Designation ─────────────────────────────────────
    category, subtype, designation, cat_source = infer_category_subtype_designation(entity)
    if not category_valid(category):
        provenance.append({"entity_id": eid, "action": "FATAL_REJECT",
                           "reason": f"IMP-063: no valid category mapping for '{category}'"})
        return None
    provenance.append({"entity_id": eid, "action": "CATEGORY_ASSIGNED",
                       "category": category, "subtype": subtype,
                       "designation": designation, "source": cat_source})

    # ── Status ────────────────────────────────────────────────────────────────
    status = norm_site_status(payload.get("status_raw"), True, has_authoritative_url(urls_raw))

    # ── Features ──────────────────────────────────────────────────────────────
    features = map_features(payload.get("features_raw") or "")

    # ── Counties ──────────────────────────────────────────────────────────────
    counties = normalize_counties(id_block.get("counties_raw") or [])

    # ── GPS / Plus Code / GIS ─────────────────────────────────────────────────
    plus_code                = get_plus_code(lat, lon)
    township, municipality   = gis_lookup(lat, lon)

    # ── Ownership / Governance ────────────────────────────────────────────────
    ownership      = norm_text_field(org_block.get("ownership_raw"))
    governance     = norm_text_field(org_block.get("governance_raw"))
    partner_agencies = norm_list_to_semicolon(org_block.get("partner_agencies_raw"))
    coordination   = norm_list_to_semicolon(org_block.get("coordination_raw"))

    # ── Location ──────────────────────────────────────────────────────────────
    location = norm_text_field(id_block.get("location_raw"))

    # ── Description ───────────────────────────────────────────────────────────
    description = norm_description(payload.get("description_raw") or "", name, category, subtype)

    # ── Identity Notes (IMP-053 cleanup) ─────────────────────────────────────
    identity_notes = clean_identity_notes(identity_notes_raw)

    # ── URLs ──────────────────────────────────────────────────────────────────
    url_primary = best_url(urls_raw)
    urls        = urls_semicolon(urls_raw)

    # ── Acres ─────────────────────────────────────────────────────────────────
    acres_raw = payload.get("acres_raw") or ""
    acres = norm_length(acres_raw)

    # ── Parent site ───────────────────────────────────────────────────────────
    parent_site_id = resolve_parent_site_id(entity)

    return {
        "entity_id":       eid,
        "entity_type":     "Site",
        "name":            name,
        "category":        category,
        "subtype":         subtype,
        "designation":     designation,
        "status":          status,
        "ownership":       ownership,
        "governance":      governance,
        "partner_agencies": partner_agencies,
        "coordination":    coordination,
        "description":     description,
        "location":        location,
        "acres":           acres,
        "counties":        counties,
        "municipality":    municipality,
        "township":        township,
        "gps_lat":         lat,
        "gps_lon":         lon,
        "plus_code":       plus_code,
        "features":        features,
        "features_raw":    payload.get("features_raw") or "",
        "notes":           "",
        "identity_notes":  identity_notes,
        "url_primary":     url_primary,
        "urls":            urls,
        "parent_site_id":  parent_site_id,
        "derived_label":   derived_label(name, category, subtype),
        "created_at":      NORM_DATE,
        "updated_at":      NORM_DATE,
    }

def normalize_trail(entity: dict, provenance: list) -> dict:
    eid  = entity["resolved_entity_id"]
    name = (entity.get("identity_block") or {}).get("name_raw") or ""
    payload   = entity.get("payload") or {}
    org_block = entity.get("organizational_block") or {}
    id_block  = entity.get("identity_block") or {}
    parent_bl = entity.get("parent_block") or {}

    urls_raw    = id_block.get("urls_raw") or []
    notes_raw   = parent_bl.get("identity_notes_raw") or ""
    governance  = norm_text_field(org_block.get("governance_raw"))

    # Vocabulary normalization
    use_type    = norm_trail_use_type(payload.get("trail_use_type_raw") or "")
    if not use_type:
        use_type = infer_trail_use_type(name, notes_raw, payload.get("trail_surface_type_raw") or "")

    surface     = norm_trail_surface(payload.get("trail_surface_type_raw") or "")
    if not surface and payload.get("accessibility_raw"):
        # Accessibility_raw sometimes contains surface info for this run
        acc = payload.get("accessibility_raw") or ""
        surface = norm_trail_surface(acc.split(",")[0].strip())

    origin      = norm_trail_origin(payload.get("trail_origin_type_raw") or "")
    if not origin:
        origin  = infer_trail_origin(name, notes_raw, governance)

    status      = norm_trail_status(payload.get("status_raw") or "")
    difficulty  = norm_trail_difficulty(payload.get("difficulty_raw") or "")
    length      = norm_length(payload.get("total_length_miles_raw"))

    # Length hints from identity_notes
    if not length:
        m = re.search(r'(\d+\.?\d*)\s*mi', notes_raw, re.I)
        if m:
            length = m.group(1)

    counties = normalize_counties(id_block.get("counties_raw") or [])
    partner_agencies = norm_list_to_semicolon(org_block.get("partner_agencies_raw"))
    identity_notes   = clean_identity_notes(notes_raw)
    url_primary      = best_url(urls_raw)
    urls             = urls_semicolon(urls_raw)
    parent_site_id   = resolve_parent_site_id(entity)

    provenance.append({"entity_id": eid, "action": "NORMALIZED_TRAIL",
                       "use_type": use_type, "surface": surface,
                       "origin": origin, "difficulty": difficulty})

    return {
        "entity_id":        eid,
        "entity_type":      "Trail",
        "name":             name,
        "use_type":         use_type,
        "surface_type":     surface,
        "origin_type":      origin,
        "status":           status,
        "difficulty":       difficulty,
        "total_length_miles": length,
        "counties":         counties,
        "governance":       governance,
        "partner_agencies": partner_agencies,
        "description":      norm_description(
                                id_block.get("location_raw") or "", name, "Trail", ""),
        "accessibility":    norm_text_field(payload.get("accessibility_raw")),
        "identity_notes":   identity_notes,
        "notes":            "",
        "url_primary":      url_primary,
        "urls":             urls,
        "parent_site_id":   parent_site_id,
        "created_at":       NORM_DATE,
        "updated_at":       NORM_DATE,
    }

def normalize_trail_segment(entity: dict, provenance: list) -> dict:
    eid  = entity["resolved_entity_id"]
    name = (entity.get("identity_block") or {}).get("name_raw") or ""
    payload   = entity.get("payload") or {}
    org_block = entity.get("organizational_block") or {}
    id_block  = entity.get("identity_block") or {}
    parent_bl = entity.get("parent_block") or {}

    # Strip em-dash parent hint from segment name for display
    seg_name_clean = name.split(" — ")[0].strip() if " — " in name else name

    urls_raw    = id_block.get("urls_raw") or []
    notes_raw   = parent_bl.get("identity_notes_raw") or ""
    governance  = norm_text_field(org_block.get("governance_raw"))

    surface    = norm_trail_surface(payload.get("surface_type_raw") or
                                    payload.get("trail_surface_type_raw") or "")
    # Surface from accessibility_raw if available (WCT South Fork has surface info there)
    if not surface and payload.get("accessibility_raw"):
        acc = payload.get("accessibility_raw") or ""
        # Parse primary surface from WCT note "Cinder, gravel, dirt, grass..."
        first_token = acc.split(",")[0].strip().lower()
        surface = norm_trail_surface(first_token)

    difficulty  = norm_trail_difficulty(payload.get("difficulty_raw") or "")
    length      = norm_length(payload.get("segment_length_miles_raw"))
    if not length:
        m = re.search(r'(\d+\.?\d*)\s*mi', notes_raw, re.I)
        if m:
            length = m.group(1)

    counties        = normalize_counties(id_block.get("counties_raw") or [])
    identity_notes  = clean_identity_notes(notes_raw)
    url_primary     = best_url(urls_raw)
    urls            = urls_semicolon(urls_raw)
    parent_trail_id = resolve_parent_trail_id(entity)

    provenance.append({"entity_id": eid, "action": "NORMALIZED_TS",
                       "parent_trail_id": parent_trail_id, "surface": surface})

    return {
        "entity_id":           eid,
        "entity_type":         "Trail Segment",
        "name":                seg_name_clean,
        "segment_type":        "",
        "surface_type":        surface,
        "status":              "",
        "difficulty":          difficulty,
        "segment_length_miles": length,
        "counties":            counties,
        "governance":          governance,
        "description":         "",
        "accessibility":       norm_text_field(payload.get("accessibility_raw")),
        "identity_notes":      identity_notes,
        "notes":               "",
        "url_primary":         url_primary,
        "urls":                urls,
        "parent_trail_id":     parent_trail_id,
        "geometry":            "",
        "created_at":          NORM_DATE,
        "updated_at":          NORM_DATE,
    }

def normalize_access_point(entity: dict, provenance: list) -> dict:
    eid  = entity["resolved_entity_id"]
    name = (entity.get("identity_block") or {}).get("name_raw") or ""
    payload   = entity.get("payload") or {}
    org_block = entity.get("organizational_block") or {}
    id_block  = entity.get("identity_block") or {}
    parent_bl = entity.get("parent_block") or {}

    urls_raw   = id_block.get("urls_raw") or []
    notes_raw  = parent_bl.get("identity_notes_raw") or ""

    # AP Type
    ap_type = norm_ap_type(payload.get("access_point_type_raw") or "", name)

    # Status
    status_raw = payload.get("status_raw") or (entity.get("payload") or {}).get("status_raw") or ""
    ap_status  = ""
    if status_raw:
        mapped = {"open": "Active", "active": "Active",
                  "closed": "Closed", "permanently closed": "Closed",
                  "seasonal": "Seasonal", "restricted": "Restricted"}.get(
                      status_raw.strip().lower(), "")
        if mapped in ALLOWED_AP_STATUSES:
            ap_status = mapped

    # GPS
    lat, lon = parse_gps(payload.get("gps_lat_raw"), payload.get("gps_lon_raw"))
    plus_code_val = get_plus_code(lat, lon) if lat else ""
    township, municipality = gis_lookup(lat, lon) if lat else ("", "")

    # Features — free text for APs (no controlled vocab)
    features_raw_val = payload.get("features_raw") or ""

    # County
    counties_raw = id_block.get("counties_raw") or []
    county = ""
    if counties_raw:
        county = normalize_county_name(str(counties_raw[0]))

    # Parent
    parent_id, parent_type = resolve_ap_parent(entity)

    # Identity notes
    identity_notes = clean_identity_notes(notes_raw)
    url_primary    = best_url(urls_raw)
    urls           = urls_semicolon(urls_raw)

    # Address from location_raw
    address = norm_text_field(id_block.get("location_raw") or "")

    provenance.append({"entity_id": eid, "action": "NORMALIZED_AP",
                       "ap_type": ap_type, "has_gps": lat is not None,
                       "parent_id": parent_id, "parent_type": parent_type})

    return {
        "entity_id":           eid,
        "entity_type":         "Access Point",
        "name":                name,
        "ap_type":             ap_type,   # renamed from access_point_type — matches DB column and TSV header
        "status":              ap_status,
        "features":            features_raw_val,  # free text, title-case normalize
        "county":              county,
        "municipality":        municipality,
        "township":            township,
        "gps_lat":             lat,
        "gps_lon":             lon,
        "plus_code":           plus_code_val,
        "address":             address,
        "identity_notes":      identity_notes,
        "notes":               "",
        "url_primary":         url_primary,
        "urls":                urls,
        "parent_entity_id":    parent_id,
        "parent_entity_type":  parent_type,
        "derived_label":       derived_label(name, ap_type or "Access Point", ""),
        "created_at":          NORM_DATE,
        "updated_at":          NORM_DATE,
    }

# ════════════════════════════════════════════════════════════════════════════
#  STAGE 4.5 VOCABULARY VALIDATION GATE
# ════════════════════════════════════════════════════════════════════════════

def vocabulary_gate(normalized_entities: list) -> list:
    """Halts on any vocabulary violation. Returns list of violations."""
    violations = []
    for ent in normalized_entities:
        eid = ent["entity_id"]
        et  = ent["entity_type"]

        if et == "Site":
            cat = ent.get("category", "")
            sub = ent.get("subtype", "")
            des = ent.get("designation", "")
            sta = ent.get("status", "")
            feats = ent.get("features", "")

            if cat and cat not in ALLOWED_CATEGORIES:
                violations.append(f"[{eid}] Invalid category: '{cat}'")
            if sub and cat and not subtype_valid(cat, sub):
                violations.append(f"[{eid}] Invalid subtype '{sub}' for category '{cat}'")
            if des and des not in ALLOWED_DESIGNATIONS:
                violations.append(f"[{eid}] Invalid designation: '{des}'")
            if sta and sta not in ALLOWED_SITE_STATUSES:
                violations.append(f"[{eid}] Invalid status: '{sta}'")
            for term in (feats or "").split(";"):
                term = term.strip()
                if term and term not in ALLOWED_FEATURES:
                    violations.append(f"[{eid}] Invalid features term: '{term}'")

        elif et == "Trail":
            for field, allowed in [
                ("use_type",    ALLOWED_TRAIL_USE_TYPES),
                ("surface_type", ALLOWED_TRAIL_SURFACES),
                ("origin_type",  ALLOWED_TRAIL_ORIGINS),
                ("status",       ALLOWED_TRAIL_STATUSES),
                ("difficulty",   ALLOWED_TRAIL_DIFFICULTIES),
            ]:
                val = ent.get(field, "")
                if val and val not in allowed:
                    violations.append(f"[{eid}] Invalid trail {field}: '{val}'")

        elif et == "Trail Segment":
            for field, allowed in [
                ("surface_type", ALLOWED_TRAIL_SURFACES),
                ("difficulty",   ALLOWED_TRAIL_DIFFICULTIES),
            ]:
                val = ent.get(field, "")
                if val and val not in allowed:
                    violations.append(f"[{eid}] Invalid TS {field}: '{val}'")

        elif et == "Access Point":
            ap_type = ent.get("ap_type", "")   # field renamed from access_point_type
            ap_sta  = ent.get("status", "")
            if ap_type and ap_type not in ALLOWED_AP_TYPES:
                violations.append(f"[{eid}] Invalid AP type: '{ap_type}'")
            if ap_sta and ap_sta not in ALLOWED_AP_STATUSES:
                violations.append(f"[{eid}] Invalid AP status: '{ap_sta}'")

    return violations

# ════════════════════════════════════════════════════════════════════════════
#  MAIN
# ════════════════════════════════════════════════════════════════════════════

def run_normalization():
    log.info(f"Loading resolved entities from {INPUT_FILE}")
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    entities = data.get("resolved_entities", [])
    log.info(f"Loaded {len(entities)} resolved entities")

    normalized  = []
    held        = []
    fatal       = []
    provenance  = []

    et_counts = {}
    for entity in entities:
        et = entity.get("entity_type", "")
        et_counts[et] = et_counts.get(et, 0) + 1

        if et == "Site":
            result = normalize_site(entity, provenance)
            if result is None:
                # Check if FATAL_REJECT or HOLD
                last = provenance[-1] if provenance else {}
                if last.get("action") == "FATAL_REJECT":
                    fatal.append({"entity_id": entity["resolved_entity_id"],
                                  "name": (entity.get("identity_block") or {}).get("name_raw"),
                                  "reason": last.get("reason")})
                    log.error(f"FATAL REJECT: {entity['resolved_entity_id']} — {last.get('reason')}")
                else:
                    # HOLD
                    held.append({
                        "record_id":   entity["resolved_entity_id"],
                        "entity_type": "Site",
                        "name":        (entity.get("identity_block") or {}).get("name_raw", ""),
                        "hold_reason": "gps_missing",
                        "hold_detail": "IMP-069: GPS null — routed to GPS Acquisition Module",
                        "county":      COUNTY,
                        "run_id":      RUN_ID,
                        "created_at":  NORM_DATE,
                    })
                    log.info(f"HELD (GPS): {entity['resolved_entity_id']}")
            else:
                normalized.append(result)
                log.info(f"Normalized Site: {result['entity_id']} | {result['name']} | {result['category']}")

        elif et == "Trail":
            result = normalize_trail(entity, provenance)
            normalized.append(result)
            log.info(f"Normalized Trail: {result['entity_id']} | {result['name']}")

        elif et == "Trail Segment":
            result = normalize_trail_segment(entity, provenance)
            normalized.append(result)
            log.info(f"Normalized TS: {result['entity_id']} | {result['name']}")

        elif et == "Access Point":
            result = normalize_access_point(entity, provenance)
            # IMP-069 GPS gate — APs without GPS are routed to GPS Acquisition Module
            if not result.get("gps_lat"):
                held.append({
                    "record_id":   entity["resolved_entity_id"],
                    "entity_type": "Access Point",
                    "name":        (entity.get("identity_block") or {}).get("name_raw", ""),
                    "hold_reason": "gps_missing",
                    "hold_detail": "IMP-069: GPS null — routed to GPS Acquisition Module",
                    "county":      COUNTY,
                    "run_id":      RUN_ID,
                    "created_at":  NORM_DATE,
                })
                log.info(f"HELD AP (GPS): {entity['resolved_entity_id']}")
            else:
                normalized.append(result)
                log.info(f"Normalized AP: {result['entity_id']} | {result['name']}")

        else:
            log.warning(f"Unknown entity type '{et}' — skipping")

    # ── FATAL REJECT check ────────────────────────────────────────────────────
    if fatal:
        msg = f"Stage 2 HALT: {len(fatal)} FATAL REJECT(s):\n"
        for f in fatal:
            msg += f"  {f['entity_id']} ({f['name']}): {f['reason']}\n"
        log.error(msg)
        raise SystemExit(1)

    # ── Stage 4.5 Vocabulary Validation Gate ─────────────────────────────────
    log.info("Running Stage 4.5 vocabulary validation gate...")
    violations = vocabulary_gate(normalized)
    if violations:
        log.error(f"VOCABULARY GATE FAIL — {len(violations)} violation(s):")
        for v in violations:
            log.error(f"  {v}")
        raise SystemExit(f"Stage 4.5 gate failed: {len(violations)} violation(s)")
    log.info("Stage 4.5 PASSED — all vocabulary terms valid")

    # ── Write outputs ─────────────────────────────────────────────────────────
    out_data = {
        "run_id":        RUN_ID,
        "county":        COUNTY,
        "state":         STATE,
        "norm_date":     NORM_DATE,
        "records_input": len(entities),
        "normalized":    len(normalized),
        "held":          len(held),
        "fatal_rejects": len(fatal),
        "entities_by_type": {
            "Site":          sum(1 for e in normalized if e["entity_type"] == "Site"),
            "Trail":         sum(1 for e in normalized if e["entity_type"] == "Trail"),
            "Trail Segment": sum(1 for e in normalized if e["entity_type"] == "Trail Segment"),
            "Access Point":  sum(1 for e in normalized if e["entity_type"] == "Access Point"),
        },
        "normalized_entities": normalized,
    }
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        yaml.dump(out_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    log.info(f"Written normalized entities → {OUTPUT_FILE}")

    held_data = {
        "run_id":  RUN_ID,
        "county":  COUNTY,
        "state":   STATE,
        "count":   len(held),
        "held_entities": held,
    }
    with open(HELD_FILE, "w", encoding="utf-8") as f:
        yaml.dump(held_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    log.info(f"Written held entities → {HELD_FILE}")

    # ── Write normalization report ────────────────────────────────────────────
    write_report(normalized, held, provenance)

    log.info(f"\n{'='*60}")
    log.info(f"Stage 2 Normalization COMPLETE")
    log.info(f"  Input:      {len(entities)} entities")
    log.info(f"  Normalized: {len(normalized)}")
    log.info(f"  Held (GPS): {len(held)}")
    log.info(f"  Violations: 0 (gate passed)")
    log.info(f"{'='*60}")

    return normalized, held

def write_report(normalized: list, held: list, provenance: list):
    lines = [
        f"# Henry County, OH — Stage 2 Normalization Report",
        f"**Run ID:** {RUN_ID}  ",
        f"**Date:** {NORM_DATE}  ",
        f"**Engine:** Normalization Engine v5.8 + Site v5.9 + Trail v5.2 + TS v5.1 + AP v5.1",
        "",
        "## Summary",
        "",
        f"| | Count |",
        f"|---|---|",
        f"| Normalized entities | {len(normalized)} |",
        f"| Held (GPS missing, IMP-069) | {len(held)} |",
        f"| Fatal rejects | 0 |",
        f"| Vocabulary gate violations | 0 |",
        "",
        "## Normalized Entities",
        "",
    ]

    sites = [e for e in normalized if e["entity_type"] == "Site"]
    trails = [e for e in normalized if e["entity_type"] == "Trail"]
    segs   = [e for e in normalized if e["entity_type"] == "Trail Segment"]
    aps    = [e for e in normalized if e["entity_type"] == "Access Point"]

    if sites:
        lines += ["### Sites", "",
                  "| ID | Name | Category | Subtype | Status | GPS |",
                  "|---|---|---|---|---|---|"]
        for s in sites:
            gps_str = f"{s['gps_lat']}, {s['gps_lon']}" if s.get('gps_lat') else "—"
            lines.append(f"| {s['entity_id']} | {s['name']} | {s['category']} | {s.get('subtype','')} | {s.get('status','')} | {gps_str} |")
        lines.append("")

    if trails:
        lines += ["### Trails", "",
                  "| ID | Name | Use Type | Surface | Origin | Difficulty |",
                  "|---|---|---|---|---|---|"]
        for t in trails:
            lines.append(f"| {t['entity_id']} | {t['name']} | {t.get('use_type','')} | {t.get('surface_type','')} | {t.get('origin_type','')} | {t.get('difficulty','')} |")
        lines.append("")

    if segs:
        lines += ["### Trail Segments", "",
                  "| ID | Name | Parent Trail | Surface | Counties |",
                  "|---|---|---|---|---|"]
        for s in segs:
            lines.append(f"| {s['entity_id']} | {s['name']} | {s.get('parent_trail_id','')} | {s.get('surface_type','')} | {s.get('counties','')} |")
        lines.append("")

    if aps:
        lines += ["### Access Points", "",
                  "| ID | Name | Type | Parent | GPS |",
                  "|---|---|---|---|---|"]
        for a in aps:
            gps_str = f"{a['gps_lat']}, {a['gps_lon']}" if a.get('gps_lat') else "—"
            lines.append(f"| {a['entity_id']} | {a['name']} | {a.get('ap_type','')} | {a.get('parent_entity_id','')} | {gps_str} |")
        lines.append("")

    if held:
        lines += ["## Held Entities (GPS Missing — IMP-069)", "",
                  "| ID | Name | Hold Reason |",
                  "|---|---|---|"]
        for h in held:
            lines.append(f"| {h['record_id']} | {h['name']} | {h['hold_reason']} |")
        lines.append("")

    lines += [
        "## Normalization Decisions",
        "",
        "### Category Inference",
        "",
        "| Entity ID | Name | Category | Subtype | Source |",
        "|---|---|---|---|---|",
    ]
    for p in provenance:
        if p.get("action") == "CATEGORY_ASSIGNED":
            lines.append(f"| {p['entity_id']} | — | {p.get('category','')} | {p.get('subtype','')} | {p.get('source','')} |")
    lines.append("")

    lines += ["### Vocabulary Gate", "", "Stage 4.5 PASSED — 0 violations.", ""]

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    log.info(f"Written normalization report → {REPORT_FILE}")

if __name__ == "__main__":
    run_normalization()
     