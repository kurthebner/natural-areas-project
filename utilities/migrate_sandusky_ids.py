"""
migrate_sandusky_ids.py
Migrate all Sandusky entity IDs from SAN-* to OH-SAN-* format.
IMP-107 established OH-{COUNTY}-{TYPE}-{SEQ} as the canonical format, but the
Sandusky pipeline ran before migration was applied to its scripts.
"""

import sqlite3
import csv
import io
import pathlib
import sys

# IMP-128: Windows console UTF-8 fix — prevents UnicodeEncodeError on → and em dashes
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PROJECT_ROOT = pathlib.Path(__file__).parent.parent
DB_PATH = PROJECT_ROOT / "NASqlite" / "natural_areas_v5.db"
SITES_TSV = PROJECT_ROOT / "County_Spreadsheets" / "Sandusky" / "sandusky_sites.tsv"
APS_TSV = PROJECT_ROOT / "County_Spreadsheets" / "Sandusky" / "sandusky_access_points.tsv"

# Table/column pairs to migrate — order chosen so FKs update after PKs
DB_TARGETS = [
    # Primary keys first
    ("sites",               "site_id"),
    ("access_points",       "access_point_id"),
    ("trails",              "trail_id"),
    # FK columns in primary tables
    ("sites",               "parent_site_id"),
    ("access_points",       "parent_entity_id"),
    # Relationship tables
    ("site_parent",         "site_id"),
    ("site_parent",         "parent_site_id"),
    ("trail_parents",       "trail_id"),
    ("trail_parents",       "parent_site_id"),
    ("access_point_parents","access_point_id"),
    ("access_point_parents","parent_entity_id"),
    # Operational
    ("held_entities",       "record_id"),
]


def count_san(cur, table, col):
    cur.execute(f"SELECT COUNT(*) FROM {table} WHERE {col} LIKE 'SAN-%'")
    return cur.fetchone()[0]


def migrate_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    print("=== DB Migration: SAN-* to OH-SAN-* ===\n")
    before = {}
    for table, col in DB_TARGETS:
        before[(table, col)] = count_san(cur, table, col)

    try:
        for table, col in DB_TARGETS:
            n = before[(table, col)]
            if n == 0:
                continue
            cur.execute(
                f"UPDATE {table} SET {col} = 'OH-' || {col} WHERE {col} LIKE 'SAN-%'"
            )
            after = count_san(cur, table, col)
            print(f"  {table}.{col}: {n} updated, {after} SAN-* remaining")
        conn.commit()
        print("\nDB transaction committed.")
    except Exception as e:
        conn.rollback()
        print(f"\nERROR — rolled back: {e}", file=sys.stderr)
        conn.close()
        sys.exit(1)

    conn.close()


def migrate_tsv(path, col_name):
    text = path.read_text(encoding="utf-8")
    reader = csv.DictReader(io.StringIO(text), delimiter="\t")
    rows = list(reader)
    fieldnames = reader.fieldnames

    changed = 0
    for row in rows:
        val = row.get(col_name, "")
        if val.startswith("SAN-"):
            row[col_name] = "OH-" + val
            changed += 1

    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(out.getvalue(), encoding="utf-8")
    print(f"  {path.name}.{col_name}: {changed} updated")


def verify_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    print("\n=== Verification ===")
    checks = [
        ("sites",         "site_id",         0,  "OH-SAN-%", 94),
        ("held_entities", "record_id",        0,  "OH-SAN-%", 55),
        ("access_points", "access_point_id",  0,  "OH-SAN-%",  4),
        ("trails",        "trail_id",         0,  "OH-SAN-%",  1),
    ]
    all_ok = True
    for table, col, exp_san, oh_pat, exp_oh in checks:
        cur.execute(f"SELECT COUNT(*) FROM {table} WHERE {col} LIKE 'SAN-%'")
        got_san = cur.fetchone()[0]
        cur.execute(f"SELECT COUNT(*) FROM {table} WHERE {col} LIKE '{oh_pat}'")
        got_oh = cur.fetchone()[0]
        ok = got_san == exp_san and got_oh == exp_oh
        status = "OK" if ok else "FAIL"
        print(f"  [{status}] {table}.{col}: SAN-*={got_san} (exp {exp_san}), OH-SAN-*={got_oh} (exp {exp_oh})")
        if not ok:
            all_ok = False

    # Cross-reference check: every site_parent.parent_site_id should exist in sites.site_id
    cur.execute("""
        SELECT COUNT(*) FROM site_parent sp
        LEFT JOIN sites s ON sp.parent_site_id = s.site_id
        WHERE s.site_id IS NULL
    """)
    orphans = cur.fetchone()[0]
    status = "OK" if orphans == 0 else "FAIL"
    print(f"  [{status}] site_parent orphan check: {orphans} unmatched parent_site_id rows")
    if orphans:
        all_ok = False

    conn.close()
    return all_ok


if __name__ == "__main__":
    migrate_db()

    print("\n=== TSV Migration ===")
    migrate_tsv(SITES_TSV, "parent_site_id")
    migrate_tsv(APS_TSV, "parent_entity_id")

    ok = verify_db()
    print("\nMigration", "COMPLETE" if ok else "FAILED — review output above")
    sys.exit(0 if ok else 1)
