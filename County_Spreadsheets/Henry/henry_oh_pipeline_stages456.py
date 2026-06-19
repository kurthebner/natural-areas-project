#!/usr/bin/env python3
# =============================================================================
# SUPERSEDED — IMP-091 (2026-05-04)
# This monolithic pipeline script has been replaced by the parameterised model:
#   utilities/na_run_county.py + County_Spreadsheets/{County}/{county}_pipeline_config.json
# Do not use for new county runs. Kept for reference only.
# =============================================================================
"""
henry_oh_pipeline_stages456.py
Stages 4, 4.5, 5, 6 — Henry County, OH
Natural Areas Project v5 | Run ID: henry_oh_2026_04_20

Stage 4:   TSV Output (6 files, one per entity type)
Stage 4.5: Vocabulary Validation Gate (halts on any violation)
Stage 5:   TSV Integrity Check (non-halting, logs warnings)
Stage 6:   Database Upsert into NASqlite/natural_areas_v5.db

45 normalized entities eligible for upsert.
5 held entities (NONE GPS) → held_entities table only.
"""

import sys, os, csv, sqlite3, yaml, logging, pathlib, datetime, io

BASE       = "/sessions/trusting-sweet-gates/mnt/Natural Areas Project v5"
UTIL_PATH  = f"{BASE}/utilities"
sys.path.insert(0, UTIL_PATH)

from na_vocab_constants import (
    ALLOWED_CATEGORIES, ALLOWED_SUBTYPES, ALLOWED_FEATURES,
    ALLOWED_DESIGNATIONS, ALLOWED_SITE_STATUSES,
    ALLOWED_TRAIL_USE_TYPES, ALLOWED_TRAIL_SURFACES,
    ALLOWED_TRAIL_ORIGINS, ALLOWED_TRAIL_STATUSES,
    ALLOWED_TRAIL_DIFFICULTIES, ALLOWED_AP_TYPES, ALLOWED_AP_STATUSES,
)

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log = logging.getLogger(__name__)

# ── Constants ─────────────────────────────────────────────────────────────────
RUN_ID   = "henry_oh_2026_04_20"
COUNTY   = "Henry"
STATE    = "Ohio"
RUN_DATE = "2026-04-20"

NORM_FILE  = f"{BASE}/henry_oh_normalized_entities.yaml"
HELD_FILE  = f"{BASE}/henry_oh_held_entities.yaml"
OUTPUT_DIR = f"{BASE}/output"
DB_PATH    = f"{BASE}/NASqlite/natural_areas_v5.db"

NOW = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

pathlib.Path(OUTPUT_DIR).mkdir(exist_ok=True)


# ─────────────────────────────────────────────────────────────────────────────
#  Helpers
# ─────────────────────────────────────────────────────────────────────────────

def load_yaml(path: str) -> dict:
    return yaml.safe_load(pathlib.Path(path).read_text())

def sv(val) -> str:
    """Safe string coerce; None/float/int → str; strip whitespace."""
    if val is None:
        return ""
    return str(val).strip()

def write_tsv(path: str, cols: list[str], rows: list[dict]):
    """Write a TSV file with given columns."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t",
                           extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow({c: sv(row.get(c, "")) for c in cols})
    log.info(f"  Wrote {len(rows)} rows → {path}")


# ─────────────────────────────────────────────────────────────────────────────
#  Stage 4 — TSV Output
# ─────────────────────────────────────────────────────────────────────────────

SITES_COLS = [
    "name", "category", "subtype", "designation", "status",
    "ownership", "governance", "partner_agencies", "coordination",
    "description", "location", "acres", "counties", "municipality",
    "township", "gps_lat", "gps_lon", "plus_code", "features",
    "notes", "url_primary", "urls", "parent_site_id",
    "created_at", "updated_at",
]
# site_id and features_raw are DB-only — not in TSV

TRAILS_COLS = [
    "name", "alternate_names", "use_type", "surface_type", "origin_type",
    "length_mi", "counties", "governance", "partner_agencies", "status",
    "difficulty", "accessibility", "description", "trail_history",
    "identity_notes", "notes", "url_primary", "maps", "created_at", "updated_at",
]

TRAIL_SEGMENTS_COLS = [
    "parent_trail_id", "name", "counties", "governance", "length_mi",
    "surface_type", "segment_type", "status", "difficulty", "accessibility",
    "description", "identity_notes", "notes", "url_primary", "maps",
    "geometry", "created_at", "updated_at",
]

TRAIL_NETWORKS_COLS = [
    "name", "network_type", "status", "ownership", "governance",
    "partner_agencies", "counties", "states_included", "length_mi",
    "member_trail_count", "member_trail_ids", "description", "identity_notes",
    "notes", "url_primary", "maps", "created_at", "updated_at",
]

SITE_NETWORKS_COLS = [
    "name", "network_type", "status", "ownership", "governance",
    "partner_agencies", "counties", "states_included", "member_count",
    "member_site_ids", "description", "identity_notes", "notes",
    "url_primary", "created_at", "updated_at",
]

ACCESS_POINTS_COLS = [
    "name", "ap_type", "status", "parent_entity_type", "parent_entity_id",
    "county", "township", "municipality", "address", "gps_lat", "gps_lon",
    "plus_code", "features", "identity_notes", "notes", "url_primary",
    "created_at", "updated_at",
]


def stage4_tsv_output(normalized: list[dict]) -> dict[str, list[dict]]:
    """Split normalized entities by type and write TSV files. Returns by_type dict."""
    log.info("\n── Stage 4: TSV Output ──────────────────────────────────────")

    by_type: dict[str, list] = {
        "Site": [], "Trail": [], "Trail Segment": [],
        "Trail Network": [], "Site Network": [], "Access Point": [],
    }
    for e in normalized:
        et = e.get("entity_type", "")
        if et in by_type:
            by_type[et].append(e)

    # Map normalized entity fields to TSV row fields
    def site_to_row(e: dict) -> dict:
        return {
            **{c: e.get(c, "") for c in SITES_COLS},
            "parent_site_id": e.get("parent_site_id", ""),
        }

    def trail_to_row(e: dict) -> dict:
        return {
            "name":           e.get("name", ""),
            "alternate_names": e.get("alternate_names", ""),
            "use_type":       e.get("use_type", ""),
            "surface_type":   e.get("surface_type", ""),
            "origin_type":    e.get("origin_type", ""),
            "length_mi":      e.get("length_mi", ""),
            "counties":       e.get("counties", ""),
            "governance":     e.get("governance", ""),
            "partner_agencies": e.get("partner_agencies", ""),
            "status":         e.get("status", ""),
            "difficulty":     e.get("difficulty", ""),
            "accessibility":  e.get("accessibility", ""),
            "description":    e.get("description", ""),
            "trail_history":  e.get("trail_history", ""),
            "identity_notes": e.get("identity_notes", ""),
            "notes":          e.get("notes", ""),
            "url_primary":    e.get("url_primary", ""),
            "maps":           e.get("maps", ""),
            "created_at":     e.get("created_at", NOW),
            "updated_at":     e.get("updated_at", NOW),
        }

    def segment_to_row(e: dict) -> dict:
        return {
            "parent_trail_id": e.get("parent_trail_id", ""),
            "name":            e.get("name", ""),
            "counties":        e.get("counties", ""),
            "governance":      e.get("governance", ""),
            "length_mi":       e.get("length_mi", ""),
            "surface_type":    e.get("surface_type", ""),
            "segment_type":    e.get("segment_type", ""),
            "status":          e.get("status", ""),
            "difficulty":      e.get("difficulty", ""),
            "accessibility":   e.get("accessibility", ""),
            "description":     e.get("description", ""),
            "identity_notes":  e.get("identity_notes", ""),
            "notes":           e.get("notes", ""),
            "url_primary":     e.get("url_primary", ""),
            "maps":            e.get("maps", ""),
            "geometry":        e.get("geometry", ""),
            "created_at":      e.get("created_at", NOW),
            "updated_at":      e.get("updated_at", NOW),
        }

    def ap_to_row(e: dict) -> dict:
        # Resolve parent fields — normalized entity stores parent_entity_type / parent_entity_id
        pet  = e.get("parent_entity_type", "")
        peid = e.get("parent_entity_id", "")
        # If stored as parent_site_id or parent_trail_id, handle that
        if not peid:
            if e.get("parent_site_id"):
                pet, peid = "Site", e["parent_site_id"]
            elif e.get("parent_trail_id"):
                pet, peid = "Trail", e["parent_trail_id"]
        return {
            "name":               e.get("name", ""),
            "ap_type":            e.get("access_point_type", "") or e.get("ap_type", ""),
            "status":             e.get("status", ""),
            "parent_entity_type": pet,
            "parent_entity_id":   peid,
            "county":             e.get("county", "") or e.get("counties", "").split(";")[0],
            "township":           e.get("township", ""),
            "municipality":       e.get("municipality", ""),
            "address":            e.get("address", ""),
            "gps_lat":            e.get("gps_lat", ""),
            "gps_lon":            e.get("gps_lon", ""),
            "plus_code":          e.get("plus_code", ""),
            "features":           e.get("features", ""),
            "identity_notes":     e.get("identity_notes", ""),
            "notes":              e.get("notes", ""),
            "url_primary":        e.get("url_primary", ""),
            "created_at":         e.get("created_at", NOW),
            "updated_at":         e.get("updated_at", NOW),
        }

    write_tsv(f"{OUTPUT_DIR}/henry_oh_sites.tsv",          SITES_COLS,          [site_to_row(e) for e in by_type["Site"]])
    write_tsv(f"{OUTPUT_DIR}/henry_oh_trails.tsv",         TRAILS_COLS,         [trail_to_row(e) for e in by_type["Trail"]])
    write_tsv(f"{OUTPUT_DIR}/henry_oh_trail_segments.tsv", TRAIL_SEGMENTS_COLS, [segment_to_row(e) for e in by_type["Trail Segment"]])
    write_tsv(f"{OUTPUT_DIR}/henry_oh_trail_networks.tsv", TRAIL_NETWORKS_COLS, [])   # 0 entities
    write_tsv(f"{OUTPUT_DIR}/henry_oh_site_networks.tsv",  SITE_NETWORKS_COLS,  [])   # 0 entities
    write_tsv(f"{OUTPUT_DIR}/henry_oh_access_points.tsv",  ACCESS_POINTS_COLS,  [ap_to_row(e) for e in by_type["Access Point"]])

    for et, ents in by_type.items():
        log.info(f"  {et}: {len(ents)} entities")

    return by_type


# ─────────────────────────────────────────────────────────────────────────────
#  Stage 4.5 — Vocabulary Validation Gate
# ─────────────────────────────────────────────────────────────────────────────

def stage45_vocab_gate(normalized: list[dict]):
    """Halt pipeline on any vocabulary violation."""
    log.info("\n── Stage 4.5: Vocabulary Gate ────────────────────────────────")
    violations = []

    for e in normalized:
        eid = e.get("entity_id", "?")
        et  = e.get("entity_type", "")

        if et == "Site":
            cat = e.get("category", "")
            sub = e.get("subtype", "")
            des = e.get("designation", "")
            sta = e.get("status", "")
            feats = e.get("features", "")

            if cat and cat not in ALLOWED_CATEGORIES:
                violations.append(f"[{eid}] Invalid category: {cat!r}")
            if sub and cat and sub not in ALLOWED_SUBTYPES.get(cat, set()):
                violations.append(f"[{eid}] Invalid subtype {sub!r} for category {cat!r}")
            if des and des not in ALLOWED_DESIGNATIONS:
                violations.append(f"[{eid}] Invalid designation: {des!r}")
            if sta and sta not in ALLOWED_SITE_STATUSES:
                violations.append(f"[{eid}] Invalid status: {sta!r}")
            for term in (feats or "").split(";"):
                term = term.strip()
                if term and term not in ALLOWED_FEATURES:
                    violations.append(f"[{eid}] Invalid features term: {term!r}")

        elif et == "Trail":
            for field, allowed in [
                ("use_type",     ALLOWED_TRAIL_USE_TYPES),
                ("surface_type", ALLOWED_TRAIL_SURFACES),
                ("origin_type",  ALLOWED_TRAIL_ORIGINS),
                ("status",       ALLOWED_TRAIL_STATUSES),
                ("difficulty",   ALLOWED_TRAIL_DIFFICULTIES),
            ]:
                val = e.get(field, "")
                if val and val not in allowed:
                    violations.append(f"[{eid}] Invalid trail {field}: {val!r}")

        elif et == "Trail Segment":
            for field, allowed in [
                ("surface_type", ALLOWED_TRAIL_SURFACES),
                ("status",       ALLOWED_TRAIL_STATUSES),
                ("difficulty",   ALLOWED_TRAIL_DIFFICULTIES),
            ]:
                val = e.get(field, "")
                if val and val not in allowed:
                    violations.append(f"[{eid}] Invalid trail segment {field}: {val!r}")

        elif et == "Access Point":
            ap_type = e.get("access_point_type", "") or e.get("ap_type", "")
            ap_sta  = e.get("status", "")
            if ap_type and ap_type not in ALLOWED_AP_TYPES:
                violations.append(f"[{eid}] Invalid AP type: {ap_type!r}")
            if ap_sta and ap_sta not in ALLOWED_AP_STATUSES:
                violations.append(f"[{eid}] Invalid AP status: {ap_sta!r}")

    if violations:
        log.error(f"\n{'!'*60}")
        log.error(f"VOCABULARY GATE FAILED — {len(violations)} violations:")
        for v in violations:
            log.error(f"  {v}")
        log.error(f"{'!'*60}\n")
        raise SystemExit("Stage 4.5 halted — vocabulary violations must be fixed before upsert.")
    else:
        log.info(f"  PASSED — 0 violations across {len(normalized)} entities")


# ─────────────────────────────────────────────────────────────────────────────
#  Stage 5 — TSV Integrity Check
# ─────────────────────────────────────────────────────────────────────────────

def stage5_integrity_check(by_type: dict[str, list], normalized: list[dict]):
    """Non-halting integrity checks. Log warnings."""
    log.info("\n── Stage 5: TSV Integrity Check ──────────────────────────────")
    warnings = []

    site_ids   = {e["entity_id"] for e in by_type["Site"]}
    trail_ids  = {e["entity_id"] for e in by_type["Trail"]}
    entity_ids = {e["entity_id"] for e in normalized}

    # Check for GPS presence on Sites
    sites_no_gps = [e["entity_id"] for e in by_type["Site"] if not e.get("gps_lat")]
    if sites_no_gps:
        warnings.append(f"Sites missing GPS (should not occur post-GPS-merge): {sites_no_gps}")

    # Check AP GPS
    aps_no_gps = [e["entity_id"] for e in by_type["Access Point"] if not e.get("gps_lat")]
    if aps_no_gps:
        warnings.append(f"Access Points missing GPS: {aps_no_gps}")

    # Check parent_site_id references for sites
    for e in by_type["Site"]:
        psid = e.get("parent_site_id", "")
        if psid and psid not in site_ids:
            warnings.append(f"[{e['entity_id']}] parent_site_id {psid!r} not in this run's sites")

    # Check parent_trail references for segments
    for e in by_type["Trail Segment"]:
        ptid = e.get("parent_trail_id", "")
        if ptid and ptid not in trail_ids:
            warnings.append(f"[{e['entity_id']}] parent_trail_id {ptid!r} not in this run's trails")

    # Check AP parent references
    for e in by_type["Access Point"]:
        pet  = e.get("parent_entity_type", "")
        peid = e.get("parent_entity_id", "")
        if peid:
            if pet == "Site" and peid not in site_ids:
                warnings.append(f"[{e['entity_id']}] AP parent site {peid!r} not in this run")
            elif pet == "Trail" and peid not in trail_ids:
                warnings.append(f"[{e['entity_id']}] AP parent trail {peid!r} not in this run")

    # Duplicate entity_id check
    all_ids = [e["entity_id"] for e in normalized]
    seen = set()
    for eid in all_ids:
        if eid in seen:
            warnings.append(f"Duplicate entity_id: {eid!r}")
        seen.add(eid)

    if warnings:
        log.warning(f"  {len(warnings)} integrity warning(s):")
        for w in warnings:
            log.warning(f"    ⚠  {w}")
    else:
        log.info(f"  PASSED — 0 warnings")

    return warnings


# ─────────────────────────────────────────────────────────────────────────────
#  Stage 6 — Database Upsert
# ─────────────────────────────────────────────────────────────────────────────

def upsert_sites(cur: sqlite3.Cursor, sites: list[dict]):
    sql = """
    INSERT INTO sites
      (site_id, name, category, subtype, designation, status, ownership, governance,
       partner_agencies, coordination, description, location, acres, counties,
       municipality, township, gps_lat, gps_lon, plus_code, features, features_raw,
       notes, url_primary, urls, parent_site_id, created_at, updated_at)
    VALUES
      (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    ON CONFLICT(site_id) DO UPDATE SET
      name=excluded.name, category=excluded.category, subtype=excluded.subtype,
      designation=excluded.designation, status=excluded.status, ownership=excluded.ownership,
      governance=excluded.governance, partner_agencies=excluded.partner_agencies,
      coordination=excluded.coordination, description=excluded.description,
      location=excluded.location, acres=excluded.acres, counties=excluded.counties,
      municipality=excluded.municipality, township=excluded.township,
      gps_lat=excluded.gps_lat, gps_lon=excluded.gps_lon, plus_code=excluded.plus_code,
      features=excluded.features, features_raw=excluded.features_raw,
      notes=excluded.notes, url_primary=excluded.url_primary, urls=excluded.urls,
      parent_site_id=excluded.parent_site_id, updated_at=excluded.updated_at
    """
    for e in sites:
        cur.execute(sql, (
            sv(e.get("entity_id")), sv(e.get("name")), sv(e.get("category")),
            sv(e.get("subtype")), sv(e.get("designation")), sv(e.get("status")),
            sv(e.get("ownership")), sv(e.get("governance")), sv(e.get("partner_agencies")),
            sv(e.get("coordination")), sv(e.get("description")), sv(e.get("location")),
            sv(e.get("acres")), sv(e.get("counties")), sv(e.get("municipality")),
            sv(e.get("township")), sv(e.get("gps_lat")), sv(e.get("gps_lon")),
            sv(e.get("plus_code")), sv(e.get("features")), sv(e.get("features_raw")),
            sv(e.get("notes")), sv(e.get("url_primary")), sv(e.get("urls")),
            sv(e.get("parent_site_id")),
            sv(e.get("created_at") or NOW), sv(e.get("updated_at") or NOW),
        ))
    log.info(f"  Upserted {len(sites)} sites")


def upsert_trails(cur: sqlite3.Cursor, trails: list[dict]):
    sql = """
    INSERT INTO trails
      (trail_id, name, alternate_names, use_type, surface_type, origin_type, length_mi,
       counties, governance, partner_agencies, status, difficulty, accessibility,
       description, trail_history, identity_notes, notes, url_primary, maps,
       created_at, updated_at)
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
      url_primary=excluded.url_primary, maps=excluded.maps, updated_at=excluded.updated_at
    """
    for e in trails:
        cur.execute(sql, (
            sv(e.get("entity_id")), sv(e.get("name")), sv(e.get("alternate_names")),
            sv(e.get("use_type")), sv(e.get("surface_type")), sv(e.get("origin_type")),
            sv(e.get("length_mi")), sv(e.get("counties")), sv(e.get("governance")),
            sv(e.get("partner_agencies")), sv(e.get("status")), sv(e.get("difficulty")),
            sv(e.get("accessibility")), sv(e.get("description")), sv(e.get("trail_history")),
            sv(e.get("identity_notes")), sv(e.get("notes")), sv(e.get("url_primary")),
            sv(e.get("maps")), sv(e.get("created_at") or NOW), sv(e.get("updated_at") or NOW),
        ))
    log.info(f"  Upserted {len(trails)} trails")


def upsert_trail_segments(cur: sqlite3.Cursor, segments: list[dict]):
    sql = """
    INSERT INTO trail_segments
      (segment_id, parent_trail_id, name, counties, governance, length_mi,
       surface_type, segment_type, status, difficulty, accessibility,
       description, identity_notes, notes, url_primary, maps, geometry,
       created_at, updated_at)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    ON CONFLICT(segment_id) DO UPDATE SET
      parent_trail_id=excluded.parent_trail_id, name=excluded.name,
      counties=excluded.counties, governance=excluded.governance,
      length_mi=excluded.length_mi, surface_type=excluded.surface_type,
      segment_type=excluded.segment_type, status=excluded.status,
      difficulty=excluded.difficulty, accessibility=excluded.accessibility,
      description=excluded.description, identity_notes=excluded.identity_notes,
      notes=excluded.notes, url_primary=excluded.url_primary,
      maps=excluded.maps, geometry=excluded.geometry, updated_at=excluded.updated_at
    """
    for e in segments:
        cur.execute(sql, (
            sv(e.get("entity_id")), sv(e.get("parent_trail_id")), sv(e.get("name")),
            sv(e.get("counties")), sv(e.get("governance")), sv(e.get("length_mi")),
            sv(e.get("surface_type")), sv(e.get("segment_type")), sv(e.get("status")),
            sv(e.get("difficulty")), sv(e.get("accessibility")), sv(e.get("description")),
            sv(e.get("identity_notes")), sv(e.get("notes")), sv(e.get("url_primary")),
            sv(e.get("maps")), sv(e.get("geometry")),
            sv(e.get("created_at") or NOW), sv(e.get("updated_at") or NOW),
        ))
    log.info(f"  Upserted {len(segments)} trail segments")


def upsert_access_points(cur: sqlite3.Cursor, aps: list[dict]):
    sql = """
    INSERT INTO access_points
      (access_point_id, name, ap_type, status, parent_entity_type, parent_entity_id,
       county, township, municipality, address, gps_lat, gps_lon, plus_code,
       features, identity_notes, notes, url_primary, created_at, updated_at)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    ON CONFLICT(access_point_id) DO UPDATE SET
      name=excluded.name, ap_type=excluded.ap_type, status=excluded.status,
      parent_entity_type=excluded.parent_entity_type, parent_entity_id=excluded.parent_entity_id,
      county=excluded.county, township=excluded.township, municipality=excluded.municipality,
      address=excluded.address, gps_lat=excluded.gps_lat, gps_lon=excluded.gps_lon,
      plus_code=excluded.plus_code, features=excluded.features,
      identity_notes=excluded.identity_notes, notes=excluded.notes,
      url_primary=excluded.url_primary, updated_at=excluded.updated_at
    """
    for e in aps:
        # Resolve parent
        pet  = sv(e.get("parent_entity_type", ""))
        peid = sv(e.get("parent_entity_id", ""))
        if not peid:
            if e.get("parent_site_id"):
                pet, peid = "Site", sv(e["parent_site_id"])
            elif e.get("parent_trail_id"):
                pet, peid = "Trail", sv(e["parent_trail_id"])
        county = sv(e.get("county") or (e.get("counties", "").split(";")[0] if e.get("counties") else ""))

        cur.execute(sql, (
            sv(e.get("entity_id")), sv(e.get("name")), sv(e.get("access_point_type") or e.get("ap_type")),
            sv(e.get("status")), pet, peid,
            county, sv(e.get("township")), sv(e.get("municipality")),
            sv(e.get("address")), sv(e.get("gps_lat")), sv(e.get("gps_lon")),
            sv(e.get("plus_code")), sv(e.get("features")), sv(e.get("identity_notes")),
            sv(e.get("notes")), sv(e.get("url_primary")),
            sv(e.get("created_at") or NOW), sv(e.get("updated_at") or NOW),
        ))
    log.info(f"  Upserted {len(aps)} access points")


def upsert_held(cur: sqlite3.Cursor, held: list[dict]):
    sql = """
    INSERT OR IGNORE INTO held_entities
      (record_id, entity_type, name, county, hold_reason, hold_detail, run_id, created_at)
    VALUES (?,?,?,?,?,?,?,?)
    """
    for h in held:
        cur.execute(sql, (
            sv(h.get("record_id")), sv(h.get("entity_type")), sv(h.get("name")),
            sv(h.get("county")), sv(h.get("hold_reason")), sv(h.get("hold_detail")),
            sv(h.get("run_id") or RUN_ID), sv(h.get("created_at") or NOW),
        ))
    log.info(f"  Inserted {len(held)} held entities")


def upsert_run_metadata(cur: sqlite3.Cursor, n_input: int, n_normalized: int, n_held: int):
    sql = """
    INSERT OR IGNORE INTO run_metadata
      (run_id, county, state, run_date, records_input, normalized, held, rejected, notes, created_at)
    VALUES (?,?,?,?,?,?,?,?,?,?)
    """
    notes_val = (
        f"45 normalized (26 Sites, 7 Trails, 6 Trail Segments, 6 Access Points). "
        f"5 held NONE-GPS: HC WA 1/2/3, Maumee Scenic River, North Turkeyfoot WA. "
        f"Stage 4.5 vocab gate passed. Stage 3 patch: HEN_S_012 category corrected."
    )
    cur.execute(sql, (
        RUN_ID, COUNTY, STATE, RUN_DATE,
        n_input, n_normalized, n_held, 0,
        notes_val, NOW,
    ))
    log.info(f"  Upserted run_metadata for {RUN_ID}")


def stage6_upsert(by_type: dict, held: list[dict], n_input: int):
    log.info("\n── Stage 6: Database Upsert ──────────────────────────────────")
    db = sqlite3.connect(DB_PATH)
    db.execute("PRAGMA journal_mode=WAL")
    db.execute("PRAGMA foreign_keys=ON")
    cur = db.cursor()

    try:
        upsert_sites(cur,          by_type["Site"])
        upsert_trails(cur,         by_type["Trail"])
        upsert_trail_segments(cur, by_type["Trail Segment"])
        upsert_access_points(cur,  by_type["Access Point"])
        upsert_held(cur,           held)
        upsert_run_metadata(cur, n_input, sum(len(v) for v in by_type.values()), len(held))
        db.commit()
        log.info("  ✓ Commit successful")
    except Exception as ex:
        db.rollback()
        log.error(f"  ✗ DB error — rolled back: {ex}")
        raise
    finally:
        db.close()


# ─────────────────────────────────────────────────────────────────────────────
#  Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    log.info(f"Pipeline Stages 4–6 | {RUN_ID}")

    norm_data = load_yaml(NORM_FILE)
    held_data = load_yaml(HELD_FILE)
    normalized = norm_data["normalized_entities"]
    held       = held_data["held_entities"]

    log.info(f"Loaded {len(normalized)} normalized entities, {len(held)} held")

    # Stage 4
    by_type = stage4_tsv_output(normalized)

    # Stage 4.5
    stage45_vocab_gate(normalized)

    # Stage 5
    warnings = stage5_integrity_check(by_type, normalized)

    # Stage 6
    stage6_upsert(by_type, held, n_input=50)

    # Final summary
    log.info(f"\n{'='*60}")
    log.info("PIPELINE STAGES 4–6 COMPLETE")
    log.info(f"  Normalized/upserted: {len(normalized)}")
    log.info(f"  Held (NONE GPS):     {len(held)}")
    log.info(f"  Integrity warnings:  {len(warnings)}")
    log.info(f"  DB: {DB_PATH}")
    log.info(f"  TSV: {OUTPUT_DIR}/henry_oh_*.tsv")


if __name__ == "__main__":
    main()
