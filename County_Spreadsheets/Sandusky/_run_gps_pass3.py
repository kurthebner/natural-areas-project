"""
GPS Pass 3 — Corrected addresses from SCPD website + targeted park lookups.
"""

import json, time, pathlib
import urllib.request, urllib.parse

CFG_PATH = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_config.json')
LOG_PATH = pathlib.Path('County_Spreadsheets/Sandusky/_gps_acquisition_log.txt')

COUNTY_CENTROID = (41.350, -83.080)
BUFFER_DEG      = 0.35
NOMINATIM_URL   = 'https://nominatim.openstreetmap.org/search'
NOMINATIM_DELAY = 1.15
USER_AGENT      = 'NaturalAreasProject/5.0 (research; khebner@hotmail.com)'

cfg = json.loads(CFG_PATH.read_text(encoding='utf-8'))
fallback_gps = dict(cfg.get('fallback_gps', {}))

def within_county(lat, lon):
    return (abs(lat - COUNTY_CENTROID[0]) <= BUFFER_DEG and
            abs(lon - COUNTY_CENTROID[1]) <= BUFFER_DEG)

def nominatim_geocode(query):
    if not query:
        return None, None
    params = urllib.parse.urlencode({'q': query, 'format': 'json', 'limit': 1, 'countrycodes': 'us'})
    req = urllib.request.Request(f'{NOMINATIM_URL}?{params}', headers={'User-Agent': USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
        if data:
            return float(data[0]['lat']), float(data[0]['lon'])
    except:
        return None, None
    return None, None

# Corrected and additional queries based on SCPD website data
PASS3_QUERIES = {
    'SAN-S-012': [
        '2770 County Road 259, Fremont, Ohio',      # corrected from 2700
        '2770 CR 259, Fremont, Sandusky County, Ohio',
    ],
    'SAN-S-014': [
        '3861 CR 184, Fremont, Sandusky County, Ohio',
        'Franklin and Phillip Rose Wildlife Area, Fremont, Ohio',
    ],
    'SAN-S-019': [
        '1818 Township Road 74, Gibsonburg, Ohio',  # confirmed address
        '2026 Township Road 74, Gibsonburg, Ohio',
    ],
    'SAN-S-020': [
        'CR 292 and Township Road 177, Bellevue, Ohio',
        'County Road 292 at Township Road 177, Sandusky County, Ohio',
    ],
    'SAN-S-021': [
        'County Road 292, Bellevue, Sandusky County, Ohio',
        '2091 CR 292, Bellevue, Ohio',
    ],
    'SAN-AP-005': [
        '1630 Walter Avenue, Fremont, Sandusky County, Ohio',
        'Mosser Park, 1630 Walter Avenue, Fremont, Ohio',
    ],
    'SAN-AP-008': [
        'North Street boat ramp, Fremont, Ohio',
        '600 North Street, Fremont, Ohio',
    ],
    'SAN-AP-009': [
        'Miles Newton Bridge fishing access, Sandusky River, Fremont, Ohio',
        'State Street, Fremont, Sandusky County, Ohio',
    ],
    'SAN-S-029': [
        '2220 Tiffin Road, Fremont, Sandusky County, Ohio',
        'Tiffin Road park, Fremont, Ohio',
    ],
    'SAN-S-033': [
        'Oakwood Cemetery, Fremont, Ohio',
        'Oakwood Cemetery, Sandusky County, Ohio',
    ],
    'SAN-S-085': [
        'Vine Street, Clyde, Sandusky County, Ohio',
        'Gus Wolf Park, Vine Street, Clyde, Ohio',
    ],
    'SAN-S-090': [
        'Central Park Gibsonburg Ohio',
        'Gibsonburg village park Ohio',
    ],
    'SAN-S-093': [
        'Silver Rock Park, west of Gibsonburg, Ohio',
        'Township Road 42 Gibsonburg Ohio',
    ],
    'SAN-T-004': [
        'Silver Rock Park, west of Gibsonburg, Sandusky County, Ohio',
        'Silver Rock Quarry trail Ohio',
    ],
    'SAN-S-094': [
        'US Route 20 at Fort Findlay Road, Woodville, Ohio',
        'Woodville Ohio US 20 park',
    ],
    'SAN-S-096': [
        'Veterans Park, Woodville, Ohio',
        'West First Street, Woodville, Sandusky County, Ohio',
    ],
    'SAN-S-097': [
        'Woodville Ohio 43469 US Route 20',
        '43 West Main Street, Woodville, Ohio',
    ],
    'SAN-S-098': [
        'Woodville Cemetery, County Road 907, Woodville, Ohio',
        'Woodville Ohio cemetery',
    ],
    'SAN-S-099': [
        'Sycamore Hills Golf, 3728 West Hayes Avenue, Fremont, Ohio',
        '3728 W Hayes Ave Fremont OH',
    ],
    'SAN-S-102': [
        'Hidden Hills Golf, County Road 16, Woodville, Ohio',
        'CR 16 Woodville Ohio golf',
    ],
    'SAN-S-103': [
        'Sleepy Hollow Golf, 6029 State Route 101 East, Clyde, Ohio',
        '6029 SR 101 E Clyde Ohio',
    ],
    'SAN-S-030': [
        'Tindall Bridge Park, Fremont, Ohio',
        'Sandusky River park, Tindall Road, Fremont, Ohio',
    ],
    'SAN-S-031': [
        'Hydraulic Square, Ballville, Fremont, Ohio',
        'Fremont Ohio Ballville park',
    ],
    'SAN-S-041': [
        'Beeler Cemetery, Erlin Road, Fremont, Ohio',
        'Beeler Cemetery Ohio',
    ],
    'SAN-S-044': [
        'Green Creek Burial Ground, County Road 265, Fremont, Ohio',
        'Riley Township cemetery, Fremont, Ohio',
    ],
    'SAN-S-046': [
        'Four Mile House Cemetery, County Road 128, Fremont, Ohio',
        'Four Mile House Cemetery Ohio',
    ],
    'SAN-S-047': [
        'Slates Cemetery, County Road 128, Fremont, Ohio',
        'Slates Cemetery Ohio',
    ],
    'SAN-S-055': [
        'Woodville Township Cemetery, Lime Road, Woodville, Ohio',
        'Woodville Township Cemetery Ohio',
    ],
    'SAN-S-056': [
        'Sugar Creek Cemetery, Woodville, Ohio',
        'Sugar Creek Cemetery Sandusky County Ohio',
    ],
    'SAN-S-058': [
        'Wales Corners Cemetery, York Township, Ohio',
        'Wales Corners Ohio cemetery',
    ],
    'SAN-S-061': [
        'Wickwyre Cemetery, Ohio',
        'Wickwyre Cemetery York Township Ohio',
    ],
}

log_lines = ['\n=== PASS 3 RESULTS ===']
acquired = 0
still_null = 0

for eid, queries in PASS3_QUERIES.items():
    if eid in fallback_gps:
        log_lines.append(f'ALREADY_KNOWN|{eid}')
        continue

    found = False
    for q in queries:
        lat, lon = nominatim_geocode(q)
        time.sleep(NOMINATIM_DELAY)
        if lat is not None and within_county(lat, lon):
            fallback_gps[eid] = [round(lat, 6), round(lon, 6)]
            log_lines.append(f'ACCEPTED_P3|{eid}|{q}|{lat},{lon}')
            print(f'  OK P3    {eid}: ({lat:.4f}, {lon:.4f}) -- {q[:60]}')
            acquired += 1
            found = True
            break
        elif lat is not None:
            log_lines.append(f'OOB_P3|{eid}|{q}|{lat},{lon}')
            print(f'  OOB P3   {eid}: ({lat:.4f}, {lon:.4f}) -- {q[:55]}')
        else:
            log_lines.append(f'NULL_P3|{eid}|{q}')
            print(f'  NULL P3  {eid}: {q[:65]}')

    if not found:
        still_null += 1

cfg['fallback_gps'] = fallback_gps
CFG_PATH.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding='utf-8')
log_text = LOG_PATH.read_text(encoding='utf-8')
LOG_PATH.write_text(log_text + '\n'.join(log_lines) + '\n', encoding='utf-8')

print()
print(f'Pass 3 complete:')
print(f'  Additional acquired: {acquired}')
print(f'  Still null:          {still_null}')
print(f'  Total in fallback_gps: {len(fallback_gps)}')
