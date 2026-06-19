import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('tier3_null_evidence', [])

data['tier3_null_evidence'].append({
    'tier': 3,
    'governance_level': 'Sandusky County Soil & Water Conservation District (SWCD)',
    'entity_types_checked': ['Site', 'Trail', 'Trail Segment', 'Trail Network', 'Site Network', 'Access Point'],
    'result': 'null',
    'sources_checked': ['sanduskycoswcd.org — home page and program listings'],
    'reasoning': (
        'SWCD describes itself as a liaison between private landowners and federal agencies; '
        'focuses on conservation practices and programs for agricultural producers. No land '
        'holdings, nature preserves, conservation easements, or managed natural areas found. Null.'
    )
})

data['tier3_null_evidence'].append({
    'tier': 3,
    'governance_level': 'Ohio Auditor — Joint Recreation Districts',
    'entity_types_checked': ['Site', 'Trail', 'Trail Segment', 'Trail Network', 'Site Network', 'Access Point'],
    'result': 'null',
    'sources_checked': ['Ohio Auditor Entity Search — Sandusky County, Joint Recreation Districts'],
    'reasoning': 'No Joint Recreation Districts found in Sandusky County per Ohio Auditor pre-enumeration. Null.'
})

data['tier3_null_evidence'].append({
    'tier': 3,
    'governance_level': 'Ohio Auditor — Conservancy Districts',
    'entity_types_checked': ['Site', 'Trail', 'Trail Segment', 'Trail Network', 'Site Network', 'Access Point'],
    'result': 'null',
    'sources_checked': ['Ohio Auditor Entity Search — Sandusky County, Conservancy Districts'],
    'reasoning': 'No Conservancy Districts found in Sandusky County per Ohio Auditor pre-enumeration. Null.'
})

data['tier3_null_evidence'].append({
    'tier': 3,
    'governance_level': 'Ohio Auditor — Watershed Districts',
    'entity_types_checked': ['Site', 'Trail', 'Trail Segment', 'Trail Network', 'Site Network', 'Access Point'],
    'result': 'null',
    'sources_checked': ['Ohio Auditor Entity Search — Sandusky County, Watershed Districts'],
    'reasoning': 'No Watershed Districts found in Sandusky County per Ohio Auditor pre-enumeration. Null.'
})

data['tier3_null_evidence'].append({
    'tier': 3,
    'governance_level': 'Ohio Auditor — Special Districts (other)',
    'entity_types_checked': ['Site', 'Trail', 'Trail Segment', 'Trail Network', 'Site Network', 'Access Point'],
    'result': 'null',
    'sources_checked': ['Ohio Auditor Entity Search — Sandusky County, Special Districts'],
    'reasoning': 'No additional Special Districts with natural area management found in Sandusky County. Null.'
})

data['tier3_null_evidence'].append({
    'tier': 3,
    'governance_level': 'Trail Networks (District-managed)',
    'entity_types_checked': ['Trail Network'],
    'result': 'null',
    'sources_checked': ['SCPD lovemyparks.com — no multi-trail network designation found beyond NCIT (staged as Trail)'],
    'reasoning': (
        'No district-managed Trail Networks in Sandusky County. NCIT is a Trail (not a Trail Network '
        'for this county segment). White Star trail system is a single loop. Null.'
    )
})

data['tier3_null_evidence'].append({
    'tier': 3,
    'governance_level': 'Site Networks (District-managed)',
    'entity_types_checked': ['Site Network'],
    'result': 'null',
    'sources_checked': ['SCPD lovemyparks.com — properties listed individually; no multi-site network designation found'],
    'reasoning': 'No district-level Site Networks in Sandusky County. SCPD properties are individually designated. Null.'
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'Done. T3 null blocks: {len(data["tier3_null_evidence"])}, Total records: {len(data["records"])}')
