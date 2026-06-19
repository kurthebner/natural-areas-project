# =============================================================================
# SUPERSEDED — IMP-091 (2026-05-04)
# This monolithic pipeline script has been replaced by the parameterised model:
#   utilities/na_run_county.py + County_Spreadsheets/{County}/{county}_pipeline_config.json
# Do not use for new county runs. Kept for reference only.
# =============================================================================
"""
Wood County, Ohio — Natural Areas Pipeline v5.2
Resolution → Normalization → GPS → TSV Output → Vocabulary Gate → Integrity Check → DB Upsert
Run date: 2026-04-14
"""

import sys, os, csv, sqlite3, json, re
from datetime import datetime, timezone

NAP_ROOT = "/sessions/wonderful-confident-franklin/mnt/Natural Areas Project v5"
sys.path.insert(0, os.path.join(NAP_ROOT, "utilities"))
from na_plus_code import encode_plus_code

OUTPUT_DIR = os.path.join(NAP_ROOT, "County_Spreadsheets", "Wood")
PROD_DB    = os.path.join(NAP_ROOT, "NASqlite", "natural_areas_v5.db")
RUN_TS     = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
RUN_ID     = "wood_oh_2026_04_14"
PREFIX     = "WOD"

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
PARK_SUBTYPES            = {"Greenspace","Neighborhood Park","Linear Park","Dog Park",
                             "Playground Park","Sports Park","Waterfront Park","Civic Park","Historic Park"}
NATURE_PRESERVE_SUBS     = {"State Nature Preserve","Private Nature Preserve"}
WILDLIFE_AREA_SUBS       = {"State Wildlife Area","Federal Wildlife Area","Waterfowl Area",
                             "Migratory Bird Area","Wetland Management Area"}
WATER_SITE_SUBS          = {"Lake","Pond","Reservoir","River","Harbor","Marina",
                             "Boat Launch Area","Fishing Lake","Retention Pond"}
CAMPGROUND_SUBS          = {"Tent","RV","Primitive","Group","Cabin"}
RECREATION_FACILITY_SUBS = {"Sports Complex","Athletic Field","Skate Park","Swimming Pool",
                              "Recreation Center","Tennis Complex","Pickleball Complex",
                              "Golf Course","Disc Golf Course","Ice Rink","BMX Track","Pump Track"}
MUSEUM_SUBS              = {"Art Museum","Natural History Museum","History Museum",
                             "Science Museum","Children's Museum","Living Museum","Cultural Museum"}
HISTORIC_SITE_SUBS       = {"Historic Landmark","Archaeological Site","Historic Landscape",
                             "Battlefield","Historic Farmstead","Fortification","Industrial Site"}
NATURAL_AREA_SUBS        = {"Forest","Upland Forest","Floodplain Forest","Wetland","Prairie",
                             "Savanna","Meadow","Shrubland","Bog","Fen","Old-Growth Forest",
                             "Woodland","Riparian"}
CONSERVATION_AREA_SUBS   = {"Restoration Area","Habitat Management Area","Resource Protection Area",
                             "Watershed Protection Area","Forest Management Area"}
MEMORIAL_SUBS            = {"War Memorial","Veterans Memorial","Civic Memorial","Monument",
                             "Memorial Garden","Memorial Plaza"}
CULTURAL_FACILITY_SUBS   = {"Cultural Center","Performing Arts Center","Interpretive Center",
                             "Art Center","Visitor Center"}
OPEN_SPACE_SUBS          = {"Urban Open Space","Suburban Open Space","Greenbelt","Commons",
                             "Civic Lawn","Boulevard Median","Campus Open Space"}

TRAIL_USE_TYPES     = {"Multi-Use","Hiking","Bridle","Water","Bicycling","Mountain Bike",
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
# GPS TABLE
# ─────────────────────────────────────────────────────────────
GPS = {
    # Tier 2 — State
    "Mary Jane Thurston State Park":          (41.410280, -83.877780, "HIGH"),
    "Fort Meigs State Memorial":              (41.5720,   -83.6625,   "MED"),
    "Maumee River Weir Rapids Wildlife Area": (41.4020,   -83.8760,   "MED"),
    # Tier 4 — WCPD
    "Adam Phillips Pond":                     (41.3680,   -83.6247,   "MED"),
    "Wood County Museum":                     (41.3680,   -83.6247,   "MED"),
    "Bradner Preserve & Community Center":    (41.3338,   -83.4418,   "MED"),
    "Buttonwood/Betty C. Black Recreation Area": (41.5450, -83.5795,  "MED"),
    "Carter Historic Farm":                   (41.3707,   -83.6248,   "MED"),
    "J.C. Reuthinger Memorial Preserve":      (41.6105,   -83.6697,   "MED"),
    "Rudolph Bike Park":                      (41.4441,   -83.6968,   "MED"),
    "Sawyer Quarry Nature Preserve":          (41.6382,   -83.6453,   "MED"),
    "W.W. Knight Nature Preserve":            (41.6218,   -83.6570,   "MED"),
    "William Henry Harrison Park":            (41.4107,   -83.4573,   "MED"),
    # Tier 6 — Bowling Green
    "City Park":                              (41.3820,   -83.6513,   "MED"),
    "Carter Park":                            (41.3707,   -83.6248,   "MED"),
    "Simpson Garden Park":                    (41.3739,   -83.6513,   "MED"),
    "Wintergarden/St. John's Nature Preserve":(41.3720,   -83.6680,   "MED"),
    # Tier 6 — Perrysburg
    "Municipal Park":                         (41.5647,   -83.6317,   "MED"),
    "J.C. Reuthinger":                        (41.6105,   -83.6697,   "MED"),
    # Tier 8 — Private
    "577 Foundation":                         (41.5540,   -83.6218,   "MED"),
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
# FEATURES MAPPER
# ─────────────────────────────────────────────────────────────
FEATURE_MAP = [
    (r'hiking trail|walking trail|walking path|winding trail|nature trail|loop trail|trail system|interpretive trail|self.guided interpretive', "Hiking Trail"),
    (r'boardwalk',                   "Boardwalk"),
    (r'interpretive trail|self.guided interpretive', "Interpretive Sign"),
    (r'storyWalk|story walk',        "Interpretive Sign"),
    (r'bridle trail|equestrian',     "Bridle Trail"),
    (r'boat ramp|launch ramp',       "Boat Ramp"),
    (r'boat launch|watercraft|canoe|kayak', "Watercraft Access"),
    (r'boat dock',                   "Boat Dock"),
    (r'fishing pond|fishing lake|stocked.*pond|stocked.*fish', "Fishing Area"),
    (r'fishing pond|1\.5.acre pond', "Pond"),
    (r'swimming beach|swim beach',   "Swimming Beach"),
    (r'swimming pool|city pool',     "Swimming Pool"),
    (r'splash pad|spray pad',        "Spray Park"),
    (r'pavilion|shelter house|open air pavilion|rentable.*shelter|covered seating|community room', "Pavilion"),
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
    (r'pump track|strider bike',     "Pump Track"),
    (r'rock climbing|bouldering|rappelling', "Climbing Structure"),
    (r'astronomical telescope|observatory', "Observatory"),
    (r'greenhouse|native plant nursery', "Greenhouse"),
    (r'bird blind|wildlife observation|wildlife viewing|bird watching|bird watch', "Wildlife Observation Area"),
    (r'playground|play equipment',   "Playground"),
    (r'sledding hill',               "Sledding Hill"),
    (r'horseshoe',                   "Horseshoe Pitch"),
    (r'archery',                     "Archery Range"),
    (r'ropes course|high ropes',     "Ropes Course"),
    (r'shooting',                    "Shooting Range"),
    (r'dog park',                    "Dog Park"),
    (r'restroom|flush toilet|portable toilet|bathroom', "Restrooms"),
    (r'parking',                     "Parking Lot"),
    (r'kiosk|information kiosk',     "Kiosk"),
    (r'camping|campsite',            "Camping"),
    (r'cabin|camper cabin',          "Cabin Rentals"),
    (r'ADA.compliant|ADA accessible|wheelchair', "ADA Accessible"),
    (r'observation deck|scenic overlook|overlook', "Observation Deck"),
    (r'vernal pool',                 "Vernal Pool"),
    (r'hunting|public hunting|hunting by permit', "Hunting Area"),
    (r'fossil',                      "Interpretive Sign"),
    (r'native plant|native prairie|prairie restoration|pollinator garden|butterfly garden', "Pollinator Garden"),
    (r'community garden|children.s garden', "Community Garden"),
    (r'war memorial|memorial statue|monument|veterans.*memorial', "Monument"),
    (r'historic.*cabin|log cabin|historic.*building|historic.*lodge|historic structure', "Historic Structure"),
    (r'marina',                      "Marina"),
    (r'exercise station|exercise course', "Fitness Station"),
    (r'nature center',               "Nature Center"),
    (r'museum',                      "Interpretive Sign"),
    (r'educational program|guided tour', "Interpretive Sign"),
    (r'sand dune',                   "Interpretive Sign"),
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

def gps_note(conf, name):
    if conf == "HIGH": return ""
    if conf == "MED":  return "GPS from address geocode — verify precision."
    if conf == "LOW":  return "GPS approximate — centroid-level; needs field verification."
    return f"GPS needed — {name} location unconfirmed."

# ─────────────────────────────────────────────────────────────
# ENTITY DEFINITIONS
# ─────────────────────────────────────────────────────────────

SITES = [
  # ── TIER 2 — STATE ──────────────────────────────────────────
  {
    "site_id": "WOD-SI-001", "name": "Mary Jane Thurston State Park",
    "category": "Park", "subtype": "Waterfront Park", "designation": "State Park",
    "status": "Active", "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Parks and Watercraft",
    "partner_agencies": "", "coordination": "",
    "description": "105-acre Maumee River access state park with camping, trails, Miami and Erie Canal remnants, and disc golf. Shared with Henry County. Primary access from Wood County side.",
    "location": "24698 State Route 65, Grand Rapids, OH 43522", "acres": "105",
    "counties_raw": ["Wood", "Henry"], "gps_name": "Mary Jane Thurston State Park",
    "features_raw": "39 campsites (16 tent, 23 electric), day lodge (50 capacity), boat launch, marina, disc golf, hiking trails, 6 miles of trails, accessible campsites",
    "notes_extra": "Cross-county entity — Wood and Henry counties. Primary access from Wood County side. Baseline seed.",
    "url_primary": "https://parks.ohiodnr.gov/parks/details/mary-jane-thurston-state-park",
    "urls_extra": "", "parent_site_id": "", "discovery_tier": 2,
  },
  {
    "site_id": "WOD-SI-002", "name": "Fort Meigs State Memorial",
    "category": "Historic Site", "subtype": "Battlefield", "designation": "State Memorial",
    "status": "Active", "ownership": "State of Ohio",
    "governance": "Ohio History Connection",
    "partner_agencies": "", "coordination": "",
    "description": "Reconstructed War of 1812 fort and National Historic Landmark on the Maumee River. 65-acre site with museum, visitor center, and educational programs.",
    "location": "29100 West River Road, Perrysburg, OH 43551", "acres": "65",
    "counties_raw": ["Wood"], "gps_name": "Fort Meigs State Memorial",
    "features_raw": "Museum, Visitor Center, reconstructed fort (10 acres), historic battlefield, guided tours, educational programs, reenactments, accessible facilities",
    "notes_extra": "Baseline seeds 'Fort Meigs' and 'Fort Meigs State Memorial' resolved to this entity — same site. National Historic Landmark. Baseline seed confirmed.",
    "url_primary": "https://fortmeigs.org",
    "urls_extra": "https://www.ohiohistory.org/visit/museum-and-site-locator/fort-meigs/",
    "parent_site_id": "", "discovery_tier": 2,
  },
  {
    "site_id": "WOD-SI-003", "name": "Wood County Wildlife Area 1",
    "category": "Wildlife Area", "subtype": "State Wildlife Area", "designation": "State Wildlife Area",
    "status": "Active", "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Wildlife",
    "partner_agencies": "", "coordination": "",
    "description": "Small ODNR wildlife area managed for wildlife habitat and public hunting access. Exact location via ODNR map.",
    "location": "", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hunting area, wildlife viewing, wetlands, woodlands",
    "notes_extra": "ODNR DOW numbered wildlife area. Location not disclosed publicly. Baseline seed.",
    "url_primary": "https://wildohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 2,
  },
  {
    "site_id": "WOD-SI-004", "name": "Wood County Wildlife Area 2",
    "category": "Wildlife Area", "subtype": "State Wildlife Area", "designation": "State Wildlife Area",
    "status": "Active", "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Wildlife",
    "partner_agencies": "", "coordination": "",
    "description": "Small ODNR wildlife area managed for wildlife habitat and public hunting access.",
    "location": "", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hunting area, wildlife viewing, wetlands, woodlands",
    "notes_extra": "ODNR DOW numbered wildlife area. Baseline seed.",
    "url_primary": "https://wildohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 2,
  },
  {
    "site_id": "WOD-SI-005", "name": "Wood County Wildlife Area 4",
    "category": "Wildlife Area", "subtype": "State Wildlife Area", "designation": "State Wildlife Area",
    "status": "Active", "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Wildlife",
    "partner_agencies": "", "coordination": "",
    "description": "Small ODNR wildlife area managed for wildlife habitat and public hunting access. No WCA 3 exists in Wood County.",
    "location": "", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hunting area, wildlife viewing, wetlands, woodlands",
    "notes_extra": "No WCA 3 in Wood County. Baseline seed.",
    "url_primary": "https://wildohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 2,
  },
  {
    "site_id": "WOD-SI-006", "name": "Wood County Wildlife Area 5",
    "category": "Wildlife Area", "subtype": "State Wildlife Area", "designation": "State Wildlife Area",
    "status": "Active", "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Wildlife",
    "partner_agencies": "", "coordination": "",
    "description": "Small ODNR wildlife area managed for wildlife habitat and public hunting access. New controlled hunting designation for 2025.",
    "location": "", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hunting area, wildlife viewing, wetlands, woodlands",
    "notes_extra": "New for 2025 controlled hunting per ODNR records. Baseline seed.",
    "url_primary": "https://wildohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 2,
  },
  {
    "site_id": "WOD-SI-007", "name": "Wood County Wildlife Area 6",
    "category": "Wildlife Area", "subtype": "State Wildlife Area", "designation": "State Wildlife Area",
    "status": "Active", "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Wildlife",
    "partner_agencies": "", "coordination": "",
    "description": "Small ODNR wildlife area managed for wildlife habitat and public hunting access.",
    "location": "", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hunting area, wildlife viewing, wetlands, woodlands",
    "notes_extra": "ODNR DOW numbered wildlife area. Baseline seed.",
    "url_primary": "https://wildohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 2,
  },
  {
    "site_id": "WOD-SI-008", "name": "Wood County Wildlife Area 7",
    "category": "Wildlife Area", "subtype": "State Wildlife Area", "designation": "State Wildlife Area",
    "status": "Active", "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Wildlife",
    "partner_agencies": "", "coordination": "",
    "description": "Small ODNR wildlife area managed for wildlife habitat and public hunting access.",
    "location": "", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hunting area, wildlife viewing, wetlands, woodlands",
    "notes_extra": "ODNR DOW numbered wildlife area. Baseline seed.",
    "url_primary": "https://wildohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 2,
  },
  {
    "site_id": "WOD-SI-009", "name": "Wood County Wildlife Area 8",
    "category": "Wildlife Area", "subtype": "State Wildlife Area", "designation": "State Wildlife Area",
    "status": "Active", "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Wildlife",
    "partner_agencies": "", "coordination": "",
    "description": "Small ODNR wildlife area managed for wildlife habitat and public hunting access.",
    "location": "", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hunting area, wildlife viewing, wetlands, woodlands",
    "notes_extra": "ODNR DOW numbered wildlife area. Baseline seed.",
    "url_primary": "https://wildohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 2,
  },
  {
    "site_id": "WOD-SI-010", "name": "Wood County Wildlife Area 9",
    "category": "Wildlife Area", "subtype": "State Wildlife Area", "designation": "State Wildlife Area",
    "status": "Active", "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Wildlife",
    "partner_agencies": "", "coordination": "",
    "description": "Small ODNR wildlife area managed for wildlife habitat and public hunting access.",
    "location": "", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hunting area, wildlife viewing, wetlands, woodlands",
    "notes_extra": "ODNR DOW numbered wildlife area. Baseline seed.",
    "url_primary": "https://wildohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 2,
  },
  {
    "site_id": "WOD-SI-011", "name": "Wood County Wildlife Area 10",
    "category": "Wildlife Area", "subtype": "State Wildlife Area", "designation": "State Wildlife Area",
    "status": "Active", "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Wildlife",
    "partner_agencies": "", "coordination": "",
    "description": "Small ODNR wildlife area managed for wildlife habitat and public hunting access. Map available online.",
    "location": "", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hunting area, wildlife viewing, wetlands, woodlands",
    "notes_extra": "ODNR DOW numbered wildlife area. Map available on ODNR site. Baseline seed.",
    "url_primary": "https://wildohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 2,
  },
  {
    "site_id": "WOD-SI-012", "name": "Bairdstown Wildlife Production Area",
    "category": "Wildlife Area", "subtype": "State Wildlife Area", "designation": "State Wildlife Area",
    "status": "Active", "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Wildlife",
    "partner_agencies": "", "coordination": "",
    "description": "Wildlife production area managed for wildlife habitat. Roadside viewing only — no public hunting access.",
    "location": "", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Wildlife viewing, roadside viewing only",
    "notes_extra": "NEW DISCOVERY. Roadside-viewing-only wildlife production area. Not a hunting area. Near Bairdstown community.",
    "url_primary": "https://wildohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 2,
  },
  {
    "site_id": "WOD-SI-013", "name": "Dry Creek Wildlife Area",
    "category": "Wildlife Area", "subtype": "State Wildlife Area", "designation": "State Wildlife Area",
    "status": "Active", "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Wildlife",
    "partner_agencies": "", "coordination": "",
    "description": "Small ODNR wildlife area near US-24 corridor. Approximately 2.34 acres.",
    "location": "Near US-24 and Township Road 6C, Wood County, OH", "acres": "2.34",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Wildlife area, hunting",
    "notes_extra": "Approximately 2.34 acres per ODNR records. Very small parcel. Baseline seed.",
    "url_primary": "https://wildohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 2,
  },
  {
    "site_id": "WOD-SI-014", "name": "Maumee River Weir Rapids Wildlife Area",
    "category": "Wildlife Area", "subtype": "State Wildlife Area", "designation": "State Wildlife Area",
    "status": "Active", "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Wildlife",
    "partner_agencies": "", "coordination": "",
    "description": "ODNR wildlife area along Maumee River providing fishing and wildlife viewing access at the weir rapids.",
    "location": "13827 S River Road, Grand Rapids, OH 43522", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "Maumee River Weir Rapids Wildlife Area",
    "features_raw": "Fishing, wildlife viewing, river access, boat launch",
    "notes_extra": "Addressed at 13827 S River Rd, Grand Rapids. Maumee River at weir rapids. Distinct from WCPD Otsego Park nearby. Baseline seed.",
    "url_primary": "https://wildohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 2,
  },
  {
    "site_id": "WOD-SI-015", "name": "Van Tassel Wildlife Area",
    "category": "Wildlife Area", "subtype": "State Wildlife Area", "designation": "State Wildlife Area",
    "status": "Active", "ownership": "State of Ohio",
    "governance": "Ohio Department of Natural Resources, Division of Wildlife",
    "partner_agencies": "", "coordination": "",
    "description": "ODNR wildlife area providing Maumee River access only — no developed facilities.",
    "location": "", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "River access, wildlife viewing",
    "notes_extra": "NEW DISCOVERY — not in AutoRecovered baseline. River access only per ODNR records.",
    "url_primary": "https://wildohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 2,
  },
  # ── TIER 4 — COUNTY (WCPD) ──────────────────────────────────
  {
    "site_id": "WOD-SI-016", "name": "Adam Phillips Pond",
    "category": "Fishing Area", "subtype": "", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "Fishing pond created as borrow pit during I-75 construction. Stocked for public fishing. Open March through October. Co-located with Wood County Museum on historic County Home complex grounds.",
    "location": "13660 County Home Road, Bowling Green, OH 43402", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "Adam Phillips Pond",
    "features_raw": "Stocked fishing pond, parking, ADA accessible fishing",
    "notes_extra": "NEW DISCOVERY. Stocked public fishing pond. Co-located with Wood County Museum at 13660 County Home Rd — two distinct entities.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-017", "name": "Arrowwood Archery Range",
    "category": "Recreation Facility", "subtype": "", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "WCPD archery range facility at 11126 Linwood Road, Bowling Green.",
    "location": "11126 Linwood Road, Bowling Green, OH 43402", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Archery range, shooting range",
    "notes_extra": "NEW DISCOVERY — not in AutoRecovered baseline. Found on current WCPD website.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-018", "name": "Baldwin Woods Preserve",
    "category": "Nature Preserve", "subtype": "", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "Mature woodlot preserve at Range Line and Euler Roads. 126 acres with hunting by permit program.",
    "location": "Range Line and Euler Roads, Bowling Green, OH 43402", "acres": "126",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hunting by permit, hiking trails, woodlands, wetlands, grasslands",
    "notes_extra": "NEW DISCOVERY — not in AutoRecovered baseline.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-019", "name": "Beaver Creek Preserve",
    "category": "Nature Preserve", "subtype": "", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "Natural preserve along Beaver Creek with hiking and nature study opportunities.",
    "location": "", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hiking, nature study, wetlands, creek",
    "notes_extra": "NEW DISCOVERY. Exact address not confirmed at time of discovery — GPS acquisition needed.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-020", "name": "Black Swamp Preserve",
    "category": "Nature Preserve", "subtype": "", "designation": "",
    "status": "Active", "ownership": "Wood County (partial)",
    "governance": "Wood County Park District",
    "partner_agencies": "City of Bowling Green; Black Swamp Conservancy",
    "coordination": "Tri-party governance: WCPD manages park portion, City of BG has municipal interest, BSC holds conservation interest",
    "description": "Major public preserve with connection to Slippery Elm Trail. 116 bird species recorded. Tri-party managed property on E. Gypsy Lane Road.",
    "location": "E. Gypsy Lane Road, Bowling Green, OH 43402", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hiking trails, bird watching, wildlife viewing, Slippery Elm Trail connection, wetlands, woodlands",
    "notes_extra": "IDENTITY RESOLUTION: Three AutoRecovered records (WCPD, City BG, BSC) describe same physical property. WCPD record is primary. City of BG and BSC interests noted as partners/coordination. Tri-party governance confirmed.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-021", "name": "Bradner Preserve & Community Center",
    "category": "Nature Preserve", "subtype": "", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "WCPD's largest property at 233 acres featuring mature woodlot, sand dunes, grasslands, and remnant prairie. Includes interpretive center and community facilities at 11491 Fostoria Road, Bradner.",
    "location": "11491 Fostoria Road (State Route 23), Bradner, OH 43406", "acres": "233",
    "counties_raw": ["Wood"], "gps_name": "Bradner Preserve & Community Center",
    "features_raw": "Interpretive center, indoor/outdoor rentable shelter, community room, 2.38 miles of hiking trails, sand dunes, grasslands, remnant prairie, mature woodlot, educational programs, nature study",
    "notes_extra": "NEW DISCOVERY — not in AutoRecovered baseline. WCPD's largest property. 233 acres.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-022", "name": "Buttonwood/Betty C. Black Recreation Area",
    "category": "Park", "subtype": "Waterfront Park", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "Premier walleye fishing spot on the Maumee River at 27174 Hull Prairie Road, Perrysburg. Approximately 65% of Maumee River walleye are caught near this location. Boat launch and Maumee River Trail access. 27 acres.",
    "location": "27174 Hull Prairie Road, Perrysburg, OH 43551", "acres": "27",
    "counties_raw": ["Wood"], "gps_name": "Buttonwood/Betty C. Black Recreation Area",
    "features_raw": "Boat launch, watercraft access, fishing, Maumee River Trail access, parking",
    "notes_extra": "Baseline seed 'Buttonwood Access' confirmed as this entity — officially named Buttonwood/Betty C. Black Recreation Area.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-023", "name": "Carter Historic Farm",
    "category": "Historic Site", "subtype": "", "designation": "",
    "status": "Active", "ownership": "Wood County (partial)",
    "governance": "Wood County Park District",
    "partner_agencies": "City of Bowling Green",
    "coordination": "Joint facility — WCPD manages historic farm side, City of Bowling Green manages recreation side",
    "description": "Historic farm donated by Loomis family, originally purchased by Carter family in 1901. WCPD manages historic farm buildings and agricultural programs at 18331 Carter Road.",
    "location": "18331 Carter Road, Bowling Green, OH 43402", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "Carter Historic Farm",
    "features_raw": "Loomis Community Room, historic farm buildings, agricultural programs, farm tours, educational programs, guided tours",
    "notes_extra": "NEW DISCOVERY. Co-located with City of BG Carter Park at 18331 Carter Rd. Two distinct entities — do not merge. WCPD manages historic farm; City BG manages recreation (WOD-SI-040).",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-024", "name": "Cedar Creeks Preserve",
    "category": "Nature Preserve", "subtype": "", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "Natural preserve along Cedar Creek corridor with hiking and picnicking.",
    "location": "", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hiking, rentable picnic shelter, wetlands, creeks",
    "notes_extra": "NEW DISCOVERY. Exact address not confirmed at time of discovery.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-025", "name": "Cricket Frog Cove",
    "category": "Conservation Area", "subtype": "", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "160-acre wildlife habitat preserve with hunting by permit. Located 0.5 mile from Freyman Road access, Henry Township.",
    "location": "Freyman Road, Henry Township, Wood County, OH", "acres": "160",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hunting by permit, hiking trails, parking, wildlife viewing, wetlands",
    "notes_extra": "NEW DISCOVERY — not in AutoRecovered baseline. 160 acres.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-026", "name": "Fuller Preserve",
    "category": "Conservation Area", "subtype": "", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "Undeveloped natural area near Weston. Donated to Brown University then transferred to WCPD. Stand of trees over a century old. Intentionally undeveloped; hunting permitted.",
    "location": "Near Weston, Wood County, OH", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hunting, hiking, old-growth forest, grasslands, wetlands",
    "notes_extra": "NEW DISCOVERY. Intentionally undeveloped per WCPD — no facilities. Near Weston.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-027", "name": "J.C. Reuthinger Memorial Preserve",
    "category": "Conservation Area", "subtype": "", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "Home to WCPD native plant nursery, greenhouse, and Stewardship Department at 30730 Oregon Road, Perrysburg. Grows 12,000–15,000 native plants annually for use across WCPD properties. 69 acres.",
    "location": "30730 Oregon Road, Perrysburg, OH 43551", "acres": "69",
    "counties_raw": ["Wood"], "gps_name": "J.C. Reuthinger Memorial Preserve",
    "features_raw": "Native plant nursery, greenhouse, stewardship offices, hiking, educational programs, native plant programs",
    "notes_extra": "NEW DISCOVERY. Primary function is WCPD nursery and stewardship operations. Some public access for educational programs.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-028", "name": "Nature Trails Park (WCPD)",
    "category": "Nature Preserve", "subtype": "", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "Mix of woodlands, grasslands, and wetlands behind Wood County Justice Center Complex. No established trails — visitors roam at will. Features astronomical observation program with large telescope.",
    "location": "Gypsy Lane Road behind Wood County Justice Center Complex, Bowling Green, OH 43402", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hiking (unestablished), wildlife viewing, astronomy program, astronomical telescope, woodlands, grasslands, wetlands, hunting (seasonal)",
    "notes_extra": "HELD — VERIFICATION FLAG. In AutoRecovered baseline but NOT found on current WCPD website at time of discovery. May have been removed, renamed, or decommissioned. Status must be confirmed before production upsert.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-029", "name": "Otsego Park",
    "category": "Park", "subtype": "Historic Park", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "Historic stone lodge overlooking Maumee River. Formerly Grand View Park private resort. Includes boat launch and Maumee River Trail access.",
    "location": "", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Historic stone lodge (rentable), boat launch, watercraft access, Maumee River Trail access, hiking, picnicking, Maumee River",
    "notes_extra": "Baseline seed confirmed. Historic park — formerly private Grand View Park resort. Stone lodge is a significant historic structure. GPS acquisition needed.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-030", "name": "Rudolph Bike Park",
    "category": "Recreation Facility", "subtype": "Pump Track", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "Pump track and strider bike track facility on Rudolph Road. 1,783 ft continuous pump track and 159 ft strider bike track.",
    "location": "Rudolph Road, 0.5 mile N. of Mermill Road, Rudolph, OH", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "Rudolph Bike Park",
    "features_raw": "1783 ft pump track, 159 ft strider bike track, cycling, BMX",
    "notes_extra": "NEW DISCOVERY — not in AutoRecovered baseline.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-031", "name": "Rudolph Savanna",
    "category": "Natural Area", "subtype": "Savanna", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "Natural savanna habitat near Rudolph featuring native wildflowers, tall prairie grasses, and sand dunes representative of the Black Swamp heritage landscape.",
    "location": "Near Rudolph, Wood County, OH", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hiking trails, restrooms, trailhead, sand dunes, prairie grasses, wildflowers, nature study",
    "notes_extra": "NEW DISCOVERY — not in AutoRecovered baseline.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-032", "name": "Sawyer Quarry Nature Preserve",
    "category": "Nature Preserve", "subtype": "", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "Former limestone quarry donated in 2014 at 26940 Lime City Road, Perrysburg. Developed for rock climbing, rappelling, bouldering, and hiking. Houses WCPD Program Naturalist offices.",
    "location": "26940 Lime City Road, Perrysburg, OH 43551", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "Sawyer Quarry Nature Preserve",
    "features_raw": "Rock climbing, bouldering, rappelling, hiking trails, ropes course, check-in kiosk, accessible parking, program offices",
    "notes_extra": "NEW DISCOVERY. Former quarry — unique rock formation habitat. Climbing activities require registration. GPS from address geocode.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-033", "name": "W.W. Knight Nature Preserve",
    "category": "Nature Preserve", "subtype": "", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "Nature center property at 29530 White Road, Perrysburg donated by Knight family. Features LOONA boardwalk, 1.5-acre fishing pond, wetlands, remnant swamp woods, and native prairie. 44 acres with 6 miles of trails.",
    "location": "29530 White Road, Perrysburg, OH 43551", "acres": "44",
    "counties_raw": ["Wood"], "gps_name": "W.W. Knight Nature Preserve",
    "features_raw": "Nature center (10000 sq ft), Hankison Great Room (rentable), boardwalk, 1.5-acre fishing pond, parking, wetlands, remnant swamp woods, native prairie, 6 miles hiking trails, bird watching, educational programs, ADA accessible boardwalk",
    "notes_extra": "NEW DISCOVERY — not in AutoRecovered baseline. 44 acres. Nature center 10,000 sq ft.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-034", "name": "Wakeman Preserve",
    "category": "Nature Preserve", "subtype": "", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "Undeveloped natural area managed by Wood County Park District.",
    "location": "", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hiking, nature study, natural habitat",
    "notes_extra": "HELD — VERIFICATION FLAG. In AutoRecovered baseline but NOT found on current WCPD website. May have been removed, renamed, or merged. Confirm status before production upsert.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-035", "name": "White Star Park",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "WCPD park with recreational and natural habitat features.",
    "location": "", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hiking, recreation, natural habitat",
    "notes_extra": "HELD — VERIFICATION FLAG. In AutoRecovered baseline but NOT found on current WCPD website. May have been removed, renamed, or decommissioned. Confirm status before production upsert.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-036", "name": "William Henry Harrison Park",
    "category": "Park", "subtype": "Waterfront Park", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "22-acre WCPD park in Pemberville along the Portage River. Serves as a Portage River Water Trail launch point. At 644 Bierley Avenue.",
    "location": "644 Bierley Avenue, Pemberville, OH 43450", "acres": "22",
    "counties_raw": ["Wood"], "gps_name": "William Henry Harrison Park",
    "features_raw": "Boat launch, watercraft access, Portage River Water Trail access, restrooms, fishing, hiking, Portage River",
    "notes_extra": "NEW DISCOVERY. Portage River Water Trail trailhead. Distinct from Pemberville's own Memorial Park.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "site_id": "WOD-SI-037", "name": "Wood County Museum",
    "category": "Museum", "subtype": "History Museum", "designation": "",
    "status": "Active", "ownership": "Wood County",
    "governance": "Wood County Park District",
    "partner_agencies": "", "coordination": "",
    "description": "Wood County Museum on 51-acre historic County Home complex grounds managed by WCPD. The County Home complex historically housed the county infirmary.",
    "location": "13660 County Home Road, Bowling Green, OH 43402", "acres": "51",
    "counties_raw": ["Wood"], "gps_name": "Wood County Museum",
    "features_raw": "Museum, historic buildings, educational programs, historic site, parking",
    "notes_extra": "NEW DISCOVERY. IMP-068 name-pattern match: 'Museum' → category 'Museum'. Co-located with Adam Phillips Pond at 13660 County Home Rd — two distinct entities.",
    "url_primary": "https://wcparks.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 4,
  },
  # ── TIER 6 — BOWLING GREEN ──────────────────────────────────
  {
    "site_id": "WOD-SI-038", "name": "City Park",
    "category": "Park", "subtype": "Sports Park", "designation": "",
    "status": "Active", "ownership": "City of Bowling Green",
    "governance": "City of Bowling Green Parks & Recreation",
    "partner_agencies": "", "coordination": "",
    "description": "Flagship city park at 520 Conneaut Avenue with pool complex, baseball, skatepark, and 0.5-mile walking loop.",
    "location": "520 Conneaut Avenue, Bowling Green, OH 43402", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "City Park",
    "features_raw": "Swimming pool complex, baseball fields, skate park, 0.5-mile walking loop, parking, ADA accessible pool",
    "notes_extra": "NEW DISCOVERY. Bowling Green flagship city park.",
    "url_primary": "https://bgohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-039", "name": "Bellard Park",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "City of Bowling Green",
    "governance": "City of Bowling Green Parks & Recreation",
    "partner_agencies": "", "coordination": "",
    "description": "Small park at Kenwood Avenue and Sand Ridge Road featuring butterfly garden and walking trails.",
    "location": "Kenwood Avenue and Sand Ridge Road, Bowling Green, OH 43402", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Butterfly garden, walking trails, pollinator garden",
    "notes_extra": "NEW DISCOVERY.",
    "url_primary": "https://bgohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-040", "name": "Carter Park",
    "category": "Recreation Facility", "subtype": "Sports Complex", "designation": "",
    "status": "Active", "ownership": "City of Bowling Green",
    "governance": "City of Bowling Green Parks & Recreation",
    "partner_agencies": "Wood County Park District",
    "coordination": "Joint facility — City of BG manages recreation side, WCPD manages historic farm side",
    "description": "City of Bowling Green recreation facility at 18331 Carter Road. Includes 8 ball diamonds, disc golf, volleyball, shelters, and playgrounds.",
    "location": "18331 Carter Road, Bowling Green, OH 43402", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "Carter Park",
    "features_raw": "Baseball diamonds (8), disc golf course, volleyball courts (3), shelters, playgrounds, parking",
    "notes_extra": "Co-located with WCPD Carter Historic Farm at 18331 Carter Rd. Two distinct entities — do not merge. City BG manages recreation (this record); WCPD manages historic farm (WOD-SI-023).",
    "url_primary": "https://bgohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-041", "name": "Wintergarden/St. John's Nature Preserve",
    "category": "Nature Preserve", "subtype": "", "designation": "",
    "status": "Active", "ownership": "City of Bowling Green",
    "governance": "City of Bowling Green Parks & Recreation",
    "partner_agencies": "", "coordination": "",
    "description": "Municipal nature preserve at 615 S. Wintergarden Road with 168 bird species recorded.",
    "location": "615 S. Wintergarden Road, Bowling Green, OH 43402", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "Wintergarden/St. John's Nature Preserve",
    "features_raw": "Hiking trails, bird watching, wildlife viewing, 168 bird species",
    "notes_extra": "Baseline seed 'Saint Johns Woods' resolved to this entity. Confirm identity match. 168 bird species recorded.",
    "url_primary": "https://bgohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-042", "name": "Simpson Garden Park",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "City of Bowling Green",
    "governance": "City of Bowling Green Parks & Recreation",
    "partner_agencies": "", "coordination": "",
    "description": "Downtown garden park at 192 S. Main Street in central Bowling Green.",
    "location": "192 S. Main Street, Bowling Green, OH 43402", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "Simpson Garden Park",
    "features_raw": "Gardens, benches, walking, urban garden",
    "notes_extra": "NEW DISCOVERY.",
    "url_primary": "https://bgohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-043", "name": "Conneaut Park Sledding Hill",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "City of Bowling Green",
    "governance": "City of Bowling Green Parks & Recreation",
    "partner_agencies": "", "coordination": "",
    "description": "Former reservoir site at Conneaut Avenue and Haskins Road converted to sledding hill. Seasonal winter recreation.",
    "location": "Conneaut Avenue and Haskins Road, Bowling Green, OH 43402", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Sledding hill, seasonal recreation",
    "notes_extra": "NEW DISCOVERY. Former municipal reservoir site. Seasonal winter use.",
    "url_primary": "https://bgohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-044", "name": "Dunbridge Road Soccer Fields",
    "category": "Recreation Facility", "subtype": "Athletic Field", "designation": "",
    "status": "Active", "ownership": "City of Bowling Green",
    "governance": "City of Bowling Green Parks & Recreation",
    "partner_agencies": "", "coordination": "",
    "description": "Municipal soccer field complex behind Municipal Court, Bowling Green.",
    "location": "Behind Municipal Court, Bowling Green, OH 43402", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Soccer fields, athletic fields, parking",
    "notes_extra": "NEW DISCOVERY.",
    "url_primary": "https://bgohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-045", "name": "Raney Playground",
    "category": "Park", "subtype": "Playground Park", "designation": "",
    "status": "Active", "ownership": "City of Bowling Green",
    "governance": "City of Bowling Green Parks & Recreation",
    "partner_agencies": "", "coordination": "",
    "description": "Playground at Sand Ridge Road named for architect Jack Raney, added 2006. ADA accessible equipment.",
    "location": "Sand Ridge Road, Bowling Green, OH 43402", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Playground, ADA accessible play equipment",
    "notes_extra": "NEW DISCOVERY. Opened 2006.",
    "url_primary": "https://bgohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-046", "name": "Ridge Park",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "City of Bowling Green",
    "governance": "City of Bowling Green Parks & Recreation",
    "partner_agencies": "", "coordination": "",
    "description": "Newest Bowling Green park (2015) at 225 Ridge Street, developed on former elementary school site.",
    "location": "225 Ridge Street, Bowling Green, OH 43402", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Park facilities, walking, recreation",
    "notes_extra": "NEW DISCOVERY. Opened 2015 on former school grounds.",
    "url_primary": "https://bgohio.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  # ── TIER 6 — PERRYSBURG ─────────────────────────────────────
  {
    "site_id": "WOD-SI-047", "name": "Municipal Park",
    "category": "Park", "subtype": "Sports Park", "designation": "",
    "status": "Active", "ownership": "City of Perrysburg",
    "governance": "City of Perrysburg",
    "partner_agencies": "", "coordination": "",
    "description": "Flagship city park at 945 Elm Street, Perrysburg. 23.5 acres with pool, tennis, pickleball, baseball, softball, and summer recreation programs.",
    "location": "945 Elm Street, Perrysburg, OH 43551", "acres": "23.5",
    "counties_raw": ["Wood"], "gps_name": "Municipal Park",
    "features_raw": "Swimming pool (opens May 31), tennis courts, pickleball courts, baseball fields, softball fields, walking paths, parking, ADA accessible facilities",
    "notes_extra": "NEW DISCOVERY. Perrysburg's main municipal park.",
    "url_primary": "https://perrysburgoh.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-048", "name": "Bicentennial Park",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "City of Perrysburg",
    "governance": "City of Perrysburg",
    "partner_agencies": "", "coordination": "",
    "description": "Neighborhood park in Perrysburg.",
    "location": "Perrysburg, OH 43551", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Recreation, neighborhood park",
    "notes_extra": "NEW DISCOVERY.",
    "url_primary": "https://perrysburgoh.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-049", "name": "Davis Overlook",
    "category": "Open Space", "subtype": "", "designation": "",
    "status": "Active", "ownership": "City of Perrysburg",
    "governance": "City of Perrysburg",
    "partner_agencies": "", "coordination": "",
    "description": "Scenic overlook in Perrysburg with views of the Maumee River.",
    "location": "Perrysburg, OH 43551", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Scenic overlook, observation area",
    "notes_extra": "NEW DISCOVERY.",
    "url_primary": "https://perrysburgoh.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-050", "name": "Eisenhower Park",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "City of Perrysburg",
    "governance": "City of Perrysburg",
    "partner_agencies": "", "coordination": "",
    "description": "Neighborhood park in Perrysburg.",
    "location": "Perrysburg, OH 43551", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Recreation, neighborhood park",
    "notes_extra": "NEW DISCOVERY.",
    "url_primary": "https://perrysburgoh.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-051", "name": "Hood Park",
    "category": "Memorial", "subtype": "War Memorial", "designation": "",
    "status": "Active", "ownership": "City of Perrysburg",
    "governance": "City of Perrysburg",
    "partner_agencies": "", "coordination": "",
    "description": "Park in Perrysburg containing war memorials and monuments.",
    "location": "Perrysburg, OH 43551", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "War memorials, monument, walking, historic viewing",
    "notes_extra": "NEW DISCOVERY. War memorials located here per city records.",
    "url_primary": "https://perrysburgoh.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-052", "name": "Milestone Park",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "City of Perrysburg",
    "governance": "City of Perrysburg",
    "partner_agencies": "", "coordination": "",
    "description": "Perrysburg's smallest park.",
    "location": "Perrysburg, OH 43551", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Walking, relaxation, small urban park",
    "notes_extra": "NEW DISCOVERY. Described as Perrysburg's smallest park.",
    "url_primary": "https://perrysburgoh.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-053", "name": "Orleans Park",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "City of Perrysburg",
    "governance": "City of Perrysburg",
    "partner_agencies": "", "coordination": "",
    "description": "Neighborhood park in Perrysburg.",
    "location": "Perrysburg, OH 43551", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Recreation, neighborhood park",
    "notes_extra": "Baseline seed confirmed.",
    "url_primary": "https://perrysburgoh.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-054", "name": "Riverside Park",
    "category": "Park", "subtype": "Waterfront Park", "designation": "",
    "status": "Active", "ownership": "City of Perrysburg",
    "governance": "City of Perrysburg",
    "partner_agencies": "", "coordination": "",
    "description": "Riverfront park on the Maumee River with seasonal Christmas light displays and walking.",
    "location": "Perrysburg, OH 43551", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Walking, Maumee River access, seasonal events, lighting",
    "notes_extra": "NEW DISCOVERY.",
    "url_primary": "https://perrysburgoh.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-055", "name": "Rotary Community Park",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "City of Perrysburg",
    "governance": "City of Perrysburg",
    "partner_agencies": "", "coordination": "",
    "description": "Community park behind Fort Meigs YMCA in Perrysburg. 19.8 acres with trails and wooded areas.",
    "location": "Behind Fort Meigs YMCA, Perrysburg, OH 43551", "acres": "19.8",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hiking trails, wooded areas, recreation",
    "notes_extra": "NEW DISCOVERY. 19.8 acres.",
    "url_primary": "https://perrysburgoh.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-056", "name": "Rivercrest Park",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "City of Perrysburg",
    "governance": "City of Perrysburg",
    "partner_agencies": "", "coordination": "",
    "description": "Neighborhood park in Perrysburg.",
    "location": "Perrysburg, OH 43551", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Recreation, neighborhood park",
    "notes_extra": "NEW DISCOVERY.",
    "url_primary": "https://perrysburgoh.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-057", "name": "Three Meadows Park",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "City of Perrysburg",
    "governance": "City of Perrysburg",
    "partner_agencies": "", "coordination": "",
    "description": "Perrysburg park with trails, wooded areas, and open fields.",
    "location": "Perrysburg, OH 43551", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hiking trails, walking trails, wooded areas, open fields",
    "notes_extra": "NEW DISCOVERY.",
    "url_primary": "https://perrysburgoh.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-058", "name": "Woodland Park (Perrysburg)",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "City of Perrysburg",
    "governance": "City of Perrysburg",
    "partner_agencies": "", "coordination": "",
    "description": "Wooded neighborhood park in Perrysburg.",
    "location": "Perrysburg, OH 43551", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Recreation, wooded park",
    "notes_extra": "NEW DISCOVERY.",
    "url_primary": "https://perrysburgoh.gov", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  # ── TIER 6 — ROSSFORD ───────────────────────────────────────
  {
    "site_id": "WOD-SI-059", "name": "Veterans Memorial Park",
    "category": "Park", "subtype": "Waterfront Park", "designation": "",
    "status": "Active", "ownership": "City of Rossford",
    "governance": "City of Rossford",
    "partner_agencies": "", "coordination": "",
    "description": "Maumee River waterfront park in Rossford with boating, fishing, and sports facilities.",
    "location": "Rossford, OH 43460 (Maumee River waterfront)", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Ball diamond, tennis courts, basketball courts, grills, picnic shelters, boat ramp, fishing, Maumee River access",
    "notes_extra": "Baseline seed 'Rossford City Park and Marina' resolved to this entity — Veterans Memorial Park on Maumee River.",
    "url_primary": "https://rossfordohio.com", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-060", "name": "Island View Park",
    "category": "Park", "subtype": "Waterfront Park", "designation": "",
    "status": "Active", "ownership": "City of Rossford",
    "governance": "City of Rossford",
    "partner_agencies": "", "coordination": "",
    "description": "Rossford park on Route 65/Dixie Highway featuring 1.1-mile exercise course with 16 stations on the Maumee River. 124 bird species recorded.",
    "location": "Route 65/Dixie Highway past Lime City Road, Rossford, OH 43460", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "1.1-mile exercise course, 16 exercise stations, bird watching, walking, Maumee River frontage, 124 bird species",
    "notes_extra": "NEW DISCOVERY. 124 bird species recorded.",
    "url_primary": "https://rossfordohio.com", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-061", "name": "Ed Ford Memorial Park",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "City of Rossford",
    "governance": "City of Rossford",
    "partner_agencies": "", "coordination": "",
    "description": "Park built in 1998 for Rossford city centennial at Dixie Highway and Elm Street. Named for city founder.",
    "location": "Dixie Highway and Elm Street, Rossford, OH 43460", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Urban park, recreation",
    "notes_extra": "NEW DISCOVERY. Built 1998 for city Centennial. Named for city founder.",
    "url_primary": "https://rossfordohio.com", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-062", "name": "Beech Street Park",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "City of Rossford",
    "governance": "City of Rossford",
    "partner_agencies": "", "coordination": "",
    "description": "Neighborhood park on Beech Street in Rossford.",
    "location": "Beech Street, Rossford, OH 43460", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Neighborhood park, recreation",
    "notes_extra": "NEW DISCOVERY — not in AutoRecovered baseline.",
    "url_primary": "https://rossfordohio.com", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  # ── TIER 6 — NORTHWOOD ──────────────────────────────────────
  {
    "site_id": "WOD-SI-063", "name": "Ranger Park",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "City of Northwood",
    "governance": "City of Northwood",
    "partner_agencies": "", "coordination": "",
    "description": "Municipal park in Northwood, Ohio.",
    "location": "Northwood, OH 43619", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Recreation, park facilities",
    "notes_extra": "NEW DISCOVERY — not in AutoRecovered baseline.",
    "url_primary": "https://ci.northwood.oh.us", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-064", "name": "Nature Trails Park (Northwood)",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "City of Northwood",
    "governance": "City of Northwood",
    "partner_agencies": "", "coordination": "",
    "description": "Municipal park with nature trail features in Northwood.",
    "location": "Northwood, OH 43619", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hiking trails, nature, recreation",
    "notes_extra": "NEW DISCOVERY. Distinct from WCPD's Nature Trails Park (WOD-SI-028) in Bowling Green. Northwood municipal entity.",
    "url_primary": "https://ci.northwood.oh.us", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-065", "name": "Central Park (Northwood)",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "City of Northwood",
    "governance": "City of Northwood",
    "partner_agencies": "", "coordination": "",
    "description": "Central municipal park in Northwood.",
    "location": "Northwood, OH 43619", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Recreation, park facilities",
    "notes_extra": "NEW DISCOVERY — not in AutoRecovered baseline.",
    "url_primary": "https://ci.northwood.oh.us", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-066", "name": "Brentwood Park",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "City of Northwood",
    "governance": "City of Northwood",
    "partner_agencies": "", "coordination": "",
    "description": "Neighborhood park in Northwood.",
    "location": "Northwood, OH 43619", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Recreation, neighborhood park",
    "notes_extra": "NEW DISCOVERY — not in AutoRecovered baseline.",
    "url_primary": "https://ci.northwood.oh.us", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  # ── TIER 6 — OTHER VILLAGES ─────────────────────────────────
  {
    "site_id": "WOD-SI-067", "name": "Village Park (North Baltimore)",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "Village of North Baltimore",
    "governance": "Village of North Baltimore",
    "partner_agencies": "", "coordination": "",
    "description": "Village park in North Baltimore with disc golf and fishing pond. Also near southern terminus area for Slippery Elm Trail.",
    "location": "North Baltimore, OH 45872", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Disc golf course, fishing pond, pond, restrooms, walking",
    "notes_extra": "NEW DISCOVERY. Baseline seed 'North Baltimore Reservoir' may be a separate entity — flagged for manual review. This record covers the identified Village Park.",
    "url_primary": "", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-068", "name": "Railway Park",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "Village of Walbridge",
    "governance": "Village of Walbridge",
    "partner_agencies": "", "coordination": "",
    "description": "Railroad-themed park in Walbridge village.",
    "location": "Walbridge, OH 43465", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Railroad heritage, historic structure, park facilities",
    "notes_extra": "NEW DISCOVERY — not in AutoRecovered baseline.",
    "url_primary": "", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-069", "name": "Mehring Park",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "Village of Tontogany",
    "governance": "Village of Tontogany",
    "partner_agencies": "", "coordination": "",
    "description": "Municipal park in Tontogany village.",
    "location": "Tontogany, OH 43565", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Park facilities, recreation",
    "notes_extra": "NEW DISCOVERY — not in AutoRecovered baseline.",
    "url_primary": "", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-070", "name": "Centennial Park (Tontogany)",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "Village of Tontogany",
    "governance": "Village of Tontogany",
    "partner_agencies": "", "coordination": "",
    "description": "Centennial park in Tontogany village.",
    "location": "Tontogany, OH 43565", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Park facilities, recreation",
    "notes_extra": "NEW DISCOVERY — not in AutoRecovered baseline.",
    "url_primary": "", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-071", "name": "Grand Rapids Park",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "Village of Grand Rapids",
    "governance": "Village of Grand Rapids",
    "partner_agencies": "", "coordination": "",
    "description": "Village park along the Maumee River and historic Miami and Erie Canal corridor in Grand Rapids.",
    "location": "Grand Rapids, OH 43522", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Maumee River access, canal heritage, walking, picnicking",
    "notes_extra": "NEW DISCOVERY. Grand Rapids is a historic village on the Maumee River near Mary Jane Thurston State Park.",
    "url_primary": "", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  {
    "site_id": "WOD-SI-072", "name": "Memorial Park (Pemberville)",
    "category": "Park", "subtype": "Neighborhood Park", "designation": "",
    "status": "Active", "ownership": "Village of Pemberville",
    "governance": "Village of Pemberville",
    "partner_agencies": "", "coordination": "",
    "description": "Village park in Pemberville with pool, tennis, and basketball facilities.",
    "location": "Pemberville, OH 43450", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Swimming pool, tennis courts, basketball court, recreation",
    "notes_extra": "NEW DISCOVERY. Distinct from WCPD William Henry Harrison Park also in Pemberville.",
    "url_primary": "", "urls_extra": "", "parent_site_id": "", "discovery_tier": 6,
  },
  # ── TIER 7 — CONSERVANCY ────────────────────────────────────
  {
    "site_id": "WOD-SI-073", "name": "Mishe Monoto Preserve",
    "category": "Nature Preserve", "subtype": "Private Nature Preserve", "designation": "",
    "status": "Active", "ownership": "Appalachia Ohio Alliance",
    "governance": "Appalachia Ohio Alliance",
    "partner_agencies": "", "coordination": "",
    "description": "140-acre natural preserve managed by Appalachia Ohio Alliance in Wood County.",
    "location": "Wood County, OH", "acres": "140",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Hiking, nature study, natural habitat preservation",
    "notes_extra": "Baseline seed confirmed. Managed by Appalachia Ohio Alliance. 140 acres. Exact address not confirmed — GPS acquisition needed.",
    "url_primary": "", "urls_extra": "", "parent_site_id": "", "discovery_tier": 7,
  },
  # ── TIER 8 — PRIVATE ────────────────────────────────────────
  {
    "site_id": "WOD-SI-074", "name": "577 Foundation",
    "category": "Cultural Facility", "subtype": "Interpretive Center", "designation": "",
    "status": "Active", "ownership": "577 Foundation (nonprofit)",
    "governance": "577 Foundation",
    "partner_agencies": "", "coordination": "",
    "description": "Former Virginia Secor Stranahan estate at 577 E. Front Street, Perrysburg, converted to nonprofit community arts and nature center. Features geodesic biodome, fossil dig site, historic log cabin (1803), and Maumee River access. Devonian fossil site (375M years).",
    "location": "577 E. Front Street, Perrysburg, OH 43551", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "577 Foundation",
    "features_raw": "Geodesic Biodome, observation beehive, log cabin (1803 historic structure), StoryWalk Trail, River Walk, Bird Blind, fossil dig, community gardens, children's garden, solar display, pottery studio, Curiosity Shop, guided tours, educational programs, nature center, Maumee River frontage, ADA accessible grounds",
    "notes_extra": "NEW DISCOVERY. Former Stranahan estate. Public nonprofit — open to public with programming.",
    "url_primary": "https://577foundation.org", "urls_extra": "", "parent_site_id": "", "discovery_tier": 8,
  },
  {
    "site_id": "WOD-SI-075", "name": "BGSU Native Prairie Garden",
    "category": "Conservation Area", "subtype": "Restoration Area", "designation": "",
    "status": "Active", "ownership": "Bowling Green State University",
    "governance": "Bowling Green State University Office of Campus Sustainability",
    "partner_agencies": "", "coordination": "",
    "description": "Multiple BGSU prairie restoration sites off Wintergarden Road preserving native Ohio prairie species from pre-settlement Wood County. Teaching and research facility including University House Prairie, Poe Prairie, Shatzel Prairie Garden, and Butterfly Habitat.",
    "location": "Off Wintergarden Road, behind President's residence, Bowling Green, OH 43402", "acres": "",
    "counties_raw": ["Wood"], "gps_name": "",
    "features_raw": "Native prairie restoration, educational signage, controlled burn management, hiking, research, Big bluestem, Indian grass, Wild bergamot",
    "notes_extra": "NEW DISCOVERY. University-managed but publicly accessible campus natural areas. Multiple sub-sites — may warrant parent-child grouping in normalization.",
    "url_primary": "https://bgsu.edu/campus-sustainability", "urls_extra": "", "parent_site_id": "", "discovery_tier": 8,
  },
]

# ---------- TRAILS ----------

TRAILS = [
  {
    "trail_id": "WOD-TR-001", "name": "Slippery Elm Trail",
    "alternate_names": "Slippery Elm Trail",
    "use_type": "Multi-Use", "surface_type": "Paved", "origin_type": "Rail Trail",
    "length_mi": "13.1",
    "counties_raw": ["Wood"],
    "governance": "Wood County Park District",
    "partner_agencies": "", "status": "Active", "difficulty": "", "accessibility": "Paved, ADA accessible",
    "description": "Rails-to-trails conversion of former railroad corridor. 13.1-mile paved multi-use trail from Bowling Green to North Baltimore passing through Rudolph village. Trailheads at both ends with restrooms, water, and benches.",
    "trail_history": "Converted from former railroad corridor through Wood County.",
    "identity_notes": "Baseline seed confirmed. 13.1 miles paved. Key connector through Wood County.",
    "notes": "",
    "url_primary": "https://wcparks.org", "maps": "",
    "parent_site_id": "", "discovery_tier": 4,
  },
  {
    "trail_id": "WOD-TR-002", "name": "Portage River Water Trail",
    "alternate_names": "Ohio Water Trail #17",
    "use_type": "Water", "surface_type": "Water", "origin_type": "Other",
    "length_mi": "36",
    "counties_raw": ["Wood", "Ottawa"],
    "governance": "ODNR Office of Coastal Management",
    "partner_agencies": "", "status": "Active", "difficulty": "", "accessibility": "",
    "description": "Ohio State Water Trail #17. 36-mile paddling trail on the Portage River, starting at William Henry Harrison Park in Pemberville and flowing through Wood and Ottawa counties to Lake Erie.",
    "trail_history": "",
    "identity_notes": "Ohio Water Trail #17. Starts at William Henry Harrison Park (WOD-SI-036) in Pemberville. Wood County to Ottawa County to Lake Erie. 36 miles total.",
    "notes": "Cross-county trail — Wood and Ottawa counties. Wood County anchor record.",
    "url_primary": "https://ohiocoastalmanagement.ohiodnr.gov/water-trails", "maps": "",
    "parent_site_id": "", "discovery_tier": 2,
  },
  {
    "trail_id": "WOD-TR-003", "name": "Maumee River Water Trail",
    "alternate_names": "",
    "use_type": "Water", "surface_type": "Water", "origin_type": "Other",
    "length_mi": "107",
    "counties_raw": ["Williams", "Defiance", "Henry", "Wood", "Lucas"],
    "governance": "ODNR Office of Coastal Management",
    "partner_agencies": "", "status": "Active", "difficulty": "", "accessibility": "",
    "description": "Ohio State Water Trail. 107-mile paddling trail on the Maumee River through 5 counties in northwest Ohio. Wood County segment includes access points at Grand Rapids, Perrysburg, and other river communities.",
    "trail_history": "",
    "identity_notes": "Multi-county water trail anchored in Wood County. Multiple WCPD and municipal access points in Wood County segment including Fort Meigs Access (WOD-AP-001), Buttonwood (WOD-SI-022), Otsego Park (WOD-SI-029), Maple Street (WOD-AP-002), Louisiana Ave (WOD-AP-003).",
    "notes": "Cross-county trail — 5 counties. Wood County anchor record.",
    "url_primary": "https://ohiocoastalmanagement.ohiodnr.gov/water-trails", "maps": "",
    "parent_site_id": "", "discovery_tier": 2,
  },
]

# ---------- ACCESS POINTS ----------

ACCESS_POINTS = [
  {
    "access_point_id": "WOD-AP-001", "name": "Fort Meigs Access",
    "ap_type": "Fishing Access", "status": "Active",
    "parent_entity_type": "Trail", "parent_entity_id": "WOD-TR-003",
    "county": "Wood", "township": "", "municipality": "",
    "address": "Near Fort Meigs, Perrysburg, OH 43551 (Maumee River)",
    "gps_name": "",
    "features_raw": "Boat ramp, fishing access, Maumee River access",
    "identity_notes": "Baseline seed confirmed as a separate ODNR river access point — distinct from Fort Meigs State Memorial (WOD-SI-002, managed by Ohio History Connection). ODNR maintains fishing/boat access on Maumee River near the historic fort.",
    "notes": "ODNR-managed fishing and boat access. Parent: Maumee River Water Trail (WOD-TR-003). GPS acquisition needed.",
    "url_primary": "https://wildohio.gov", "discovery_tier": 2,
  },
  {
    "access_point_id": "WOD-AP-002", "name": "Maple Street Boat Launch",
    "ap_type": "Boat Launch", "status": "Active",
    "parent_entity_type": "Trail", "parent_entity_id": "WOD-TR-003",
    "county": "Wood", "township": "", "municipality": "Perrysburg",
    "address": "Maple Street, Perrysburg, OH 43551",
    "gps_name": "",
    "features_raw": "Boat launch, Maumee River water access, watercraft access",
    "identity_notes": "Baseline seed 'Maple St. Access' confirmed as this entity. City of Perrysburg maintained.",
    "notes": "City of Perrysburg boat launch on Maumee River. Parent: Maumee River Water Trail (WOD-TR-003). GPS acquisition needed.",
    "url_primary": "https://perrysburgoh.gov", "discovery_tier": 6,
  },
  {
    "access_point_id": "WOD-AP-003", "name": "Louisiana Avenue Boat Dock",
    "ap_type": "Boat Launch", "status": "Active",
    "parent_entity_type": "Trail", "parent_entity_id": "WOD-TR-003",
    "county": "Wood", "township": "", "municipality": "Perrysburg",
    "address": "Louisiana Avenue, Perrysburg, OH 43551",
    "gps_name": "",
    "features_raw": "Boat dock, Maumee River access",
    "identity_notes": "City of Perrysburg boat dock on Maumee River. Potential parent site: Riverside Park or standalone access point.",
    "notes": "City of Perrysburg boat dock. Parent: Maumee River Water Trail (WOD-TR-003). GPS acquisition needed.",
    "url_primary": "https://perrysburgoh.gov", "discovery_tier": 6,
  },
]

# ─────────────────────────────────────────────────────────────
# VOCABULARY VALIDATION GATE (Stage 4.5)
# ─────────────────────────────────────────────────────────────
errors = []

def vocab_check_sites(sites):
    subtype_map = {
        "Park": PARK_SUBTYPES,
        "Nature Preserve": NATURE_PRESERVE_SUBS,
        "Wildlife Area": WILDLIFE_AREA_SUBS,
        "Water Site": WATER_SITE_SUBS,
        "Campground": CAMPGROUND_SUBS,
        "Recreation Facility": RECREATION_FACILITY_SUBS,
        "Museum": MUSEUM_SUBS,
        "Historic Site": HISTORIC_SITE_SUBS,
        "Natural Area": NATURAL_AREA_SUBS,
        "Conservation Area": CONSERVATION_AREA_SUBS,
        "Memorial": MEMORIAL_SUBS,
        "Cultural Facility": CULTURAL_FACILITY_SUBS,
        "Open Space": OPEN_SPACE_SUBS,
    }
    for s in sites:
        sid = s["site_id"]
        cat = s["category"]
        sub = s.get("subtype", "")
        if cat not in SITE_CATEGORIES:
            errors.append(f"IMP-063 FATAL: {sid} '{s['name']}' — invalid category '{cat}'")
        if sub:
            valid_subs = subtype_map.get(cat)
            if valid_subs and sub not in valid_subs:
                errors.append(f"SUBTYPE VIOLATION: {sid} '{s['name']}' — '{cat}' has invalid subtype '{sub}'")

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

HELD_IDS = {"WOD-SI-028", "WOD-SI-034", "WOD-SI-035"}

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
        "site_id":          s["site_id"],
        "name":             clean(s["name"]),
        "category":         s["category"],
        "subtype":          s.get("subtype", ""),
        "designation":      clean(s.get("designation", "")),
        "status":           s.get("status", "Active"),
        "ownership":        clean(s.get("ownership", "")),
        "governance":       clean(s.get("governance", "")),
        "partner_agencies": clean(s.get("partner_agencies", "")),
        "coordination":     clean(s.get("coordination", "")),
        "description":      clean(s.get("description", "")),
        "location":         clean(s.get("location", "")),
        "acres":            fmt_acres(s.get("acres", "")),
        "counties":         counties,
        "municipality":     "",
        "township":         "",
        "gps_lat":          fmt_gps(lat),
        "gps_lon":          fmt_gps(lon),
        "plus_code":        plus_code,
        "features":         features,
        "notes":            clean(notes),
        "url_primary":      clean(s.get("url_primary", "")),
        "urls":             clean(s.get("urls_extra", "")),
        "parent_site_id":   s.get("parent_site_id", ""),
        "created_at":       RUN_TS,
        "updated_at":       RUN_TS,
        "features_raw":     clean(s.get("features_raw", "")),
    }

def build_trail_row(t):
    counties = normalize_counties(t["counties_raw"])
    return {
        "trail_id":         t["trail_id"],
        "name":             clean(t["name"]),
        "alternate_names":  clean(t.get("alternate_names", "")),
        "use_type":         t.get("use_type", ""),
        "surface_type":     t.get("surface_type", ""),
        "origin_type":      t.get("origin_type", ""),
        "length_mi":        t.get("length_mi", ""),
        "counties":         counties,
        "governance":       clean(t.get("governance", "")),
        "partner_agencies": clean(t.get("partner_agencies", "")),
        "status":           t.get("status", "Active"),
        "difficulty":       t.get("difficulty", ""),
        "accessibility":    t.get("accessibility", ""),
        "description":      clean(t.get("description", "")),
        "trail_history":    clean(t.get("trail_history", "")),
        "identity_notes":   clean(t.get("identity_notes", "")),
        "notes":            clean(t.get("notes", "")),
        "url_primary":      clean(t.get("url_primary", "")),
        "maps":             clean(t.get("maps", "")),
        "created_at":       RUN_TS,
        "updated_at":       RUN_TS,
    }

def build_ap_row(ap):
    lat, lon, plus_code, conf = get_gps(ap.get("gps_name", ""))
    features = map_features(ap.get("features_raw", ""))
    note_parts = [ap.get("notes", "")]
    gn = gps_note(conf, ap["name"])
    if gn: note_parts.append(gn)
    notes = " ".join(p for p in note_parts if p)
    return {
        "access_point_id":    ap["access_point_id"],
        "name":               clean(ap["name"]),
        "ap_type":            ap["ap_type"],
        "status":             ap.get("status", "Active"),
        "parent_entity_type": ap.get("parent_entity_type", ""),
        "parent_entity_id":   ap.get("parent_entity_id", ""),
        "county":             ap.get("county", "Wood"),
        "township":           "",
        "municipality":       ap.get("municipality", ""),
        "address":            clean(ap.get("address", "")),
        "gps_lat":            fmt_gps(lat),
        "gps_lon":            fmt_gps(lon),
        "plus_code":          plus_code,
        "features":           features,
        "identity_notes":     clean(ap.get("identity_notes", "")),
        "notes":              clean(notes),
        "url_primary":        clean(ap.get("url_primary", "")),
        "created_at":         RUN_TS,
        "updated_at":         RUN_TS,
    }

# Build rows
for s in SITES:
    row = build_site_row(s)
    SITES_OUT.append(row)
    if s["site_id"] in HELD_IDS:
        HELD_OUT.append(("Site", s["site_id"], s["name"], "website_not_found — WCPD status unverified; awaiting manual confirmation"))

for t in TRAILS:
    row = build_trail_row(t)
    TRAILS_OUT.append(row)
    if t.get("parent_site_id"):
        TRAIL_PARENTS_OUT.append({"trail_id": t["trail_id"], "parent_site_id": t["parent_site_id"]})

for ap in ACCESS_POINTS:
    APS_OUT.append(build_ap_row(ap))

# ─────────────────────────────────────────────────────────────
# STAGE 4.5 — VOCABULARY VALIDATION GATE
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
# STAGE 4 — TSV OUTPUT
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

sites_path  = os.path.join(OUTPUT_DIR, "wood_oh_sites.tsv")
trails_path = os.path.join(OUTPUT_DIR, "wood_oh_trails.tsv")
segs_path   = os.path.join(OUTPUT_DIR, "wood_oh_trail_segments.tsv")
tnets_path  = os.path.join(OUTPUT_DIR, "wood_oh_trail_networks.tsv")
snets_path  = os.path.join(OUTPUT_DIR, "wood_oh_site_networks.tsv")
aps_path    = os.path.join(OUTPUT_DIR, "wood_oh_access_points.tsv")

write_tsv(sites_path, SITE_COLS, SITES_OUT)
write_tsv(trails_path, TRAIL_COLS, TRAILS_OUT, TRAIL_KEYS)

for path, label in [(segs_path, "Trail Segments"), (tnets_path, "Trail Networks"), (snets_path, "Site Networks")]:
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Wood County, OH — {label}\n# No entities found at discovery. 2026-04-14\n")
    print(f"  {path.split('/')[-1]}: 0 records (no entities)")

write_tsv(aps_path, AP_COLS, APS_OUT, AP_KEYS)

print(f"  {sites_path.split('/')[-1]}: {len(SITES_OUT)} sites")
print(f"  {trails_path.split('/')[-1]}: {len(TRAILS_OUT)} trails")
print(f"  {aps_path.split('/')[-1]}: {len(APS_OUT)} access points")

# ─────────────────────────────────────────────────────────────
# STAGE 5 — INTEGRITY CHECK
# ─────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("STAGE 5 — TSV INTEGRITY CHECK")
print("="*60)

integ_errors = []
site_ids  = {r["site_id"]          for r in SITES_OUT}
trail_ids = {r["trail_id"]         for r in TRAILS_OUT}
ap_ids    = {r["access_point_id"]  for r in APS_OUT}

for tp in TRAIL_PARENTS_OUT:
    if tp["parent_site_id"] not in site_ids:
        integ_errors.append(f"TRAIL PARENT REF: {tp['trail_id']} → {tp['parent_site_id']} not in sites")

for ap in APS_OUT:
    pid   = ap.get("parent_entity_id", "")
    ptype = ap.get("parent_entity_type", "")
    if pid and ptype == "Trail" and pid not in trail_ids:
        conn = sqlite3.connect(PROD_DB)
        row  = conn.execute("SELECT trail_id FROM trails WHERE trail_id=?", (pid,)).fetchone()
        conn.close()
        if not row:
            integ_errors.append(f"AP PARENT REF: {ap['access_point_id']} → Trail {pid} not found in trails or DB")

for r in SITES_OUT:
    if not r["name"]:     integ_errors.append(f"MISSING NAME: {r['site_id']}")
    if not r["category"]: integ_errors.append(f"MISSING CATEGORY: {r['site_id']}")
for r in TRAILS_OUT:
    if not r["name"]:     integ_errors.append(f"MISSING NAME: {r['trail_id']}")

all_site_ids  = [r["site_id"]         for r in SITES_OUT]
all_trail_ids = [r["trail_id"]        for r in TRAILS_OUT]
all_ap_ids    = [r["access_point_id"] for r in APS_OUT]
for lst, label in [(all_site_ids,"sites"),(all_trail_ids,"trails"),(all_ap_ids,"access_points")]:
    if len(lst) != len(set(lst)):
        integ_errors.append(f"DUPLICATE IDs in {label}: {[x for x in lst if lst.count(x)>1]}")

gps_sites   = sum(1 for r in SITES_OUT if r["gps_lat"])
nogps_sites = [r["name"] for r in SITES_OUT if not r["gps_lat"]]
gps_aps     = sum(1 for r in APS_OUT if r["gps_lat"])
print(f"  Sites with GPS: {gps_sites}/{len(SITES_OUT)}")
if nogps_sites:
    print(f"  Sites lacking GPS ({len(nogps_sites)}): {', '.join(nogps_sites[:10])}{'...' if len(nogps_sites)>10 else ''}")

if integ_errors:
    print("❌ INTEGRITY ERRORS:")
    for e in integ_errors: print(f"  {e}")
    sys.exit(1)
else:
    print("✅ Integrity check passed.")

# ─────────────────────────────────────────────────────────────
# STAGE 6 — DATABASE UPSERT
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
    cur.execute("INSERT OR IGNORE INTO trail_parents (trail_id, parent_site_id) VALUES (?, ?)", (tid, psid))

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
    """, (eid, etype, ename, "verification_required", reason, "Wood", RUN_ID, now))

def upsert_discovery_prov(eid, etype, tier):
    cur.execute("""
        INSERT OR IGNORE INTO discovery_provenance
          (entity_id, entity_type, county, discovery_tier, source_notes, run_id, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (eid, etype, "Wood", tier, f"Wood County pipeline run {RUN_ID}", RUN_ID, now))

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
    ap_tier = next(ap["discovery_tier"] for ap in ACCESS_POINTS if ap["access_point_id"]==r["access_point_id"])
    upsert_discovery_prov(r["access_point_id"], "Access Point", ap_tier)
    upsert_ap_parent(r["access_point_id"], r["parent_entity_type"], r["parent_entity_id"])
    ap_count += 1

# Write held entities (3 WCPD unverified parks)
for etype, eid, ename, reason in HELD_OUT:
    upsert_held(etype, eid, ename, reason)

# Write 4 unconfirmed baseline seeds (not entity records — logged to held only)
UNCONFIRMED_SEEDS = [
    ("WOD-SEED-001", "Devils Hole Prairie",
     "GNIS geographic/historical place name for remnant Black Swamp prairie feature. No managed public access site confirmed. May be protected within larger conservancy holding."),
    ("WOD-SEED-002", "Hulls Prairie",
     "GNIS geographic/historical place name; likely Hull Prairie Road area feature. No independently managed public site confirmed."),
    ("WOD-SEED-003", "Tontogany Prairie",
     "GNIS geographic/historical place name for a prairie remnant near Tontogany village. No managed public site confirmed."),
    ("WOD-SEED-004", "North Baltimore Reservoir",
     "Municipal water reservoir; not confirmed as public natural area with open access. Village Park (disc golf/pond) recorded separately as WOD-SI-067."),
]
for seed_id, seed_name, seed_detail in UNCONFIRMED_SEEDS:
    cur.execute("""
        INSERT OR IGNORE INTO held_entities (record_id, entity_type, name, hold_reason, hold_detail, county, run_id, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (seed_id, "Site", seed_name, "unconfirmed_baseline_seed", seed_detail, "Wood", RUN_ID, now))

# Run metadata
cur.execute("""
    INSERT OR IGNORE INTO run_metadata (run_id, county, state, run_date, records_input, normalized, held, notes, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (RUN_ID, "Wood", "OH", now[:10],
      s_count + t_count + ap_count,
      s_count + t_count + ap_count,
      len(HELD_OUT) + len(UNCONFIRMED_SEEDS),
      "pipeline_version=5.2", now))

conn.commit()
conn.close()

print(f"  Upserted: {s_count} sites, {t_count} trails, {ap_count} access points")
print(f"  Held (WCPD unverified): {len(HELD_OUT)} entities")
print(f"  Held (unconfirmed seeds): {len(UNCONFIRMED_SEEDS)} seeds")

# ─────────────────────────────────────────────────────────────
# SUMMARY
# ─────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("WOOD COUNTY PIPELINE — COMPLETE")
print("="*60)
print(f"Run ID:        {RUN_ID}")
print(f"Run timestamp: {RUN_TS}")
print(f"Sites:         {s_count} (including {len([x for x in HELD_OUT if x[0]=='Site'])} held)")
print(f"Trails:        {t_count}")
print(f"Access Points: {ap_count}")
print(f"Trail Segs:    0")
print(f"Trail Nets:    0")
print(f"Site Nets:     0")
print(f"Unconfirmed seeds logged: {len(UNCONFIRMED_SEEDS)}")
print(f"\nOutput: {OUTPUT_DIR}")
print(f"DB: {PROD_DB}")
print("="*60)
