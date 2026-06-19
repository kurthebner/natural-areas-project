"""
GPS Pass 2 — Alternate queries for key null entities (IMP-081 fallback protocol).
Tries name + city, name + county as alternates for rural county road addresses.
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

# Key nulls with alternate queries (IMP-081 fallback: name + city OR name + county)
RETRY_QUERIES = {
    'SAN-S-012': [
        'Decoy Marsh, Fremont, Ohio',
        'Decoy Marsh, Sandusky County, Ohio',
    ],
    'SAN-S-014': [
        'Franklin Rosa Wildlife Preserve, Fremont, Ohio',
        'Rosa Wildlife Preserve, Sandusky County, Ohio',
    ],
    'SAN-S-015': [
        'Green Creek Reserve, Clyde, Ohio',
        'Green Creek Township Park, Sandusky County, Ohio',
    ],
    'SAN-S-016': [
        'Muddy Creek Reserve, Fremont, Ohio',
        'Muddy Creek Reserve, Sandusky County, Ohio',
    ],
    'SAN-S-017': [
        'Mull Covered Bridge, Fremont, Ohio',
        'Mull Covered Bridge, Sandusky County, Ohio',
    ],
    'SAN-S-019': [
        'Ringneck Ridge, Gibsonburg, Ohio',
        'Ringneck Ridge, Sandusky County, Ohio',
    ],
    'SAN-S-020': [
        'Shelley Wetland, Bellevue, Ohio',
        'Shelley Wetland, Sandusky County, Ohio',
    ],
    'SAN-S-021': [
        'Tea Kaufman Homestead, Bellevue, Ohio',
        'Tea Kaufman Homestead, Sandusky County, Ohio',
    ],
    'SAN-S-026': [
        'White Star Barn, Gibsonburg, Ohio',
        '5013 Township Road 65, Gibsonburg, Ohio',
    ],
    'SAN-S-027': [
        'Doug Haubert Wetland, Gibsonburg, Ohio',
        'Doug Haubert Wetland, Sandusky County, Ohio',
    ],
    'SAN-S-028': [
        'Wolf Creek Park, Fremont, Ohio',
        'Wolf Creek Park, Sandusky County, Ohio',
    ],
    'SAN-T-003': [
        "Waggoner's Run Trail, Gibsonburg, Ohio",
        "Waggoner's Run, Sandusky County, Ohio",
    ],
    'SAN-AP-004': [
        'Tea Kaufman Homestead Access, Bellevue, Ohio',
        '2091 CR 292, Bellevue, Sandusky County, Ohio',
    ],
    'SAN-AP-005': [
        '1630 Walter Avenue, Fremont, Ohio',
        'Mosser Park, Fremont, Ohio',
    ],
    'SAN-AP-006': [
        'Wolf Creek Park canoe launch, Fremont, Ohio',
        '2409 SR 53, Fremont, Sandusky County, Ohio',
    ],
    'SAN-AP-008': [
        'Sand Docks, Fremont, Ohio',
        'Sandusky River boat launch, North Street, Fremont, Ohio',
    ],
    'SAN-AP-009': [
        'Miles Newton Bridge, Fremont, Ohio',
        'Sandusky River fishing access, downtown Fremont, Ohio',
    ],
    # Fremont parks that were null
    'SAN-S-029': [
        'Conner Park, Fremont, Ohio',
        '2220 Tiffin Road, Fremont, Sandusky County, Ohio',
    ],
    'SAN-S-030': [
        'Tindall Bridge Park, Fremont, Ohio',
        'Chudzinski Johannsen Park, Fremont, Ohio',
    ],
    'SAN-S-031': [
        'Hydraulic Square Park, Fremont, Ohio',
        'Ballville Township Park, Fremont, Ohio',
    ],
    'SAN-S-032': [
        'Sandusky Township Park, Oak Harbor Road, Fremont, Ohio',
        'Sandusky Township recreational park, Sandusky County, Ohio',
    ],
    'SAN-S-033': [
        '1225 Oakwood Street, Fremont, Sandusky County, Ohio',
        'Oakwood Cemetery Fremont Ohio',
    ],
    # Clyde parks
    'SAN-S-085': [
        'Gus Wolf Park, Clyde, Ohio',
        'Vine Street Park, Clyde, Sandusky County, Ohio',
    ],
    'SAN-S-086': [
        'Hendricks Park, Clyde, Ohio',
        'Raccoon Creek Reservoir park, Clyde, Ohio',
    ],
    'SAN-S-087': [
        'Paden Park, Clyde, Ohio',
        'Mulberry Street park, Clyde, Sandusky County, Ohio',
    ],
    'SAN-S-088': [
        'Raccoon Creek Reservoir, Clyde, Ohio',
        'Raccoon Creek Reservoir Sandusky County Ohio',
    ],
    # Gibsonburg parks
    'SAN-S-090': [
        'Central Park, Gibsonburg, Ohio',
        'Gibsonburg central park Ohio',
    ],
    'SAN-S-092': [
        'Williams Park, Gibsonburg, Ohio',
        'Gibsonburg Williams Park Ohio',
    ],
    'SAN-S-093': [
        'Silver Rock Park, Gibsonburg, Ohio',
        'Silver Rock Park Sandusky County Ohio',
    ],
    'SAN-T-004': [
        'Silver Rock Park trail, Gibsonburg, Ohio',
        'Silver Rock Park, Sandusky County, Ohio',
    ],
    # Woodville parks
    'SAN-S-094': [
        'Busdiecker Park, Woodville, Ohio',
        'Fort Findlay Road and Main Street, Woodville, Sandusky County, Ohio',
    ],
    'SAN-S-096': [
        'Veterans Park, Woodville, Ohio',
        'First Street park, Woodville, Ohio',
    ],
    'SAN-S-097': [  # was OOB — retrying with county-anchored query
        'Limelite Eagle Park, Woodville, Sandusky County, Ohio',
        'US Route 20, Woodville, Ohio 43469',
    ],
    'SAN-S-098': [
        'Woodville Cemetery, Cemetery Drive, Woodville, Ohio',
        'Woodville Municipal Cemetery, Sandusky County, Ohio',
    ],
    # Golf courses
    'SAN-S-099': [
        'Sycamore Hills Golf Club, Fremont, Ohio',
        'Sycamore Hills Golf Course, Sandusky County, Ohio',
    ],
    'SAN-S-102': [
        'Hidden Hills Golf Club, Woodville, Ohio',
        'Hidden Hills Golf Course, Sandusky County, Ohio',
    ],
    'SAN-S-103': [
        'Sleepy Hollow Golf Course, Clyde, Ohio',
        '6029 State Route 101, Clyde, Sandusky County, Ohio',
    ],
    # Cemeteries still null
    'SAN-S-041': [
        'Beeler Cemetery, Fremont, Ohio',
        'North Erlin Road cemetery, Fremont, Ohio',
    ],
    'SAN-S-043': [
        'Schoch Cemetery, Fremont, Ohio',
        'Schoch Cemetery, Sandusky County, Ohio',
    ],
    'SAN-S-044': [
        'Green Creek Burial Ground, Riley Township, Sandusky County, Ohio',
        'Green Creek burial ground cemetery Ohio',
    ],
    'SAN-S-046': [
        'Four Mile House Cemetery, Sandusky County, Ohio',
        'Four Mile House Cemetery, Fremont, Ohio',
    ],
    'SAN-S-047': [
        'Slates Cemetery, Fremont, Ohio',
        'Slates Cemetery, Sandusky County, Ohio',
    ],
    'SAN-S-048': [
        'Chestnut Grove Cemetery, Fremont, Ohio',
        'Chestnut Grove Cemetery Ohio',
    ],
    'SAN-S-049': [
        'Parkhurst Cemetery, Sandusky County, Ohio',
        'Parkhurst Cemetery, Bellevue, Ohio',
    ],
    'SAN-S-050': [
        'Tew Cemetery, Sandusky County, Ohio',
        'Tew Cemetery, Bellevue, Ohio',
    ],
    'SAN-S-052': [
        'Washington Chapel Cemetery, Sandusky County, Ohio',
        'Washington Chapel Cemetery, Lindsey, Ohio',
    ],
    'SAN-S-053': [
        'Hessville Cemetery, Sandusky County, Ohio',
        'Hessville Cemetery, Ohio',
    ],
    'SAN-S-054': [
        'Westwood Cemetery, Woodville, Ohio',
        'Westwood Cemetery, Sandusky County, Ohio',
    ],
    'SAN-S-055': [
        'Woodville Township Cemetery, Woodville, Ohio',
        'Woodville Township Cemetery, Sandusky County, Ohio',
    ],
    'SAN-S-056': [
        'Sugar Creek Cemetery, Woodville, Ohio',
        'Sugar Creek Cemetery, Sandusky County, Ohio',
    ],
    'SAN-S-057': [
        'Ellsworth Cemetery, Fremont, Ohio',
        'Ellsworth Cemetery, Sandusky County, Ohio',
    ],
    'SAN-S-058': [
        'Wales Corners Cemetery, Sandusky County, Ohio',
        'Wales Corners Cemetery, Ohio',
    ],
    'SAN-S-059': [
        'York Chapel Cemetery, Sandusky County, Ohio',
        'York Chapel Cemetery, York Township, Ohio',
    ],
    'SAN-S-060': [
        'Gilbert Cemetery, York Township, Ohio',
        'Gilbert Cemetery, Sandusky County, Ohio',
    ],
    'SAN-S-061': [
        'Wickwyre Cemetery, York Township, Ohio',
        'Wickwyre Cemetery, Sandusky County, Ohio',
    ],
    'SAN-S-068': [
        'State Street and Front Street park, Fremont, Ohio',
        'Tschumy Corner, Fremont, Ohio',
    ],
    # Bellevue parks (more specific queries)
    'SAN-S-073': [
        'Amsden Park, Bellevue, Ohio',
        'Amsden Street, Bellevue, Sandusky County, Ohio',
    ],
    'SAN-S-074': [
        'Buckingham Park, Bellevue, Ohio',
        'Buckingham Drive park, Bellevue, Ohio',
    ],
    'SAN-S-075': [
        'Ellis Park, Bellevue, Ohio',
        'Ellis Avenue park, Bellevue, Ohio',
    ],
    'SAN-S-077': [
        'Ridge Park, Bellevue, Ohio',
        'Ridge Drive park, Bellevue, Ohio',
    ],
    'SAN-S-078': [
        'Robert Peters Athletic Field, Bellevue, Ohio',
        'Greenwood Heights athletic field, Bellevue, Ohio',
    ],
}

log_lines = [
    '=== PASS 2 RESULTS ===',
    f'Entities in fallback_gps at start of pass 2: {len(fallback_gps)}',
]

acquired = 0
still_null = 0

for eid, alt_queries in RETRY_QUERIES.items():
    if eid in fallback_gps:
        log_lines.append(f'ALREADY_KNOWN|{eid}|skip')
        continue

    found = False
    for q in alt_queries:
        lat, lon = nominatim_geocode(q)
        time.sleep(NOMINATIM_DELAY)
        if lat is not None and within_county(lat, lon):
            fallback_gps[eid] = [round(lat, 6), round(lon, 6)]
            log_lines.append(f'ACCEPTED_P2|{eid}|{q}|{lat},{lon}')
            print(f'  OK P2    {eid}: ({lat:.4f}, {lon:.4f}) — {q[:60]}')
            acquired += 1
            found = True
            break
        elif lat is not None:
            log_lines.append(f'OOB_P2|{eid}|{q}|{lat},{lon}')
            print(f'  OOB P2   {eid}: ({lat:.4f}, {lon:.4f}) — {q[:55]}')
        else:
            log_lines.append(f'NULL_P2|{eid}|{q}|')
            print(f'  NULL P2  {eid}: {q[:65]}')

    if not found:
        still_null += 1

cfg['fallback_gps'] = fallback_gps
CFG_PATH.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding='utf-8')

log_path_content = LOG_PATH.read_text(encoding='utf-8')
LOG_PATH.write_text(log_path_content + '\n' + '\n'.join(log_lines) + '\n', encoding='utf-8')

print()
print(f'Pass 2 complete:')
print(f'  Additional acquired: {acquired}')
print(f'  Still null:          {still_null}')
print(f'  Total in fallback_gps: {len(fallback_gps)}')
