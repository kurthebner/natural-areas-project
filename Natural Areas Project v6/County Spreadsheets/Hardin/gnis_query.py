import urllib.request, json, sys, gzip
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

url = 'https://edits.nationalmap.gov/apps/gaz-domestic/graphql'

query = """query SearchNamesList_loadList($appVisibility: AppVisibility!, $cacheBust: Int!, $pagination: GazRecordsSearchPagination!, $filter: GazRecordsSearchFilter!) {
  connection: searchGazRecords(appVisibility: $appVisibility, cacheBust: $cacheBust, pagination: $pagination, filter: $filter) {
    totalCount
    pageInfo { hasNextPage }
    edges {
      node {
        gazId
        officialNameValue
        gazFeatureClassificationName
        derivedShapeSequencePointGeoJSONs
      }
    }
  }
}"""

payload = {
    'operationName': 'SearchNamesList_loadList',
    'variables': {
        'appVisibility': 'Public',
        'cacheBust': 4,
        'pagination': {
            'first': 1000,
            'orderBy': [{'column': 'OfficialNameValue', 'direction': 'Asc'}]
        },
        'filter': {
            'name': '',
            'namesSearchMode': 'IncludesKeywords',
            'includeVariantNames': False,
            'gazRecordDesignationCodes': [],
            'includeGazRecordDesignationCode': False,
            'gazFeatureClassifications': [],
            'bgnDecisionTypeCodes': [],
            'includeBgnDecisionTypeCode': False,
            'bgnDecisionDate': {},
            'featureEditDate': {},
            'dateAdded': {},
            'stateOrEquivalentId': 'affc992f-9a58-5953-8f01-98c102538ded',
            'countyOrEquivalentId': 'cc09a323-8165-5b12-97d4-8d51f0b1c742',
            'cellId': None,
            'isUnknownCoords': False,
            'isConflated': None,
            'censusCode': {'greaterThan': None, 'lessThan': None},
            'gsaCode': {'greaterThan': None, 'lessThan': None},
            'opmCode': {'greaterThan': None, 'lessThan': None}
        }
    },
    'query': query
}

body = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(url, data=body, headers={
    'Content-Type': 'application/json',
    'User-Agent': 'NaturalAreasProject/6.0',
    'Accept': 'application/json',
})

with urllib.request.urlopen(req, timeout=30) as r:
    raw = r.read()
    text = gzip.decompress(raw).decode('utf-8') if raw[:2] == b'\x1f\x8b' else raw.decode('utf-8')

data = json.loads(text)
if 'errors' in data:
    print('GraphQL errors:', data['errors'])
    sys.exit(1)

conn = data['data']['connection']
print(f'Total Hardin County features: {conn["totalCount"]}')

cems = []
for e in conn['edges']:
    node = e['node']
    if node['gazFeatureClassificationName'] == 'Cemetery':
        name = node['officialNameValue']
        gaz_id = node['gazId']
        geo = node['derivedShapeSequencePointGeoJSONs']
        lat, lon = None, None
        if geo:
            # geo is a list of GeoJSON point strings; take first one
            first = geo[0] if isinstance(geo, list) else geo
            if isinstance(first, str):
                pt = json.loads(first)
                coords = pt.get('coordinates', [])
                if coords:
                    lon, lat = coords[0], coords[1]
            elif isinstance(first, dict):
                coords = first.get('coordinates', [])
                if coords:
                    lon, lat = coords[0], coords[1]
        cems.append((name, gaz_id, lat, lon))

print(f'Cemeteries: {len(cems)}')
print()
for name, gaz_id, lat, lon in sorted(cems):
    print(f'  {name:<42} GNIS:{gaz_id}  {lat}, {lon}')
