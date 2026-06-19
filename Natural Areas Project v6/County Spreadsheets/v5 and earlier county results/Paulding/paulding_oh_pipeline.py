#!/usr/bin/env python3
# =============================================================================
# SUPERSEDED — IMP-091 (2026-05-04)
# This monolithic pipeline script has been replaced by the parameterised model:
#   utilities/na_run_county.py + County_Spreadsheets/{County}/{county}_pipeline_config.json
# Do not use for new county runs. Kept for reference only.
# =============================================================================
"""
paulding_oh_pipeline.py — Natural Areas Project
Paulding County, Ohio — Full Pipeline Script
Stages: GPS Acquisition → Normalization → TSV Output → Integrity Check → SQLite Upsert

Generated: 2026-04-08
Entities: 22 Sites, 4 Trails, 1 Trail Network, 5 Access Points (32 total)
Held:
  PAU-S-009  Guilda H. Culler Memorial Park   gps_missing (no address known)
  PAU-S-021  Flat Rock Creek Nature Preserve  gps_missing (ACRES closed preserve)
  PAU-AP-005 Viall's Lock Campsite            gps_missing (no specific coords found)

USAGE:
  cd "Natural Areas Project v5"
  python County_Spreadsheets/Paulding/paulding_oh_pipeline.py [--db PATH] [--dry-run]

OPTIONS:
  --db PATH     Path to SQLite database (default: NASqlite/natural_areas_v5.db)
  --dry-run     Print SQL without executing; still writes TSVs
"""

import sys
import os
import time
import sqlite3
import argparse
import csv
from datetime import datetime, timezone

# ── Path setup ──────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
UTIL_DIR = os.path.join(PROJECT_ROOT, 'utilities')
sys.path.insert(0, UTIL_DIR)

try:
    from na_plus_code import encode_plus_code
except ImportError:
    print("ERROR: Cannot import na_plus_code from utilities/. Run from project root.", file=sys.stderr)
    sys.exit(1)

try:
    from na_township_lookup import OhioTownshipLookup
    _LOOKUP = OhioTownshipLookup()
    _LOOKUP_AVAILABLE = True
except Exception as e:
    print(f"WARNING: OhioTownshipLookup unavailable ({e}). Township/municipality fields will be blank.")
    _LOOKUP_AVAILABLE = False

try:
    import requests
    _REQUESTS_OK = True
except ImportError:
    print("WARNING: 'requests' not available. GPS acquisition via Nominatim disabled.")
    _REQUESTS_OK = False

# ── Config ───────────────────────────────────────────────────────────────────
COUNTY = "Paulding"
STATE = "Ohio"
RUN_ID = "paulding_oh_2026_04_08"
RUN_DATE = "2026-04-08"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
OUTPUT_DIR = SCRIPT_DIR  # TSVs written alongside this script
DEFAULT_DB = os.path.join(PROJECT_ROOT, "NASqlite", "natural_areas_v5.db")

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
NOMINATIM_DELAY = 1.1  # seconds between requests (Nominatim policy: 1 req/sec)
NOMINATIM_HEADERS = {
    "User-Agent": "NaturalAreasProject/5.x (research use; admin contact available)",
    "Accept-Language": "en"
}

# ── Paulding County bounding box (rough plausibility check) ──────────────────
PAULDING_LAT_MIN, PAULDING_LAT_MAX = 40.97, 41.25
PAULDING_LON_MIN, PAULDING_LON_MAX = -84.81, -84.25

# ── Village centroids (fallback when Nominatim fails) ────────────────────────
VILLAGE_CENTROIDS = {
    "Paulding":    (41.1370, -84.5730),
    "Antwerp":     (41.1814, -84.7352),
    "Payne":       (41.0794, -84.7269),
    "Oakwood":     (41.0966, -84.3892),
    "Latty":       (41.0908, -84.5862),
    "Grover Hill": (41.0177, -84.4784),
    "Junction":    (41.1283, -84.7023),
    "Cecil":       (41.1969, -84.5775),
}

# ── Hardcoded GPS from research (entities without precise addresses) ──────────
# These bypass Nominatim entirely and are used directly in normalization.
# Sources noted in comments.
HARDCODED_GPS = {
    # Forrest Woods SNP: ~3/4 mile north of Forder Bridge on CR-73
    # Forder Bridge = 41.223, -84.670 (HMDB historical marker source)
    # +0.014 deg lat ≈ 3/4 mile; medium confidence
    "PAU-S-002": (41.237, -84.670, "Research: ~0.75 mi N of Forder Bridge on CR-73 (HMDB ref)"),

    # Forder Bridge Conservation Area: at Forder Bridge on the Maumee River
    # DMS: 41°13.391'N, 84°40.187'W → 41.2232, -84.6698 (high confidence, HMDB)
    "PAU-S-020": (41.2232, -84.6698, "HMDB historical marker (Forder Bridge, CR-73 at Maumee River)"),

    # Forder Bridge Water Trail Access: same geographic location as S-020
    "PAU-AP-004": (41.2232, -84.6698, "HMDB historical marker (Forder Bridge, CR-73 at Maumee River)"),
}


# ═══════════════════════════════════════════════════════════════════════════
# GPS ACQUISITION
# ═══════════════════════════════════════════════════════════════════════════

def nominatim_query(query_str):
    """Query Nominatim for a location string; return (lat, lon) or None."""
    if not _REQUESTS_OK:
        return None
    try:
        r = requests.get(
            NOMINATIM_URL,
            params={"q": query_str, "format": "json", "limit": 1, "countrycodes": "us"},
            headers=NOMINATIM_HEADERS,
            timeout=10
        )
        r.raise_for_status()
        results = r.json()
        if results:
            lat = float(results[0]["lat"])
            lon = float(results[0]["lon"])
            return (lat, lon)
        return None
    except Exception as e:
        print(f"  Nominatim error for '{query_str}': {e}")
        return None

def plausible_paulding(lat, lon):
    """Return True if coordinate is within Paulding County bounding box."""
    return (PAULDING_LAT_MIN <= lat <= PAULDING_LAT_MAX and
            PAULDING_LON_MIN <= lon <= PAULDING_LON_MAX)

def acquire_gps(record_id, queries, fallback_village=None):
    """
    Try each Nominatim query in order. If plausible result found, return it.
    Otherwise fall back to village centroid if provided.
    Returns (lat, lon, method_note) or (None, None, reason).
    """
    # Check hardcoded GPS first (highest confidence for non-addressed entities)
    if record_id in HARDCODED_GPS:
        lat, lon, method = HARDCODED_GPS[record_id]
        print(f"  {record_id}: Using hardcoded GPS ({lat:.5f}, {lon:.5f}) — {method}")
        return lat, lon, method

    for q in queries:
        result = nominatim_query(q)
        time.sleep(NOMINATIM_DELAY)
        if result:
            lat, lon = result
            if plausible_paulding(lat, lon):
                print(f"  {record_id}: GPS acquired via Nominatim ({lat:.5f}, {lon:.5f})")
                return lat, lon, f"Nominatim: {q}"
            else:
                print(f"  {record_id}: Nominatim result out of county bounds ({lat:.5f}, {lon:.5f}), trying next query")

    # Fallback to village centroid
    if fallback_village and fallback_village in VILLAGE_CENTROIDS:
        lat, lon = VILLAGE_CENTROIDS[fallback_village]
        print(f"  {record_id}: Using {fallback_village} village centroid ({lat:.5f}, {lon:.5f})")
        return lat, lon, f"Centroid: Village of {fallback_village}"

    print(f"  {record_id}: GPS not acquired; entity will be HELD")
    return None, None, "gps_missing"


# ═══════════════════════════════════════════════════════════════════════════
# NORMALIZATION HELPERS
# ═══════════════════════════════════════════════════════════════════════════

def get_gis(lat, lon):
    """Return (township, municipality) from GIS lookup or ('', '')."""
    if not _LOOKUP_AVAILABLE or lat is None:
        return "", ""
    try:
        # get_both() returns a (township, municipality) tuple
        twp, mun = _LOOKUP.get_both(lat, lon)
        return (twp or ""), (mun or "")
    except Exception as e:
        print(f"  GIS lookup error: {e}")
        return "", ""

def get_plus_code(lat, lon):
    """Return Plus Code string or empty string."""
    if lat is None or lon is None:
        return ""
    return encode_plus_code(lat, lon)

def clean(val):
    """Strip and sanitize a field value — no tabs, no newlines."""
    if val is None:
        return ""
    return str(val).strip().replace("\t", " ").replace("\n", " ").replace("\r", " ")

def acres_float(val):
    """Convert acreage string to float or None."""
    if not val:
        return None
    try:
        return float(str(val).replace(",", "").strip())
    except ValueError:
        return None


# ═══════════════════════════════════════════════════════════════════════════
# ENTITY DATA — RAW (pre-normalization)
# Values from paulding_oh_raw_discovery.yaml; normalized below.
# ═══════════════════════════════════════════════════════════════════════════

# Each site dict carries everything needed for normalization + TSV + upsert.
# GPS fields start blank; filled during GPS acquisition stage below.

SITES_RAW = [
    {
        "record_id": "PAU-S-001",
        "name": "Lake Wayne R. Carr Wildlife Area",
        "category": "Wildlife Area",
        "subtype": "State Wildlife Area",
        "designation": "State Wildlife Area",
        "status": "Active",
        "ownership": "State of Ohio",
        "governance": "ODNR Division of Wildlife",
        "partner_agencies": "",
        "coordination": "",
        "description": (
            "Lake Wayne R. Carr Wildlife Area is an ODNR Division of Wildlife managed area in "
            "Paulding County, Ohio. The area centers on a small lake (Wayne R. Carr Lake) and "
            "provides public hunting and fishing access. Watercraft permitted at idle speed only — "
            "no wake allowed on the lake. Area covers approximately 18 acres."
        ),
        "location": "Paulding County, Ohio",
        "acres": "18.34",
        "counties": "Paulding",
        "municipality_override": "",
        "features": "Fishing Area; Hunting Area; Watercraft Access",
        "notes": "Powercraft restricted to idle speed on Wayne R. Carr Lake per Ohio Admin Code Rule 1501:31-5-02.",
        "url_primary": "https://wildlife.ohiodnr.gov/",
        "urls": "",
        "parent_site_id": "",
        "nominatim_queries": [
            "Lake Wayne R Carr Wildlife Area, Paulding County, Ohio",
            "Wayne R Carr Lake, Paulding County, Ohio",
        ],
        "fallback_village": None,
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-002",
        "name": "Forrest Woods State Nature Preserve",
        "category": "Nature Preserve",
        "subtype": "State Nature Preserve",
        "designation": "State Nature Preserve",
        "status": "Active",
        "ownership": "Black Swamp Conservancy",
        "governance": "Black Swamp Conservancy",
        "partner_agencies": "Black Swamp Conservancy; ODNR DNAP",
        "coordination": "",
        "description": (
            "Forrest Woods State Nature Preserve is one of the highest-quality remnants of the "
            "historic Great Black Swamp in northwest Ohio. Black Swamp Conservancy's largest owned "
            "nature preserve. Contains mature upland and floodplain forest with 39+ rare, threatened, "
            "and endangered plant and animal species. Portions dedicated as a State Nature Preserve "
            "by ODNR DNAP in 2008. Access is restricted; contact BSC. Active BSC restoration ongoing."
        ),
        "location": "County Road 73, north of Forder's Bridge, Paulding County, Ohio",
        "acres": "292",
        "counties": "Paulding",
        "municipality_override": "",
        "features": "Old-Growth Stand; Floodplain Forest; Upland Forest",
        "notes": (
            "Acreage from baseline (292 ac); alternate sources cite 193–346 ac reflecting property expansions. "
            "ODNR state designation covers portions; BSC owns full property. Visitors must contact BSC. "
            "GPS approximate — area near County Road 73 / Forder's Bridge."
        ),
        "url_primary": "https://blackswamp.org/",
        "urls": "https://naturepreserves.ohiodnr.gov/; https://members.wetlandsofdistinction.org/woddirectory/Details/forrest-woods-state-nature-preserve-2016228",
        "parent_site_id": "",
        "nominatim_queries": [
            "Forrest Woods State Nature Preserve, Paulding County, Ohio",
            "County Road 73 Forder Bridge Paulding County Ohio",
        ],
        "fallback_village": None,
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-003",
        "name": "Canal Park",
        "category": "Park",
        "subtype": "Historic Park",
        "designation": "",
        "status": "Active",
        "ownership": "Paulding County Park District",
        "governance": "Paulding County Park District",
        "partner_agencies": "Buckeye Trail Association; North Country Trail Association",
        "coordination": "BTA maintains trail section through park",
        "description": (
            "Canal Park is located at the historic junction of the Miami-Erie Canal and the Wabash-Erie "
            "Canal (Junction, Ohio), on St. Rt. 111. A historical marker marks the canal junction site. "
            "The park is a primary access point for the Buckeye Trail and North Country National Scenic "
            "Trail. Eagle Scout footbridge replaced in 2023."
        ),
        "location": "St. Rt. 111, near Junction, Paulding County, Ohio",
        "acres": "",
        "counties": "Paulding",
        "municipality_override": "",
        "features": "Historic Canal Segment; Historic Marker; Bridge; Hiking Trail",
        "notes": (
            "Postal address city is Defiance but actual location is Paulding County at Junction. "
            "BT Defiance Section begins here (Point 1). Canal Park Trailhead AP = PAU-AP-001."
        ),
        "url_primary": "https://pauldingohparks.com/canal-park/",
        "urls": "",
        "parent_site_id": "",
        "nominatim_queries": [
            "15872 Road 153 Junction Ohio",
            "Canal Park Junction Ohio Paulding County",
            "Junction Ohio 45840",
        ],
        "fallback_village": "Junction",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-004",
        "name": "Cecil Bridge Park",
        "category": "Park",
        "subtype": "Waterfront Park",
        "designation": "",
        "status": "Active",
        "ownership": "Paulding County Park District",
        "governance": "Paulding County Park District",
        "partner_agencies": "Toledo Metroparks",
        "coordination": "",
        "description": (
            "Cecil Bridge Park is located on Road 105 at the Cecil Bridge along the Maumee River "
            "in the Cecil area of Paulding County. A popular launch point for paddlers on the Maumee "
            "River Water Trail between Cecil and Defiance. Features river access, kayaking, canoeing, "
            "boating, fishing, and picnicking."
        ),
        "location": "Road 105 at the Cecil Bridge, Cecil area, Paulding County, Ohio",
        "acres": "",
        "counties": "Paulding",
        "municipality_override": "",
        "features": "Watercraft Access; Fishing Area; Picnic Area",
        "notes": "Maumee River Water Trail access point — see PAU-AP-002.",
        "url_primary": "https://pauldingohparks.com/",
        "urls": "",
        "parent_site_id": "",
        "nominatim_queries": [
            "Cecil Bridge Road 105 Paulding County Ohio",
            "Cecil Bridge Park Cecil Ohio",
        ],
        "fallback_village": "Cecil",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-005",
        "name": "Five Span Park",
        "category": "Park",
        "subtype": "Waterfront Park",
        "designation": "",
        "status": "Active",
        "ownership": "Paulding County Park District",
        "governance": "Paulding County Park District",
        "partner_agencies": "",
        "coordination": "",
        "description": (
            "Five Span Park is the most utilized Paulding County Park District park. Located on the "
            "Auglaize River at the junction of State Routes 111 and 637. Named for its distinctive "
            "historic five-span bridge. Features include seasonal floating dock, boat ramp, fishing, "
            "picnic facilities, fire rings, and restrooms."
        ),
        "location": "Junction of SR 111 and SR 637, Auglaize River, Paulding County, Ohio",
        "acres": "",
        "counties": "Paulding",
        "municipality_override": "",
        "features": "Watercraft Access; Historic Bridge; Boat Ramp; Boat Dock; Fishing Area; Picnic Area; Fire Ring; Restrooms",
        "notes": "Postal address (19483 OH-637, Defiance 43512) uses Defiance city; actual location Paulding County.",
        "url_primary": "https://pauldingohparks.com/",
        "urls": "",
        "parent_site_id": "",
        "nominatim_queries": [
            "19483 OH-637 Defiance Ohio 43512",
            "Five Span Park Paulding County Ohio",
            "SR 111 SR 637 Auglaize River Paulding County Ohio",
        ],
        "fallback_village": "Junction",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-006",
        "name": "Flat Rock Trail Park",
        "category": "Park",
        "subtype": "Greenspace",
        "designation": "",
        "status": "Active",
        "ownership": "Paulding County Park District",
        "governance": "Paulding County Park District",
        "partner_agencies": "",
        "coordination": "",
        "description": (
            "Flat Rock Trail Park was obtained by the Paulding County Park District from the Paulding "
            "County Commissioners on July 26, 2021. Located on the east end of Johnson Road (12600 Rd. 119) "
            "along the Flat Rock Creek corridor. Includes improved parking, primitive campsites with fire "
            "rings, and hiking access."
        ),
        "location": "12600 Rd. 119, Paulding, Ohio",
        "acres": "",
        "counties": "Paulding",
        "municipality_override": "",
        "features": "Camping; Fire Ring; Hiking Trail",
        "notes": "Park active but developing as of 2026-04-07. Adjacent to Flat Rock Creek Nature Preserve (ACRES).",
        "url_primary": "https://pauldingohparks.com/flat-rock-trail-park/",
        "urls": "",
        "parent_site_id": "",
        "nominatim_queries": [
            "12600 Road 119 Paulding Ohio",
            "Flat Rock Trail Park Paulding County Ohio",
        ],
        "fallback_village": "Paulding",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-007",
        "name": "New Rochester Park",
        "category": "Park",
        "subtype": "Historic Park",
        "designation": "",
        "status": "Active",
        "ownership": "Paulding County Park District",
        "governance": "Paulding County Park District",
        "partner_agencies": "",
        "coordination": "",
        "description": (
            "New Rochester Park is located on the Maumee River at 11885 Rd. 424, Cecil, Ohio. Rests "
            "on the historic site of New Rochester, the first county seat of Paulding County. Dedicated "
            "as the first Paulding County park on Labor Day 1935. Eagle viewing area on the Maumee River "
            "bank where a pair of bald eagles has nested."
        ),
        "location": "11885 Rd. 424, Cecil, Ohio 45821",
        "acres": "",
        "counties": "Paulding",
        "municipality_override": "",
        "features": "Watercraft Access; Wildlife Observation Area; Historic Marker; Picnic Area",
        "notes": "Also known as Rochester Park. PCPD website slug: /new-rochester/. Returned to PCPD in 2016 after ODOT use.",
        "url_primary": "https://pauldingohparks.com/new-rochester/",
        "urls": "",
        "parent_site_id": "",
        "nominatim_queries": [
            "11885 Road 424 Cecil Ohio 45821",
            "New Rochester Park Cecil Ohio Paulding County",
        ],
        "fallback_village": "Cecil",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-008",
        "name": "Fort Brown Park",
        "category": "Park",
        "subtype": "Historic Park",
        "designation": "",
        "status": "Active",
        "ownership": "Paulding County Park District",
        "governance": "Paulding County Park District",
        "partner_agencies": "",
        "coordination": "",
        "description": (
            "Fort Brown Park is located at the confluence of the Big Auglaize and Little Auglaize Rivers, "
            "one mile south of Charloe on Road 171 (9597 Rd. 171, Oakwood). PCPD accepted maintenance "
            "responsibility in 2019. Features an 1812-era monument marking Fort Brown, built by General "
            "William Henry Harrison. Future small craft boat launch planned."
        ),
        "location": "9597 Rd. 171, Oakwood, Ohio",
        "acres": "",
        "counties": "Paulding",
        "municipality_override": "",
        "features": "Watercraft Access; Fishing Area; Historic Marker",
        "notes": "Named for Colonel Brown who commanded stockade. Monument erected 1953. Future boat launch planned.",
        "url_primary": "https://pauldingohparks.com/fort-brown-park/",
        "urls": "",
        "parent_site_id": "",
        "nominatim_queries": [
            "9597 Road 171 Oakwood Ohio",
            "Fort Brown Park Paulding County Ohio",
        ],
        "fallback_village": "Oakwood",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-009",
        "name": "Guilda H. Culler Memorial Park",
        "category": "Park",
        "subtype": "Greenspace",
        "designation": "",
        "status": "Under Development",
        "ownership": "Paulding County Park District",
        "governance": "Paulding County Park District",
        "partner_agencies": "",
        "coordination": "",
        "description": (
            "Guilda H. Culler Memorial Park is a developing Paulding County Park District park on land "
            "donated by Gary and Linda Mabis. Named in memory of Guilda H. Culler. In early development stages."
        ),
        "location": "Paulding County, Ohio",
        "acres": "",
        "counties": "Paulding",
        "municipality_override": "",
        "features": "",
        "notes": "Address and GPS unknown as of 2026-04-07. HELD pending GPS acquisition.",
        "url_primary": "https://pauldingohparks.com/",
        "urls": "",
        "parent_site_id": "",
        "nominatim_queries": [],
        "fallback_village": None,
        "held": True,
        "held_reason": "gps_missing",
    },
    {
        "record_id": "PAU-S-010",
        "name": "Black Swamp Nature Center",
        "category": "Natural Area",
        "subtype": "Wetland",
        "designation": "",
        "status": "Active",
        "ownership": "Paulding County Commissioners",
        "governance": "Paulding Soil & Water Conservation District",
        "partner_agencies": "Paulding County Commissioners; Paulding SWCD",
        "coordination": "",
        "description": (
            "Black Swamp Nature Center (BSNC) is a 51-acre county-owned natural area and nature center "
            "facility managed by the Paulding SWCD. Includes approximately 24 acres of woodland, 14 acres "
            "of wetlands, and 6 acres of meadow along Flat Rock Creek. Features a boat launch on Flat Rock "
            "Creek, trails along three ponds, the former Sugar Beet dam site, a nature center building, "
            "and parking. Formerly ODNR Paulding Ponds Wildlife Area, transferred to county in 1994."
        ),
        "location": "753 Fairground Drive, Paulding, Ohio 45879",
        "acres": "51",
        "counties": "Paulding",
        "municipality_override": "Paulding",
        "features": "Wetland; Meadow; Watercraft Access; Hiking Trail; Pond; Dam; Nature Center; Picnic Area; Parking Lot",
        "notes": (
            "Also addressed as 451 McDonald Pike. Resolves baseline seeds: Paulding Ponds Wildlife Area (#10) "
            "and probable identity match for Flatrock Creek Access (#9). "
            "Paulding County Trails Project Phase 1 will connect BSNC to Lela McGuire-Jeffery Park (2027-2028)."
        ),
        "url_primary": "https://pauldingswcd.org/black-swamp-nature-preserve/",
        "urls": "https://pauldingswcd.org/; https://pauldingswcd.org/trail-guide-information/",
        "parent_site_id": "",
        "nominatim_queries": [
            "753 Fairground Drive Paulding Ohio 45879",
            "Black Swamp Nature Center Paulding Ohio",
        ],
        "fallback_village": "Paulding",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-011",
        "name": "Riverside Veterans Memorial Park",
        "category": "Park",
        "subtype": "Waterfront Park",
        "designation": "",
        "status": "Active",
        "ownership": "Village of Antwerp",
        "governance": "Village of Antwerp",
        "partner_agencies": "Toledo Metroparks",
        "coordination": "",
        "description": (
            "Riverside Veterans Memorial Park (commonly Riverside Park) is located on East River Street "
            "in Antwerp, Ohio, with approximately 10 acres along the Maumee River. Features a Veterans "
            "Memorial, playground, reservable group pavilion, canoe/kayak launch on the Maumee River "
            "(Water Trail River Mile 99), Boy Scout-developed hiking trail, fishing access, restrooms, "
            "and the Holly Beach Splashpad."
        ),
        "location": "East River Street, Antwerp, Ohio 45813",
        "acres": "10",
        "counties": "Paulding",
        "municipality_override": "Antwerp",
        "features": "Monument; Playground; Pavilion; Grill; Watercraft Access; Hiking Trail; Fishing Area; Restrooms; Spray Park; Old-Growth Stand",
        "notes": "Maumee River Water Trail access at River Mile 99. Holly Beach Splashpad opened 2022. See PAU-AP-003.",
        "url_primary": "https://villageofantwerp.com/our-parks/",
        "urls": "https://villageofantwerp.com/canoe-and-kayak-launch-at-riverside-park/",
        "parent_site_id": "",
        "nominatim_queries": [
            "East River Street Antwerp Ohio 45813",
            "Riverside Park Antwerp Ohio",
        ],
        "fallback_village": "Antwerp",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-012",
        "name": "Lela McGuire-Jeffery Park",
        "category": "Recreation Facility",
        "subtype": "Sports Complex",
        "designation": "",
        "status": "Active",
        "ownership": "Village of Paulding",
        "governance": "Village of Paulding",
        "partner_agencies": "Paulding Ball Association",
        "coordination": "",
        "description": (
            "Lela McGuire-Jeffery Park is a ball sports complex in the Village of Paulding opened May 14, "
            "2011. Named via bequest from Lela McGuire Jeffery, developed by the Paulding Ball Association. "
            "Features four ball diamonds (one lighted), concession stand, restrooms, and handicap accessible "
            "facilities. Future trail connection to Black Swamp Nature Center planned (2027-2028)."
        ),
        "location": "Village of Paulding, Ohio 45879",
        "acres": "",
        "counties": "Paulding",
        "municipality_override": "Paulding",
        "features": "Ball Diamond; ADA Accessible; Restrooms",
        "notes": "Opened May 14, 2011. Paulding County Trails Project Phase 1 connection to BSNC planned 2027-2028.",
        "url_primary": "https://www.villageofpaulding.com/parks-recreation",
        "urls": "",
        "parent_site_id": "",
        "nominatim_queries": [
            "Lela McGuire-Jeffery Park Paulding Ohio",
            "Paulding Ball Complex Paulding Ohio",
        ],
        "fallback_village": "Paulding",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-013",
        "name": "Herb Monroe Community Park",
        "category": "Park",
        "subtype": "Neighborhood Park",
        "designation": "",
        "status": "Active",
        "ownership": "Village of Paulding",
        "governance": "Village of Paulding",
        "partner_agencies": "",
        "coordination": "",
        "description": "Herb Monroe Community Park is located at 122 E. Jackson St. in the Village of Paulding. Features Freedom Station, an 11,000 sq. ft. community playground.",
        "location": "122 E. Jackson St., Paulding, Ohio 45879",
        "acres": "",
        "counties": "Paulding",
        "municipality_override": "Paulding",
        "features": "Playground",
        "notes": "Also known as Freedom Station Park.",
        "url_primary": "https://www.villageofpaulding.com/parks-recreation",
        "urls": "",
        "parent_site_id": "",
        "nominatim_queries": [
            "122 E Jackson St Paulding Ohio 45879",
            "Herb Monroe Community Park Paulding Ohio",
        ],
        "fallback_village": "Paulding",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-014",
        "name": "Paulding Water Park",
        "category": "Recreation Facility",
        "subtype": "Swimming Pool",
        "designation": "",
        "status": "Seasonal",
        "ownership": "Village of Paulding",
        "governance": "Village of Paulding",
        "partner_agencies": "",
        "coordination": "",
        "description": (
            "Paulding Water Park is an aquatic recreation facility in the Village of Paulding, completed "
            "June 2001. Features a zero-entry swimming pool, water slide, baby pool, water features, "
            "shade umbrellas, and lounge chairs."
        ),
        "location": "Village of Paulding, Ohio 45879",
        "acres": "",
        "counties": "Paulding",
        "municipality_override": "Paulding",
        "features": "Swimming Pool; Waterslide; Spray Park",
        "notes": "Completed June 2001. May be same facility as Paulding Municipal Pool.",
        "url_primary": "https://www.villageofpaulding.com/pool",
        "urls": "https://www.villageofpaulding.com/parks-recreation",
        "parent_site_id": "",
        "nominatim_queries": [
            "Paulding Water Park Paulding Ohio",
            "Paulding Municipal Pool Paulding Ohio",
        ],
        "fallback_village": "Paulding",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-015",
        "name": "Paulding Skate Park",
        "category": "Recreation Facility",
        "subtype": "Skate Park",
        "designation": "",
        "status": "Active",
        "ownership": "Village of Paulding",
        "governance": "Village of Paulding",
        "partner_agencies": "",
        "coordination": "",
        "description": "Paulding Skate Park opened in October 2005 in the Village of Paulding.",
        "location": "Village of Paulding, Ohio 45879",
        "acres": "",
        "counties": "Paulding",
        "municipality_override": "Paulding",
        "features": "Skate Park",
        "notes": "Opened October 2005.",
        "url_primary": "https://www.villageofpaulding.com/parks-recreation",
        "urls": "",
        "parent_site_id": "",
        "nominatim_queries": [
            "Paulding Skate Park Paulding Ohio",
        ],
        "fallback_village": "Paulding",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-016",
        "name": "Reservoir Park",
        "category": "Park",
        "subtype": "",
        "designation": "",
        "status": "No Public Entry",
        "ownership": "Village of Paulding",
        "governance": "Village of Paulding",
        "partner_agencies": "",
        "coordination": "",
        "description": (
            "Reservoir Park is a 67-acre water supply reservoir owned and operated by the Village of "
            "Paulding at 901 McDonald Pike. Public access is currently prohibited. Historical recreation "
            "included fishing and boating. Future trail connection from Lela McGuire-Jeffery Park planned "
            "(Paulding County Trails Project Phase 1, 2027-2028)."
        ),
        "location": "901 McDonald Pike, Paulding, Ohio 45879",
        "acres": "67",
        "counties": "Paulding",
        "municipality_override": "Paulding",
        "features": "",
        "notes": "Public access currently prohibited — active water supply infrastructure. Future trail connection planned.",
        "url_primary": "https://www.villageofpaulding.com/parks-recreation",
        "urls": "",
        "parent_site_id": "",
        "nominatim_queries": [
            "901 McDonald Pike Paulding Ohio 45879",
            "Paulding Reservoir Paulding Ohio",
        ],
        "fallback_village": "Paulding",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-017",
        "name": "Payne Community Park",
        "category": "Park",
        "subtype": "Neighborhood Park",
        "designation": "",
        "status": "Active",
        "ownership": "Village of Payne",
        "governance": "Village of Payne",
        "partner_agencies": "",
        "coordination": "",
        "description": (
            "Payne Community Park is a small village park in Payne, Ohio. Features a stocked catch-and-release "
            "fishing pond (no license required), a walking path, and playground equipment. Walking path and "
            "playground funded via ODNR NatureWorks Grant. Available for organized event rental ($50)."
        ),
        "location": "Village of Payne, Ohio 45880",
        "acres": "",
        "counties": "Paulding",
        "municipality_override": "Payne",
        "features": "Pond; Fishing Area; Hiking Trail; Playground; Pavilion",
        "notes": "ODNR NatureWorks Grant funded walking path and playground. Fish from Remlinger Fish Farm, Kalida.",
        "url_primary": "https://www.villageofpayne.com/park/",
        "urls": "",
        "parent_site_id": "",
        "nominatim_queries": [
            "Payne Community Park Payne Ohio",
            "Village of Payne Park Ohio",
        ],
        "fallback_village": "Payne",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-018",
        "name": "Oakwood Community Park",
        "category": "Park",
        "subtype": "Neighborhood Park",
        "designation": "",
        "status": "Active",
        "ownership": "Village of Oakwood",
        "governance": "Village of Oakwood",
        "partner_agencies": "",
        "coordination": "",
        "description": (
            "Oakwood Community Park is the central gathering place for the Village of Oakwood in Paulding "
            "County. Features playground equipment, sports fields, and picnic areas. The Auglaize River is nearby."
        ),
        "location": "Village of Oakwood, Ohio 45873",
        "acres": "",
        "counties": "Paulding",
        "municipality_override": "Oakwood",
        "features": "Playground; Athletic Field; Picnic Area",
        "notes": "Auglaize Canoe & Kayak (private commercial outfitter) operates adjacent — not a natural areas entity.",
        "url_primary": "",
        "urls": "",
        "parent_site_id": "",
        "nominatim_queries": [
            "Oakwood Community Park Oakwood Ohio Paulding County",
            "Village of Oakwood Ohio 45873",
        ],
        "fallback_village": "Oakwood",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-019",
        "name": "Latty Town Park",
        "category": "Park",
        "subtype": "Neighborhood Park",
        "designation": "",
        "status": "Active",
        "ownership": "Village of Latty",
        "governance": "Village of Latty",
        "partner_agencies": "",
        "coordination": "",
        "description": "Latty Town Park is a small community park in the Village of Latty, Paulding County, Ohio.",
        "location": "Village of Latty, Ohio",
        "acres": "",
        "counties": "Paulding",
        "municipality_override": "Latty",
        "features": "",
        "notes": "Minimal information available.",
        "url_primary": "",
        "urls": "",
        "parent_site_id": "",
        "nominatim_queries": [
            "Latty Town Park Latty Ohio",
            "Village of Latty Ohio",
        ],
        "fallback_village": "Latty",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-020",
        "name": "Forder Bridge Conservation Area",
        "category": "Conservation Area",
        "subtype": "Restoration Area",
        "designation": "",
        "status": "Active",
        "ownership": "Black Swamp Conservancy",
        "governance": "Black Swamp Conservancy",
        "partner_agencies": "ODNR",
        "coordination": "H2Ohio wetland and stream restoration project",
        "description": (
            "A 54-acre conservation property along the Maumee River in Paulding County purchased by "
            "Black Swamp Conservancy in 2016. Former agricultural land restored to native floodplain habitat. "
            "H2Ohio project installed approximately 4 acres of wetland restoration and repaired two on-site "
            "streams, preventing approximately 160 lbs phosphorus and 645 lbs nitrogen annually from entering "
            "the Maumee River. Walk-in access from designated parking lot. Official Maumee River Water Trail "
            "access point at Forder Bridge. No camping, no motor vehicles."
        ),
        "location": "County Road 73, Forder Bridge, Paulding County, Ohio",
        "acres": "54",
        "counties": "Paulding",
        "municipality_override": "",
        "features": "Habitat Restoration Area; Wetland Restoration; Watercraft Access; Parking Lot",
        "notes": (
            "Distinct parcel from Forrest Woods SNP (PAU-S-002), located just south on County Road 73. "
            "BSC's Forder Bridge/Forrest Woods corridor totals ~391 protected acres. Walk-in only; no vehicles. "
            "Maumee River Water Trail access point — see PAU-AP-004."
        ),
        "url_primary": "https://blackswamp.org/",
        "urls": "https://www.chronolog.io/site/BSC110",
        "parent_site_id": "",
        "nominatim_queries": [
            "Forder Bridge County Road 73 Paulding County Ohio",
            "County Road 73 Paulding County Ohio",
        ],
        "fallback_village": None,
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-S-021",
        "name": "Flat Rock Creek Nature Preserve",
        "category": "Nature Preserve",
        "subtype": "Private Nature Preserve",
        "designation": "",
        "status": "No Public Entry",
        "ownership": "ACRES Land Trust",
        "governance": "ACRES Land Trust",
        "partner_agencies": "",
        "coordination": "",
        "description": (
            "A nature preserve owned and managed by ACRES Land Trust in Paulding County, Ohio, approximately "
            "4 miles east of Payne. Features upland and floodplain forests along Flat Rock Creek. Closed to "
            "public access per ACRES Land Trust closed preserves list."
        ),
        "location": "Approximately 4 miles east of Payne, Ohio, Paulding County",
        "acres": "",
        "counties": "Paulding",
        "municipality_override": "",
        "features": "Upland Forest; Floodplain Forest",
        "notes": "CLOSED to public access (ACRES closed preserves). No public trails or visitation. HELD pending GPS.",
        "url_primary": "https://acreslandtrust.org/closedpreserve/closed-flat-rock-creek/",
        "urls": "",
        "parent_site_id": "",
        "nominatim_queries": [],
        "fallback_village": None,
        "held": True,
        "held_reason": "gps_missing",
    },
    {
        "record_id": "PAU-S-022",
        "name": "Thorn Bottom Hunting Preserve",
        "category": "Hunting Area",
        "subtype": "",
        "designation": "",
        "status": "Seasonal",
        "ownership": "Private",
        "governance": "Private",
        "partner_agencies": "",
        "coordination": "",
        "description": (
            "A 652-acre private fee-access hunting preserve in Paulding County, Ohio, on County Road 60 "
            "in Grover Hill. Opened in 1996 by Brad Dysinger. Features wetlands, brush piles, oxbows, "
            "woods, and food plots maintained for hunting. Pheasant hunting operation. Season runs "
            "October 1 through March 15 (closed Christmas and Ohio deer gun week)."
        ),
        "location": "County Road 60, Grover Hill, Paulding County, Ohio",
        "acres": "652",
        "counties": "Paulding",
        "municipality_override": "Grover Hill",
        "features": "Wetland; Hunting Area",
        "notes": "Private hunting preserve with fee-based seasonal access (Oct 1 – Mar 15). Significant Black Swamp remnant habitat.",
        "url_primary": "https://thornbottom.com/",
        "urls": "",
        "parent_site_id": "",
        "nominatim_queries": [
            "County Road 60 Grover Hill Paulding County Ohio",
            "Thorn Bottom Hunting Preserve Grover Hill Ohio",
        ],
        "fallback_village": "Grover Hill",
        "held": False,
        "held_reason": "",
    },
]

TRAILS_RAW = [
    {
        "record_id": "PAU-TR-001",
        "name": "Miami and Erie Canal Towpath",
        "alternate_names": "Miami & Erie Canal Towpath; Miami-Erie Canal Towpath Trail",
        "use_type": "Hiking",
        "surface_type": "Mixed",
        "origin_type": "Canal Towpath",
        "length_mi": "105",
        "counties": "Hamilton; Butler; Warren; Montgomery; Miami; Shelby; Auglaize; Allen; Putnam; Paulding",
        "governance": "ODNR",
        "partner_agencies": "Buckeye Trail Association; North Country Trail Association",
        "status": "Active",
        "difficulty": "",
        "accessibility": "",
        "description": (
            "The Miami and Erie Canal Towpath follows the historic towpath of the Miami and Erie Canal "
            "(completed Cincinnati to Toledo 1825-1845). Canal land is State of Ohio (ODNR). In Paulding "
            "County, the towpath forms the physical trail used by the Buckeye Trail Delphos Section (through "
            "southeast county) and continues to Canal Park at Junction — the northern terminus of the Miami "
            "and Erie Canal, historic junction with the Wabash-Erie Canal."
        ),
        "trail_history": "Miami and Erie Canal completed 1845; canal corridor transferred to ODNR mid-1980s.",
        "identity_notes": (
            "Northern terminus at Junction, Paulding County (Canal Park). BT Delphos Section and BT Defiance "
            "Section use this corridor in Paulding County — those trail entities at Tier 7."
        ),
        "notes": "ODNR has Miami & Erie Canal maps including Paulding County segment.",
        "url_primary": "https://ohiodnr.gov/discover-and-learn/safety-conservation/about-ODNR/real-estate/ohio-canal-maps/miami-erie-canal-maps",
        "maps": "",
    },
    {
        "record_id": "PAU-TR-002",
        "name": "Maumee River Water Trail",
        "alternate_names": "Maumee Scenic River Water Trail",
        "use_type": "Water",
        "surface_type": "Water",
        "origin_type": "Other",
        "length_mi": "107",
        "counties": "Paulding; Defiance; Henry; Wood; Lucas",
        "governance": "Toledo Metroparks",
        "partner_agencies": "Toledo Metroparks; ODNR Division of Wildlife; Defiance Soil & Water Conservation District; Black Swamp Conservancy",
        "status": "Active",
        "difficulty": "",
        "accessibility": "",
        "description": (
            "The Maumee River Water Trail is a 107-mile designated water trail along the Maumee River from "
            "the Ohio-Indiana state line to Lake Erie. Passes through Paulding, Defiance, Henry, Wood, and "
            "Lucas counties. In Paulding County, includes the scenic portion of the Maumee River. The trail "
            "has 39 access points total; Paulding County access points include Cecil Bridge Park (PAU-AP-002), "
            "Forder Bridge area (PAU-AP-004), and Riverside Veterans Memorial Park in Antwerp (PAU-AP-003)."
        ),
        "trail_history": "",
        "identity_notes": "Water trail; use_type = Water Trail. Coordination by Toledo Metroparks.",
        "notes": "Trail brochure: metroparkstoledo.com. 39 access points along 107-mile route.",
        "url_primary": "https://metroparkstoledo.com/features-and-rentals/maumee-river-water-trail/",
        "maps": "https://metroparkstoledo.com/media/3621/maumee-waterway-brochure-031318-web.pdf",
    },
    {
        "record_id": "PAU-TR-003",
        "name": "Buckeye Trail — Delphos Section",
        "alternate_names": "BT Delphos Section",
        "use_type": "Hiking",
        "surface_type": "Mixed",
        "origin_type": "Canal Towpath",
        "length_mi": "47",
        "counties": "Paulding; Putnam; Allen; Auglaize",
        "governance": "Buckeye Trail Association",
        "partner_agencies": "ODNR; North Country Trail Association",
        "status": "Active",
        "difficulty": "",
        "accessibility": "",
        "description": (
            "The Buckeye Trail Delphos Section is a 47-mile hiking trail through Auglaize, Allen, Putnam, "
            "and Paulding counties. Follows the Miami and Erie Canal towpath corridor. The Paulding County "
            "portion follows the M&E Canal towpath to Junction, Ohio (Point 1 of Defiance Section). "
            "Includes Viall's Lock Campsite (primitive, no facilities) in Paulding County."
        ),
        "trail_history": "",
        "identity_notes": (
            "Co-routes with Miami and Erie Canal Towpath (PAU-TR-001) through Paulding County. NCT (PAU-TN-001) "
            "also co-routes. BTA is managing org; trail not federally designated as of 2026-04-08."
        ),
        "notes": "If BT receives NST designation, entity may need reclassification. Viall's Lock Campsite → PAU-AP-005.",
        "url_primary": "https://www.buckeyetrail.org/sections/delphos",
        "maps": "",
    },
    {
        "record_id": "PAU-TR-004",
        "name": "Buckeye Trail — Defiance Section",
        "alternate_names": "BT Defiance Section",
        "use_type": "Hiking",
        "surface_type": "Mixed",
        "origin_type": "Canal Towpath",
        "length_mi": "52",
        "counties": "Paulding; Defiance; Williams",
        "governance": "Buckeye Trail Association",
        "partner_agencies": "North Country Trail Association; ODNR",
        "status": "Active",
        "difficulty": "",
        "accessibility": "",
        "description": (
            "The Buckeye Trail Defiance Section is a 52-mile trail beginning at Junction, Ohio (Canal Park, "
            "PAU-S-003) in Paulding County, extending northeast. Both the Buckeye Trail and the North Country "
            "National Scenic Trail (NCT) co-route the full 52 miles of the Defiance Section."
        ),
        "trail_history": "",
        "identity_notes": (
            "Co-routes with NCT (PAU-TN-001) for full 52-mile section. Paulding County portion is the start "
            "(Point 1 at Junction/Canal Park, PAU-S-003). Canal Park Trailhead (PAU-AP-001) is Paulding entry."
        ),
        "notes": "BTA managing org; not federally designated as of 2026-04-08.",
        "url_primary": "https://www.buckeyetrail.org/sections/sections-map.php?section=defiance",
        "maps": "",
    },
]

TRAIL_NETWORKS_RAW = [
    {
        "record_id": "PAU-TN-001",
        "name": "North Country National Scenic Trail",
        "network_type": "National Scenic Trail",
        "status": "Active",
        "ownership": "Federal / NPS",
        "governance": "National Park Service",
        "partner_agencies": "Buckeye Trail Association; North Country Trail Association",
        "counties": "Multi-state",
        "states_included": "NY; PA; OH; MI; WI; MN; ND",
        "length_mi": "4800",
        "member_trail_count": "2",
        "member_trail_ids": "PAU-TR-003; PAU-TR-004",
        "description": (
            "The North Country National Scenic Trail spans approximately 4,800 miles from Crown Point, "
            "New York to Lake Sakakawea State Park, North Dakota. Administered by the National Park Service. "
            "In Ohio, the NCT co-routes almost entirely with the Buckeye Trail (~1,076 miles). In Paulding "
            "County, the NCT follows the Miami and Erie Canal towpath via the Buckeye Trail's Delphos Section "
            "and Defiance Section. Canal Park (PCPD) at Junction is a primary access point."
        ),
        "identity_notes": (
            "Multi-state trail network. Paulding County member trails: BT Delphos Section (PAU-TR-003) and "
            "BT Defiance Section (PAU-TR-004). NCT and BT diverge at River Road (Defiance Section Point 20) "
            "after co-routing 52 miles; NCT continues north, BT continues east."
        ),
        "notes": (
            "Buckeye Trail is NOT federally designated as of 2026-04-08; NPS feasibility study for NST "
            "designation ongoing (expected to conclude 2026). Access points in Paulding County: "
            "(1) Canal Park/Junction (PAU-AP-001); (2) Viall's Lock Campsite (PAU-AP-005, held)."
        ),
        "url_primary": "https://www.nps.gov/noco/index.htm",
        "maps": "https://www.nps.gov/noco/planyourvisit/maps.htm",
    },
]

ACCESS_POINTS_RAW = [
    {
        "record_id": "PAU-AP-001",
        "name": "Canal Park Trailhead",
        "ap_type": "Trailhead",
        "status": "Active",
        "parent_entity_type": "Trail Network",
        "parent_entity_name": "North Country National Scenic Trail",
        "parent_entity_id": "PAU-TN-001",
        "county": "Paulding",
        "address": "St. Rt. 111, near Junction, Paulding County, Ohio",
        "features": "Parking; Trailhead; Historic Site; Historical Marker",
        "identity_notes": (
            "Located at Canal Park (PAU-S-003, PCPD). Serves as BT Defiance Section start (Point 1) "
            "and NCT access point at historic Miami-Erie/Wabash-Erie Canal junction."
        ),
        "notes": "Postal address city is Defiance but actual county is Paulding.",
        "url_primary": "https://pauldingohparks.com/canal-park/",
        "nominatim_queries": [
            "15872 Road 153 Junction Ohio",
            "Canal Park Junction Ohio Paulding County",
        ],
        "fallback_village": "Junction",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-AP-002",
        "name": "Cecil Bridge Water Trail Access",
        "ap_type": "Watercraft Access Point",
        "status": "Active",
        "parent_entity_type": "Trail",
        "parent_entity_name": "Maumee River Water Trail",
        "parent_entity_id": "PAU-TR-002",
        "county": "Paulding",
        "address": "Road 105 at Cecil Bridge, Cecil area, Paulding County, Ohio",
        "features": "Kayak/Canoe Launch; Boat Launch; River Access; Fishing; Picnic Area",
        "identity_notes": "Located at Cecil Bridge Park (PAU-S-004, PCPD). Maumee River Water Trail access point.",
        "notes": "Primary launch for paddlers on scenic Maumee River between Cecil and Defiance.",
        "url_primary": "",
        "nominatim_queries": [
            "Cecil Bridge Road 105 Paulding County Ohio",
        ],
        "fallback_village": "Cecil",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-AP-003",
        "name": "Riverside Park Water Trail Access",
        "ap_type": "Watercraft Access Point",
        "status": "Active",
        "parent_entity_type": "Trail",
        "parent_entity_name": "Maumee River Water Trail",
        "parent_entity_id": "PAU-TR-002",
        "county": "Paulding",
        "address": "East River Street, Antwerp, Ohio 45813",
        "features": "Kayak/Canoe Launch; River Access; Restrooms; Parking",
        "identity_notes": (
            "Located at Riverside Veterans Memorial Park (PAU-S-011, Village of Antwerp). "
            "Official Maumee River Water Trail access point at River Mile 99."
        ),
        "notes": "",
        "url_primary": "https://villageofantwerp.com/canoe-and-kayak-launch-at-riverside-park/",
        "nominatim_queries": [
            "East River Street Antwerp Ohio 45813",
            "Riverside Park Antwerp Ohio",
        ],
        "fallback_village": "Antwerp",
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-AP-004",
        "name": "Forder Bridge Water Trail Access",
        "ap_type": "Watercraft Access Point",
        "status": "Active",
        "parent_entity_type": "Trail",
        "parent_entity_name": "Maumee River Water Trail",
        "parent_entity_id": "PAU-TR-002",
        "county": "Paulding",
        "address": "County Road 73 at Forder Bridge, Paulding County, Ohio",
        "features": "Kayak/Canoe Launch; River Access; Parking",
        "identity_notes": (
            "Located on BSC-owned Forder Bridge Conservation Area (PAU-S-020). Walk-in access only; "
            "park in designated lot. No motor vehicles. No camping. Official Maumee River Water Trail access point."
        ),
        "notes": "Parking lot coordinates may differ from river access point.",
        "url_primary": "",
        "nominatim_queries": [
            "Forder Bridge County Road 73 Paulding County Ohio",
        ],
        "fallback_village": None,
        "held": False,
        "held_reason": "",
    },
    {
        "record_id": "PAU-AP-005",
        "name": "Viall's Lock Campsite",
        "ap_type": "Trailhead",
        "status": "Active",
        "parent_entity_type": "Trail",
        "parent_entity_name": "Buckeye Trail — Delphos Section",
        "parent_entity_id": "PAU-TR-003",
        "county": "Paulding",
        "address": "Road 163, Paulding County, Ohio",
        "features": "Primitive Camping; Trailhead",
        "identity_notes": (
            "Primitive campsite on BT Delphos Section in Paulding County, off Road 163. No facilities. "
            "Co-located with NCT route (PAU-TN-001). Parent: BT Delphos Section (PAU-TR-003)."
        ),
        "notes": "HELD — GPS and exact Road 163 location not found in available sources.",
        "url_primary": "https://www.buckeyetrail.org/sections/delphos",
        "nominatim_queries": [],
        "fallback_village": None,
        "held": True,
        "held_reason": "gps_missing",
    },
]


# ═══════════════════════════════════════════════════════════════════════════
# TSV GENERATION HELPERS
# ═══════════════════════════════════════════════════════════════════════════

def make_tsv_row(fields):
    """Join fields with tabs; validate tab count. Returns TSV row string."""
    row = "\t".join(clean(f) for f in fields)
    tab_count = row.count("\t")
    expected = len(fields) - 1
    if tab_count != expected:
        raise ValueError(f"Tab count mismatch: expected {expected}, got {tab_count}")
    return row

def write_tsv(path, header_fields, data_rows):
    """Write header + data rows to TSV file."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(make_tsv_row(header_fields) + "\n")
        for row in data_rows:
            f.write(make_tsv_row(row) + "\n")
    print(f"  Written: {path} ({len(data_rows)} data rows)")


# ═══════════════════════════════════════════════════════════════════════════
# SCHEMA SQL
# ═══════════════════════════════════════════════════════════════════════════

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS sites (
    site_id         TEXT PRIMARY KEY,
    name            TEXT NOT NULL,
    category        TEXT,
    subtype         TEXT,
    designation     TEXT,
    status          TEXT,
    ownership       TEXT,
    governance      TEXT,
    partner_agencies TEXT,
    coordination    TEXT,
    description     TEXT,
    location        TEXT,
    acres           REAL,
    counties        TEXT,
    municipality    TEXT,
    township        TEXT,
    gps_lat         REAL,
    gps_lon         REAL,
    plus_code       TEXT,
    features        TEXT,
    notes           TEXT,
    url_primary     TEXT,
    urls            TEXT,
    parent_site_id  TEXT,
    created_at      TEXT,
    updated_at      TEXT
);

CREATE TABLE IF NOT EXISTS trails (
    trail_id            TEXT PRIMARY KEY,
    name                TEXT NOT NULL,
    alternate_names     TEXT,
    use_type            TEXT,
    surface_type        TEXT,
    origin_type         TEXT,
    length_mi           REAL,
    counties            TEXT,
    governance          TEXT,
    partner_agencies    TEXT,
    status              TEXT,
    difficulty          TEXT,
    accessibility       TEXT,
    description         TEXT,
    trail_history       TEXT,
    identity_notes      TEXT,
    notes               TEXT,
    url_primary         TEXT,
    maps                TEXT,
    created_at          TEXT,
    updated_at          TEXT
);

CREATE TABLE IF NOT EXISTS trail_networks (
    network_id          TEXT PRIMARY KEY,
    name                TEXT NOT NULL,
    network_type        TEXT,
    status              TEXT,
    ownership           TEXT,
    governance          TEXT,
    partner_agencies    TEXT,
    counties            TEXT,
    states_included     TEXT,
    length_mi           REAL,
    member_trail_count  INTEGER,
    member_trail_ids    TEXT,
    description         TEXT,
    identity_notes      TEXT,
    notes               TEXT,
    url_primary         TEXT,
    maps                TEXT,
    created_at          TEXT,
    updated_at          TEXT
);

CREATE TABLE IF NOT EXISTS site_networks (
    network_id      TEXT PRIMARY KEY,
    name            TEXT NOT NULL,
    network_type    TEXT,
    status          TEXT,
    ownership       TEXT,
    governance      TEXT,
    partner_agencies TEXT,
    counties        TEXT,
    states_included TEXT,
    member_count    INTEGER,
    member_site_ids TEXT,
    description     TEXT,
    identity_notes  TEXT,
    notes           TEXT,
    url_primary     TEXT,
    created_at      TEXT,
    updated_at      TEXT
);

CREATE TABLE IF NOT EXISTS trail_segments (
    segment_id      TEXT PRIMARY KEY,
    parent_trail_id TEXT,
    name            TEXT,
    counties        TEXT,
    governance      TEXT,
    length_mi       REAL,
    surface_type    TEXT,
    segment_type    TEXT,
    status          TEXT,
    difficulty      TEXT,
    accessibility   TEXT,
    description     TEXT,
    identity_notes  TEXT,
    notes           TEXT,
    url_primary     TEXT,
    maps            TEXT,
    geometry        TEXT,
    created_at      TEXT,
    updated_at      TEXT
);

CREATE TABLE IF NOT EXISTS access_points (
    access_point_id     TEXT PRIMARY KEY,
    name                TEXT NOT NULL,
    ap_type             TEXT,
    status              TEXT,
    parent_entity_type  TEXT,
    parent_entity_id    TEXT,
    county              TEXT,
    township            TEXT,
    municipality        TEXT,
    address             TEXT,
    gps_lat             REAL,
    gps_lon             REAL,
    plus_code           TEXT,
    features            TEXT,
    identity_notes      TEXT,
    notes               TEXT,
    url_primary         TEXT,
    created_at          TEXT,
    updated_at          TEXT
);

CREATE TABLE IF NOT EXISTS trail_network_members (
    network_id      TEXT NOT NULL,
    trail_id        TEXT NOT NULL,
    PRIMARY KEY (network_id, trail_id)
);

CREATE TABLE IF NOT EXISTS access_point_parents (
    access_point_id     TEXT NOT NULL,
    parent_entity_type  TEXT NOT NULL,
    parent_entity_id    TEXT NOT NULL,
    PRIMARY KEY (access_point_id, parent_entity_type, parent_entity_id)
);

CREATE TABLE IF NOT EXISTS held_entities (
    held_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id       TEXT NOT NULL,
    entity_type     TEXT NOT NULL,
    name            TEXT,
    reason          TEXT,
    notes           TEXT,
    run_id          TEXT,
    created_at      TEXT
);

CREATE TABLE IF NOT EXISTS run_metadata (
    run_id          TEXT PRIMARY KEY,
    county          TEXT,
    state           TEXT,
    run_date        TEXT,
    entity_counts   TEXT,
    held_counts     TEXT,
    notes           TEXT,
    created_at      TEXT
);
"""


# ═══════════════════════════════════════════════════════════════════════════
# MAIN PIPELINE
# ═══════════════════════════════════════════════════════════════════════════

def run_pipeline(db_path, dry_run):
    print("=" * 70)
    print("PAULDING COUNTY, OHIO — NATURAL AREAS PROJECT PIPELINE")
    print(f"Run ID: {RUN_ID}  |  DB: {db_path}  |  Dry run: {dry_run}")
    print("=" * 70)

    # ── STAGE 4: GPS Acquisition ─────────────────────────────────────────
    print("\n── STAGE 4: GPS ACQUISITION ──")
    sites_normalized = []
    held_sites = []

    for s in SITES_RAW:
        if s["held"]:
            print(f"  {s['record_id']}: HELD ({s['held_reason']}) — skipping GPS")
            held_sites.append(s)
            continue

        lat, lon, method = acquire_gps(
            s["record_id"], s["nominatim_queries"], s.get("fallback_village")
        )

        # If GPS still None and entity is not explicitly held, try harder
        if lat is None:
            print(f"  {s['record_id']}: No GPS obtained — marking as HELD (gps_missing)")
            s["held"] = True
            s["held_reason"] = "gps_missing"
            held_sites.append(s)
            continue

        s["gps_lat"] = lat
        s["gps_lon"] = lon
        s["gps_method"] = method

        # Plus Code
        s["plus_code"] = get_plus_code(lat, lon)

        # GIS township/municipality
        twp, mun = get_gis(lat, lon)
        s["township"] = twp
        # Use override if municipality discovery pre-populated it; GIS fills otherwise
        if s.get("municipality_override"):
            s["municipality"] = s["municipality_override"]
        else:
            s["municipality"] = mun

        sites_normalized.append(s)

    # Access Points GPS
    print("\n── STAGE 4b: GPS ACQUISITION — ACCESS POINTS ──")
    aps_normalized = []
    held_aps = []

    for ap in ACCESS_POINTS_RAW:
        if ap["held"]:
            print(f"  {ap['record_id']}: HELD ({ap['held_reason']}) — skipping GPS")
            held_aps.append(ap)
            continue

        lat, lon, method = acquire_gps(
            ap["record_id"], ap["nominatim_queries"], ap.get("fallback_village")
        )

        if lat is None:
            print(f"  {ap['record_id']}: No GPS obtained — marking as HELD (gps_missing)")
            ap["held"] = True
            ap["held_reason"] = "gps_missing"
            held_aps.append(ap)
            continue

        ap["gps_lat"] = lat
        ap["gps_lon"] = lon
        ap["gps_method"] = method
        ap["plus_code"] = get_plus_code(lat, lon)

        twp, mun = get_gis(lat, lon)
        ap["township"] = twp
        ap["municipality"] = mun

        aps_normalized.append(ap)

    print(f"\n  Sites normalized: {len(sites_normalized)} | Held: {len(held_sites)}")
    print(f"  APs normalized:   {len(aps_normalized)} | Held: {len(held_aps)}")

    # ── STAGE 8: TSV OUTPUT ───────────────────────────────────────────────
    print("\n── STAGE 8: TSV OUTPUT ──")

    # -- Sites TSV (25 fields, 24 tabs) --
    sites_header = [
        "name", "category", "subtype", "designation", "status",
        "ownership", "governance", "partner_agencies", "coordination",
        "description", "location", "acres", "counties",
        "municipality", "township",
        "gps_lat", "gps_lon", "plus_code",
        "features", "notes", "url_primary", "urls",
        "parent_site_id", "created_at", "updated_at"
    ]
    sites_rows = []
    for s in sites_normalized:
        lat_str = f"{s['gps_lat']:.5f}" if s.get("gps_lat") else ""
        lon_str = f"{s['gps_lon']:.5f}" if s.get("gps_lon") else ""
        row = [
            s["name"], s["category"], s["subtype"], s["designation"], s["status"],
            s["ownership"], s["governance"], s["partner_agencies"], s["coordination"],
            s["description"], s["location"],
            str(acres_float(s["acres"])) if acres_float(s["acres"]) else "",
            s["counties"],
            s.get("municipality", ""), s.get("township", ""),
            lat_str, lon_str, s.get("plus_code", ""),
            s["features"], s["notes"], s["url_primary"], s["urls"],
            s["parent_site_id"], NOW, NOW
        ]
        assert len(row) == 25, f"{s['record_id']}: expected 25 fields, got {len(row)}"
        sites_rows.append(row)

    sites_tsv_path = os.path.join(OUTPUT_DIR, "paulding_oh_sites.tsv")
    write_tsv(sites_tsv_path, sites_header, sites_rows)

    # -- Trails TSV (19 fields, 18 tabs) --
    trails_header = [
        "Trail Name", "Alternate Names", "Trail Use Type", "Trail Surface Type",
        "Trail Origin Type", "Total Length (Miles)", "Counties", "Governance",
        "Partner Agencies", "Status", "Difficulty", "Accessibility",
        "Description", "Trail History", "Identity Notes", "Notes",
        "URL", "Maps", "Trail ID"
    ]
    trails_rows = []
    for t in TRAILS_RAW:
        row = [
            t["name"], t["alternate_names"], t["use_type"], t["surface_type"],
            t["origin_type"], t["length_mi"], t["counties"], t["governance"],
            t["partner_agencies"], t["status"], t["difficulty"], t["accessibility"],
            t["description"], t["trail_history"], t["identity_notes"], t["notes"],
            t["url_primary"], t["maps"], t["record_id"]
        ]
        assert len(row) == 19, f"{t['record_id']}: expected 19 fields, got {len(row)}"
        trails_rows.append(row)

    trails_tsv_path = os.path.join(OUTPUT_DIR, "paulding_oh_trails.tsv")
    write_tsv(trails_tsv_path, trails_header, trails_rows)

    # -- Trail Networks TSV (17 fields, 16 tabs) --
    tn_header = [
        "Network Name", "Network Type", "Status", "Ownership", "Governance",
        "Partner Agencies", "Counties", "States Included", "Total Length (Miles)",
        "Member Trail Count", "Member Trail IDs", "Description", "Identity Notes",
        "Notes", "URL", "Maps", "Network ID"
    ]
    tn_rows = []
    for tn in TRAIL_NETWORKS_RAW:
        row = [
            tn["name"], tn["network_type"], tn["status"], tn["ownership"], tn["governance"],
            tn["partner_agencies"], tn["counties"], tn["states_included"], tn["length_mi"],
            tn["member_trail_count"], tn["member_trail_ids"], tn["description"],
            tn["identity_notes"], tn["notes"], tn["url_primary"], tn["maps"], tn["record_id"]
        ]
        assert len(row) == 17, f"{tn['record_id']}: expected 17 fields, got {len(row)}"
        tn_rows.append(row)

    tn_tsv_path = os.path.join(OUTPUT_DIR, "paulding_oh_trail_networks.tsv")
    write_tsv(tn_tsv_path, tn_header, tn_rows)

    # -- Access Points TSV (17 fields, 16 tabs) --
    ap_header = [
        "Access Point Name", "Access Point Type", "Status",
        "Identity Parent Entity Type", "Identity Parent Entity Name",
        "County", "Township", "Municipality", "Address",
        "GPS Lat", "GPS Lon", "Plus Code", "Features",
        "Identity Notes", "Notes", "URL", "Access Point ID"
    ]
    ap_rows = []
    for ap in aps_normalized:
        lat_str = f"{ap['gps_lat']:.5f}" if ap.get("gps_lat") else ""
        lon_str = f"{ap['gps_lon']:.5f}" if ap.get("gps_lon") else ""
        row = [
            ap["name"], ap["ap_type"], ap["status"],
            ap["parent_entity_type"], ap["parent_entity_name"],
            ap["county"], ap.get("township", ""), ap.get("municipality", ""),
            ap["address"],
            lat_str, lon_str, ap.get("plus_code", ""),
            ap["features"], ap["identity_notes"], ap["notes"],
            ap["url_primary"], ap["record_id"]
        ]
        assert len(row) == 17, f"{ap['record_id']}: expected 17 fields, got {len(row)}"
        ap_rows.append(row)

    ap_tsv_path = os.path.join(OUTPUT_DIR, "paulding_oh_access_points.tsv")
    write_tsv(ap_tsv_path, ap_header, ap_rows)

    # Empty TSVs for entity types with no data
    ts_header = [
        "Segment Name", "Parent Trail ID", "Counties", "Governance", "Length (Miles)",
        "Surface Type", "Segment Type", "Status", "Difficulty", "Accessibility",
        "Description", "Identity Notes", "Notes", "URL", "Maps", "Segment ID"
    ]
    ts_tsv_path = os.path.join(OUTPUT_DIR, "paulding_oh_trail_segments.tsv")
    write_tsv(ts_tsv_path, ts_header, [])

    sn_header = [
        "Network Name", "Network Type", "Status", "Ownership", "Governance",
        "Partner Agencies", "Counties", "States Included",
        "Member Count", "Member Site IDs", "Description", "Identity Notes",
        "Notes", "URL", "Network ID"
    ]
    sn_tsv_path = os.path.join(OUTPUT_DIR, "paulding_oh_site_networks.tsv")
    write_tsv(sn_tsv_path, sn_header, [])

    # ── STAGE 9: TSV INTEGRITY CHECK ─────────────────────────────────────
    print("\n── STAGE 9: TSV INTEGRITY CHECK ──")
    integrity_ok = True

    checks = [
        (sites_tsv_path, 25, 24, "Sites"),
        (trails_tsv_path, 19, 18, "Trails"),
        (tn_tsv_path, 17, 16, "Trail Networks"),
        (ap_tsv_path, 17, 16, "Access Points"),
        (ts_tsv_path, 16, 15, "Trail Segments"),
        (sn_tsv_path, 15, 14, "Site Networks"),
    ]

    for tsv_path, expected_fields, expected_tabs, label in checks:
        errors = []
        with open(tsv_path, encoding="utf-8") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            line = line.rstrip("\n")
            tabs = line.count("\t")
            if tabs != expected_tabs:
                errors.append(f"  Row {i+1}: {tabs} tabs (expected {expected_tabs})")
            for field in line.split("\t"):
                if field != field.strip():
                    errors.append(f"  Row {i+1}: field has leading/trailing whitespace")
                    break

        if errors:
            integrity_ok = False
            print(f"  {label}: FAIL ({len(errors)} error(s))")
            for e in errors[:5]:
                print(f"    {e}")
        else:
            print(f"  {label}: OK ({len(lines)-1} data rows, {expected_tabs} tabs/row)")

    if not integrity_ok:
        print("\nINTEGRITY CHECK FAILED — halting upsert.")
        sys.exit(1)

    print("\n  All TSV integrity checks passed.")

    # ── STAGE 7: DATABASE UPSERT ─────────────────────────────────────────
    print(f"\n── STAGE 7: DATABASE UPSERT ({'DRY RUN' if dry_run else 'LIVE'}) ──")

    if not dry_run:
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

    con = sqlite3.connect(":memory:" if dry_run else db_path)
    cur = con.cursor()
    cur.executescript(SCHEMA_SQL)

    def execute(sql, params=()):
        if dry_run:
            preview = sql.strip()[:80].replace("\n", " ")
            print(f"  [DRY-RUN] {preview} ...")
        else:
            cur.execute(sql, params)

    # Upsert Sites
    site_upsert_sql = """
    INSERT OR REPLACE INTO sites
        (site_id, name, category, subtype, designation, status, ownership, governance,
         partner_agencies, coordination, description, location, acres, counties,
         municipality, township, gps_lat, gps_lon, plus_code, features, notes,
         url_primary, urls, parent_site_id, created_at, updated_at)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """
    site_count = 0
    for s in sites_normalized:
        params = (
            s["record_id"], s["name"], s["category"], s["subtype"],
            s["designation"], s["status"], s["ownership"], s["governance"],
            s["partner_agencies"], s["coordination"], s["description"],
            s["location"], acres_float(s["acres"]), s["counties"],
            s.get("municipality", ""), s.get("township", ""),
            s.get("gps_lat"), s.get("gps_lon"), s.get("plus_code", ""),
            s["features"], s["notes"], s["url_primary"], s["urls"],
            s["parent_site_id"], NOW, NOW
        )
        execute(site_upsert_sql, params)
        site_count += 1
    print(f"  Sites upserted: {site_count}")

    # Upsert Trails
    trail_upsert_sql = """
    INSERT OR REPLACE INTO trails
        (trail_id, name, alternate_names, use_type, surface_type, origin_type,
         length_mi, counties, governance, partner_agencies, status, difficulty,
         accessibility, description, trail_history, identity_notes, notes,
         url_primary, maps, created_at, updated_at)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """
    for t in TRAILS_RAW:
        params = (
            t["record_id"], t["name"], t["alternate_names"], t["use_type"],
            t["surface_type"], t["origin_type"],
            float(t["length_mi"]) if t["length_mi"] else None,
            t["counties"], t["governance"], t["partner_agencies"], t["status"],
            t["difficulty"], t["accessibility"], t["description"],
            t["trail_history"], t["identity_notes"], t["notes"],
            t["url_primary"], t["maps"], NOW, NOW
        )
        execute(trail_upsert_sql, params)
    print(f"  Trails upserted: {len(TRAILS_RAW)}")

    # Upsert Trail Networks
    tn_upsert_sql = """
    INSERT OR REPLACE INTO trail_networks
        (network_id, name, network_type, status, ownership, governance, partner_agencies,
         counties, states_included, length_mi, member_trail_count, member_trail_ids,
         description, identity_notes, notes, url_primary, maps, created_at, updated_at)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """
    for tn in TRAIL_NETWORKS_RAW:
        params = (
            tn["record_id"], tn["name"], tn["network_type"], tn["status"],
            tn["ownership"], tn["governance"], tn["partner_agencies"],
            tn["counties"], tn["states_included"],
            float(tn["length_mi"]) if tn["length_mi"] else None,
            int(tn["member_trail_count"]) if tn["member_trail_count"] else None,
            tn["member_trail_ids"],
            tn["description"], tn["identity_notes"], tn["notes"],
            tn["url_primary"], tn["maps"], NOW, NOW
        )
        execute(tn_upsert_sql, params)
    print(f"  Trail networks upserted: {len(TRAIL_NETWORKS_RAW)}")

    # Upsert Access Points
    ap_upsert_sql = """
    INSERT OR REPLACE INTO access_points
        (access_point_id, name, ap_type, status, parent_entity_type, parent_entity_id,
         county, township, municipality, address, gps_lat, gps_lon, plus_code,
         features, identity_notes, notes, url_primary, created_at, updated_at)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """
    for ap in aps_normalized:
        params = (
            ap["record_id"], ap["name"], ap["ap_type"], ap["status"],
            ap["parent_entity_type"], ap["parent_entity_id"],
            ap["county"], ap.get("township", ""), ap.get("municipality", ""),
            ap["address"], ap.get("gps_lat"), ap.get("gps_lon"), ap.get("plus_code", ""),
            ap["features"], ap["identity_notes"], ap["notes"],
            ap["url_primary"], NOW, NOW
        )
        execute(ap_upsert_sql, params)
    print(f"  Access points upserted: {len(aps_normalized)}")

    # Trail network members
    tn_member_sql = """
    INSERT OR IGNORE INTO trail_network_members (network_id, trail_id) VALUES (?,?)
    """
    execute(tn_member_sql, ("PAU-TN-001", "PAU-TR-003"))
    execute(tn_member_sql, ("PAU-TN-001", "PAU-TR-004"))

    # AP parent relationships
    ap_parent_sql = """
    INSERT OR IGNORE INTO access_point_parents
        (access_point_id, parent_entity_type, parent_entity_id)
    VALUES (?,?,?)
    """
    for ap in aps_normalized:
        execute(ap_parent_sql, (ap["record_id"], ap["parent_entity_type"], ap["parent_entity_id"]))

    # Write held entities
    # Schema: record_id, entity_type, name, county, hold_reason, hold_detail, run_id, created_at
    held_sql = """
    INSERT INTO held_entities (record_id, entity_type, name, county, hold_reason, hold_detail, run_id, created_at)
    VALUES (?,?,?,?,?,?,?,?)
    """
    for s in held_sites:
        execute(held_sql, (
            s["record_id"], "Site", s["name"], COUNTY,
            s["held_reason"], s.get("notes", ""), RUN_ID, NOW
        ))
    for ap in held_aps:
        execute(held_sql, (
            ap["record_id"], "Access Point", ap["name"], COUNTY,
            ap["held_reason"], ap.get("notes", ""), RUN_ID, NOW
        ))
    held_total = len(held_sites) + len(held_aps)
    print(f"  Held entities written: {held_total}")

    # Run metadata (schema: run_id, county, state, run_date, records_input, normalized, held, rejected, notes, created_at)
    total_input = len(SITES_RAW) + len(TRAILS_RAW) + len(TRAIL_NETWORKS_RAW) + len(ACCESS_POINTS_RAW)
    total_normalized = len(sites_normalized) + len(TRAILS_RAW) + len(TRAIL_NETWORKS_RAW) + len(aps_normalized)
    total_held = held_total
    execute(
        """INSERT OR REPLACE INTO run_metadata
           (run_id, county, state, run_date, records_input, normalized, held, rejected, notes, created_at)
           VALUES (?,?,?,?,?,?,?,?,?,?)""",
        (RUN_ID, COUNTY, STATE, RUN_DATE, total_input, total_normalized, total_held, 0,
         "Full pipeline run: GPS acquisition (Nominatim+centroids+hardcoded), normalization, TSV output, integrity check, upsert.",
         NOW)
    )

    if not dry_run:
        con.commit()
    con.close()

    # ── FINAL SUMMARY ────────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("PIPELINE COMPLETE — PAULDING COUNTY, OHIO")
    print("=" * 70)
    print(f"  Sites upserted:         {len(sites_normalized)}")
    print(f"  Trails upserted:        {len(TRAILS_RAW)}")
    print(f"  Trail networks upserted:{len(TRAIL_NETWORKS_RAW)}")
    print(f"  Access points upserted: {len(aps_normalized)}")
    print(f"  Trail segments:         0")
    print(f"  Site networks:          0")
    print(f"  Held (sites):           {len(held_sites)}")
    print(f"  Held (access points):   {len(held_aps)}")
    print(f"\n  TSV output directory: {OUTPUT_DIR}")
    print(f"  Database: {db_path}")
    if dry_run:
        print("\n  [DRY RUN — no writes to database]")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Paulding County, Ohio — Natural Areas Project Pipeline"
    )
    parser.add_argument(
        "--db", default=DEFAULT_DB,
        help=f"Path to SQLite database (default: {DEFAULT_DB})"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print SQL without executing; TSVs are still written"
    )
    args = parser.parse_args()
    run_pipeline(db_path=args.db, dry_run=args.dry_run)
