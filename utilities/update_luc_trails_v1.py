"""
OH-LUC trail length_mi and maps backfill — Metroparks Toledo (Step 3)
Sources: metroparkstoledo.com individual trail pages, visited 2026-05-23.
All metroparkstoledo.com trails share the same all-parks brochure PDF as map.

Trails still NULL after this script:
  OH-LUC-T-001  Paved Bike Trail              — ohiodnr.gov (Maumee Bay, not yet visited)
  OH-LUC-T-004  Multi-use Trail               — ohiodnr.gov (Maumee Bay, not yet visited)
  OH-LUC-T-077  Manhattan Marsh Buckeye Basin — no length on current metroparkstoledo.com page
  OH-LUC-T-078  Anthony Wayne Trail           — ArcGIS dashboard
  OH-LUC-T-079  Oak Savanna and Cactus Loop   — nature.org (Kitty Todd)
  OH-LUC-T-080  Salamander Flats Wetland      — nature.org (Kitty Todd)
  OH-LUC-T-081  Sandhill Crane Viewing Area   — nature.org (Kitty Todd)
  OH-LUC-T-082  Miakonda Historical Trail     — erieshorescouncil.org
  OH-LUC-T-083  Camp Miakonda Orienteering    — erieshorescouncil.org

Notes on non-standard lengths:
  OH-LUC-T-056  Swan Creek Meadow Trail: page shows "Airport Hw. 1.3 mile loop round trip;
                Glendale Trailhead 1.05 miles round trip" — using 1.3 mi (Airport Hw loop)
  OH-LUC-T-059  Swan Creek Sycamore Trail: page shows "1.8 Round Trip" — using 1.8 mi

Run from project root:
  python utilities/update_luc_trails_v1.py
"""
import sqlite3
import datetime
import sys

sys.stdout.reconfigure(encoding='utf-8')

DB = 'NASqlite/natural_areas_v5.db'
now = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')

LUC_MAP = 'https://metroparkstoledo.com/media/11414/8-2025-all-parks-brochure-web.pdf'

# (trail_id, length_mi, maps_url)
# All from metroparkstoledo.com individual trail pages
UPDATES = [
    ('OH-LUC-T-011', 1.6,  LUC_MAP),   # Wabash Cannonball Trail Connector
    ('OH-LUC-T-012', 7.0,  LUC_MAP),   # University/Parks Trail
    ('OH-LUC-T-014', 1.9,  LUC_MAP),   # Oak Openings Corridor Trail (Moseley Trail)
    ('OH-LUC-T-015', 1.6,  LUC_MAP),   # Swan Creek Connector Trail
    ('OH-LUC-T-018', 1.0,  LUC_MAP),   # Blue Creek Quarry Loop Trail
    ('OH-LUC-T-019', 1.5,  LUC_MAP),   # Fallen Timbers Northwest Territory Trail
    ('OH-LUC-T-031', 3.0,  LUC_MAP),   # Pearson All Purpose Trail
    ('OH-LUC-T-032', 1.3,  LUC_MAP),   # Pearson Black Swamp Trail
    ('OH-LUC-T-033', 3.0,  LUC_MAP),   # Pearson Bicycle Trail
    ('OH-LUC-T-034', 2.9,  LUC_MAP),   # Pearson Exercise Trail
    ('OH-LUC-T-035', 1.3,  LUC_MAP),   # Pearson Wood Thrush Trail
    ('OH-LUC-T-036', 2.5,  LUC_MAP),   # Pearson North All Purpose Trail
    ('OH-LUC-T-037', 0.56, LUC_MAP),   # Pearson North Yellow Trail
    ('OH-LUC-T-040', 2.8,  LUC_MAP),   # Secor All Purpose Trail
    ('OH-LUC-T-041', 1.6,  LUC_MAP),   # Secor Bluebird Habitat Trail
    ('OH-LUC-T-042', 0.7,  LUC_MAP),   # Secor Forest Edge Trail
    ('OH-LUC-T-043', 0.3,  LUC_MAP),   # Secor Prairie Trail
    ('OH-LUC-T-044', 4.8,  LUC_MAP),   # Secor Ski Trail
    ('OH-LUC-T-045', 1.2,  LUC_MAP),   # Secor Upland Woods Trail
    ('OH-LUC-T-046', 0.8,  LUC_MAP),   # Secor Wetwoods Trail
    ('OH-LUC-T-047', 0.8,  LUC_MAP),   # Secor Wildflower Trail
    ('OH-LUC-T-048', 0.2,  LUC_MAP),   # Secor Woodland Pond Trail
    ('OH-LUC-T-049', 0.6,  LUC_MAP),   # Side Cut Canal Locks Trail
    ('OH-LUC-T-050', 3.9,  LUC_MAP),   # Side Cut Fallen Timbers Trail
    ('OH-LUC-T-051', 1.3,  LUC_MAP),   # Side Cut Riverview Trail
    ('OH-LUC-T-052', 0.9,  LUC_MAP),   # Side Cut Wood Duck Trail
    ('OH-LUC-T-053', 3.3,  LUC_MAP),   # Swan Creek All Purpose
    ('OH-LUC-T-054', 1.72, LUC_MAP),   # Swan Creek Big Woods Trail
    ('OH-LUC-T-055', 0.76, LUC_MAP),   # Swan Creek Trail
    ('OH-LUC-T-056', 1.3,  LUC_MAP),   # Swan Creek Meadow Trail (Airport Hw. 1.3 mi loop)
    ('OH-LUC-T-057', 1.32, LUC_MAP),   # Swan Creek North Loop Trail
    ('OH-LUC-T-058', 0.6,  LUC_MAP),   # Swan Creek Floodplain Trail
    ('OH-LUC-T-059', 1.8,  LUC_MAP),   # Swan Creek Sycamore Trail (1.8 mi round trip)
    ('OH-LUC-T-060', 1.0,  LUC_MAP),   # Westwinds Trail
    ('OH-LUC-T-061', 1.65, LUC_MAP),   # Wildwood All Purpose Walk/Bike Trail
    ('OH-LUC-T-062', 1.35, LUC_MAP),   # Wildwood Floodplain Trail
    ('OH-LUC-T-063', 1.6,  LUC_MAP),   # Wildwood Grasslands Trail
    ('OH-LUC-T-064', 0.6,  LUC_MAP),   # Wildwood Meadow Loop Trail
    ('OH-LUC-T-065', 0.4,  LUC_MAP),   # Wildwood Ridge Trail
    ('OH-LUC-T-066', 1.3,  LUC_MAP),   # Wildwood Prairie Trail
    ('OH-LUC-T-067', 2.5,  LUC_MAP),   # Wildwood Upland Woods Trail
    ('OH-LUC-T-068', 0.6,  LUC_MAP),   # Wiregrass Loop Trail
    ('OH-LUC-T-069', 1.1,  LUC_MAP),   # Middlegrounds Walk/Bike Path
    ('OH-LUC-T-070', 0.7,  LUC_MAP),   # Cannonball Prairie Leopard Frog Trail
    ('OH-LUC-T-071', 1.5,  LUC_MAP),   # Cannonball Prairie Big Bluestem Trail
    # T-077 maps only (no length on page)
    ('OH-LUC-T-077', None, LUC_MAP),   # Manhattan Marsh Preserve Buckeye Basin Loop Trail
]

conn = sqlite3.connect(DB)
cur = conn.cursor()
len_ok = 0
map_ok = 0

try:
    # Pre-flight: confirm all trail_ids exist
    missing = []
    for trail_id, *_ in UPDATES:
        cur.execute('SELECT count(*) FROM trails WHERE trail_id=?', (trail_id,))
        if cur.fetchone()[0] == 0:
            missing.append(trail_id)
    if missing:
        print(f'ERROR: trail_ids not found in DB: {missing}')
        sys.exit(1)
    print(f'Pre-flight OK: all {len(UPDATES)} trail_ids exist.')
    print()

    for trail_id, length_mi, maps_url in UPDATES:
        if length_mi is not None:
            cur.execute(
                'UPDATE trails SET length_mi=?, maps=?, updated_at=? WHERE trail_id=? AND length_mi IS NULL',
                (length_mi, maps_url, now, trail_id)
            )
            n = cur.rowcount
            len_ok += n
            map_ok += n
            print(f'  {trail_id}  length={length_mi} mi  maps=set  rows={n}')
        else:
            # Maps only
            cur.execute(
                'UPDATE trails SET maps=?, updated_at=? WHERE trail_id=? AND (maps IS NULL OR maps="")',
                (maps_url, now, trail_id)
            )
            n = cur.rowcount
            map_ok += n
            print(f'  {trail_id}  length=skip  maps=set  rows={n}')

    conn.commit()
    print()
    print(f'OK: COMMIT successful.')
    print(f'    length_mi updated: {len_ok} trail(s)')
    print(f'    maps updated:      {map_ok} trail(s)')
    print()

    # Post-flight
    cur.execute("SELECT count(*) FROM trails WHERE trail_id LIKE 'OH-LUC-T-%' AND length_mi IS NOT NULL")
    filled = cur.fetchone()[0]
    cur.execute("SELECT count(*) FROM trails WHERE trail_id LIKE 'OH-LUC-T-%' AND length_mi IS NULL")
    remaining = cur.fetchone()[0]
    print(f'Post-flight OH-LUC:')
    print(f'  length_mi filled: {filled}')
    print(f'  still NULL:       {remaining}')
    if remaining:
        cur.execute("SELECT trail_id, name FROM trails WHERE trail_id LIKE 'OH-LUC-T-%' AND length_mi IS NULL ORDER BY trail_id")
        for r in cur.fetchall():
            print(f'    {r[0]}  {r[1]}')

except Exception as e:
    conn.rollback()
    print(f'ERROR: {e}')
    sys.exit(1)
finally:
    conn.close()
