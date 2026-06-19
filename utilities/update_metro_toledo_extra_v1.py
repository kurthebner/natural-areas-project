"""
metroparkstoledo.com trail length_mi backfill — non-LUC counties
Sources: metroparkstoledo.com individual trail pages, visited 2026-05-23.
Covers: OH-FUL, OH-MC (Oak Openings), OH-OTT (Howard Marsh), OH-WOD (Providence)

Run from project root:
  python utilities/update_metro_toledo_extra_v1.py
"""
import sqlite3
import datetime
import sys

sys.stdout.reconfigure(encoding='utf-8')

DB = 'NASqlite/natural_areas_v5.db'
now = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')

LUC_MAP = 'https://metroparkstoledo.com/media/11414/8-2025-all-parks-brochure-web.pdf'

UPDATES = [
    # Fulton County
    ('OH-FUL-T-016', 12.0,  LUC_MAP),  # Beach Ridge Singletrack Trail
    ('OH-FUL-T-017', 1.5,   LUC_MAP),  # Chessie Circle Trail
    # Multi-county — Oak Openings + Towpath
    ('OH-MC-T-009',  8.3,   LUC_MAP),  # Towpath Trail
    ('OH-MC-T-020',  5.3,   LUC_MAP),  # Oak Openings All Purpose/Bike Trail
    ('OH-MC-T-021',  2.2,   LUC_MAP),  # Oak Openings Evergreen Trail
    ('OH-MC-T-022',  2.8,   LUC_MAP),  # Oak Openings Ferns and Lakes Trail
    ('OH-MC-T-023',  15.2,  LUC_MAP),  # Oak Openings Hiking Trail
    ('OH-MC-T-024',  22.4,  LUC_MAP),  # Oak Openings Horse Trail
    ('OH-MC-T-025',  1.5,   LUC_MAP),  # Oak Openings Foxfire Trail
    ('OH-MC-T-026',  0.6,   LUC_MAP),  # Oak Openings Mallard Lake Loop
    ('OH-MC-T-027',  2.9,   LUC_MAP),  # Oak Openings Ridge Trail
    ('OH-MC-T-028',  1.6,   LUC_MAP),  # Oak Openings Sand Dunes Trail
    ('OH-MC-T-029',  3.2,   LUC_MAP),  # Oak Openings Ski Trails
    ('OH-MC-T-030',  1.0,   LUC_MAP),  # Oak Openings Springbrook Lake Trail
    # Ottawa County — Howard Marsh
    ('OH-OTT-T-072', 1.3,   LUC_MAP),  # Howard Marsh Sandpiper Trail
    ('OH-OTT-T-073', 1.4,   LUC_MAP),  # Howard Marsh Mallard Trail
    ('OH-OTT-T-074', 1.6,   LUC_MAP),  # Howard Marsh Madewell Trail
    ('OH-OTT-T-075', 3.8,   LUC_MAP),  # Howard Marsh Egret Trail
    ('OH-OTT-T-076', 2.3,   LUC_MAP),  # Howard Marsh Sora Trail
    # Wood County — Providence
    ('OH-WOD-T-038', 2.25,  LUC_MAP),  # Providence River Bluff Trail
    ('OH-WOD-T-039', 0.4,   LUC_MAP),  # Providence Wolf Rapids
]

conn = sqlite3.connect(DB)
cur = conn.cursor()
ok = 0

try:
    missing = [tid for tid, *_ in UPDATES
               if cur.execute('SELECT count(*) FROM trails WHERE trail_id=?', (tid,)).fetchone()[0] == 0]
    if missing:
        print(f'ERROR: not found: {missing}')
        sys.exit(1)
    print(f'Pre-flight OK: all {len(UPDATES)} trail_ids exist.')
    print()

    for trail_id, length_mi, maps_url in UPDATES:
        cur.execute(
            'UPDATE trails SET length_mi=?, maps=?, updated_at=? WHERE trail_id=? AND length_mi IS NULL',
            (length_mi, maps_url, now, trail_id)
        )
        n = cur.rowcount
        ok += n
        print(f'  {trail_id}  {length_mi} mi  rows={n}')

    conn.commit()
    print()
    print(f'OK: COMMIT — {ok} trail(s) updated.')
    print()

    # Post-flight per county
    for county in ('OH-FUL', 'OH-MC', 'OH-OTT', 'OH-WOD'):
        cur.execute(f"SELECT count(*) FROM trails WHERE trail_id LIKE '{county}%' AND length_mi IS NOT NULL")
        filled = cur.fetchone()[0]
        cur.execute(f"SELECT count(*) FROM trails WHERE trail_id LIKE '{county}%'")
        total = cur.fetchone()[0]
        print(f'  {county}: {filled}/{total} trails with length_mi')

except Exception as e:
    conn.rollback()
    print(f'ERROR: {e}')
    sys.exit(1)
finally:
    conn.close()
