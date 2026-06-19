#!/usr/bin/env python3
# =============================================================================
# SUPERSEDED — IMP-091 (2026-05-04)
# This monolithic pipeline script has been replaced by the parameterised model:
#   utilities/na_run_county.py + County_Spreadsheets/{County}/{county}_pipeline_config.json
# Do not use for new county runs. Kept for reference only.
# =============================================================================
"""
van_wert_oh_pipeline.py — Natural Areas Project
Van Wert County, Ohio — Full Pipeline Script
Stages 2–6: Normalization → GPS Acquisition → TSV Output → Vocab Validation Gate
            → Integrity Check → SQLite Upsert

RUN_ID:  van_wert_oh_2026_04_14
PREFIX:  VNW
Records: 23 raw → 19 Sites, 3 Trails, 0 Trail Segments, 0 Trail Networks,
                   0 Site Networks, 1 Access Point

USAGE:
  cd "Natural Areas Project v5"
  python County_Spreadsheets/Van\ Wert/van_wert_oh_pipeline.py [--db PATH] [--dry-run]

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
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
UTIL_DIR    = os.path.join(PROJECT_ROOT, 'utilities')
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
COUNTY      = "Van Wert"
STATE       = "Ohio"
RUN_ID      = "van_wert_oh_2026_04_14"
RUN_DATE    = "2026-04-19"
NOW         = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
OUTPUT_DIR  = SCRIPT_DIR
DEFAULT_DB  = os.path.join(PROJECT_ROOT, "NASqlite", "natural_areas_v5.db")

NOMINATIM_URL     = "https://nominatim.openstreetmap.org/search"
NOMINATIM_DELAY   = 1.1
NOMINATIM_HEADERS = {
    "User-Agent": "NaturalAreasProject/5.x (research use; admin contact available)",
    "Accept-Language": "en"
}

# Van Wert County bounding box (plausibility check)
VNW_LAT_MIN, VNW_LAT_MAX = 40.69, 41.01
VNW_LON_MIN, VNW_LON_MAX = -84.93, -84.44

# ── Vocabulary constants ─────────────────────────────────────────────────────
# Site categories (§2.1)
ALLOWED_CATEGORIES = {
    "Campground", "Cemetery", "Community Garden", "Conservation Area",
    "Cultural Facility", "Curated Biological Site", "Fishing Area",
    "Historic Site", "Hunting Area", "Memorial", "Museum", "Natural Area",
    "Nature Preserve", "Open Space", "Park", "Recreation Facility",
    "Water Site", "Wildlife Area",
}

# Subtypes by category (§3.2)
ALLOWED_SUBTYPES = {
    "Park": {
        "Greenspace", "Neighborhood Park", "Linear Park", "Dog Park",
        "Playground Park", "Sports Park", "Waterfront Park", "Civic Park", "Historic Park",
    },
    "Nature Preserve": {
        "State Nature Preserve", "County Nature Preserve", "Municipal Nature Preserve",
        "Private Nature Preserve", "Land Trust Preserve", "Conservation Easement Preserve",
    },
    "Recreation Facility": {
        "Sports Complex", "Athletic Field", "Golf Course", "Swimming Pool",
        "Tennis Complex", "Pickleball Complex", "Skate Park", "Disc Golf Course",
        "Ice Rink", "BMX Track", "Pump Track", "Recreation Center",
    },
    "Wildlife Area": {
        "State Wildlife Area", "Federal Wildlife Area", "Waterfowl Area",
        "Migratory Bird Area", "Wetland Management Area",
    },
    "Water Site": {
        "Lake", "Pond", "Reservoir", "River", "Harbor", "Marina",
    },
    "Memorial": {
        "War Memorial", "Veterans Memorial", "Civic Memorial", "Monument",
        "Memorial Garden", "Memorial Plaza",
    },
    "Cultural Facility": {
        "Cultural Center", "Performing Arts Center", "Interpretive Center",
        "Heritage Center", "Art Center", "Visitor Center",
    },
    "Curated Biological Site": {
        "Arboretum", "Botanical Garden", "Zoo", "Aquarium", "Aviary",
        "Insectarium", "Butterfly House", "Reptile House", "Biopark", "Living Museum",
    },
    "Historic Site": {
        "Historic Landmark", "Archaeological Site", "Historic Landscape",
        "Battlefield", "Historic Structure",
    },
    "Cemetery": {
        "Public Cemetery", "Private Cemetery", "Family Cemetery",
        "Veterans Cemetery", "Church Cemetery",
    },
    "Campground": {
        "Tent Campground", "RV Campground", "Primitive Campground",
        "Group Campground", "Cabin Campground",
    },
    "Open Space": {
        "Urban Open Space", "Suburban Open Space", "Greenbelt", "Commons",
        "Civic Lawn", "Boulevard Median",
    },
    "Conservation Area": {
        "Restoration Area", "Habitat Management Area", "Resource Protection Area",
        "Watershed Protection Area", "Forest Management Area",
    },
    "Natural Area": {
        "Forest", "Upland Forest", "Floodplain Forest", "Prairie", "Grassland",
        "Meadow", "Shrubland", "Savanna", "Old Field", "Successional Area",
        "Wetland", "Marsh", "Fen", "Bog", "Swamp", "Riparian Area",
        "Ravine", "Cliff or Bluff", "Barrens",
    },
    "Hunting Area": set(),
    "Fishing Area": set(),
    "Museum": {
        "History Museum", "Art Museum", "Science Museum", "Children's Museum",
        "Natural History Museum",
    },
    "Community Garden": set(),
}

ALLOWED_STATUSES = {"Active", "Planned", "Under Construction", "Defunct", "Closed", "Seasonal"}

ALLOWED_DESIGNATIONS = {
    # Federal
    "National Park", "National Monument", "National Recreation Area",
    "National Wildlife Refuge", "National Forest", "National Grassland",
    "National Scenic Trail", "National Historic Trail", "National Historic Landmark",
    "National Wild and Scenic River", "Wilderness Area",
    # State
    "State Park", "State Forest", "State Nature Preserve", "State Wildlife Area",
    "State Scenic River", "State Hunting Area", "State Fishing Area",
    "State Recreation Area", "State Historic Site", "State Memorial",
    "State Nature Area",
    # Other
    "Registered Natural Landmark",
}

ALLOWED_FEATURES = {
    "ADA Accessible", "AED", "Alvar", "Amphibian Area", "Amphitheater",
    "Apiary", "Arboretum", "Archery Range", "Art Gallery", "Art Installation",
    "Athletic Field", "Ball Diamond", "Ballroom", "Bandstand", "Basketball Court",
    "Beach", "Bike Rack", "Bike Repair Station", "Bird Viewing Area", "Boardwalk",
    "Boat Dock", "Boat Ramp", "Bocce Court", "Bog", "Bluff", "Boathouse",
    "Bridge", "Bridle Trail", "Building Ruins", "Butterfly or Pollinator Garden",
    "Camping", "Cabin Rentals", "Canal Structure", "Cave or Cavern",
    "Cemetery Section", "Chapel", "Cliff", "Climbing Structure", "Community Center",
    "Community Garden", "Composting Station", "Conservatory", "Covered Shelter",
    "Cricket Pitch", "Culvert", "Dam", "Dance Floor", "Dance Performance Space",
    "Demonstration Farm Plot", "Demonstration Garden", "Disc Golf Course", "Dog Park",
    "Drainage Ditch", "Dune", "Educational Pavilion", "Electric Vehicle Charging",
    "Equestrian Arena", "Farm Store", "Fence", "Fen", "Fieldhouse", "Fire Ring",
    "Fire Tower", "Fishing Area", "Fitness Station", "Football Field",
    "Football Stadium", "Fountain", "Garage", "Garden", "Gate", "Gatehouse",
    "Gazebo", "Glacial Erratic", "Golf Course", "Gorge", "Greenhouse", "Grill",
    "Guided Tours", "Habitat Restoration Area", "Handball Court", "Hiking Trail",
    "Hilltop", "Historic Bridge", "Historic Canal Segment", "Historic Cemetery Section",
    "Historic Fence Line", "Historic Foundation", "Historic Lock", "Historic Marker",
    "Historic Marker Cluster", "Historic Millrace", "Historic Road Trace",
    "Historic Ruins", "Historic Structure", "Historic Well", "Horseshoe Pitch",
    "Hunting Area", "Ice Rink", "Information Board", "Insectarium",
    "Interpretive Exhibit", "Interpretive Garden", "Interpretive Sign",
    "Island", "Kiosk", "Kite Flying", "Lacrosse Field", "Lake", "Landmark Tree",
    "Levee", "Lodge", "Lookout Cabin", "Maintenance Building", "Marina",
    "Marsh", "Meadow", "Model Airplane Field", "Model Rocketry Field",
    "Mini Golf", "Monitoring Station", "Monument", "Mountain Bike Trail",
    "Multi-use Trail", "Museum Building", "Musical Instruments",
    "Musical Performance Space", "Native American Artifacts",
    "Native American Cultural Site", "Native American Earthwork", "Natural Arch",
    "Nature Center", "Nature Play Area", "Observation Deck", "Observation Tower",
    "Observatory", "Old-Growth Stand", "Orchard", "Outdoor Art Installation",
    "Outdoor Classroom", "Overflow Parking", "Overlook (built)", "Overlook (natural)",
    "Parking Lot", "Pavilion", "Peninsula", "Pickleball Court", "Picnic Area",
    "Picnic Shelter", "Picnic Table Cluster", "Pipeline Corridor",
    "Pioneer Historic Site", "Pioneer Re-creation", "Planetarium", "Playground",
    "Pollinator Garden", "Pond", "Powerline Corridor", "Prairie", "Prairie Restoration",
    "Public Art Installation", "Pump Station", "Pump Track", "Rain Garden",
    "Ravine", "Reforestation Area", "Reptile House", "Research Plot", "Restrooms",
    "Ropes Course", "Retaining Wall", "Retention Basin", "Ridge", "Rock Outcrop",
    "Scenic View", "Sculpture", "Sedge Meadow", "Shooting Range", "Shotgun Range",
    "Shuffleboard Court", "Silo", "Sinkhole", "Ski Slopes", "Skate Park",
    "Sledding Hill", "Slide", "Soccer Pitch", "Spillway", "Spray Park", "Spring",
    "Stable", "Stage", "Stormwater Basin", "Stream Segment", "Swimming Beach",
    "Swimming Pool", "Swing Set", "Tennis Court", "Theatre", "Topiary",
    "Trapping Area", "Transit Stop", "Trolley", "Tropical Garden",
    "Utility Corridor", "Valley", "Vegetable Garden", "Vernal Pool", "Via Ferrata",
    "Viewing Platform", "Vineyard", "Visitor Center", "Volleyball Court", "Wall",
    "Water Park", "Water Tower", "Watercraft Access", "Waterfall (built)",
    "Waterfall (natural)", "Waterslide", "Weather Station", "Weir", "Wetland",
    "Wetland Restoration", "Wilderness Area", "Wild Animal Rehabilitation",
    "Wildlife Observation Area", "Working Railway", "Zoo",
}

# Trail vocabulary
ALLOWED_TRAIL_USE_TYPES    = {"Multi-Use", "Hiking", "Bridle", "Water", "Bicycling",
                               "Mountain Bike", "BMX", "Pump Track", "Snowmobile",
                               "Cross Country Ski", "Other"}
ALLOWED_TRAIL_SURFACES     = {"Paved", "Crushed Stone", "Gravel", "Natural Surface",
                               "Boardwalk", "Water", "Mixed", "Other"}
ALLOWED_TRAIL_ORIGINS      = {"Rail Trail", "Canal Towpath", "Historic Route",
                               "Greenway Corridor", "Purpose-Built", "Utility Corridor",
                               "Roadside Corridor", "Other"}
ALLOWED_TRAIL_STATUSES     = {"Active", "Planned", "Under Construction", "Gap", "Closed"}
ALLOWED_TRAIL_DIFFICULTIES = {"Easy", "Moderate", "Difficult", "Strenuous", "Expert"}

# AP vocabulary
ALLOWED_AP_TYPES   = {"Trailhead", "Parking Area", "Boat Ramp", "Boat Launch",
                       "Watercraft Access Point", "River Access", "Fishing Access",
                       "Hazard Portage", "Bicycle Access", "Snowmobile Access",
                       "Cross Country Ski Access", "Equestrian Access",
                       "Roadside Pull-Off", "Pedestrian Entrance", "Vehicle Entrance",
                       "Transit Access", "Ferry Access", "Shuttle Access",
                       "Administrative Access", "Other"}
ALLOWED_AP_STATUSES = {"Active", "Closed", "Seasonal", "Restricted"}


# ── Normalized entity definitions (Stage 2 output) ───────────────────────────

SITES = [
    # ── Tier 2 — State ──────────────────────────────────────────────────────
    {
        "site_id":        "VNW-S-001",
        "name":           "Whitey Case Wildlife Production Area",
        "category":       "Wildlife Area",
        "subtype":        "State Wildlife Area",
        "designation":    "State Hunting Area",
        "status":         "Active",
        "ownership":      "State of Ohio",
        "governance":     "ODNR Division of Wildlife",
        "partner_agencies": "",
        "coordination":   "",
        "description":    "Nine-acre state wildlife production area managed by ODNR Division of Wildlife for wildlife habitat and public hunting.",
        "location":       "Van Wert County, OH",
        "acres":          9.29,
        "counties":       "Van Wert",
        "municipality":   "",
        "address":        "",
        "gps_lat":        40.800000,   # LOW confidence — toposports approx; GPS_VERIFY_NEEDED
        "gps_lon":        -84.790000,
        "gps_confidence": "LOW",
        "features":       "Hunting Area",
        "features_raw":   "Public hunting; 9.29 acres; wildlife habitat",
        "notes":          "GPS_VERIFY_NEEDED: toposports source only (2 decimal places); authoritative ODNR GIS coords needed.",
        "url_primary":    "",
        "urls":           "",
        "parent_site_id": "",
        "temp_id":        "VNW-T2-001",
    },
    {
        "site_id":        "VNW-S-002",
        "name":           "Van Wert Rest Area — Eastbound (US 30 MM9)",
        "category":       "Recreation Facility",
        "subtype":        "",
        "designation":    "",
        "status":         "Active",
        "ownership":      "State of Ohio",
        "governance":     "Ohio Department of Transportation (ODOT)",
        "partner_agencies": "Dolly Parton's Imagination Library of Ohio",
        "coordination":   "",
        "description":    "Eastbound US 30 rest area at mile marker 9 in Van Wert County. Reopened March 2025 after renovation. Features storybook trail created in partnership with Dolly Parton's Imagination Library of Ohio.",
        "location":       "US 30 Eastbound, Mile Marker 9, Van Wert County, OH",
        "acres":          None,
        "counties":       "Van Wert",
        "municipality":   "",
        "address":        "",
        "gps_lat":        None,
        "gps_lon":        None,
        "gps_confidence": "NONE",
        "features":       "ADA Accessible; Interpretive Sign; Lodge; Picnic Area; Restrooms",
        "features_raw":   "Restrooms (ADA compliant); covered lodge/rest building; picnic area; storybook trail signage (Dolly Parton Imagination Library of Ohio); opened March 2025",
        "notes":          "Parent of VNW-T-001 (Convoy Rest Area Storybook Trail). GPS not acquired — highway rest area; no street address.",
        "url_primary":    "https://hometownstations.com/van-wert/2025/07/governor-dewine-dedicates-renovated-us-30-van-wert-eastbound-rest-area/",
        "urls":           "",
        "parent_site_id": "",
        "temp_id":        "VNW-T2-002",
    },
    {
        "site_id":        "VNW-S-003",
        "name":           "Van Wert Rest Area — Westbound (US 30 MM9)",
        "category":       "Recreation Facility",
        "subtype":        "",
        "designation":    "",
        "status":         "Active",
        "ownership":      "State of Ohio",
        "governance":     "Ohio Department of Transportation (ODOT)",
        "partner_agencies": "",
        "coordination":   "",
        "description":    "Westbound US 30 rest area at mile marker 9 in Van Wert County. Reopened March 2025 after renovation.",
        "location":       "US 30 Westbound, Mile Marker 9, Van Wert County, OH",
        "acres":          None,
        "counties":       "Van Wert",
        "municipality":   "",
        "address":        "",
        "gps_lat":        None,
        "gps_lon":        None,
        "gps_confidence": "NONE",
        "features":       "ADA Accessible; Lodge; Picnic Area; Restrooms",
        "features_raw":   "Restrooms (ADA compliant); covered lodge/rest building; picnic area; opened March 2025. STORYBOOK_TRAIL_CONFIRM_NEEDED — may have storybook trail per Wyandot County precedent; unconfirmed.",
        "notes":          "STORYBOOK_TRAIL_CONFIRM_NEEDED: storybook trail unconfirmed at WB facility. Create VNW-T-004/VNW-S-005 if confirmed. GPS not acquired.",
        "url_primary":    "",
        "urls":           "",
        "parent_site_id": "",
        "temp_id":        "VNW-T2-003",
    },
    # ── Tier 3 — District ───────────────────────────────────────────────────
    {
        "site_id":        "VNW-S-004",
        "name":           "Convoy Edgewood Park",
        "category":       "Park",
        "subtype":        "",
        "designation":    "",
        "status":         "Active",
        "ownership":      "Tully-Convoy Park District",
        "governance":     "Tully-Convoy Park District",
        "partner_agencies": "",
        "coordination":   "",
        "description":    "Community park managed by the Tully-Convoy Park District. Features four baseball/softball diamonds, basketball courts, playground, community building, pavilion, and a scenic pond.",
        "location":       "643 N Main St, Convoy, OH 45832",
        "acres":          None,
        "counties":       "Van Wert",
        "municipality":   "Convoy",
        "address":        "643 N Main St, Convoy, OH 45832",
        "gps_lat":        None,
        "gps_lon":        None,
        "gps_confidence": "NONE",
        "features":       "Ball Diamond; Basketball Court; Community Center; Pavilion; Playground; Pond",
        "features_raw":   "4 baseball/softball diamonds; 2 basketball courts; playground; community building; pavilion; scenic pond",
        "notes":          "Managed by Tully-Convoy Park District (statutory district), not Village of Convoy. Confirmed Tier 3. PO Box 302, Convoy OH. Phone: 419-749-4060.",
        "url_primary":    "",
        "urls":           "",
        "parent_site_id": "",
        "temp_id":        "VNW-T3-001",
    },
    # ── Tier 6 — Municipal (City of Van Wert) ───────────────────────────────
    {
        "site_id":        "VNW-S-005",
        "name":           "Smiley Park",
        "category":       "Park",
        "subtype":        "",
        "designation":    "",
        "status":         "Active",
        "ownership":      "City of Van Wert",
        "governance":     "City of Van Wert",
        "partner_agencies": "",
        "coordination":   "",
        "description":    "City park spanning 29.4 acres along Leeson Avenue. Features multiple athletic facilities, fishing pond, and hosts the Children's Garden & Butterfly House.",
        "location":       "1451 Leeson Ave, Van Wert, OH 45891",
        "acres":          29.4,
        "counties":       "Van Wert",
        "municipality":   "Van Wert",
        "address":        "1451 Leeson Ave, Van Wert, OH 45891",
        "gps_lat":        None,
        "gps_lon":        None,
        "gps_confidence": "NONE",
        "features":       "Ball Diamond; Basketball Court; Fishing Area; Pavilion; Picnic Area; Playground; Pond; Tennis Court",
        "features_raw":   "Baseball/softball diamonds; basketball courts; fishing pond; pavilion; picnic area; playground; tennis courts; 29.4 acres",
        "notes":          "Parent of VNW-S-006 (Children's Garden & Butterfly House). Phone: 419-238-9121.",
        "url_primary":    "https://vanwert.org/parks-department/smiley-park/",
        "urls":           "https://visitvanwert.com/things-to-do/outdoor-adventure/",
        "parent_site_id": "",
        "temp_id":        "VNW-T6-001",
    },
    {
        "site_id":        "VNW-S-006",
        "name":           "Children's Garden and Butterfly House",
        "category":       "Curated Biological Site",
        "subtype":        "Butterfly House",
        "designation":    "",
        "status":         "Active",
        "ownership":      "City of Van Wert",
        "governance":     "City of Van Wert",
        "partner_agencies": "",
        "coordination":   "",
        "description":    "Enclosed butterfly house and children's garden located within Smiley Park. Features interpretive pollinator displays and a gazebo.",
        "location":       "1409 Leeson Ave, Van Wert, OH 45891",
        "acres":          None,
        "counties":       "Van Wert",
        "municipality":   "Van Wert",
        "address":        "1409 Leeson Ave, Van Wert, OH 45891",
        "gps_lat":        None,
        "gps_lon":        None,
        "gps_confidence": "NONE",
        "features":       "Butterfly or Pollinator Garden; Gazebo; Interpretive Garden",
        "features_raw":   "Enclosed butterfly house; children's pollinator garden; gazebo; interpretive displays",
        "notes":          "Child site of VNW-S-005 (Smiley Park).",
        "url_primary":    "https://visitvanwert.com/things-to-do/outdoor-adventure/",
        "urls":           "",
        "parent_site_id": "VNW-S-005",
        "temp_id":        "VNW-T6-001a",
    },
    {
        "site_id":        "VNW-S-007",
        "name":           "Van Wert Reservoir Recreation Area",
        "category":       "Park",
        "subtype":        "Waterfront Park",
        "designation":    "",
        "status":         "Active",
        "ownership":      "City of Van Wert",
        "governance":     "City of Van Wert",
        "partner_agencies": "",
        "coordination":   "",
        "description":    "Waterfront recreation area encompassing the City of Van Wert's two municipal water supply reservoirs. Features a 3.1-mile paved health trail loop, fishing access, boat launch, bird watching areas, and sledding hill. Includes child sites Reservoir 1 and Reservoir 2.",
        "location":       "S Washington St, Van Wert, OH 45891",
        "acres":          None,
        "counties":       "Van Wert",
        "municipality":   "Van Wert",
        "address":        "S Washington St, Van Wert, OH 45891",
        "gps_lat":        None,
        "gps_lon":        None,
        "gps_confidence": "NONE",
        "features":       "ADA Accessible; Bird Viewing Area; Fishing Area; Parking Lot; Sledding Hill",
        "features_raw":   "ADA accessible path (health trail 3.1 mi paved loop); bird watching; fishing access; parking; sledding hill; boat launch permit ($20/2yr); city water supply reservoirs",
        "notes":          "Parent of VNW-S-008 (Reservoir 1), VNW-S-009 (Reservoir 2), VNW-T-002 (Health Trail), VNW-AP-001 (Boat Launch). Trail and AP excluded from features per §6.1.",
        "url_primary":    "https://vanwert.org/parks-department/reservoir-recreation-area/",
        "urls":           "",
        "parent_site_id": "",
        "temp_id":        "VNW-T6-002",
    },
    {
        "site_id":        "VNW-S-008",
        "name":           "Van Wert Reservoir 1",
        "category":       "Water Site",
        "subtype":        "Reservoir",
        "designation":    "",
        "status":         "Active",
        "ownership":      "City of Van Wert",
        "governance":     "City of Van Wert",
        "partner_agencies": "ODNR Division of Wildlife",
        "coordination":   "",
        "description":    "City of Van Wert municipal water supply reservoir. 61 acres of water surface with 1.2 miles of shoreline. ODNR manages fish stocking. Used for public fishing and non-motorized recreation.",
        "location":       "S Washington St, Van Wert, OH 45891",
        "acres":          61.0,
        "counties":       "Van Wert",
        "municipality":   "Van Wert",
        "address":        "",
        "gps_lat":        None,
        "gps_lon":        None,
        "gps_confidence": "NONE",
        "features":       "Fishing Area",
        "features_raw":   "61 acres of water surface; 1.2 miles of shoreline; ODNR fish stocking; public fishing; city water supply reservoir (ODNR lake map, surveyed 2014)",
        "notes":          "Child site of VNW-S-007. GPS_VERIFY_NEEDED: GPS centroid not yet confirmed. Acreage confirmed via ODNR lake survey 2014.",
        "url_primary":    "",
        "urls":           "",
        "parent_site_id": "VNW-S-007",
        "temp_id":        "VNW-T6-002a",
    },
    {
        "site_id":        "VNW-S-009",
        "name":           "Van Wert Reservoir 2",
        "category":       "Water Site",
        "subtype":        "Reservoir",
        "designation":    "",
        "status":         "Active",
        "ownership":      "City of Van Wert",
        "governance":     "City of Van Wert",
        "partner_agencies": "ODNR Division of Wildlife",
        "coordination":   "",
        "description":    "City of Van Wert municipal water supply reservoir. 101 acres of water surface with 2.1 miles of shoreline. Includes ADA-accessible fishing areas and boat ramp access (permit required).",
        "location":       "S Washington St, Van Wert, OH 45891",
        "acres":          101.0,
        "counties":       "Van Wert",
        "municipality":   "Van Wert",
        "address":        "",
        "gps_lat":        40.840922,
        "gps_lon":        -84.574103,
        "gps_confidence": "MED",
        "features":       "ADA Accessible; Boat Ramp; Fishing Area",
        "features_raw":   "101 acres of water surface; 2.1 miles of shoreline; ADA accessible; boat ramp; fishing area; city water supply; ODNR fish stocking (ODNR lake map, surveyed 2014). GPS: Ohio Hometown Locator/Ohio gazetteer.",
        "notes":          "Child site of VNW-S-007. GPS confirmed 40.8409N, 84.5741W (Ohio Hometown Locator). Acreage confirmed via ODNR lake survey 2014.",
        "url_primary":    "",
        "urls":           "",
        "parent_site_id": "VNW-S-007",
        "temp_id":        "VNW-T6-002b",
    },
    {
        "site_id":        "VNW-S-010",
        "name":           "Franklin Park",
        "category":       "Park",
        "subtype":        "",
        "designation":    "",
        "status":         "Active",
        "ownership":      "City of Van Wert",
        "governance":     "City of Van Wert",
        "partner_agencies": "Van Wert County Foundation",
        "coordination":   "",
        "description":    "City park funded in part by Van Wert County Foundation. Features pavilion, picnic areas, playground, and spray park.",
        "location":       "305 Frothingham St, Van Wert, OH 45891",
        "acres":          None,
        "counties":       "Van Wert",
        "municipality":   "Van Wert",
        "address":        "305 Frothingham St, Van Wert, OH 45891",
        "gps_lat":        None,
        "gps_lon":        None,
        "gps_confidence": "NONE",
        "features":       "Pavilion; Picnic Area; Playground; Spray Park",
        "features_raw":   "Pavilion; picnic area; playground; splash pad/spray park; Van Wert County Foundation co-funded",
        "notes":          "VWCF co-funded; operated by City of Van Wert. Phone: 419-238-9121.",
        "url_primary":    "https://vanwert.org/parks-department/franklin-park/",
        "urls":           "",
        "parent_site_id": "",
        "temp_id":        "VNW-T6-003",
    },
    {
        "site_id":        "VNW-S-011",
        "name":           "Jubilee Park",
        "category":       "Park",
        "subtype":        "",
        "designation":    "",
        "status":         "Active",
        "ownership":      "City of Van Wert",
        "governance":     "City of Van Wert",
        "partner_agencies": "",
        "coordination":   "",
        "description":    "City neighborhood park. Features ball diamonds, pavilion, and playground.",
        "location":       "137 Gleason Ave, Van Wert, OH 45891",
        "acres":          None,
        "counties":       "Van Wert",
        "municipality":   "Van Wert",
        "address":        "137 Gleason Ave, Van Wert, OH 45891",
        "gps_lat":        None,
        "gps_lon":        None,
        "gps_confidence": "NONE",
        "features":       "Ball Diamond; Pavilion; Playground",
        "features_raw":   "Baseball/softball diamonds; pavilion; playground",
        "notes":          "Phone: 419-238-9121.",
        "url_primary":    "https://vanwert.org/parks-department/jubilee-park/",
        "urls":           "",
        "parent_site_id": "",
        "temp_id":        "VNW-T6-004",
    },
    {
        "site_id":        "VNW-S-012",
        "name":           "Memorial Park",
        "category":       "Memorial",
        "subtype":        "Veterans Memorial",
        "designation":    "",
        "status":         "Active",
        "ownership":      "American Legion Post #178",
        "governance":     "City of Van Wert",
        "partner_agencies": "American Legion Post #178",
        "coordination":   "",
        "description":    "Veterans memorial park owned and maintained by American Legion Post #178. Features veteran monuments, garden displays, and open grassy areas.",
        "location":       "611 W Main St, Van Wert, OH 45891",
        "acres":          None,
        "counties":       "Van Wert",
        "municipality":   "Van Wert",
        "address":        "611 W Main St, Van Wert, OH 45891",
        "gps_lat":        None,
        "gps_lon":        None,
        "gps_confidence": "NONE",
        "features":       "Garden; Monument; Parking Lot",
        "features_raw":   "Veteran monuments; parking lot; display of gardens; open grassy areas; owned and cared for by American Legion Post #178",
        "notes":          "Owned/maintained by American Legion Post #178; listed in City of Van Wert parks inventory.",
        "url_primary":    "https://vanwert.org/parks-department/memorial-park/",
        "urls":           "",
        "parent_site_id": "",
        "temp_id":        "VNW-T6-005",
    },
    {
        "site_id":        "VNW-S-013",
        "name":           "Fountain Park",
        "category":       "Park",
        "subtype":        "Civic Park",
        "designation":    "",
        "status":         "Active",
        "ownership":      "City of Van Wert",
        "governance":     "City of Van Wert",
        "partner_agencies": "Van Wert Evergreen Garden Club",
        "coordination":   "",
        "description":    "Downtown civic park rentable for events. Features Band Pavilion hosting Summer Music Series (Friday evenings June–August), gazebo with seasonal flower baskets maintained by Van Wert Evergreen Garden Club, concession stand, and restrooms.",
        "location":       "210 W Main St, Van Wert, OH 45891",
        "acres":          None,
        "counties":       "Van Wert",
        "municipality":   "Van Wert",
        "address":        "210 W Main St, Van Wert, OH 45891",
        "gps_lat":        None,
        "gps_lon":        None,
        "gps_confidence": "NONE",
        "features":       "Bandstand; Gazebo; Restrooms",
        "features_raw":   "Gazebo with hanging flower baskets (Van Wert Evergreen Garden Club); Band Pavilion (Summer Music Series Fridays June–August); concession stand; restrooms (open during scheduled activities); park benches; rentable",
        "notes":          "Rentable venue. Corner of W Main St & S Jefferson St downtown Van Wert. Restrooms seasonal (open during scheduled activities only).",
        "url_primary":    "https://vanwert.org/parks-department/fountain-park/",
        "urls":           "",
        "parent_site_id": "",
        "temp_id":        "VNW-T6-006",
    },
    {
        "site_id":        "VNW-S-014",
        "name":           "Rotary Athletic Complex",
        "category":       "Recreation Facility",
        "subtype":        "Sports Complex",
        "designation":    "",
        "status":         "Active",
        "ownership":      "City of Van Wert",
        "governance":     "City of Van Wert",
        "partner_agencies": "",
        "coordination":   "",
        "description":    "Multi-sport athletic complex featuring baseball/softball diamonds and soccer fields.",
        "location":       "9085 John Brown Rd, Van Wert, OH 45891",
        "acres":          None,
        "counties":       "Van Wert",
        "municipality":   "Van Wert",
        "address":        "9085 John Brown Rd, Van Wert, OH 45891",
        "gps_lat":        None,
        "gps_lon":        None,
        "gps_confidence": "NONE",
        "features":       "Ball Diamond; Soccer Pitch",
        "features_raw":   "Baseball/softball diamonds; soccer fields; Van Wert Rotary Club facility",
        "notes":          "Also listed as Rotary Athletic Park in some sources.",
        "url_primary":    "",
        "urls":           "https://visitvanwert.com/things-to-do/outdoor-adventure/",
        "parent_site_id": "",
        "temp_id":        "VNW-T6-007",
    },
    {
        "site_id":        "VNW-S-015",
        "name":           "Rotary Dog Park",
        "category":       "Park",
        "subtype":        "Dog Park",
        "designation":    "",
        "status":         "Active",
        "ownership":      "City of Van Wert",
        "governance":     "City of Van Wert",
        "partner_agencies": "",
        "coordination":   "",
        "description":    "Off-leash dog park with pavilion.",
        "location":       "1264 S Washington St, Van Wert, OH 45891",
        "acres":          None,
        "counties":       "Van Wert",
        "municipality":   "Van Wert",
        "address":        "1264 S Washington St, Van Wert, OH 45891",
        "gps_lat":        None,
        "gps_lon":        None,
        "gps_confidence": "NONE",
        "features":       "Dog Park; Pavilion",
        "features_raw":   "Off-leash dog park; pavilion",
        "notes":          "Not in baseline seeds; discovered via visitvanwert.com. Phone: 419-238-9121.",
        "url_primary":    "",
        "urls":           "https://visitvanwert.com/things-to-do/outdoor-adventure/",
        "parent_site_id": "",
        "temp_id":        "VNW-T6-008",
    },
    # ── Tier 6 — Municipal (Village of Ohio City) ────────────────────────────
    {
        "site_id":        "VNW-S-016",
        "name":           "Ohio City Fireman's Park",
        "category":       "Park",
        "subtype":        "",
        "designation":    "",
        "status":         "Active",
        "ownership":      "Village of Ohio City",
        "governance":     "Village of Ohio City",
        "partner_agencies": "",
        "coordination":   "",
        "description":    "Village park in Ohio City. Features and amenities undocumented; requires direct contact with Village of Ohio City for details.",
        "location":       "St. Rt. 118, Ohio City, OH 45874",
        "acres":          None,
        "counties":       "Van Wert",
        "municipality":   "Ohio City",
        "address":        "St. Rt. 118, Ohio City, OH 45874",
        "gps_lat":        None,
        "gps_lon":        None,
        "gps_confidence": "NONE",
        "features":       "",
        "features_raw":   "",
        "notes":          "DETAILS_INCOMPLETE: Village web presence minimal; contact Village of Ohio City at 419-965-2000 for park features.",
        "url_primary":    "",
        "urls":           "https://visitvanwert.com/things-to-do/outdoor-adventure/",
        "parent_site_id": "",
        "temp_id":        "VNW-T6-009",
    },
    # ── Tier 6 — Municipal (Village of Middle Point) ─────────────────────────
    {
        "site_id":        "VNW-S-017",
        "name":           "Middle Point Ball Park",
        "category":       "Recreation Facility",
        "subtype":        "Athletic Field",
        "designation":    "",
        "status":         "Active",
        "ownership":      "Village of Middle Point",
        "governance":     "Village of Middle Point",
        "partner_agencies": "",
        "coordination":   "",
        "description":    "Village baseball/softball park.",
        "location":       "406 N Adams St, Middle Point, OH 45863",
        "acres":          None,
        "counties":       "Van Wert",
        "municipality":   "Middle Point",
        "address":        "406 N Adams St, Middle Point, OH 45863",
        "gps_lat":        None,
        "gps_lon":        None,
        "gps_confidence": "NONE",
        "features":       "",
        "features_raw":   "Ball park/athletic field; Village of Middle Point",
        "notes":          "Not in baseline seeds; discovered via visitvanwert.com. Phone: 419-968-2427.",
        "url_primary":    "",
        "urls":           "https://visitvanwert.com/things-to-do/outdoor-adventure/",
        "parent_site_id": "",
        "temp_id":        "VNW-T6-011",
    },
    # ── Tier 7 — Conservancy ─────────────────────────────────────────────────
    {
        "site_id":        "VNW-S-018",
        "name":           "Hiestand Woods Park and Preserve",
        "category":       "Nature Preserve",
        "subtype":        "Private Nature Preserve",
        "designation":    "",
        "status":         "Active",
        "ownership":      "Van Wert County Foundation",
        "governance":     "Van Wert County Foundation",
        "partner_agencies": "",
        "coordination":   "",
        "description":    "78-acre nature preserve and park established in 1945 using Clara Anderson estate funds. Features shelter houses, playground, and nature preserve paths. Planned improvements include restrooms, expanded parking, water fountains, fitness stations, elevated boardwalk, and Ninja Warrior Challenge Course stations.",
        "location":       "1510 Hospital Dr, Van Wert, OH 45891",
        "acres":          78.0,
        "counties":       "Van Wert",
        "municipality":   "Van Wert",
        "address":        "1510 Hospital Dr, Van Wert, OH 45891",
        "gps_lat":        None,
        "gps_lon":        None,
        "gps_confidence": "NONE",
        "features":       "Covered Shelter; Playground",
        "features_raw":   "Shelter houses; playground; nature preserve paths (undocumented length/surface); planned: restrooms, expanded parking, water fountains, fitness stations, elevated boardwalk, Ninja Warrior Challenge Course",
        "notes":          "FIELD_VERIFY_NEEDED: nature preserve trail paths lack name, length, and surface documentation. Create Trail record when VWCF modernization data available. Purchased 1945, Clara Anderson estate.",
        "url_primary":    "https://vanwertcountyfoundation.org/impact/parks/hiestand-woods-park/",
        "urls":           "",
        "parent_site_id": "",
        "temp_id":        "VNW-T7-001",
    },
    # ── Tier 8 — Private ─────────────────────────────────────────────────────
    {
        "site_id":        "VNW-S-019",
        "name":           "Van-Del Drive-In",
        "category":       "Cultural Facility",
        "subtype":        "",
        "designation":    "",
        "status":         "Active",
        "ownership":      "Private",
        "governance":     "Private",
        "partner_agencies": "",
        "coordination":   "",
        "description":    "Private drive-in theater in Middle Point. In scope per IMP-073 (private entertainment venues including drive-in theaters are includable at Tier 8).",
        "location":       "19986 Lincoln Highway, Middle Point, OH 45863",
        "acres":          None,
        "counties":       "Van Wert",
        "municipality":   "Middle Point",
        "address":        "19986 Lincoln Highway, Middle Point, OH 45863",
        "gps_lat":        None,
        "gps_lon":        None,
        "gps_confidence": "NONE",
        "features":       "",
        "features_raw":   "Drive-in theater; private entertainment venue; Lincoln Highway / US 30 corridor; Middle Point OH",
        "notes":          "In scope per IMP-073. Tier 8 private. Baseline seed confirmed.",
        "url_primary":    "",
        "urls":           "",
        "parent_site_id": "",
        "temp_id":        "VNW-T8-001",
    },
]

TRAILS = [
    {
        "trail_id":        "VNW-T-001",
        "name":            "Convoy Rest Area Storybook Trail",
        "alternate_names": "US 30 Rest Area Storybook Trail; Dolly Parton Imagination Library Trail",
        "use_type":        "Hiking",
        "surface_type":    "Paved",
        "origin_type":     "Purpose-Built",
        "length_mi":       None,   # LENGTH_VERIFY_NEEDED
        "counties":        "Van Wert",
        "governance":      "Ohio Department of Transportation (ODOT)",
        "partner_agencies": "Dolly Parton's Imagination Library of Ohio",
        "status":          "Active",
        "difficulty":      "Easy",
        "accessibility":   "",
        "description":     "Outdoor storybook trail at the US 30 Eastbound Convoy rest area. Walking path with stands displaying pages from a children's book. Created in partnership with Dolly Parton's Imagination Library of Ohio.",
        "trail_history":   "",
        "identity_notes":  "Trail confirmed via governor's ribbon-cutting article (hometownstations.com, July 2025). Trail length not documented; ODOT contact or field measurement needed.",
        "notes":           "LENGTH_VERIFY_NEEDED: trail length not documented. Parent site: VNW-S-002 (Van Wert Rest Area — Eastbound).",
        "url_primary":     "https://hometownstations.com/van-wert/2025/07/governor-dewine-dedicates-renovated-us-30-van-wert-eastbound-rest-area/",
        "maps":            "",
        "parent_site_id":  "VNW-S-002",
        "temp_id":         "VNW-T2-004",
    },
    {
        "trail_id":        "VNW-T-002",
        "name":            "Van Wert Reservoir Health Trail",
        "alternate_names": "Reservoir Loop Trail",
        "use_type":        "Hiking",
        "surface_type":    "Paved",
        "origin_type":     "Purpose-Built",
        "length_mi":       3.1,
        "counties":        "Van Wert",
        "governance":      "City of Van Wert",
        "partner_agencies": "",
        "status":          "Active",
        "difficulty":      "Easy",
        "accessibility":   "ADA Accessible",
        "description":     "3.1-mile paved loop trail around the Van Wert Reservoir Recreation Area. Primarily used for walking and health/fitness.",
        "trail_history":   "",
        "identity_notes":  "",
        "notes":           "Parent site: VNW-S-007 (Van Wert Reservoir Recreation Area).",
        "url_primary":     "https://vanwert.org/parks-department/reservoir-recreation-area/",
        "maps":            "",
        "parent_site_id":  "VNW-S-007",
        "temp_id":         "VNW-T6-002c",
    },
    {
        "trail_id":        "VNW-T-003",
        "name":            "Warrior Trail",
        "alternate_names": "Ohio City Greenway",
        "use_type":        "Multi-Use",
        "surface_type":    "Mixed",
        "origin_type":     "Rail Trail",
        "length_mi":       2.6,
        "counties":        "Van Wert",
        "governance":      "Village of Ohio City",
        "partner_agencies": "",
        "status":          "Active",
        "difficulty":      "Easy",
        "accessibility":   "",
        "description":     "2.6-mile multi-use rail trail in Ohio City developed through the Ohio City Greenway Project. Asphalt and gravel surface on former rail corridor.",
        "trail_history":   "Developed on former rail corridor through the Ohio City Greenway Project.",
        "identity_notes":  "",
        "notes":           "Not in baseline seeds; discovered Tier 3 review. Managed by Village of Ohio City (Tier 6 Municipal).",
        "url_primary":     "",
        "maps":            "",
        "parent_site_id":  "",
        "temp_id":         "VNW-T6-010",
    },
]

ACCESS_POINTS = [
    {
        "access_point_id":  "VNW-AP-001",
        "name":             "Van Wert Reservoir Boat Launch",
        "ap_type":          "Boat Launch",
        "status":           "Active",
        "parent_entity_type": "Site",
        "parent_entity_id": "VNW-S-007",
        "county":           "Van Wert",
        "township":         "",
        "municipality":     "Van Wert",
        "address":          "S Washington St, Van Wert, OH 45891",
        "gps_lat":          None,
        "gps_lon":          None,
        "gps_confidence":   "NONE",
        "features":         "Handicap-accessible fishing pier; Boat permit required ($20/2yr)",
        "identity_notes":   "",
        "notes":            "Boat permit required; $20 for 2-year permit. Handicap-accessible fishing pier adjacent.",
        "url_primary":      "",
        "temp_id":          "VNW-T6-002d",
    },
]

# Entities with zero records (header-only TSVs)
TRAIL_SEGMENTS = []
TRAIL_NETWORKS = []
SITE_NETWORKS  = []


# ── GPS Acquisition (Stage 3) ─────────────────────────────────────────────────

def nominatim_geocode(query, county_hint="Van Wert County, Ohio"):
    """Query Nominatim; return (lat, lon) or (None, None)."""
    if not _REQUESTS_OK:
        return None, None
    params = {
        "q": query,
        "format": "json",
        "limit": 1,
        "countrycodes": "us",
    }
    try:
        resp = requests.get(NOMINATIM_URL, params=params, headers=NOMINATIM_HEADERS, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if data:
            lat = round(float(data[0]["lat"]), 6)
            lon = round(float(data[0]["lon"]), 6)
            # Plausibility: must be within expanded Ohio bounding box
            if 38.0 <= lat <= 42.5 and -85.5 <= lon <= -80.0:
                return lat, lon
    except Exception as e:
        print(f"  Nominatim error for '{query}': {e}")
    return None, None


def in_vnw_bbox(lat, lon):
    return (VNW_LAT_MIN <= lat <= VNW_LAT_MAX and
            VNW_LON_MIN <= lon <= VNW_LON_MAX)


GPS_QUERIES = {
    # site_id → Nominatim query string
    "VNW-S-002": "US 30 Eastbound Rest Area Van Wert County Ohio",
    "VNW-S-003": "US 30 Westbound Rest Area Van Wert County Ohio",
    "VNW-S-004": "643 N Main St Convoy Ohio",
    "VNW-S-005": "1451 Leeson Ave Van Wert Ohio",
    "VNW-S-006": "1409 Leeson Ave Van Wert Ohio",
    "VNW-S-007": "Van Wert Reservoir Recreation Area S Washington St Van Wert Ohio",
    "VNW-S-008": "Van Wert Reservoir 1 Van Wert Ohio",
    "VNW-S-010": "305 Frothingham St Van Wert Ohio",
    "VNW-S-011": "137 Gleason Ave Van Wert Ohio",
    "VNW-S-012": "611 W Main St Van Wert Ohio",
    "VNW-S-013": "210 W Main St Van Wert Ohio",
    "VNW-S-014": "9085 John Brown Rd Van Wert Ohio",
    "VNW-S-015": "1264 S Washington St Van Wert Ohio",
    "VNW-S-016": "Fireman's Park Ohio City Ohio",
    "VNW-S-017": "406 N Adams St Middle Point Ohio",
    "VNW-S-018": "1510 Hospital Dr Van Wert Ohio",
    "VNW-S-019": "19986 Lincoln Highway Middle Point Ohio",
    # Trails
    "VNW-T-003": "Warrior Trail Ohio City Ohio",
    # Access Points
    "VNW-AP-001": "Van Wert Reservoir Boat Launch Van Wert Ohio",
}

# Fallback centroids when Nominatim returns no result
HIGHWAY_FALLBACKS = {
    "VNW-S-002": (40.8655, -84.5940),   # US 30 MM9 EB approximate
    "VNW-S-003": (40.8653, -84.5938),   # US 30 MM9 WB approximate
    "VNW-S-007": (40.859117, -84.584631),  # S Washington St, Van Wert (Nominatim MED)
    "VNW-S-016": (40.771437, -84.615513),  # Ohio City village centroid (LOW)
    "VNW-S-019": (40.852000, -84.448000),  # US 30 / Lincoln Hwy near Middle Point (LOW)
}


def acquire_gps(entities, entity_id_field):
    """Attempt GPS acquisition for all entities lacking coordinates."""
    for ent in entities:
        eid = ent[entity_id_field]
        if ent.get("gps_lat") is not None:
            continue  # Already have GPS
        query = GPS_QUERIES.get(eid)
        if not query:
            continue

        print(f"  GPS [{eid}]: querying '{query}'")
        lat, lon = nominatim_geocode(query)
        time.sleep(NOMINATIM_DELAY)

        if lat is None and eid in HIGHWAY_FALLBACKS:
            lat, lon = HIGHWAY_FALLBACKS[eid]
            # S-007 came from a real Nominatim street geocode → MED; others → LOW
            conf = "MED" if eid == "VNW-S-007" else "LOW"
            print(f"  GPS [{eid}]: Nominatim null → using fallback {lat}, {lon} ({conf})")
            ent["gps_lat"] = lat
            ent["gps_lon"] = lon
            ent["gps_confidence"] = conf
        elif lat is not None:
            print(f"  GPS [{eid}]: acquired {lat}, {lon}")
            ent["gps_lat"] = lat
            ent["gps_lon"] = lon
            if ent.get("gps_confidence") == "NONE":
                ent["gps_confidence"] = "HIGH"
        else:
            print(f"  GPS [{eid}]: not acquired")


def propagate_parent_gps(entities):
    """For child sites still lacking GPS, use parent site GPS as LOW-confidence fallback."""
    id_map = {s["site_id"]: s for s in entities}
    for s in entities:
        if s.get("gps_lat") is None and s.get("parent_site_id"):
            parent = id_map.get(s["parent_site_id"])
            if parent and parent.get("gps_lat") is not None:
                s["gps_lat"] = parent["gps_lat"]
                s["gps_lon"] = parent["gps_lon"]
                s["gps_confidence"] = "LOW"
                print(f"  GPS [{s['site_id']}]: propagated from parent {s['parent_site_id']} (LOW)")


def propagate_trail_gps(trails, sites):
    """For trails lacking GPS, use parent site GPS as LOW-confidence fallback."""
    id_map = {s["site_id"]: s for s in sites}
    for t in trails:
        if t.get("gps_lat") is None and t.get("parent_site_id"):
            parent = id_map.get(t["parent_site_id"])
            if parent and parent.get("gps_lat") is not None:
                t["gps_lat"] = parent["gps_lat"]
                t["gps_lon"] = parent["gps_lon"]
                t["gps_confidence"] = "LOW"
                print(f"  GPS [{t['trail_id']}]: propagated from parent site {t['parent_site_id']} (LOW)")


def propagate_ap_gps(aps, sites):
    """For APs lacking GPS, use parent site GPS as LOW-confidence fallback."""
    id_map = {s["site_id"]: s for s in sites}
    for ap in aps:
        if ap.get("gps_lat") is None and ap.get("parent_entity_id"):
            parent = id_map.get(ap["parent_entity_id"])
            if parent and parent.get("gps_lat") is not None:
                ap["gps_lat"] = parent["gps_lat"]
                ap["gps_lon"] = parent["gps_lon"]
                ap["gps_confidence"] = "LOW"
                print(f"  GPS [{ap['access_point_id']}]: propagated from parent site (LOW)")


def add_plus_codes(entities, id_field):
    for ent in entities:
        lat = ent.get("gps_lat")
        lon = ent.get("gps_lon")
        if lat is not None and lon is not None:
            ent["plus_code"] = encode_plus_code(lat, lon)
        else:
            ent["plus_code"] = ""


def add_gis_lookup(entities, id_field):
    if not _LOOKUP_AVAILABLE:
        return
    for ent in entities:
        lat = ent.get("gps_lat")
        lon = ent.get("gps_lon")
        if lat is not None and lon is not None:
            try:
                result = _LOOKUP.lookup(lat, lon)
                if result:
                    if not ent.get("township"):
                        ent["township"] = result.get("township", "")
                    if not ent.get("municipality"):
                        ent["municipality"] = result.get("municipality", "")
            except Exception:
                pass


# ── Vocabulary Validation Gate (Stage 4.5) ────────────────────────────────────

def validate_sites(sites):
    errors = []
    for s in sites:
        sid = s["site_id"]
        # Category
        cat = s.get("category", "")
        if cat not in ALLOWED_CATEGORIES:
            errors.append(f"{sid}: invalid category '{cat}'")
        # Subtype
        sub = s.get("subtype", "")
        if sub:
            allowed_subs = ALLOWED_SUBTYPES.get(cat, set())
            if sub not in allowed_subs:
                errors.append(f"{sid}: invalid subtype '{sub}' for category '{cat}'")
        # Designation
        des = s.get("designation", "")
        if des and des not in ALLOWED_DESIGNATIONS:
            errors.append(f"{sid}: invalid designation '{des}'")
        # Status
        sta = s.get("status", "")
        if sta and sta not in ALLOWED_STATUSES:
            errors.append(f"{sid}: invalid status '{sta}'")
        # Features
        feats_str = s.get("features", "")
        if feats_str:
            for term in feats_str.split(";"):
                term = term.strip()
                if term and term not in ALLOWED_FEATURES:
                    errors.append(f"{sid}: invalid features term '{term}'")
    return errors


def validate_trails(trails):
    errors = []
    for t in trails:
        tid = t["trail_id"]
        for field, allowed in [
            ("use_type",    ALLOWED_TRAIL_USE_TYPES),
            ("surface_type", ALLOWED_TRAIL_SURFACES),
            ("origin_type", ALLOWED_TRAIL_ORIGINS),
            ("status",      ALLOWED_TRAIL_STATUSES),
            ("difficulty",  ALLOWED_TRAIL_DIFFICULTIES),
        ]:
            val = t.get(field, "")
            if val and val not in allowed:
                errors.append(f"{tid}: invalid {field} '{val}'")
    return errors


def validate_access_points(aps):
    errors = []
    for ap in aps:
        aid = ap["access_point_id"]
        if ap.get("ap_type", "") not in ALLOWED_AP_TYPES:
            errors.append(f"{aid}: invalid ap_type '{ap.get('ap_type', '')}'")
        if ap.get("status", "") not in ALLOWED_AP_STATUSES:
            errors.append(f"{aid}: invalid status '{ap.get('status', '')}'")
    return errors


# ── TSV Output (Stage 4) ──────────────────────────────────────────────────────

SITE_TSV_COLUMNS = [
    "name", "category", "subtype", "designation", "status",
    "ownership", "governance", "partner_agencies", "coordination",
    "description", "location", "acres", "counties", "municipality", "township",
    "gps_lat", "gps_lon", "plus_code", "features", "notes",
    "url_primary", "urls", "parent_site_id", "created_at", "updated_at",
]

TRAIL_TSV_COLUMNS = [
    "name", "alternate_names", "use_type", "surface_type", "origin_type",
    "length_mi", "counties", "governance", "partner_agencies",
    "status", "difficulty", "accessibility",
    "description", "trail_history", "identity_notes", "notes",
    "url_primary", "maps", "created_at", "updated_at",
]

TRAIL_SEGMENT_TSV_COLUMNS = [
    "name", "counties", "governance", "length_mi", "surface_type",
    "segment_type", "status", "difficulty", "accessibility",
    "description", "identity_notes", "notes", "url_primary", "maps",
    "geometry", "created_at", "updated_at",
]

TRAIL_NETWORK_TSV_COLUMNS = [
    "name", "network_type", "status", "ownership", "governance",
    "partner_agencies", "counties", "states_included", "length_mi",
    "member_trail_count", "member_trail_ids",
    "description", "identity_notes", "notes", "url_primary", "maps",
    "created_at", "updated_at",
]

SITE_NETWORK_TSV_COLUMNS = [
    "name", "network_type", "status", "ownership", "governance",
    "partner_agencies", "counties", "states_included",
    "member_count", "member_site_ids",
    "description", "identity_notes", "notes", "url_primary",
    "created_at", "updated_at",
]

AP_TSV_COLUMNS = [
    "name", "ap_type", "status",
    "parent_entity_type", "parent_entity_id",
    "county", "township", "municipality", "address",
    "gps_lat", "gps_lon", "plus_code", "features",
    "identity_notes", "notes", "url_primary",
    "created_at", "updated_at",
]


def write_tsv(filename, columns, rows):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns, delimiter="\t",
                                extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            # Stamp timestamps if not present
            row.setdefault("created_at", NOW)
            row.setdefault("updated_at", NOW)
            # Convert None to ""
            out = {k: ("" if v is None else v) for k, v in row.items()}
            writer.writerow(out)
    print(f"  Wrote {len(rows)} rows → {os.path.basename(path)}")
    return path


# ── Integrity Check (Stage 5) ─────────────────────────────────────────────────

def integrity_check(sites, trails, aps):
    warnings = []
    known_site_ids = {s["site_id"] for s in sites}

    # Missing GPS
    no_gps_sites = [s["site_id"] for s in sites if s.get("gps_lat") is None]
    if no_gps_sites:
        warnings.append(f"Sites missing GPS ({len(no_gps_sites)}): {', '.join(no_gps_sites)}")

    # Parent site IDs valid
    for s in sites:
        psid = s.get("parent_site_id", "")
        if psid and psid not in known_site_ids:
            warnings.append(f"{s['site_id']}: parent_site_id '{psid}' not in this run")

    for t in trails:
        psid = t.get("parent_site_id", "")
        if psid and psid not in known_site_ids:
            warnings.append(f"{t['trail_id']}: parent_site_id '{psid}' not in this run")

    for ap in aps:
        peid = ap.get("parent_entity_id", "")
        if peid and peid not in known_site_ids:
            warnings.append(f"{ap['access_point_id']}: parent_entity_id '{peid}' not in this run")

    # Duplicate IDs
    site_ids = [s["site_id"] for s in sites]
    dups = [sid for sid in site_ids if site_ids.count(sid) > 1]
    if dups:
        warnings.append(f"Duplicate site IDs: {set(dups)}")

    trail_ids = [t["trail_id"] for t in trails]
    dups = [tid for tid in trail_ids if trail_ids.count(tid) > 1]
    if dups:
        warnings.append(f"Duplicate trail IDs: {set(dups)}")

    return warnings


# ── Database Upsert (Stage 6) ──────────────────────────────────────────────────

def upsert_sites(cur, sites, dry_run):
    sql = """
    INSERT INTO sites (
        site_id, name, category, subtype, designation, status,
        ownership, governance, partner_agencies, coordination,
        description, location, acres, counties, municipality, township,
        gps_lat, gps_lon, plus_code, features, features_raw, notes,
        url_primary, urls, parent_site_id, created_at, updated_at
    ) VALUES (
        :site_id, :name, :category, :subtype, :designation, :status,
        :ownership, :governance, :partner_agencies, :coordination,
        :description, :location, :acres, :counties, :municipality, :township,
        :gps_lat, :gps_lon, :plus_code, :features, :features_raw, :notes,
        :url_primary, :urls, :parent_site_id, :created_at, :updated_at
    )
    ON CONFLICT(site_id) DO UPDATE SET
        name=excluded.name, category=excluded.category, subtype=excluded.subtype,
        designation=excluded.designation, status=excluded.status,
        ownership=excluded.ownership, governance=excluded.governance,
        partner_agencies=excluded.partner_agencies, coordination=excluded.coordination,
        description=excluded.description, location=excluded.location,
        acres=excluded.acres, counties=excluded.counties,
        municipality=excluded.municipality, township=excluded.township,
        gps_lat=excluded.gps_lat, gps_lon=excluded.gps_lon, plus_code=excluded.plus_code,
        features=excluded.features, features_raw=excluded.features_raw,
        notes=excluded.notes, url_primary=excluded.url_primary, urls=excluded.urls,
        parent_site_id=excluded.parent_site_id, updated_at=excluded.updated_at
    """
    for s in sites:
        row = dict(s)
        row.setdefault("created_at", NOW)
        row.setdefault("updated_at", NOW)
        # Nullify empty strings for numeric fields
        for nf in ("acres", "gps_lat", "gps_lon"):
            if row.get(nf) == "":
                row[nf] = None
        if dry_run:
            print(f"  [DRY-RUN] UPSERT site {row['site_id']} — {row['name']}")
        else:
            cur.execute(sql, row)


def upsert_site_parents(cur, sites, dry_run):
    for s in sites:
        if s.get("parent_site_id"):
            sql = """
            INSERT OR IGNORE INTO site_parent (site_id, parent_site_id)
            VALUES (?, ?)
            """
            if dry_run:
                print(f"  [DRY-RUN] site_parent {s['site_id']} → {s['parent_site_id']}")
            else:
                cur.execute(sql, (s["site_id"], s["parent_site_id"]))


def upsert_trails(cur, trails, dry_run):
    sql = """
    INSERT INTO trails (
        trail_id, name, alternate_names, use_type, surface_type, origin_type,
        length_mi, counties, governance, partner_agencies,
        status, difficulty, accessibility,
        description, trail_history, identity_notes, notes,
        url_primary, maps, created_at, updated_at
    ) VALUES (
        :trail_id, :name, :alternate_names, :use_type, :surface_type, :origin_type,
        :length_mi, :counties, :governance, :partner_agencies,
        :status, :difficulty, :accessibility,
        :description, :trail_history, :identity_notes, :notes,
        :url_primary, :maps, :created_at, :updated_at
    )
    ON CONFLICT(trail_id) DO UPDATE SET
        name=excluded.name, alternate_names=excluded.alternate_names,
        use_type=excluded.use_type, surface_type=excluded.surface_type,
        origin_type=excluded.origin_type, length_mi=excluded.length_mi,
        counties=excluded.counties, governance=excluded.governance,
        partner_agencies=excluded.partner_agencies,
        status=excluded.status, difficulty=excluded.difficulty,
        accessibility=excluded.accessibility,
        description=excluded.description, trail_history=excluded.trail_history,
        identity_notes=excluded.identity_notes, notes=excluded.notes,
        url_primary=excluded.url_primary, maps=excluded.maps,
        updated_at=excluded.updated_at
    """
    for t in trails:
        row = dict(t)
        row.setdefault("created_at", NOW)
        row.setdefault("updated_at", NOW)
        if row.get("length_mi") == "":
            row["length_mi"] = None
        if dry_run:
            print(f"  [DRY-RUN] UPSERT trail {row['trail_id']} — {row['name']}")
        else:
            cur.execute(sql, row)


def upsert_trail_parents(cur, trails, dry_run):
    for t in trails:
        if t.get("parent_site_id"):
            sql = """
            INSERT OR IGNORE INTO trail_parents (trail_id, parent_site_id)
            VALUES (?, ?)
            """
            if dry_run:
                print(f"  [DRY-RUN] trail_parent {t['trail_id']} → {t['parent_site_id']}")
            else:
                cur.execute(sql, (t["trail_id"], t["parent_site_id"]))


def upsert_access_points(cur, aps, dry_run):
    sql = """
    INSERT INTO access_points (
        access_point_id, name, ap_type, status,
        parent_entity_type, parent_entity_id,
        county, township, municipality, address,
        gps_lat, gps_lon, plus_code, features,
        identity_notes, notes, url_primary,
        created_at, updated_at
    ) VALUES (
        :access_point_id, :name, :ap_type, :status,
        :parent_entity_type, :parent_entity_id,
        :county, :township, :municipality, :address,
        :gps_lat, :gps_lon, :plus_code, :features,
        :identity_notes, :notes, :url_primary,
        :created_at, :updated_at
    )
    ON CONFLICT(access_point_id) DO UPDATE SET
        name=excluded.name, ap_type=excluded.ap_type, status=excluded.status,
        parent_entity_type=excluded.parent_entity_type,
        parent_entity_id=excluded.parent_entity_id,
        county=excluded.county, township=excluded.township,
        municipality=excluded.municipality, address=excluded.address,
        gps_lat=excluded.gps_lat, gps_lon=excluded.gps_lon, plus_code=excluded.plus_code,
        features=excluded.features, identity_notes=excluded.identity_notes,
        notes=excluded.notes, url_primary=excluded.url_primary,
        updated_at=excluded.updated_at
    """
    for ap in aps:
        row = dict(ap)
        row.setdefault("created_at", NOW)
        row.setdefault("updated_at", NOW)
        for nf in ("gps_lat", "gps_lon"):
            if row.get(nf) == "":
                row[nf] = None
        if dry_run:
            print(f"  [DRY-RUN] UPSERT AP {row['access_point_id']} — {row['name']}")
        else:
            cur.execute(sql, row)


def upsert_run_metadata(cur, sites, trails, aps, dry_run):
    records_input = 23  # Total raw records in discovery YAML
    normalized = len(sites) + len(trails) + len(aps)
    held = 0
    notes = (
        "Van Wert County OH pipeline complete. "
        "19 Sites, 3 Trails, 1 Access Point. "
        "Non-blocking flags: GPS_VERIFY_NEEDED (VNW-S-001, VNW-S-008), "
        "STORYBOOK_TRAIL_CONFIRM_NEEDED (VNW-S-003 WB), "
        "LENGTH_VERIFY_NEEDED (VNW-T-001), "
        "DETAILS_INCOMPLETE (VNW-S-016), "
        "FIELD_VERIFY_NEEDED (VNW-S-018 trail paths)."
    )
    sql = """
    INSERT INTO run_metadata (run_id, county, state, run_date, records_input,
                              normalized, held, notes, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(run_id) DO UPDATE SET
        normalized=excluded.normalized, held=excluded.held,
        notes=excluded.notes
    """
    if dry_run:
        print(f"  [DRY-RUN] run_metadata {RUN_ID} — normalized={normalized} held={held}")
    else:
        cur.execute(sql, (RUN_ID, COUNTY, STATE, RUN_DATE,
                          records_input, normalized, held, notes, NOW))


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Van Wert County OH — NAP Pipeline")
    parser.add_argument("--db", default=DEFAULT_DB, help="Path to SQLite database")
    parser.add_argument("--dry-run", action="store_true",
                        help="Write TSVs but do not modify database")
    args = parser.parse_args()

    print("=" * 60)
    print(f"Van Wert County OH — NAP Pipeline  ({RUN_ID})")
    print(f"DB: {args.db}")
    print(f"Dry run: {args.dry_run}")
    print("=" * 60)

    # ── Stage 2: Normalization complete (hardcoded above) ────────────────────
    print("\n[Stage 2] Normalization — complete (19 Sites, 3 Trails, 1 AP)")

    # Stamp timestamps and ensure all expected fields exist
    for ent in SITES:
        ent.setdefault("created_at", NOW)
        ent.setdefault("updated_at", NOW)
        ent.setdefault("township", "")
        ent.setdefault("plus_code", "")
    for ent in TRAILS + ACCESS_POINTS:
        ent.setdefault("created_at", NOW)
        ent.setdefault("updated_at", NOW)
    for t in TRAILS:
        t.setdefault("gps_lat", None)
        t.setdefault("gps_lon", None)
        t.setdefault("gps_confidence", "NONE")
    for ap in ACCESS_POINTS:
        ap.setdefault("plus_code", "")

    # ── Stage 3: GPS Acquisition ─────────────────────────────────────────────
    print("\n[Stage 3] GPS Acquisition")
    if _REQUESTS_OK:
        acquire_gps(SITES, "site_id")
        propagate_parent_gps(SITES)
        propagate_trail_gps(TRAILS, SITES)
        propagate_ap_gps(ACCESS_POINTS, SITES)
    else:
        print("  Skipped (requests not available)")
        propagate_parent_gps(SITES)
        propagate_trail_gps(TRAILS, SITES)
        propagate_ap_gps(ACCESS_POINTS, SITES)

    # Plus codes
    add_plus_codes(SITES, "site_id")
    add_plus_codes(TRAILS, "trail_id")
    add_plus_codes(ACCESS_POINTS, "access_point_id")

    # GIS lookup
    add_gis_lookup(SITES, "site_id")

    # GPS acquisition summary
    gps_acquired = sum(1 for s in SITES if s.get("gps_lat") is not None)
    print(f"  GPS acquired: {gps_acquired}/{len(SITES)} sites")

    # ── Stage 4.5: Vocabulary Validation Gate ────────────────────────────────
    print("\n[Stage 4.5] Vocabulary Validation Gate")
    all_errors = []
    all_errors.extend(validate_sites(SITES))
    all_errors.extend(validate_trails(TRAILS))
    all_errors.extend(validate_access_points(ACCESS_POINTS))

    if all_errors:
        print("FATAL: Vocabulary validation FAILED — halting pipeline.")
        for err in all_errors:
            print(f"  ERROR: {err}")
        sys.exit(1)
    else:
        print("  All vocabulary checks PASSED.")

    # ── Stage 4: TSV Output ──────────────────────────────────────────────────
    print("\n[Stage 4] TSV Output")
    write_tsv("van_wert_oh_sites.tsv",          SITE_TSV_COLUMNS,         SITES)
    write_tsv("van_wert_oh_trails.tsv",         TRAIL_TSV_COLUMNS,        TRAILS)
    write_tsv("van_wert_oh_trail_segments.tsv", TRAIL_SEGMENT_TSV_COLUMNS, TRAIL_SEGMENTS)
    write_tsv("van_wert_oh_trail_networks.tsv", TRAIL_NETWORK_TSV_COLUMNS, TRAIL_NETWORKS)
    write_tsv("van_wert_oh_site_networks.tsv",  SITE_NETWORK_TSV_COLUMNS,  SITE_NETWORKS)
    write_tsv("van_wert_oh_access_points.tsv",  AP_TSV_COLUMNS,           ACCESS_POINTS)

    # ── Stage 5: Integrity Check ──────────────────────────────────────────────
    print("\n[Stage 5] Integrity Check")
    warnings = integrity_check(SITES, TRAILS, ACCESS_POINTS)
    if warnings:
        for w in warnings:
            print(f"  WARNING: {w}")
    else:
        print("  No integrity issues found.")

    # ── Stage 6: Database Upsert ─────────────────────────────────────────────
    print("\n[Stage 6] Database Upsert")
    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    try:
        upsert_sites(cur, SITES, args.dry_run)
        upsert_site_parents(cur, SITES, args.dry_run)
        upsert_trails(cur, TRAILS, args.dry_run)
        upsert_trail_parents(cur, TRAILS, args.dry_run)
        upsert_access_points(cur, ACCESS_POINTS, args.dry_run)
        upsert_run_metadata(cur, SITES, TRAILS, ACCESS_POINTS, args.dry_run)
        if not args.dry_run:
            conn.commit()
            print(f"  Committed {len(SITES)} sites, {len(TRAILS)} trails, "
                  f"{len(ACCESS_POINTS)} APs to {os.path.basename(args.db)}")
    except Exception as e:
        conn.rollback()
        print(f"  ERROR during upsert: {e}", file=sys.stderr)
        raise
    finally:
        conn.close()

    print("\n" + "=" * 60)
    print("PIPELINE COMPLETE")
    print(f"  Sites:         {len(SITES)}")
    print(f"  Trails:        {len(TRAILS)}")
    print(f"  Trail Segments: {len(TRAIL_SEGMENTS)}")
    print(f"  Trail Networks: {len(TRAIL_NETWORKS)}")
    print(f"  Site Networks:  {len(SITE_NETWORKS)}")
    print(f"  Access Points: {len(ACCESS_POINTS)}")
    gps_missing = [s["site_id"] for s in SITES if s.get("gps_lat") is None]
    if gps_missing:
        print(f"  Sites still missing GPS: {', '.join(gps_missing)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
