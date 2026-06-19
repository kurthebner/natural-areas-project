#!/usr/bin/env python3
"""
Natural Areas Project v5 — DB Key Migration
Converts all entity IDs to OH-{COUNTY}-{TYPE}-{SEQ} format.
  - Multi-county entities → OH-MC-{TYPE}-{SEQ}
  - Single-county entities → OH-{ABBREV}-{TYPE}-{SEQ}
  - Fixes wrong-county prefixes
  - Deletes Category 2 duplicate trail records
  - Reassigns sequences for Category 1 collisions
  - Fixes "Lucas, Ohio" → "Lucas" in counties fields
  - Updates all TSV files
"""

import sqlite3, re, shutil, json, csv
from pathlib import Path
from collections import defaultdict

DB_PATH  = "/sessions/busy-nifty-ride/mnt/Natural Areas Project v5/NASqlite/natural_areas_v5.db"
BACKUP   = DB_PATH.replace(".db", "_pre_keyfix_backup.db")
TSV_ROOT = Path("/sessions/busy-nifty-ride/mnt/Natural Areas Project v5/County_Spreadsheets")

COUNTY_TO_ABBREV = {
    "Franklin":"FR","Scioto":"SC","Putnam":"PUT","Defiance":"DEF","Fulton":"FUL",
    "Henry":"HEN","Lucas":"LUC","Van Wert":"VNW","Wayne":"WA","Williams":"WIL",
    "Wood":"WOD","Paulding":"PAU","Delaware":"DEL","Fairfield":"FAI","Union":"UNI",
    "Pickaway":"PKW","Ottawa":"OTT","Adams":"ADA","Madison":"MAD","Holmes":"HOL",
    "Pike":"PIK","Marion":"MAR","Knox":"KNO","Licking":"LIC","Fayette":"FAY",
    "Hocking":"HOC","Logan":"LOG","Morrow":"MRW","Perry":"PER","Ross":"ROS",
    "Champaign":"CHA","Auglaize":"AUG","Allen":"ALL","Gallia":"GAL","Jackson":"JAC",
    "Lawrence":"LAW","Hamilton":"HAM","Butler":"BUT","Warren":"WRN","Montgomery":"MGY",
    "Miami":"MIA","Shelby":"SHE",
}

# Category 2: confirmed duplicates of canonical MC records → DELETE from DB and TSVs
DELETE_IDS = {
    "DEF-T-002","LUC-T-013","PAU-TR-002","WOD-TR-003",
    "HEN_T_006","LUC-T-010","WIL-TR-003",
}

# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────

def parse_counties(val):
    if not val: return []
    cleaned = re.sub(r",?\s*Ohio\b", "", str(val), flags=re.I)
    return [p.strip() for p in re.split(r"[;,]", cleaned) if p.strip()]

def extract_parts(old_id):
    """Returns (prefix, type_code, seq_str) from old entity ID."""
    old_id = old_id.strip()
    if "_" in old_id and "-" not in old_id:
        # HEN_S_001 or HEN_TS_001 style
        parts = old_id.split("_")
        prefix    = parts[0]
        seq       = parts[-1]
        type_code = "_".join(parts[1:-1])
        return prefix, type_code, seq
    else:
        # FR-S-0001 or FR-TS-001 or MC-T-0001 style
        parts = old_id.split("-")
        prefix    = parts[0]
        seq       = parts[-1]
        type_code = "-".join(parts[1:-1])
        return prefix, type_code, seq

def make_new_id(county, type_code, seq_str):
    return f"OH-{county}-{type_code}-{seq_str}"

def priority_key(old_id, prefix):
    """Lower = higher priority when resolving collisions.
    Existing MC records trump all; FR next; then others alphabetically."""
    if prefix == "MC": return 0
    if prefix == "FR": return 1
    if prefix == "SC": return 2
    return 3

# ─────────────────────────────────────────────
# STEP 0: Backup
# ─────────────────────────────────────────────
print("="*60)
print("STEP 0 — Backup")
print("="*60)
shutil.copy2(DB_PATH, BACKUP)
print(f"  Backed up to: {BACKUP}")

con = sqlite3.connect(DB_PATH)
con.row_factory = sqlite3.Row
cur = con.cursor()
cur.execute("PRAGMA foreign_keys = OFF")
con.commit()

# ─────────────────────────────────────────────
# STEP 1: Load all entity IDs with their counties
# ─────────────────────────────────────────────
print("\n" + "="*60)
print("STEP 1 — Loading entity IDs")
print("="*60)

ENTITY_TABLES = [
    ("sites",          "site_id",          "counties"),
    ("trails",         "trail_id",          "counties"),
    ("trail_segments", "segment_id",        "counties"),
    ("trail_networks", "network_id",        "counties"),
    ("site_networks",  "network_id",        "counties"),
    ("access_points",  "access_point_id",   "county"),   # singular
]

# { old_id: {"table":..., "pk_col":..., "counties_col":...,
#             "counties_val":..., "name":..., "prefix":...,
#             "type_code":..., "seq_str":..., "new_county":...,
#             "tentative_new_id":...} }
entities = {}
deleted_names = {}  # track names of deleted Category 2 entities for logging

for table, pk_col, counties_col in ENTITY_TABLES:
    cur.execute(f"SELECT {pk_col}, name, {counties_col} FROM {table}")
    for row in cur.fetchall():
        eid, name, counties_val = row[0], row[1], row[2]
        if eid in DELETE_IDS:
            deleted_names[eid] = name
            continue  # will delete separately
        prefix, type_code, seq_str = extract_parts(eid)
        # Determine new county prefix
        county_list = parse_counties(counties_val)
        if len(county_list) > 1:
            new_county = "MC"
        elif len(county_list) == 1:
            c = county_list[0]
            new_county = COUNTY_TO_ABBREV.get(c, prefix)  # fallback to existing prefix
        else:
            new_county = prefix  # no county info — keep prefix
        tentative = make_new_id(new_county, type_code, seq_str)
        entities[eid] = {
            "table": table, "pk_col": pk_col, "counties_col": counties_col,
            "counties_val": counties_val, "name": name,
            "prefix": prefix, "type_code": type_code, "seq_str": seq_str,
            "new_county": new_county, "tentative_new_id": tentative,
        }

print(f"  Loaded {len(entities)} entities (excluding {len(DELETE_IDS)} Category 2 deletes)")

# ─────────────────────────────────────────────
# STEP 2: Detect collisions and build final ID map
# ─────────────────────────────────────────────
print("\n" + "="*60)
print("STEP 2 — Collision detection and ID map")
print("="*60)

# Group by tentative new ID
by_tentative = defaultdict(list)
for eid, info in entities.items():
    by_tentative[info["tentative_new_id"]].append(eid)

collisions = {tid: eids for tid, eids in by_tentative.items() if len(eids) > 1}
print(f"  Collisions found: {len(collisions)}")
for tid, eids in sorted(collisions.items()):
    print(f"    {tid}:")
    for eid in eids:
        print(f"      {eid} → {entities[eid]['name'][:55]}")

# Resolve collisions
# For each collision group: sort by priority, winner keeps the sequence,
# losers get assigned next available sequence in their (type_code) namespace within MC.

# Track max sequences already claimed in each namespace: (new_county, type_code) → set of seq_strs
claimed = defaultdict(set)
for eid, info in entities.items():
    claimed[(info["new_county"], info["type_code"])].add(info["seq_str"])

def next_seq(new_county, type_code):
    """Return next 4-digit sequence number not yet claimed in this namespace."""
    existing = claimed[(new_county, type_code)]
    # Convert all to integers
    existing_ints = set()
    for s in existing:
        try: existing_ints.add(int(s))
        except: pass
    n = 1
    while n in existing_ints:
        n += 1
    seq_str = f"{n:04d}"
    claimed[(new_county, type_code)].add(seq_str)
    return seq_str

# Build final ID map
# id_map: old_id → new_id
id_map = {}
reassignments = []

for tentative_id, eids in collisions.items():
    # Sort: priority 0 = MC (canonical), 1 = FR, 2 = SC, 3 = others
    sorted_eids = sorted(eids, key=lambda e: (priority_key(e, entities[e]["prefix"]), e))
    winner = sorted_eids[0]
    id_map[winner] = tentative_id  # winner keeps tentative ID

    for loser in sorted_eids[1:]:
        info = entities[loser]
        # Check if loser is same entity as winner (name match → should have been Category 2)
        if info["name"] == entities[winner]["name"]:
            print(f"  WARNING: {loser} has same name as {winner} — should be Category 2 delete!")
        # Assign next available sequence in the MC namespace
        new_seq = next_seq(info["new_county"], info["type_code"])
        new_id  = make_new_id(info["new_county"], info["type_code"], new_seq)
        id_map[loser] = new_id
        reassignments.append((loser, info["name"][:50], tentative_id, new_id))
        # remove old seq from claimed and add new one (already done in next_seq)
        claimed[(info["new_county"], info["type_code"])].discard(info["seq_str"])

# Add non-collision entities to id_map
for eid, info in entities.items():
    if eid not in id_map:
        id_map[eid] = info["tentative_new_id"]

print(f"\n  Final ID map: {len(id_map)} renames")
print(f"  Category 1 reassignments: {len(reassignments)}")
for old, name, tentative, new in reassignments:
    print(f"    {old} ({name}) → {tentative} (COLLISION) → reassigned to {new}")

# Verify no remaining collisions
new_id_values = list(id_map.values())
assert len(new_id_values) == len(set(new_id_values)), \
    f"Still have collisions after resolution! {len(new_id_values)} vs {len(set(new_id_values))} unique"
print("  ✓ No remaining collisions after resolution")

# ─────────────────────────────────────────────
# STEP 3: Delete Category 2 records
# ─────────────────────────────────────────────
print("\n" + "="*60)
print("STEP 3 — Delete Category 2 duplicate trails")
print("="*60)

# FK tables that reference trail_id
trail_fk_tables = [
    ("trail_parents",         "trail_id"),
    ("trail_to_segment",      "trail_id"),
    ("trail_network_members", "trail_id"),
    ("discovery_provenance",  "entity_id"),
    ("resolution_provenance", "entity_id"),
    ("normalization_provenance", "entity_id"),
    ("entity_conflicts",      "entity_id"),
    ("entity_uncertainty",    "entity_id"),
    ("held_entities",         "record_id"),
    ("manual_review_queue",   "record_id"),
]

for del_id in sorted(DELETE_IDS):
    name = deleted_names.get(del_id, "?")
    print(f"  Deleting {del_id} ({name})")
    # Delete from FK tables first
    for fk_table, fk_col in trail_fk_tables:
        cur.execute(f"DELETE FROM {fk_table} WHERE {fk_col} = ?", (del_id,))
        if cur.rowcount:
            print(f"    removed {cur.rowcount} row(s) from {fk_table}.{fk_col}")
    # Delete from trails primary
    cur.execute("DELETE FROM trails WHERE trail_id = ?", (del_id,))
    print(f"    deleted from trails ({cur.rowcount} row)")

con.commit()
print(f"  ✓ Deleted {len(DELETE_IDS)} Category 2 records")

# ─────────────────────────────────────────────
# STEP 4: Apply ID renames across all tables
# ─────────────────────────────────────────────
print("\n" + "="*60)
print("STEP 4 — Applying ID renames")
print("="*60)

# Define all (table, column) pairs that hold entity IDs
# We update in a safe order: FKs before PKs would cause constraint violations if FKs checked,
# but foreign_keys = OFF, so order within each entity type doesn't matter.
# We'll update PKs and all FK columns for each entity type.

UPDATE_SPECS = [
    # (table, column)
    # Sites
    ("sites",               "site_id"),
    ("site_parent",         "site_id"),
    ("site_parent",         "parent_site_id"),
    ("trail_parents",       "parent_site_id"),
    ("site_network_members","site_id"),
    # Trails
    ("trails",              "trail_id"),
    ("trail_parents",       "trail_id"),
    ("trail_to_segment",    "trail_id"),
    ("trail_network_members","trail_id"),
    # Trail Segments
    ("trail_segments",      "segment_id"),
    ("trail_segments",      "parent_trail_id"),
    ("trail_to_segment",    "segment_id"),
    # Trail Networks
    ("trail_networks",      "network_id"),
    ("trail_network_members","network_id"),
    # Site Networks
    ("site_networks",       "network_id"),
    ("site_network_members","network_id"),
    # Access Points
    ("access_points",       "access_point_id"),
    ("access_points",       "parent_entity_id"),
    ("access_point_parents","access_point_id"),
    ("access_point_parents","parent_entity_id"),
    # Provenance / operational tables
    ("discovery_provenance",    "entity_id"),
    ("resolution_provenance",   "entity_id"),
    ("normalization_provenance","entity_id"),
    ("entity_conflicts",        "entity_id"),
    ("entity_uncertainty",      "entity_id"),
    ("held_entities",           "record_id"),
    ("manual_review_queue",     "record_id"),
]

total_updates = 0
for table, col in UPDATE_SPECS:
    updated = 0
    for old_id, new_id in id_map.items():
        if old_id == new_id:
            continue
        cur.execute(f"UPDATE {table} SET {col} = ? WHERE {col} = ?", (new_id, old_id))
        updated += cur.rowcount
    if updated:
        print(f"  {table}.{col}: {updated} row(s) updated")
        total_updates += updated

con.commit()
print(f"  ✓ Total cell updates: {total_updates}")

# ─────────────────────────────────────────────
# STEP 5: Fix "Lucas, Ohio" county values
# ─────────────────────────────────────────────
print("\n" + "="*60)
print("STEP 5 — Fix 'Lucas, Ohio' county values")
print("="*60)

for table, pk_col, counties_col in ENTITY_TABLES:
    if counties_col == "county":
        cur.execute(f"UPDATE {table} SET {counties_col} = 'Lucas' "
                    f"WHERE {counties_col} LIKE 'Lucas, Ohio%'")
    else:
        # May have "Lucas, Ohio" embedded in a multi-county list
        cur.execute(f"SELECT {pk_col}, {counties_col} FROM {table} "
                    f"WHERE {counties_col} LIKE '%Lucas, Ohio%'")
        rows = cur.fetchall()
        for row in rows:
            eid, val = row[0], row[1]
            fixed = re.sub(r"Lucas,\s*Ohio\b", "Lucas", val, flags=re.I)
            cur.execute(f"UPDATE {table} SET {counties_col} = ? WHERE {pk_col} = ?",
                        (fixed, eid))
            print(f"  Fixed {eid}: '{val}' → '{fixed}'")

con.commit()

# General cleanup: strip ", Ohio" suffix from any remaining county values
for table, pk_col, counties_col in ENTITY_TABLES:
    cur.execute(f"SELECT {pk_col}, {counties_col} FROM {table} "
                f"WHERE {counties_col} LIKE '%, Ohio%'")
    rows = cur.fetchall()
    for row in rows:
        eid, val = row[0], row[1]
        fixed = re.sub(r",\s*Ohio\b", "", val, flags=re.I).strip()
        cur.execute(f"UPDATE {table} SET {counties_col} = ? WHERE {pk_col} = ?",
                    (fixed, eid))
        print(f"  Fixed {eid}: '{val}' → '{fixed}'")

con.commit()
print("  ✓ County value cleanup done")

# ─────────────────────────────────────────────
# STEP 6: Update TSV files
# ─────────────────────────────────────────────
print("\n" + "="*60)
print("STEP 6 — Update TSV files")
print("="*60)

# Build a set of IDs to delete from TSVs (Category 2)
tsv_updated = 0
tsv_skipped = 0

# TSV column heuristic: any cell value that exists in id_map (as old key) gets remapped.
# Any cell value in DELETE_IDS gets the row deleted.

def update_tsv(tsv_path):
    global tsv_updated, tsv_skipped
    path = Path(tsv_path)
    if not path.exists():
        return
    try:
        with open(path, "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f, delimiter="\t")
            rows = list(reader)
    except Exception as e:
        print(f"  ERROR reading {path.name}: {e}")
        return

    if not rows:
        return

    new_rows = []
    file_changed = False
    deleted_rows = 0
    updated_cells = 0

    for i, row in enumerate(rows):
        if i == 0:
            new_rows.append(row)
            continue
        # Check if any cell in this row is a DELETE_ID (would be the entity's own ID)
        should_delete = any(cell.strip() in DELETE_IDS for cell in row)
        if should_delete:
            deleted_rows += 1
            file_changed = True
            continue
        # Remap any cells that are in id_map
        new_row = []
        for cell in row:
            cell_stripped = cell.strip()
            if cell_stripped in id_map and id_map[cell_stripped] != cell_stripped:
                new_row.append(id_map[cell_stripped])
                updated_cells += 1
                file_changed = True
            elif ";" in cell_stripped:
                # Could be semicolon-separated ID list (e.g. member_trail_ids)
                parts = [p.strip() for p in cell_stripped.split(";")]
                new_parts = []
                changed = False
                for p in parts:
                    if p in id_map and id_map[p] != p:
                        new_parts.append(id_map[p])
                        changed = True
                    elif p in DELETE_IDS:
                        # Remove deleted ID from list
                        changed = True
                    else:
                        new_parts.append(p)
                if changed:
                    new_row.append("; ".join(new_parts))
                    updated_cells += 1
                    file_changed = True
                else:
                    new_row.append(cell)
            else:
                new_row.append(cell)
        new_rows.append(new_row)

    if file_changed:
        with open(path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter="\t")
            writer.writerows(new_rows)
        print(f"  Updated {path.parent.name}/{path.name}: "
              f"{updated_cells} cells remapped, {deleted_rows} rows deleted")
        tsv_updated += 1
    else:
        tsv_skipped += 1

# Walk all TSV files under TSV_ROOT
for tsv_path in sorted(TSV_ROOT.rglob("*.tsv")):
    update_tsv(tsv_path)

print(f"  ✓ TSV files updated: {tsv_updated}, unchanged: {tsv_skipped}")

# ─────────────────────────────────────────────
# STEP 7: Verification
# ─────────────────────────────────────────────
print("\n" + "="*60)
print("STEP 7 — Verification")
print("="*60)

con2 = sqlite3.connect(DB_PATH)
cur2 = con2.cursor()

# Check no old-format IDs remain (anything NOT starting with OH-)
issues = 0
for table, pk_col, _ in ENTITY_TABLES:
    cur2.execute(f"SELECT {pk_col} FROM {table} WHERE {pk_col} NOT LIKE 'OH-%'")
    rows = cur2.fetchall()
    if rows:
        print(f"  WARN: {table} still has {len(rows)} non-OH- IDs: "
              f"{[r[0] for r in rows[:5]]}")
        issues += 1

# Check Category 2 IDs are gone
for del_id in DELETE_IDS:
    cur2.execute("SELECT COUNT(*) FROM trails WHERE trail_id = ?", (del_id,))
    if cur2.fetchone()[0] > 0:
        print(f"  ERROR: {del_id} still exists in trails!")
        issues += 1

# Check canonical MC records exist with new IDs
for old, new in [("MC-T-0001","OH-MC-T-0001"),("MC-T-0002","OH-MC-T-0002")]:
    cur2.execute("SELECT name FROM trails WHERE trail_id = ?", (new,))
    row = cur2.fetchone()
    if row:
        print(f"  ✓ Canonical {new} = {row[0]}")
    else:
        print(f"  ERROR: Canonical {new} not found!")
        issues += 1

# Entity counts
for table, pk_col, _ in ENTITY_TABLES:
    cur2.execute(f"SELECT COUNT(*) FROM {table}")
    count = cur2.fetchone()[0]
    print(f"  {table}: {count} records")

# Sample spot-check
print("\n  Spot-check sample IDs:")
cur2.execute("SELECT site_id, name FROM sites WHERE site_id LIKE 'OH-FR-S%' ORDER BY site_id LIMIT 5")
for r in cur2.fetchall():
    print(f"    {r[0]} | {r[1][:50]}")

cur2.execute("SELECT trail_id, name FROM trails WHERE trail_id LIKE 'OH-MC-T%' ORDER BY trail_id")
for r in cur2.fetchall():
    print(f"    {r[0]} | {r[1][:50]}")

con2.close()

if issues == 0:
    print("\n  ✓ All verification checks passed")
else:
    print(f"\n  ✗ {issues} verification issue(s) — review output above")

# Save the final ID map for reference
id_map_path = "/sessions/busy-nifty-ride/mnt/outputs/id_map.json"
with open(id_map_path, "w") as f:
    json.dump({"renames": id_map, "deleted": list(DELETE_IDS)}, f, indent=2)
print(f"\n  ID map saved to: {id_map_path}")
print("\nMigration complete.")
