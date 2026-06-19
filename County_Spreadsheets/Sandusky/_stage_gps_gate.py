"""
GPS Gate — Stage 2c (Sites) + Stage 2d (APs) for Sandusky County.
- Copies fallback_gps coordinates into entity records
- Sets gps_unresolvable=True for linear corridors / distributed groups
- Holds all active entities without GPS as gps_missing
"""

import json, pathlib

CFG_PATH = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_config.json')

cfg = json.loads(CFG_PATH.read_text(encoding='utf-8'))
fps = cfg.get('fallback_gps', {})
sites  = cfg.get('sites', [])
trails = cfg.get('trails', [])
aps    = cfg.get('access_points', [])

gps_filled           = 0
gps_unresolvable_ct  = 0
gps_missing_held     = []
already_held         = 0

def is_gps_unresolvable(record):
    return 'GPS_UNRESOLVABLE' in (record.get('notes') or '')

def is_held(record):
    sf = record.get('status_flag') or ''
    if sf.startswith('HELD'):
        return True
    # APs encode hold in notes
    notes = record.get('notes') or ''
    return 'HELD' in notes and ('cross_county_held' in notes or 'gps_missing' in notes)


# --- Sites ---
for site in sites:
    eid = site['site_id']
    if is_held(site):
        already_held += 1
        continue
    if is_gps_unresolvable(site):
        site['gps_unresolvable'] = True
        gps_unresolvable_ct += 1
        print(f'  UNRESOLVABLE  {eid}: {site["name"][:55]}')
        continue
    if eid in fps:
        lat, lon = fps[eid]
        site['gps_lat']        = lat
        site['gps_lon']        = lon
        site['gps_confidence'] = 'geocoded_nominatim'
        gps_filled += 1
    else:
        site['status_flag'] = 'HELD'
        site['hold_detail'] = 'gps_missing'
        gps_missing_held.append(eid)
        print(f'  HELD gps_miss {eid}: {site["name"][:55]}')

# --- Trails ---
for trail in trails:
    eid = trail['trail_id']
    if is_held(trail):
        already_held += 1
        continue
    if is_gps_unresolvable(trail):
        trail['gps_unresolvable'] = True
        gps_unresolvable_ct += 1
        print(f'  UNRESOLVABLE  {eid}: {trail["name"][:55]}')
        continue
    if eid in fps:
        lat, lon = fps[eid]
        trail['gps_lat']        = lat
        trail['gps_lon']        = lon
        trail['gps_confidence'] = 'geocoded_nominatim'
        gps_filled += 1
    else:
        trail['status_flag'] = 'HELD'
        trail['hold_detail'] = 'gps_missing'
        gps_missing_held.append(eid)
        print(f'  HELD gps_miss {eid}: {trail["name"][:55]}')

# --- Access Points ---
for ap in aps:
    eid = ap['access_point_id']
    if is_held(ap):
        already_held += 1
        continue
    if is_gps_unresolvable(ap):
        ap['gps_unresolvable'] = True
        gps_unresolvable_ct += 1
        print(f'  UNRESOLVABLE  {eid}: {ap["name"][:55]}')
        continue
    if eid in fps:
        lat, lon = fps[eid]
        ap['gps_lat']        = lat
        ap['gps_lon']        = lon
        ap['gps_confidence'] = 'geocoded_nominatim'
        gps_filled += 1
    else:
        ap['status_flag'] = 'HELD'
        ap['hold_detail'] = 'gps_missing'
        gps_missing_held.append(eid)
        print(f'  HELD gps_miss {eid}: {ap["name"][:55]}')

cfg['sites']         = sites
cfg['trails']        = trails
cfg['access_points'] = aps
CFG_PATH.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding='utf-8')

print()
print('GPS Gate complete:')
print(f'  GPS filled (coordinates copied):  {gps_filled}')
print(f'  GPS_UNRESOLVABLE (pass gate):     {gps_unresolvable_ct}')
print(f'  Held for gps_missing:             {len(gps_missing_held)}')
print(f'  Already held (skipped):           {already_held}')
print()
print('Entities held for gps_missing:')
for eid in gps_missing_held:
    print(f'  {eid}')
