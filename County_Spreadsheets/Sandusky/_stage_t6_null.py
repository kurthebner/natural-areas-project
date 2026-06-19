import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('tier6_null_evidence', [])

# --- Fremont — City Cemetery ---
data['tier6_null_evidence'].append({
    'tier': 6,
    'governance_level': 'City of Fremont — City Cemetery',
    'entity_types_checked': ['Site (Cemetery)'],
    'result': 'null',
    'sources_checked': [
        'fremontohio.org/departments/parks/ — no city cemetery listed',
        'Oakwood Cemetery (1225 Oakwood St, Fremont OH) — confirmed Ballville Township-owned '
        '(since 2021 per T5 discovery); city address but township governance, staged at T5',
        'No evidence of separate City of Fremont-managed cemetery in any source',
    ],
    'reasoning': (
        'City of Fremont does not appear to operate its own cemetery. '
        'Oakwood Cemetery carries a Fremont address but has been township-managed since 2021 (T5). '
        'Null.'
    ),
})

# --- Green Springs — Village Parks ---
data['tier6_null_evidence'].append({
    'tier': 6,
    'governance_level': 'Village of Green Springs — Parks',
    'entity_types_checked': ['Site', 'Trail', 'Access Point'],
    'result': 'null — pending human contact verification',
    'sources_checked': [
        'gsohio.org/departments/parks-rentals — HTTP 403 blocked; page exists but content inaccessible',
        'Whirlpool Park (2220 E. CR 181, Green Springs OH) — CLOSED; '
        'contaminated with PCBs and toxic metals from former Whirlpool Corp. industrial waste (1950s); '
        'EPA investigated; Whirlpool sold land 2008; not a viable public park entity',
        'Ron Abraham State Forest — staged at T2 (ODNR, not village-managed)',
        'Village parks page implies at least one shelter/park exists per shelter reservation page',
        'Search results: no additional village-managed parks named in any source',
    ],
    'reasoning': (
        'Village of Green Springs parks page is HTTP 403 blocked. '
        'Whirlpool Park is closed and contaminated — not staged. '
        'Ron Abraham State Forest is T2. '
        'No other named village parks found in web sources. '
        'Human contact recommended before finalizing null: '
        'Village of Green Springs Fiscal Officer: 419-639-2123. '
        'Staging as null for pipeline purposes; open flag added.'
    ),
})

# --- Burgoon — Village Parks ---
data['tier6_null_evidence'].append({
    'tier': 6,
    'governance_level': 'Village of Burgoon — All entity types',
    'entity_types_checked': ['Site', 'Trail', 'Trail Segment', 'Trail Network', 'Site Network', 'Access Point'],
    'result': 'null',
    'sources_checked': [
        'No village website found for Burgoon OH (population 183, 0.12 sq mi)',
        'Sandusky County CVB other-attractions page — no Burgoon parks listed',
        'SCPD properties — no SCPD holdings in Burgoon village',
        'Search results — no parks or recreation areas found for Village of Burgoon',
    ],
    'reasoning': (
        'Burgoon is a very small village (183 residents, 0.12 sq mi). '
        'No village website exists. No parks or recreation facilities found in any source. Null.'
    ),
})

# --- Helena — Village Parks ---
data['tier6_null_evidence'].append({
    'tier': 6,
    'governance_level': 'Village of Helena — Parks',
    'entity_types_checked': ['Site', 'Trail', 'Access Point'],
    'result': 'null — pending human contact verification',
    'sources_checked': [
        'villageofhelena.org/park-recreation/ — page exists but content is a navigation stub only; '
        'no park names, addresses, or features listed',
        'Third-party sources (Yelp, Pacer, TrekOhio, Bloggerbill) — no named Helena village park found',
        'No parks found in any source, but Park & Recreation page heading implies a facility exists',
    ],
    'reasoning': (
        'Village of Helena Park & Recreation page exists (villageofhelena.org/park-recreation/) '
        'but contains no park names or details — page is a navigation stub. '
        'Existence of a Parks & Recreation section is an affirmative signal that a facility may exist. '
        'Human contact required before finalizing null: Village of Helena, 504 Church St, 567-482-1545. '
        'Staging as null for pipeline purposes; open flag added.'
    ),
})

# --- T6 All Municipalities — Trail Segments ---
data['tier6_null_evidence'].append({
    'tier': 6,
    'governance_level': 'All T6 municipalities — Trail Segments',
    'entity_types_checked': ['Trail Segment'],
    'result': 'null',
    'sources_checked': [
        'No named municipal trail segment entities found across any municipality',
        'Silver Rock Park Walking Trail staged as Trail (not segmented)',
        'NCIT segments at Biggs-Kettner and Lindsey are SCPD/multi-county (T3)',
    ],
    'reasoning': 'No municipal-level Trail Segment entities found. Null.',
})

# --- T6 All Municipalities — Trail Networks ---
data['tier6_null_evidence'].append({
    'tier': 6,
    'governance_level': 'All T6 municipalities — Trail Networks',
    'entity_types_checked': ['Trail Network'],
    'result': 'null',
    'sources_checked': ['No municipal-managed multi-trail networks found in any municipality'],
    'reasoning': 'No municipal-level Trail Network entities. Null.',
})

# --- T6 All Municipalities — Site Networks ---
data['tier6_null_evidence'].append({
    'tier': 6,
    'governance_level': 'All T6 municipalities — Site Networks',
    'entity_types_checked': ['Site Network'],
    'result': 'null',
    'sources_checked': ['No municipal-managed multi-site networks found in any municipality'],
    'reasoning': 'No municipal-level Site Network entities. Null.',
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'T6 null evidence staged. T6 null blocks: {len(data["tier6_null_evidence"])}. Total records: {len(data["records"])}')
