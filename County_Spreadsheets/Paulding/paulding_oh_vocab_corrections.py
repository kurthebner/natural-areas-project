#!/usr/bin/env python3
"""
paulding_oh_vocab_corrections.py
Applies controlled-vocabulary corrections to Paulding County entities
after post-pipeline vocabulary audit (2026-04-08).

VIOLATIONS FOUND AND CORRECTED:
────────────────────────────────────────────────────────────────────

SITES — Subtype
  PAU-S-012  subtype "Sports Park" → "Sports Complex"
             (Sports Park is a Park subtype; valid RecFac subtypes:
              Sports Complex, Athletic Field, Skate Park, etc.)

SITES — Designation
  PAU-S-002  "Ohio State Nature Preserve" → "State Nature Preserve"
             (Designation vocab lists exactly "State Nature Preserve")

SITES — Features  (many: invalid terms, wrong spellings, wrong names)
  PAU-S-002  Old-Growth Trees→Old-Growth Stand; Wildlife Habitat→removed;
             Restricted Access→removed; Floodplain/Upland Forest ✓
  PAU-S-003  Historic Site→Historic Canal Segment; Historical Marker→Historic Marker;
             Trailhead→removed (not a site feature); Footbridge→Bridge; Hiking→Hiking Trail
  PAU-S-004  River Access→Watercraft Access; Kayak/Canoe Launch→merged into Watercraft Access;
             Fishing→Fishing Area; Water Trail Access→merged
  PAU-S-005  River Access→Watercraft Access; Floating Dock→Boat Dock;
             Fishing→Fishing Area; Restrooms (Portable)→Restrooms
  PAU-S-006  Primitive Camping→Camping; Hiking→Hiking Trail; Creek Access→removed
  PAU-S-007  River Access→Watercraft Access; Wildlife Viewing→Wildlife Observation Area;
             Historic Site→Historic Marker
  PAU-S-008  River Access→Watercraft Access; Fishing→Fishing Area; Historic Site→removed
             (redundant); Historical Marker→Historic Marker; Seating→removed
  PAU-S-010  Woodland→removed; Boat Launch→Watercraft Access; Hiking→Hiking Trail;
             Historic Site→Dam (Sugar Beet dam site); Parking→Parking Lot; Programming→removed
  PAU-S-011  Veterans Memorial→Monument; Picnic Pavilion→Pavilion;
             Pavilion (Reservable)→Pavilion (deduped); BBQ Grill→Grill;
             Kayak/Canoe Launch→Watercraft Access; Hiking→Hiking Trail;
             Fishing→Fishing Area; Splash Pad→Spray Park; Old-Growth Trees→Old-Growth Stand
  PAU-S-012  Concession Stand→removed; Accessible→ADA Accessible;
             Baseball/Softball→removed (use type ≠ feature); Lighting→removed
  PAU-S-014  Water Slide→Waterslide; Water Play Area→Spray Park; Seating→removed
  PAU-S-016  Reservoir→removed (not in Features vocab)
  PAU-S-017  Fishing Pond→Pond; Fishing Area; Walking Path→Hiking Trail;
             Pavilion (Reservable)→Pavilion
  PAU-S-018  Sports Field→Athletic Field
  PAU-S-020  Floodplain Restoration→Habitat Restoration Area; Native Plantings→removed;
             River Access→Watercraft Access; Parking→Parking Lot
  PAU-S-022  Woodland→removed; Wildlife Habitat→removed;
             Hunting→Hunting Area; Fee Access→removed

TRAILS — Use Type
  PAU-TR-001  "Hiking; Walking" → "Hiking"
              ("Walking" not in vocabulary; maps to Hiking)
  PAU-TR-002  "Water Trail; Canoeing; Kayaking" → "Water"
              (only valid water use type is "Water")

TRAILS — Surface Type
  PAU-TR-001  "Natural Surface; Gravel; Crushed Limestone" → "Mixed"
              (multiple documented surfaces → Mixed; "Crushed Limestone" → "Crushed Stone")
  PAU-TR-003  "Gravel; Natural Surface; Paved" → "Mixed"
  PAU-TR-004  "Gravel; Natural Surface; Paved" → "Mixed"

TRAILS — Origin Type
  PAU-TR-001  "Historic Canal Towpath" → "Canal Towpath"
  PAU-TR-002  "Scenic River Water Trail" → "Other"
              (no valid origin type for a designated river water route)
  PAU-TR-003  "Historic Canal Towpath" → "Canal Towpath"
  PAU-TR-004  "Historic Canal Towpath" → "Canal Towpath"

────────────────────────────────────────────────────────────────────
"""

import sqlite3
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
DB_PATH = os.path.join(PROJECT_ROOT, "NASqlite", "natural_areas_v5.db")
OUTPUT_DIR = SCRIPT_DIR

# ── Corrected features by site_id ────────────────────────────────────────────
SITE_CORRECTIONS = {
    "PAU-S-002": {
        "designation": "State Nature Preserve",
        "features": "Old-Growth Stand; Floodplain Forest; Upland Forest",
    },
    "PAU-S-003": {
        "features": "Historic Canal Segment; Historic Marker; Bridge; Hiking Trail",
    },
    "PAU-S-004": {
        "features": "Watercraft Access; Fishing Area; Picnic Area",
    },
    "PAU-S-005": {
        "features": "Watercraft Access; Historic Bridge; Boat Ramp; Boat Dock; Fishing Area; Picnic Area; Fire Ring; Restrooms",
    },
    "PAU-S-006": {
        "features": "Camping; Fire Ring; Hiking Trail",
    },
    "PAU-S-007": {
        "features": "Watercraft Access; Wildlife Observation Area; Historic Marker; Picnic Area",
    },
    "PAU-S-008": {
        "features": "Watercraft Access; Fishing Area; Historic Marker",
    },
    "PAU-S-010": {
        "features": "Wetland; Meadow; Watercraft Access; Hiking Trail; Pond; Dam; Nature Center; Picnic Area; Parking Lot",
    },
    "PAU-S-011": {
        "features": "Monument; Playground; Pavilion; Grill; Watercraft Access; Hiking Trail; Fishing Area; Restrooms; Spray Park; Old-Growth Stand",
    },
    "PAU-S-012": {
        "subtype": "Sports Complex",
        "features": "Ball Diamond; ADA Accessible; Restrooms",
    },
    "PAU-S-013": {
        # features already "Playground" — valid, no change
    },
    "PAU-S-014": {
        "features": "Swimming Pool; Waterslide; Spray Park",
    },
    "PAU-S-016": {
        "features": "",   # Reservoir not in Features vocab
    },
    "PAU-S-017": {
        "features": "Pond; Fishing Area; Hiking Trail; Playground; Pavilion",
    },
    "PAU-S-018": {
        "features": "Playground; Athletic Field; Picnic Area",
    },
    "PAU-S-020": {
        "features": "Habitat Restoration Area; Wetland Restoration; Watercraft Access; Parking Lot",
    },
    "PAU-S-022": {
        "features": "Wetland; Hunting Area",
    },
}

# ── Corrected trail fields ────────────────────────────────────────────────────
TRAIL_CORRECTIONS = {
    "PAU-TR-001": {
        "use_type":     "Hiking",
        "surface_type": "Mixed",
        "origin_type":  "Canal Towpath",
    },
    "PAU-TR-002": {
        "use_type":     "Water",
        "surface_type": "Water",      # already correct but set explicitly
        "origin_type":  "Other",
    },
    "PAU-TR-003": {
        "surface_type": "Mixed",
        "origin_type":  "Canal Towpath",
    },
    "PAU-TR-004": {
        "surface_type": "Mixed",
        "origin_type":  "Canal Towpath",
    },
}


def apply_corrections(db_path):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    print("── Applying site corrections ──")
    for site_id, fields in SITE_CORRECTIONS.items():
        if not fields:
            continue
        for col, val in fields.items():
            cur.execute(
                f"UPDATE sites SET {col} = ? WHERE site_id = ?",
                (val, site_id)
            )
            if cur.rowcount:
                print(f"  {site_id}.{col} updated")
            else:
                print(f"  WARNING: {site_id} not found in sites table")

    print("\n── Applying trail corrections ──")
    for trail_id, fields in TRAIL_CORRECTIONS.items():
        for col, val in fields.items():
            cur.execute(
                f"UPDATE trails SET {col} = ? WHERE trail_id = ?",
                (val, trail_id)
            )
            if cur.rowcount:
                print(f"  {trail_id}.{col} updated")
            else:
                print(f"  WARNING: {trail_id} not found in trails table")

    con.commit()
    con.close()
    print("\n  DB corrections committed.")


def regenerate_tsvs(db_path, output_dir):
    """Pull corrected data from DB and rewrite TSV files."""
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def write_tsv(path, headers, rows):
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write("\t".join(headers) + "\n")
            for row in rows:
                line = "\t".join(
                    "" if v is None else str(v).strip().replace("\t", " ").replace("\n", " ")
                    for v in row
                )
                f.write(line + "\n")
        print(f"  Written: {path} ({len(rows)} rows)")

    # Sites TSV (25 fields)
    cur.execute("""
        SELECT name, category, subtype, designation, status,
               ownership, governance, partner_agencies, coordination,
               description, location, acres, counties,
               municipality, township, gps_lat, gps_lon, plus_code,
               features, notes, url_primary, urls, parent_site_id,
               created_at, updated_at
        FROM sites WHERE counties = 'Paulding'
        ORDER BY site_id
    """)
    sites_rows = [tuple(r) for r in cur.fetchall()]
    write_tsv(
        os.path.join(output_dir, "paulding_oh_sites.tsv"),
        ["name","category","subtype","designation","status",
         "ownership","governance","partner_agencies","coordination",
         "description","location","acres","counties",
         "municipality","township","gps_lat","gps_lon","plus_code",
         "features","notes","url_primary","urls","parent_site_id",
         "created_at","updated_at"],
        sites_rows
    )

    # Trails TSV (19 fields)
    cur.execute("""
        SELECT name, alternate_names, use_type, surface_type, origin_type,
               length_mi, counties, governance, partner_agencies, status,
               difficulty, accessibility, description, trail_history,
               identity_notes, notes, url_primary, maps, trail_id
        FROM trails WHERE trail_id LIKE 'PAU-%'
        ORDER BY trail_id
    """)
    trails_rows = [tuple(r) for r in cur.fetchall()]
    write_tsv(
        os.path.join(output_dir, "paulding_oh_trails.tsv"),
        ["Trail Name","Alternate Names","Trail Use Type","Trail Surface Type",
         "Trail Origin Type","Total Length (Miles)","Counties","Governance",
         "Partner Agencies","Status","Difficulty","Accessibility",
         "Description","Trail History","Identity Notes","Notes",
         "URL","Maps","Trail ID"],
        trails_rows
    )

    # Trail Networks TSV (17 fields) — unchanged but rewrite for consistency
    cur.execute("""
        SELECT name, network_type, status, ownership, governance,
               partner_agencies, counties, states_included, length_mi,
               member_trail_count, member_trail_ids, description,
               identity_notes, notes, url_primary, maps, network_id
        FROM trail_networks WHERE network_id LIKE 'PAU-%'
        ORDER BY network_id
    """)
    tn_rows = [tuple(r) for r in cur.fetchall()]
    write_tsv(
        os.path.join(output_dir, "paulding_oh_trail_networks.tsv"),
        ["Network Name","Network Type","Status","Ownership","Governance",
         "Partner Agencies","Counties","States Included","Total Length (Miles)",
         "Member Trail Count","Member Trail IDs","Description",
         "Identity Notes","Notes","URL","Maps","Network ID"],
        tn_rows
    )

    # Access Points TSV (17 fields) — unchanged but rewrite
    cur.execute("""
        SELECT name, ap_type, status, parent_entity_type,
               parent_entity_id,
               county, township, municipality, address,
               gps_lat, gps_lon, plus_code, features,
               identity_notes, notes, url_primary, access_point_id
        FROM access_points WHERE access_point_id LIKE 'PAU-%'
        ORDER BY access_point_id
    """)
    ap_rows = [tuple(r) for r in cur.fetchall()]
    write_tsv(
        os.path.join(output_dir, "paulding_oh_access_points.tsv"),
        ["Access Point Name","Access Point Type","Status",
         "Identity Parent Entity Type","Identity Parent Entity Name",
         "County","Township","Municipality","Address",
         "GPS Lat","GPS Lon","Plus Code","Features",
         "Identity Notes","Notes","URL","Access Point ID"],
        ap_rows
    )

    con.close()


def tsv_integrity_check(output_dir):
    checks = [
        ("paulding_oh_sites.tsv",         24, "Sites"),
        ("paulding_oh_trails.tsv",         18, "Trails"),
        ("paulding_oh_trail_networks.tsv", 16, "Trail Networks"),
        ("paulding_oh_access_points.tsv",  16, "Access Points"),
    ]
    print("\n── TSV Integrity Check ──")
    all_ok = True
    for fname, expected_tabs, label in checks:
        path = os.path.join(output_dir, fname)
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
        errors = []
        for i, line in enumerate(lines):
            tabs = line.rstrip("\n").count("\t")
            if tabs != expected_tabs:
                errors.append(f"  Row {i+1}: {tabs} tabs (expected {expected_tabs})")
        if errors:
            all_ok = False
            print(f"  {label}: FAIL")
            for e in errors[:5]:
                print(e)
        else:
            print(f"  {label}: OK ({len(lines)-1} data rows, {expected_tabs} tabs/row)")
    return all_ok


if __name__ == "__main__":
    print("=" * 60)
    print("PAULDING COUNTY — VOCABULARY CORRECTIONS")
    print("=" * 60)
    apply_corrections(DB_PATH)
    print("\n── Regenerating TSVs from corrected DB ──")
    regenerate_tsvs(DB_PATH, OUTPUT_DIR)
    ok = tsv_integrity_check(OUTPUT_DIR)
    if ok:
        print("\n  All checks passed. Corrections complete.")
    else:
        print("\n  INTEGRITY FAILURES — review above.")
        sys.exit(1)
