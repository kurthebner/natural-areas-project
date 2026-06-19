#!/usr/bin/env python3
"""
normalize_timestamps_v1.py  —  IMP-128 one-time DB timestamp normalization

Finds all existing DB records whose created_at or updated_at values do not
match the canonical format (YYYY-MM-DDTHH:MM:SSZ) and rewrites them to
the canonical format in a single transaction.

Known non-canonical formats present in the DB before this fix:
  (a) YYYY-MM-DDTHH:MM:SS.ffffff          -- datetime.utcnow().isoformat()
                                              (no TZ, microseconds) from upsert_ottawa.py
  (b) YYYY-MM-DDTHH:MM:SS.ffffff+00:00    -- datetime.now(utc).isoformat()
                                              (UTC offset, microseconds) from old upsert scripts
  (c) YYYY-MM-DD HH:MM:SS                 -- SQLite datetime('now') from na_feature_cleanup
                                              (space separator, no timezone)

Safe: already-canonical values (YYYY-MM-DDTHH:MM:SSZ) are left untouched.
Safe: NULL values are left untouched.
Safe: Unrecognised formats are left untouched and reported.

Usage:
    python utilities/normalize_timestamps_v1.py
"""

import re
import sqlite3
import pathlib

DB_PATH = pathlib.Path(__file__).parent.parent / "NASqlite" / "natural_areas_v5.db"

# ---------------------------------------------------------------------------
# CANONICAL PATTERN  -- already-good values; nothing to do
# ---------------------------------------------------------------------------
CANONICAL_RE = re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$')

# ---------------------------------------------------------------------------
# NORMALISATION  -- extract date+time, drop microseconds, reassemble with Z
# ---------------------------------------------------------------------------
# Matches any of:
#   2026-05-18T14:03:36.957114+00:00
#   2026-05-18T14:03:36.957114
#   2026-05-18T14:03:36+00:00
#   2026-05-18T14:03:36
#   2026-05-18 14:03:36.957114
#   2026-05-18 14:03:36
_PARSE_RE = re.compile(
    r'^(\d{4}-\d{2}-\d{2})[T ](\d{2}:\d{2}:\d{2})(?:\.\d+)?(?:Z|\+00:\d{2})?$'
)

# Date-only format (e.g. from Henry County upsert) -- normalise to T00:00:00Z
_DATE_ONLY_RE = re.compile(r'^(\d{4}-\d{2}-\d{2})$')

def normalize_ts(ts: str):
    """Return canonical timestamp string, or None if already canonical / NULL.
    Returns False if format is unrecognised (caller should warn)."""
    if ts is None:
        return None
    if CANONICAL_RE.match(ts):
        return None                 # already canonical — no change needed
    m = _PARSE_RE.match(ts)
    if m:
        return f'{m.group(1)}T{m.group(2)}Z'
    m2 = _DATE_ONLY_RE.match(ts)
    if m2:
        return f'{m2.group(1)}T00:00:00Z'  # date-only → midnight UTC
    return False                    # unrecognised format


# ---------------------------------------------------------------------------
# TABLES AND COLUMNS TO CHECK
# ---------------------------------------------------------------------------
TABLES = [
    ('sites',          'site_id',          ['created_at', 'updated_at']),
    ('trails',         'trail_id',         ['created_at', 'updated_at']),
    ('trail_segments', 'segment_id',       ['created_at', 'updated_at']),
    ('trail_networks', 'network_id',       ['created_at', 'updated_at']),
    ('site_networks',  'network_id',       ['created_at', 'updated_at']),
    ('access_points',  'access_point_id',  ['created_at', 'updated_at']),
    ('held_entities',  'record_id',        ['created_at']),
    ('run_metadata',   'run_id',           ['created_at']),
]


def run():
    print(f"Database : {DB_PATH}")
    if not DB_PATH.exists():
        print("ERROR: database file not found.")
        return

    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row

    total_fixed   = 0
    total_warned  = 0
    table_summary = []

    try:
        conn.execute("BEGIN")

        for table, pk_col, ts_cols in TABLES:
            # Check the table exists
            exists = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
                (table,)
            ).fetchone()
            if not exists:
                print(f"  SKIP  {table} -- table not found")
                continue

            fixed_this_table  = 0
            warned_this_table = 0

            for col in ts_cols:
                # Check the column exists
                col_info = conn.execute(f"PRAGMA table_info({table})").fetchall()
                col_names = {r['name'] for r in col_info}
                if col not in col_names:
                    print(f"  SKIP  {table}.{col} -- column not found")
                    continue

                rows = conn.execute(
                    f"SELECT {pk_col}, {col} FROM {table} WHERE {col} IS NOT NULL"
                ).fetchall()

                for row in rows:
                    pk_val = row[pk_col]
                    orig   = row[col]
                    result = normalize_ts(orig)

                    if result is None:
                        continue                          # already canonical
                    if result is False:
                        print(f"  WARN  {table}.{col}  {pk_val!r}: unrecognised format: {orig!r}")
                        warned_this_table += 1
                        continue

                    conn.execute(
                        f"UPDATE {table} SET {col} = ? WHERE {pk_col} = ?",
                        (result, pk_val)
                    )
                    fixed_this_table += 1

            if fixed_this_table or warned_this_table:
                print(f"  {table:20s}  fixed={fixed_this_table:4d}  warned={warned_this_table}")
            else:
                print(f"  {table:20s}  (all canonical)")

            total_fixed  += fixed_this_table
            total_warned += warned_this_table
            table_summary.append((table, fixed_this_table, warned_this_table))

        conn.commit()

    except Exception as exc:
        conn.rollback()
        print(f"\nERROR — rolled back: {exc}")
        raise

    finally:
        conn.close()

    print()
    print("-" * 50)
    print(f"Total rows normalised : {total_fixed}")
    print(f"Unrecognised formats  : {total_warned}  (no changes made for these)")
    print()
    if total_warned:
        print("Review WARN lines above and handle unrecognised formats manually.")
    else:
        print("All timestamps are now in canonical format (YYYY-MM-DDTHH:MM:SSZ).")


if __name__ == '__main__':
    run()
