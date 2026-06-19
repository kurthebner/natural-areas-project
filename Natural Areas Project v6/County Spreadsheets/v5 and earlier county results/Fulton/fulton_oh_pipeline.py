# =============================================================================
# SUPERSEDED — IMP-091 (2026-05-04)
# This monolithic pipeline script has been replaced by the parameterised model:
#   utilities/na_run_county.py + County_Spreadsheets/{County}/{county}_pipeline_config.json
# Do not use for new county runs. Kept for reference only.
# =============================================================================
"""
Fulton County, Ohio — Natural Areas Pipeline v5.2
Resolution → Normalization → GPS → TSV Output → Vocabulary Gate → Integrity Check → DB Upsert
Run date: 2026-04-13
"""

import sys, os, csv, sqlite3, json, re
from datetime import datetime, timezone

NAP_ROOT = "/sessions/wonderful-confident-franklin/mnt/Natural Areas Project v5"
sys.path.insert(0, os.path.join(NAP_ROOT, "utilities"))
from na_plus_code import encode_plus_code

OUTPUT_DIR = os.path.join(NAP_ROOT, "County_Spreadsheets", "Fulton")
PROD_DB    = os.path.join(NAP_ROOT, "NASqlite", "natural_areas_v5.db")
RUN_TS     = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
RUN_ID     = "fulton_oh_2026_04_13"
PREFIX     = "FUL"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─────────────────────────────────────────────────────────────
# VOCABULARY CONSTANTS
# ─────────────────────────────────────────────────────────────
SITE_CATEGORIES = {
    "Campground","Cemetery","Community Garden","Conservation Area","Cultural Facility",
    "Curated Biological Site","Fishing Area","Historic Site","Hunting Area","Memorial",
    "Museum","Natural Area","Nature Preserve","Open Space","Park","Recreation Facility",
    "Water Site","Wildlife Area",
}
PARK_SUBTYPES          = {"Greenspace","Neighborhood Park","Linear Park","Dog Park",
                           "Playground Park","Sports Park","Waterfront Park","Civic Park","Historic Park"}
NATURE_PRESERVE_SUBS   = {"State Nature Preserve","Private Nature Preserve"}
WILDLIFE_AREA_SUBS     = {"State Wildlife Area","Federal Wildlife Area","Waterfowl Area",
                           "Migratory Bird Area","Wetland Management Area"}
WATER_SITE_SUBS        = {"Lake","Pond","Reservoir","River","Harbor","Marina",
                           "Boat Launch Area","Fishing Lake","Retention Pond"}
CAMPGROUND_SUBS        = {"Tent","RV","Primitive","Group","Cabin"}
RECREATION_FACILITY_SUBS = {"Sports Complex","Athletic Field","Skate Park","Swimming Pool",
                              "Recreation Center","Tennis Complex","Pickleball Complex",
                              "Golf Course","Disc Golf Course","Ice Rink","BMX Track","Pump Track"}
MUSEUM_SUBS            = {"Art Museum","Natural History Museum","History Museum",
                           "Science Museum","Children's Museum","Living Museum"}

TRAIL_USE_TYPES    = {"Multi-Use","Hiking","Bridle","Water","Bicycling","Mountain Bike",
                       "BMX","Pump Track","Snowmobile","Cross Country Ski","Other"}
TRAIL_SURFACE_TYPES = {"Paved","Crushed Stone","Gravel","Natural Surface","Boardwalk","Water","Mixed","Other"}
TRAIL_ORIGIN_TYPES  = {"Rail Trail","Canal Towpath","Historic Route","Greenway Corridor",
                        "Purpose-Built","Utility Corridor","Roadside Corridor","Other"}
TRAIL_STATUS_VALUES = {"Active","Planned","Under Construction","Gap","Closed"}

AP_TYPES    = {"Trailhead","Parking Area","Boat Ramp","Boat Launch","Watercraft Access Point",
               "River Access","Fishing Access","Hazard Portage","Bicycle Access",
               "Snowmobile Access","Cross Country Ski Access","Equestrian Access",
               "Roadside Pull-Off","Pedestrian Entrance","Vehicle Entrance",
               "Transit Access","Ferry Access","Shuttle Access","Administrative Access","Other"}
AP_STATUSES = {"Active","Closed","Seasonal","Restricted"}

# ─────────────────────────────────────────────────────────────
# GPS TABLE  (confirmed from authoritative sources)
# ─────────────────────────────────────────────────────────────
GPS = {
    # Tier 2 — State
    "Goll Woods State Nature Preserve":  (41.554461, -84.361370, "HIGH"),
    "Harrison Lake State Park":          (41.64361,  -84.37222,  "HIGH"),
    "Maumee State Forest":               (41.52056,  -83.90194,  "MED"),   # HELD
    "Tiffin River Wildlife Area":        (41.60556,  -84.31167,  "MED"),
    "Fulton Pond Wildlife Area":         (41.5972,   -83.9278,   "MED"),
    # Tier 3 — District
    # Oak Openings Corridor: no GPS (HELD, Fulton parcels uncharted)
    # Tier 6 — Wauseon
    "Biddle Park":                       (41.5581,   -84.1428,   "MED"),  # 900 N Glenwood approx
    "Depot Park":                        (41.5448,   -84.1387,   "LOW"),  # downtown Wauseon approx
    "Rotary Park & Goodwin Preserve":    (41.5462,   -84.1440,   "LOW"),  # Wood St area
    "Homecoming Park":                   (41.5411,   -84.1507,   "HIGH"), # 715 Lawrence Ave confirmed
    "Memorial Park (Wauseon)":           (41.5492,   -84.1449,   "HIGH"), # 202 Madison St confirmed
    "Reighard Park":                     (41.5528,   -84.1314,   "HIGH"), # 615 Oak St confirmed
    "South Park (Wauseon)":              (41.5437,   -84.1401,   "HIGH"), # 405 E Park St confirmed
    "Wabash Park (Wauseon)":             (41.5460,   -84.1395,   "LOW"),  # approx central Wauseon
    "Harmon Park":                       (41.5500,   -84.1385,   "LOW"),  # approx
    # Tier 6 — Archbold
    "Lion's Park":                       (41.5227,   -84.2989,   "LOW"),  # E Holland St approx
    "Memorial Park (Archbold)":          (41.5143,   -84.3025,   "LOW"),  # south side approx
    "North Pointe Park":                 (41.5206,   -84.3050,   "LOW"),  # St Anne & Primrose approx
    "Ruihley Park":                      (41.5239,   -84.3122,   "HIGH"), # 401 W Holland St confirmed
    "South Street Park":                 (41.5163,   -84.3080,   "LOW"),  # South & West Sts approx
    "Woodland Park":                     (41.5168,   -84.2950,   "LOW"),  # SR 66 Archbold east approx
    # Tier 6 — Delta
    "Delta Park":                        (41.5765,   -84.0138,   "LOW"),  # Delta central approx
    "Wildwood Park (Delta)":             (41.5779,   -84.0152,   "MED"),  # Adrian St / Longnecker Grove GNIS
    # Tier 6 — Fayette (unverified — no GPS assigned)
    # Tier 6 — Lyons
    "Dunbar-Ingall Park":                (41.6998,   -84.0742,   "LOW"),  # W Morenci St approx
    # Tier 6 — Metamora
    "Metamora Community Park":           (41.5585,   -84.0776,   "LOW"),  # Metamora village center approx
    # Tier 6 — Swanton
    "Pilliod Park":                      (41.5940,   -83.8985,   "LOW"),  # adj library approx
    "Rotary Park (Swanton)":             (41.5939,   -83.8980,   "LOW"),  # adj Pilliod approx
    "Swanton Memorial Park":             (41.5924,   -83.8968,   "LOW"),  # Swanton approx
    # Tier 7 — Conservancy
    "Pettisville Community Park":        (41.5316,   -84.2195,   "HIGH"), # 18405 CR DE confirmed
    # Tier 8 — Private
    "Sauder Village":                    (41.542968, -84.30179,  "HIGH"), # baseline GPS
    "Bracy Gold Bison Ranch":            (41.6379,   -83.9316,   "HIGH"), # baseline GPS
    "4-H Camp Palmer":                   (41.6440,   -84.3720,   "LOW"),  # adj Harrison Lake SP approx
    "Robert Fulton Agriculture Center":  (41.5676,   -84.1425,   "HIGH"), # baseline GPS
    # Trails
    "Cannonball Trail (Wauseon)":        (41.5480,   -84.1410,   "MED"),  # from identity notes
}

def get_gps(name):
    entry = GPS.get(name)
    if entry:
        lat, lon, conf = entry
        return round(lat, 6), round(lon, 6), encode_plus_code(lat, lon), conf
    return None, None, "", "NONE"

def fmt_gps(v):
    if v is None: return ""
    return str(round(v, 6)).rstrip("0").rstrip(".")

def clean(v):
    if v is None: return ""
    return str(v).strip().replace("\t", " ").replace("\n", " ").replace("\r", " ")

def fmt_acres(raw):
    if not raw: return ""
    s = str(raw).replace(",", "").strip()
    m = re.search(r'[\d]+(?:\.\d+)?', s)
    return m.group(0) if m else ""

def fmt_length(raw):
    if not raw: return ""
    s = str(raw).strip()
    m = re.search(r'([\d]+(?:\.\d+)?)', s)
    return m.group(1) if m else ""

def normalize_counties(lst):
    out = []
    for c in (lst or []):
        c = re.sub(r',?\s*(Ohio|OH)\s*$', '', str(c), flags=re.I).strip()
        c = re.sub(r'\s+County\s*$', '', c, flags=re.I).strip()
        if c: out.append(c)
    return "; ".join(sorted(set(out)))

# ─────────────────────────────────────────────────────────────
# FEATURES MAPPER  (features_raw → controlled vocab pipe-delimited)
# ─────────────────────────────────────────────────────────────
FEATURE_MAP = [
    # hiking / walking
    (r'hiking trail|walking trail|walking path|winding trail|nature trail|loop trail|trail system|interpretive trail|self.guided interpretive', "Hiking Trail"),
    (r'boardwalk',                  "Boardwalk"),
    (r'interpretive trail|self.guided interpretive', "Interpretive Sign"),  # mapped; "Hiking Trail" also fires above
    (r'bridle trail|equestrian',    "Bridle Trail"),
    # water
    (r'boat ramp|launch ramp',      "Boat Ramp"),
    (r'boat launch|watercraft|canoe|kayak', "Watercraft Access"),
    (r'fishing pond|fishing lake|13.acre pond', "Fishing Area"),
    (r'fishing pond',               "Pond"),                                 # also emit Pond for fishing ponds
    (r'swimming beach|swim beach',  "Swimming Beach"),
    (r'swimming pool|city pool',    "Swimming Pool"),
    (r'splash pad|spray pad',       "Spray Park"),
    # picnic / shelter
    (r'pavilion|shelter house|open air pavilion|rentable.*shelter|covered seating', "Pavilion"),
    (r'picnic area|picnic spot|picnic table', "Picnic Area"),
    (r'gazebo',                     "Gazebo"),
    # sports
    (r'baseball|softball',          "Ball Diamond"),
    (r'basketball court',           "Basketball Court"),
    (r'tennis court',               "Tennis Court"),
    (r'pickleball court',           "Pickleball Court"),
    (r'volleyball court|sand volleyball', "Volleyball Court"),
    (r'soccer field|soccer complex', "Soccer Pitch"),
    (r'football field',             "Football Field"),
    (r'disc golf',                  "Disc Golf Course"),
    (r'skate park|skate ramp',      "Skate Park"),
    (r'miniature golf',             "Mini Golf"),
    # recreation
    (r'playground|play equipment|play train|imagination kingdom', "Playground"),
    (r'sledding hill',              "Sledding Hill"),
    (r'horseshoe',                  "Horseshoe Pitch"),
    (r'archery',                    "Archery Range"),
    (r'ropes course|high ropes',    "Ropes Course"),
    (r'shooting sports',            "Shooting Range"),
    (r'dog park',                   "Dog Park"),
    # amenities
    (r'restroom|flush toilet|portable toilet|bathroom', "Restrooms"),
    (r'parking',                    "Parking Lot"),
    (r'kiosk|information kiosk',    "Kiosk"),
    # concession stand and dump station: no vocabulary equivalent — captured in features_raw only
    (r'camping|campsite',           "Camping"),
    (r'cabin|camper cabin|yurt',    "Cabin Rentals"),
    (r'ADA.compliant|ADA accessible|wheelchair', "ADA Accessible"),
    # natural
    (r'observation deck',           "Observation Deck"),
    (r'vernal pool',                "Vernal Pool"),
    (r'hunting area|public hunting', "Hunting Area"),
    (r'wildlife viewing|wildlife.*observation', "Wildlife Observation Area"),
    # historical
    (r'historic.*depot|train depot|caboose|railroad artifact', "Historic Structure"),
    (r'war memorial|memorial statue|monument|WWI|military monument', "Monument"),
    # educational / farm
    (r'nature center|nature lab',   "Nature Center"),
    (r'wagon tour|tractor.*tour|guided.*tour', "Guided Tours"),
    (r'farm store|bison.*store',    "Farm Store"),
    # misc
    (r'pollinator garden',          "Pollinator Garden"),
]

def map_features(raw_text):
    if not raw_text: return ""
    raw_lower = raw_text.lower()
    found = []
    seen = set()
    for pattern, term in FEATURE_MAP:
        if term not in seen and re.search(pattern, raw_lower):
            found.append(term)
            seen.add(term)
    return "; ".join(found)

# ─────────────────────────────────────────────────────────────
# NOTES BUILDER
# ─────────────────────────────────────────────────────────────
def gps_note(conf, name):
    if conf == "HIGH": return ""
    if conf == "MED":  return "GPS from address geocode — verify precision."
    if conf == "LOW":  return "GPS approximate — centroid-level; needs field verification."
    return f"GPS needed — {name} location unconfirmed."

# ─────────────────────────────────────────────────────────────
# ENTITY DEFINITIONS
# Stage 1 (Resolution) + Stage 2b/2c (Normalization) combined inline
# Each dict = one resolved+normalized record ready for TSV/DB
# ─────────────────────────────────────────────────────────────

# ---------- SITES ----------

SITES = [
  # ── TIER 2 — STATE ──────────────────────────────────────────
  {
    "site_id": "FUL-SI-001",
    "name": "Goll Woods State Nature Preserve",
    "category": "Nature Preserve",         # IMP-065: designation=SNP
    "subtype": "State Nature Preserve",
    "designation": "State Nature Preserve",
    "status": "Active",
    "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Natural Areas and Preserves",
    "partner_agencies": "",
    "coordination": "",
    "description": "A 321-acre state nature preserve in northwestern Ohio containing a remnant of the historic Great Black Swamp. Features old-growth forest with trees up to 400 years old and 4-foot diameters. Renowned for number and variety of spring wildflowers including large-flowered trillium (Ohio's state wildflower), bloodroot, columbine, marsh marigold, spotted coral-root, and three-birds-orchid. Approximately 100 acres designated old-growth forest. National Natural Landmark.",
    "location": "5800 County Road 26, Archbold, Ohio 43502",
    "acres": "320.64",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Goll Woods State Nature Preserve",
    "features_raw": "Two parking areas (East lot: 5800 CR 26; West lot); observation deck overlooking Tiffin River; boardwalks through wet areas; multiple benches; vernal pools; kiosk; portable toilet at East lot; Northwest District Preserve Office on site; Goll Cemetery adjacent to trails; 5.25 miles of trails (4 named loops)",
    "notes_extra": "National Natural Landmark. Baseline seed confirmed. Acreage: 320.64 (Wikipedia/baseline).",
    "url_primary": "http://naturepreserves.ohiodnr.gov/gollwoods",
    "urls_extra": "https://trekohio.com/2017/03/12/goll-woods-state-nature-preserve/; https://en.wikipedia.org/wiki/Goll_Woods_State_Nature_Preserve",
    "parent_site_id": "",
    "discovery_tier": 2,
  },
  {
    "site_id": "FUL-SI-002",
    "name": "Harrison Lake State Park",
    "category": "Park",
    "subtype": "Waterfront Park",           # primary feature is 95-acre lake with swimming beach
    "designation": "State Park",
    "status": "Active",
    "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Parks and Watercraft",
    "partner_agencies": "",
    "coordination": "",
    "description": "A 142-acre public recreation area established 1950, surrounding 95-acre Harrison Lake (created 1939 by damming Mill Creek, a tributary of the Tiffin River). The lake has a maximum depth of fifteen feet near the dam. Popular for swimming, fishing, camping, canoeing, and hiking.",
    "location": "26246 Harrison Lake Road, Fayette, Ohio 43521",
    "acres": "142",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Harrison Lake State Park",
    "features_raw": "Swimming beach; boat ramp; watercraft rental; 3.5-mile hiking trail; 193 campsites (126 electric); camper cabins; yurts; showers; flush toilets; dump station; pet-designated sites; playground; horseshoe pits; picnic areas; disc golf; ADA-compliant site; camp office on site",
    "notes_extra": "Baseline seed confirmed. Established 1950. Lake: 95 acres. Fish species: bluegill, largemouth bass, channel catfish, white crappie, bullhead, northern pike.",
    "url_primary": "https://en.wikipedia.org/wiki/Harrison_Lake_State_Park",
    "urls_extra": "https://stateparks.com/harrison_lake_state_park_in_ohio.html",
    "parent_site_id": "",
    "discovery_tier": 2,
  },
  {
    "site_id": "FUL-SI-003",
    "name": "Maumee State Forest",
    "category": "Conservation Area",
    "subtype": "",
    "designation": "State Forest",
    "status": "Active",
    "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Forestry",
    "partner_agencies": "",
    "coordination": "",
    "description": "A 3,452-acre state forest occupying largely flat land formerly cleared for farming, spanning Fulton, Henry, and Lucas counties. Represents a remnant example of oak openings habitat that once covered much of Northwest Ohio and Southeast Michigan. A patchwork of non-contiguous parcels. One of only four Ohio State Forests with all-terrain vehicle trails and the only one in Northwest Ohio.",
    "location": "3390 County Rd. D, Swanton, OH 43558",
    "acres": "3452",
    "counties_raw": ["Fulton", "Henry", "Lucas"],
    "municipality": "",
    "township": "",
    "gps_name": "Maumee State Forest",
    "features_raw": "66 miles of hiking trails/firelanes; 8 miles of bridle trails; 8 miles of APV/ATV trails; Stewardship Trail (2-mile self-guided interpretive trail); public hunting; map available from Division of Forestry",
    "notes_extra": "HELD — cross-county entity (Fulton, Henry, Lucas). Fulton County portion not specifically delineated by source; GIS verification needed. Acreage: 3,452 (Wikipedia). GPS at forest HQ (3390 County Rd. D, Swanton). Baseline seed.",
    "url_primary": "https://en.wikipedia.org/wiki/Maumee_State_Forest",
    "urls_extra": "https://ohiodnr.gov/wps/portal/gov/odnr/go-and-do/see-the-sights/lake-erie-birding-trail/oak-openings-loop/maumee-state-forest",
    "parent_site_id": "",
    "discovery_tier": 2,
  },
  {
    "site_id": "FUL-SI-004",
    "name": "Tiffin River Wildlife Area",
    "category": "Wildlife Area",
    "subtype": "State Wildlife Area",       # IMP-065: ODNR Division of Wildlife, state-owned
    "designation": "State Wildlife Area",
    "status": "Active",
    "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Wildlife",
    "partner_agencies": "",
    "coordination": "",
    "description": "A non-contiguous 465-acre State Wildlife Management Area in western Fulton County on State Route 66, between Fayette and Archbold. Pheasant releases by Ohio DNR for hunting purposes. Named after the Tiffin River.",
    "location": "Ohio State Route 66, between Fayette and Archbold, Ohio; parking via County Road 23",
    "acres": "465",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Tiffin River Wildlife Area",
    "features_raw": "Public hunting; pheasant releases; parking lot off County Road 23; fishing in Tiffin River and tributaries (catfish, bass, panfish)",
    "notes_extra": "NEW DISCOVERY — not in baseline. Non-contiguous parcels. GPS from Wikipedia infobox (41°36'20\"N 84°18'42\"W).",
    "url_primary": "https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/tiffin-river-wildlife-area",
    "urls_extra": "https://en.wikipedia.org/wiki/Tiffin_River_Wildlife_Area",
    "parent_site_id": "",
    "discovery_tier": 2,
  },
  {
    "site_id": "FUL-SI-005",
    "name": "Fulton Pond Wildlife Area",
    "category": "Wildlife Area",
    "subtype": "State Wildlife Area",       # IMP-065: ODNR Division of Wildlife, state-owned
    "designation": "State Wildlife Area",
    "status": "Active",
    "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Wildlife",
    "partner_agencies": "",
    "coordination": "",
    "description": "A 35-acre state wildlife area located 2 miles northwest of Swanton, Ohio, adjacent to the Ohio Turnpike. Contains a 13-acre fishing pond with 0.7 miles of shoreline.",
    "location": "8529 Co Rd 3, Swanton, OH 43558; entrance on Township Road 3",
    "acres": "35",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Fulton Pond Wildlife Area",
    "features_raw": "13-acre fishing pond; 0.7 miles shoreline; public fishing; adjacent to Ohio Turnpike; entrance on Township Road 3",
    "notes_extra": "Baseline seed confirmed. GPS from ODNR fishing map (approximate centroid). 13-acre pond.",
    "url_primary": "https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/fulton-pond-wildlife-area",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 2,
  },
  # ── TIER 3 — DISTRICT ──────────────────────────────────────
  {
    "site_id": "FUL-SI-006",
    "name": "Oak Openings Corridor (Metroparks Toledo — Fulton County parcels)",
    "category": "Conservation Area",
    "subtype": "",
    "designation": "",
    "status": "Active",
    "ownership": "Metroparks Toledo",
    "governance": "Metroparks Toledo",
    "partner_agencies": "Green Ribbon Initiative partners; The Nature Conservancy; ODNR Division of Forestry",
    "coordination": "Green Ribbon Initiative — multi-agency effort to preserve Oak Openings Region",
    "description": "Conservation land acquired by Metroparks Toledo in Swan Creek Township, Fulton County, as part of the Oak Openings Corridor connecting Secor and Oak Openings Preserve Metroparks. Part of approximately 1,900 total acres in western Lucas County and Fulton County. Goal is to reduce habitat fragmentation in the globally significant Oak Openings Region.",
    "location": "Swan Creek Township, Fulton County, Ohio",
    "acres": "",
    "counties_raw": ["Fulton", "Lucas"],
    "municipality": "",
    "township": "",
    "gps_name": "",   # no GPS — HELD
    "features_raw": "Conservation/natural area parcels; Oak Openings Corridor Trail (planned extension to Swanton); habitat restoration",
    "notes_extra": "HELD — cross-county entity (Lucas + Fulton). Fulton County portion is undeveloped conservation land parcels in Swan Creek Township. Public access status uncertain. Individual parcel identities unknown. GIS parcel resolution needed. NEW DISCOVERY.",
    "url_primary": "https://metroparkstoledo.com/conservation/highlights/oak-openings-corridor/",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 3,
  },
  # ── TIER 6 — MUNICIPAL: WAUSEON ────────────────────────────
  {
    "site_id": "FUL-SI-007",
    "name": "Biddle Park",
    "category": "Recreation Facility",    # primary identity: "large athletic complex"
    "subtype": "Sports Complex",
    "designation": "",
    "status": "Active",
    "ownership": "City of Wauseon",
    "governance": "City of Wauseon Parks & Recreation",
    "partner_agencies": "",
    "coordination": "",
    "description": "Large athletic complex serving as the primary sports facility for the City of Wauseon. Named in honor of Dorothy B. and Clark O. Biddle. Wauseon's largest park at 73.4 acres, opened May 2009. Located on the east side of Wauseon on Glenwood Avenue.",
    "location": "900 North Glenwood Avenue, Wauseon, OH 43567",
    "acres": "73.4",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Biddle Park",
    "features_raw": "8 baseball/softball fields; 3 tee-ball fields; 3 batting cages; 3 basketball courts; 3 sand volleyball courts; 1 football field; 9 soccer fields",
    "notes_extra": "Baseline seed confirmed. Address from search: 900 N Glenwood Ave. GPS approximate — needs field verification.",
    "url_primary": "https://www.cityofwauseon.com/our-parks",
    "urls_extra": "https://wauseon.recdesk.com/Community/Facility",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-008",
    "name": "Depot Park",
    "category": "Park",
    "subtype": "Historic Park",           # historic train depot, caboose as primary features
    "designation": "",
    "status": "Active",
    "ownership": "City of Wauseon",
    "governance": "City of Wauseon Parks & Recreation",
    "partner_agencies": "",
    "coordination": "",
    "description": "A small historic park featuring a preserved train depot and caboose in Wauseon. Opened July 15, 1970. 1.9 acres.",
    "location": "Wauseon, OH 43567",
    "acres": "1.9",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Depot Park",
    "features_raw": "Historical train depot; preserved train caboose; wooden play train",
    "notes_extra": "Baseline seed confirmed. Opened 1970. GPS approximate.",
    "url_primary": "https://www.cityofwauseon.com/our-parks",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-009",
    "name": "Rotary Park & Goodwin Preserve",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "City of Wauseon",
    "governance": "City of Wauseon Parks & Recreation",
    "partner_agencies": "",
    "coordination": "",
    "description": "Combined park and natural area along Wood Street in Wauseon. Rotary Park offers a fishing pond and playground. Goodwin Preserve, established 2004, is a wooded area with grills, picnic spots, and walking trail adjacent to Rotary Park. Parking off Wood Street.",
    "location": "Wood Street, Wauseon, OH 43567",
    "acres": "4.5",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Rotary Park & Goodwin Preserve",
    "features_raw": "Fishing pond; playground; Goodwin Preserve wooded area; grills; picnic spots; walking trail; Rotary Shelter House; parking off Wood Street",
    "notes_extra": "Baseline had separate entries for 'Rotary Park' and 'Goodwin Preserve' — confirmed as contiguous/connected. Merged as single entity; Goodwin Preserve may warrant independent identity in future. GPS approximate.",
    "url_primary": "https://www.cityofwauseon.com/our-parks",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-010",
    "name": "Homecoming Park",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "City of Wauseon",
    "governance": "City of Wauseon Parks & Recreation",
    "partner_agencies": "",
    "coordination": "",
    "description": "A 34.3-acre municipal park in Wauseon offering a variety of recreational amenities including a wooded walking path and sledding hill.",
    "location": "715 Lawrence Ave, Wauseon, OH 43567",
    "acres": "34.3",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Homecoming Park",
    "features_raw": "Sledding hill; walking path; wooded walking path; public restrooms; 2 playgrounds; gazebo; pickleball courts; 2 open air pavilions",
    "notes_extra": "Baseline seed confirmed. Address: 715 Lawrence Ave. GPS confirmed from mypacer.com.",
    "url_primary": "https://www.cityofwauseon.com/our-parks",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-011",
    "name": "Memorial Park (Wauseon)",
    "category": "Park",
    "subtype": "Historic Park",           # war memorial statue is primary identity feature
    "designation": "",
    "status": "Active",
    "ownership": "City of Wauseon",
    "governance": "City of Wauseon Parks & Recreation",
    "partner_agencies": "",
    "coordination": "",
    "description": "A small neighborhood park opened June 19, 1924, located on West Elm Street just outside downtown Wauseon. Features a war memorial statue. Also referred to as North Park in some sources.",
    "location": "202 Madison St (also: West Elm Street area), Wauseon, OH 43567",
    "acres": "2.4",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Memorial Park (Wauseon)",
    "features_raw": "Playground; half basketball court; war memorial statue",
    "notes_extra": "Baseline lists as 'North Park/Memorial Park'. City parks page confirms this is Memorial Park, opened 1924. Also called North Park. Address confirmed: 202 Madison St. GPS confirmed from mypacer.com.",
    "url_primary": "https://www.cityofwauseon.com/our-parks",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-012",
    "name": "Reighard Park",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "City of Wauseon",
    "governance": "City of Wauseon Parks & Recreation",
    "partner_agencies": "",
    "coordination": "",
    "description": "An 18.5-acre park opened April 3, 1940, featuring Imagination Kingdom playground, the City Pool, three shelter houses, restroom facilities, tennis courts, disc golf course, and winding trails.",
    "location": "615 Oak St, Wauseon, OH 43567",
    "acres": "18.5",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Reighard Park",
    "features_raw": "Disc golf course; City Pool (swimming); Imagination Kingdom playground; 3 shelter houses; restrooms; tennis courts; winding trails",
    "notes_extra": "Baseline seed confirmed. Opened 1940. Address: 615 Oak St. GPS confirmed from mypacer.com.",
    "url_primary": "https://www.cityofwauseon.com/our-parks",
    "urls_extra": "https://udisc.com/courses/reighard-park-cRDL",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-013",
    "name": "South Park (Wauseon)",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "City of Wauseon",
    "governance": "City of Wauseon Parks & Recreation",
    "partner_agencies": "",
    "coordination": "",
    "description": "A neighborhood park in Wauseon with playground equipment and lighted basketball courts.",
    "location": "405 E Park St, Wauseon, OH 43567",
    "acres": "",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "South Park (Wauseon)",
    "features_raw": "Playground equipment; 2 lighted basketball courts",
    "notes_extra": "Baseline seed confirmed. Address: 405 E Park St. GPS confirmed from mypacer.com.",
    "url_primary": "https://www.cityofwauseon.com/our-parks",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-014",
    "name": "Wabash Park (Wauseon)",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "City of Wauseon",
    "governance": "City of Wauseon Parks & Recreation",
    "partner_agencies": "",
    "coordination": "",
    "description": "A neighborhood park in Wauseon featuring a skate park and basic recreational amenities. Became a City park November 20, 1951.",
    "location": "Wauseon, OH 43567",
    "acres": "",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Wabash Park (Wauseon)",
    "features_raw": "Playground; half basketball court; skate ramps/equipment (skate park)",
    "notes_extra": "Baseline seed confirmed. Established 1951. GPS approximate.",
    "url_primary": "https://www.cityofwauseon.com/our-parks",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-015",
    "name": "Harmon Park",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "City of Wauseon",
    "governance": "City of Wauseon Parks & Recreation",
    "partner_agencies": "",
    "coordination": "",
    "description": "An 8.3-acre park in Wauseon offering walking and running trails in a natural setting.",
    "location": "Wauseon, OH 43567",
    "acres": "8.3",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Harmon Park",
    "features_raw": "Walking trails; running trails; green space",
    "notes_extra": "NEW DISCOVERY — not in baseline. Confirmed via mypacer park listing. 8.3 acres. GPS approximate — map verification needed.",
    "url_primary": "https://www.mypacer.com/parks/c18dt/wauseon-ohio",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  # ── TIER 6 — MUNICIPAL: ARCHBOLD ───────────────────────────
  {
    "site_id": "FUL-SI-016",
    "name": "Lion's Park",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "Village of Archbold",
    "governance": "Village of Archbold Parks & Recreation",
    "partner_agencies": "",
    "coordination": "",
    "description": "A small neighborhood park on East Holland Street in Archbold.",
    "location": "East Holland Street, Archbold, OH 43502",
    "acres": "",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Lion's Park",
    "features_raw": "Basketball court; playground equipment",
    "notes_extra": "Baseline seed confirmed. GPS approximate.",
    "url_primary": "https://www.archbold.com/parks___recreation/parks.php",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-017",
    "name": "Memorial Park (Archbold)",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "Village of Archbold",
    "governance": "Village of Archbold Parks & Recreation",
    "partner_agencies": "",
    "coordination": "",
    "description": "A 40+ acre park on the south side of Archbold, home to baseball and softball programs. Features monuments honoring military service.",
    "location": "South side of Archbold, OH 43502",
    "acres": "40",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Memorial Park (Archbold)",
    "features_raw": "Volleyball courts; basketball courts; large playground; 4 tennis courts; restrooms; picnic shelter; baseball/softball fields; military monuments",
    "notes_extra": "Baseline seed confirmed. Also known as Memorial Park Ball Fields. GPS approximate.",
    "url_primary": "https://www.archbold.com/parks___recreation/parks.php",
    "urls_extra": "https://archboldparks.recdesk.com/Community/Facility",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-018",
    "name": "North Pointe Park",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "Village of Archbold",
    "governance": "Village of Archbold Parks & Recreation",
    "partner_agencies": "",
    "coordination": "",
    "description": "A residential area neighborhood park centrally located near the intersection of St. Anne and Primrose Streets in Archbold.",
    "location": "St. Anne & Primrose Streets, Archbold, OH 43502",
    "acres": "",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "North Pointe Park",
    "features_raw": "Playground; lighted basketball court; picnic shelter; sledding hill",
    "notes_extra": "Baseline seed confirmed. GPS approximate.",
    "url_primary": "https://www.archbold.com/parks___recreation/parks.php",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-019",
    "name": "Ruihley Park",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "Village of Archbold",
    "governance": "Village of Archbold Parks & Recreation",
    "partner_agencies": "",
    "coordination": "",
    "description": "A 27-acre community park in the center of Archbold, described as 'beautiful and serene,' serving as a major community events venue.",
    "location": "401 W Holland St, Archbold, OH 43502",
    "acres": "27",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Ruihley Park",
    "features_raw": "Pavilion; Scout Cabin; Cottage; community pool; splash pad; pickleball courts; playgrounds; walking paths; volleyball courts; restrooms",
    "notes_extra": "Baseline seed confirmed. Address: 401 W Holland St. GPS confirmed from mypacer.com.",
    "url_primary": "https://www.archbold.com/parks___recreation/parks.php",
    "urls_extra": "https://archboldparks.recdesk.com/Community/Facility?type=2",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-020",
    "name": "South Street Park",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "Village of Archbold",
    "governance": "Village of Archbold Parks & Recreation",
    "partner_agencies": "",
    "coordination": "",
    "description": "A neighborhood park at the corner of South and West Streets in Archbold with recent playground improvements.",
    "location": "South Street & West Street, Archbold, OH 43502",
    "acres": "",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "South Street Park",
    "features_raw": "Playground equipment; resurfaced basketball court; trees",
    "notes_extra": "Baseline seed confirmed. GPS approximate.",
    "url_primary": "https://www.archbold.com/parks___recreation/parks.php",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-021",
    "name": "Woodland Park",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "Village of Archbold",
    "governance": "Village of Archbold Parks & Recreation",
    "partner_agencies": "",
    "coordination": "",
    "description": "A large (approximately 60-acre) park adjacent to the Woodland Oaks subdivision on SR 66. The newest addition to Archbold's park system, featuring a disc golf course and wooded recreation area.",
    "location": "Adjacent to Woodland Oaks subdivision, SR 66, Archbold, OH 43502",
    "acres": "60",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Woodland Park",
    "features_raw": "Playground; restrooms; concession stand; basketball courts; walking trails; disc golf course; flag football/soccer fields",
    "notes_extra": "Baseline seed confirmed. Newest park in Archbold system. GPS approximate.",
    "url_primary": "https://www.archbold.com/parks___recreation/parks.php",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  # ── TIER 6 — MUNICIPAL: DELTA ──────────────────────────────
  {
    "site_id": "FUL-SI-022",
    "name": "Delta Park",
    "category": "Park",
    "subtype": "Sports Park",             # 7 baseball/softball diamonds + soccer complex dominant
    "designation": "",
    "status": "Active",
    "ownership": "Village of Delta",
    "governance": "Village of Delta Parks & Recreation",
    "partner_agencies": "",
    "coordination": "",
    "description": "The primary active park in the Village of Delta, established 1955 on 23 acres. Home to the annual Delta Chicken Festival (2nd weekend of July). Also known as Delta Municipal Park.",
    "location": "Delta, OH 43515",
    "acres": "23",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Delta Park",
    "features_raw": "2 sand volleyball courts; 2 basketball courts; skate park; 4 sets of playground equipment; 7 baseball/softball diamonds; 3 shelter houses (1 rentable); extensive soccer complex",
    "notes_extra": "NEW DISCOVERY — not directly in baseline. Established 1955. GPS approximate.",
    "url_primary": "https://www.villageofdelta.org/1207/Parks-Recreation",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-023",
    "name": "Wildwood Park (Delta)",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Inactive",                 # described as "overgrown and no longer maintained"
    "ownership": "Village of Delta",
    "governance": "Village of Delta Parks & Recreation",
    "partner_agencies": "",
    "coordination": "",
    "description": "Delta's first park, established July 1926 on a 7-acre property historically known as 'Longnecker Grove.' Originally featured swings, slides, ball diamonds, a bandstand, and winter ice skating. Now described as overgrown and no longer maintained.",
    "location": "Adrian Street, north end of Greenlawn Cemetery, Delta, OH 43515",
    "acres": "7",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Wildwood Park (Delta)",
    "features_raw": "Abandoned/overgrown; historically: playground, ball diamonds, bandstand, ice skating",
    "notes_extra": "NEW DISCOVERY. Corresponds to GNIS feature 'Longnecker Grove' (GPS 41.5764407,-84.0152237). Established 1926. Status: Inactive — described as overgrown and no longer maintained. Baseline GNIS seed 'Longnecker Grove' resolves to this park.",
    "url_primary": "https://www.villageofdelta.org/1207/Parks-Recreation",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  # ── TIER 6 — MUNICIPAL: FAYETTE ────────────────────────────
  {
    "site_id": "FUL-SI-024",
    "name": "Hatcher Park",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "Village of Fayette",
    "governance": "Village of Fayette Parks Department",
    "partner_agencies": "",
    "coordination": "",
    "description": "",
    "location": "Fayette, OH 43521",
    "acres": "",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "",   # unverified — no GPS
    "features_raw": "",
    "notes_extra": "UNVERIFIED — baseline seed 'Hatcher Park'. Fayette parks page mentions only baseball/softball diamonds but does not list park names. Existence not independently confirmed. Map verification required. No GPS acquired.",
    "url_primary": "https://www.villageoffayette.com/2152/Parks-Recreation",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-025",
    "name": "Normal Grove Park",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "Village of Fayette",
    "governance": "Village of Fayette Parks Department",
    "partner_agencies": "",
    "coordination": "",
    "description": "",
    "location": "Fayette, OH 43521",
    "acres": "",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "",   # unverified — no GPS
    "features_raw": "",
    "notes_extra": "UNVERIFIED — baseline seed 'Nomal Grove Park' (likely spelling error for Normal Grove Park). Mentioned in Fayette village photo gallery. Not detailed on official parks page. Map verification required. No GPS acquired.",
    "url_primary": "https://www.villageoffayette.com/2152/Parks-Recreation",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  # ── TIER 6 — MUNICIPAL: LYONS ──────────────────────────────
  {
    "site_id": "FUL-SI-026",
    "name": "Dunbar-Ingall Park",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "Village of Lyons",
    "governance": "Village of Lyons",
    "partner_agencies": "",
    "coordination": "",
    "description": "A community park along West Morenci Street hosting community events including the annual tree lighting ceremony. The village accepted a 3/4-acre land donation for park expansion.",
    "location": "West Morenci Street (OH-120), Lyons, OH 43533",
    "acres": "",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Dunbar-Ingall Park",
    "features_raw": "Community event space; planned gazebo; green space",
    "notes_extra": "Baseline seed confirmed. Recent 3/4-acre land donation. Gazebo improvement planned. GPS approximate.",
    "url_primary": "https://www.lyons-ohio.com/community-parks.html",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-027",
    "name": "Green Memorial Park",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "Village of Lyons",
    "governance": "Village of Lyons",
    "partner_agencies": "",
    "coordination": "",
    "description": "",
    "location": "Lyons, OH 43533",
    "acres": "",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "",   # no GPS — listed on parks page but no details
    "features_raw": "",
    "notes_extra": "Baseline seed confirmed. Listed on Lyons village community parks page but no specific details available. Map verification needed for address and features. GPS not acquired.",
    "url_primary": "https://www.lyons-ohio.com/community-parks.html",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-028",
    "name": "Lyons Community Ball Park",
    "category": "Recreation Facility",
    "subtype": "Athletic Field",          # primarily ball fields by name and description
    "designation": "",
    "status": "Active",
    "ownership": "Village of Lyons",
    "governance": "Village of Lyons",
    "partner_agencies": "",
    "coordination": "",
    "description": "Public ball fields in the Village of Lyons.",
    "location": "Lyons, OH 43533",
    "acres": "",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "",   # no GPS
    "features_raw": "Ball park facilities; baseball/softball fields",
    "notes_extra": "Baseline seed confirmed. Map verification needed for address. GPS not acquired.",
    "url_primary": "https://www.lyons-ohio.com/community-parks.html",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  # ── TIER 6 — MUNICIPAL: METAMORA ───────────────────────────
  {
    "site_id": "FUL-SI-029",
    "name": "Metamora Community Park",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "Village of Metamora",
    "governance": "Village of Metamora",
    "partner_agencies": "",
    "coordination": "",
    "description": "Community park in the Village of Metamora hosting annual 'Park O Rama' events and community gatherings. Five acres on the west side designated for soccer tournaments.",
    "location": "Metamora, OH 43540",
    "acres": "",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Metamora Community Park",
    "features_raw": "Soccer fields (5-acre west side); 2 modern-style pavilions (1 with restrooms); asphalt walking trail; large covered seating areas with picnic tables",
    "notes_extra": "NEW DISCOVERY. Confirmed via Fulton County Visitors Bureau calendar and search results. Hosts annual Park O Rama festival. GPS approximate.",
    "url_primary": "https://www.metamoraohio.org/",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  # ── TIER 6 — MUNICIPAL: SWANTON ────────────────────────────
  {
    "site_id": "FUL-SI-030",
    "name": "Pilliod Park",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "Village of Swanton",
    "governance": "Village of Swanton",
    "partner_agencies": "",
    "coordination": "",
    "description": "A 4-acre picturesque park adjacent to the Swanton Public Library, featuring Swanton's preserved red caboose, gazebos, and a paved walkway. Home to the village's annual holiday light display.",
    "location": "Adjacent to Swanton Public Library, Swanton, OH 43558",
    "acres": "4.0",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Pilliod Park",
    "features_raw": "Red caboose; gazebos; paved walkway; holiday light display",
    "notes_extra": "Baseline seed confirmed. Note: Swanton is split between Fulton and Lucas counties — GIS verification needed to confirm county. GPS approximate.",
    "url_primary": "https://visitfultoncounty.com/240/Pilliod-Parik",
    "urls_extra": "https://visitfultoncounty.com/239/Village-of-Swanton-Parks",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-031",
    "name": "Rotary Park (Swanton)",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "Village of Swanton",
    "governance": "Village of Swanton",
    "partner_agencies": "",
    "coordination": "",
    "description": "A small park described as an offshoot of Pilliod Park in Swanton.",
    "location": "Swanton, OH 43558 (adjacent to Pilliod Park)",
    "acres": "",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Rotary Park (Swanton)",
    "features_raw": "",
    "notes_extra": "Baseline seed confirmed. Described as an offshoot/extension of Pilliod Park. Limited information. Note: Swanton split between Fulton/Lucas counties — GIS verification needed. GPS approximate.",
    "url_primary": "https://visitfultoncounty.com/241/Rotary-Park",
    "urls_extra": "https://visitfultoncounty.com/239/Village-of-Swanton-Parks",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  {
    "site_id": "FUL-SI-032",
    "name": "Swanton Memorial Park",
    "category": "Park",
    "subtype": "Sports Park",             # baseball, soccer, volleyball, tennis, basketball dominant
    "designation": "",
    "status": "Active",
    "ownership": "Village of Swanton",
    "governance": "Village of Swanton",
    "partner_agencies": "",
    "coordination": "",
    "description": "A large community park of 30+ acres in Swanton, with Ai Creek running through the park. Land originally donated by the McNeill family. Features a WWI Doughboy statue.",
    "location": "Swanton, OH 43558",
    "acres": "30",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Swanton Memorial Park",
    "features_raw": "Baseball diamonds; soccer fields; sand volleyball courts; tennis/pickleball courts; basketball courts; playgrounds; WWI Doughboy statue",
    "notes_extra": "Baseline seed confirmed. Ai Creek runs through park. Land donated by McNeill family. Note: Swanton split between Fulton/Lucas counties — GIS verification needed. GPS approximate.",
    "url_primary": "https://visitfultoncounty.com/242/Swanton-Memorial-Park",
    "urls_extra": "https://snoflo.org/parks/ohio/swanton-memorial-park",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  # ── TIER 7 — CONSERVANCY ───────────────────────────────────
  {
    "site_id": "FUL-SI-033",
    "name": "Pettisville Community Park",
    "category": "Park",
    "subtype": "Neighborhood Park",
    "designation": "",
    "status": "Active",
    "ownership": "PARC Inc. (501(c)(3) non-profit)",
    "governance": "PARC Inc.",
    "partner_agencies": "Village of Pettisville",
    "coordination": "",
    "description": "A community park in the Village of Pettisville operated by PARC Inc., a 501(c)(3) non-profit. Funded by biennial Friendship Days festivals and pavilion rentals. Open year-round 7am–11pm.",
    "location": "18405 County Road D-E, Pettisville, OH 43553",
    "acres": "26.6",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Pettisville Community Park",
    "features_raw": "Pickleball courts; basketball courts (lighted); pavilion (rentable, seats 120); fountain; recycling facilities; fishing derby location; community event space",
    "notes_extra": "NEW DISCOVERY. Governance: PARC Inc. (non-profit), not the Village. Address: 18405 County Road D-E. Acreage: 26.6 (mypacer). GPS confirmed.",
    "url_primary": "https://www.pettisvillepark.org/",
    "urls_extra": "https://www.pettisvillepark.org/park-info",
    "parent_site_id": "",
    "discovery_tier": 7,
  },
  # ── TIER 8 — PRIVATE ───────────────────────────────────────
  {
    "site_id": "FUL-SI-034",
    "name": "Sauder Village",
    "category": "Museum",
    "subtype": "Living Museum",           # IMP-068 + IMP-065: "Village" living-history museum
    "designation": "",
    "status": "Active",
    "ownership": "Sauder Village (private non-profit)",
    "governance": "Sauder Village",
    "partner_agencies": "",
    "coordination": "",
    "description": "Ohio's largest living-history museum recreating life in Northwest Ohio's Great Black Swamp from 1803 to 1928. Three distinct areas: 1800s crafts/buildings, a 1920s small town, and pioneer-era buildings. Open seasonally late April to late October. Admission charged.",
    "location": "22611 State Route 2, Archbold, OH 43502",
    "acres": "235",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Sauder Village",
    "features_raw": "Historic village buildings; 1800s and 1920s era displays; train ride; horse-drawn carriage; museum; Sauder Heritage Inn (98 rooms, indoor pool); 87-site campground; splash pad; fishing; bike trail; playground",
    "notes_extra": "Baseline seed confirmed. IMP-068: 'Village' + living-history museum context → category=Museum, subtype=Living Museum. Seasonal access (late April–late October). Admission-based. GPS from baseline.",
    "url_primary": "https://saudervillage.org/",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 8,
  },
  {
    "site_id": "FUL-SI-035",
    "name": "Bracy Gold Bison Ranch",
    "category": "Open Space",
    "subtype": "",
    "designation": "",
    "status": "Active",
    "ownership": "Bracy Gold (private)",
    "governance": "Bracy Gold Bison Ranch (private owner)",
    "partner_agencies": "",
    "coordination": "",
    "description": "A 55-acre working bison ranch established in 2018, home to grass-fed bison and free-range chickens. Offers tractor-drawn wagon tours into the bison pasture by appointment (mid-May through September). Also offers RV and tent camping on the working ranch. Farm store selling bison meat and products.",
    "location": "11616 County Road 4, Swanton, OH 43558",
    "acres": "55",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Bracy Gold Bison Ranch",
    "features_raw": "Wagon tours (by appointment); RV and tent camping; farm store (bison meat, products); annual Great Pumpkin Drop-Off event; bison pasture",
    "notes_extra": "Baseline seed confirmed. Tours by appointment; not open-access. Established 2018. GPS from baseline.",
    "url_primary": "https://bracygoldbison.com/",
    "urls_extra": "https://visitfultoncounty.com/299/Bracy-Gold-Bison-Ranch--A-Hidden-Gem-in-",
    "parent_site_id": "",
    "discovery_tier": 8,
  },
  {
    "site_id": "FUL-SI-036",
    "name": "4-H Camp Palmer",
    "category": "Campground",
    "subtype": "Cabin",                   # IMP-065: "rustic cabins" in description → Cabin subtype
    "designation": "",
    "status": "Active",
    "ownership": "4-H Camp Palmer Inc. (serves 11 NW Ohio counties)",
    "governance": "4-H Camp Palmer Inc. / Ohio State University Extension",
    "partner_agencies": "Ohio State University Extension",
    "coordination": "",
    "description": "A 146-acre privately owned youth camp adjacent to Harrison Lake State Park, operated by 4-H Camp Palmer Inc. for 4-H members across 11 Northwestern Ohio counties. Offers youth summer camps, school group retreats, outdoor education, and rental programs. Not open for general public day use.",
    "location": "26450 County Road MN, Fayette, OH 43521",
    "acres": "146",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "4-H Camp Palmer",
    "features_raw": "High ropes course; team building; archery range; canoe programs; swimming pool; shooting sports; Woodland Lodge; Rob's Cabin; rustic cabins; recreation hall; dining hall; Craft Hall; Nature Lab; sports field; sand volleyball court; tennis court; basketball court; miniature golf; Adirondack Shelter",
    "notes_extra": "Baseline seed 'Camp Palmer'. IMP-065: 'rustic cabins' in description → Cabin subtype. Programmatic access only (registered camps, school groups, rentals) — not open to general public. Address: 26450 County Road MN. GPS approximate.",
    "url_primary": "https://www.camppalmer.org/",
    "urls_extra": "https://buckeyefunder.osu.edu/4hcamppalmer",
    "parent_site_id": "",
    "discovery_tier": 8,
  },
  {
    "site_id": "FUL-SI-037",
    "name": "Robert Fulton Agriculture Center",
    "category": "Cultural Facility",
    "subtype": "",
    "designation": "",
    "status": "Active",
    "ownership": "Ohio State University Extension",
    "governance": "OSU Extension / Fulton County",
    "partner_agencies": "Fulton County",
    "coordination": "",
    "description": "An OSU Extension facility with land lab and educational programming for agriculture and natural resource topics in Fulton County. Limited public access.",
    "location": "8770 State Route 108, Wauseon, OH 43567",
    "acres": "",
    "counties_raw": ["Fulton"],
    "municipality": "",
    "township": "",
    "gps_name": "Robert Fulton Agriculture Center",
    "features_raw": "Land lab; educational programming; agricultural research",
    "notes_extra": "Baseline seed confirmed. Educational/research facility — limited public access. GPS from baseline.",
    "url_primary": "https://fulton.osu.edu/",
    "urls_extra": "",
    "parent_site_id": "",
    "discovery_tier": 8,
  },
]

# ---------- TRAILS ----------

TRAILS = [
  # ── TIER 2 — Goll Woods loops ───────────────────────────────
  {
    "trail_id": "FUL-TR-001",
    "name": "Toadshade Trail",
    "alternate_names": "",
    "use_type": "Hiking",
    "surface_type": "Natural Surface",
    "origin_type": "",
    "length_mi": "1.5",
    "counties_raw": ["Fulton"],
    "governance": "Ohio Department of Natural Resources, Division of Natural Areas and Preserves",
    "partner_agencies": "",
    "status": "Active",
    "difficulty": "",
    "accessibility": "",
    "description": "Named loop trail within Goll Woods State Nature Preserve. One of four named loop trails in the 5.25-mile trail system.",
    "trail_history": "",
    "identity_notes": "Named loop trail at Goll Woods SNP. Length from TrekOhio.",
    "notes": "",
    "url_primary": "https://trekohio.com/2017/03/12/goll-woods-state-nature-preserve/",
    "maps": "https://dam.assets.ohio.gov/image/upload/ohiodnr.gov/documents/natural-areas/maps/GOLL_8_5x11.pdf",
    "parent_site_id": "FUL-SI-001",
    "discovery_tier": 2,
  },
  {
    "trail_id": "FUL-TR-002",
    "name": "Tuliptree Trail",
    "alternate_names": "",
    "use_type": "Hiking",
    "surface_type": "Natural Surface",
    "origin_type": "",
    "length_mi": "1.25",
    "counties_raw": ["Fulton"],
    "governance": "Ohio Department of Natural Resources, Division of Natural Areas and Preserves",
    "partner_agencies": "",
    "status": "Active",
    "difficulty": "",
    "accessibility": "",
    "description": "Named loop trail within Goll Woods State Nature Preserve.",
    "trail_history": "",
    "identity_notes": "Named loop trail at Goll Woods SNP. Length from TrekOhio.",
    "notes": "",
    "url_primary": "https://trekohio.com/2017/03/12/goll-woods-state-nature-preserve/",
    "maps": "https://dam.assets.ohio.gov/image/upload/ohiodnr.gov/documents/natural-areas/maps/GOLL_8_5x11.pdf",
    "parent_site_id": "FUL-SI-001",
    "discovery_tier": 2,
  },
  {
    "trail_id": "FUL-TR-003",
    "name": "Bur Oak Trail",
    "alternate_names": "",
    "use_type": "Hiking",
    "surface_type": "Natural Surface",
    "origin_type": "",
    "length_mi": "1.0",
    "counties_raw": ["Fulton"],
    "governance": "Ohio Department of Natural Resources, Division of Natural Areas and Preserves",
    "partner_agencies": "",
    "status": "Active",
    "difficulty": "",
    "accessibility": "",
    "description": "Named loop trail within Goll Woods State Nature Preserve.",
    "trail_history": "",
    "identity_notes": "Named loop trail at Goll Woods SNP. Length from TrekOhio.",
    "notes": "",
    "url_primary": "https://trekohio.com/2017/03/12/goll-woods-state-nature-preserve/",
    "maps": "https://dam.assets.ohio.gov/image/upload/ohiodnr.gov/documents/natural-areas/maps/GOLL_8_5x11.pdf",
    "parent_site_id": "FUL-SI-001",
    "discovery_tier": 2,
  },
  {
    "trail_id": "FUL-TR-004",
    "name": "Cottonwood Trail",
    "alternate_names": "",
    "use_type": "Hiking",
    "surface_type": "Natural Surface",
    "origin_type": "",
    "length_mi": "1.5",
    "counties_raw": ["Fulton"],
    "governance": "Ohio Department of Natural Resources, Division of Natural Areas and Preserves",
    "partner_agencies": "",
    "status": "Active",
    "difficulty": "",
    "accessibility": "",
    "description": "Named loop trail within Goll Woods State Nature Preserve.",
    "trail_history": "",
    "identity_notes": "Named loop trail at Goll Woods SNP. Length from TrekOhio.",
    "notes": "",
    "url_primary": "https://trekohio.com/2017/03/12/goll-woods-state-nature-preserve/",
    "maps": "https://dam.assets.ohio.gov/image/upload/ohiodnr.gov/documents/natural-areas/maps/GOLL_8_5x11.pdf",
    "parent_site_id": "FUL-SI-001",
    "discovery_tier": 2,
  },
  {
    "trail_id": "FUL-TR-005",
    "name": "Stewardship Trail",
    "alternate_names": "",
    "use_type": "Hiking",
    "surface_type": "Natural Surface",
    "origin_type": "",
    "length_mi": "2.0",
    "counties_raw": ["Fulton", "Henry", "Lucas"],
    "governance": "Ohio Department of Natural Resources, Division of Forestry",
    "partner_agencies": "",
    "status": "Active",
    "difficulty": "",
    "accessibility": "",
    "description": "A 2-mile self-guided interpretive trail within Maumee State Forest.",
    "trail_history": "",
    "identity_notes": "Self-guided interpretive trail at Maumee State Forest. Located in multi-county forest (Fulton/Henry/Lucas). HELD — primary county of location not confirmed via GIS.",
    "notes": "HELD — cross-county entity. Primary county of trail location requires GIS verification.",
    "url_primary": "https://en.wikipedia.org/wiki/Maumee_State_Forest",
    "maps": "",
    "parent_site_id": "FUL-SI-003",
    "discovery_tier": 2,
  },
  # ── TIER 6 — MUNICIPAL ─────────────────────────────────────
  {
    "trail_id": "FUL-TR-006",
    "name": "Cannonball Trail (Wauseon)",
    "alternate_names": "Wabash Cannonball Trail — Wauseon Segment",
    "use_type": "Multi-Use",              # source: "walking, running, biking, rollerblading"
    "surface_type": "Paved",             # "Asphalt/blacktop" → Paved
    "origin_type": "Rail Trail",         # Wabash Cannonball Trail is a rail-trail
    "length_mi": "2.0",
    "counties_raw": ["Fulton"],
    "governance": "City of Wauseon / Northwestern Ohio Rails-to-Trails Association (NORTA)",
    "partner_agencies": "Northwestern Ohio Rails-to-Trails Association (NORTA)",
    "status": "Active",
    "difficulty": "",
    "accessibility": "",
    "description": "A 2-mile paved urban segment of the Wabash Cannonball Trail crossing Wauseon from east to west. Part of the broader 64.1-mile cross-county rail trail.",
    "trail_history": "",
    "identity_notes": "Baseline had two duplicate entries: 'Cannonball Trail (Wauseon Segment)' and 'Cannonball Trail'. Same entity. This is the paved 2-mile Wauseon segment of WCT; identity parent is FUL-TR-007 (Wabash Cannonball Trail North Fork). Baseline GPS: 41.5480,-84.1410.",
    "notes": "Trail segment identity: this is the paved Wauseon city segment of the Wabash Cannonball Trail (FUL-TR-007). City of Wauseon maintains paved section; NORTA maintains remainder.",
    "url_primary": "https://www.cityofwauseon.com/our-parks",
    "maps": "",
    "parent_site_id": "",
    "discovery_tier": 6,
  },
  # ── TIER 7 — CONSERVANCY ───────────────────────────────────
  {
    "trail_id": "FUL-TR-007",
    "name": "Wabash Cannonball Trail (North Fork)",
    "alternate_names": "Wabash Cannonball Trail; WCT North Fork",
    "use_type": "Multi-Use",             # "walking, running, biking, rollerblading"
    "surface_type": "Mixed",             # asphalt (Wauseon + Lucas) + crushed stone/cinder (rural)
    "origin_type": "Rail Trail",         # former Wabash Railroad corridor
    "length_mi": "64.1",                 # total trail; Fulton County portion ~12 miles
    "counties_raw": ["Fulton", "Henry", "Williams", "Lucas"],
    "governance": "Northwestern Ohio Rails-to-Trails Association (NORTA)",
    "partner_agencies": "Metroparks Toledo (Lucas County section); City of Wauseon (Wauseon segment)",
    "status": "Active",
    "difficulty": "",
    "accessibility": "",
    "description": "A 64.1-mile converted rail trail on the former Wabash Railroad corridor traversing Fulton, Henry, Williams, and Lucas counties. NORTA owns and maintains the Fulton, Henry, and Williams County sections (approximately 32 miles of unpaved cinder/crushed-stone surface with paved Wauseon segment); Metroparks Toledo manages the Lucas County section. North Country National Scenic Trail affiliate.",
    "trail_history": "Converted from the former Wabash Railroad corridor. One of Ohio's longest rail-trails.",
    "identity_notes": "Baseline seed 'Wabash Cannonball Trail (North Fork)'. Cross-county entity already anchored in DB as WIL-TR-003 (Williams County). This FUL-TR-007 record is the Fulton County anchor. Fulton County access: (1) CR 23 north of US 20A trailhead (FUL-AP-001); (2) Wauseon city parks; (3) Fraker Mill covered bridge. May migrate to cross-county Trail Network entity. Baseline contained duplicate Wauseon entries — resolved by FUL-TR-006.",
    "notes": "Cross-county trail — also recorded as WIL-TR-003 (Williams County anchor). HELD pending cross-county network entity resolution.",
    "url_primary": "https://www.wabashcannonballtrail.org/",
    "maps": "https://www.wabashcannonballtrail.org/trail-access/",
    "parent_site_id": "",
    "discovery_tier": 7,
  },
]

# ---------- ACCESS POINTS ----------

ACCESS_POINTS = [
  {
    "access_point_id": "FUL-AP-001",
    "name": "Wabash Cannonball Trail — CR 23 Trailhead",
    "ap_type": "Trailhead",
    "status": "Active",
    "parent_entity_type": "Trail",
    "parent_entity_id": "FUL-TR-007",
    "county": "Fulton",
    "township": "",
    "municipality": "",
    "address": "County Road 23, north of US 20A, Wauseon area, Fulton County, OH",
    "gps_name": "",   # no GPS acquired
    "features_raw": "Parking (including horse trailer parking); information kiosk; pollinator garden",
    "identity_notes": "Primary trailhead for the Wabash Cannonball Trail (North Fork) in the Wauseon area. Located north of US 20A on Fulton County Road 23. Includes horse trailer parking. GPS acquisition needed — map verification required.",
    "notes": "Horse trailer parking available. Parent: FUL-TR-007 (Wabash Cannonball Trail North Fork).",
    "url_primary": "https://www.wabashcannonballtrail.org/trail-access/",
    "discovery_tier": 7,
  },
]

# ─────────────────────────────────────────────────────────────
# VOCABULARY VALIDATION GATE (Stage 4.5)
# ─────────────────────────────────────────────────────────────
errors = []

def vocab_check_sites(sites):
    for s in sites:
        sid = s["site_id"]
        cat = s["category"]
        sub = s.get("subtype", "")
        if cat not in SITE_CATEGORIES:
            errors.append(f"IMP-063 FATAL: {sid} '{s['name']}' — invalid category '{cat}'")
        if sub:
            valid_subs = {
                "Park": PARK_SUBTYPES,
                "Nature Preserve": NATURE_PRESERVE_SUBS,
                "Wildlife Area": WILDLIFE_AREA_SUBS,
                "Water Site": WATER_SITE_SUBS,
                "Campground": CAMPGROUND_SUBS,
                "Recreation Facility": RECREATION_FACILITY_SUBS,
                "Museum": MUSEUM_SUBS,
            }.get(cat)
            if valid_subs and sub not in valid_subs:
                errors.append(f"SUBTYPE VIOLATION: {sid} '{s['name']}' — category '{cat}' has invalid subtype '{sub}'")

def vocab_check_trails(trails):
    for t in trails:
        tid = t["trail_id"]
        for field, vocab, label in [
            ("use_type", TRAIL_USE_TYPES, "use_type"),
            ("surface_type", TRAIL_SURFACE_TYPES, "surface_type"),
            ("origin_type", TRAIL_ORIGIN_TYPES, "origin_type"),
            ("status", TRAIL_STATUS_VALUES, "status"),
        ]:
            val = t.get(field, "")
            if val and val not in vocab:
                errors.append(f"TRAIL VOCAB VIOLATION: {tid} — {label} '{val}' not in vocabulary")

def vocab_check_aps(aps):
    for ap in aps:
        aid = ap["access_point_id"]
        if ap["ap_type"] not in AP_TYPES:
            errors.append(f"AP VOCAB VIOLATION: {aid} — ap_type '{ap['ap_type']}' not in vocabulary")
        if ap["status"] and ap["status"] not in AP_STATUSES:
            errors.append(f"AP VOCAB VIOLATION: {aid} — status '{ap['status']}' not in vocabulary")

# ─────────────────────────────────────────────────────────────
# BUILD NORMALIZED OUTPUT ROWS
# ─────────────────────────────────────────────────────────────
SITES_OUT = []
TRAILS_OUT = []
APS_OUT = []
TRAIL_PARENTS_OUT = []
HELD_OUT = []

HELD_IDS = {"FUL-SI-003", "FUL-SI-006", "FUL-TR-005", "FUL-TR-007"}

def build_site_row(s):
    lat, lon, plus_code, conf = get_gps(s["gps_name"])
    features = map_features(s["features_raw"])
    counties = normalize_counties(s["counties_raw"])
    note_parts = []
    if s["notes_extra"]: note_parts.append(s["notes_extra"])
    gn = gps_note(conf, s["name"])
    if gn: note_parts.append(gn)
    notes = " ".join(note_parts)
    return {
        "site_id":         s["site_id"],
        "name":            clean(s["name"]),
        "category":        s["category"],
        "subtype":         s.get("subtype", ""),
        "designation":     clean(s.get("designation", "")),
        "status":          s.get("status", "Active"),
        "ownership":       clean(s.get("ownership", "")),
        "governance":      clean(s.get("governance", "")),
        "partner_agencies":clean(s.get("partner_agencies", "")),
        "coordination":    clean(s.get("coordination", "")),
        "description":     clean(s.get("description", "")),
        "location":        clean(s.get("location", "")),
        "acres":           fmt_acres(s.get("acres", "")),
        "counties":        counties,
        "municipality":    "",
        "township":        "",
        "gps_lat":         fmt_gps(lat),
        "gps_lon":         fmt_gps(lon),
        "plus_code":       plus_code,
        "features":        features,
        "notes":           clean(notes),
        "url_primary":     clean(s.get("url_primary", "")),
        "urls":            clean(s.get("urls_extra", "")),
        "parent_site_id":  s.get("parent_site_id", ""),
        "created_at":      RUN_TS,
        "updated_at":      RUN_TS,
        "features_raw":    clean(s.get("features_raw", "")),
    }

def build_trail_row(t):
    counties = normalize_counties(t["counties_raw"])
    return {
        "trail_id":        t["trail_id"],
        "name":            clean(t["name"]),
        "alternate_names": clean(t.get("alternate_names", "")),
        "use_type":        t.get("use_type", ""),
        "surface_type":    t.get("surface_type", ""),
        "origin_type":     t.get("origin_type", ""),
        "length_mi":       t.get("length_mi", ""),
        "counties":        counties,
        "governance":      clean(t.get("governance", "")),
        "partner_agencies":clean(t.get("partner_agencies", "")),
        "status":          t.get("status", "Active"),
        "difficulty":      t.get("difficulty", ""),
        "accessibility":   t.get("accessibility", ""),
        "description":     clean(t.get("description", "")),
        "trail_history":   clean(t.get("trail_history", "")),
        "identity_notes":  clean(t.get("identity_notes", "")),
        "notes":           clean(t.get("notes", "")),
        "url_primary":     clean(t.get("url_primary", "")),
        "maps":            clean(t.get("maps", "")),
        "created_at":      RUN_TS,
        "updated_at":      RUN_TS,
    }

def build_ap_row(ap):
    lat, lon, plus_code, conf = get_gps(ap.get("gps_name", ""))
    features = map_features(ap.get("features_raw", ""))
    note_parts = [ap.get("notes", "")]
    gn = gps_note(conf, ap["name"])
    if gn: note_parts.append(gn)
    notes = " ".join(p for p in note_parts if p)
    return {
        "access_point_id":  ap["access_point_id"],
        "name":             clean(ap["name"]),
        "ap_type":          ap["ap_type"],
        "status":           ap.get("status", "Active"),
        "parent_entity_type": ap.get("parent_entity_type", ""),
        "parent_entity_id":  ap.get("parent_entity_id", ""),
        "county":           ap.get("county", "Fulton"),
        "township":         "",
        "municipality":     "",
        "address":          clean(ap.get("address", "")),
        "gps_lat":          fmt_gps(lat),
        "gps_lon":          fmt_gps(lon),
        "plus_code":        plus_code,
        "features":         features,
        "identity_notes":   clean(ap.get("identity_notes", "")),
        "notes":            clean(notes),
        "url_primary":      clean(ap.get("url_primary", "")),
        "created_at":       RUN_TS,
        "updated_at":       RUN_TS,
    }

# Build rows
for s in SITES:
    row = build_site_row(s)
    SITES_OUT.append(row)
    if s["site_id"] in HELD_IDS:
        HELD_OUT.append(("Site", s["site_id"], s["name"], "cross-county or access unconfirmed — awaiting GIS resolution"))

for t in TRAILS:
    row = build_trail_row(t)
    TRAILS_OUT.append(row)
    if t["trail_id"] in HELD_IDS:
        HELD_OUT.append(("Trail", t["trail_id"], t["name"], t.get("notes", "")))
    # Trail parent relationship
    if t.get("parent_site_id"):
        TRAIL_PARENTS_OUT.append({
            "trail_id": t["trail_id"],
            "parent_site_id": t["parent_site_id"],
        })

for ap in ACCESS_POINTS:
    APS_OUT.append(build_ap_row(ap))

# ─────────────────────────────────────────────────────────────
# VOCABULARY VALIDATION GATE (Stage 4.5)
# ─────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("STAGE 4.5 — VOCABULARY VALIDATION GATE")
print("="*60)
vocab_check_sites(SITES)
vocab_check_trails(TRAILS)
vocab_check_aps(ACCESS_POINTS)

if errors:
    print("❌ VOCABULARY VIOLATIONS — PIPELINE HALTED:")
    for e in errors: print(f"  {e}")
    sys.exit(1)
else:
    print("✅ All vocabulary checks passed.")

# ─────────────────────────────────────────────────────────────
# TSV OUTPUT (Stage 4)
# ─────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("STAGE 4 — TSV OUTPUT")
print("="*60)

SITE_COLS  = ["name","category","subtype","designation","status","ownership","governance",
              "partner_agencies","coordination","description","location","acres","counties",
              "municipality","township","gps_lat","gps_lon","plus_code","features","notes",
              "url_primary","urls","parent_site_id","created_at","updated_at"]
TRAIL_COLS = ["Trail Name","Alternate Names","Trail Use Type","Trail Surface Type","Trail Origin Type",
              "Total Length (Miles)","Counties","Governance","Partner Agencies","Status","Difficulty",
              "Accessibility","Description","Trail History","Identity Notes","Notes","URL","Maps","Trail ID"]
TRAIL_KEYS = ["name","alternate_names","use_type","surface_type","origin_type","length_mi",
              "counties","governance","partner_agencies","status","difficulty","accessibility",
              "description","trail_history","identity_notes","notes","url_primary","maps","trail_id"]
AP_COLS    = ["Access Point Name","Access Point Type","Status","Identity Parent Entity Type",
              "Identity Parent Entity Name","County","Township","Municipality","Address",
              "GPS Lat","GPS Lon","Plus Code","Features","Identity Notes","Notes","URL","Access Point ID"]
AP_KEYS    = ["name","ap_type","status","parent_entity_type","parent_entity_id","county",
              "township","municipality","address","gps_lat","gps_lon","plus_code","features",
              "identity_notes","notes","url_primary","access_point_id"]

def write_tsv(path, cols, rows, key_map=None):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", quoting=csv.QUOTE_MINIMAL)
        w.writerow(cols)
        for r in rows:
            if key_map:
                w.writerow([clean(str(r.get(k, ""))) for k in key_map])
            else:
                w.writerow([clean(str(r.get(c, ""))) for c in cols])

sites_path   = os.path.join(OUTPUT_DIR, "fulton_oh_sites.tsv")
trails_path  = os.path.join(OUTPUT_DIR, "fulton_oh_trails.tsv")
segs_path    = os.path.join(OUTPUT_DIR, "fulton_oh_trail_segments.tsv")
tnets_path   = os.path.join(OUTPUT_DIR, "fulton_oh_trail_networks.tsv")
snets_path   = os.path.join(OUTPUT_DIR, "fulton_oh_site_networks.tsv")
aps_path     = os.path.join(OUTPUT_DIR, "fulton_oh_access_points.tsv")

write_tsv(sites_path, SITE_COLS, SITES_OUT)
write_tsv(trails_path, TRAIL_COLS, TRAILS_OUT, TRAIL_KEYS)

# Trail segments, trail networks, site networks — empty (no entities found)
for path, label in [(segs_path, "Trail Segments"), (tnets_path, "Trail Networks"), (snets_path, "Site Networks")]:
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Fulton County, OH — {label}\n# No entities found at discovery. 2026-04-13\n")
    print(f"  {path.split('/')[-1]}: 0 records (no entities)")

write_tsv(aps_path, AP_COLS, APS_OUT, AP_KEYS)

print(f"  {sites_path.split('/')[-1]}: {len(SITES_OUT)} sites")
print(f"  {trails_path.split('/')[-1]}: {len(TRAILS_OUT)} trails")
print(f"  {aps_path.split('/')[-1]}: {len(APS_OUT)} access points")

# ─────────────────────────────────────────────────────────────
# INTEGRITY CHECK (Stage 5)
# ─────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("STAGE 5 — TSV INTEGRITY CHECK")
print("="*60)

integ_errors = []

site_ids = {r["site_id"] for r in SITES_OUT}
trail_ids = {r["trail_id"] for r in TRAILS_OUT}
ap_ids   = {r["access_point_id"] for r in APS_OUT}

# Check trail parent refs
for tp in TRAIL_PARENTS_OUT:
    if tp["parent_site_id"] not in site_ids:
        integ_errors.append(f"TRAIL PARENT REF: {tp['trail_id']} → {tp['parent_site_id']} not in sites")

# Check AP parent refs
for ap in APS_OUT:
    pid = ap.get("parent_entity_id", "")
    ptype = ap.get("parent_entity_type", "")
    if pid:
        if ptype == "Trail" and pid not in trail_ids:
            # Check cross-county trails in DB
            conn = sqlite3.connect(PROD_DB)
            row = conn.execute("SELECT trail_id FROM trails WHERE trail_id=?", (pid,)).fetchone()
            conn.close()
            if not row:
                integ_errors.append(f"AP PARENT REF: {ap['access_point_id']} → Trail {pid} not found in trails or DB")

# Check required fields
for r in SITES_OUT:
    if not r["name"]:   integ_errors.append(f"MISSING NAME: {r['site_id']}")
    if not r["category"]: integ_errors.append(f"MISSING CATEGORY: {r['site_id']}")
for r in TRAILS_OUT:
    if not r["name"]:   integ_errors.append(f"MISSING NAME: {r['trail_id']}")

# Check for duplicate IDs
for id_set, label in [(site_ids,"sites"),(trail_ids,"trails"),(ap_ids,"access_points")]:
    pass  # sets eliminate duplicates; check via list instead
all_site_ids   = [r["site_id"]          for r in SITES_OUT]
all_trail_ids  = [r["trail_id"]         for r in TRAILS_OUT]
all_ap_ids     = [r["access_point_id"]  for r in APS_OUT]
for lst, label in [(all_site_ids,"sites"),(all_trail_ids,"trails"),(all_ap_ids,"access_points")]:
    if len(lst) != len(set(lst)):
        integ_errors.append(f"DUPLICATE IDs in {label}: {[x for x in lst if lst.count(x)>1]}")

# GPS coverage report
gps_sites    = sum(1 for r in SITES_OUT if r["gps_lat"])
nogps_sites  = [r["name"] for r in SITES_OUT if not r["gps_lat"]]
gps_trails   = sum(1 for r in TRAILS_OUT if True)  # trails don't carry GPS directly
gps_aps      = sum(1 for r in APS_OUT if r["gps_lat"])
print(f"  Sites with GPS: {gps_sites}/{len(SITES_OUT)}")
if nogps_sites:
    print(f"  Sites lacking GPS ({len(nogps_sites)}): {', '.join(nogps_sites)}")

if integ_errors:
    print("❌ INTEGRITY ERRORS:")
    for e in integ_errors: print(f"  {e}")
    sys.exit(1)
else:
    print("✅ Integrity check passed.")

# ─────────────────────────────────────────────────────────────
# DATABASE UPSERT (Stage 6)
# ─────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("STAGE 6 — DATABASE UPSERT")
print("="*60)

conn = sqlite3.connect(PROD_DB)
cur  = conn.cursor()
now  = RUN_TS

def upsert_site(r):
    cur.execute("""
        INSERT INTO sites
          (site_id,name,category,subtype,designation,status,ownership,governance,
           partner_agencies,coordination,description,location,acres,counties,
           municipality,township,gps_lat,gps_lon,plus_code,features,notes,
           url_primary,urls,parent_site_id,created_at,updated_at,features_raw)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT(site_id) DO UPDATE SET
          name=excluded.name, category=excluded.category, subtype=excluded.subtype,
          designation=excluded.designation, status=excluded.status,
          ownership=excluded.ownership, governance=excluded.governance,
          partner_agencies=excluded.partner_agencies, coordination=excluded.coordination,
          description=excluded.description, location=excluded.location,
          acres=excluded.acres, counties=excluded.counties,
          municipality=excluded.municipality, township=excluded.township,
          gps_lat=excluded.gps_lat, gps_lon=excluded.gps_lon,
          plus_code=excluded.plus_code, features=excluded.features,
          notes=excluded.notes, url_primary=excluded.url_primary,
          urls=excluded.urls, parent_site_id=excluded.parent_site_id,
          updated_at=excluded.updated_at, features_raw=excluded.features_raw
    """, (
        r["site_id"], r["name"], r["category"], r["subtype"], r["designation"],
        r["status"], r["ownership"], r["governance"], r["partner_agencies"],
        r["coordination"], r["description"], r["location"],
        float(r["acres"]) if r["acres"] else None,
        r["counties"], r["municipality"], r["township"],
        float(r["gps_lat"]) if r["gps_lat"] else None,
        float(r["gps_lon"]) if r["gps_lon"] else None,
        r["plus_code"], r["features"], r["notes"],
        r["url_primary"], r["urls"], r["parent_site_id"],
        r["created_at"], r["updated_at"], r["features_raw"],
    ))

def upsert_trail(r):
    cur.execute("""
        INSERT INTO trails
          (trail_id,name,alternate_names,use_type,surface_type,origin_type,
           length_mi,counties,governance,partner_agencies,status,difficulty,
           accessibility,description,trail_history,identity_notes,notes,
           url_primary,maps,created_at,updated_at)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT(trail_id) DO UPDATE SET
          name=excluded.name, alternate_names=excluded.alternate_names,
          use_type=excluded.use_type, surface_type=excluded.surface_type,
          origin_type=excluded.origin_type, length_mi=excluded.length_mi,
          counties=excluded.counties, governance=excluded.governance,
          partner_agencies=excluded.partner_agencies, status=excluded.status,
          difficulty=excluded.difficulty, accessibility=excluded.accessibility,
          description=excluded.description, trail_history=excluded.trail_history,
          identity_notes=excluded.identity_notes, notes=excluded.notes,
          url_primary=excluded.url_primary, maps=excluded.maps,
          updated_at=excluded.updated_at
    """, (
        r["trail_id"], r["name"], r["alternate_names"],
        r["use_type"], r["surface_type"], r["origin_type"],
        float(r["length_mi"]) if r["length_mi"] else None,
        r["counties"], r["governance"], r["partner_agencies"],
        r["status"], r["difficulty"], r["accessibility"],
        r["description"], r["trail_history"], r["identity_notes"],
        r["notes"], r["url_primary"], r["maps"],
        r["created_at"], r["updated_at"],
    ))

def upsert_trail_parent(tid, psid):
    cur.execute("""
        INSERT OR IGNORE INTO trail_parents (trail_id, parent_site_id)
        VALUES (?, ?)
    """, (tid, psid))

def upsert_ap(r):
    cur.execute("""
        INSERT INTO access_points
          (access_point_id,name,ap_type,status,parent_entity_type,parent_entity_id,
           county,township,municipality,address,gps_lat,gps_lon,plus_code,features,
           identity_notes,notes,url_primary,created_at,updated_at)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT(access_point_id) DO UPDATE SET
          name=excluded.name, ap_type=excluded.ap_type, status=excluded.status,
          parent_entity_type=excluded.parent_entity_type,
          parent_entity_id=excluded.parent_entity_id,
          county=excluded.county, township=excluded.township,
          municipality=excluded.municipality, address=excluded.address,
          gps_lat=excluded.gps_lat, gps_lon=excluded.gps_lon,
          plus_code=excluded.plus_code, features=excluded.features,
          identity_notes=excluded.identity_notes, notes=excluded.notes,
          url_primary=excluded.url_primary, updated_at=excluded.updated_at
    """, (
        r["access_point_id"], r["name"], r["ap_type"], r["status"],
        r["parent_entity_type"], r["parent_entity_id"],
        r["county"], r["township"], r["municipality"], r["address"],
        float(r["gps_lat"]) if r["gps_lat"] else None,
        float(r["gps_lon"]) if r["gps_lon"] else None,
        r["plus_code"], r["features"], r["identity_notes"], r["notes"],
        r["url_primary"], r["created_at"], r["updated_at"],
    ))

def upsert_ap_parent(ap_id, ptype, pid):
    cur.execute("""
        INSERT OR IGNORE INTO access_point_parents (access_point_id, parent_entity_type, parent_entity_id)
        VALUES (?, ?, ?)
    """, (ap_id, ptype, pid))

def upsert_held(etype, eid, ename, reason):
    cur.execute("""
        INSERT OR IGNORE INTO held_entities (record_id, entity_type, name, hold_reason, hold_detail, county, run_id, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (eid, etype, ename, "cross_county_or_access_unconfirmed", reason, "Fulton", RUN_ID, now))

def upsert_discovery_prov(eid, etype, tier):
    cur.execute("""
        INSERT OR IGNORE INTO discovery_provenance
          (entity_id, entity_type, county, discovery_tier, source_notes, run_id, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (eid, etype, "Fulton", tier, f"Fulton County pipeline run {RUN_ID}", RUN_ID, now))

# Upsert all
s_count = t_count = ap_count = 0
for r in SITES_OUT:
    upsert_site(r)
    upsert_discovery_prov(r["site_id"], "Site",
                          next(s["discovery_tier"] for s in SITES if s["site_id"]==r["site_id"]))
    s_count += 1

for r in TRAILS_OUT:
    upsert_trail(r)
    upsert_discovery_prov(r["trail_id"], "Trail",
                          next(t["discovery_tier"] for t in TRAILS if t["trail_id"]==r["trail_id"]))
    t_count += 1

for tp in TRAIL_PARENTS_OUT:
    upsert_trail_parent(tp["trail_id"], tp["parent_site_id"])

for r in APS_OUT:
    upsert_ap(r)
    upsert_discovery_prov(r["access_point_id"], "Access Point", 7)
    upsert_ap_parent(r["access_point_id"], r["parent_entity_type"], r["parent_entity_id"])
    ap_count += 1

# Write held entities
for etype, eid, ename, reason in HELD_OUT:
    upsert_held(etype, eid, ename, reason)

# Run metadata
cur.execute("""
    INSERT OR IGNORE INTO run_metadata (run_id, county, state, run_date, records_input, normalized, held, notes, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (RUN_ID, "Fulton", "OH", now[:10], s_count + t_count + ap_count, s_count + t_count + ap_count, len(HELD_OUT), "pipeline_version=5.2", now))

conn.commit()
conn.close()

print(f"  Upserted: {s_count} sites, {t_count} trails, {ap_count} access points")
print(f"  Held: {len(HELD_OUT)} entities flagged in held_entities table")

# ─────────────────────────────────────────────────────────────
# SUMMARY
# ─────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("FULTON COUNTY PIPELINE — COMPLETE")
print("="*60)
print(f"Run ID:        {RUN_ID}")
print(f"Run timestamp: {RUN_TS}")
print(f"Sites:         {s_count} (including {len([x for x in HELD_OUT if x[0]=='Site'])} held)")
print(f"Trails:        {t_count} (including {len([x for x in HELD_OUT if x[0]=='Trail'])} held)")
print(f"Access Points: {ap_count}")
print(f"Trail Segs:    0")
print(f"Trail Nets:    0")
print(f"Site Nets:     0")
print(f"\nOutput: {OUTPUT_DIR}")
print(f"DB: {PROD_DB}")
print("="*60)
