"""
Stage 4b — GPS Acquisition Prep (Sandusky County)
Populates gps_queries and fallback_gps in the pipeline config.
Sets gps_unresolvable notes for linear/distributed entities.
Sandusky County centroid: 41.350, -83.080 (IMP-081 bounding box check)
"""

import json, yaml, pathlib

CFG_PATH  = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_config.json')
YAML_PATH = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')

cfg      = json.loads(CFG_PATH.read_text(encoding='utf-8'))
raw_data = yaml.safe_load(YAML_PATH.read_text(encoding='utf-8'))
records  = raw_data.get('records', [])

# ── County metadata ──────────────────────────────────────────────────────────
cfg['run_id']   = 'sandusky_ohio_2026_05_21'
cfg['run_date'] = '2026-05-21'
cfg['bbox']     = [41.218, 41.483, -83.267, -82.827]  # Sandusky County bounds
cfg['run_notes'] = (
    'First run — DB was empty at start. '
    '10 held (cross_county_held). '
    'NCIT upserts as OH-MC-T-0110. '
    'GNIS-only cemeteries (T8) expected to be gps_missing -> held.'
)

# ── Build ID -> record map ───────────────────────────────────────────────────
s_idx = t_idx = ts_idx = tn_idx = sn_idx = ap_idx = 0
id_map = {}
for rec in records:
    etype = rec['entity_type']
    if etype == 'Site':
        s_idx += 1; eid = f'SAN-S-{s_idx:03d}'
    elif etype == 'Trail':
        t_idx += 1; eid = f'SAN-T-{t_idx:03d}'
    elif etype == 'Trail Segment':
        ts_idx += 1; eid = f'SAN-TS-{ts_idx:03d}'
    elif etype == 'Trail Network':
        tn_idx += 1; eid = f'SAN-TN-{tn_idx:03d}'
    elif etype == 'Site Network':
        sn_idx += 1; eid = f'SAN-SN-{sn_idx:03d}'
    elif etype == 'Access Point':
        ap_idx += 1; eid = f'SAN-AP-{ap_idx:03d}'
    else:
        continue
    id_map[eid] = rec

HELD = {'SAN-S-003','SAN-S-004','SAN-S-005','SAN-AP-002','SAN-AP-003',
        'SAN-S-079','SAN-S-080','SAN-S-081','SAN-S-105','SAN-S-107'}

# Entities with gps_unresolvable status (linear corridors, distributed tracts)
GPS_UNRESOLVABLE = {
    'SAN-T-001': (
        'GPS unresolvable — 28-mile linear trail corridor through Sandusky County; '
        'no single coordinate represents the entity. Trail runs Elmore to Bellevue. '
        'Determined 2026-05-21.'
    ),
    'SAN-S-008': (
        'GPS unresolvable — Sandusky County Wildlife Areas 1-7 are 7 separate non-adjacent '
        'numbered ODNR tracts; no single coordinate represents the group entity. '
        'Each tract requires individual verification. Determined 2026-05-21.'
    ),
}

# ── fallback_gps — entities with GPS already known from YAML ─────────────────
fallback = {}
for eid, rec in id_map.items():
    if eid in HELD:
        continue
    lat = rec.get('gps_lat_raw')
    lon = rec.get('gps_lon_raw')
    if lat is not None and lon is not None:
        fallback[eid] = [float(lat), float(lon)]

# ── gps_queries — Nominatim query strings ────────────────────────────────────
# Pattern: use street address if available, else name + city/county + Ohio

queries = {}

# Helper: clean up location_raw for geocoding
def addr_query(name, location, fallback_loc='Sandusky County, Ohio'):
    loc = (location or '').strip()
    # Remove trailing parenthetical notes like "(Riley Township)"
    import re
    loc = re.sub(r'\s*\(.*?\)\s*$', '', loc).strip()
    # If location has a recognizable street address format, use it directly
    if loc and any(c.isdigit() for c in loc[:10]):
        # Has a number at start — likely a street address
        if 'ohio' not in loc.lower() and 'oh' not in loc.upper()[-6:]:
            loc += ', Ohio'
        return loc
    elif loc and len(loc) > 10 and 'ohio' not in loc.lower() and 'sandusky' not in loc.lower():
        return f'{name}, {loc}, Ohio'
    elif loc and len(loc) > 10:
        return f'{name}, {loc}'
    else:
        return f'{name}, {fallback_loc}'

def_loc = 'Sandusky County, Ohio'

# T2 State Sites
queries['SAN-S-001'] = ''  # has fallback GPS from YAML
queries['SAN-S-002'] = ''  # has fallback GPS from YAML
queries['SAN-S-006'] = 'Ron Abraham Forest, Sandusky County, Ohio'
queries['SAN-S-007'] = 'Aldrich Pond Wildlife Area, Sandusky County, Ohio'
# SAN-S-008 = gps_unresolvable; no query

# T2 APs
queries['SAN-AP-001'] = 'Pickerel Creek Wildlife Area SR 6 observation deck, Sandusky County, Ohio'
queries['SAN-AP-007'] = '201 Walnut Street, Fremont, Ohio'

# T3 SCPD Sites
queries['SAN-S-009'] = '2134 County Road 260, Vickery, Ohio'
queries['SAN-S-010'] = '2020 Old Oak Harbor Road, Fremont, Ohio'
queries['SAN-S-011'] = '720 South Main Street, Lindsey, Ohio'
queries['SAN-S-012'] = '2700 County Road 259, Fremont, Ohio'
queries['SAN-S-013'] = '1329 Tiffin Street, Fremont, Ohio'
queries['SAN-S-014'] = '3861 County Road 184, Fremont, Ohio'
queries['SAN-S-015'] = 'Green Creek Township Reserve, Sandusky County, Ohio'
queries['SAN-S-016'] = 'Muddy Creek Reserve, Rice Township, Sandusky County, Ohio'
queries['SAN-S-017'] = '1515 County Road 9, Fremont, Ohio'
queries['SAN-S-018'] = '1616 North River Road, Fremont, Ohio'
queries['SAN-S-019'] = 'Ringneck Ridge, 2026 Township Road 74, Gibsonburg, Ohio'
queries['SAN-S-020'] = 'Shelley Wetland, Bellevue, Sandusky County, Ohio'
queries['SAN-S-021'] = '2091 County Road 292, Bellevue, Ohio'
queries['SAN-S-022'] = '2341 County Road 213, Clyde, Ohio'
queries['SAN-S-023'] = '925 South Main Street, Gibsonburg, Ohio'
queries['SAN-S-024'] = '925 South Main Street, Gibsonburg, Ohio'
queries['SAN-S-025'] = '910 South Main Street, Gibsonburg, Ohio'
queries['SAN-S-026'] = '5013 County Road 65, Gibsonburg, Ohio'
queries['SAN-S-027'] = '1330 County Road 66, Gibsonburg, Ohio'
queries['SAN-S-028'] = '2409 South State Route 53, Fremont, Ohio'

# T3 Trails
# SAN-T-001 = NCIT = gps_unresolvable (linear); no query
queries['SAN-T-002'] = '925 South Main Street, Gibsonburg, Ohio'   # White Star Quarry Loop
queries['SAN-T-003'] = '5013 County Road 65, Gibsonburg, Ohio'     # Waggoner's Run MTB

# T3 APs
queries['SAN-AP-004'] = '2091 County Road 292, Bellevue, Ohio'     # NCIT Tea Kaufman
queries['SAN-AP-005'] = '1630 Walter Avenue, Fremont, Ohio'        # NCIT Mosser Park
queries['SAN-AP-006'] = '2409 South State Route 53, Fremont, Ohio' # Wolf Creek Launch

# T5 Township Parks
queries['SAN-S-029'] = '2220 Tiffin Road, Fremont, Ohio'           # Conner Park
queries['SAN-S-030'] = 'Chudzinski-Johannsen Park, Fremont, Ohio'  # Ballville Twp
queries['SAN-S-031'] = 'Hydraulic Square, Fremont, Ohio'           # Ballville Twp
queries['SAN-S-032'] = 'Sandusky Township Park, Fremont, Ohio'     # Sandusky Twp

# T5 Cemeteries with street addresses
queries['SAN-S-033'] = '1225 Oakwood Street, Fremont, Ohio'        # Oakwood Cemetery
queries['SAN-S-034'] = 'Smith Cemetery, Jackson Township, Sandusky County, Ohio'
queries['SAN-S-035'] = 'West Union Cemetery, Gibsonburg, Ohio'
queries['SAN-S-036'] = 'Briar Hill Cemetery, Rice Township, Sandusky County, Ohio'
queries['SAN-S-037'] = 'Greenwood Cemetery, Rice Township, Sandusky County, Ohio'
queries['SAN-S-038'] = 'Hineline Cemetery, Rice Township, Sandusky County, Ohio'
queries['SAN-S-039'] = 'LaPrairie Cemetery, Rice Township, Sandusky County, Ohio'
queries['SAN-S-040'] = 'Faith Lutheran Cemetery, Rice Township, Sandusky County, Ohio'
queries['SAN-S-041'] = '363 North Erlin Road, Fremont, Ohio'       # Beeler Cemetery
queries['SAN-S-042'] = '1800 US Route 6, Fremont, Ohio'            # Faust Cemetery
queries['SAN-S-043'] = 'Schoch Cemetery, County Road 233, Fremont, Ohio'
queries['SAN-S-044'] = 'Green Creek Burial Ground, County Road 265, Fremont, Ohio'
queries['SAN-S-045'] = '2529 Oak Harbor Road, Fremont, Ohio'       # Binkley Cemetery
queries['SAN-S-046'] = '880 County Road 128, Fremont, Ohio'        # Four Mile House Cemetery
queries['SAN-S-047'] = '551 County Road 128, Fremont, Ohio'        # Slates Cemetery
queries['SAN-S-048'] = 'Chestnut Grove Cemetery, US Route 23, Scott Township, Sandusky County, Ohio'
queries['SAN-S-049'] = 'Parkhurst Cemetery, State Route 101, Townsend Township, Sandusky County, Ohio'
queries['SAN-S-050'] = 'Tew Cemetery, State Route 101, Townsend Township, Sandusky County, Ohio'
queries['SAN-S-051'] = 'Lindsey Cemetery, Lindsey, Ohio'
queries['SAN-S-052'] = 'Washington Chapel Cemetery, Washington Township, Sandusky County, Ohio'
queries['SAN-S-053'] = 'Hessville Cemetery, State Route 600, Washington Township, Sandusky County, Ohio'
queries['SAN-S-054'] = 'Westwood Cemetery, State Route 105, Woodville Township, Sandusky County, Ohio'
queries['SAN-S-055'] = 'Woodville Township Cemetery, County Road 30, Woodville, Ohio'
queries['SAN-S-056'] = 'Sugar Creek Cemetery, US Route 20, Woodville, Ohio'
queries['SAN-S-057'] = 'Ellsworth Cemetery, State Route 101, York Township, Sandusky County, Ohio'
queries['SAN-S-058'] = 'Wales Corners Cemetery, County Road 175, York Township, Sandusky County, Ohio'
queries['SAN-S-059'] = 'York Chapel Cemetery, County Road 292, York Township, Sandusky County, Ohio'
queries['SAN-S-060'] = 'Gilbert Cemetery, County Road 177, York Township, Sandusky County, Ohio'
queries['SAN-S-061'] = 'Wickwyre Cemetery, County Road 308, York Township, Sandusky County, Ohio'
queries['SAN-S-062'] = 'Green Creek Township Cemetery, Sandusky County, Ohio'

# T6 Fremont Parks
queries['SAN-S-063'] = '1313 Oak Harbor Road, Fremont, Ohio'
queries['SAN-S-064'] = '601 St Joseph Street, Fremont, Ohio'
queries['SAN-S-065'] = '1400 Birchard Avenue, Fremont, Ohio'
queries['SAN-S-066'] = '1019 Birchard Avenue, Fremont, Ohio'
queries['SAN-S-067'] = '329 Avis Street, Fremont, Ohio'
queries['SAN-S-068'] = 'Corner of State Street and Front Street, Fremont, Ohio'
queries['SAN-S-069'] = '610 Morrison Street, Fremont, Ohio'
queries['SAN-S-070'] = '1111 Tiffin Street, Fremont, Ohio'
queries['SAN-S-071'] = '344 2nd Street, Fremont, Ohio'

# T6 Fremont APs
queries['SAN-AP-008'] = 'End of North Street, Fremont, Ohio'       # Sand Docks
queries['SAN-AP-009'] = 'Miles Newton Bridge, Fremont, Ohio'       # Fishing Access

# T6 Bellevue Parks (GIS_VERIFY_COUNTY — Sandusky primary)
queries['SAN-S-072'] = '110 Cherry Boulevard, Bellevue, Ohio'
queries['SAN-S-073'] = 'Amsden Street Park, Bellevue, Ohio'
queries['SAN-S-074'] = 'Buckingham Drive Park, Bellevue, Ohio'
queries['SAN-S-075'] = 'Ellis Avenue Park, Bellevue, Ohio'
queries['SAN-S-076'] = 'Kern Street Park, Bellevue, Ohio'
queries['SAN-S-077'] = 'Ridge Drive Park, Bellevue, Ohio'
queries['SAN-S-078'] = 'Robert Peters Athletic Field, Bellevue, Ohio'

# T6 Other Municipalities
queries['SAN-S-082'] = '240 South Main Street, Lindsey, Ohio'      # Wendelle Miller Park
queries['SAN-S-083'] = '135 East Cherry Street, Clyde, Ohio'
queries['SAN-S-084'] = '246 South Street, Clyde, Ohio'
queries['SAN-S-085'] = 'Vine Street Park, Clyde, Ohio'
queries['SAN-S-086'] = 'South Main Street at Raccoon Creek Reservoir, Clyde, Ohio'
queries['SAN-S-087'] = 'Mulberry Street at South Street, Clyde, Ohio'
queries['SAN-S-088'] = 'Raccoon Creek Reservoir, South Main Street, Clyde, Ohio'
queries['SAN-S-089'] = '422 East McPherson Highway, Clyde, Ohio'
queries['SAN-S-090'] = 'West Yeasting Street at Gibson Street, Gibsonburg, Ohio'
queries['SAN-S-091'] = 'West Madison Street, Gibsonburg, Ohio'
queries['SAN-S-092'] = 'East Stone Street at North Main Street, Gibsonburg, Ohio'
queries['SAN-S-093'] = 'Silver Rock Park, Township Road 42, Gibsonburg, Ohio'
queries['SAN-T-004'] = 'Silver Rock Park, Gibsonburg, Ohio'
queries['SAN-S-094'] = 'Main Street at Fort Findlay Road, Woodville, Ohio'
queries['SAN-S-095'] = 'Erie Street, Woodville, Ohio'
queries['SAN-S-096'] = 'West First Street, Woodville, Ohio'
queries['SAN-S-097'] = 'Main Street, Woodville, Ohio'              # Limelite Eagle Park
queries['SAN-S-098'] = 'Cemetery Drive, Woodville, Ohio'           # Woodville Cemetery (village)

# T8 Golf Courses
queries['SAN-S-099'] = '3728 West Hayes Avenue, Fremont, Ohio'
queries['SAN-S-100'] = '2340 East State Street, Fremont, Ohio'
queries['SAN-S-101'] = '1959 South Main Street, Clyde, Ohio'
queries['SAN-S-102'] = '4900 County Road 16, Woodville, Ohio'
queries['SAN-S-103'] = '6029 State Route 101 East, Clyde, Ohio'   # Sleepy Hollow (CLOSED)
queries['SAN-S-104'] = '1313 Tiffin Street, Fremont, Ohio'        # River Cliff Golf
queries['SAN-S-106'] = '5690 County Road 237, Clyde, Ohio'        # WR Hunt Club

# T8 GNIS Cemeteries (no addresses — best-effort Nominatim)
queries['SAN-S-108'] = 'County Home Cemetery, Sandusky County, Ohio'
queries['SAN-S-109'] = 'Old Fremont Cemetery, Fremont, Ohio'
queries['SAN-S-110'] = 'Green Springs Cemetery, Green Springs, Ohio'
queries['SAN-S-111'] = 'Reformed Church Cemetery, Bellevue, Ohio'
queries['SAN-S-112'] = 'Saint Ann Cemetery, Sandusky County, Ohio'
queries['SAN-S-113'] = 'Saint Joseph Cemetery, Sandusky County, Ohio'
queries['SAN-S-114'] = 'Saint Lawrence Cemetery, Sandusky County, Ohio'
queries['SAN-S-115'] = "Saint Mary's Cemetery, Sandusky County, Ohio"
queries['SAN-S-116'] = "Saint Paul's Cemetery, Sandusky County, Ohio"
queries['SAN-S-117'] = 'Saint Philomena Cemetery, Sandusky County, Ohio'
queries['SAN-S-118'] = 'Mount Lebanon Cemetery, Sandusky County, Ohio'
queries['SAN-S-119'] = 'Trinity Cemetery, Sandusky County, Ohio'
queries['SAN-S-120'] = 'North Union Cemetery, Sandusky County, Ohio'
queries['SAN-S-121'] = 'Greenlawn Memory Gardens, Sandusky County, Ohio'
queries['SAN-S-122'] = 'Bakertown Cemetery, Sandusky County, Ohio'
queries['SAN-S-123'] = 'Bowlus Cemetery, Sandusky County, Ohio'
queries['SAN-S-124'] = 'Collins Cemetery, Sandusky County, Ohio'
queries['SAN-S-125'] = 'Colwell Cemetery, Sandusky County, Ohio'
queries['SAN-S-126'] = 'Dana Cemetery, Sandusky County, Ohio'
queries['SAN-S-127'] = 'Decker Cemetery, Sandusky County, Ohio'
queries['SAN-S-128'] = 'Fuller Cemetery, Sandusky County, Ohio'
queries['SAN-S-129'] = 'Halters Cemetery, Sandusky County, Ohio'
queries['SAN-S-130'] = 'Hayes Cemetery, Sandusky County, Ohio'
queries['SAN-S-131'] = 'Hill Cemetery, Sandusky County, Ohio'
queries['SAN-S-132'] = 'Hite Cemetery, Sandusky County, Ohio'
queries['SAN-S-133'] = 'Lathrop Cemetery, Sandusky County, Ohio'
queries['SAN-S-134'] = 'Ludwig Cemetery, Sandusky County, Ohio'
queries['SAN-S-135'] = 'McCreary Farm Cemetery, Sandusky County, Ohio'
queries['SAN-S-136'] = 'McGormley Cemetery, Sandusky County, Ohio'
queries['SAN-S-137'] = 'Metzgar Cemetery, Sandusky County, Ohio'
queries['SAN-S-138'] = 'Overmyer Cemetery, Sandusky County, Ohio'
queries['SAN-S-139'] = 'Pember Farm Cemetery, Sandusky County, Ohio'
queries['SAN-S-140'] = 'Quinshan Cemetery, Sandusky County, Ohio'
queries['SAN-S-141'] = 'Shawl Cemetery, Sandusky County, Ohio'
queries['SAN-S-142'] = 'Whittlesey Cemetery, Sandusky County, Ohio'

# ── Write to config ──────────────────────────────────────────────────────────
cfg['gps_queries']  = queries
cfg['fallback_gps'] = fallback

# Mark gps_unresolvable in entity notes
sites_by_id  = {s['site_id']: s for s in cfg['sites']}
trails_by_id = {t['trail_id']: t for t in cfg['trails']}

for eid, note in GPS_UNRESOLVABLE.items():
    if eid in trails_by_id:
        existing = trails_by_id[eid].get('notes', '') or ''
        trails_by_id[eid]['notes'] = (existing + ' | ' if existing else '') + \
            f'GPS_UNRESOLVABLE: {note}'
    elif eid in sites_by_id:
        existing = sites_by_id[eid].get('notes', '') or ''
        sites_by_id[eid]['notes'] = (existing + ' | ' if existing else '') + \
            f'GPS_UNRESOLVABLE: {note}'

CFG_PATH.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding='utf-8')
print(f'GPS prep complete.')
print(f'  fallback_gps entries:  {len(fallback)}')
print(f'  gps_queries entries:   {len([q for q in queries.values() if q])}')
print(f'  gps_unresolvable:      {list(GPS_UNRESOLVABLE.keys())}')
