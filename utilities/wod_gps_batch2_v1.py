"""
wod_gps_batch2_v1.py
Wood County — GPS acquisition batch 2 (2026-05-23)

Acquires GPS for 23 sites across City of Bowling Green, City of Perrysburg,
City of Rossford, and village parks (Walbridge, Tontogany, Grand Rapids,
Pemberville), plus BGSU Native Prairie Garden.

All GPS sourced from Nominatim/OSM park-name or address lookup.

Sites NOT included (not resolvable via Nominatim):
  OH-WOD-SI-044  Dunbridge Road Soccer Fields (location "behind Municipal Court" uncertain)
  OH-WOD-SI-058  Woodland Park (Perrysburg) — not in OSM
  OH-WOD-SI-061  Ed Ford Memorial Park (Rossford) — not in OSM
  OH-WOD-SI-067  Village Park (North Baltimore) — not in OSM
  OH-WOD-SI-073  Mishe Monoto Preserve — no address known
  OH-WOD-SI-076  Bell Woods Nature Preserve (BSC) — GPS null, not in OSM
  OH-WOD-SI-077  Pat & Clint Mauk's Prairie (BSC) — GPS null, not in OSM
  OH-WOD-SI-003 through SI-015  ODNR Wildlife Areas — require ODNR GIS layer

Run from project root:
  python utilities/wod_gps_batch2_v1.py
"""

import sqlite3
import datetime
import pathlib
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PROJECT_ROOT = pathlib.Path(__file__).parent.parent
DB_PATH = PROJECT_ROOT / 'NASqlite' / 'natural_areas_v5.db'

sys.path.insert(0, str(PROJECT_ROOT))
from utilities.na_plus_code import encode_plus_code

now = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')

# (site_id, gps_lat, gps_lon)
GPS_UPDATES = [
    # City of Bowling Green parks
    ('OH-WOD-SI-039', 41.366858, -83.652015),   # Bellard Park — OSM park record
    ('OH-WOD-SI-043', 41.37751,  -83.664336),   # Conneaut Haskins Park — OSM park
    ('OH-WOD-SI-045', 41.367161, -83.654461),   # Raney Park — OSM park record
    ('OH-WOD-SI-046', 41.378462, -83.648353),   # Ridge Park — 225 Ridge St address

    # City of Perrysburg parks
    ('OH-WOD-SI-048', 41.540388, -83.625405),   # Bicentennial Park — OSM park
    ('OH-WOD-SI-049', 41.550677, -83.659183),   # Davis Overlook — OSM park
    ('OH-WOD-SI-050', 41.541684, -83.63388),    # Eisenhower Park — OSM park
    ('OH-WOD-SI-051', 41.56086,  -83.63052),    # Hood Park — OSM park
    ('OH-WOD-SI-052', 41.555718, -83.616606),   # Milestone Park — OSM park
    ('OH-WOD-SI-053', 41.558309, -83.645486),   # Orleans Park — OSM park
    ('OH-WOD-SI-054', 41.559242, -83.634115),   # Riverside Park — OSM park
    ('OH-WOD-SI-055', 41.534771, -83.653053),   # Rotary Community Park — OSM park
    ('OH-WOD-SI-056', 41.534891, -83.660216),   # Rivercrest Park — OSM park
    ('OH-WOD-SI-057', 41.557303, -83.596258),   # Three Meadows Park — OSM park

    # City of Rossford parks
    ('OH-WOD-SI-059', 41.615737, -83.564352),   # Veterans Memorial Park — OSM park
    ('OH-WOD-SI-060', 41.601646, -83.571117),   # Island View Park — OSM park
    ('OH-WOD-SI-062', 41.609495, -83.555318),   # Beech Street Park — OSM road-level

    # Village parks
    ('OH-WOD-SI-068', 41.590858, -83.495492),   # Railway Park Walbridge — OSM playground
    ('OH-WOD-SI-069', 41.418859, -83.739349),   # Mehring Park Tontogany — OSM park
    ('OH-WOD-SI-070', 41.422079, -83.738343),   # Centennial Park Tontogany — OSM park
    ('OH-WOD-SI-071', 41.410461, -83.859555),   # Grand Rapids Park — OSM footway (approx)
    ('OH-WOD-SI-072', 41.412902, -83.457686),   # Memorial Park Pemberville — OSM park

    # BGSU
    ('OH-WOD-SI-075', 41.376303, -83.674557),   # BGSU Native Prairie Garden — Wintergarden Rd (approx)
]


def run():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    try:
        print('Pre-flight checks')
        print('-' * 60)

        ids = [u[0] for u in GPS_UPDATES]
        placeholders = ','.join(['?' for _ in ids])
        cur.execute(
            f'SELECT site_id, name, gps_lat FROM sites '
            f'WHERE site_id IN ({placeholders}) ORDER BY site_id',
            ids
        )
        rows = {r[0]: r for r in cur.fetchall()}

        missing = [sid for sid in ids if sid not in rows]
        if missing:
            print(f'  WARN: not found in DB: {missing}')

        print(f'  Sites to update: {len(GPS_UPDATES)}  (found: {len(rows)})')
        print()
        for sid, lat, lon in GPS_UPDATES:
            row = rows.get(sid)
            if row:
                cur_gps = str(row[2]) if row[2] else 'no GPS'
                print(f'  {sid}: {row[1][:42]:<42}  {cur_gps} -> {lat},{lon}')

        cur.execute("SELECT count(*) FROM sites WHERE site_id LIKE 'OH-WOD-%' AND (gps_lat IS NULL OR gps_lat='')")
        print(f'\n  GPS-missing WOD sites before: {cur.fetchone()[0]}')

        print()
        input('Pre-flight OK. Press Enter to execute (Ctrl-C to abort)...')
        print()

        updated = 0
        for sid, lat, lon in GPS_UPDATES:
            if sid not in rows:
                print(f'  SKIP {sid}: not in DB')
                continue
            try:
                plus_code = encode_plus_code(lat, lon)
            except Exception as e:
                plus_code = None
                print(f'    WARN: plus_code failed for {sid}: {e}')

            cur.execute(
                'UPDATE sites SET gps_lat=?, gps_lon=?, plus_code=?, updated_at=? '
                'WHERE site_id=?',
                (lat, lon, plus_code, now, sid)
            )
            print(f'  Updated {sid}: {lat},{lon} plus={plus_code}')
            updated += 1

        conn.commit()
        print()
        print(f'COMMIT OK -- {updated} GPS records updated')
        print()

        # Post-flight
        print('Post-flight verification')
        print('-' * 60)
        cur.execute("SELECT count(*) FROM sites WHERE site_id LIKE 'OH-WOD-%' AND (gps_lat IS NULL OR gps_lat='')")
        still_missing = cur.fetchone()[0]
        print(f'  GPS-missing WOD sites after: {still_missing}')

        # Spot check
        spot = ['OH-WOD-SI-039', 'OH-WOD-SI-054', 'OH-WOD-SI-068', 'OH-WOD-SI-072']
        for sid in spot:
            cur.execute('SELECT site_id, name, gps_lat, gps_lon, plus_code FROM sites WHERE site_id=?', (sid,))
            r = cur.fetchone()
            if r:
                print(f'  {r[0]}: {r[1][:35]} | {r[2]},{r[3]} | {r[4]}')

    except KeyboardInterrupt:
        conn.rollback()
        print()
        print('Aborted -- rollback. No changes made.')
        sys.exit(0)
    except Exception as e:
        conn.rollback()
        print(f'ERROR: {e}')
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        conn.close()


if __name__ == '__main__':
    run()
