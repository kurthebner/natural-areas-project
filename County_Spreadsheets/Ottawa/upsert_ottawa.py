#!/usr/bin/env python3
"""
upsert_ottawa.py — Stage 6: Database Upsert for Ottawa County, Ohio
Upserts 199 entities (192 main pipeline + 7 cross-county) into natural_areas_v5.db.

Run ID: ottawa_ohio_2026_05_18
County: Ottawa, Ohio
Entities: 134 sites, 55 trails (51 + 4 MC), 8 APs (6 + 2 unblocked), 2 site networks (1 + 1 MC)
Held (remaining): 0 — all 6 originally held entities resolved via cross-county pass
"""

import json, sqlite3, pathlib, sys
from datetime import datetime, timezone

DB_PATH   = pathlib.Path("/sessions/jolly-kind-bardeen/mnt/Natural Areas Project v5/NASqlite/natural_areas_v5.db")
NORM_PATH = pathlib.Path("/sessions/jolly-kind-bardeen/mnt/outputs/ottawa_ohio_normalized.json")

RUN_ID   = "ottawa_ohio_2026_05_18"
COUNTY   = "Ottawa"
STATE    = "Ohio"
RUN_DATE = "2026-05-20"
NOW      = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

# ── helpers ──────────────────────────────────────────────────────────────
def c(v):
    return "" if v is None else str(v).strip()

def flt(v):
    if v is None or v == "":
        return None
    try:
        return float(v)
    except (ValueError, TypeError):
        return None

def intt(v):
    if v is None or v == "":
        return None
    try:
        return int(v)
    except (ValueError, TypeError):
        return None

# ── load normalized entities ─────────────────────────────────────────────
data     = json.loads(NORM_PATH.read_text())
entities = data["normalized_entities"]
sites    = [e for e in entities if e["entity_type"] == "Site"]
trails   = [e for e in entities if e["entity_type"] == "Trail"]
aps      = [e for e in entities if e["entity_type"] == "Access Point"]
networks = [e for e in entities if e["entity_type"] == "Site Network"]

print(f"Loaded from normalized.json: {len(sites)} sites, {len(trails)} trails, {len(aps)} APs, {len(networks)} site networks")

# ── cross-county entities (inline — not in normalized.json) ──────────────
CC_TRAILS = [
    {
        "trail_id":       "OH-MC-T-0109",
        "name":           "Metzger Marsh Trail",
        "alternate_names":"",
        "use_type":       "",
        "surface_type":   "",
        "origin_type":    "",
        "length_mi":      None,
        "counties":       "Lucas;Ottawa",
        "governance":     "U.S. Fish & Wildlife Service",
        "partner_agencies":"Ohio Division of Wildlife",
        "status":         "Active",
        "difficulty":     "",
        "accessibility":  "",
        "description":    "A trail within the Ottawa National Wildlife Refuge at the Metzger Marsh Unit, a 740-acre coastal marsh along Lake Erie. The eastern 182 acres of the unit lie in Lucas County, co-owned and co-managed by the Ohio Division of Wildlife and USFWS.",
        "trail_history":  "",
        "identity_notes": "Trail at Ottawa NWR — Metzger Marsh Unit. Metzger Marsh Unit spans Ottawa and Lucas counties. Condition B MC ID assigned: OH-MC-T-0109.",
        "notes":          "",
        "url_primary":    "https://www.fws.gov/refuge/ottawa/visit-us/trails",
        "maps":           "https://www.fws.gov/refuge/ottawa/map?trail=metzger-marsh-trail",
    },
    {
        "trail_id":       "OH-MC-T-0110",
        "name":           "North Coast Inland Trail",
        "alternate_names":"NCIT",
        "use_type":       "",
        "surface_type":   "",
        "origin_type":    "Rail Trail",
        "length_mi":      None,
        "counties":       "Erie;Huron;Ottawa;Sandusky",
        "governance":     "Park District of Ottawa County",
        "partner_agencies":"",
        "status":         "Active",
        "difficulty":     "",
        "accessibility":  "",
        "description":    "Approximately 100-mile rail trail from Lorain to Genoa traversing Erie, Huron, Sandusky, and Ottawa counties. The Ottawa County segment runs from the Sandusky County line northwest through Elmore to Veterans Park in Genoa (terminus). Also designated as US Bike Route 30. Trail converts from multi-use paved to on-road route at Martin-Williston Road then reconnects to multi-use paved to the Genoa terminus.",
        "trail_history":  "",
        "identity_notes": "CROSS_COUNTY_CANDIDATE. Spans Erie; Huron; Ottawa; Sandusky counties. Park District of Ottawa County manages the Ottawa County segment. Condition B MC ID assigned: OH-MC-T-0110.",
        "notes":          "",
        "url_primary":    "https://ottawacountyparksoh.org/parks-and-trails/north-coast-inland-trail/",
        "maps":           "",
    },
    {
        "trail_id":       "OH-OTT-T-124",
        "name":           "Lake Erie Islands Water Trail",
        "alternate_names":"LEIT",
        "use_type":       "",
        "surface_type":   "",
        "origin_type":    "",
        "length_mi":      None,
        "counties":       "Ottawa",
        "governance":     "Put-in-Bay Township Park District",
        "partner_agencies":"",
        "status":         "Active",
        "difficulty":     "",
        "accessibility":  "",
        "description":    "ODNR's 12th designated state water trail. Four island-loop segments in Ottawa County: South Bass Island Trail, Middle Bass Island Trail, North Bass Island Trail, and Mainland Trail. Kelleys Island segment is in Erie County.",
        "trail_history":  "",
        "identity_notes": "CROSS_COUNTY_CANDIDATE. ODNR-designated state water trail. Primary managing entity is Put-in-Bay Township Park District (T3 per management tier rule). Kelleys Island segment is Erie County — out of scope for Ottawa County run. Counties provisional (Ottawa only); Erie County not yet processed — Scenario A: provisional ID OH-OTT-T-124 retained until Erie County run.",
        "notes":          "",
        "url_primary":    "https://ottawacountyparksoh.org/",
        "maps":           "",
    },
    {
        "trail_id":       "OH-MC-TR-002",
        "name":           "Portage River Water Trail",
        "alternate_names":"PRWT",
        "use_type":       "",
        "surface_type":   "",
        "origin_type":    "",
        "length_mi":      36.0,
        "counties":       "Ottawa;Wood",
        "governance":     "Toledo Metropolitan Area Council of Governments",
        "partner_agencies":"Park District of Ottawa County; U.S. Fish & Wildlife Service; Ohio Department of Natural Resources",
        "status":         "Active",
        "difficulty":     "",
        "accessibility":  "",
        "description":    "A 36-mile state-designated water trail on the Portage River, officially designated July 19, 2022, spanning Ottawa and Wood counties. The Ottawa County segment runs from Lake Erie Beach Access in Port Clinton (Mile 0) to approximately Mile 23 near Elmore, with 8 documented Ottawa County launch sites.",
        "trail_history":  "Officially state-designated by ODNR on July 19, 2022. Coordinated by TMACOG with USFWS, ODNR, and partner organizations.",
        "identity_notes": "KNOWN_MC:OH-MC-TR-002. Ottawa/Wood multi-county water trail. Ottawa County is first county to pipeline this entity. Confirmed via PDOC website.",
        "notes":          "",
        "url_primary":    "https://ottawacountyparksoh.org/parks-and-trails/portage-river-water-trail/",
        "maps":           "",
    },
]

CC_SITE_NETWORKS = [
    {
        "network_id":    "OH-MC-SN-0002",
        "name":          "Ottawa National Wildlife Refuge Complex",
        "network_type":  "Wildlife Refuge Complex",
        "status":        "Active",
        "ownership":     "Federal",
        "governance":    "U.S. Fish & Wildlife Service",
        "partner_agencies":"",
        "counties":      "Lucas;Ottawa",
        "states_included":"",
        "member_count":  None,
        "member_site_ids":"",
        "description":   "Ohio's only National Wildlife Refuge Complex, formally designated by USFWS. Ohio members include Ottawa NWR (Ottawa County), Cedar Point NWR (Lucas County), and West Sister Island NWR (Lucas County). Schoonover Waterfowl Production Area in Michigan is administratively part of the complex but is out of Ohio scope.",
        "identity_notes":"USFWS formally designates this as the 'Ottawa National Wildlife Refuge Complex' — Ohio's only NWR complex. Spans Ottawa and Lucas counties. Schoonover WPA (Michigan) out of Ohio scope. Condition B MC ID assigned: OH-MC-SN-0002.",
        "notes":         "",
        "url_primary":   "https://www.fws.gov/refuge/ottawa",
    },
]

CC_APS = [
    {
        "access_point_id":  "OH-OTT-AP-007",
        "name":             "Oak Harbor Station Interurban Overlook and Hand Powered Boat Launch",
        "ap_type":          "",
        "status":           "Active",
        "parent_entity_type":"Trail",
        "parent_entity_id": "OH-MC-TR-002",
        "county":           "Ottawa",
        "township":         "",
        "municipality":     "Oak Harbor",
        "address":          "South end of Church Street, Oak Harbor, OH 43449",
        "gps_lat":          None,
        "gps_lon":          None,
        "plus_code":        "",
        "features":         "",
        "identity_notes":   "Water access point on Portage River (Portage River Water Trail; OH-MC-TR-002). 'Interurban' name refers to historical interurban rail corridor.",
        "notes":            "",
        "url_primary":      "https://www.oakharbor.oh.us/departments/public_works/parks.php",
    },
    {
        "access_point_id":  "OH-OTT-AP-008",
        "name":             "Lake Erie Islands Water Trail — Access Point 9 (Lucien M. Clemons Park)",
        "ap_type":          "Kayak-Canoe Launch",
        "status":           "Active",
        "parent_entity_type":"Trail",
        "parent_entity_id": "OH-OTT-T-124",
        "county":           "Ottawa",
        "township":         "",
        "municipality":     "Marblehead",
        "address":          "East end of Lucien M. Clemons Park, Marblehead, OH 43440",
        "gps_lat":          None,
        "gps_lon":          None,
        "plus_code":        "",
        "features":         "",
        "identity_notes":   "Access Point 9 of Lake Erie Islands Water Trail (LEIT; OH-OTT-T-124). Parent site: Lucien M. Clemons Park. Physical access managed by Village of Marblehead within the park.",
        "notes":            "",
        "url_primary":      "https://www.marbleheadohio.org/parks/page/lucien-m-clemons-park",
    },
]

# ── connect ───────────────────────────────────────────────────────────────
print(f"\nConnecting to DB: {DB_PATH}")
con = sqlite3.connect(str(DB_PATH))
cur = con.cursor()

# ════════════════════════════════════════════════════════════════════════
# DDL — CREATE TABLE IF NOT EXISTS (IMP-087)
# Tables already exist; these are safety guards only.
# ════════════════════════════════════════════════════════════════════════
DDL = [
    # Primary entity tables
    """CREATE TABLE IF NOT EXISTS sites (
        site_id TEXT PRIMARY KEY, name TEXT, category TEXT, subtype TEXT,
        designation TEXT, status TEXT, ownership TEXT, governance TEXT,
        partner_agencies TEXT, coordination TEXT, description TEXT,
        location TEXT, acres REAL, counties TEXT, municipality TEXT,
        township TEXT, gps_lat REAL, gps_lon REAL, plus_code TEXT,
        features TEXT, notes TEXT, url_primary TEXT, urls TEXT,
        parent_site_id TEXT, created_at TEXT, updated_at TEXT, features_raw TEXT)""",
    """CREATE TABLE IF NOT EXISTS trails (
        trail_id TEXT PRIMARY KEY, name TEXT, alternate_names TEXT,
        use_type TEXT, surface_type TEXT, origin_type TEXT, length_mi REAL,
        counties TEXT, governance TEXT, partner_agencies TEXT, status TEXT,
        difficulty TEXT, accessibility TEXT, description TEXT, trail_history TEXT,
        identity_notes TEXT, notes TEXT, url_primary TEXT, maps TEXT,
        created_at TEXT, updated_at TEXT)""",
    """CREATE TABLE IF NOT EXISTS access_points (
        access_point_id TEXT PRIMARY KEY, name TEXT, ap_type TEXT, status TEXT,
        parent_entity_type TEXT, parent_entity_id TEXT, county TEXT, township TEXT,
        municipality TEXT, address TEXT, gps_lat REAL, gps_lon REAL, plus_code TEXT,
        features TEXT, identity_notes TEXT, notes TEXT, url_primary TEXT,
        created_at TEXT, updated_at TEXT)""",
    """CREATE TABLE IF NOT EXISTS site_networks (
        network_id TEXT PRIMARY KEY, name TEXT, network_type TEXT, status TEXT,
        ownership TEXT, governance TEXT, partner_agencies TEXT, counties TEXT,
        states_included TEXT, member_count INTEGER, member_site_ids TEXT,
        description TEXT, identity_notes TEXT, notes TEXT, url_primary TEXT,
        created_at TEXT, updated_at TEXT, org_type TEXT)""",
    """CREATE TABLE IF NOT EXISTS trail_segments (
        segment_id TEXT PRIMARY KEY, name TEXT, counties TEXT, created_at TEXT, updated_at TEXT)""",
    """CREATE TABLE IF NOT EXISTS trail_networks (
        network_id TEXT PRIMARY KEY, name TEXT, counties TEXT, created_at TEXT, updated_at TEXT)""",
    # Relationship tables
    """CREATE TABLE IF NOT EXISTS site_parent (site_id TEXT, parent_site_id TEXT,
        PRIMARY KEY (site_id, parent_site_id))""",
    """CREATE TABLE IF NOT EXISTS trail_parents (trail_id TEXT, parent_site_id TEXT,
        PRIMARY KEY (trail_id, parent_site_id))""",
    """CREATE TABLE IF NOT EXISTS trail_to_segment (trail_id TEXT, segment_id TEXT,
        PRIMARY KEY (trail_id, segment_id))""",
    """CREATE TABLE IF NOT EXISTS trail_network_members (network_id TEXT, trail_id TEXT,
        PRIMARY KEY (network_id, trail_id))""",
    """CREATE TABLE IF NOT EXISTS site_network_members (network_id TEXT, site_id TEXT,
        PRIMARY KEY (network_id, site_id))""",
    """CREATE TABLE IF NOT EXISTS access_point_parents (access_point_id TEXT,
        parent_entity_type TEXT, parent_entity_id TEXT,
        PRIMARY KEY (access_point_id))""",
    # Operational tables
    """CREATE TABLE IF NOT EXISTS held_entities (
        held_id INTEGER PRIMARY KEY AUTOINCREMENT,
        record_id TEXT, entity_type TEXT, name TEXT, county TEXT,
        hold_reason TEXT, hold_detail TEXT, run_id TEXT, created_at TEXT)""",
    """CREATE TABLE IF NOT EXISTS manual_review_queue (
        review_id INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_id TEXT, entity_type TEXT, flag TEXT, notes TEXT,
        run_id TEXT, created_at TEXT)""",
    """CREATE TABLE IF NOT EXISTS entity_conflicts (
        conflict_id INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_id TEXT, field TEXT, value_a TEXT, value_b TEXT,
        resolution TEXT, run_id TEXT, created_at TEXT)""",
    """CREATE TABLE IF NOT EXISTS entity_uncertainty (
        uncertainty_id INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_id TEXT, flag TEXT, notes TEXT, run_id TEXT, created_at TEXT)""",
    """CREATE TABLE IF NOT EXISTS entity_geometry (
        geometry_id INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_id TEXT, geometry_type TEXT, geometry TEXT,
        run_id TEXT, created_at TEXT)""",
    # Provenance tables
    """CREATE TABLE IF NOT EXISTS run_metadata (
        run_id TEXT PRIMARY KEY, county TEXT, state TEXT, run_date TEXT,
        records_input INTEGER, normalized INTEGER, held INTEGER, rejected INTEGER,
        notes TEXT, created_at TEXT)""",
    """CREATE TABLE IF NOT EXISTS discovery_provenance (
        prov_id INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_id TEXT, entity_type TEXT, county TEXT, discovery_tier INTEGER,
        source_url TEXT, notes TEXT, run_id TEXT, created_at TEXT)""",
    """CREATE TABLE IF NOT EXISTS resolution_provenance (
        prov_id INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_id TEXT, entity_type TEXT, county TEXT, resolution_action TEXT,
        merged_from TEXT, conflict_detail TEXT, notes TEXT,
        run_id TEXT, created_at TEXT)""",
    """CREATE TABLE IF NOT EXISTS normalization_provenance (
        prov_id INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_id TEXT, entity_type TEXT, county TEXT, outcome TEXT,
        hold_reason TEXT, notes TEXT, run_id TEXT, created_at TEXT)""",
]
for ddl in DDL:
    cur.execute(ddl)
con.commit()
print("DDL: all tables verified.")

# ════════════════════════════════════════════════════════════════════════
# 1. SITES — 134 entities
# ════════════════════════════════════════════════════════════════════════
site_count = 0
for e in sites:
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
        c(e.get("site_id")),
        c(e.get("name")),
        c(e.get("category")),
        c(e.get("subtype")),
        c(e.get("designation")),
        c(e.get("status")),
        c(e.get("ownership")),
        c(e.get("governance")),
        c(e.get("partner_agencies")),
        c(e.get("coordination")),
        c(e.get("description")),
        c(e.get("location")),
        flt(e.get("acres")),
        c(e.get("counties")),
        c(e.get("municipality")),
        c(e.get("township")),
        flt(e.get("gps_lat")),
        flt(e.get("gps_lon")),
        c(e.get("plus_code")),
        c(e.get("features")),
        c(e.get("notes")),
        c(e.get("url_primary")),
        c(e.get("url_secondary")),   # normalized field → DB column 'urls'
        c(e.get("parent_site_id")),
        NOW,
        NOW,
        c(e.get("features_raw")),
    ))
    site_count += 1

# site_parent relationship table
sp_count = 0
for e in sites:
    psid = c(e.get("parent_site_id"))
    if psid:
        cur.execute("""
            INSERT OR IGNORE INTO site_parent (site_id, parent_site_id)
            VALUES (?, ?)
        """, (c(e["site_id"]), psid))
        sp_count += 1

con.commit()
print(f"Sites: {site_count} upserted, {sp_count} site_parent rows inserted.")

# ════════════════════════════════════════════════════════════════════════
# 2. TRAILS — 51 normalized + 4 cross-county = 55 total
# ════════════════════════════════════════════════════════════════════════
def upsert_trail(cur, t):
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
        c(t.get("trail_id")),
        c(t.get("name")),
        c(t.get("alternate_names", "")),
        c(t.get("use_type", "")),
        c(t.get("surface_type", t.get("surface", ""))),
        c(t.get("origin_type", t.get("origin", ""))),
        flt(t.get("length_mi")),
        c(t.get("counties")),
        c(t.get("governance", "")),
        c(t.get("partner_agencies", "")),
        c(t.get("status", "")),
        c(t.get("difficulty", "")),
        c(t.get("accessibility", "")),
        c(t.get("description", "")),
        c(t.get("trail_history", "")),
        c(t.get("identity_notes", "")),
        c(t.get("notes", "")),
        c(t.get("url_primary", "")),
        c(t.get("maps", "")),
        NOW,
        NOW,
    ))

trail_count = 0
tp_count = 0
for e in trails:
    upsert_trail(cur, e)
    trail_count += 1
    # trail_parents relationship
    psid = c(e.get("parent_site_id", ""))
    if psid:
        cur.execute("INSERT OR IGNORE INTO trail_parents (trail_id, parent_site_id) VALUES (?,?)",
                    (c(e["trail_id"]), psid))
        tp_count += 1

for t in CC_TRAILS:
    upsert_trail(cur, t)
    trail_count += 1

con.commit()
print(f"Trails: {trail_count} upserted, {tp_count} trail_parent rows inserted.")

# ════════════════════════════════════════════════════════════════════════
# 3. ACCESS POINTS — 6 normalized + 2 cross-county = 8 total
# ════════════════════════════════════════════════════════════════════════
def upsert_ap(cur, e):
    cur.execute("""
        INSERT INTO access_points
          (access_point_id,name,ap_type,status,parent_entity_type,parent_entity_id,
           county,township,municipality,address,gps_lat,gps_lon,plus_code,
           features,identity_notes,notes,url_primary,created_at,updated_at)
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
        c(e.get("access_point_id")),
        c(e.get("name")),
        c(e.get("ap_type", "")),
        c(e.get("status", "")),
        c(e.get("parent_entity_type", "")),
        c(e.get("parent_entity_id", "")),
        c(e.get("county", "")),
        c(e.get("township", "")),
        c(e.get("municipality", "")),
        c(e.get("address", "")),
        flt(e.get("gps_lat")),
        flt(e.get("gps_lon")),
        c(e.get("plus_code", "")),
        c(e.get("features", "")),
        c(e.get("identity_notes", "")),
        c(e.get("notes", "")),
        c(e.get("url_primary", "")),
        NOW,
        NOW,
    ))
    # access_point_parents relationship
    pet = c(e.get("parent_entity_type", ""))
    peid = c(e.get("parent_entity_id", ""))
    if pet and peid:
        cur.execute("""
            INSERT OR REPLACE INTO access_point_parents
              (access_point_id, parent_entity_type, parent_entity_id)
            VALUES (?,?,?)
        """, (c(e["access_point_id"]), pet, peid))

ap_count = 0
for e in aps:
    upsert_ap(cur, e)
    ap_count += 1
for e in CC_APS:
    upsert_ap(cur, e)
    ap_count += 1

con.commit()
print(f"Access Points: {ap_count} upserted.")

# ════════════════════════════════════════════════════════════════════════
# 4. SITE NETWORKS — 1 normalized + 1 cross-county = 2 total
# ════════════════════════════════════════════════════════════════════════
def upsert_sn(cur, e):
    nid = c(e.get("site_network_id") or e.get("network_id", ""))
    cur.execute("""
        INSERT INTO site_networks
          (network_id,name,network_type,status,ownership,governance,
           partner_agencies,counties,states_included,member_count,
           member_site_ids,description,identity_notes,notes,url_primary,
           created_at,updated_at,org_type)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT(network_id) DO UPDATE SET
          name=excluded.name, network_type=excluded.network_type,
          status=excluded.status, ownership=excluded.ownership,
          governance=excluded.governance, partner_agencies=excluded.partner_agencies,
          counties=excluded.counties, states_included=excluded.states_included,
          member_count=excluded.member_count, member_site_ids=excluded.member_site_ids,
          description=excluded.description, identity_notes=excluded.identity_notes,
          notes=excluded.notes, url_primary=excluded.url_primary,
          updated_at=excluded.updated_at
    """, (
        nid,
        c(e.get("name")),
        c(e.get("network_type", "")),
        c(e.get("status", "")),
        c(e.get("ownership", "")),
        c(e.get("governance", "")),
        c(e.get("partner_agencies", "")),
        c(e.get("counties", "")),
        c(e.get("states_included", "")),
        intt(e.get("member_count")),
        c(e.get("member_site_ids", "")),
        c(e.get("description", "")),
        c(e.get("identity_notes", "")),
        c(e.get("notes", "")),
        c(e.get("url_primary", "")),
        NOW,
        NOW,
        "",   # org_type — not populated for Ottawa
    ))

sn_count = 0
for e in networks:
    upsert_sn(cur, e)
    sn_count += 1
for e in CC_SITE_NETWORKS:
    upsert_sn(cur, e)
    sn_count += 1

con.commit()
print(f"Site Networks: {sn_count} upserted.")

# ════════════════════════════════════════════════════════════════════════
# 5. PROVENANCE — normalization_provenance for all 199 entities
# ════════════════════════════════════════════════════════════════════════
prov_count = 0

# Main pipeline entities (192)
for e in entities:
    eid = (e.get("site_id") or e.get("trail_id") or e.get("access_point_id")
           or e.get("site_network_id") or e.get("entity_id") or "")
    cur.execute("""
        INSERT INTO normalization_provenance
          (entity_id,entity_type,county,outcome,hold_reason,notes,run_id,created_at)
        VALUES (?,?,?,?,?,?,?,?)
    """, (
        c(eid),
        c(e.get("entity_type")),
        COUNTY,
        "normalized",
        "",
        "",
        RUN_ID,
        NOW,
    ))
    prov_count += 1

# Cross-county entities (7)
cc_prov = [
    ("OH-MC-T-0109",  "Trail",        "normalized", "Condition B MC ID assigned"),
    ("OH-MC-T-0110",  "Trail",        "normalized", "Condition B MC ID assigned"),
    ("OH-OTT-T-124",  "Trail",        "normalized", "Scenario A — provisional ID"),
    ("OH-MC-TR-002",  "Trail",        "normalized", "Ottawa first to pipeline; pre-existing MC ID"),
    ("OH-MC-SN-0002", "Site Network", "normalized", "Condition B MC ID assigned"),
    ("OH-OTT-AP-007", "Access Point", "normalized", "Unblocked — parent OH-MC-TR-002 confirmed"),
    ("OH-OTT-AP-008", "Access Point", "normalized", "Unblocked — parent OH-OTT-T-124 confirmed"),
]
for eid, etype, outcome, notes in cc_prov:
    cur.execute("""
        INSERT INTO normalization_provenance
          (entity_id,entity_type,county,outcome,hold_reason,notes,run_id,created_at)
        VALUES (?,?,?,?,?,?,?,?)
    """, (eid, etype, COUNTY, outcome, "", notes, RUN_ID, NOW))
    prov_count += 1

# Resolution provenance for MC ID assignments
mc_assignments = [
    ("OH-MC-T-0109",  "Trail",        "mc_id_assigned",   "OH-OTT-T-084", "Condition B — USFWS; no primary county anchor"),
    ("OH-MC-T-0110",  "Trail",        "mc_id_assigned",   "OH-OTT-T-125", "Condition B — multi-county rail trail"),
    ("OH-OTT-T-124",  "Trail",        "provisional_id",   "OH-OTT-T-124", "Scenario A — Ottawa-only; Erie not yet run"),
    ("OH-MC-SN-0002", "Site Network", "mc_id_assigned",   "OH-OTT-SN-001","Condition B — USFWS; no primary county anchor"),
    ("OH-OTT-AP-007", "Access Point", "parent_resolved",  "",             "Parent OH-MC-TR-002 confirmed via cross-county pass"),
    ("OH-OTT-AP-008", "Access Point", "parent_resolved",  "",             "Parent OH-OTT-T-124 confirmed via cross-county pass"),
]
for eid, etype, action, merged_from, notes in mc_assignments:
    cur.execute("""
        INSERT INTO resolution_provenance
          (entity_id,entity_type,county,resolution_run,notes,run_id,created_at)
        VALUES (?,?,?,?,?,?,?)
    """, (eid, etype, COUNTY, action, f"{merged_from} | {notes}".strip(" |"), RUN_ID, NOW))

con.commit()
print(f"Provenance: {prov_count} normalization_provenance rows inserted.")

# ════════════════════════════════════════════════════════════════════════
# 6. RUN METADATA
# ════════════════════════════════════════════════════════════════════════
cur.execute("""
    INSERT OR IGNORE INTO run_metadata
      (run_id,county,state,run_date,records_input,normalized,held,rejected,notes,created_at)
    VALUES (?,?,?,?,?,?,?,?,?,?)
""", (
    RUN_ID,
    COUNTY,
    STATE,
    RUN_DATE,
    198,    # original resolved.json count
    199,    # 192 main + 7 cross-county
    0,      # all 6 held entities resolved via cross-county pass
    0,
    "Ottawa County Ohio pipeline complete. 199 entities upserted (134 sites, 55 trails, 8 APs, 2 site networks). 7 cross-county entities resolved: OH-MC-T-0109 (Metzger Marsh Trail), OH-MC-T-0110 (North Coast Inland Trail), OH-OTT-T-124 (LEIT provisional), OH-MC-TR-002 (PRWT), OH-MC-SN-0002 (Ottawa NWR Complex), OH-OTT-AP-007, OH-OTT-AP-008. Stage 5 human review approved.",
    NOW,
))
con.commit()
print(f"run_metadata: run {RUN_ID} inserted.")

# ════════════════════════════════════════════════════════════════════════
# 7. VERIFICATION
# ════════════════════════════════════════════════════════════════════════
print("\n── Post-upsert verification ──")
site_n   = cur.execute("SELECT COUNT(*) FROM sites WHERE counties LIKE '%Ottawa%'").fetchone()[0]
trail_n  = cur.execute("SELECT COUNT(*) FROM trails WHERE counties LIKE '%Ottawa%'").fetchone()[0]
ap_n     = cur.execute("SELECT COUNT(*) FROM access_points WHERE county='Ottawa'").fetchone()[0]
sn_n     = cur.execute("SELECT COUNT(*) FROM site_networks WHERE counties LIKE '%Ottawa%'").fetchone()[0]
sp_n     = cur.execute("SELECT COUNT(*) FROM site_parent").fetchone()[0]
tp_n     = cur.execute("SELECT COUNT(*) FROM trail_parents").fetchone()[0]
app_n    = cur.execute("SELECT COUNT(*) FROM access_point_parents WHERE access_point_id LIKE 'OH-OTT-AP%'").fetchone()[0]
run_n    = cur.execute("SELECT normalized, held FROM run_metadata WHERE run_id=?", (RUN_ID,)).fetchone()

print(f"  Sites with Ottawa in counties:       {site_n}")
print(f"  Trails with Ottawa in counties:      {trail_n}")
print(f"  Access Points (county=Ottawa):       {ap_n}")
print(f"  Site Networks with Ottawa:           {sn_n}")
print(f"  site_parent rows (all):              {sp_n}")
print(f"  trail_parents rows (all):            {tp_n}")
print(f"  access_point_parents (OTT APs):      {app_n}")
print(f"  run_metadata normalized/held:        {run_n}")

# Spot-check key entities
checks = [
    ("OH-OTT-S-001", "sites",         "site_id"),
    ("OH-MC-T-0109", "trails",        "trail_id"),
    ("OH-MC-T-0110", "trails",        "trail_id"),
    ("OH-OTT-T-124", "trails",        "trail_id"),
    ("OH-MC-TR-002", "trails",        "trail_id"),
    ("OH-MC-SN-0002","site_networks", "network_id"),
    ("OH-OTT-AP-007","access_points", "access_point_id"),
    ("OH-OTT-AP-008","access_points", "access_point_id"),
]
print("\n  Key entity spot-checks:")
all_ok = True
for eid, tbl, col in checks:
    row = cur.execute(f"SELECT {col}, name FROM {tbl} WHERE {col}=?", (eid,)).fetchone()
    if row:
        print(f"    ✓ {eid} — {row[1][:50]}")
    else:
        print(f"    ✗ {eid} — NOT FOUND")
        all_ok = False

con.close()

print("\n" + "="*60)
if all_ok:
    print("✓ Stage 6 complete — Ottawa County upsert successful.")
    print(f"  Run ID: {RUN_ID}")
    print(f"  Entities: 134 sites | 55 trails | 8 APs | 2 site networks")
    print(f"  Total: 199 rows")
else:
    print("✗ Some spot-checks failed — review output above.")
    sys.exit(1)
                               