# =============================================================================
# SUPERSEDED — IMP-091 (2026-05-04)
# This monolithic pipeline script has been replaced by the parameterised model:
#   utilities/na_run_county.py + County_Spreadsheets/{County}/{county}_pipeline_config.json
# Do not use for new county runs. Kept for reference only.
# =============================================================================
"""
Williams County, Ohio — Natural Areas Pipeline v5.2 (Production Schema)
Generates spec-compliant TSV files and upserts into production DB.
Run date: 2026-04-12
"""

import sys
import os
import csv
import json
import sqlite3
import yaml
from datetime import datetime, timezone

# ============================================================
# PATHS
# ============================================================
NAP_ROOT = "/sessions/wonderful-confident-franklin/mnt/Natural Areas Project v5"
sys.path.insert(0, os.path.join(NAP_ROOT, "utilities"))
from na_plus_code import encode_plus_code

YAML_FILE    = "/sessions/wonderful-confident-franklin/mnt/outputs/Williams_OH_raw_discovery.yaml"
GPS_FILE     = "/sessions/wonderful-confident-franklin/williams_gps_results.json"
GPS_CONF_MOD = "/sessions/wonderful-confident-franklin/williams_gps_table.py"
OUTPUT_DIR   = os.path.join(NAP_ROOT, "County_Spreadsheets", "Williams")
PROD_DB      = os.path.join(NAP_ROOT, "NASqlite", "natural_areas_v5.db")
RUN_TS       = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
RUN_DATE     = "2026-04-12"
RUN_ID       = "williams_oh_2026_04_12"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================
# GPS confidence table (inline to avoid subprocess issues)
# ============================================================
GPS_CONFIDENCE = {
    "Lake La Su An Wildlife Area": "MED",
    "Fish Creek Wildlife Area": "LOW",
    "Parkersburg Wildlife Area": "LOW",
    "St. Joseph River Wildlife Area": "MED",
    "Nettle Lake Wildlife Area": "MED",
    "Mud Lake Bog State Nature Preserve": "LOW",
    "Opdycke Park": "HIGH",
    "George Bible Park": "LOW",
    "Goldie Newman Park/Wildlife Area": "LOW",
    "Dreamers Meadow": "LOW",
    "Springfield Township Park": "MED",
    "Recreation Park": "MED",
    "East End Park and Pool": "MED",
    "Garver Park": "MED",
    "Moore Park and Pool": "LOW",
    "Maple Grove Park": "LOW",
    "Roseland Park": "MED",
    "Fountain City Park": "MED",
    "Hitt Park": "MED",
    "Mattie Marsh Park": "MED",
    "Israel Gardens Butterfly Park": "MED",
    "Central Park": "MED",
    "Montpelier Municipal Park": "MED",
    "Main Street Park": "MED",
    "Robert A. Storrer Municipal Park": "MED",
    "Founders Park": "MED",
    "Iron Horse River Trail": "MED",
    "Miller Park": "MED",
    "Gerhart Park": "LOW",
    "Downtown Park": "LOW",
    "Puppy Pound Park": "LOW",
    "Walz Park": "MED",
    "Edon Community Park": "LOW",
    "Harold C Baker Park": "LOW",
    "Leanne Field": "LOW",
    "Beard Park": "LOW",
    "Cannonball Park": "LOW",
    "Crommer Park": "LOW",
    "Fred Wyman Field": "LOW",
    "Pioneer Memorial Park": "LOW",
    "West Unity Memorial Park": "MED",
    "Alvordton Community Park": "LOW",
    "West Unity Trail Head": "LOW",
    "Knight's Landing": "LOW",
    "St. Joseph River Confluence Preserve": "LOW",
    "St. Joseph River Floodplain Preserve": "LOW",
    "Wabash Cannonball Trail": "LOW",
    "Pioneer Scout Reservation": "MED",
    "Lake Seneca Beach": "LOW",
    "Memory Point Park": "LOW",
    "Davis Woods": "LOW",
}

# ============================================================
# LOAD DATA
# ============================================================
print("=" * 60)
print("Williams County, OH — Pipeline v5.2 (Production)")
print(f"Run: {RUN_ID}")
print("=" * 60)

with open(YAML_FILE) as f:
    raw_data = yaml.safe_load(f)
with open(GPS_FILE) as f:
    gps_data = json.load(f)

entity_records = [r for r in raw_data["records"]
                  if "entity_type" in r and "tier_result" not in r]
print(f"Entity records: {len(entity_records)}")

# ============================================================
# ID COUNTERS
# ============================================================
PREFIX = "WIL"
_counters = {"S": 0, "TR": 0, "AP": 0}

def next_id(code):
    _counters[code] += 1
    return f"{PREFIX}-{code}-{_counters[code]:03d}"

# ============================================================
# GPS HELPER
# ============================================================
def get_gps(name):
    entry = gps_data.get(name)
    if entry:
        lat = round(float(entry[0]), 6)
        lon = round(float(entry[1]), 6)
        pc = encode_plus_code(lat, lon)
        return lat, lon, pc
    return None, None, ""

def fmt_gps(val):
    """Format GPS float for TSV — up to 6 sig figs, no trailing zeros."""
    if val is None:
        return ""
    return str(round(val, 6)).rstrip("0").rstrip(".")

# ============================================================
# NORMALIZATION HELPERS
# ============================================================
def normalize_county(counties_raw):
    """Return alphabetized, semicolon-delimited county names without 'County' suffix."""
    import re
    cleaned = []
    for c in (counties_raw or []):
        c = re.sub(r',?\s*(Ohio|OH)\s*$', '', str(c), flags=re.I).strip()
        c = re.sub(r'\s+County\s*$', '', c, flags=re.I).strip()
        if c and c not in ("and multiple other states",):
            cleaned.append(c)
    return "; ".join(sorted(set(cleaned))) if cleaned else "Williams"

def clean_field(val):
    """Strip, remove internal tabs and newlines."""
    if val is None:
        return ""
    return str(val).strip().replace("\t", " ").replace("\n", " ").replace("\r", " ")

def fmt_acres(raw):
    """Return numeric acres string or blank."""
    import re
    if not raw:
        return ""
    s = str(raw).replace(",", "").strip()
    m = re.search(r'[\d]+(?:\.\d+)?', s)
    if m:
        return m.group(0)
    return ""

MULTI_COUNTY_TRAILS = {"Wabash Cannonball Trail", "North Country National Scenic Trail"}

HELD = []
SITES_OUT = []
TRAILS_OUT = []
APS_OUT = []

# ============================================================
# PROCESS ENTITIES
# ============================================================
for rec in entity_records:
    et = rec.get("entity_type", "")
    name = rec.get("name_raw", "")
    tier = rec.get("discovery_tier", 0)
    gov = clean_field(rec.get("governance_raw", ""))
    own = clean_field(rec.get("ownership_raw", ""))
    partner = clean_field(rec.get("partner_agencies_raw", ""))
    coord = clean_field(rec.get("coordination_raw", ""))
    counties_raw = rec.get("counties_raw", ["Williams County, Ohio"])
    counties = normalize_county(counties_raw)
    lat, lon, plus_code = get_gps(name)

    # ---- SITES ----
    if et == "Site":
        sid = next_id("S")
        name_lower = name.lower()
        gov_lower = gov.lower()

        # Category / subtype
        if "state nature preserve" in name_lower:
            category = "Nature Preserve"
            subtype = "State Nature Preserve"
            designation = "State Nature Preserve"
        elif "wildlife area" in name_lower and tier == 2:
            category = "Wildlife Area"
            subtype = "Wildlife Area"
            designation = "Wildlife Area"
        elif "wildlife area" in name_lower:
            category = "Wildlife Area"
            subtype = "Wildlife Area"
            designation = ""
        elif "preserve" in name_lower and ("conservancy" in gov_lower or "black swamp" in gov_lower):
            category = "Nature Preserve"
            subtype = "Conservancy Preserve"
            designation = ""
        elif "scout reservation" in name_lower or "boy scouts" in gov_lower or "erie shores" in gov_lower:
            category = "Private Reserve"
            subtype = "Scouting Reservation"
            designation = ""
        elif "lake seneca" in name_lower or "memory point" in name_lower:
            category = "Private Reserve"
            subtype = "Private Community Area"
            designation = ""
        elif "woods" in name_lower and not gov:
            category = "Natural Feature"
            subtype = "Woodland"
            designation = ""
        elif "township" in gov_lower:
            category = "Park"
            subtype = "Township Park"
            designation = ""
        elif "county park" in gov_lower or "park board" in gov_lower or "williams county" in gov_lower:
            category = "Park"
            subtype = "County Park"
            designation = ""
        elif "city of" in gov_lower:
            category = "Park"
            subtype = "City Park"
            designation = ""
        elif any(v in gov_lower for v in ["village of", "montpelier park", "edgerton", "edon", "pioneer", "west unity", "stryker", "montpelier parks"]):
            category = "Park"
            subtype = "Village Park"
            designation = ""
        else:
            category = "Park"
            subtype = "Community Park"
            designation = ""

        features = clean_field(rec.get("features_raw", ""))
        description = clean_field(rec.get("description_raw", ""))
        location = clean_field(rec.get("location_raw", ""))
        acres = fmt_acres(rec.get("acres_raw", ""))
        urls_list = rec.get("urls_raw", [])
        url_primary = urls_list[0] if urls_list else ""
        urls_extra = "; ".join(urls_list[1:]) if len(urls_list) > 1 else ""
        identity_notes = clean_field(rec.get("identity_notes_raw", ""))

        # notes: capture key flags
        notes_parts = []
        if "UNVERIFIED" in identity_notes:
            notes_parts.append("UNVERIFIED from online sources — needs map verification.")
        if "UNCERTAIN" in identity_notes:
            notes_parts.append("Identity or governance uncertain — needs resolution.")
        gps_conf = GPS_CONFIDENCE.get(name, "LOW")
        if gps_conf == "LOW":
            notes_parts.append("GPS approximate — centroid-level; needs field verification.")
        elif gps_conf == "MED":
            notes_parts.append("GPS from address geocode — verify precision.")
        notes = " ".join(notes_parts)

        SITES_OUT.append({
            "site_id": sid,
            "name": name,
            "category": category,
            "subtype": subtype,
            "designation": designation,
            "status": "Active",
            "ownership": own,
            "governance": gov,
            "partner_agencies": partner,
            "coordination": coord,
            "description": description,
            "location": location,
            "acres": acres,
            "counties": counties,
            "municipality": "",  # GIS lookup not available; blank per spec
            "township": "",      # GIS lookup not available; blank per spec
            "gps_lat": fmt_gps(lat),
            "gps_lon": fmt_gps(lon),
            "plus_code": plus_code,
            "features": features,
            "notes": notes,
            "url_primary": url_primary,
            "urls": urls_extra,
            "parent_site_id": "",
            "created_at": RUN_TS,
            "updated_at": RUN_TS,
            "features_raw": features,  # DB extra field
        })

    # ---- TRAILS ----
    elif et == "Trail":
        trid = next_id("TR")

        # Hold multi-county/multi-state trails
        if name in MULTI_COUNTY_TRAILS:
            hold_reason = "multi_state_federal" if "North Country" in name else "multi_county"
            HELD.append({
                "record_id": trid,
                "entity_type": "Trail",
                "name": name,
                "county": "Williams",
                "hold_reason": hold_reason,
                "hold_detail": f"Multi-county trail pending all relevant counties: {counties}",
                "run_id": RUN_ID,
                "created_at": RUN_TS,
            })
            print(f"  HELD Trail: {name} ({hold_reason}) → {trid}")
            continue

        # Iron Horse River Trail
        use_type = "Multi-Use"
        surface_type = "Mixed"
        origin_type = "Riparian"
        length_mi = "2"  # numeric only per spec
        urls_list = rec.get("urls_raw", [])
        url_primary = urls_list[0] if urls_list else ""
        maps_urls = "; ".join(urls_list[1:]) if len(urls_list) > 1 else ""
        identity_notes = clean_field(rec.get("identity_notes_raw", ""))
        description = clean_field(rec.get("description_raw", ""))
        accessibility = clean_field(rec.get("accessibility_raw", ""))

        TRAILS_OUT.append({
            "trail_id": trid,
            "name": name,
            "alternate_names": "",
            "use_type": use_type,
            "surface_type": surface_type,
            "origin_type": origin_type,
            "length_mi": length_mi,
            "counties": counties,
            "governance": gov,
            "partner_agencies": partner,
            "status": "Active",
            "difficulty": "",
            "accessibility": accessibility,
            "description": description,
            "trail_history": "",
            "identity_notes": identity_notes,
            "notes": "",
            "url_primary": url_primary,
            "maps": maps_urls,
        })

    # ---- ACCESS POINTS ----
    elif et == "Access Point":
        apid = next_id("AP")
        name_lower = name.lower()
        description = clean_field(rec.get("description_raw", ""))
        features = clean_field(rec.get("features_raw", ""))
        urls_list = rec.get("urls_raw", [])
        url_str = "; ".join(urls_list) if urls_list else ""
        location = clean_field(rec.get("location_raw", ""))
        identity_notes = clean_field(rec.get("identity_notes_raw", ""))

        # AP type
        if "canoe" in name_lower or "canoe" in description.lower() or "landing" in name_lower:
            ap_type = "Watercraft Access Point"
        else:
            ap_type = "Trailhead"

        # Parent entity
        if "dreamers meadow" in name_lower or "west unity trail" in name_lower:
            parent_type = "Trail"
            parent_id = "WIL-TR-003"  # Wabash Cannonball Trail
        elif "knight" in name_lower:
            parent_type = "Site"
            parent_id = ""  # Tiffin River not a staged entity; leave blank
        else:
            parent_type = ""
            parent_id = ""

        # GPS required for APs; hold if missing after acquisition
        if not lat:
            HELD.append({
                "record_id": apid,
                "entity_type": "Access Point",
                "name": name,
                "county": "Williams",
                "hold_reason": "missing_gps",
                "hold_detail": "GPS not acquired; access point requires GPS for statewide inclusion.",
                "run_id": RUN_ID,
                "created_at": RUN_TS,
            })
            print(f"  HELD AP: {name} (missing_gps) → {apid}")
            continue

        APS_OUT.append({
            "access_point_id": apid,
            "name": name,
            "ap_type": ap_type,
            "status": "Active",
            "parent_entity_type": parent_type,
            "parent_entity_id": parent_id,
            "county": "Williams",
            "township": "",
            "municipality": "",
            "address": location,
            "gps_lat": fmt_gps(lat),
            "gps_lon": fmt_gps(lon),
            "plus_code": plus_code,
            "features": features,
            "identity_notes": identity_notes,
            "notes": "",
            "url_primary": url_str,
        })

print(f"\nNormalization:")
print(f"  Sites:         {len(SITES_OUT)}")
print(f"  Trails:        {len(TRAILS_OUT)}")
print(f"  Access Points: {len(APS_OUT)}")
print(f"  Held:          {len(HELD)}")

# ============================================================
# TSV OUTPUT (spec-compliant headers + data)
# ============================================================
print("\n--- TSV Output ---")

def write_tsv(path, header, records, key_map):
    """Write TSV with header row. key_map maps header names to record keys."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n",
                            quoting=csv.QUOTE_NONE, escapechar="\\")
        writer.writerow(header)
        for rec in records:
            row = []
            for h in header:
                key = key_map.get(h, h.lower().replace(" ", "_").replace("(", "").replace(")", ""))
                val = rec.get(key, "")
                if val is None:
                    val = ""
                # Sanitize: no tabs, no newlines, no leading/trailing spaces
                val = str(val).replace("\t", " ").replace("\n", " ").replace("\r", " ").strip()
                row.append(val)
            writer.writerow(row)
    print(f"  {os.path.basename(path)}: {len(records)} data rows, {len(header)-1} tabs/row")

# ---- Sites ----
SITE_HEADER = [
    "name", "category", "subtype", "designation", "status",
    "ownership", "governance", "partner_agencies", "coordination",
    "description", "location", "acres", "counties", "municipality", "township",
    "gps_lat", "gps_lon", "plus_code", "features", "notes",
    "url_primary", "urls", "parent_site_id", "created_at", "updated_at"
]
assert len(SITE_HEADER) == 25

sites_tsv = os.path.join(OUTPUT_DIR, "williams_oh_sites.tsv")
write_tsv(sites_tsv, SITE_HEADER, SITES_OUT, {h: h for h in SITE_HEADER})

# ---- Trails ----
TRAIL_HEADER = [
    "Trail Name", "Alternate Names", "Trail Use Type", "Trail Surface Type",
    "Trail Origin Type", "Total Length (Miles)", "Counties", "Governance",
    "Partner Agencies", "Status", "Difficulty", "Accessibility",
    "Description", "Trail History", "Identity Notes", "Notes",
    "URL", "Maps", "Trail ID"
]
assert len(TRAIL_HEADER) == 19

TRAIL_KEY_MAP = {
    "Trail Name": "name",
    "Alternate Names": "alternate_names",
    "Trail Use Type": "use_type",
    "Trail Surface Type": "surface_type",
    "Trail Origin Type": "origin_type",
    "Total Length (Miles)": "length_mi",
    "Counties": "counties",
    "Governance": "governance",
    "Partner Agencies": "partner_agencies",
    "Status": "status",
    "Difficulty": "difficulty",
    "Accessibility": "accessibility",
    "Description": "description",
    "Trail History": "trail_history",
    "Identity Notes": "identity_notes",
    "Notes": "notes",
    "URL": "url_primary",
    "Maps": "maps",
    "Trail ID": "trail_id",
}

trails_tsv = os.path.join(OUTPUT_DIR, "williams_oh_trails.tsv")
write_tsv(trails_tsv, TRAIL_HEADER, TRAILS_OUT, TRAIL_KEY_MAP)

# ---- Access Points ----
AP_HEADER = [
    "Access Point Name", "Access Point Type", "Status",
    "Identity Parent Entity Type", "Identity Parent Entity Name",
    "County", "Township", "Municipality", "Address",
    "GPS Lat", "GPS Lon", "Plus Code",
    "Features", "Identity Notes", "Notes", "URL", "Access Point ID"
]
assert len(AP_HEADER) == 17

AP_KEY_MAP = {
    "Access Point Name": "name",
    "Access Point Type": "ap_type",
    "Status": "status",
    "Identity Parent Entity Type": "parent_entity_type",
    "Identity Parent Entity Name": "parent_entity_id",
    "County": "county",
    "Township": "township",
    "Municipality": "municipality",
    "Address": "address",
    "GPS Lat": "gps_lat",
    "GPS Lon": "gps_lon",
    "Plus Code": "plus_code",
    "Features": "features",
    "Identity Notes": "identity_notes",
    "Notes": "notes",
    "URL": "url_primary",
    "Access Point ID": "access_point_id",
}

ap_tsv = os.path.join(OUTPUT_DIR, "williams_oh_access_points.tsv")
write_tsv(ap_tsv, AP_HEADER, APS_OUT, AP_KEY_MAP)

# ---- Empty TSVs for completeness ----
for fname, header, ntabs in [
    ("williams_oh_trail_segments.tsv",
     ["Trail Segment Name","Trail Segment Type","Surface Type","Difficulty","Counties",
      "Parent Trail ID","GPS Lat","GPS Lon","Plus Code","Length (Miles)",
      "Geometry","Identity Notes","Notes","URL","Trail Segment ID","created_at","updated_at"],
     16),
    ("williams_oh_trail_networks.tsv",
     ["Trail Network Name","Network Type","Member Trail IDs","Total Length (Miles)","Counties",
      "Governance","Partner Agencies","Status","Description","Identity Notes","Notes","URL","Maps",
      "GPS Lat","GPS Lon","Plus Code","Trail Network ID"],
     16),
    ("williams_oh_site_networks.tsv",
     ["Site Network Name","Network Type","Member Site IDs","Counties","Governance",
      "Status","Description","Identity Notes","Notes","URL",
      "GPS Lat","GPS Lon","Plus Code","Site Network ID","created_at"],
     14),
]:
    path = os.path.join(OUTPUT_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\t".join(header) + "\n")
    print(f"  {fname}: 0 data rows (null)")

# ============================================================
# INTEGRITY CHECK
# ============================================================
print("\n--- Integrity Check ---")

def check_tsv_file(path, expected_tabs, label):
    issues = []
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    if not lines:
        return [f"{label}: empty file"]
    for i, line in enumerate(lines):
        line = line.rstrip("\n").rstrip("\r")
        tabs = line.count("\t")
        if tabs != expected_tabs:
            issues.append(f"Row {i}: {tabs} tabs (expected {expected_tabs})")
    return issues

checks = [
    (sites_tsv, 24, "Sites"),
    (trails_tsv, 18, "Trails"),
    (ap_tsv, 16, "Access Points"),
    (os.path.join(OUTPUT_DIR, "williams_oh_trail_segments.tsv"), 16, "Trail Segments"),
    (os.path.join(OUTPUT_DIR, "williams_oh_trail_networks.tsv"), 16, "Trail Networks"),
    (os.path.join(OUTPUT_DIR, "williams_oh_site_networks.tsv"), 14, "Site Networks"),
]

all_ok = True
for path, exp, label in checks:
    issues = check_tsv_file(path, exp, label)
    if issues:
        all_ok = False
        print(f"  FAIL {label}: {issues[:3]}")
    else:
        with open(path) as f:
            n = sum(1 for _ in f) - 1
        print(f"  OK   {label}: {n} rows")

if not all_ok:
    print("INTEGRITY CHECK FAILED")
    sys.exit(1)
print("  All integrity checks passed.")

# ============================================================
# DATABASE UPSERT (production DB)
# ============================================================
print(f"\n--- DB Upsert → {PROD_DB} ---")

# Use WAL mode to reduce locking issues on network mount
conn = sqlite3.connect(PROD_DB, timeout=30)
conn.execute("PRAGMA journal_mode=WAL")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# ---- Upsert sites ----
site_cols = [
    "site_id", "name", "category", "subtype", "designation", "status",
    "ownership", "governance", "partner_agencies", "coordination",
    "description", "location", "acres", "counties", "municipality", "township",
    "gps_lat", "gps_lon", "plus_code", "features", "notes",
    "url_primary", "urls", "parent_site_id", "created_at", "updated_at", "features_raw"
]
n_sites = 0
for s in SITES_OUT:
    vals = []
    for col in site_cols:
        v = s.get(col, "")
        if col in ("acres", "gps_lat", "gps_lon"):
            try:
                vals.append(float(v) if v else None)
            except:
                vals.append(None)
        else:
            vals.append(v if v else "")
    cur.execute(
        f"INSERT OR REPLACE INTO sites ({','.join(site_cols)}) VALUES ({','.join(['?']*len(site_cols))})",
        vals
    )
    n_sites += 1
print(f"  Sites upserted: {n_sites}")

# ---- Upsert trails ----
trail_cols = [
    "trail_id", "name", "alternate_names", "use_type", "surface_type", "origin_type",
    "length_mi", "counties", "governance", "partner_agencies", "status",
    "difficulty", "accessibility", "description", "trail_history", "identity_notes",
    "notes", "url_primary", "maps", "created_at", "updated_at"
]
n_trails = 0
for t in TRAILS_OUT:
    t["created_at"] = RUN_TS
    t["updated_at"] = RUN_TS
    vals = []
    for col in trail_cols:
        v = t.get(col, "")
        if col == "length_mi":
            try:
                vals.append(float(v) if v else None)
            except:
                vals.append(None)
        else:
            vals.append(v if v else "")
    cur.execute(
        f"INSERT OR REPLACE INTO trails ({','.join(trail_cols)}) VALUES ({','.join(['?']*len(trail_cols))})",
        vals
    )
    n_trails += 1
print(f"  Trails upserted: {n_trails}")

# ---- Upsert access points ----
ap_cols = [
    "access_point_id", "name", "ap_type", "status",
    "parent_entity_type", "parent_entity_id",
    "county", "township", "municipality", "address",
    "gps_lat", "gps_lon", "plus_code",
    "features", "identity_notes", "notes", "url_primary",
    "created_at", "updated_at"
]
n_aps = 0
for ap in APS_OUT:
    ap["created_at"] = RUN_TS
    ap["updated_at"] = RUN_TS
    vals = []
    for col in ap_cols:
        v = ap.get(col, "")
        if col in ("gps_lat", "gps_lon"):
            try:
                vals.append(float(v) if v else None)
            except:
                vals.append(None)
        else:
            vals.append(v if v else "")
    cur.execute(
        f"INSERT OR REPLACE INTO access_points ({','.join(ap_cols)}) VALUES ({','.join(['?']*len(ap_cols))})",
        vals
    )
    n_aps += 1
print(f"  Access Points upserted: {n_aps}")

# ---- Upsert held entities ----
n_held = 0
for h in HELD:
    cur.execute(
        "INSERT INTO held_entities (record_id, entity_type, name, county, hold_reason, hold_detail, run_id, created_at) VALUES (?,?,?,?,?,?,?,?)",
        (h["record_id"], h["entity_type"], h["name"], h["county"],
         h["hold_reason"], h["hold_detail"], h["run_id"], h["created_at"])
    )
    n_held += 1
print(f"  Held entities: {n_held}")

# ---- Run metadata ----
cur.execute(
    "INSERT INTO run_metadata (run_id, county, state, run_date, records_input, normalized, held, rejected, notes, created_at) VALUES (?,?,?,?,?,?,?,?,?,?)",
    (RUN_ID, "Williams", "Ohio", RUN_DATE,
     len(entity_records), len(SITES_OUT) + len(TRAILS_OUT) + len(APS_OUT),
     len(HELD), 0,
     f"Williams County full pipeline: {len(SITES_OUT)} sites, {len(TRAILS_OUT)} trails, {len(APS_OUT)} APs, {len(HELD)} held.",
     RUN_TS)
)

conn.commit()
conn.close()
print(f"  DB committed.")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("Pipeline complete!")
print(f"  Output dir: {OUTPUT_DIR}")
print(f"  Sites:          {n_sites}")
print(f"  Trails:         {n_trails}")
print(f"  Trail Segments: 0 (null)")
print(f"  Trail Networks: 0 (null)")
print(f"  Site Networks:  0 (null)")
print(f"  Access Points:  {n_aps}")
print(f"  Held:           {n_held}")
print("=" * 60)

print("\nEntity IDs:")
for s in SITES_OUT:
    flag = ""
    if s.get("notes"):
        if "UNVERIFIED" in s["notes"]: flag = " [UNVERIFIED]"
        elif "GPS approx" in s["notes"] and "centroid" in s["notes"]: flag += " [GPS_APPROX]"
    print(f"  {s['site_id']}  {s['name']}{flag}")
for t in TRAILS_OUT:
    print(f"  {t['trail_id']}  {t['name']}")
for ap in APS_OUT:
    print(f"  {ap['access_point_id']}  {ap['name']}")
for h in HELD:
    print(f"  {h['record_id']}  {h['name']} [HELD: {h['hold_reason']}]")
