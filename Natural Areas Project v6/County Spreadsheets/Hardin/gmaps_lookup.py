"""
Use Google Maps Geocoding API via Nominatim structured search
to find cemetery coordinates. Falls back to checking if Google
Maps place URL coordinates are within Hardin County bounds.
"""
import urllib.request, urllib.parse, json, time, re

LAT_MIN, LAT_MAX = 40.39, 40.93
LON_MIN, LON_MAX = -84.02, -83.26

cemeteries = [
    ('OH-HAR-S-008', 'Shanks Cemetery'),
    ('OH-HAR-S-025', 'Gunn Cemetery'),       # already tried - miss
    ('OH-HAR-S-046', 'Hickory Grove Cemetery'),
    ('OH-HAR-S-047', 'Grassy Point Cemetery'),
    ('OH-HAR-S-051', 'Briedenbaugh Cemetery'),
    ('OH-HAR-S-052', 'Draper Cemetery'),
    ('OH-HAR-S-054', 'Show Cemetery'),
    ('OH-HAR-S-055', 'Sorgen Cemetery'),
    ('OH-HAR-S-056', 'Hatcher Cemetery'),
]

# Try Nominatim with state + county constraint
headers = {'User-Agent': 'NaturalAreasProject/6.0 khebner@hotmail.com'}

for sid, name in cemeteries:
    # Try with viewbox constraint to Hardin County
    params = urllib.parse.urlencode({
        'q': name,
        'format': 'json',
        'limit': 5,
        'countrycodes': 'us',
        'viewbox': f'{LON_MIN},{LAT_MIN},{LON_MAX},{LAT_MAX}',
        'bounded': 1,
    })
    url = f'https://nominatim.openstreetmap.org/search?{params}'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        hits = [d for d in data if float(d['lat']) >= LAT_MIN and float(d['lat']) <= LAT_MAX
                and float(d['lon']) >= LON_MIN and float(d['lon']) <= LON_MAX]
        if hits:
            h = hits[0]
            print(f'  HIT  {sid} | {name:<35} | {h["lat"]}, {h["lon"]} | {h["display_name"][:60]}')
        else:
            print(f'  MISS {sid} | {name}')
    except Exception as e:
        print(f'  ERR  {sid} | {name} | {e}')
    time.sleep(1.1)
