import yaml, pathlib

f = pathlib.Path(r'D:\users\user1\Documents\CP Projects\Natural Areas Project v6\County Spreadsheets\Hardin\hardin_ohio_raw_discovery.yaml')
data = yaml.safe_load(f.read_text(encoding='utf-8'))

t4_records = [

# --- T4 ALL ENTITY TYPES: NULL ---
{
    'entity_type_result': {
        'tier': 4,
        'governance_level': 'County',
        'entity_type': 'All',
        'result': 'null',
        'sources_checked': [
            'hardincountyohio.gov — county homepage; no parks/recreation department page; no county park links; county website is primarily administrative (commissioners, auditor, health, SWCD)',
            'hardincountyohio.gov — SWCD section (Silver Creek Center already captured at T3 per IMP-004)',
            'NRHP Hardin County — 7 listings (Wikipedia): Ada Pennsylvania Station and Railroad Park (Ada, village-managed T6); Hardin County Courthouse (downtown Kenton, not natural area); Kenton Courthouse Square Historic District (downtown, not natural area); Kenton Public Library (Carnegie library, not natural area); Mount Victory Historic District (village, not natural area); North Main-North Detroit Street Historic District (residential, not natural area); Zimmerman Kame (McDonald Township — NRHP 1974, glacial kame/archaeological site, private farmland, tree-covered, no public access infrastructure, no county ownership confirmed)',
            'Saulisberry Park / France Lake — 200-acre City of Kenton facility at 13344 SR-67W; administered by City of Kenton parks and recreation; former stone quarry with lake; T6 entity; deferred to Tier 6',
            'Hardin County Fairgrounds — county-owned fair facility; agricultural/event venue; not a natural area; out of scope',
            'County financial records — E02 TRAILER & RECREATIONAL PARK enterprise fund; likely Hardin County Fairgrounds RV parking or campground; agricultural fair facility; not a natural area',
            'Veterans Memorial Park District — already captured at T3 as statutory park district',
            'Hardin County Chamber/Tourism — hardinvisit.com check: no county-managed natural area Sites identified beyond entities already captured at higher tiers',
        ],
        'reasoning': (
            'Hardin County government does not operate a county parks department or county-owned natural area Sites independent of the Veterans Memorial Park District (T3). '
            'NRHP check complete: Zimmerman Kame is on private agricultural land with no public access; all other NRHP listings are historic urban structures without natural area character. '
            'Saulisberry Park/France Lake (200 ac, quarry lake) is City of Kenton-managed; deferred to T6. '
            'County fairgrounds excluded (not a natural area). '
            'No T4 natural area Sites, Trailthings, Site Networks, or Access Points.'
        ),
        'deferred_to_t6': [
            'Saulisberry Park / France Lake Campground — 13344 SR-67W, Kenton; City of Kenton parks and recreation; 200 acres; France Lake (former quarry); fishing, camping, hiking, playground, dirt bike track; eBird hotspot L3661530; no swimming; permit required for lake activities',
            'Ada Pennsylvania Station and Railroad Park — 112 E. Central Ave., Ada; NRHP 1998; Village of Ada entity; confirm village governance at T6',
        ],
    }
},

]

data.setdefault('records', [])
data['records'].extend(t4_records)
f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False), encoding='utf-8')
print(f'Total records now: {len(data["records"])}')
