import yaml, pathlib

f = pathlib.Path('County_Spreadsheets/Sandusky/sandusky_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))
data.setdefault('tier8_null_evidence', [])

# --- Camps, Retreat Centers, Scout Camps ---
data['tier8_null_evidence'].append({
    'tier': 8,
    'governance_level': 'Private camps and retreat centers — Sandusky County',
    'entity_types_checked': ['Site'],
    'result': 'null',
    'sources_checked': [
        'Search: "scout camp Sandusky County Ohio" — no physical BSA/GSA camp in county found; '
        'OSU Extension 4-H camp is at Kelleys Island (Erie County), not Sandusky County',
        'Search: "church camp retreat Sandusky County Ohio" — no church camp with physical Sandusky County address confirmed',
        'Search: "private nature preserve Sandusky County Ohio" — no private nature preserves with public access beyond T7 BSC properties found',
    ],
    'reasoning': (
        'No private camps, retreat centers, or scout camps with a physical Sandusky County address found. '
        'OSU Extension programs use off-county facilities. Null.'
    ),
})

# --- Hunting Preserves (beyond WR Hunt Club) ---
data['tier8_null_evidence'].append({
    'tier': 8,
    'governance_level': 'Private hunting preserves — Sandusky County (beyond WR Hunt Club)',
    'entity_types_checked': ['Site'],
    'result': 'null',
    'sources_checked': [
        'Search: "hunting preserve Sandusky County Ohio" — WR Hunt Club (staged) is the only confirmed result',
        'ODNR licensed hunting preserves search — no additional Sandusky County licensed preserves found beyond WR Hunt Club',
        'Ringneck Ridge (SCPD) has ODNR pheasant releases but is SCPD-managed (T3)',
    ],
    'reasoning': 'WR Hunt Club is the only confirmed hunting preserve in Sandusky County. Null for additional hunting preserves.',
})

# --- Agritourism ---
data['tier8_null_evidence'].append({
    'tier': 8,
    'governance_level': 'Agritourism sites — Sandusky County',
    'entity_types_checked': ['Site'],
    'result': 'null',
    'sources_checked': [
        'Search: "Sandusky County Ohio agritourism" — no identity-bearing agritourism sites with trail systems or named natural areas found',
        'Ohio Agritourism Association directory — no Sandusky County members with recreation/trail components found',
    ],
    'reasoning': 'No qualifying agritourism sites (those with trails, natural areas, or identity-bearing features) found. Null.',
})

# --- GNIS Cross-reference — Staged at T5 but not in OhioGenealogyExpress ---
data['tier8_null_evidence'].append({
    'tier': 8,
    'governance_level': 'GNIS cross-reference — cemeteries staged T5 not on OhioGenealogyExpress list',
    'entity_types_checked': ['Site (Cemetery)'],
    'result': 'noted — no action required for T8',
    'sources_checked': [
        'OhioGenealogyExpress sandusky county list does not include: '
        'Slates Cemetery (Sandusky Twp), Parkhurst Cemetery (Townsend Twp), '
        'Sugar Creek Cemetery (Woodville Twp), LaPrairie Cemetery (Rice Twp), '
        'Faith Lutheran Cemetery (Rice Twp), Green Creek Township Cemetery (unconfirmed). '
        'These were staged at T5 from township official websites. '
        'Absence from OhioGenealogyExpress may indicate they are not transcribed yet, '
        'use alternate names, or were captured under different entries.',
        'PeopleLegacy returned HTTP 403 — USGS GNIS file fallback not executed; '
        'recommend verifying these 6 cemeteries against USGS GNIS Ohio state file in a future session.',
    ],
    'reasoning': (
        'Six T5-staged cemeteries absent from OhioGenealogyExpress. '
        'All were confirmed from authoritative township websites — no T8 action required. '
        'USGS GNIS file cross-check recommended to confirm no additional unstaged cemeteries. '
        'Noted for completeness; not a T8 entity yield.'
    ),
})

# --- York Free Chapel (GNIS disambiguation) ---
data['tier8_null_evidence'].append({
    'tier': 8,
    'governance_level': 'York Free Chapel — GNIS disambiguation',
    'entity_types_checked': ['Site'],
    'result': 'null — likely duplicate of York Chapel Cemetery (T5)',
    'sources_checked': [
        'OhioGenealogyExpress lists both "York Free Chapel" and "York Free Chapel Cemetery" '
        'as separate entries. "York Free Chapel Cemetery" matches the already-staged York Chapel '
        'Cemetery (York Township, T5, County Road 292). "York Free Chapel" (without Cemetery) '
        'likely refers to the same burial ground under a variant name, not a separate entity.',
    ],
    'reasoning': (
        '"York Free Chapel" GNIS entry is assessed as a variant name for the York Chapel Cemetery '
        'already staged at T5. No new T8 entity warranted. If field verification reveals a '
        'separate church building entity, revisit.'
    ),
})

# --- Trails, Trail Segments, Trail Networks, Site Networks, Access Points ---
data['tier8_null_evidence'].append({
    'tier': 8,
    'governance_level': 'All T8 private entities — Trails, Trail Segments, Trail Networks, Site Networks, Access Points',
    'entity_types_checked': ['Trail', 'Trail Segment', 'Trail Network', 'Site Network', 'Access Point'],
    'result': 'null',
    'sources_checked': [
        'No private-managed named trails found beyond Silver Rock Park Walking Trail (T6/Village of Gibsonburg)',
        'No private trail networks found',
        'No private site networks found',
        'No private Access Points distinct from their parent sites found',
        'WR Hunt Club has no named public trail system documented',
        'Schedel Arboretum has garden paths but no named trail system found in sources',
    ],
    'reasoning': (
        'No named private trails, trail segments, trail networks, site networks, or '
        'standalone access points found in Sandusky County at T8. Null.'
    ),
})

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print(f'T8 null evidence staged. T8 null blocks: {len(data["tier8_null_evidence"])}. Total records: {len(data["records"])}')
