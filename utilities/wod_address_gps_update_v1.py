"""
wod_address_gps_update_v1.py
Wood County — address corrections, GPS acquisition, and SI-028 phantom deletion.
Run date: 2026-05-23

Changes:

DELETE:
  OH-WOD-SI-028  Nature Trails Park (WCPD) — confirmed AutoRecovered phantom.
    Astronomical observation program belongs to Beaver Creek Preserve (SI-019).
    Nature Trails Park at 4950 Curtice Rd is a City of Northwood entity (SI-064).

WCPD SITES — location corrections and GPS acquisition:
  OH-WOD-SI-016  Adam Phillips Pond — location corrected to confirmed address
  OH-WOD-SI-017  Arrowwood Archery Range — address confirmed; GPS acquired
  OH-WOD-SI-018  Baldwin Woods Preserve — address confirmed; GPS acquired
  OH-WOD-SI-019  Beaver Creek Preserve — address confirmed; GPS acquired
  OH-WOD-SI-020  Black Swamp Preserve — location corrected; GPS acquired
  OH-WOD-SI-024  Cedar Creeks Preserve — address confirmed; GPS acquired; notes updated
  OH-WOD-SI-025  Cricket Frog Cove — address confirmed; GPS acquired
  OH-WOD-SI-026  Fuller Preserve — address confirmed; GPS acquired
  OH-WOD-SI-029  Otsego Park — address confirmed; GPS still not resolvable via Nominatim
  OH-WOD-SI-030  Rudolph Bike Park — address corrected; GPS corrected (was museum GPS)
  OH-WOD-SI-031  Rudolph Savanna — address confirmed; GPS acquired

CITY OF NORTHWOOD PARKS — address and GPS:
  OH-WOD-SI-063  Ranger Park — address confirmed (3201 Curtice Rd); GPS acquired
  OH-WOD-SI-064  Nature Trails Park (Northwood) — address confirmed; GPS from user
  OH-WOD-SI-065  Central Park (Northwood) — address confirmed; GPS acquired
  OH-WOD-SI-066  Brentwood Park — address confirmed; GPS acquired

GPS source: Nominatim / OSM geocoding except SI-064 (user-provided).
Plus codes: computed via na_plus_code.encode_plus_code.

Run from project root:
  python utilities/wod_address_gps_update_v1.py
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

# --- Data ---

# (site_id, new_location, new_gps_lat, new_gps_lon, notes_override_or_None)
# notes_override: if not None, replaces notes; use '' to clear GPS-needed language
UPDATES = [
    # WCPD — Adam Phillips Pond: corrected address (was museum address 13660 County Home Rd)
    ('OH-WOD-SI-016', '1740 E Gypsy Lane Rd, Bowling Green, OH 43402', None, None, None),

    # WCPD — Arrowwood Archery Range: address confirmed; GPS from Nominatim
    ('OH-WOD-SI-017', '11126 Linwood Rd, Bowling Green, OH 43402',
     41.349831, -83.617235, None),

    # WCPD — Baldwin Woods Preserve: address confirmed; GPS from Nominatim park-name lookup
    ('OH-WOD-SI-018', '14080 Range Line Rd, Weston, OH 43402',
     41.36059, -83.760078, None),

    # WCPD — Beaver Creek Preserve: address confirmed; GPS from Nominatim park-name lookup
    ('OH-WOD-SI-019', '23028 Long Judson Rd, Grand Rapids, OH 43522',
     41.401308, -83.845652, None),

    # WCPD — Black Swamp Preserve: address corrected (was "E. Gypsy Lane Road"); GPS from Nominatim
    ('OH-WOD-SI-020', '1014 S Maple St, Bowling Green, OH 43402',
     41.359115, -83.657326, None),

    # WCPD — Cedar Creeks Preserve: address confirmed; GPS acquired; clear GPS-needed note
    ('OH-WOD-SI-024', '4575 Walbridge Rd, Northwood, OH 43619',
     41.588105, -83.441897,
     'Address confirmed via Wood County Park District website (2026-05-23). '
     '42 acres; wet woods and grasslands; 1.72-mi hiking trails; playground; '
     'play field; pollinator gardens; little free library; picnic shelter.'),

    # WCPD — Cricket Frog Cove: address confirmed; GPS from Nominatim park-name lookup
    ('OH-WOD-SI-025', '14810 Freyman Rd, Cygnet, OH 43413',
     41.2385, -83.68349, None),

    # WCPD — Fuller Preserve: address confirmed (was "Near Weston"); GPS from Nominatim park-name
    ('OH-WOD-SI-026', '12153 Cross Creek Rd, Bowling Green, OH 43402',
     41.435389, -83.631475, None),

    # WCPD — Otsego Park: address confirmed; GPS not resolvable via Nominatim
    ('OH-WOD-SI-029', '20000 W River Rd, Bowling Green, OH 43402',
     None, None,
     'Address confirmed via Wood County Park District website (2026-05-23). '
     '21 acres on Maumee River; 0.22-mi trail; playgrounds; river walk; boat launch; '
     'fishing; Thompson Stone Hall (glass lookout). GPS acquisition still needed.'),

    # WCPD — Rudolph Bike Park: address corrected; GPS corrected (was 41.4441,-83.6968, incorrect)
    ('OH-WOD-SI-030', '14045 Mermill Rd, Rudolph, OH 43462',
     41.297667, -83.671084, None),

    # WCPD — Rudolph Savanna: address confirmed; GPS from Nominatim address lookup
    ('OH-WOD-SI-031', '10330 Rudolph Rd, Rudolph, OH 43462',
     41.304004, -83.669577, None),

    # City of Northwood — Ranger Park
    ('OH-WOD-SI-063', '3201 Curtice Rd, Northwood, OH 43619',
     41.616121, -83.475775,
     'Confirmed 2026-05-23 via northwoodoh.gov/residents/parks.php. '
     '5-acre Stoner Pond; 0.4-mi walking path; picnic tables; fishing; '
     'fishing dock (opened 2024); annual Kids Fishing Derby.'),

    # City of Northwood — Nature Trails Park (address + GPS from user, 2026-05-23)
    ('OH-WOD-SI-064', '4950 Curtice Rd, Northwood, OH 43619',
     41.6126, -83.43209,
     'Confirmed 2026-05-23 via northwoodoh.gov/residents/parks.php and user. '
     'Scenic one-mile trail with exercise stations donated by St. Charles Hospital. '
     'Benches along trail.'),

    # City of Northwood — Central Park
    ('OH-WOD-SI-065', 'Oram Rd, Northwood, OH 43619',
     41.611069, -83.48184,
     'Confirmed 2026-05-23 via northwoodoh.gov/residents/parks.php. '
     'Behind Northwood Municipal Building. Hosts Northwood Fall Festival and '
     'Palooza in the Park. Playground; basketball court; pickleball court; '
     'baseball diamond; outdoor shelter house.'),

    # City of Northwood — Brentwood Park
    ('OH-WOD-SI-066', '320 Brentwood Dr, Northwood, OH 43619',
     41.613492, -83.533732,
     'Confirmed 2026-05-23 via northwoodoh.gov/residents/parks.php. West side. '
     'Walking trail; playground; disc golf; pickleball courts; basketball court; '
     'picnic area; soccer fields; t-ball/softball/baseball diamonds; outdoor shelter; '
     'concession stand; restrooms; Miracle League of Northwest Ohio rubberized '
     'baseball field (accessible).'),
]

# SI-064 also needs url_primary and plus_code handled specially below
SI_064_URL = 'https://www.northwoodoh.gov/residents/parks.php'

# Delete phantom
DELETE_ID = 'OH-WOD-SI-028'
DELETE_REASON = (
    'Confirmed AutoRecovered phantom (2026-05-23). '
    'Astronomical observation program (large telescope, observation deck) '
    'belongs to Beaver Creek Preserve (OH-WOD-SI-019), confirmed via '
    'Wood County Park District website. '
    '"Nature Trails Park" at 4950 Curtice Rd is a City of Northwood entity '
    '(OH-WOD-SI-064), not a WCPD property. No FK references.'
)


def run():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    try:
        # --- Pre-flight ---
        print('Pre-flight checks')
        print('-' * 60)

        # Confirm delete target exists
        cur.execute('SELECT site_id, name FROM sites WHERE site_id=?', (DELETE_ID,))
        r = cur.fetchone()
        print(f'  {DELETE_ID}: {"FOUND -- " + r[1] if r else "NOT FOUND"}')
        if not r:
            print(f'  WARN: {DELETE_ID} not found -- already deleted?')

        # FK check for delete target
        fk_checks = [
            ('access_points',        'parent_entity_id'),
            ('access_point_parents', 'parent_entity_id'),
            ('trail_parents',        'parent_site_id'),
            ('site_parent',          'site_id'),
            ('site_parent',          'parent_site_id'),
            ('site_network_members', 'site_id'),
        ]
        refs = []
        for tbl, col in fk_checks:
            cur.execute(f'SELECT count(*) FROM {tbl} WHERE {col}=?', (DELETE_ID,))
            n = cur.fetchone()[0]
            if n:
                refs.append(f'{tbl}.{col}={n}')
        if refs:
            print(f'  ERROR: FK references for {DELETE_ID}: {refs}')
            sys.exit(1)
        print(f'  {DELETE_ID} FK check: clean')

        # Preview update targets
        ids = [u[0] for u in UPDATES]
        placeholders = ','.join(['?' for _ in ids])
        cur.execute(
            f'SELECT site_id, name, gps_lat, gps_lon FROM sites '
            f'WHERE site_id IN ({placeholders}) ORDER BY site_id',
            ids
        )
        rows = {r[0]: r for r in cur.fetchall()}
        print(f'\n  Update targets ({len(UPDATES)}):')
        for sid, loc, lat, lon, notes in UPDATES:
            row = rows.get(sid)
            if row:
                cur_gps = f'{row[2]},{row[3]}' if row[2] else 'no GPS'
                new_gps = f'{lat},{lon}' if lat else 'no change'
                print(f'    {sid}: {row[1][:40]:<40} GPS: {cur_gps} -> {new_gps}')
            else:
                print(f'    {sid}: NOT FOUND IN DB')

        print()
        cur.execute("SELECT count(*) FROM sites WHERE site_id LIKE 'OH-WOD-%'")
        print(f'  OH-WOD-* sites before: {cur.fetchone()[0]}')

        print()
        input('Pre-flight OK. Press Enter to execute (Ctrl-C to abort)...')
        print()

        # --- Execute ---

        # 1. Delete SI-028
        cur.execute('DELETE FROM sites WHERE site_id=?', (DELETE_ID,))
        print(f'  Deleted {DELETE_ID}: {cur.rowcount} row(s)  [{DELETE_REASON[:70]}...]')

        # 2. Update sites
        updated = 0
        for sid, new_loc, new_lat, new_lon, notes_override in UPDATES:
            cur.execute('SELECT gps_lat, gps_lon, location, notes, url_primary FROM sites WHERE site_id=?', (sid,))
            row = cur.fetchone()
            if not row:
                print(f'  SKIP {sid}: not found')
                continue

            cur_lat, cur_lon, cur_loc, cur_notes, cur_url = row

            # Compute plus code if new GPS provided
            plus_code = None
            if new_lat and new_lon:
                try:
                    plus_code = encode_plus_code(new_lat, new_lon)
                except Exception as e:
                    print(f'    WARN: plus_code failed for {sid}: {e}')

            # Determine final values
            final_lat = new_lat if new_lat is not None else cur_lat
            final_lon = new_lon if new_lon is not None else cur_lon
            final_loc = new_loc  # always update location
            final_notes = notes_override if notes_override is not None else cur_notes

            # Special case: SI-064 gets url_primary
            if sid == 'OH-WOD-SI-064':
                cur.execute(
                    'UPDATE sites SET location=?, gps_lat=?, gps_lon=?, '
                    'plus_code=?, notes=?, url_primary=?, updated_at=? '
                    'WHERE site_id=?',
                    (final_loc, final_lat, final_lon,
                     plus_code, final_notes, SI_064_URL, now, sid)
                )
            elif new_lat is not None:
                cur.execute(
                    'UPDATE sites SET location=?, gps_lat=?, gps_lon=?, '
                    'plus_code=?, notes=?, updated_at=? '
                    'WHERE site_id=?',
                    (final_loc, final_lat, final_lon,
                     plus_code, final_notes, now, sid)
                )
            else:
                # Address/notes only update (no GPS change)
                cur.execute(
                    'UPDATE sites SET location=?, notes=?, updated_at=? '
                    'WHERE site_id=?',
                    (final_loc, final_notes, now, sid)
                )

            gps_note = f'GPS: {final_lat},{final_lon} plus={plus_code}' if new_lat else 'addr only'
            print(f'  Updated {sid}: {gps_note}')
            updated += 1

        conn.commit()
        print()
        print(f'COMMIT OK -- 1 deleted, {updated} updated')
        print()

        # --- Post-flight ---
        print('Post-flight verification')
        print('-' * 60)

        cur.execute('SELECT count(*) FROM sites WHERE site_id=?', (DELETE_ID,))
        print(f'  {DELETE_ID} in sites: {cur.fetchone()[0]} (expect 0)')

        cur.execute("SELECT count(*) FROM sites WHERE site_id LIKE 'OH-WOD-%'")
        total = cur.fetchone()[0]
        print(f'  OH-WOD-* sites after: {total}')

        print()
        print('  Sample GPS spot-check:')
        spot_ids = ['OH-WOD-SI-019', 'OH-WOD-SI-024', 'OH-WOD-SI-064', 'OH-WOD-SI-066']
        for sid in spot_ids:
            cur.execute(
                'SELECT site_id, name, location, gps_lat, gps_lon, plus_code '
                'FROM sites WHERE site_id=?', (sid,)
            )
            r = cur.fetchone()
            if r:
                print(f'    {r[0]}: {r[1][:30]} | {r[2][:45]} | {r[3]},{r[4]} | {r[5]}')

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
