import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('tier7_null_evidence', [])

# --- Black Swamp Conservancy — Public Holdings (all already T3) ---
data['tier7_null_evidence'].append({
    'tier': 7,
    'governance_level': 'Black Swamp Conservancy — Public holdings in Sandusky County',
    'entity_types_checked': ['Site', 'Trail', 'Access Point'],
    'result': 'null — all public holdings transferred to SCPD and staged at T3',
    'sources_checked': [
        'blackswamp.org/property/redhorse-bend/ — 78 ac, transferred to Sandusky County Park District; staged T3',
        'blackswamp.org/property/christy-farms-nature-preserve/ — ~147 ac, donated to SCPD 2019; staged T3',
        'blackswamp.org/property/decoy-marsh/ — 67 ac, SCPD-managed; staged T3',
        'BSC listed as partner/conservation originator in T3 records for all three properties',
    ],
    'reasoning': (
        'Black Swamp Conservancy is the originating conservation organization for Redhorse Bend, '
        'Christy Farm Nature Preserve, and Decoy Marsh — all now owned and/or managed by Sandusky '
        'County Park District (SCPD). These are T3 entities, not T7. BSC\'s role as conservation '
        'originator is noted in partner_agencies_raw for each T3 record. No new T7 entities. Null.'
    ),
})

# --- Black Swamp Conservancy — Agricultural Easements (excluded §4.2) ---
data['tier7_null_evidence'].append({
    'tier': 7,
    'governance_level': 'Black Swamp Conservancy — Agricultural conservation easements',
    'entity_types_checked': ['Site'],
    'result': 'null — excluded per §4.2 (agricultural easements, no public access, no recreation role)',
    'sources_checked': [
        'Washusky Farms easement — 604 ac, west of Fremont, Sandusky County. '
        'Private working farm (Ron and Judy Mauch/Chester and Betty Mauch). '
        'USDA + Ohio Dept of Agriculture co-funded. 2011. No public access. '
        'Source: ocj.com/2011/12/black-swamp-conservancy-protects-600-acre-farm/',
        'Frankart Farm easement — ~510 ac, crosses Seneca and Sandusky counties (CROSS_COUNTY_CANDIDATE). '
        'Private working farm. No public access. '
        'Source: blackswamp.org/preserving-the-family-farm-planning-for-the-future/',
    ],
    'reasoning': (
        'Two BSC agricultural conservation easements identified in or crossing Sandusky County. '
        'Both are private working farms with no public access and no recreation role. '
        'Excluded per §4.2 (Agricultural easements with no recreation role). '
        'Frankart Farm crosses Seneca and Sandusky counties — CROSS_COUNTY_CANDIDATE noted for completeness '
        'but not staged as no T7 entity qualifies. Null.'
    ),
})

# --- North Central Ohio Land Conservancy (NCOLC) ---
data['tier7_null_evidence'].append({
    'tier': 7,
    'governance_level': 'North Central Ohio Land Conservancy — Sandusky County',
    'entity_types_checked': ['Site', 'Trail', 'Access Point'],
    'result': 'null — easement on Blue Heron Reserve; land owned/managed by SCPD, staged T3',
    'sources_checked': [
        'ncolc.org/property/blue-heron-reserve/ — 160 ac conservation easement; '
        'SCPD is the land owner and manager; NCOLC holds the conservation easement only. '
        'Blue Heron Reserve staged at T3 under SCPD governance.',
    ],
    'reasoning': (
        'NCOLC holds the conservation easement on Blue Heron Reserve, but the land is owned '
        'and managed by Sandusky County Park District (T3). No new T7 entity warranted — '
        'NCOLC\'s role noted as easement holder in partner_agencies_raw of T3 record. '
        'No other NCOLC holdings found in Sandusky County. Null.'
    ),
})

# --- Western Reserve Land Conservancy (WRLC) ---
data['tier7_null_evidence'].append({
    'tier': 7,
    'governance_level': 'Western Reserve Land Conservancy — Sandusky County',
    'entity_types_checked': ['Site', 'Trail', 'Access Point'],
    'result': 'null — one agricultural easement found; excluded §4.2',
    'sources_checked': [
        'wrlandconservancy.org — Edwards Farm (Maple View Farms LLC) easement — 656 ac, '
        'near City of Clyde, southeastern Sandusky County. Keith and Natalie Edwards. 2018. '
        'Private working farm (corn/soybeans/winter wheat). No public access. '
        'Source: wrlandconservancy.org/one-square-mile-of-family-farmland-preserved/',
    ],
    'reasoning': (
        'WRLC holds one conservation easement in Sandusky County (Edwards Farm, 656 ac). '
        'This is a private agricultural easement with no public access and no recreation role. '
        'Excluded per §4.2. No other WRLC public-access properties found in Sandusky County. Null.'
    ),
})

# --- Western Wildlife Corridor, Inc. ---
data['tier7_null_evidence'].append({
    'tier': 7,
    'governance_level': 'Western Wildlife Corridor, Inc. — Sandusky County',
    'entity_types_checked': ['Site', 'Trail', 'Access Point'],
    'result': 'null — organization operates in Hamilton County (Cincinnati area), not Sandusky County',
    'sources_checked': [
        'westernwildlifecorridor.org; LTA profile — WWC operates along the Ohio River Valley '
        'in the greater Cincinnati area (Hamilton County), spanning 30+ miles from Mill Creek '
        'to Great Miami River at Indiana border. Geographically unrelated to Sandusky County.',
        'Open flag from prior tiers resolved: "Muddy Creek Preserve (Western Wildlife Corridor)" '
        'was a naming confusion. The Muddy Creek Reserve in Sandusky County is SCPD (T3). '
        'The Western Wildlife Corridor organization has no presence in Sandusky County.',
    ],
    'reasoning': (
        'WWC is active exclusively in southwest Ohio (Hamilton County / Cincinnati area). '
        'No holdings or activity in Sandusky County. Open flag resolved. Null.'
    ),
})

# --- ONAPA / Ohio State Nature Preserves ---
data['tier7_null_evidence'].append({
    'tier': 7,
    'governance_level': 'ONAPA / Ohio State Nature Preserves — Sandusky County',
    'entity_types_checked': ['Site'],
    'result': 'null — zero ODNR state nature preserves in Sandusky County per authoritative sources',
    'sources_checked': [
        'onapa.org/preserve-map.html — links to ODNR DNAP database; no Sandusky County preserves',
        'Wikipedia: List of Ohio State Nature Preserves — zero entries in Sandusky County',
        'Sears Woods (Crawford County) was ruled out — not in Sandusky County',
    ],
    'reasoning': (
        'ONAPA mandatory cross-check completed. No ODNR state nature preserves in Sandusky County. '
        'Adjacent counties (Erie, Seneca, Ottawa) have several; Sandusky County has none. Null.'
    ),
})

# --- Other Organizations (TNC, TPL, Coalition of Ohio Land Trusts) ---
data['tier7_null_evidence'].append({
    'tier': 7,
    'governance_level': 'Other land trusts — TNC, TPL, Coalition of Ohio Land Trusts',
    'entity_types_checked': ['Site', 'Trail', 'Access Point'],
    'result': 'null',
    'sources_checked': [
        'The Nature Conservancy (TNC) — Sandusky Bay restoration work is regional/partnership scale; '
        'no confirmed TNC fee-simple holdings in Sandusky County. Putnam Marsh is Erie County.',
        'Trust for Public Land (TPL) — East Sandusky Bay properties (Eagle Point, Putnam Marsh, etc.) '
        'are in Erie County under Erie MetroParks. No TPL properties in Sandusky County.',
        'Coalition of Ohio Land Trusts (ohiolandtrusts.org) — no Sandusky County member trusts identified.',
    ],
    'reasoning': 'No additional land trust entities found for Sandusky County. Null.',
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'T7 null evidence staged. T7 null blocks: {len(data["tier7_null_evidence"])}. Total records: {len(data["records"])}')
