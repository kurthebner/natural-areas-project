"""
utilities/update_sandusky_config_for_gps_release.py
GPS Release Prep — Sandusky County

Two things this script does:
1. Migrates all SAN-* entity IDs to OH-SAN-* throughout sandusky_config.json
   (Special case: SAN-T-001 → OH-MC-T-0110, the NCIT resolved ID.)
2. For the 44 gps_missing held entities: adds GPS coordinates and clears HELD status
   so that _stage_normalization.py will normalize them on the next run.

Run once from project root:
  python utilities/update_sandusky_config_for_gps_release.py

After running, verify counts, then run:
  python County_Spreadsheets/Sandusky/_stage_normalization.py
  python County_Spreadsheets/Sandusky/_run_pipeline.py --confirm-review
"""

import json
import pathlib
import re
import sys

# IMP-128: Windows console UTF-8 fix — prevents UnicodeEncodeError on → and em dashes
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CFG_PATH = pathlib.Path(
    "County_Spreadsheets/Sandusky/sandusky_config.json"
)

# ---------------------------------------------------------------------------
# GPS table for the 44 gps_missing entities (keyed by OLD SAN-* IDs)
# Confidence levels: HIGH = precise source; MED = street/address geocode;
#                    LOW = road/area approximation
# ---------------------------------------------------------------------------
GPS_RELEASE = {
    # Access Points
    "SAN-AP-001": (41.40992,    -82.94858,   "MED"),   # SR 6 observation deck, manual est.
    "SAN-AP-005": (41.3670099,  -83.1518776, "HIGH"),  # Mosser Park / NCIT access

    # ODNR Wildlife
    "SAN-S-007":  (41.4490345,  -83.252608,  "HIGH"),  # Aldrich Pond WA

    # SCPD program-use reserves — road/area geocoding APPROX
    "SAN-S-015":  (41.2727011,  -83.0083963, "LOW"),   # Green Creek Township & Reserve
    "SAN-S-016":  (41.4572304,  -83.0912877, "LOW"),   # Muddy Creek Reserve
    "SAN-S-020":  (41.2724467,  -82.8980809, "LOW"),   # Shelley Wetland

    # Private/FC sites
    "SAN-S-019":  (41.3912939,  -83.2800276, "HIGH"),  # Ringneck Ridge
    "SAN-S-026":  (41.3674803,  -83.3173664, "HIGH"),  # White Star Barn & Historical Cabins
    "SAN-S-027":  (41.3755979,  -83.3018001, "HIGH"),  # Doug Haubert Wetland

    # Municipal parks
    "SAN-S-029":  (41.3121019,  -83.1302356, "HIGH"),  # Conner Park
    "SAN-S-030":  (41.3090819,  -83.1537715, "HIGH"),  # Chudzinski-Johannsen Park
    "SAN-S-032":  (41.3778773,  -83.1349355, "HIGH"),  # Sandusky Township Park
    "SAN-S-073":  (41.2657527,  -82.8572347, "HIGH"),  # Amsden Park (bellevuerec.com)
    "SAN-S-074":  (41.2657239,  -82.8469607, "HIGH"),  # Buckingham Park
    "SAN-S-078":  (41.2795082,  -82.8459942, "HIGH"),  # Robert Peters Athletic Field
    "SAN-S-087":  (41.3007012,  -82.9801118, "HIGH"),  # Paden Park
    "SAN-S-090":  (41.3832823,  -83.3228757, "HIGH"),  # Central Park (Woodville)
    "SAN-S-094":  (41.4490322,  -83.3595781, "HIGH"),  # H.W. Busdiecker Park
    "SAN-S-096":  (41.451426,   -83.362528,  "HIGH"),  # Veterans Park

    # Golf courses
    "SAN-S-099":  (41.3427842,  -83.185926,  "HIGH"),  # Sycamore Hills Golf Club
    "SAN-S-102":  (41.4794468,  -83.3971739, "HIGH"),  # Hidden Hills Golf Club

    # Cemeteries — precise (GeoNames / Nominatim / address)
    "SAN-S-034":  (41.28893,    -83.25443,   "HIGH"),  # Smith Cemetery (GeoNames 5172269)
    "SAN-S-036":  (41.41046,    -83.09477,   "HIGH"),  # Briar Hill Cemetery (GeoNames 5148206)
    "SAN-S-037":  (41.4287128,  -83.1058393, "HIGH"),  # Greenwood Cemetery (Nominatim)
    "SAN-S-038":  (41.4335923,  -83.1739964, "HIGH"),  # Hineline Cemetery (Nominatim)
    "SAN-S-041":  (41.3491876,  -83.0169166, "HIGH"),  # Beeler Cemetery (Nominatim)
    "SAN-S-044":  (41.4048813,  -83.0212801, "HIGH"),  # Green Creek Burial Ground
    "SAN-S-046":  (41.3654574,  -83.175762,  "HIGH"),  # Four Mile House Cemetery (address)
    "SAN-S-047":  (41.3531925,  -83.1736943, "MED"),   # Slates Cemetery (address)
    "SAN-S-048":  (41.3252637,  -83.4169581, "HIGH"),  # Chestnut Grove Cemetery (Nominatim)
    "SAN-S-055":  (41.4633939,  -83.3620929, "HIGH"),  # Woodville Cemetery (Nominatim)
    "SAN-S-061":  (41.32073,    -82.84998,   "HIGH"),  # Wickwyre Cemetery (GeoNames 5176772)
    "SAN-S-109":  (41.3411305,  -83.1217771, "HIGH"),  # Old Fremont Cemetery (Nominatim)
    "SAN-S-112":  (41.3307777,  -83.1302880, "HIGH"),  # Saint Ann's Cemetery (Nominatim)
    "SAN-S-113":  (41.3333868,  -83.1299223, "HIGH"),  # Saint Joseph's Cemetery (Nominatim)
    "SAN-S-115":  (41.3060134,  -82.9806959, "HIGH"),  # Saint Mary's Cemetery (Nominatim)
    "SAN-S-116":  (41.4324329,  -83.1731984, "HIGH"),  # Saint Paul's Cemetery (Nominatim)

    # Cemeteries — approximate (road/intersection calculation)
    "SAN-S-039":  (41.413,      -83.098,     "LOW"),   # LaPrairie Cemetery (SR53+CR129)
    "SAN-S-040":  (41.403,      -83.174,     "LOW"),   # Faith Lutheran Cemetery (CR128)
    "SAN-S-049":  (41.34,       -82.90,      "LOW"),   # Parkhurst Cemetery (SR101 area)
    "SAN-S-056":  (41.453,      -83.326,     "LOW"),   # Sugar Creek Cemetery (US20 E of Woodville)
    "SAN-S-062":  (41.2926942,  -83.0131206, "LOW"),   # Green Creek Twp Cemetery UNCONFIRMED

    # Trails
    "SAN-T-003":  (41.3674803,  -83.3173664, "HIGH"),  # Waggoner's Run MTB Trail
    "SAN-T-004":  (41.3958358,  -83.3379287, "HIGH"),  # Silver Rock Park Walking Trail
}

CONF_MAP = {"HIGH": "geocoded_research", "MED": "geocoded_nominatim", "LOW": "fallback_low"}

# ---------------------------------------------------------------------------
# ID migration table  (SAN-* → OH-SAN-*; special case NCIT)
# We handle this by a general rule: prepend "OH-" to anything starting "SAN-"
# except SAN-T-001 which resolves to the multi-county ID OH-MC-T-0110.
# ---------------------------------------------------------------------------
NCIT_PROVISIONAL = "SAN-T-001"
NCIT_FINAL       = "OH-MC-T-0110"

def migrate_id(old_id: str) -> str:
    if not old_id:
        return old_id
    if old_id == NCIT_PROVISIONAL:
        return NCIT_FINAL
    if old_id.startswith("SAN-"):
        return "OH-" + old_id
    return old_id   # already migrated or not Sandusky


def migrate_ids_in_dict(d: dict) -> dict:
    """Walk all string values in a dict and apply migrate_id to SAN-* tokens."""
    result = {}
    for k, v in d.items():
        if isinstance(v, str):
            # Migrate any SAN-* token that appears as the entire value
            result[k] = migrate_id(v) if v.startswith("SAN-") else v
        elif isinstance(v, list):
            result[k] = [migrate_id(x) if isinstance(x, str) and x.startswith("SAN-") else x for x in v]
        elif isinstance(v, dict):
            result[k] = migrate_ids_in_dict(v)
        else:
            result[k] = v
    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=== Sandusky Config GPS Release & ID Migration ===\n")

    cfg = json.loads(CFG_PATH.read_text(encoding="utf-8"))

    # ── 1. Migrate entity-level IDs and parent references in all lists ─────────
    id_fields = {
        "sites":         "site_id",
        "trails":        "trail_id",
        "access_points": "access_point_id",
    }
    parent_fields = ["parent_site_id", "parent_entity_id"]

    for list_key, id_field in id_fields.items():
        for ent in cfg.get(list_key, []):
            old_id = ent.get(id_field, "")
            new_id = migrate_id(old_id)
            if new_id != old_id:
                ent[id_field] = new_id
            for pf in parent_fields:
                if ent.get(pf):
                    ent[pf] = migrate_id(ent[pf])

    # ── 2. Migrate fallback_gps keys ──────────────────────────────────────────
    old_fps = cfg.get("fallback_gps", {})
    cfg["fallback_gps"] = {migrate_id(k): v for k, v in old_fps.items()}

    # ── 3. Add GPS for the 44 gps_missing entities + clear HELD ───────────────
    released = 0
    for list_key, id_field in id_fields.items():
        for ent in cfg.get(list_key, []):
            eid_new = ent.get(id_field, "")
            # Map back to old SAN-* key to look up in GPS_RELEASE
            old_key = eid_new.replace("OH-SAN-", "SAN-", 1).replace(NCIT_FINAL, NCIT_PROVISIONAL, 1)
            if old_key not in GPS_RELEASE:
                continue
            lat, lon, conf = GPS_RELEASE[old_key]
            # Add GPS to entity record
            ent["gps_lat"]        = lat
            ent["gps_lon"]        = lon
            ent["gps_confidence"] = CONF_MAP[conf]
            # Add to fallback_gps (for IMP-031 fill-forward on future re-runs)
            cfg["fallback_gps"][eid_new] = [lat, lon]
            # Clear HELD status
            ent["status_flag"] = ""
            ent["hold_detail"] = ""
            released += 1
            print(f"  Released {eid_new}: GPS={lat}, {lon} [{conf}]")

    print(f"\nTotal released: {released}")

    # ── 4. Write config back ───────────────────────────────────────────────────
    CFG_PATH.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nConfig written: {CFG_PATH}")

    # ── 5. Sanity check ────────────────────────────────────────────────────────
    cfg2 = json.loads(CFG_PATH.read_text(encoding="utf-8"))
    held = sum(
        1 for lst in [cfg2.get("sites", []), cfg2.get("trails", []), cfg2.get("access_points", [])]
        for e in lst
        if (e.get("status_flag") or "").startswith("HELD")
    )
    active = sum(
        len(cfg2.get(k, [])) for k in ["sites", "trails", "access_points"]
    ) - held

    # Check no SAN-* IDs remain (except in notes/comments)
    san_ids = []
    for list_key, id_field in id_fields.items():
        for ent in cfg2.get(list_key, []):
            if (ent.get(id_field) or "").startswith("SAN-"):
                san_ids.append(ent[id_field])

    print(f"\nPost-update counts:")
    print(f"  Active: {active}  |  Still held: {held}")
    print(f"  SAN-* IDs remaining in entity records: {len(san_ids)}")
    if san_ids:
        print(f"  WARNING: {san_ids[:10]}")
    else:
        print("  OK — all entity IDs migrated to OH-* format.")

    # Check a few key IDs
    ncit = next((t for t in cfg2.get("trails", []) if t.get("trail_id") == NCIT_FINAL), None)
    print(f"  NCIT (OH-MC-T-0110) found in trails: {ncit is not None}")


if __name__ == "__main__":
    main()
