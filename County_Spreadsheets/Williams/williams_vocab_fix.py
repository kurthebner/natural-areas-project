"""
Williams County — Vocabulary Correction Script
Reads existing TSVs, applies all controlled vocabulary fixes, rewrites TSVs, updates DB.
No YAML needed — operates on the already-generated TSV files.
"""

import sys
import csv
import sqlite3
import os
from datetime import datetime, timezone

NAP_ROOT   = "/sessions/wonderful-confident-franklin/mnt/Natural Areas Project v5"
WILLIAMS   = os.path.join(NAP_ROOT, "County_Spreadsheets", "Williams")
PROD_DB    = os.path.join(NAP_ROOT, "NASqlite", "natural_areas_v5.db")
RUN_TS     = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
RUN_ID     = "williams_oh_2026_04_12"

# ============================================================
# CONTROLLED VOCABULARY — COMPLETE FEATURE SET (v5.5 §6.2)
# ============================================================
VALID_FEATURES = {
    "ADA Accessible", "AED", "Alvar", "Amphibian Area", "Amphitheater",
    "Apiary", "Arboretum", "Archery Range", "Art Gallery", "Art Installation",
    "Athletic Field", "Ball Diamond", "Ballroom", "Bandstand", "Basketball Court",
    "Beach", "Bike Rack", "Bike Repair Station", "Bird Viewing Area", "Boardwalk",
    "Boat Dock", "Boat Ramp", "Bocce Court", "Bog", "Bluff", "Boathouse", "Bridge",
    "Bridle Trail", "Building Ruins", "Butterfly or Pollinator Garden", "Camping",
    "Canal Structure", "Cave or Cavern", "Cemetery Section", "Chapel", "Cliff",
    "Climbing Structure", "Community Center", "Community Garden", "Composting Station",
    "Conservatory", "Covered Shelter", "Cricket Pitch", "Culvert", "Dam",
    "Dance Floor", "Dance Performance Space", "Demonstration Farm Plot",
    "Demonstration Garden", "Disc Golf Course", "Dog Park", "Drainage Ditch",
    "Dune", "Educational Pavilion", "Electric Vehicle Charging", "Equestrian Arena",
    "Fence", "Fen", "Fieldhouse", "Fire Ring", "Fire Tower", "Fishing Area",
    "Fitness Station", "Football Field", "Football Stadium", "Fountain", "Garage",
    "Garden", "Gate", "Gatehouse", "Gazebo", "Glacial Erratic", "Golf Course",
    "Gorge", "Greenhouse", "Grill", "Habitat Restoration Area", "Handball Court",
    "Hiking Trail", "Hilltop", "Historic Bridge", "Historic Canal Segment",
    "Historic Cemetery Section", "Historic Fence Line", "Historic Foundation",
    "Historic Lock", "Historic Marker", "Historic Marker Cluster",
    "Historic Millrace", "Historic Road Trace", "Historic Ruins",
    "Historic Structure", "Historic Well", "Horseshoe Pitch", "Hunting Area",
    "Ice Rink", "Information Board", "Insectarium", "Interpretive Exhibit",
    "Interpretive Garden", "Interpretive Sign", "Island", "Kiosk", "Kite Flying",
    "Lacrosse Field", "Lake", "Landmark Tree", "Levee", "Lodge", "Lookout Cabin",
    "Maintenance Building", "Marina", "Marsh", "Meadow", "Model Airplane Field",
    "Model Rocketry Field", "Mini Golf", "Monitoring Station", "Monument",
    "Mountain Bike Trail", "Multi-use Trail", "Museum Building",
    "Musical Instruments", "Musical Performance Space", "Native American Artifacts",
    "Native American Cultural Site", "Native American Earthwork", "Natural Arch",
    "Nature Center", "Nature Play Area", "Observation Deck", "Observation Tower",
    "Observatory", "Old-Growth Stand", "Orchard", "Outdoor Art Installation",
    "Outdoor Classroom", "Overflow Parking", "Overlook (built)", "Overlook (natural)",
    "Parking Lot", "Pavilion", "Peninsula", "Pickleball Court", "Picnic Area",
    "Picnic Shelter", "Picnic Table Cluster", "Pipeline Corridor",
    "Pioneer Historic Site", "Pioneer Re-creation", "Planetarium", "Playground",
    "Pollinator Garden", "Pond", "Powerline Corridor", "Prairie",
    "Prairie Restoration", "Public Art Installation", "Pump Station", "Pump Track",
    "Rain Garden", "Ravine", "Reforestation Area", "Reptile House", "Research Plot",
    "Restrooms", "Retaining Wall", "Retention Basin", "Ridge", "Rock Outcrop",
    "Scenic View", "S&M Dungeon", "Sculpture", "Sedge Meadow", "Shooting Range",
    "Shotgun Range", "Shuffleboard Court", "Silo", "Sinkhole", "Ski Slopes",
    "Skate Park", "Sledding Hill", "Slide", "Soccer Pitch", "Spillway",
    "Spray Park", "Spring", "Stable", "Stage", "Stormwater Basin",
    "Stream Segment", "Swimming Beach", "Swimming Pool", "Swing Set",
    "Tennis Court", "Theatre", "Topiary", "Trapping Area", "Transit Stop",
    "Trolley", "Tropical Garden", "Utility Corridor", "Valley",
    "Vegetable Garden", "Via Ferrata", "Viewing Platform", "Vineyard",
    "Visitor Center", "Volleyball Court", "Wall", "Water Park", "Water Tower",
    "Watercraft Access", "Waterfall (built)", "Waterfall (natural)", "Waterslide",
    "Weather Station", "Weir", "Wetland", "Wetland Restoration",
    "Wilderness Area", "Wild Animal Rehabilitation", "Wildlife Observation Area",
    "Working Railway", "Zoo",
}

# Valid categories (v5.5 §2.1)
VALID_CATEGORIES = {
    "Campground", "Cemetery", "Community Garden", "Conservation Area",
    "Cultural Facility", "Curated Biological Site", "Fishing Area", "Historic Site",
    "Hunting Area", "Memorial", "Museum", "Natural Area", "Nature Preserve",
    "Open Space", "Park", "Recreation Facility", "Water Site", "Wildlife Area",
}

# Valid subtypes per category (v5.5 §3.2)
VALID_SUBTYPES = {
    "Park": {"Greenspace", "Neighborhood Park", "Linear Park", "Dog Park",
             "Playground Park", "Sports Park", "Waterfront Park", "Civic Park", "Historic Park"},
    "Natural Area": {"Forest", "Upland Forest", "Floodplain Forest", "Prairie", "Grassland",
                     "Meadow", "Shrubland", "Savanna", "Old Field", "Successional Area",
                     "Wetland", "Marsh", "Fen", "Bog", "Swamp", "Riparian Area",
                     "Ravine", "Cliff or Bluff", "Barrens", "Dune"},
    "Nature Preserve": {"State Nature Preserve", "Private Nature Preserve"},
    "Wildlife Area": {"State Wildlife Area", "Federal Wildlife Area", "Waterfowl Area",
                      "Migratory Bird Area", "Wetland Management Area"},
    "Campground": {"Tent Campground", "RV Campground", "Primitive Campground",
                   "Group Campground", "Cabin Campground"},
    "Water Site": {"Lake", "Pond", "Reservoir", "River", "Harbor", "Marina",
                   "Boat Launch Area", "Fishing Lake", "Retention Pond"},
}

# Valid designations (v5.5 §4)
VALID_DESIGNATIONS = {
    "National Park", "National Monument", "National Historic Site", "National Memorial",
    "National Historic Landmark", "National Natural Landmark", "National Recreation Area",
    "National Wildlife Refuge", "National Scenic Trail", "National Wild and Scenic River",
    "National Heritage Area", "National Battlefield", "National Cemetery",
    "National Register of Historic Places (NRHP)",
    "State Park", "State Nature Preserve", "State Wildlife Area", "State Fishing Area",
    "State Hunting Area", "State Memorial", "State Forest", "State Scenic River",
    "State Natural Landmark", "State Archaeological Preserve", "State Historic Site",
    "State Recreation Area",
    "County Historic Landmark", "Municipal Historic Landmark", "Local Historic Landmark",
    "Local Nature Preserve", "Registered Cemetery", "Protected Wetland", "Mitigation Bank",
    "Conservation Easement", "Land Trust Preserve", "None", "",
}

# ============================================================
# CATEGORY / SUBTYPE / DESIGNATION CORRECTION MAP
# keyed by site name; value: (new_category, new_subtype, new_designation)
# Only entries where corrections are needed from v2 values.
# ============================================================
SITE_CORRECTIONS = {
    # Category "Private Reserve" → correct category per entity:
    "Pioneer Scout Reservation": ("Campground", "", ""),
    "Lake Seneca Beach":         ("Water Site", "Lake", ""),
    "Memory Point Park":         ("Park", "Neighborhood Park", ""),
    # Category "Natural Feature" → "Natural Area" per IMP-063
    "Davis Woods":               ("Natural Area", "Forest", ""),
    # Designation "Wildlife Area" → "State Wildlife Area"
    # Subtype "Wildlife Area" → "State Wildlife Area"
    "Lake La Su An Wildlife Area":         ("Wildlife Area", "State Wildlife Area", "State Wildlife Area"),
    "Fish Creek Wildlife Area":            ("Wildlife Area", "State Wildlife Area", "State Wildlife Area"),
    "Parkersburg Wildlife Area":           ("Wildlife Area", "State Wildlife Area", "State Wildlife Area"),
    "St. Joseph River Wildlife Area":      ("Wildlife Area", "State Wildlife Area", "State Wildlife Area"),
    "Nettle Lake Wildlife Area":           ("Wildlife Area", "State Wildlife Area", "State Wildlife Area"),
    "Goldie Newman Park/Wildlife Area":    ("Wildlife Area", "State Wildlife Area", ""),
    # Park subtype corrections per §7.3
    # "County Park" → null (no vocab equivalent)
    "Opdycke Park":              ("Park", "", ""),
    "George Bible Park":         ("Park", "", ""),
    # "Township Park" → null
    "Springfield Township Park": ("Park", "", ""),
    # "City Park" → "Neighborhood Park"
    "Recreation Park":           ("Park", "Neighborhood Park", ""),
    "East End Park and Pool":    ("Park", "Neighborhood Park", ""),
    "Garver Park":               ("Park", "Neighborhood Park", ""),
    "Moore Park and Pool":       ("Park", "Neighborhood Park", ""),
    "Maple Grove Park":          ("Park", "Neighborhood Park", ""),
    "Roseland Park":             ("Park", "Neighborhood Park", ""),
    "Fountain City Park":        ("Park", "Neighborhood Park", ""),
    "Hitt Park":                 ("Park", "Neighborhood Park", ""),
    "Mattie Marsh Park":         ("Park", "Neighborhood Park", ""),
    "Israel Gardens Butterfly Park": ("Park", "Neighborhood Park", ""),
    "Central Park":              ("Park", "Neighborhood Park", ""),
    # "Village Park" → "Neighborhood Park"
    "Montpelier Municipal Park":        ("Park", "Neighborhood Park", ""),
    "Main Street Park":                 ("Park", "Neighborhood Park", ""),
    "Robert A. Storrer Municipal Park": ("Park", "Neighborhood Park", ""),
    "Founders Park":                    ("Park", "Neighborhood Park", ""),
    "Miller Park":                      ("Park", "Neighborhood Park", ""),
    "Gerhart Park":                     ("Park", "Neighborhood Park", ""),
    "Downtown Park":                    ("Park", "Neighborhood Park", ""),
    "Puppy Pound Park":                 ("Park", "Neighborhood Park", ""),
    "Walz Park":                        ("Park", "Neighborhood Park", ""),
    "Edon Community Park":              ("Park", "Neighborhood Park", ""),
    "Harold C Baker Park":              ("Park", "Neighborhood Park", ""),
    "Leanne Field":                     ("Park", "Neighborhood Park", ""),
    "Beard Park":                       ("Park", "Neighborhood Park", ""),
    "Cannonball Park":                  ("Park", "Neighborhood Park", ""),
    "Crommer Park":                     ("Park", "Neighborhood Park", ""),
    "Fred Wyman Field":                 ("Park", "Neighborhood Park", ""),
    "Pioneer Memorial Park":            ("Park", "Neighborhood Park", ""),
    "West Unity Memorial Park":         ("Park", "Neighborhood Park", ""),
    # "Community Park" → "Neighborhood Park"
    "Alvordton Community Park":         ("Park", "Neighborhood Park", ""),
    # "Conservancy Preserve" → "Private Nature Preserve"
    "St. Joseph River Confluence Preserve": ("Nature Preserve", "Private Nature Preserve", ""),
    "St. Joseph River Floodplain Preserve": ("Nature Preserve", "Private Nature Preserve", ""),
    # Mud Lake Bog: no category correction needed (already Nature Preserve / State Nature Preserve)
}

# ============================================================
# FEATURES NORMALIZATION
# Maps raw text patterns (case-insensitive substring) → controlled vocab term
# ============================================================
_FEATURE_PATTERNS = [
    (["ada accessible", "ada restrooms", " ada "], "ADA Accessible"),
    (["amphitheater"], "Amphitheater"),
    (["archery range", "archery"], "Archery Range"),
    (["ball diamond", "baseball", "softball diamond", "softball field",
      "2 ball fields", "5 baseball", "ball fields", "multiple baseball",
      "batting cage"], "Ball Diamond"),
    (["basketball court", "basketball courts", "1 basketball", "basketball"],
     "Basketball Court"),
    (["beach", "swimming beach", "private beach"], "Beach"),
    (["boardwalk trail", "boardwalk"], "Boardwalk"),
    (["boat dock", "dock"], "Boat Dock"),
    (["boat ramp", "boat ramps"], "Boat Ramp"),
    (["butterfly", "pollinator garden", "children's garden", "butterfly park",
      "butterfly park"], "Butterfly or Pollinator Garden"),
    (["camping", "primitive camping", "camp frontier"], "Camping"),
    (["community center", "community center (under construction"], "Community Center"),
    (["covered shelter", "enclosed shelter", "open-air shelter",
      "outdoor shelter", "ivan e. day", "indoor pavilion"], "Covered Shelter"),
    (["disc golf", "18-hole disc golf"], "Disc Golf Course"),
    (["dog park", "off-leash"], "Dog Park"),
    (["equestrian", "horse trailer", "mounting block", "bridle trail"],
     "Equestrian Arena"),
    (["fishing", "public fishing"], "Fishing Area"),
    (["fountain"], "Fountain"),
    (["flower garden", "flower gardens", "gardens", "garden"], "Garden"),
    (["gazebo"], "Gazebo"),
    (["golf course", "driving/chipping hill"], "Golf Course"),
    (["grill"], "Grill"),
    (["agricultural fields (being restored)", "habitat restoration"],
     "Habitat Restoration Area"),
    (["hiking trail", "nature trail", "walking trail",
      "paved path", "paved paths", "walking path", "walking paths",
      "trailhead access", "trail"], "Hiking Trail"),
    (["historic cemetery", "louden cemetery"], "Historic Cemetery Section"),
    (["bank barn", "historic structure", "building ruin"], "Historic Structure"),
    (["hunting"], "Hunting Area"),
    (["kiosk", "information kiosk", "information board"], "Kiosk"),
    (["lake", "two lakes", "lake access"], "Lake"),
    (["amphibian area", "forested wetlands", "wetlands", "wetland",
      "marsh"], "Wetland"),
    (["meadow", "floodplain"], "Meadow"),
    (["observation deck"], "Observation Deck"),
    (["large parking lot", "parking lot", "parking area", "parking"],
     "Parking Lot"),
    (["george bible pavilion", "3 pavilions", "pavilion (rentable",
      "pavilion"], "Pavilion"),
    (["pickleball court", "pickleball courts", "3 pickleball"], "Pickleball Court"),
    (["picnic area", "picnic shelter", "picnic table",
      "picnic areas", "picnic shelters"], "Picnic Area"),
    (["playground", "play equipment", "2 playgrounds", "leisure playground",
      "imagination station", "gaga ball pit", "nature play"], "Playground"),
    (["two ponds", "fishing pond", "pond"], "Pond"),
    (["restroom", "flush toilet", "restrooms (key"], "Restrooms"),
    (["skate park"], "Skate Park"),
    (["sledding hill", "sledding"], "Sledding Hill"),
    (["soccer field", "soccer pitch", "soccer"], "Soccer Pitch"),
    (["splash pad", "spray park"], "Spray Park"),
    (["stage", "bandstand"], "Stage"),
    (["east end pool", "moore pool", "public pool", "swimming pool",
      "water slide", "aquatic center", "swim"], "Swimming Pool"),
    (["tennis court", "tennis courts", "1 tennis", "2 tennis"], "Tennis Court"),
    (["sand volleyball", "volleyball court", "volleyball courts"],
     "Volleyball Court"),
    (["canoe", "canoeing", "kayak", "watercraft", "river access"], "Watercraft Access"),
    (["wildlife habitat", "wildlife sanctuary", "wildlife observation"],
     "Wildlife Observation Area"),
    (["rock climbing", "rappelling"], "Climbing Structure"),
    (["amphitheater"], "Amphitheater"),
]


def normalize_features(raw):
    if not raw:
        return ""
    raw_lower = raw.lower()
    matched = set()
    for patterns, term in _FEATURE_PATTERNS:
        assert term in VALID_FEATURES, f"BUG: {term!r} not in vocabulary"
        if any(p in raw_lower for p in patterns):
            matched.add(term)
    # Amphitheater subsumes Stage for open-air performance venues
    if "Amphitheater" in matched:
        matched.discard("Stage")
    return "; ".join(sorted(matched))


# ============================================================
# APPLY CORRECTIONS TO SITES TSV
# ============================================================
sites_path = os.path.join(WILLIAMS, "williams_oh_sites.tsv")
with open(sites_path, encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter="\t")
    fieldnames = reader.fieldnames
    sites = list(reader)

SITE_HEADER = [
    "name", "category", "subtype", "designation", "status",
    "ownership", "governance", "partner_agencies", "coordination",
    "description", "location", "acres", "counties", "municipality", "township",
    "gps_lat", "gps_lon", "plus_code", "features", "notes",
    "url_primary", "urls", "parent_site_id", "created_at", "updated_at"
]

print("=" * 60)
print("Williams County — Vocabulary Correction")
print("=" * 60)
print(f"\nSites to correct: {len(sites)}")

corrected_sites = []
for s in sites:
    name = s["name"]

    # Apply category/subtype/designation corrections
    if name in SITE_CORRECTIONS:
        cat, sub, des = SITE_CORRECTIONS[name]
        if s["category"] != cat or s["subtype"] != sub or s["designation"] != des:
            print(f"  {name}:")
            if s["category"] != cat:
                print(f"    category: {s['category']!r} → {cat!r}")
            if s["subtype"] != sub:
                print(f"    subtype:  {s['subtype']!r} → {sub!r}")
            if s["designation"] != des and (s["designation"] or des):
                print(f"    designation: {s['designation']!r} → {des!r}")
        s["category"] = cat
        s["subtype"] = sub
        s["designation"] = des

    # Normalize features from raw stored in notes/features column
    # The features column has raw discovery text — normalize it
    raw_features = s.get("features", "")
    s["features"] = normalize_features(raw_features)

    # Timestamp update
    s["updated_at"] = RUN_TS

    corrected_sites.append(s)

# Write corrected sites TSV
with open(sites_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter="\t", lineterminator="\n",
                        quoting=csv.QUOTE_NONE, escapechar="\\")
    writer.writerow(SITE_HEADER)
    for s in corrected_sites:
        row = [s.get(h, "") or "" for h in SITE_HEADER]
        writer.writerow(row)

print(f"\nSites TSV rewritten: {len(corrected_sites)} rows")

# ============================================================
# APPLY CORRECTIONS TO TRAILS TSV
# ============================================================
trails_path = os.path.join(WILLIAMS, "williams_oh_trails.tsv")
with open(trails_path, encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter="\t")
    trail_fieldnames = reader.fieldnames
    trails = list(reader)

TRAIL_HEADER = [
    "Trail Name", "Alternate Names", "Trail Use Type", "Trail Surface Type",
    "Trail Origin Type", "Total Length (Miles)", "Counties", "Governance",
    "Partner Agencies", "Status", "Difficulty", "Accessibility",
    "Description", "Trail History", "Identity Notes", "Notes",
    "URL", "Maps", "Trail ID"
]

for t in trails:
    if t.get("Trail Origin Type") == "Riparian":
        print(f"\n  Trail '{t['Trail Name']}': origin_type 'Riparian' → 'Purpose-Built'")
        t["Trail Origin Type"] = "Purpose-Built"

with open(trails_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter="\t", lineterminator="\n",
                        quoting=csv.QUOTE_NONE, escapechar="\\")
    writer.writerow(TRAIL_HEADER)
    for t in trails:
        row = [t.get(h, "") or "" for h in TRAIL_HEADER]
        writer.writerow(row)

print(f"\nTrails TSV rewritten: {len(trails)} rows")

# ============================================================
# VOCABULARY AUDIT (post-correction)
# ============================================================
print("\n--- Post-correction Vocabulary Audit ---")
with open(sites_path, encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter="\t")
    rows = list(reader)

cat_issues = [r["name"] for r in rows if r["category"] not in VALID_CATEGORIES]
sub_issues = []
for r in rows:
    if r["subtype"]:
        valid_sub = VALID_SUBTYPES.get(r["category"], set())
        # Some categories have no subtypes defined in VALID_SUBTYPES — that's ok
        if valid_sub and r["subtype"] not in valid_sub:
            sub_issues.append(f"  {r['name']}: {r['subtype']!r}")
des_issues = [f"  {r['name']}: {r['designation']!r}" for r in rows
              if r["designation"] and r["designation"] not in VALID_DESIGNATIONS]
feat_issues = []
for r in rows:
    if r["features"]:
        for feat in r["features"].split("; "):
            feat = feat.strip()
            if feat and feat not in VALID_FEATURES:
                feat_issues.append(f"  {r['name']}: '{feat}'")

print(f"  Category violations:    {len(cat_issues)}" + (" ✅" if not cat_issues else ""))
for x in cat_issues: print(f"    {x}")
print(f"  Subtype violations:     {len(sub_issues)}" + (" ✅" if not sub_issues else ""))
for x in sub_issues: print(x)
print(f"  Designation violations: {len(des_issues)}" + (" ✅" if not des_issues else ""))
for x in des_issues: print(x)
print(f"  Feature violations:     {len(feat_issues)}" + (" ✅" if not feat_issues else ""))
for x in feat_issues: print(x)

with open(trails_path, encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter="\t")
    trows = list(reader)

valid_origin = {"Rail Trail","Canal Towpath","Historic Route","Greenway Corridor",
                "Purpose-Built","Utility Corridor","Roadside Corridor","Other",""}
trail_vocab_issues = [f"  {t['Trail Name']}: origin={t['Trail Origin Type']!r}"
                      for t in trows if t.get("Trail Origin Type","") not in valid_origin]
print(f"  Trail origin violations:{len(trail_vocab_issues)}" + (" ✅" if not trail_vocab_issues else ""))
for x in trail_vocab_issues: print(x)

# ============================================================
# SAMPLE OUTPUT
# ============================================================
print("\n--- Sample corrected site records ---")
for r in rows[:5]:
    print(f"  {r['name']}: cat={r['category']!r} sub={r['subtype']!r} des={r['designation']!r}")
    print(f"    features: {r['features'][:100]!r}{'...' if len(r['features'])>100 else ''}")

# ============================================================
# DATABASE UPDATE
# ============================================================
print(f"\n--- DB Update → {PROD_DB} ---")
conn = sqlite3.connect(PROD_DB, timeout=30)
conn.execute("PRAGMA journal_mode=WAL")
cur = conn.cursor()

# Remove and re-insert corrected Williams site records
cur.execute("DELETE FROM sites WHERE site_id LIKE 'WIL-S-%'")
cur.execute("DELETE FROM trails WHERE trail_id LIKE 'WIL-TR-%'")
# Leave APs unchanged — no vocab corrections needed there

site_db_cols = [
    "site_id", "name", "category", "subtype", "designation", "status",
    "ownership", "governance", "partner_agencies", "coordination",
    "description", "location", "acres", "counties", "municipality", "township",
    "gps_lat", "gps_lon", "plus_code", "features", "notes",
    "url_primary", "urls", "parent_site_id", "created_at", "updated_at", "features_raw"
]

for i, s in enumerate(corrected_sites, start=1):
    s["site_id"] = f"WIL-S-{i:03d}"   # reconstruct from ordinal position
    s["features_raw"] = s.get("features", "")  # store corrected vocab features as features_raw too
    vals = []
    for col in site_db_cols:
        v = s.get(col, "") or ""
        if col in ("acres", "gps_lat", "gps_lon"):
            try:
                vals.append(float(v) if v else None)
            except:
                vals.append(None)
        else:
            vals.append(v)
    cur.execute(
        f"INSERT INTO sites ({','.join(site_db_cols)}) VALUES ({','.join(['?']*len(site_db_cols))})",
        vals
    )
print(f"  Sites re-inserted: {len(corrected_sites)}")

trail_db_cols = [
    "trail_id", "name", "alternate_names", "use_type", "surface_type", "origin_type",
    "length_mi", "counties", "governance", "partner_agencies", "status",
    "difficulty", "accessibility", "description", "trail_history", "identity_notes",
    "notes", "url_primary", "maps", "created_at", "updated_at"
]
TRAIL_DB_MAP = {
    "trail_id": "Trail ID", "name": "Trail Name", "alternate_names": "Alternate Names",
    "use_type": "Trail Use Type", "surface_type": "Trail Surface Type",
    "origin_type": "Trail Origin Type", "length_mi": "Total Length (Miles)",
    "counties": "Counties", "governance": "Governance", "partner_agencies": "Partner Agencies",
    "status": "Status", "difficulty": "Difficulty", "accessibility": "Accessibility",
    "description": "Description", "trail_history": "Trail History",
    "identity_notes": "Identity Notes", "notes": "Notes",
    "url_primary": "URL", "maps": "Maps",
}
for t in trails:
    vals = []
    for col in trail_db_cols:
        if col in ("created_at", "updated_at"):
            vals.append(RUN_TS)
            continue
        tsv_col = TRAIL_DB_MAP.get(col, col)
        v = t.get(tsv_col, "") or ""
        if col == "length_mi":
            try:
                vals.append(float(v) if v else None)
            except:
                vals.append(None)
        else:
            vals.append(v)
    cur.execute(
        f"INSERT INTO trails ({','.join(trail_db_cols)}) VALUES ({','.join(['?']*len(trail_db_cols))})",
        vals
    )
print(f"  Trails re-inserted: {len(trails)}")

conn.commit()
conn.close()
print("  DB committed.")
print("\nVocabulary correction complete.")
