"""
gps_multicounty_batch_v1.py
Multi-county GPS acquisition batch — 2026-05-23

Acquires GPS for 73 GPS-missing sites across 6 counties:
  FR (1), FUL (4), HAN (45), SAN (1), SC (2), WOD (20)

Method: Nominatim/OSM geocoding with county bounding box validation (IMP-081).
Each site is tried with up to 2 query formats; first to pass bbox check is accepted.

NOTE: ODNR wildlife areas (numbered county parcels) are typically NOT in OSM.
Expect most of the ~26 wildlife area entries to remain UNRESOLVED and require
a separate ODNR GIS pass (ODNR Ohio Lake Map Resource — see na_gps_acquisition §5.9).

Run from project root:
  python utilities/gps_multicounty_batch_v1.py
"""

import sqlite3
import datetime
import pathlib
import sys
import urllib.request
import urllib.parse
import json
import time

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PROJECT_ROOT = pathlib.Path(__file__).parent.parent
DB_PATH = PROJECT_ROOT / 'NASqlite' / 'natural_areas_v5.db'

sys.path.insert(0, str(PROJECT_ROOT))
from utilities.na_plus_code import encode_plus_code

now = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')

NOMINATIM_UA = 'NaturalAreasProject/5.0 khebner@hotmail.com'
RATE_LIMIT = 1.1   # seconds between Nominatim calls — mandatory per ToS

# County centroids (lat, lon) for bounding box validation — IMP-081
COUNTY_CENTROIDS = {
    'FR':  (39.98, -82.98),   # Franklin County
    'FUL': (41.58, -84.14),   # Fulton County
    'HAN': (41.00, -83.65),   # Hancock County
    'SAN': (41.39, -82.99),   # Sandusky County
    'SC':  (38.81, -82.98),   # Scioto County
    'WOD': (41.37, -83.61),   # Wood County
}
BUFFER_DEG = 0.40  # ±0.40° (~28 mi) — slightly wider than IMP-081 default for edge sites

# GPS_TARGETS: (site_id, display_name, county_code, [query1, query2, ...])
GPS_TARGETS = [

    # ===== FR (Franklin County — 1 site) =====
    ('OH-FR-S-1040', 'Finnell Park', 'FR',
     ['Finnell Park, Columbus, Ohio',
      'Finnell Park, Franklin County, Ohio']),

    # ===== FUL (Fulton County — 4 sites) =====
    ('OH-FUL-SI-024', 'Hatcher Park', 'FUL',
     ['Hatcher Park, Fayette, Ohio',
      'Hatcher Park, Fulton County, Ohio']),
    ('OH-FUL-SI-025', 'Normal Grove Park', 'FUL',
     ['Normal Grove Park, Fayette, Ohio',
      'Normal Grove Park, Fulton County, Ohio']),
    ('OH-FUL-SI-027', 'Green Memorial Park', 'FUL',
     ['Green Memorial Park, Lyons, Ohio',
      'Green Memorial Park, Fulton County, Ohio']),
    ('OH-FUL-SI-028', 'Lyons Community Ball Park', 'FUL',
     ['Lyons Community Ball Park, Lyons, Ohio',
      'Lyons Community Park, Lyons, Ohio']),

    # ===== HAN (Hancock County — 45 sites) =====

    # ODNR Division of Wildlife — numbered areas (likely not in OSM; expect UNRESOLVED)
    ('OH-HAN-S-003', 'Hancock County Wildlife Area 1', 'HAN',
     ['Hancock County Wildlife Area 1, Ohio',
      'Hancock County Wildlife Area 1, Hancock County, Ohio']),
    ('OH-HAN-S-004', 'Hancock County Wildlife Area 3', 'HAN',
     ['Hancock County Wildlife Area 3, Ohio',
      'Hancock County Wildlife Area 3, Hancock County, Ohio']),
    ('OH-HAN-S-005', 'Hancock County Wildlife Area 4', 'HAN',
     ['Hancock County Wildlife Area 4, Ohio',
      'Hancock County Wildlife Area 4, Hancock County, Ohio']),
    ('OH-HAN-S-006', 'Hancock County Wildlife Area 5', 'HAN',
     ['Hancock County Wildlife Area 5, Ohio',
      'Hancock County Wildlife Area 5, Hancock County, Ohio']),
    ('OH-HAN-S-007', 'Hancock County Wildlife Area 6', 'HAN',
     ['Hancock County Wildlife Area 6, Ohio',
      'Hancock County Wildlife Area 6, Hancock County, Ohio']),
    ('OH-HAN-S-008', 'Hancock County Wildlife Area 7', 'HAN',
     ['Hancock County Wildlife Area 7, Ohio',
      'Hancock County Wildlife Area 7, Hancock County, Ohio']),
    ('OH-HAN-S-009', 'Wildlife Production Area 9', 'HAN',
     ['Wildlife Production Area 9, Hancock County, Ohio']),
    ('OH-HAN-S-010', 'Wildlife Production Area 25', 'HAN',
     ['Wildlife Production Area 25, Hancock County, Ohio']),
    ('OH-HAN-S-011', 'Wildlife Production Area 32', 'HAN',
     ['Wildlife Production Area 32, Hancock County, Ohio']),
    ('OH-HAN-S-012', 'Wildlife Production Area 41', 'HAN',
     ['Wildlife Production Area 41, Hancock County, Ohio']),
    ('OH-HAN-S-013', 'Wildlife Production Area 43', 'HAN',
     ['Wildlife Production Area 43, Hancock County, Ohio']),
    ('OH-HAN-S-014', 'Wildlife Production Area 45', 'HAN',
     ['Wildlife Production Area 45, Hancock County, Ohio']),
    ('OH-HAN-S-015', 'Wildlife Production Area 46', 'HAN',
     ['Wildlife Production Area 46, Hancock County, Ohio']),

    # Hancock Park District
    ('OH-HAN-S-035', 'Riverbend Conservation Area', 'HAN',
     ['Riverbend Conservation Area, Findlay, Ohio',
      'Riverbend Conservation Area, Hancock County, Ohio']),
    ('OH-HAN-S-088', 'Arcadia Lions Community Park', 'HAN',
     ['301 W Brown Rd, Arcadia, Ohio',
      'Arcadia Lions Community Park, Arcadia, Ohio']),
    ('OH-HAN-S-090', 'Vanlue Community Park', 'HAN',
     ['Vanlue Community Park, Vanlue, Ohio',
      'John Street, Vanlue, Ohio']),

    # City of Findlay — Flag Acres complex child sites
    ('OH-HAN-S-057', 'Roethlisberger Field', 'HAN',
     ['3430 North Main Street, Findlay, Ohio',
      'Roethlisberger Field, Findlay, Ohio']),
    ('OH-HAN-S-058', 'The Cube Ice Arena', 'HAN',
     ['3430 North Main Street, Findlay, Ohio',
      'The Cube Ice Arena, Findlay, Ohio']),
    ('OH-HAN-S-059', 'Marathon Diamonds', 'HAN',
     ['3430 North Main Street, Findlay, Ohio',
      'Marathon Diamonds, Findlay, Ohio']),

    # City of Findlay — Blanchard River complex child sites
    ('OH-HAN-S-065', 'Guthrie Field', 'HAN',
     ['1827 South Blanchard Street, Findlay, Ohio',
      'Guthrie Field, Findlay, Ohio']),
    ('OH-HAN-S-066', 'Hancock Field', 'HAN',
     ['1827 South Blanchard Street, Findlay, Ohio',
      'Hancock Field, Findlay, Ohio']),
    ('OH-HAN-S-067', 'Koehler Field', 'HAN',
     ['1000 South Blanchard Street, Findlay, Ohio',
      'Koehler Field, Findlay, Ohio']),
    ('OH-HAN-S-069', 'Remington Field', 'HAN',
     ['1827 South Blanchard Street, Findlay, Ohio',
      'Remington Field, Findlay, Ohio']),

    # City of Findlay — other
    ('OH-HAN-S-075', 'Downtown Recreation Area', 'HAN',
     ['Downtown Recreation Area, Findlay, Ohio',
      'Blanchard River Recreation Area, Findlay, Ohio']),
    ('OH-HAN-S-084', 'Lake LeComte (Reservoir 5)', 'HAN',
     ['Lake LeComte, Fostoria, Ohio',
      'Lake LeComte, Hancock County, Ohio']),
    ('OH-HAN-S-101', 'Findlay Reservoir #2 Fishing Area', 'HAN',
     ['Findlay Reservoir 2, Findlay, Ohio',
      'Findlay Reservoir, Hancock County, Ohio']),

    # Township / Village parks
    ('OH-HAN-S-093', 'Van Buren Sportsplex', 'HAN',
     ['12829 Ohio 613, Van Buren, Ohio',
      'Van Buren Sportsplex, Van Buren, Ohio']),
    ('OH-HAN-S-094', 'Hoadley Park', 'HAN',
     ['Hoadley Park, Van Buren, Ohio',
      'Ash Street, Van Buren, Ohio']),

    # Camp Berry (Boy Scout camp)
    ('OH-HAN-S-099', 'Camp Berry', 'HAN',
     ['11716 County Road 40, Findlay, Ohio',
      'Camp Berry, Hancock County, Ohio']),

    # Golf courses
    ('OH-HAN-S-104', 'Red Hawk Run Golf Club', 'HAN',
     ['18441 US Route 224, Findlay, Ohio',
      'Red Hawk Run Golf Club, Findlay, Ohio']),
    ('OH-HAN-S-106', 'Wayside Golf Club', 'HAN',
     ['18125 Ohio 568, Findlay, Ohio',
      'Wayside Golf Club, Findlay, Ohio']),
    ('OH-HAN-S-107', 'Shady Acres Golf Course', 'HAN',
     ['100 Shady Acres, McComb, Ohio',
      'Shady Acres Golf Course, McComb, Ohio']),
    ('OH-HAN-S-108', 'Sycamore Springs Golf Course', 'HAN',
     ['11492 Township Road 25, Arlington, Ohio',
      'Sycamore Springs Golf Course, Arlington, Ohio']),
    ('OH-HAN-S-109', 'Lakeland Golf Course', 'HAN',
     ['3770 County Road 23, Fostoria, Ohio',
      'Lakeland Golf Course, Fostoria, Ohio']),
    ('OH-HAN-S-110', 'Loudon Meadows Golf Club', 'HAN',
     ['11072 W State Route 18, Fostoria, Ohio',
      'Loudon Meadows Golf Club, Fostoria, Ohio']),
    ('OH-HAN-S-112', 'Oak Mallett Golf Club', 'HAN',
     ['15925 Township Road 205, Findlay, Ohio',
      'Oak Mallett Golf Club, Findlay, Ohio']),

    # Cemeteries (many in OSM)
    ('OH-HAN-S-040', 'Baker-Hamlin Cemetery', 'HAN',
     ['Baker Hamlin Cemetery, Hancock County, Ohio',
      'Baker-Hamlin Cemetery, Cass Township, Ohio']),
    ('OH-HAN-S-043', 'Houcktown Cemetery', 'HAN',
     ['Houcktown Cemetery, Ohio',
      'Houcktown Cemetery, Jackson Township, Hancock County, Ohio']),
    ('OH-HAN-S-044', 'Bright Cemetery', 'HAN',
     ['Bright Cemetery, Hancock County, Ohio',
      'Bright Cemetery, Marion Township, Ohio']),
    ('OH-HAN-S-048', 'Portage Township Cemetery', 'HAN',
     ['Portage Township Cemetery, Hancock County, Ohio',
      'Portage Cemetery, Hancock County, Ohio']),
    ('OH-HAN-S-141', 'Frontiers Repose Cemetery', 'HAN',
     ['Frontiers Repose Cemetery, Hancock County, Ohio']),
    ('OH-HAN-S-145', 'High Bank Cemetery', 'HAN',
     ['High Bank Cemetery, Hancock County, Ohio']),
    ('OH-HAN-S-146', 'Indian Grove Cemetery', 'HAN',
     ['Indian Grove Cemetery, Hancock County, Ohio']),
    ('OH-HAN-S-153', 'Maple Lawn Cemetery', 'HAN',
     ['Maple Lawn Cemetery, Hancock County, Ohio']),
    ('OH-HAN-S-157', 'Riley Creek Cemetery', 'HAN',
     ['Riley Creek Cemetery, Hancock County, Ohio']),

    # ===== SAN (Sandusky County — 1 site) =====
    ('OH-SAN-S-008', 'Sandusky County Wildlife Areas', 'SAN',
     ['Sandusky County Wildlife Area, Sandusky County, Ohio']),

    # ===== SC (Scioto County — 2 sites) =====
    ('OH-SC-S-0002', 'Alum Rock', 'SC',
     ['Alum Rock, Scioto County, Ohio',
      'Alum Rock, Ohio']),
    ('OH-SC-S-0028', 'Sciotoville Community Square', 'SC',
     ['Sciotoville Community Square, Portsmouth, Ohio',
      'Harding Avenue, Sciotoville, Ohio']),

    # ===== WOD (Wood County — 20 sites) =====

    # ODNR DOW wildlife areas (likely not in OSM; expect UNRESOLVED)
    ('OH-WOD-SI-003', 'Wood County Wildlife Area 1', 'WOD',
     ['Wood County Wildlife Area 1, Ohio',
      'Wood County Wildlife Area 1, Wood County, Ohio']),
    ('OH-WOD-SI-004', 'Wood County Wildlife Area 2', 'WOD',
     ['Wood County Wildlife Area 2, Ohio',
      'Wood County Wildlife Area 2, Wood County, Ohio']),
    ('OH-WOD-SI-005', 'Wood County Wildlife Area 4', 'WOD',
     ['Wood County Wildlife Area 4, Ohio',
      'Wood County Wildlife Area 4, Wood County, Ohio']),
    ('OH-WOD-SI-006', 'Wood County Wildlife Area 5', 'WOD',
     ['Wood County Wildlife Area 5, Ohio',
      'Wood County Wildlife Area 5, Wood County, Ohio']),
    ('OH-WOD-SI-007', 'Wood County Wildlife Area 6', 'WOD',
     ['Wood County Wildlife Area 6, Ohio',
      'Wood County Wildlife Area 6, Wood County, Ohio']),
    ('OH-WOD-SI-008', 'Wood County Wildlife Area 7', 'WOD',
     ['Wood County Wildlife Area 7, Ohio',
      'Wood County Wildlife Area 7, Wood County, Ohio']),
    ('OH-WOD-SI-009', 'Wood County Wildlife Area 8', 'WOD',
     ['Wood County Wildlife Area 8, Ohio',
      'Wood County Wildlife Area 8, Wood County, Ohio']),
    ('OH-WOD-SI-010', 'Wood County Wildlife Area 9', 'WOD',
     ['Wood County Wildlife Area 9, Ohio',
      'Wood County Wildlife Area 9, Wood County, Ohio']),
    ('OH-WOD-SI-011', 'Wood County Wildlife Area 10', 'WOD',
     ['Wood County Wildlife Area 10, Ohio',
      'Wood County Wildlife Area 10, Wood County, Ohio']),
    ('OH-WOD-SI-012', 'Bairdstown Wildlife Production Area', 'WOD',
     ['Bairdstown Wildlife Production Area, Ohio',
      'Bairdstown Wildlife Area, Wood County, Ohio']),
    ('OH-WOD-SI-013', 'Dry Creek Wildlife Area', 'WOD',
     ['Dry Creek Wildlife Area, Wood County, Ohio',
      'Dry Creek Wildlife Area, Ohio']),
    ('OH-WOD-SI-015', 'Van Tassel Wildlife Area', 'WOD',
     ['Van Tassel Wildlife Area, Wood County, Ohio',
      'Van Tassel Wildlife Area, Ohio']),

    # WOD — other GPS-missing
    ('OH-WOD-SI-029', 'Otsego Park', 'WOD',
     ['20000 W River Road, Bowling Green, Ohio',
      'Otsego Park, Wood County, Ohio']),
    ('OH-WOD-SI-044', 'Dunbridge Road Soccer Fields', 'WOD',
     ['Dunbridge Road Soccer Fields, Bowling Green, Ohio',
      'Bowling Green Municipal Court, Bowling Green, Ohio']),
    ('OH-WOD-SI-058', 'Woodland Park (Perrysburg)', 'WOD',
     ['Woodland Park, Perrysburg, Ohio']),
    ('OH-WOD-SI-061', 'Ed Ford Memorial Park', 'WOD',
     ['Ed Ford Memorial Park, Rossford, Ohio',
      'Elm Street and Dixie Highway, Rossford, Ohio']),
    ('OH-WOD-SI-067', 'Village Park (North Baltimore)', 'WOD',
     ['Village Park, North Baltimore, Ohio',
      'North Baltimore Community Park, North Baltimore, Ohio']),
    ('OH-WOD-SI-073', 'Mishe Monoto Preserve', 'WOD',
     ['Mishe Monoto Preserve, Wood County, Ohio',
      'Mishe Monoto Preserve, Ohio']),
    ('OH-WOD-SI-076', 'Bell Woods Nature Preserve', 'WOD',
     ['4825 Sugar Ridge Road, Pemberville, Ohio',
      'Bell Woods Nature Preserve, Pemberville, Ohio']),
    ('OH-WOD-SI-077', "Pat & Clint Mauk's Prairie", 'WOD',
     ['4825 Sugar Ridge Road, Pemberville, Ohio',
      "Pat Mauk's Prairie, Pemberville, Ohio"]),
]


def nominatim_query(query_str, county_code):
    """Submit one Nominatim query. Returns (lat, lon) if within county bbox, else None."""
    params = {
        'q': query_str,
        'format': 'json',
        'limit': 1,
        'countrycodes': 'us',
        'addressdetails': 0,
    }
    url = 'https://nominatim.openstreetmap.org/search?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent': NOMINATIM_UA})
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            results = json.loads(resp.read())
        time.sleep(RATE_LIMIT)
    except Exception as e:
        time.sleep(RATE_LIMIT)
        print(f'    REQ-ERR: {e}')
        return None

    if not results:
        return None

    r = results[0]
    lat, lon = float(r['lat']), float(r['lon'])
    clat, clon = COUNTY_CENTROIDS[county_code]
    if abs(lat - clat) > BUFFER_DEG or abs(lon - clon) > BUFFER_DEG:
        print(f'    BBOX-REJECT ({lat:.4f},{lon:.4f}) too far from {county_code} centroid')
        return None

    return lat, lon


def acquire_gps(display_name, county_code, queries):
    """Try each query in order. Returns (lat, lon, query_used) or None."""
    for q in queries:
        result = nominatim_query(q, county_code)
        if result:
            return result[0], result[1], q
    return None


def run():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # ---- Pre-flight ----
    print('Pre-flight checks')
    print('-' * 60)

    ids = [t[0] for t in GPS_TARGETS]
    placeholders = ','.join(['?' for _ in ids])
    cur.execute(
        f'SELECT site_id, name, gps_lat FROM sites WHERE site_id IN ({placeholders}) ORDER BY site_id',
        ids
    )
    in_db = {r[0]: r for r in cur.fetchall()}

    missing_from_db = [sid for sid in ids if sid not in in_db]
    if missing_from_db:
        print(f'  WARN: not found in DB: {missing_from_db}')

    already_has_gps = [sid for sid in ids if in_db.get(sid, (None, None, None))[2] not in (None, '')]
    if already_has_gps:
        print(f'  NOTE: already have GPS (will skip): {already_has_gps}')

    cur.execute("SELECT count(*) FROM sites WHERE (gps_lat IS NULL OR gps_lat='') AND site_id NOT LIKE 'OH-MC-%'")
    before_count = cur.fetchone()[0]
    print(f'  GPS-missing (non-MC) before: {before_count}')
    to_attempt = [t for t in GPS_TARGETS if t[0] in in_db and in_db[t[0]][2] in (None, '')]
    print(f'  Sites to attempt: {len(to_attempt)}  (of {len(GPS_TARGETS)} targets; {len(ids) - len(to_attempt)} skipped)')
    print()
    input('Pre-flight OK. Press Enter to start Nominatim queries (Ctrl-C to abort)...')
    print()

    # ---- Acquire GPS via Nominatim ----
    resolved = []    # [(site_id, lat, lon, query_used)]
    unresolved = []  # [site_id]

    for site_id, display_name, county_code, queries in GPS_TARGETS:
        if site_id not in in_db:
            continue
        if in_db[site_id][2] not in (None, ''):
            continue  # already has GPS

        label = f'{site_id}: {display_name[:38]:<38}'
        print(f'  {label}', end='  ', flush=True)

        result = acquire_gps(display_name, county_code, queries)
        if result:
            lat, lon, query_used = result
            print(f'OK  {lat:.6f},{lon:.6f}')
            resolved.append((site_id, lat, lon, query_used))
        else:
            print('UNRESOLVED')
            unresolved.append(site_id)

    print()
    print(f'--- Results ---')
    print(f'  Resolved:   {len(resolved)}')
    print(f'  Unresolved: {len(unresolved)}')
    if unresolved:
        print()
        print('  Unresolved IDs (need ODNR GIS or manual lookup):')
        for sid in unresolved:
            name = in_db[sid][1] if sid in in_db else '???'
            print(f'    {sid}: {name}')

    if not resolved:
        print()
        print('Nothing to commit.')
        conn.close()
        return

    print()
    input(f'Commit {len(resolved)} GPS updates to DB? Press Enter (Ctrl-C to abort)...')
    print()

    # ---- Update DB ----
    updated = 0
    try:
        for site_id, lat, lon, query_used in resolved:
            try:
                plus_code = encode_plus_code(lat, lon)
            except Exception as e:
                plus_code = None
                print(f'    WARN: plus_code failed for {site_id}: {e}')

            cur.execute(
                'UPDATE sites SET gps_lat=?, gps_lon=?, plus_code=?, updated_at=? WHERE site_id=?',
                (lat, lon, plus_code, now, site_id)
            )
            name_short = (in_db[site_id][1] or '')[:35]
            print(f'  Updated {site_id}: {name_short:<35}  {lat},{lon}  plus={plus_code}')
            updated += 1

        conn.commit()
        print()
        print(f'COMMIT OK -- {updated} GPS records updated')

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

    # ---- Post-flight ----
    print()
    print('Post-flight verification')
    print('-' * 60)
    cur.execute("SELECT count(*) FROM sites WHERE (gps_lat IS NULL OR gps_lat='') AND site_id NOT LIKE 'OH-MC-%'")
    after_count = cur.fetchone()[0]
    print(f'  GPS-missing (non-MC) after:  {after_count}  (was {before_count})')
    print(f'  Resolved this run:           {updated}')
    print(f'  Still unresolved:            {len(unresolved)}')

    if unresolved:
        print()
        print('  Unresolved — recommended next steps:')
        wod_wca = [s for s in unresolved if 'WOD' in s and 'Wildlife' in (in_db.get(s, ('','',''))[1] or '')]
        han_wca = [s for s in unresolved if 'HAN' in s and ('Wildlife' in (in_db.get(s, ('','',''))[1] or '') or 'Production' in (in_db.get(s, ('','',''))[1] or ''))]
        other = [s for s in unresolved if s not in wod_wca and s not in han_wca]
        if wod_wca or han_wca:
            print(f'    {len(wod_wca) + len(han_wca)} ODNR DOW wildlife area sites -> ODNR Ohio Lake Map Resource')
            print('      https://experience.arcgis.com/experience/2a39044c75b04e68872564b4c6ec0638')
        if other:
            print(f'    {len(other)} other sites -> manual lookup or SORP parcel data')
            for sid in other:
                name = in_db.get(sid, ('','',''))[1] or '???'
                print(f'      {sid}: {name}')

    conn.close()


if __name__ == '__main__':
    run()
