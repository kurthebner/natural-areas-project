"""
utilities/release_paulding_gps.py
GPS Release — Paulding County (4 held entities)

Releases:
  OH-PAU-S-001  Lake Wayne R. Carr Wildlife Area
  OH-PAU-S-009  Guilda H. Culler Memorial Park
  OH-PAU-S-021  Flat Rock Creek Nature Preserve
  OH-PAU-AP-005 Viall's Lock Campsite

GPS coordinates previously written to paulding_oh_raw_discovery.yaml by
update_gps_coordinates.py. This script:
  1. Runs GIS township/municipality lookup for all 4 GPS points
  2. Generates Plus Codes
  3. Upserts entities to DB (sites + access_points tables)
  4. Adds access_point_parents row for OH-PAU-AP-005
  5. Deletes 4 rows from held_entities
  6. Appends rows to Paulding TSVs

Run from project root:
  python utilities/release_paulding_gps.py
  python utilities/release_paulding_gps.py --dry-run
"""

import argparse
import sqlite3
import sys
import pathlib
from datetime import datetime, timezone

# IMP-128: Windows console UTF-8 fix — prevents UnicodeEncodeError on → and em dashes
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PROJECT_ROOT = pathlib.Path(__file__).parent.parent
DB_PATH      = PROJECT_ROOT / "NASqlite" / "natural_areas_v5.db"
SITES_TSV    = PROJECT_ROOT / "County_Spreadsheets/Paulding/paulding_oh_sites.tsv"
APS_TSV      = PROJECT_ROOT / "County_Spreadsheets/Paulding/paulding_oh_access_points.tsv"

sys.path.insert(0, str(PROJECT_ROOT / "utilities"))

from na_plus_code import encode_plus_code

try:
    from na_township_lookup import OhioTownshipLookup
    _LOOKUP = OhioTownshipLookup()
    _LOOKUP_AVAILABLE = True
except Exception as e:
    print(f"WARNING: OhioTownshipLookup unavailable: {e}")
    _LOOKUP = None
    _LOOKUP_AVAILABLE = False

# ---------------------------------------------------------------------------
# Normalized entity data
# GPS coordinates sourced via update_gps_coordinates.py research pass.
# ---------------------------------------------------------------------------

NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

SITES_RELEASE = [
    {
        "site_id":         "OH-PAU-S-001",
        "name":            "Lake Wayne R. Carr Wildlife Area",
        "category":        "Wildlife Area",
        "subtype":         "State Wildlife Area",
        "designation":     "State Wildlife Area",
        "status":          "Active",
        "ownership":       "State of Ohio",
        "governance":      "ODNR Division of Wildlife",
        "partner_agencies": "",
        "coordination":    "",
        "description": (
            "Lake Wayne R. Carr Wildlife Area is an ODNR Division of Wildlife managed area in "
            "Paulding County, Ohio. The area centers on a small lake (Wayne R. Carr Lake) and "
            "provides public hunting and fishing access. Watercraft permitted at idle speed only "
            "— no wake allowed on the lake. Area covers approximately 18 acres."
        ),
        "location":        "Paulding County, Ohio",
        "acres":           18.34,
        "counties":        "Paulding",
        "gps_lat":         41.1580269,
        "gps_lon":        -84.7863068,
        # GPS confidence: HIGH — 12525 Rd 11, Antwerp OH (address geocode)
        "features_raw":    "Fishing Area; Hunting Area; Watercraft Access",
        "features":        "Fishing Area; Hunting Area; Watercraft Access",
        "notes":           "Powercraft restricted to idle speed on Wayne R. Carr Lake per Ohio Admin Code Rule 1501:31-5-02.",
        "url_primary":     "https://wildlife.ohiodnr.gov/",
        "urls":            "",
        "parent_site_id":  "",
    },
    {
        "site_id":         "OH-PAU-S-009",
        "name":            "Guilda H. Culler Memorial Park",
        "category":        "Park",
        "subtype":         "Greenspace",
        "designation":     "",
        "status":          "Under Development",
        "ownership":       "Paulding County Park District",
        "governance":      "Paulding County Park District",
        "partner_agencies": "",
        "coordination":    "",
        "description": (
            "Guilda H. Culler Memorial Park is a developing Paulding County Park District park on "
            "land donated by Gary and Linda Mabis. Named in memory of Guilda H. Culler. "
            "In early development stages."
        ),
        "location":        "Paulding County, Ohio",
        "acres":           None,
        "counties":        "Paulding",
        "gps_lat":         41.2159711,
        "gps_lon":        -84.6269824,
        # GPS confidence: LOW — Crane Township centroid (no address available)
        "features_raw":    "",
        "features":        "",
        "notes":           "GPS approximate (Crane Township centroid; no address on file as of 2026-04-07). Under development.",
        "url_primary":     "https://pauldingohparks.com/",
        "urls":            "",
        "parent_site_id":  "",
    },
    {
        "site_id":         "OH-PAU-S-021",
        "name":            "Flat Rock Creek Nature Preserve",
        "category":        "Nature Preserve",
        "subtype":         "Private Nature Preserve",
        "designation":     "",
        "status":          "No Public Entry",
        "ownership":       "ACRES Land Trust",
        "governance":      "ACRES Land Trust",
        "partner_agencies": "",
        "coordination":    "",
        "description": (
            "A nature preserve owned and managed by ACRES Land Trust in Paulding County, Ohio, "
            "approximately 4 miles east of Payne. Features upland and floodplain forests along "
            "Flat Rock Creek. Closed to public access per ACRES Land Trust closed preserves list."
        ),
        "location":        "Approximately 4 miles east of Payne, Ohio, Paulding County",
        "acres":           None,
        "counties":        "Paulding",
        "gps_lat":         41.1077358,
        "gps_lon":        -84.6586975,
        # GPS confidence: HIGH — eBird hotspot L4718683
        "features_raw":    "Upland Forest; Floodplain Forest",
        "features":        "Floodplain Forest; Upland Forest",  # alphabetized
        "notes":           "CLOSED to public access (ACRES closed preserves list). No public trails or visitation.",
        "url_primary":     "https://acreslandtrust.org/closedpreserve/closed-flat-rock-creek/",
        "urls":            "",
        "parent_site_id":  "",
    },
]

AP_RELEASE = {
    "access_point_id":    "OH-PAU-AP-005",
    "name":               "Viall's Lock Campsite",
    "ap_type":            "Trailhead",
    "status":             "Active",
    "parent_entity_type": "Trail",
    "parent_entity_id":   "OH-MC-TR-003",
    "county":             "Paulding",
    "address":            "Road 163, Paulding County, Ohio",
    "gps_lat":            41.1625559,
    "gps_lon":           -84.4516157,
    # GPS confidence: LOW — Road 163 approximate (no precise location in sources)
    "features":           "Camping",
    "identity_notes": (
        "Primitive campsite on BT Delphos Section in Paulding County, off Road 163. "
        "No facilities. Co-located with NCT route (OH-PAU-TN-001). "
        "Parent: Buckeye Trail – Delphos Section (OH-MC-TR-003)."
    ),
    "notes":              "GPS approximate (Road 163 area). Originally held pending GPS acquisition.",
    "url_primary":        "https://www.buckeyetrail.org/sections/delphos",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def gis_lookup(lat, lon):
    if not _LOOKUP_AVAILABLE:
        return "", ""
    try:
        twp, mun = _LOOKUP.get_both(lat, lon)
        return twp or "", mun or ""
    except Exception as e:
        print(f"  GIS error: {e}")
        return "", ""


def clean(v):
    if v is None:
        return ""
    return str(v).replace("\t", " ").replace("\n", " ").replace("\r", " ")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Paulding GPS release — 4 held entities")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print what would happen; do not write to DB or TSVs")
    args = parser.parse_args()

    print("=== Paulding GPS Release (4 held entities) ===\n")

    # ── 1. GIS lookups + Plus Codes ───────────────────────────────────────────
    print("[1] GIS township/municipality lookup + Plus Codes")
    for s in SITES_RELEASE:
        twp, mun = gis_lookup(s["gps_lat"], s["gps_lon"])
        s["township"]    = twp
        s["municipality"] = mun
        s["plus_code"]   = encode_plus_code(s["gps_lat"], s["gps_lon"])
        print(f"  {s['site_id']:20s} twp={twp!r:20s}  mun={mun!r:20s}  plus={s['plus_code']}")

    ap = AP_RELEASE
    ap_twp, ap_mun = gis_lookup(ap["gps_lat"], ap["gps_lon"])
    ap["township"]    = ap_twp
    ap["municipality"] = ap_mun
    ap["plus_code"]   = encode_plus_code(ap["gps_lat"], ap["gps_lon"])
    print(f"  {ap['access_point_id']:20s} twp={ap_twp!r:20s}  mun={ap_mun!r:20s}  plus={ap['plus_code']}")

    if args.dry_run:
        print("\n[DRY-RUN] Would upsert 3 sites + 1 AP, clean 4 held_entities rows.")
        print("  Sites:")
        for s in SITES_RELEASE:
            print(f"    {s['site_id']} — {s['name']}  gps=({s['gps_lat']}, {s['gps_lon']})")
        print(f"  AP: {ap['access_point_id']} — {ap['name']}  gps=({ap['gps_lat']}, {ap['gps_lon']})")
        print("\nDry-run complete. No changes written.")
        return

    # ── 2. DB upsert ─────────────────────────────────────────────────────────
    print("\n[2] DB upsert")
    conn = sqlite3.connect(str(DB_PATH))
    try:
        cur = conn.cursor()

        # Sites
        site_sql = """
        INSERT OR REPLACE INTO sites
            (site_id, name, category, subtype, designation, status, ownership, governance,
             partner_agencies, coordination, description, location, acres, counties,
             municipality, township, gps_lat, gps_lon, plus_code, features, notes,
             url_primary, urls, parent_site_id, features_raw, created_at, updated_at)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """
        for s in SITES_RELEASE:
            cur.execute(site_sql, (
                s["site_id"], s["name"], s["category"], s["subtype"], s["designation"],
                s["status"], s["ownership"], s["governance"], s["partner_agencies"],
                s["coordination"], s["description"], s["location"], s["acres"],
                s["counties"], s["municipality"], s["township"],
                s["gps_lat"], s["gps_lon"], s["plus_code"],
                s["features"], s["notes"], s["url_primary"], s["urls"],
                s["parent_site_id"], s["features_raw"], NOW, NOW,
            ))
            print(f"  Upserted site: {s['site_id']} — {s['name']}")

        # Access Point
        ap_sql = """
        INSERT OR REPLACE INTO access_points
            (access_point_id, name, ap_type, status, parent_entity_type, parent_entity_id,
             county, township, municipality, address, gps_lat, gps_lon, plus_code,
             features, identity_notes, notes, url_primary, created_at, updated_at)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """
        cur.execute(ap_sql, (
            ap["access_point_id"], ap["name"], ap["ap_type"], ap["status"],
            ap["parent_entity_type"], ap["parent_entity_id"],
            ap["county"], ap["township"], ap["municipality"], ap["address"],
            ap["gps_lat"], ap["gps_lon"], ap["plus_code"],
            ap["features"], ap["identity_notes"], ap["notes"], ap["url_primary"],
            NOW, NOW,
        ))
        print(f"  Upserted AP:   {ap['access_point_id']} — {ap['name']}")

        # access_point_parents
        cur.execute("""
        INSERT OR IGNORE INTO access_point_parents
            (access_point_id, parent_entity_type, parent_entity_id)
        VALUES (?, ?, ?)
        """, (ap["access_point_id"], ap["parent_entity_type"], ap["parent_entity_id"]))
        print(f"  access_point_parents: {ap['access_point_id']} -> {ap['parent_entity_id']}")

        # Delete from held_entities
        to_release = [s["site_id"] for s in SITES_RELEASE] + [ap["access_point_id"]]
        deleted = 0
        for eid in to_release:
            cur.execute("DELETE FROM held_entities WHERE record_id = ?", (eid,))
            deleted += cur.rowcount
        print(f"  Deleted {deleted} rows from held_entities")

        conn.commit()
        print("  Committed.")

    except Exception as exc:
        conn.rollback()
        print(f"  ERROR: {exc}", file=sys.stderr)
        raise
    finally:
        conn.close()

    # ── 3. TSV updates ───────────────────────────────────────────────────────
    print("\n[3] TSV updates")

    # Sites TSV (25 cols — site_id and features_raw excluded per CLAUDE.md §7)
    # Columns: name, category, subtype, designation, status, ownership, governance,
    #          partner_agencies, coordination, description, location, acres, counties,
    #          municipality, township, gps_lat, gps_lon, plus_code, features, notes,
    #          url_primary, urls, parent_site_id, created_at, updated_at
    with open(SITES_TSV, "a", encoding="utf-8", newline="") as f:
        for s in SITES_RELEASE:
            row_fields = [
                s["name"], s["category"], s["subtype"], s["designation"], s["status"],
                s["ownership"], s["governance"], s["partner_agencies"], s["coordination"],
                s["description"], s["location"],
                "" if s["acres"] is None else str(s["acres"]),
                s["counties"], s["municipality"], s["township"],
                str(s["gps_lat"]), str(s["gps_lon"]), s["plus_code"],
                s["features"], s["notes"], s["url_primary"], s["urls"],
                s["parent_site_id"], NOW, NOW,
            ]
            f.write("\t".join(clean(v) for v in row_fields) + "\n")
    print(f"  Appended 3 rows to {SITES_TSV.name}")

    # Access Points TSV — matches existing Paulding format (17 cols):
    # Access Point Name | Access Point Type | Status | Identity Parent Entity Type |
    # Identity Parent Entity Name | County | Township | Municipality | Address |
    # GPS Lat | GPS Lon | Plus Code | Features | Identity Notes | Notes | URL |
    # Access Point ID
    with open(APS_TSV, "a", encoding="utf-8", newline="") as f:
        ap_row_fields = [
            ap["name"], ap["ap_type"], ap["status"],
            ap["parent_entity_type"],
            "Buckeye Trail – Delphos Section",   # parent name
            ap["county"], ap["township"], ap["municipality"], ap["address"],
            str(ap["gps_lat"]), str(ap["gps_lon"]), ap["plus_code"],
            ap["features"], ap["identity_notes"], ap["notes"], ap["url_primary"],
            ap["access_point_id"],
        ]
        f.write("\t".join(clean(v) for v in ap_row_fields) + "\n")
    print(f"  Appended 1 row to {APS_TSV.name}")

    # ── 4. Verification ──────────────────────────────────────────────────────
    print("\n[4] Verification")
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()
    for s in SITES_RELEASE:
        cur.execute(
            "SELECT site_id, name, gps_lat, gps_lon, township, municipality FROM sites WHERE site_id=?",
            (s["site_id"],)
        )
        row = cur.fetchone()
        print(f"  {row}")
    cur.execute(
        "SELECT access_point_id, name, gps_lat, gps_lon, township FROM access_points WHERE access_point_id=?",
        (ap["access_point_id"],)
    )
    print(f"  {cur.fetchone()}")

    cur.execute("SELECT COUNT(*) FROM held_entities WHERE county='Paulding'")
    remaining_paulding = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM held_entities")
    remaining_total = cur.fetchone()[0]
    print(f"\n  Paulding held remaining: {remaining_paulding}")
    print(f"  Total held remaining:    {remaining_total}")

    # Spot-check access_point_parents
    cur.execute(
        "SELECT * FROM access_point_parents WHERE access_point_id=?",
        (ap["access_point_id"],)
    )
    print(f"  access_point_parents row: {cur.fetchone()}")

    conn.close()

    print("\nPaulding GPS release complete.")
    print(f"  Sites released: {len(SITES_RELEASE)}")
    print(f"  APs released:   1")
    print(f"  Total released: {len(SITES_RELEASE) + 1}")


if __name__ == "__main__":
    main()
