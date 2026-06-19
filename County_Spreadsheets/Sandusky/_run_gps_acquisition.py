"""
Standalone GPS batch acquisition for Sandusky County.
Calls Nominatim for each entity in gps_queries.
Validates against county bounding box (IMP-081).
Writes accepted results to fallback_gps in the config.
Writes rejected/null results to a separate log.

Sandusky County, Ohio:
  bbox: lat 41.218-41.483, lon -83.267 to -82.827
  centroid: 41.350, -83.080
  buffer: 0.35 deg (~25 mi)
"""

import json, time, pathlib
import urllib.request, urllib.parse

CFG_PATH = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_config.json')
LOG_PATH = pathlib.Path('County_Spreadsheets/Sandusky/_gps_acquisition_log.txt')

COUNTY_CENTROID = (41.350, -83.080)
BUFFER_DEG      = 0.35
NOMINATIM_URL   = 'https://nominatim.openstreetmap.org/search'
NOMINATIM_DELAY = 1.15   # seconds (Nominatim policy: max 1 req/sec)
USER_AGENT      = 'NaturalAreasProject/5.0 (research; khebner@hotmail.com)'

cfg = json.loads(CFG_PATH.read_text(encoding='utf-8'))
gps_queries  = cfg.get('gps_queries', {})
fallback_gps = dict(cfg.get('fallback_gps', {}))   # start with known GPS

def within_county(lat, lon):
    return (abs(lat - COUNTY_CENTROID[0]) <= BUFFER_DEG and
            abs(lon - COUNTY_CENTROID[1]) <= BUFFER_DEG)

def nominatim_geocode(query):
    if not query:
        return None, None
    params = urllib.parse.urlencode({
        'q': query, 'format': 'json', 'limit': 1,
        'countrycodes': 'us',
    })
    url = f'{NOMINATIM_URL}?{params}'
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
        if data:
            return float(data[0]['lat']), float(data[0]['lon'])
    except Exception as e:
        return None, None
    return None, None

log_lines = []
acquired = 0
rejected_oob = 0
rejected_null = 0
already_known = 0

# Entities that already have GPS in fallback_gps (from YAML)
preloaded = set(fallback_gps.keys())

print(f'Starting GPS batch acquisition: {len(gps_queries)} entities')
print(f'Pre-loaded: {len(preloaded)} (from YAML GPS)')

for eid, query in gps_queries.items():
    if eid in preloaded:
        already_known += 1
        log_lines.append(f'PRELOADED|{eid}|{query}|{fallback_gps[eid]}')
        continue

    if not query:
        log_lines.append(f'NO_QUERY|{eid}||')
        continue

    lat, lon = nominatim_geocode(query)
    time.sleep(NOMINATIM_DELAY)

    if lat is None:
        rejected_null += 1
        log_lines.append(f'NULL|{eid}|{query}|')
        print(f'  NULL     {eid}: {query[:60]}')
    elif not within_county(lat, lon):
        rejected_oob += 1
        log_lines.append(f'OOB|{eid}|{query}|{lat},{lon}')
        print(f'  OOB      {eid}: ({lat:.4f}, {lon:.4f}) — {query[:55]}')
    else:
        fallback_gps[eid] = [round(lat, 6), round(lon, 6)]
        acquired += 1
        log_lines.append(f'ACCEPTED|{eid}|{query}|{lat},{lon}')
        print(f'  OK       {eid}: ({lat:.4f}, {lon:.4f}) — {query[:55]}')

# Write results back to config
cfg['fallback_gps'] = fallback_gps
CFG_PATH.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding='utf-8')
LOG_PATH.write_text('\n'.join(log_lines) + '\n', encoding='utf-8')

print()
print(f'GPS acquisition complete:')
print(f'  Acquired:       {acquired}')
print(f'  Pre-loaded:     {already_known}')
print(f'  Null (no hit):  {rejected_null}')
print(f'  Out of bounds:  {rejected_oob}')
print(f'  Total in fallback_gps: {len(fallback_gps)}')
