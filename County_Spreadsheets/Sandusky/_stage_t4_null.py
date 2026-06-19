import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('tier4_null_evidence', [])

data['tier4_null_evidence'].append({
    'tier': 4,
    'governance_level': 'Sandusky County Government (county commissioners, county departments)',
    'entity_types_checked': ['Site', 'Trail', 'Trail Segment', 'Trail Network', 'Site Network', 'Access Point'],
    'result': 'null',
    'sources_checked': [
        'sanduskycountyoh.gov — full site navigation; no parks/recreation department found',
        'Sandusky County Park District (SCPD) handles all county parks function — already staged at T3'
    ],
    'reasoning': (
        'Sandusky County has no county-government parks or recreation department. SCPD (Tier 3) '
        'handles all county park functions. County commissioners manage no natural areas directly. Null.'
    )
})

data['tier4_null_evidence'].append({
    'tier': 4,
    'governance_level': 'NRHP Bridges and Structures — county-accessible outdoor sites',
    'entity_types_checked': ['Site', 'Access Point'],
    'result': 'null',
    'sources_checked': [
        'Wikipedia: National Register of Historic Places listings in Sandusky County, Ohio (12 entries)',
        'Mull Covered Bridge — already staged at T3 (SCPD co-managed)',
        'Soldiers and McKinley Memorial Parkways — decorative brick streets, not parks; no recreational amenities',
        'Remaining 10 NRHP entries — private historic homes, churches, courthouse; no public outdoor recreation'
    ],
    'reasoning': (
        'Mull Covered Bridge already captured at T3. Soldiers/McKinley Memorial Parkways are '
        'historic brick streets with medians; no recreational park character. Other NRHP entries '
        'are private residential properties. Null for new county-level entities.'
    )
})

data['tier4_null_evidence'].append({
    'tier': 4,
    'governance_level': 'County Fairgrounds',
    'entity_types_checked': ['Site'],
    'result': 'null',
    'sources_checked': [
        'sanduskycountyfair.com — independently owned and operated by Sandusky County Fair & Agricultural Society',
        'Not county-government owned; receives minimal local/state support'
    ],
    'reasoning': (
        'Sandusky County Fairgrounds (902 Rawson Ave, Fremont) is independently owned by the '
        'Sandusky County Fair & Agricultural Society — not county government. Primarily a speedway '
        'and fairgrounds complex; no natural area character. T8 candidate if assessed; not T4.'
    )
})

data['tier4_null_evidence'].append({
    'tier': 4,
    'governance_level': 'County Golf Courses',
    'entity_types_checked': ['Site'],
    'result': 'null',
    'sources_checked': [
        'Green Hills Golf Course (1959 S Main St, Clyde) — privately owned by Crockett family since 1956',
        'Sycamore Hills Golf Course — private; no county or SCPD ownership confirmed',
        'Fremont Country Club — private club'
    ],
    'reasoning': 'All golf courses in Sandusky County are privately owned. No county park district golf course. Null per IMP-099.'
})

data['tier4_null_evidence'].append({
    'tier': 4,
    'governance_level': 'County Cemeteries (infirmary, soldiers relief)',
    'entity_types_checked': ['Site'],
    'result': 'null',
    'sources_checked': [
        'sandusky.ohgenweb.org/cemeteries.html — cemetery list; no county infirmary cemetery identified in Sandusky County',
        'Ohio Veterans Home cemetery is in Erie County (city of Sandusky), not Sandusky County'
    ],
    'reasoning': (
        'No Sandusky County infirmary/poorhouse cemetery or soldiers relief cemetery '
        'identified as county-owned and publicly accessible. Null per IMP-099.'
    )
})

data['tier4_null_evidence'].append({
    'tier': 4,
    'governance_level': 'County Trails, Trail Segments, Trail Networks',
    'entity_types_checked': ['Trail', 'Trail Segment', 'Trail Network'],
    'result': 'null',
    'sources_checked': [
        'County government website — no county trail program',
        'Barn Mural Trail — Sandusky County CVB tourism driving route; not a physical trail or NAP entity',
        'Waggoner\'s Run MTB Trail — SCPD-managed (T3 miss, staged separately)'
    ],
    'reasoning': (
        'No county-government-managed trails or trail networks. Barn Mural Trail is a tourism '
        'driving route on public roads, not a physical trail. Waggoner\'s Run is SCPD (T3). Null.'
    )
})

data['tier4_null_evidence'].append({
    'tier': 4,
    'governance_level': 'County Site Networks',
    'entity_types_checked': ['Site Network'],
    'result': 'null',
    'sources_checked': [
        'No county-government parks district separate from SCPD; SCPD is a park district (T3)',
        'No other county-branded multi-site network identified'
    ],
    'reasoning': 'SCPD is the parks district (T3). No county-government-managed Site Network. Null.'
})

# Cross-tier discoveries noted during T4 review
data['tier4_null_evidence'].append({
    'tier': 4,
    'governance_level': 'Cross-tier discoveries during T4 review (informational)',
    'entity_types_checked': [],
    'result': 'cross_tier',
    'sources_checked': [
        'Waggoner\'s Run MTB Trail (SCPD T3 miss) — staged separately as T3 record',
        'Darr-Root Fishing Access (ODNR T2 miss) — staged separately as T2 record',
        'Sand Docks (City of Fremont) — flagged for T6 Municipal discovery',
        'Raccoon Creek Reservoir (City of Clyde) — flagged for T6 Municipal discovery',
        'Raccoon Creek Reservoir Fishing Area — ODNR cooperative agreement; primary mgmt is City of Clyde (T6)'
    ],
    'reasoning': (
        'T4 cross-referencing revealed two previously missed records from earlier tiers. '
        'Both staged with correct tier designations. Sand Docks and Raccoon Creek Reservoir '
        'deferred to T6 Municipal discovery.'
    )
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'Done. T4 null blocks: {len(data["tier4_null_evidence"])}, Total records: {len(data["records"])}')
