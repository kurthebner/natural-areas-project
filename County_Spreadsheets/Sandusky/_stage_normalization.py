"""
Stage 3 — Normalization Engine for Sandusky County, Ohio.
Reads raw discovery YAML + config JSON, populates normalized fields for all
active entities, applies IMP-086 parent_held rule, writes back to config.
"""

import json, yaml, re, pathlib, sys

# IMP-128: Windows console UTF-8 fix — prevents UnicodeEncodeError on → and em dashes
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

YAML_PATH = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
CFG_PATH  = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_config.json')

raw  = YAML_PATH.read_text(encoding='utf-8')
data = yaml.safe_load(raw)
records = data.get('records', [])

cfg    = json.loads(CFG_PATH.read_text(encoding='utf-8'))
sites  = cfg.get('sites', [])
trails = cfg.get('trails', [])
aps    = cfg.get('access_points', [])

yaml_sites  = [r for r in records if r['entity_type'] == 'Site']
yaml_trails = [r for r in records if r['entity_type'] == 'Trail']
yaml_aps    = [r for r in records if r['entity_type'] == 'Access Point']

assert len(yaml_sites)  == len(sites),  f'Site mismatch: YAML={len(yaml_sites)} cfg={len(sites)}'
assert len(yaml_trails) == len(trails), f'Trail mismatch'
assert len(yaml_aps)    == len(aps),    f'AP mismatch'


# ── Hold detection ─────────────────────────────────────────────────────────────
def is_held(rec):
    sf = rec.get('status_flag') or ''
    if sf.startswith('HELD'):
        return True
    notes = rec.get('notes') or ''
    return 'HELD' in notes and ('cross_county' in notes or 'gps_missing' in notes or 'parent_held' in notes)


# ── Metadata stripping (IMP-053) ───────────────────────────────────────────────
STRIP_RE = re.compile(
    r'(T\d+\s+miss[^.]*\.?\s*|'
    r'T\d+\s+pick-?up[^.]*\.?\s*|'
    r'GIS_VERIFY[_A-Z]*[^.]*\.?\s*|'
    r'OBJECTID\s*:\s*\d+[^.]*\.?\s*|'
    r'GPS_PENDING[^.]*\.?\s*|'
    r'GPS\s+needed[^.]*\.?\s*|'
    r'GPS\s+unresolvable[^.]*\.?\s*|'
    r'GPS_UNRESOLVABLE[^.]*\.?\s*|'
    r'IMP-\d+[^.]*\.?\s*)',
    re.IGNORECASE,
)

def strip_metadata(text):
    if not text:
        return ''
    cleaned = STRIP_RE.sub('', text)
    cleaned = re.sub(r'\s{2,}', ' ', cleaned).strip()
    cleaned = re.sub(r'^\s*[.;]\s*', '', cleaned).strip()
    return cleaned


# ── Feature mapping ────────────────────────────────────────────────────────────
FEATURE_MAP = [
    # order matters — longer patterns first per IMP-026
    (r'mountain bike trail|mountain biking trail', 'Mountain Bike Trail'),
    (r'self.guided interpretive trail|interpretive trail', 'Interpretive Sign'),
    (r'hiking trail|walking trail|walking path|nature trail|loop trail|trail system|winding trail', 'Hiking Trail'),
    (r'multi.use trail', 'Multi-use Trail'),
    (r'bridle trail|equestrian', 'Bridle Trail'),
    (r'boardwalk', 'Boardwalk'),
    (r'swimming beach|swim beach|quarry.*swim|beach.*swim|swim.*beach', 'Swimming Beach'),
    (r'swimming pool|city pool', 'Swimming Pool'),
    (r'splash pad|spray pad', 'Spray Park'),
    (r'boat ramp|launch ramp', 'Boat Ramp'),
    (r'boat launch|watercraft|canoe|kayak', 'Watercraft Access'),
    (r'fishing pond|fishing lake', 'Fishing Area'),
    (r'picnic shelter', 'Picnic Shelter'),
    (r'picnic area|picnic spot|picnic table', 'Picnic Area'),
    (r'pavilion|shelter house|open air pavilion|shelter.*rent|rentable.*shelter|covered.*seating', 'Pavilion'),
    (r'gazebo', 'Gazebo'),
    (r'basketball court', 'Basketball Court'),
    (r'tennis court', 'Tennis Court'),
    (r'pickleball court', 'Pickleball Court'),
    (r'volleyball court|sand volleyball', 'Volleyball Court'),
    (r'soccer field|soccer complex', 'Soccer Pitch'),
    (r'football field', 'Football Field'),
    (r'baseball|softball', 'Ball Diamond'),
    (r'disc golf', 'Disc Golf Course'),
    (r'skate park|skate ramp', 'Skate Park'),
    (r'miniature golf|mini.golf', 'Mini Golf'),
    (r'playground|play equipment|climbing structure', 'Playground'),
    (r'sledding hill', 'Sledding Hill'),
    (r'horseshoe', 'Horseshoe Pitch'),
    (r'archery range|archery', 'Archery Range'),
    (r'ropes course|high ropes', 'Ropes Course'),
    (r'shooting range|shooting sports', 'Shooting Range'),
    (r'dog park', 'Dog Park'),
    (r'restroom|flush toilet|portable toilet|bathroom|shower house|shower', 'Restrooms'),
    (r'parking lot|parking area|overflow parking|truck.*trailer.*parking', 'Parking Lot'),
    (r'kiosk|information kiosk', 'Kiosk'),
    (r'campsite|camping area|campground', 'Camping'),
    (r'cabin|camper cabin|log cabin|reconstructed.*cabin', 'Cabin Rentals'),
    (r'ADA.compliant|ADA accessible|wheelchair|handicapped accessible|accessible to people with disab', 'ADA Accessible'),
    (r'observation deck', 'Observation Deck'),
    (r'observation tower', 'Observation Tower'),
    (r'hunting area|public hunting|hunting permitted|trapping', 'Hunting Area'),
    (r'bird.*viewing|bird.*observation|bird.*watching|birding|lake erie birding trail', 'Bird Viewing Area'),
    (r'nature center|nature lab|wilson nature center', 'Nature Center'),
    (r'pollinator.*garden|pollinator meadow', 'Pollinator Garden'),
    (r'native.*grass|native grassland|prairie|wildflower meadow|pollinator meadow', 'Prairie'),
    (r'wetland|diked marsh|constructed wetland|marsh', 'Marsh'),
    (r'covered bridge|historic.*bridge', 'Historic Bridge'),
    (r'historic marker|historic sign', 'Historic Marker'),
    (r'historic.*structure|historic.*building|historic.*cabin|historic.*barn', 'Historic Structure'),
    (r'monument|memorial statue|war memorial', 'Monument'),
    (r'riparian|river frontage|sandusky river', 'Stream Segment'),
    (r'fishing', 'Fishing Area'),
    (r'beach', 'Beach'),
    (r'boating|hand.powered|electric motor', 'Watercraft Access'),
    (r'bike rack', 'Bike Rack'),
    (r'pond', 'Pond'),
    (r'spring', 'Spring'),
    (r'mountain biking|mountain bike', 'Mountain Bike Trail'),
    (r'ncit trailhead|trailhead', 'Hiking Trail'),
    (r'arboretum', 'Arboretum'),
    (r'museum|museum building', 'Museum Building'),
    (r'historic.*home|historic.*house|historic.*mansion|historic.*structure|historic.*ruins|hayes home', 'Historic Structure'),
    (r'grave|burial site', 'Historic Marker'),
    (r'grills|fire pit|fire ring', 'Fire Ring'),
    (r'athletic field|athletic complex', 'Athletic Field'),
    (r'band.*stand|bandstand', 'Bandstand'),
    (r'amphitheater', 'Amphitheater'),
    (r'sand volleyball|volleyball', 'Volleyball Court'),
]

def map_features(features_raw):
    if not features_raw or str(features_raw).strip() in ('None', 'none', ''):
        return ''
    raw_lower = str(features_raw).lower()
    matched = set()
    for pattern, vocab_term in sorted(FEATURE_MAP, key=lambda x: -len(x[0])):
        if re.search(pattern, raw_lower, re.IGNORECASE):
            matched.add(vocab_term)
    return ';'.join(sorted(matched))


# ── Governance/ownership cleanup ──────────────────────────────────────────────
def clean_org(text):
    if not text:
        return ''
    t = str(text)
    t = re.sub(r'\s*\(inferred[^)]*\)', '', t, flags=re.IGNORECASE).strip()
    return t.strip()


# ── URL handling ──────────────────────────────────────────────────────────────
def get_urls(urls_raw):
    if not urls_raw:
        return '', ''
    if isinstance(urls_raw, str):
        lst = [u.strip() for u in urls_raw.split(';') if u.strip()]
    else:
        lst = [u for u in (urls_raw or []) if u]
    url_primary   = lst[0] if lst else ''
    url_secondary = ';'.join(lst[1:]) if len(lst) > 1 else ''
    return url_primary, url_secondary


# ── Acres extraction ──────────────────────────────────────────────────────────
def get_acres(rec):
    for fld in ('acres_raw',):
        v = rec.get(fld)
        if v:
            return str(v)
    for fld in ('description_raw', 'features_raw'):
        txt = rec.get(fld) or ''
        m = re.search(r'(\d[\d,]*(?:\.\d+)?)\s*[\-]?acres?', txt, re.IGNORECASE)
        if m:
            return m.group(1).replace(',', '')
    return ''


# ── Category / Subtype classification ────────────────────────────────────────
# Per-entity overrides for non-obvious cases
CATEGORY_OVERRIDES = {
    'OH-SAN-S-001': ('Historic Site', 'Historic Landmark'),
    'OH-SAN-S-006': ('Natural Area', 'Upland Forest'),
    'OH-SAN-S-008': ('Wildlife Area', 'State Wildlife Area'),
    'OH-SAN-S-009': ('Conservation Area', ''),
    'OH-SAN-S-010': ('Nature Preserve', 'County Nature Preserve'),
    'OH-SAN-S-011': ('Conservation Area', ''),
    'OH-SAN-S-013': ('Park', ''),
    'OH-SAN-S-014': ('Conservation Area', ''),
    'OH-SAN-S-017': ('Historic Site', 'Historic Structure'),
    'OH-SAN-S-018': ('Conservation Area', ''),
    'OH-SAN-S-021': ('Conservation Area', ''),
    'OH-SAN-S-022': ('Natural Area', 'Upland Forest'),
    'OH-SAN-S-023': ('Park', ''),
    'OH-SAN-S-024': ('Park', 'Waterfront Park'),
    'OH-SAN-S-025': ('Campground', ''),
    'OH-SAN-S-028': ('Park', ''),
    'OH-SAN-S-031': ('Park', 'Civic Park'),
    'OH-SAN-S-068': ('Park', 'Civic Park'),
    'OH-SAN-S-088': ('Water Site', 'Reservoir'),
    'OH-SAN-S-089': ('Cemetery', 'Public Cemetery'),
    'OH-SAN-S-091': ('Park', 'Civic Park'),
    'OH-SAN-S-104': ('Recreation Facility', 'Golf Course'),
    'OH-SAN-S-108': ('Cemetery', 'Public Cemetery'),
    'OH-SAN-S-110': ('Cemetery', 'Public Cemetery'),
}

def classify_site(eid, name, gov, own, tier):
    if eid in CATEGORY_OVERRIDES:
        return CATEGORY_OVERRIDES[eid]
    n = (name or '').lower()
    g = (gov or '').lower()

    # Cemetery (most specific — check first)
    if any(x in n for x in ['cemetery', 'burial ground', 'memory garden']):
        if 'private family' in g or g.startswith('private'):
            return 'Cemetery', 'Family Cemetery'
        if any(x in g for x in ['church', 'religious', 'reformed church']):
            return 'Cemetery', 'Church Cemetery'
        if 'greenlawn' in n or 'commercial' in g:
            return 'Cemetery', 'Private Cemetery'
        return 'Cemetery', 'Public Cemetery'

    # Golf / Country Club
    if any(x in n for x in ['golf', 'country club']):
        return 'Recreation Facility', 'Golf Course'

    # Hunt Club
    if 'hunt club' in n:
        return 'Hunting Area', ''

    # Hunting / wildlife management
    if any(x in n for x in ['ringneck ridge', 'doug haubert', 'wildlife preserve', 'wildlife reserve']):
        return 'Conservation Area', ''

    # Reservoir / Water Site
    if 'reservoir' in n:
        return 'Water Site', 'Reservoir'

    # ODNR Wildlife Area
    if 'division of wildlife' in g or 'wildlife area' in n.replace('wildlife preserve',''):
        return 'Wildlife Area', 'State Wildlife Area'

    # Campground
    if 'campground' in n:
        return 'Campground', ''

    # Nature Preserve
    if 'nature preserve' in n or 'christy farm' in n:
        return 'Nature Preserve', 'County Nature Preserve'

    # Conservation Area (reserves, wetlands, marshes, bends, homesteads managed by park district)
    if any(x in n for x in ['reserve', 'wetland', 'marsh', 'homestead', 'redhorse', 'creek bend', 'decoy',
                             'blue heron', 'muddy creek', 'green creek', 'shelley']):
        return 'Conservation Area', ''

    # Historic
    if 'covered bridge' in n:
        return 'Historic Site', 'Historic Structure'
    if 'ohio history connection' in g:
        return 'Historic Site', 'Historic Landmark'
    if 'barn' in n and ('historical' in n or 'historic' in n or 'log cabin' in n):
        return 'Historic Site', 'Historic Structure'

    # Arboretum
    if 'arboretum' in n:
        return 'Curated Biological Site', 'Arboretum'

    # Recreation Facility
    if any(x in n for x in ['athletic field', 'recreation complex', 'sports complex']):
        return 'Recreation Facility', 'Athletic Field'
    if 'magdalyn aigler' in n:
        return 'Recreation Facility', 'Athletic Field'

    # Park (default for municipal, township, SCPD parks)
    return 'Park', ''


# ── Designation extraction ────────────────────────────────────────────────────
def get_designation(eid, name, gov, identity_notes_raw, tier):
    designations = []
    notes = (identity_notes_raw or '').lower()
    n = (name or '').lower()
    g = (gov or '').lower()

    if 'state park' in notes and 'state park' not in 'state park designation':
        designations.append('State Park')
    if eid == 'OH-SAN-S-001':
        return 'National Historic Landmark;National Register of Historic Places (NRHP);State Memorial;State Park'
    if 'state wildlife area' in notes or ('division of wildlife' in g and tier == 2):
        designations.append('State Wildlife Area')
    if 'state scenic river' in notes:
        designations.append('State Scenic River')
    if 'state nature preserve' in notes:
        designations.append('State Nature Preserve')
    if 'national register of historic places' in notes or 'nrhp' in notes:
        designations.append('National Register of Historic Places (NRHP)')
    if 'national natural landmark' in notes:
        designations.append('National Natural Landmark')
    if 'state forest' in notes:
        designations.append('State Forest')

    return ';'.join(sorted(set(designations)))


# ── Description cleaning (IMP-052 opener stripping) ───────────────────────────
OPENER_RE = re.compile(
    r'^((\d[\d,\.]*\s*acres?[^.]*\.?\s*)|'
    r'(located\s+at\s+[^.]+\.?\s*)|'
    r'(located\s+in\s+[^.]+\.?\s*)|'
    r'(situated\s+at\s+[^.]+\.?\s*))',
    re.IGNORECASE,
)

def clean_description(desc_raw):
    if not desc_raw:
        return ''
    desc = str(desc_raw).strip()
    # strip prohibited openers
    cleaned = OPENER_RE.sub('', desc).strip()
    if not cleaned or cleaned == desc:
        cleaned = desc  # no opener found, keep original
    return cleaned


# ═══════════════════════════════════════════════════════════════════════════════
#  NORMALIZE SITES
# ═══════════════════════════════════════════════════════════════════════════════

site_id_map = {s['site_id']: s for s in sites}
normalized_count = 0
held_parent = []

for i, (cfg_site, raw_site) in enumerate(zip(sites, yaml_sites)):
    eid = cfg_site['site_id']

    if is_held(cfg_site):
        continue  # skip held entities

    # Organizational fields (free-text, copy verbatim after cleanup)
    cfg_site['ownership']       = clean_org(raw_site.get('ownership_raw', ''))
    cfg_site['governance']      = clean_org(raw_site.get('governance_raw', ''))
    cfg_site['partner_agencies'] = clean_org(raw_site.get('partner_agencies_raw', '') or '')
    cfg_site['coordination']    = clean_org(raw_site.get('coordination_raw', '') or '')

    # Category / Subtype
    cat, sub = classify_site(
        eid,
        cfg_site['name'],
        raw_site.get('governance_raw', ''),
        raw_site.get('ownership_raw', ''),
        raw_site.get('discovery_tier', 0),
    )
    cfg_site['category'] = cat
    cfg_site['subtype']  = sub

    # Designation
    cfg_site['designation'] = get_designation(
        eid,
        cfg_site['name'],
        raw_site.get('governance_raw', ''),
        raw_site.get('identity_notes_raw', ''),
        raw_site.get('discovery_tier', 0),
    )

    # Description (with opener stripping IMP-052)
    cfg_site['description'] = clean_description(raw_site.get('description_raw', ''))

    # Location
    cfg_site['location'] = (raw_site.get('location_raw', '') or '').strip()

    # Acres
    cfg_site['acres'] = get_acres(raw_site)

    # Features (vocabulary mapping, IMP-049/050/051)
    cfg_site['features'] = map_features(raw_site.get('features_raw', ''))

    # Notes — from identity_notes_raw with metadata stripping (IMP-053)
    identity_notes = raw_site.get('identity_notes_raw', '') or ''
    cfg_site['notes'] = strip_metadata(identity_notes)

    # URLs
    url_p, url_s = get_urls(raw_site.get('urls_raw', []))
    cfg_site['url_primary']   = url_p
    cfg_site['url_secondary'] = url_s

    # Parent site (child sites of White Star Park)
    if eid in ('OH-SAN-S-024', 'OH-SAN-S-025', 'OH-SAN-S-026', 'OH-SAN-S-027'):
        cfg_site['parent_site_id'] = 'OH-SAN-S-023'

    normalized_count += 1

# IMP-086: parent_held check for child sites
for s in sites:
    if is_held(s):
        continue
    parent_id = s.get('parent_site_id')
    if parent_id and parent_id in site_id_map:
        parent = site_id_map[parent_id]
        if is_held(parent):
            s['status_flag'] = 'HELD'
            s['hold_detail'] = 'parent_held'
            held_parent.append(s['site_id'])
            print(f'  IMP-086 parent_held: {s["site_id"]} (parent {parent_id} is held)')
            normalized_count -= 1  # uncounted


# ═══════════════════════════════════════════════════════════════════════════════
#  NORMALIZE TRAILS
# ═══════════════════════════════════════════════════════════════════════════════

# Trail use/surface/origin mappings
TRAIL_NORM = {
    'OH-MC-T-0110': {
        'use_type': 'Multi-Use', 'surface_type': 'Paved', 'origin_type': 'Rail Trail',
        'length_mi': '28', 'difficulty': '',
    },
    'OH-SAN-T-002': {
        'use_type': 'Hiking', 'surface_type': 'Natural Surface', 'origin_type': 'Purpose-Built',
        'length_mi': '0.8', 'difficulty': 'Easy',
    },
    'OH-SAN-T-003': {
        'use_type': 'Mountain Bike', 'surface_type': 'Natural Surface', 'origin_type': 'Purpose-Built',
        'length_mi': '', 'difficulty': 'Moderate',
    },
    'OH-SAN-T-004': {
        'use_type': 'Hiking', 'surface_type': 'Natural Surface', 'origin_type': 'Purpose-Built',
        'length_mi': '', 'difficulty': 'Easy',
    },
}

for cfg_trail, raw_trail in zip(trails, yaml_trails):
    eid = cfg_trail['trail_id']
    if is_held(cfg_trail):
        continue

    tnorm = TRAIL_NORM.get(eid, {})
    cfg_trail['use_type']    = tnorm.get('use_type', '')
    cfg_trail['surface_type'] = tnorm.get('surface_type', '')
    cfg_trail['origin_type'] = tnorm.get('origin_type', '')
    cfg_trail['length_mi']   = tnorm.get('length_mi', '')
    cfg_trail['difficulty']  = tnorm.get('difficulty', '')

    cfg_trail['ownership']       = clean_org(raw_trail.get('ownership_raw', ''))
    cfg_trail['governance']      = clean_org(raw_trail.get('governance_raw', ''))
    cfg_trail['partner_agencies'] = clean_org(raw_trail.get('partner_agencies_raw', '') or '')
    cfg_trail['description']     = (raw_trail.get('description_raw', '') or '').strip()
    cfg_trail['accessibility']   = (raw_trail.get('accessibility_raw', '') or '').strip()

    # identity_notes — strip metadata
    inotes = raw_trail.get('identity_notes_raw', '') or ''
    cfg_trail['identity_notes'] = strip_metadata(inotes)

    url_p, url_s = get_urls(raw_trail.get('urls_raw', []))
    cfg_trail['url_primary'] = url_p
    cfg_trail['maps']        = url_s

    # Parent site for OH-SAN-T-002, OH-SAN-T-003 (White Star Park area, Waggoner's Run at White Star)
    if eid == 'OH-SAN-T-002':
        cfg_trail['parent_site_id'] = 'OH-SAN-S-024'  # White Star Quarry parent
    if eid == 'OH-SAN-T-003':
        cfg_trail['parent_site_id'] = 'OH-SAN-S-023'  # White Star Park

    # Counties for NCIT
    if eid == 'OH-MC-T-0110':
        cfg_trail['counties'] = 'Erie;Huron;Ottawa;Sandusky'

    # Handle NCIT entity_id (use temp_id as the real ID in upsert)
    if cfg_trail.get('temp_id') == 'OH-MC-T-0110':
        cfg_trail['trail_id_final'] = 'OH-MC-T-0110'


# ═══════════════════════════════════════════════════════════════════════════════
#  NORMALIZE ACCESS POINTS
# ═══════════════════════════════════════════════════════════════════════════════

AP_NORM = {
    'OH-SAN-AP-001': {'ap_type': 'Pedestrian Entrance',     'parent_entity_type': 'Site',  'parent_entity_id': 'OH-SAN-S-002'},
    'OH-SAN-AP-004': {'ap_type': 'Trailhead',              'parent_entity_type': 'Trail', 'parent_entity_id': 'OH-MC-T-0110'},
    'OH-SAN-AP-005': {'ap_type': 'Trailhead',              'parent_entity_type': 'Trail', 'parent_entity_id': 'OH-MC-T-0110'},
    'OH-SAN-AP-006': {'ap_type': 'Watercraft Access Point','parent_entity_type': 'Site',  'parent_entity_id': 'OH-SAN-S-028'},
    'OH-SAN-AP-007': {'ap_type': 'Boat Ramp',              'parent_entity_type': 'Site',  'parent_entity_id': 'OH-SAN-S-005'},
    'OH-SAN-AP-008': {'ap_type': 'Boat Ramp',              'parent_entity_type': '',      'parent_entity_id': ''},
    'OH-SAN-AP-009': {'ap_type': 'Fishing Access',         'parent_entity_type': '',      'parent_entity_id': ''},
}

for cfg_ap, raw_ap in zip(aps, yaml_aps):
    eid = cfg_ap['access_point_id']
    if is_held(cfg_ap):
        continue

    ap_meta = AP_NORM.get(eid, {})
    cfg_ap['ap_type']            = ap_meta.get('ap_type', 'Other')
    cfg_ap['parent_entity_type'] = ap_meta.get('parent_entity_type', '')
    cfg_ap['parent_entity_id']   = ap_meta.get('parent_entity_id', '')

    cfg_ap['governance']      = clean_org(raw_ap.get('governance_raw', ''))
    cfg_ap['ownership']       = clean_org(raw_ap.get('ownership_raw', ''))
    cfg_ap['address']         = (raw_ap.get('location_raw', '') or '').strip()
    cfg_ap['features']        = map_features(raw_ap.get('features_raw', ''))
    cfg_ap['accessibility']   = (raw_ap.get('accessibility_raw', '') or '').strip()

    inotes = raw_ap.get('identity_notes_raw', '') or ''
    cfg_ap['identity_notes'] = strip_metadata(inotes)

    url_p, _ = get_urls(raw_ap.get('urls_raw', []))
    cfg_ap['url_primary'] = url_p

# IMP-086: parent_held check for APs
for ap in aps:
    if is_held(ap):
        continue
    parent_eid = ap.get('parent_entity_id', '')
    if not parent_eid:
        continue
    # Check if parent is a held Site
    if parent_eid in site_id_map:
        parent_site = site_id_map[parent_eid]
        if is_held(parent_site):
            ap['status_flag'] = 'HELD'
            ap['hold_detail'] = 'parent_held'
            held_parent.append(ap['access_point_id'])
            print(f'  IMP-086 parent_held: {ap["access_point_id"]} (parent site {parent_eid} is held)')
    # Parent trail check: NCIT (OH-MC-T-0110) is active (gps_unresolvable), so APs of NCIT are not held
    # SAN-S-005 is held, so AP-007 gets parent_held

cfg['sites']         = sites
cfg['trails']        = trails
cfg['access_points'] = aps
CFG_PATH.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding='utf-8')

# ── Final summary ──────────────────────────────────────────────────────────────
total_held = sum(1 for s in sites if is_held(s)) + sum(1 for t in trails if is_held(t)) + sum(1 for a in aps if is_held(a))
total_active = (len(sites)+len(trails)+len(aps)) - total_held

print()
print('Normalization complete:')
print(f'  Normalized sites:  {sum(1 for s in sites if not is_held(s))}')
print(f'  Normalized trails: {sum(1 for t in trails if not is_held(t))}')
print(f'  Normalized APs:    {sum(1 for a in aps if not is_held(a))}')
print(f'  Held for parent_held: {held_parent}')
print(f'  Total held (all reasons): {total_held}')
print(f'  Total active for output:  {total_active}')
