"""
HAN-* → OH-HAN-* ID prefix fix (Hancock County)
Equivalent to the IMP-107 migration that should have caught these.
All HAN-S-*, HAN-T-*, HAN-AP-* IDs get 'OH-' prepended.

Affected columns:
  sites.site_id                        (166 rows)
  trails.trail_id                       (25 rows)
  access_points.access_point_id        (19 rows)
  access_points.parent_entity_id       (19 rows)
  normalization_provenance.entity_id   (54 rows)

Run from project root:
  python utilities/han_id_fix.py
"""
import sqlite3
import datetime
import sys

sys.stdout.reconfigure(encoding='utf-8')

DB = 'NASqlite/natural_areas_v5.db'

UPDATES = [
    # (table, column)
    ('sites',                    'site_id'),
    ('trails',                   'trail_id'),
    ('access_points',            'access_point_id'),
    ('access_points',            'parent_entity_id'),
    ('normalization_provenance', 'entity_id'),
]

conn = sqlite3.connect(DB)
cur = conn.cursor()

try:
    # Pre-flight: confirm no OH-HAN-* already exist (collision check)
    for tbl, col in [('sites','site_id'),('trails','trail_id'),('access_points','access_point_id')]:
        cur.execute(f'SELECT count(*) FROM {tbl} WHERE {col} LIKE "OH-HAN-%"')
        n = cur.fetchone()[0]
        if n:
            print(f'ERROR: {tbl}.{col} already has {n} OH-HAN-* rows — aborting to avoid collision.')
            sys.exit(1)
    print('Pre-flight OK: no existing OH-HAN-* IDs found.')
    print()

    # Pre-flight: show expected row counts
    for tbl, col in UPDATES:
        cur.execute(f'SELECT count(*) FROM {tbl} WHERE {col} LIKE "HAN-%"')
        n = cur.fetchone()[0]
        print(f'  {tbl}.{col}: {n} HAN-* rows to update')
    print()

    # Execute updates in a single transaction
    total = 0
    for tbl, col in UPDATES:
        cur.execute(
            f'UPDATE {tbl} SET {col} = "OH-" || {col} WHERE {col} LIKE "HAN-%"'
        )
        n = cur.rowcount
        print(f'  Updated {tbl}.{col}: {n} row(s)')
        total += n

    conn.commit()
    print()
    print(f'OK: COMMIT successful. {total} total rows updated.')
    print()

    # Post-flight verification
    print('Post-flight verification:')
    for tbl, col in UPDATES:
        cur.execute(f'SELECT count(*) FROM {tbl} WHERE {col} LIKE "HAN-%"')
        old = cur.fetchone()[0]
        cur.execute(f'SELECT count(*) FROM {tbl} WHERE {col} LIKE "OH-HAN-%"')
        new = cur.fetchone()[0]
        status = 'OK' if old == 0 else 'WARN: old IDs remain!'
        print(f'  {tbl}.{col}: HAN-* remaining={old}, OH-HAN-* now={new}  [{status}]')

except Exception as e:
    conn.rollback()
    print(f'ERROR: {e}')
    sys.exit(1)
finally:
    conn.close()
