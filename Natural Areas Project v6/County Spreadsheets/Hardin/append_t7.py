import yaml, pathlib

f = pathlib.Path(r'D:\users\user1\Documents\CP Projects\Natural Areas Project v6\County Spreadsheets\Hardin\hardin_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))

t7_records = [

{
    'entity_type_result': {
        'tier': 7,
        'governance_level': 'Conservancy & Land Trust',
        'entity_type': 'All',
        'result': 'null',
        'sources_checked': [
            'West Central Ohio Land Conservancy (WCOLC) — wcolc.org; confirmed serves Hardin County; ~3,148 acres protected across 7-county service area; all holdings are agricultural conservation easements; no named public-access natural area preserves found in Hardin County',
            'The Nature Conservancy Ohio — nature.org/ohio; no TNC preserves in Hardin County; closest is Big Darby headwaters (Logan County) and Kitty Todd (Lucas County)',
            'Black Swamp Conservancy (BSC) — service area does not include Hardin County (Erie, Fulton, Henry, Lucas, Ottawa, Putnam, Sandusky, Seneca, Van Wert, Williams, Wood)',
            'North Central Ohio Land Conservancy (NCOLC) — ncolc.org; serves Richland County area; not applicable to Hardin County',
            'ONAPA preserve map — onapa.org/preserve-map.html; ONAPA provides stewardship for ODNR state nature preserves; Lawrence Woods SNP already cataloged at T2; ONAPA is not a separate landowner',
            'Simon Kenton Trail/Pathfinders — trail currently ends in Logan/Champaign Counties; no Hardin County segment constructed or formally designated',
            'Land Trust Alliance directory — landtrustalliance.org; only WCOLC identified as serving Hardin County',
            'General WebSearch for Hardin County land trusts and conservation nonprofits — no additional organizations found',
        ],
        'reasoning': (
            'No nonprofit conservation organization holds named, identity-bearing, publicly accessible '
            'natural area Sites in Hardin County. WCOLC is the primary land trust serving Hardin County '
            'but holds only agricultural conservation easements (consistent with prior county run results '
            'for Paulding and Putnam Counties). All other regional land trusts are outside the county '
            'service area. Simon Kenton Trail planned extension into Hardin County is not yet constructed '
            '(unconfirmed baseline seed). No T7 entities for Hardin County.'
        ),
    }
},

]

data.setdefault('records', [])
data['records'].extend(t7_records)
f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False), encoding='utf-8')
print(f'Total records now: {len(data["records"])}')
