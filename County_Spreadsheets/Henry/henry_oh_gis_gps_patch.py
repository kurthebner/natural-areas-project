#!/usr/bin/env python3
"""
henry_oh_gis_gps_patch.py — Post-pipeline ODNR GIS GPS Patch
Henry County, Ohio | Run ID: henry_oh_2026_04_20

Applies ODNR GIS parcel centroids to 4 held wildlife area entities
(HEN_S_013/014/015/023) and upgrades HEN_S_006 from LOW → HIGH confidence.

Source: ODNR DOW_Services/Roads_ParkingAreas/FeatureServer layer 28
Method: Polygon centroid from official DOW parcel boundary geometry
Confidence: HIGH (authoritative state GIS parcel data)
"""

import sys, os, yaml, logging, pathlib, sqlite3, datetime

BASE       = "/sessions/trusting-sweet-gates/mnt/Natural Areas Project v5"
PROCESSING = f"{BASE}/processing"
UTIL_PATH  = f"{BASE}/utilities"
DB_PATH    = f"{BASE}/NASqlite/natural_areas_v5.db"

sys.path.insert(0, UTIL_PATH)
sys.path.insert(0, PROCESSING)

import importlib.util
stage2_path = f"{PROCESSING}/henry_oh_normalization_stage2.py"
spec = importlib.util.spec_from_file_location("stage2", stage2_path)
stage2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stage2)

normalize_site  = stage2.normalize_site
gis_lookup      = stage2.gis_lookup
get_plus_code   = stage2.get_plus_code

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

RUN_ID    = "henry_oh_2026_04_20"
NORM_DATE = "2026-04-27"

NORM_FILE     = f"{BASE}/henry_oh_normalized_entities.yaml"
HELD_FILE     = f"{BASE}/henry_oh_held_entities.yaml"
RESOLVED_FILE = f"{BASE}/henry_oh_resolved_entities.yaml"

# ── ODNR GIS centroids (from DOW parcel boundary polygons) ───────────────────
GIS_GPS = {
    "HEN_S_013": {"lat": 41.323055, "lon": -83.890652, "name": "Henry County Wildlife Area 1",  "acres": 59.89},
    "HEN_S_014": {"lat": 41.322366, "lon": -84.161557, "name": "Henry County Wildlife Area 2",  "acres": 38.85},
    "HEN_S_015": {"lat": 41.277479, "lon": -84.077872, "name": "Henry County Wildlife Area 3",  "acres": 40.46},
    "HEN_S_023": {"lat": 41.411469, "lon": -83.989405, "name": "North Turkeyfoot Wildlife Area", "acres": 548.53},
    # GPS upgrade (already normalized, LOW → HIGH)
    "HEN_S_006": {"lat": 41.332353, "lon": -84.179489, "name": "Florida Wildlife Area",          "acres": 3.44},
}

GPS_NOTE = (
    "GPS: ODNR GIS polygon centroid — DOW_Services/Roads_ParkingAreas/FeatureServer "
    "layer 28 (official DOW parcel boundary, queried 2026-04-27)"
)


def load_yaml(path):
    return yaml.safe_load(pathlib.Path(path).read_text())

def save_yaml(path, data):
    pathlib.Path(path).write_text(yaml.dump(data, allow_unicode=True, sort_keys=False))


def main():
    logger.info("ODNR GIS GPS Patch — Henry County, OH")

    norm_data     = load_yaml(NORM_FILE)
    held_data     = load_yaml(HELD_FILE)
    resolved_data = load_yaml(RESOLVED_FILE)

    norm_entities  = norm_data["normalized_entities"]
    held_entities  = held_data["held_entities"]
    resolved_map   = {e["resolved_entity_id"]: e for e in resolved_data["resolved_entities"]}

    # ── 1. Upgrade HEN_S_006 (Florida WA) in normalized_entities ─────────────
    eid_upgrade = "HEN_S_006"
    info = GIS_GPS[eid_upgrade]
    lat, lon = info["lat"], info["lon"]
    twp, muni = gis_lookup(lat, lon)
    pc = get_plus_code(lat, lon)

    upgraded = False
    for ent in norm_entities:
        if ent.get("entity_id") == eid_upgrade:
            old_lat = ent.get("gps_lat")
            old_pc  = ent.get("plus_code")
            ent["gps_lat"]     = round(lat, 6)
            ent["gps_lon"]     = round(lon, 6)
            ent["plus_code"]   = pc
            ent["township"]    = twp
            ent["municipality"] = muni
            note = GPS_NOTE
            existing = ent.get("identity_notes", "")
            ent["identity_notes"] = f"{existing} | GPS upgraded: LOW centroid → HIGH (ODNR GIS parcel, 2026-04-27)" if existing else f"GPS upgraded: LOW centroid → HIGH (ODNR GIS parcel, 2026-04-27)"
            # Remove LOW confidence warning from notes if present
            existing_notes = ent.get("notes", "")
            if "LOW confidence" in existing_notes:
                # strip the LOW-confidence note
                cleaned = ". ".join(
                    s for s in existing_notes.split(". ")
                    if "LOW confidence" not in s
                ).strip()
                ent["notes"] = (cleaned + f" {GPS_NOTE}").strip() if cleaned else GPS_NOTE
            else:
                ent["notes"] = f"{existing_notes} {GPS_NOTE}".strip() if existing_notes else GPS_NOTE
            logger.info(f"  ✓ Upgraded {eid_upgrade}: lat={old_lat}→{ent['gps_lat']}, plus_code {old_pc}→{pc}, twp={twp}, muni={muni}")
            upgraded = True
            break
    if not upgraded:
        logger.warning(f"  !! {eid_upgrade} not found in normalized_entities — skipping upgrade")

    # ── 2. Normalize held WA entities with ODNR GIS GPS ──────────────────────
    newly_normalized = []
    remaining_held   = []

    for held in held_entities:
        eid = held["record_id"]

        if eid == "HEN_S_019":
            # Linear feature — stays held permanently
            remaining_held.append(held)
            logger.info(f"  → {eid} stays held (linear feature, NONE GPS by design)")
            continue

        if eid not in GIS_GPS:
            remaining_held.append(held)
            logger.info(f"  → {eid} has no GIS GPS entry — remains held")
            continue

        info = GIS_GPS[eid]
        lat, lon = info["lat"], info["lon"]

        resolved_entity = resolved_map.get(eid)
        if not resolved_entity:
            logger.error(f"  !! No resolved entity found for {eid} — stays held")
            remaining_held.append(held)
            continue

        # Inject GPS into payload
        payload = resolved_entity.get("payload", {})
        payload["gps_lat_raw"] = str(lat)
        payload["gps_lon_raw"] = str(lon)

        twp, muni = gis_lookup(lat, lon)
        logger.info(f"\n  {eid} — {info['name']}: ({lat}, {lon}) | twp={twp!r}, muni={muni!r}")

        provenance = []
        norm = normalize_site(resolved_entity, provenance)

        if norm is None:
            logger.error(f"  !! normalize_site returned None for {eid} — stays held")
            remaining_held.append(held)
            continue

        # Ensure GPS is set (force if normalize_site didn't pick it up)
        if not norm.get("gps_lat"):
            norm["gps_lat"]      = round(lat, 6)
            norm["gps_lon"]      = round(lon, 6)
            norm["plus_code"]    = get_plus_code(lat, lon)
            norm["township"]     = twp
            norm["municipality"] = muni

        # Tag GPS source
        existing_notes = norm.get("identity_notes", "")
        gps_tag = f"GPS: HIGH confidence — ODNR GIS parcel centroid (DOW_Services layer 28, 2026-04-27)"
        norm["identity_notes"] = f"{existing_notes} | {gps_tag}" if existing_notes else gps_tag

        newly_normalized.append(norm)
        logger.info(f"  → Normalized: lat={norm['gps_lat']}, lon={norm['gps_lon']}, pc={norm.get('plus_code')}")

    # ── 3. Merge newly normalized ─────────────────────────────────────────────
    norm_entities.extend(newly_normalized)

    type_counts = {}
    for e in norm_entities:
        et = e.get("entity_type", "Unknown")
        type_counts[et] = type_counts.get(et, 0) + 1

    norm_data["normalized_entities"] = norm_entities
    norm_data["normalized"] = len(norm_entities)
    norm_data["held"]       = len(remaining_held)
    norm_data["entities_by_type"] = type_counts
    save_yaml(NORM_FILE, norm_data)
    logger.info(f"\n  Normalized entities: {len(norm_entities)} total ({len(newly_normalized)} newly added)")

    held_data["held_entities"] = remaining_held
    held_data["count"]         = len(remaining_held)
    save_yaml(HELD_FILE, held_data)
    logger.info(f"  Held entities: {len(remaining_held)} remaining")

    # ── 4. Database updates ───────────────────────────────────────────────────
    conn = sqlite3.connect(DB_PATH)
    cur  = conn.cursor()
    now  = datetime.datetime.now().isoformat()

    # 4a. Upgrade HEN_S_006
    for ent in norm_entities:
        if ent.get("entity_id") == "HEN_S_006":
            cur.execute("""
                UPDATE sites SET
                    gps_lat    = ?, gps_lon     = ?,
                    plus_code  = ?, township    = ?,
                    municipality = ?, notes      = ?,
                    identity_notes = ?, updated_at = ?
                WHERE site_id = ?
            """, (
                ent.get("gps_lat"), ent.get("gps_lon"),
                ent.get("plus_code"), ent.get("township"),
                ent.get("municipality"), ent.get("notes"),
                ent.get("identity_notes"), now,
                "HEN_S_006",
            ))
            logger.info(f"  DB updated: HEN_S_006 ({cur.rowcount} row)")
            break

    # 4b. Upsert newly normalized entities
    for norm in newly_normalized:
        cur.execute("""
            INSERT INTO sites
                (site_id, name, category, subtype, designation, status, ownership,
                 governance, partner_agencies, coordination, description, location,
                 acres, counties, municipality, township, gps_lat, gps_lon, plus_code,
                 features, features_raw, notes, url_primary, urls, parent_site_id,
                 identity_notes, created_at, updated_at)
            VALUES
                (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ON CONFLICT(site_id) DO UPDATE SET
                gps_lat=excluded.gps_lat, gps_lon=excluded.gps_lon,
                plus_code=excluded.plus_code, township=excluded.township,
                municipality=excluded.municipality, identity_notes=excluded.identity_notes,
                updated_at=excluded.updated_at
        """, (
            norm.get("entity_id"),
            norm.get("name"),
            norm.get("category"),
            norm.get("subtype"),
            norm.get("designation"),
            norm.get("status"),
            norm.get("ownership"),
            norm.get("governance"),
            norm.get("partner_agencies"),
            norm.get("coordination"),
            norm.get("description"),
            norm.get("location"),
            norm.get("acres"),
            norm.get("counties"),
            norm.get("municipality"),
            norm.get("township"),
            norm.get("gps_lat"),
            norm.get("gps_lon"),
            norm.get("plus_code"),
            norm.get("features"),
            norm.get("features_raw"),
            norm.get("notes"),
            norm.get("url_primary"),
            norm.get("urls"),
            norm.get("parent_site_id"),
            norm.get("identity_notes"),
            now, now,
        ))
        logger.info(f"  DB upserted: {norm.get('entity_id')} — {norm.get('name')}")

    # 4c. Update run_metadata
    cur.execute("""
        UPDATE run_metadata SET normalized=?, held=?, updated_at=?
        WHERE run_id=?
    """, (len(norm_entities), len(remaining_held), now, RUN_ID))

    conn.commit()
    conn.close()
    logger.info("  DB committed.")

    # ── 5. Summary ────────────────────────────────────────────────────────────
    logger.info(f"\n{'='*60}")
    logger.info(f"ODNR GIS GPS Patch COMPLETE")
    logger.info(f"  HEN_S_006 GPS upgraded: LOW → HIGH (ODNR GIS parcel)")
    logger.info(f"  Newly normalized: {len(newly_normalized)}")
    for n in newly_normalized:
        logger.info(f"    {n['entity_id']} — {n['name']} ({n['gps_lat']}, {n['gps_lon']})")
    logger.info(f"  Remaining held: {len(remaining_held)}")
    for h in remaining_held:
        logger.info(f"    {h['record_id']} — {h['name']} ({h['hold_reason']})")
    logger.info(f"  Total normalized: {len(norm_entities)}")

if __name__ == "__main__":
    main()
