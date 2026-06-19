"""
Nominatim geocoding for remaining Hardin County cemeteries with no GPS.
Queries OSM Nominatim for each cemetery by name + "Hardin County, Ohio".
Applies high-confidence matches directly; prints uncertain matches for review.
"""
import urllib.request, json, time, sqlite3, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DB = r'D:\users\user1\Documents\CP Projects\Natural Areas Project v6\NASqlite\natural_areas_v6.db'

# Cemeteries with no GPS in DB (as of 2026-06-02 post-upsert)
unresolved = [
    ('OH-HAR-S-008', 'Shanks Cemetery'),
    ('OH-HAR-S-010', 'Ft. McArthur Cemetery'),
    ('OH-HAR-S-025', 'Gunn Cemetery'),
    ('OH-HAR-S-051', 'Briedenbaugh Cemetery'),
    ('OH-HAR-S-052', 'Draper Cemetery'),
    ('OH-HAR-S-054', 'Show Cemetery'),
    ('OH-HAR-S-055', 'Sorgen Cemetery'),
    ('OH-HAR-S-056', 'Hatcher Cemetery'),
    ('OH-HAR-S-059', 'Indian Burial Grounds (Buck Township)'),
    ('OH-HAR-S-065', 'Strahm Cemetery'),
    ('OH-HAR-S-066', 'Craig Cemetery'),
    ('OH-HAR-S-069', 'Vanfleet Cemetery'),
    ('OH-HAR-S-075', 'Jennings Cemetery'),
    ('OH-HAR-S-076', 'Rarey Cemetery'),
    ('OH-HAR-S-077', 'Schurtzer Cemetery'),
    ('OH-HAR-S-078', 'Briggs Cemetery'),
    ('OH-HAR-S-079', 'Glenn Cemetery'),
    ('OH-HAR-S-080', 'Price-Patterson Cemetery'),
    ('OH-HAR-S-081', 'Armorsville Cemetery'),
    ('OH-HAR-S-083', 'Kindle Cemetery'),
    ('OH-HAR-S-086', 'Thorn Cemetery'),
    ('OH-HAR-S-090', 'Fultz Cemetery'),
    ('OH-HAR-S-091', 'Harvey Cemetery'),
    ('OH-HAR-S-092', 'Indian Burial Grounds (McDonald Township)'),
    ('OH-HAR-S-094', 'Poe Cemetery'),
    ('OH-HAR-S-095', 'Chesney Cemetery'),
    ('OH-HAR-S-097', 'Pioneer Cemetery (Kenton)'),
    ('OH-HAR-S-098', 'Osborn Cemetery'),
    ('OH-HAR-S-099', 'Spitzer Cemetery'),
    ('OH-HAR-S-101', 'H. Hemphill Cemetery'),
    ('OH-HAR-S-102', 'Marsh Cemetery'),
    ('OH-HAR-S-105', 'Schneider Cemetery'),
    ('OH-HAR-S-107', 'Wroten Cemetery'),
    ('OH-HAR-S-108', 'Jones Cemetery'),
    ('OH-HAR-S-110', 'Waggoner Cemetery'),
    ('OH-HAR-S-111', 'Wagner Cemetery'),
]

# Hardin County bounding box (roughly): lat 40.35–40.88, lon -84.00 – -83.25
LAT_MIN, LAT_MAX = 40.35, 40.88
LON_MIN, LON_MAX = -84.00, -83.25

def nominatim_search(name):
    """Search Nominatim for cemetery in Hardin County, Ohio."""
    # Try with 'Hardin County Ohio' suffix
    for q in [f'{name}, Hardin County, Ohio', f'{name}, Ohio']:
        url = (
            'https://nominatim.openstreetmap.org/search'
            f'?q={urllib.parse.quote(q)}'
            '&format=json&limit=5&addressdetails=1'
            '&countrycodes=us'
        )
        req = urllib.request.Request(url, headers={
            'User-Agent': 'NaturalAreasProject/6.0 (khebner@hotmail.com)'
        })
        try:
            with urllib.request.urlopen(req, timeout=15) as r:
                results = json.loads(r.read())
        except Exception as e:
            print(f'  [NOMINATIM ERROR] {e}')
            return None

        time.sleep(1.1)  # Nominatim rate limit: 1 req/sec

        for res in results:
            lat = float(res['lat'])
            lon = float(res['lon'])
            if LAT_MIN <= lat <= LAT_MAX and LON_MIN <= lon <= LON_MAX:
                return lat, lon, res.get('display_name', ''), res.get('importance', 0)
    return None


import urllib.parse

matched = []
no_match = []

print(f'Geocoding {len(unresolved)} cemeteries via Nominatim...')
print()

for sid, name in unresolved:
    result = nominatim_search(name)
    if result:
        lat, lon, display, importance = result
        matched.append((sid, name, lat, lon, display))
        print(f'  MATCH  {sid} | {name:<42} | {lat:.6f}, {lon:.6f}')
        print(f'         {display[:80]}')
    else:
        no_match.append((sid, name))
        print(f'  MISS   {sid} | {name}')

print()
print(f'Matched: {len(matched)}')
print(f'No match: {len(no_match)}')

if no_match:
    print('\nUnresolved:')
    for sid, name in no_match:
        print(f'  {sid} | {name}')

# Apply matched GPS to DB
if matched:
    print('\nApplying matched GPS to database...')
    con = sqlite3.connect(DB)
    cur = con.cursor()
    applied = 0
    for sid, name, lat, lon, display in matched:
        cur.execute(
            "UPDATE sites SET gps_lat=?, gps_lon=?, updated_at=datetime('now') WHERE site_id=?",
            (lat, lon, sid)
        )
        if cur.rowcount:
            applied += 1
            print(f'  Applied {sid} | {name} | {lat:.6f}, {lon:.6f}')
    con.commit()
    con.close()
    print(f'\nApplied GPS to {applied} sites in DB.')
