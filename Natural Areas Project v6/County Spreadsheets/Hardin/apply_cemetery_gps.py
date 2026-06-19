import json

# 32 clean matches from OSM + confirmed Woodlawn old
clean_matches = [
    ('OH-HAR-S-009', 40.7180503, -83.6584242),  # Cessna Cemetery
    ('OH-HAR-S-011', 40.7241547, -83.5608422),  # Grant Cemetery
    ('OH-HAR-S-012', 40.74610,   -83.82280),    # Woodlawn Cemetery (confirmed address match)
    ('OH-HAR-S-016', 40.7842186, -83.9618874),  # Hall Cemetery
    ('OH-HAR-S-017', 40.560505,  -83.8336339),  # Roundhead Cemetery (Old)
    ('OH-HAR-S-018', 40.5608266, -83.8298368),  # Roundhead Cemetery (New)
    ('OH-HAR-S-019', 40.587193,  -83.8419431),  # Henkle/Hinkle Cemetery
    ('OH-HAR-S-020', 40.7799846, -83.6750413),  # Dola Cemetery
    ('OH-HAR-S-023', 40.7873209, -83.5283663),  # Patterson Cemetery
    ('OH-HAR-S-024', 40.8047708, -83.5547599),  # Hueston Cemetery
    ('OH-HAR-S-026', 40.598399,  -83.6730231),  # Norman Cemetery
    ('OH-HAR-S-027', 40.5543972, -83.6540682),  # Seig Cemetery (OSM: Sieg)
    ('OH-HAR-S-028', 40.5386436, -83.7193764),  # Yelverton Cemetery (OSM: Sloan-Yelverton)
    ('OH-HAR-S-048', 40.7561966, -83.8618491),  # Saint Johns Cemetery
    ('OH-HAR-S-053', 40.476652,  -83.8418741),  # Fry Cemetery
    ('OH-HAR-S-057', 40.5934592, -83.5685402),  # Lynn Grove Cemetery
    ('OH-HAR-S-063', 40.7227003, -83.7630742),  # Huntersville Cemetery
    ('OH-HAR-S-067', 40.7426686, -83.9363853),  # Fisher Cemetery
    ('OH-HAR-S-070', 40.5837391, -83.5043317),  # Otterbein Cemetery
    ('OH-HAR-S-072', 40.6583202, -83.9562865),  # Ward Cemetery
    ('OH-HAR-S-073', 40.634259,  -83.3451391),  # Wheeler Cemetery
    ('OH-HAR-S-082', 40.7920589, -83.8793903),  # Candler Cemetery
    ('OH-HAR-S-084', 40.7334668, -83.8775158),  # Maysville Cemetery
    ('OH-HAR-S-085', 40.8083149, -83.7843068),  # McElroy Cemetery
    ('OH-HAR-S-087', 40.7321194, -83.8617229),  # Carman Cemetery
    ('OH-HAR-S-088', 40.7100985, -83.8223962),  # Preston Cemetery
    ('OH-HAR-S-089', 40.7105651, -83.8029988),  # Shadley Cemetery
    ('OH-HAR-S-093', 40.5807558, -83.8224924),  # McArthur Cemetery
    ('OH-HAR-S-096', 40.4003298, -83.8088241),  # County Home Cemetery
    ('OH-HAR-S-100', 40.5977385, -83.8717002),  # Bowdle Cemetery
    ('OH-HAR-S-104', 40.5945147, -83.8664905),  # Rutledge Cemetery
    ('OH-HAR-S-106', 40.5547755, -83.6360413),  # Bailey Cemetery
]

# NOTE: OH-HAR-S-010 (Ft. McArthur Cemetery) held for human-assist — may differ from McArthur Cemetery
# NOTE: OH-HAR-S-013 (Woodlawn New) held for human-assist — awaiting Street View confirmation

with open(r'D:\users\user1\Documents\CP Projects\Natural Areas Project v6\County Spreadsheets\Hardin\hardin_config.json') as f:
    c = json.load(f)

match_map = {sid: (lat, lon) for sid, lat, lon in clean_matches}
applied = 0

for s in c['sites']:
    sid = s.get('site_id')
    if sid in match_map:
        lat, lon = match_map[sid]
        s['gps_lat'] = lat
        s['gps_lon'] = lon
        s['gps_unresolvable'] = False
        s['gps_confidence'] = 'MEDIUM'
        applied += 1
        print(f'  Applied {sid} | {s["name"]} | {lat}, {lon}')

with open(r'D:\users\user1\Documents\CP Projects\Natural Areas Project v6\County Spreadsheets\Hardin\hardin_config.json', 'w') as f:
    json.dump(c, f, indent=2, ensure_ascii=False, default=str)

print(f'\nApplied GPS to {applied} sites. Config saved.')
