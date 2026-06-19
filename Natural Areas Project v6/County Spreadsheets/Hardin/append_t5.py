import yaml, pathlib

f = pathlib.Path(r'D:\users\user1\Documents\CP Projects\Natural Areas Project v6\County Spreadsheets\Hardin\hardin_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))

# Helper for cemetery record
def cem(name, twp, location, notes=None, ident_notes=None, baseline_id=None):
    return {
        'entity_type': 'Site',
        'name_raw': name,
        'counties_raw': ['Hardin'],
        'county_primary': 'Hardin',
        'ownership_raw': f'{twp} Township trustees, Hardin County',
        'governance_raw': f'{twp} Township trustees, Hardin County',
        'partner_agencies_raw': None,
        'coordination_raw': None,
        'description_raw': f'Township cemetery in {twp} Township, Hardin County, Ohio.',
        'habitat_type_raw': None,
        'features_raw': 'Cemetery; public access',
        'access_notes_raw': None,
        'location_raw': location,
        'acres_raw': None,
        'gps_lat_raw': None,
        'gps_lon_raw': None,
        'boundary_document_raw': None,
        'urls_raw': ['https://sites.rootsweb.com/~ohcps/hardin.html'],
        'ebird_hotspot_id': None,
        'identity_notes_raw': ident_notes,
        'township_raw': None,
        'municipality_raw': None,
        'last_verified_date': '2026-06-01',
        'field_verified': False,
        'discovery_tier': 5,
        'seeded_from_baseline': False,
        'baseline_id': baseline_id,
    }

t5_records = [

# =============================================================================
# TIER 5 — TOWNSHIPS
# Township Parks: Null for all 15 townships
# Township Cemeteries: Staged below
# =============================================================================

# --- T5 PARKS / RECREATION: NULL ---
{
    'entity_type_result': {
        'tier': 5,
        'governance_level': 'Township',
        'entity_type': 'Sites (Parks/Recreation)',
        'result': 'null',
        'pre_enumeration': {
            'source': 'Townships_Officials2022-2023.xlsx — Hardin County filter',
            'date': '2026-06-01',
            'townships_confirmed': [
                'Blanchard', 'Buck', 'Cessna', 'Dudley', 'Goshen', 'Hale',
                'Jackson', 'Liberty', 'Lynn', 'Marion', 'McDonald', 'Pleasant',
                'Roundhead', 'Taylor Creek', 'Washington',
            ],
            'total': 15,
            'defunct_candidates': 'None — all 15 present in OTA roster',
        },
        'township_results': {
            'Blanchard': 'No website found; no parks; within Veterans Memorial Park District service area; cemeteries enumerated below',
            'Buck': 'No website found; no parks; within Veterans Memorial Park District; cemeteries enumerated below',
            'Cessna': 'Website: cessnatwp.org (confirmed Hardin County); no parks listed; within Veterans Memorial Park District; cemeteries enumerated below',
            'Dudley': 'No website found; no parks; cemeteries enumerated below',
            'Goshen': 'Website: goshentwpoh.org (confirmed Hardin County — address 21012 CR 100, Kenton OH); no parks listed; cemeteries maintained by township road department',
            'Hale': 'No website found; no parks; cemeteries enumerated below',
            'Jackson': 'No dedicated Hardin County Jackson Township website confirmed; no parks; cemeteries enumerated below',
            'Liberty': 'No dedicated website; Liberty Township audit confirms cemetery services and road/bridge/fire only; no parks; cemeteries below',
            'Lynn': 'No website found; no parks; within Veterans Memorial Park District; cemeteries below',
            'Marion': 'No dedicated Hardin County Marion Township website found; search overwhelmed by Marion County/City results; no parks found',
            'McDonald': 'No website found; no parks; Zimmerman Kame in McDonald Twp is on private land (already addressed at T4); cemeteries below',
            'Pleasant': 'Website: pleasant-township.org (confirmed Hardin County — 555 W. Franklin St., Kenton, OH); no parks listed; within Veterans Memorial Park District; "Pleasant Township Green Parcel" (baseline) not confirmed — will be unconfirmed baseline seed; cemeteries below',
            'Roundhead': 'No official website; Facebook page; Wikipedia notes community has "a Park" but no name, governance, or confirmation of public access; staging as unconfirmed; cemeteries below',
            'Taylor Creek': 'No website; county hosts official contact info; no parks; cemeteries below',
            'Washington': 'No website; search overwhelmed by wrong-county results; no parks; Dola Cemetery noted; cemeteries below',
        },
        'sources_checked': [
            'cessnatwp.org', 'goshentwpoh.org', 'pleasant-township.org',
            'Wikipedia township articles for all 15',
            'Hardin County official contacts PDF (hardincountyohio.gov)',
            'Hardin County Cemeteries (sites.rootsweb.com/~ohcps/hardin.html)',
            'Ohio Auditor audit reports (Liberty Township audit)',
        ],
    }
},

# --- T5 CEMETERIES ---
# Goshen Township (confirmed: maintained by Goshen Twp Road Dept)
cem('McKendree Cemetery', 'Goshen',
    'SE side of CR 265, 1/2 mile north of TR 235 and TR 120, Goshen Township, Hardin County',
    ident_notes='Goshen Township-maintained cemetery per Goshen Township website. Road department maintains grounds.'),
cem('Shanks Cemetery', 'Goshen',
    'CR 215, 300 yards east of Rev Horn Run, Goshen Township, Hardin County',
    ident_notes='Goshen Township-maintained cemetery per Goshen Township website. Road department maintains grounds.'),

# Cessna Township (confirmed: on cessnatwp.org website)
cem('Cessna Cemetery', 'Cessna',
    '1/4 mile SE from SR 701 and TR 105, Cessna Township, Hardin County',
    ident_notes='Cessna Township cemetery per cessnatwp.org. Alternate names: Obenour Cemetery. c.1840.'),
cem('Ft. McArthur Cemetery', 'Cessna',
    'South of CR 106 and east of TR 125, Cessna Township, Hardin County',
    ident_notes='c.1812; 16 graves; Cessna Township. Cessna Township website lists cemeteries; township-maintained assumed.'),
cem('Grant Cemetery', 'Pleasant',
    'North side TR 74, west of SR 53, north of Kenton, Pleasant Township, Hardin County',
    ident_notes='Pleasant Township cemetery per pleasant-township.org/grant-cemetary. Still accepting burials.',
    baseline_id=None),

# Liberty Township (confirmed: provides cemetery services per audit)
cem('Woodlawn Cemetery', 'Liberty',
    'Corner of CR 60 and west side of SR 235, Liberty Township, Hardin County',
    ident_notes='Liberty Township cemetery per audit (township provides cemetery services). Alternate name: Old Washington Cemetery.'),
cem('Woodlawn (New) Cemetery', 'Liberty',
    'Corner of CR 60 and east side of SR 235, Liberty Township, Hardin County',
    ident_notes='Liberty Township cemetery, new section east of SR 235.'),

# McDonald Township (notable: eBird hotspot)
cem('Fairview-McDonald Cemetery', 'McDonald',
    '5302 SR 67, west of Kenton, McDonald Township, Hardin County',
    ident_notes='Active, well-maintained cemetery with mature trees. eBird hotspot L30884117. Ownership: McDonald Township trustees assumed based on maintenance and naming pattern.'),

# Blanchard Township cemeteries (no website; public ownership assumed for named township cemeteries)
cem('Dunkirk Cemetery', 'Blanchard',
    'NW corner of SR 68 and TR 40, Blanchard Township, Hardin County',
    ident_notes='Township cemetery in Blanchard Township. Village of Dunkirk located in Blanchard Township; cemetery governance TBD (township vs. village).'),
cem('Hall Cemetery', 'Blanchard',
    'East of TR 165 and 600 feet south of TR 46, Blanchard Township, Hardin County',
    ident_notes='Blanchard Township cemetery per Hardin County WPA plat maps and rootsweb list.'),

# Roundhead Township cemeteries
cem('Roundhead Cemetery (Old)', 'Roundhead',
    '2465 CR 190, east of SR 235, north side, Roundhead Township, Hardin County',
    ident_notes='Roundhead Township cemetery, c.1836. Alternate name: Old Church Cemetery.'),
cem('Roundhead Cemetery (New)', 'Roundhead',
    '2800 CR 190, 1/4 mile east of SR 235, south side, Roundhead Township, Hardin County',
    ident_notes='Roundhead Township cemetery, c.1880.'),
cem('Henkle/Hinkle Cemetery', 'Roundhead',
    'NW corner SR 67 and SR 235, Roundhead Township, Hardin County',
    ident_notes='c.1825-1938. Historical township cemetery, Roundhead Township.'),

# Washington Township cemeteries
cem('Dola Cemetery', 'Washington',
    'North side SR 81, Washington Township, Hardin County',
    ident_notes='Washington Township cemetery. Alternate name: Washington Cemetery. Dola is a community in Washington Township.'),

# Hale Township cemeteries
cem('Hale Cemetery', 'Hale',
    'North side SR 273 west of Mount Victory, east of TR 179, Hale Township, Hardin County',
    ident_notes='Hale Township cemetery.'),
cem('Ridgeway Cemetery', 'Hale',
    'West side of TR 179, south of SR 273, Hale Township, Hardin County',
    ident_notes='Hale Township cemetery; near Ridgeway village.'),

# Jackson Township cemeteries
cem('Patterson Cemetery', 'Jackson',
    'TR 195 north of SR 81 on east side, Jackson Township, Hardin County',
    ident_notes='Jackson Township cemetery. Alternate name: New Cemetery.'),
cem('Hueston Cemetery', 'Jackson',
    'CR 183 and CR 20, west of Forest, Jackson Township, Hardin County',
    ident_notes='c.1831, Jackson Township.'),

# Lynn Township cemeteries
cem('Gunn Cemetery', 'Lynn',
    '300 ft south of SR 67, west of CR 95, Lynn Township, Hardin County'),
cem('Norman Cemetery', 'Lynn',
    'West side CR 115, south of SR 67W, Lynn Township, Hardin County'),

# Taylor Creek Township cemeteries
cem('Seig Cemetery', 'Taylor Creek',
    'CR 200, east of US 68, Taylor Creek Township, Hardin County'),
cem('Yelverton Cemetery', 'Taylor Creek',
    'East side of CR 115 at TR 210, Taylor Creek Township, Hardin County',
    ident_notes='Alternate name: Sloan Cemetery.'),

# --- T5 ROUNDHEAD COMMUNITY PARK (UNCONFIRMED) ---
{
    'entity_type': 'Site',
    'name_raw': 'Roundhead Community Park (name unconfirmed)',
    'counties_raw': ['Hardin'],
    'county_primary': 'Hardin',
    'ownership_raw': None,
    'governance_raw': None,
    'partner_agencies_raw': None,
    'coordination_raw': None,
    'description_raw': 'Wikipedia describes the Roundhead community as having "a Park" among its features (alongside a volunteer fire department, church, and two cemeteries). No further details on name, ownership, acreage, or public access found.',
    'habitat_type_raw': None,
    'features_raw': None,
    'access_notes_raw': None,
    'location_raw': 'Roundhead community, Roundhead Township, Hardin County',
    'acres_raw': None,
    'gps_lat_raw': None,
    'gps_lon_raw': None,
    'boundary_document_raw': None,
    'urls_raw': ['https://en.wikipedia.org/wiki/Roundhead,_Ohio'],
    'ebird_hotspot_id': None,
    'identity_notes_raw': 'IDENTITY_UNCONFIRMED — Wikipedia mentions "a Park" in Roundhead community but no name, ownership, governance, or public access details found. May be informal open space or may not meet cataloging threshold. Requires field verification or authoritative source.',
    'township_raw': None,
    'municipality_raw': None,
    'last_verified_date': '2026-06-01',
    'field_verified': False,
    'discovery_tier': 5,
    'seeded_from_baseline': False,
    'baseline_id': None,
},

# --- T5 SITE NETWORKS: NULL ---
{
    'entity_type_result': {
        'tier': 5,
        'governance_level': 'Township',
        'entity_type': 'Site Network',
        'result': 'null',
        'sources_checked': [
            'All 15 Hardin County townships checked — no township manages multiple Sites forming a qualifying network',
        ],
        'reasoning': 'No township in Hardin County manages multiple named natural area Sites. Township parks are null; cemeteries are individual Sites. Rule 2 threshold (2+ member Sites under a conservation/land-holding org) not met.',
    }
},

# --- T5 ACCESS POINTS: NULL ---
{
    'entity_type_result': {
        'tier': 5,
        'governance_level': 'Township',
        'entity_type': 'Access Point',
        'result': 'null',
        'sources_checked': ['No township-managed Sites with formal AP infrastructure found beyond cemetery entrances (which are not stadalone APs)'],
        'reasoning': 'No qualifying Access Points for T5 township entities. Cemetery entrances are not cataloged as separate APs.',
    }
},

# --- T5 TRAILTHINGS: NULL ---
{
    'entity_type_result': {
        'tier': 5,
        'governance_level': 'Township',
        'entity_type': 'Trailthing',
        'result': 'null',
        'sources_checked': ['All 15 townships checked — no township-managed trail infrastructure found'],
        'reasoning': 'No township-managed trails in Hardin County.',
    }
},

# --- UNCONFIRMED BASELINE SEEDS FROM T5 ---
{
    'entity_type_result': {
        'tier': 5,
        'governance_level': 'Township — Unconfirmed Baseline Seeds',
        'entity_type': 'Site',
        'result': 'unconfirmed_baseline_seeds',
        'seeds': [
            {
                'baseline_id': 'Pleasant Township Green Parcel',
                'status': 'UNCONFIRMED_BASELINE_SEED',
                'tiers_searched': [1, 2, 3, 4, 5],
                'sources_checked': 'pleasant-township.org; Hardin County rootsweb; SORP CSV; WebSearch',
                'hold_detail': 'Baseline entry "Pleasant Township Green Parcel" describes informal open space with informal recreation managed by Pleasant Township trustees. Pleasant Township website does not mention any parks. No authoritative source documents a managed natural area by this name. Likely informal open space without formal identity. Hold_reason: unconfirmed_baseline_seed.',
            },
        ],
    }
},

]

data.setdefault('records', [])
data['records'].extend(t5_records)
f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False), encoding='utf-8')
print(f'Total records now: {len(data["records"])}')
