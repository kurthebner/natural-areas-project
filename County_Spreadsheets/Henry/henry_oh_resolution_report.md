# Henry County, OH — Stage 1 Resolution Report
**Run ID:** `henry_oh_2026_04_20`
**Resolution Date:** 2026-04-26
**Records Input:** 50
**Entities Resolved:** 50
**Merge Clusters Formed:** 0
**Singletons:** 50
**Review Sets:** 104

## Entity Counts

| Entity Type | Count |
|-------------|-------|
| Site | 31 |
| Trail | 7 |
| Trail Segment | 6 |
| Access Point | 6 |
| **TOTAL** | **50** |

## ID Assignments

- `HEN_S_001` — Site — **Big Creek Park** — parent: —
- `HEN_S_002` — Site — **Deshler Crossroads Park** — parent: —
- `HEN_S_003` — Site — **Deshler Reservoir Park** — parent: —
- `HEN_S_004` — Site — **Dr. John Bloomfield Home & Carriage House Museum** — parent: —
- `HEN_S_005` — Site — **East Riverdowns Park** — parent: —
- `HEN_S_006` — Site — **Florida Wildlife Area** — parent: —
- `HEN_S_007` — Site — **Fredrick Steward Memorial Park** — parent: —
- `HEN_S_008` — Site — **Glenwood Park** — parent: —
- `HEN_S_009` — Site — **Hamler Community Park** — parent: —
- `HEN_S_010` — Site — **Hamler Memorial Park** — parent: —
- `HEN_S_011` — Site — **Henry County Fairgrounds** — parent: —
- `HEN_S_012` — Site — **Henry County Historical Society Fairgrounds Historic Complex** — parent: —
- `HEN_S_013` — Site — **Henry County Wildlife Area 1** — parent: —
- `HEN_S_014` — Site — **Henry County Wildlife Area 2** — parent: —
- `HEN_S_015` — Site — **Henry County Wildlife Area 3** — parent: —
- `HEN_S_016` — Site — **Holgate Village Park** — parent: —
- `HEN_S_017` — Site — **Liberty Center Firemen's Park** — parent: —
- `HEN_S_018` — Site — **Mary Jane Thurston State Park** — parent: —
- `HEN_S_019` — Site — **Maumee State Scenic River** — parent: —
- `HEN_S_020` — Site — **Meyerholtz Wildlife Park** — parent: —
- `HEN_S_021` — Site — **Napoleon Dog Park** — parent: —
- `HEN_S_022` — Site — **New Bavaria Park** — parent: —
- `HEN_S_023` — Site — **North Turkeyfoot Wildlife Area** — parent: —
- `HEN_S_024` — Site — **Oakwood Park** — parent: —
- `HEN_S_025` — Site — **Oberhaus Park** — parent: —
- `HEN_S_026` — Site — **Old School Park** — parent: —
- `HEN_S_027` — Site — **Ritter Park** — parent: —
- `HEN_S_028` — Site — **Swearingen Park** — parent: —
- `HEN_S_029` — Site — **Veterans Memorial Park** — parent: —
- `HEN_S_030` — Site — **Vorwerk Park** — parent: —
- `HEN_S_031` — Site — **Wayne Park** — parent: —
- `HEN_T_001` — Trail — **Blue Trail** — parent: {'parent_site_id': 'HEN_S_018'}
- `HEN_T_002` — Trail — **Miami & Erie Canal Towpath Hiking Trail** — parent: —
- `HEN_T_003` — Trail — **Orange Trail** — parent: {'parent_site_id': 'HEN_S_018'}
- `HEN_T_004` — Trail — **Storybook Trail** — parent: {'parent_site_id': 'HEN_S_018'}
- `HEN_T_005` — Trail — **Tow Path** — parent: {'parent_site_id': 'HEN_S_018'}
- `HEN_T_006` — Trail — **Wabash Cannonball Trail** — parent: —
- `HEN_T_007` — Trail — **Yellow Trail** — parent: {'parent_site_id': 'HEN_S_018'}
- `HEN_TS_001` — Trail Segment — **Damascus Leg — Miami & Erie Canal Towpath** — parent: {'parent_trail_id': 'HEN_T_002'}
- `HEN_TS_002` — Trail Segment — **Independence Leg — Miami & Erie Canal Towpath** — parent: {'parent_trail_id': 'HEN_T_002'}
- `HEN_TS_003` — Trail Segment — **Napoleon Leg — Miami & Erie Canal Towpath** — parent: {'parent_trail_id': 'HEN_T_002'}
- `HEN_TS_004` — Trail Segment — **Renegade Leg — Miami & Erie Canal Towpath** — parent: {'parent_trail_id': 'HEN_T_002'}
- `HEN_TS_005` — Trail Segment — **Wabash Cannonball Trail - South Fork** — parent: {'parent_trail_id': 'HEN_T_006'}
- `HEN_TS_006` — Trail Segment — **WideWater Section — Miami & Erie Canal Towpath** — parent: {'parent_trail_id': 'HEN_T_002'}
- `HEN_AP_001` — Access Point — **Mary Jane Thurston State Park Boat Launch Ramp** — parent: {'parent_entity_id': 'HEN_S_018', 'parent_entity_type': 'Site'}
- `HEN_AP_002` — Access Point — **Mary Jane Thurston State Park Marina** — parent: {'parent_entity_id': 'HEN_S_018', 'parent_entity_type': 'Site'}
- `HEN_AP_003` — Access Point — **Oberhaus Park Boat Dock** — parent: {'parent_entity_id': 'HEN_S_025', 'parent_entity_type': 'Site'}
- `HEN_AP_004` — Access Point — **Ritter Park Boat Launch** — parent: {'parent_entity_id': 'HEN_S_027', 'parent_entity_type': 'Site'}
- `HEN_AP_005` — Access Point — **WCT Henry CR 6C Trailhead** — parent: {'parent_entity_id': 'HEN_T_006', 'parent_entity_type': 'Trail'}
- `HEN_AP_006` — Access Point — **Wabash Cannonball Trail Liberty Center Depot Trailhead** — parent: {'parent_entity_id': 'HEN_T_006', 'parent_entity_type': 'Trail'}

## Review Sets

- **Site** score=77.6: ['North Turkeyfoot Wildlife Area', 'Florida Wildlife Area'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=69.8: ['North Turkeyfoot Wildlife Area', 'Henry County Wildlife Area 1'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=69.8: ['North Turkeyfoot Wildlife Area', 'Henry County Wildlife Area 2'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=69.8: ['North Turkeyfoot Wildlife Area', 'Henry County Wildlife Area 3'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=51.4: ['North Turkeyfoot Wildlife Area', 'Meyerholtz Wildlife Park'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=71.1: ['Florida Wildlife Area', 'Henry County Wildlife Area 1'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=71.1: ['Florida Wildlife Area', 'Henry County Wildlife Area 2'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=71.1: ['Florida Wildlife Area', 'Henry County Wildlife Area 3'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=51.4: ['Florida Wildlife Area', 'Meyerholtz Wildlife Park'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=83.6: ['Henry County Wildlife Area 1', 'Henry County Wildlife Area 2'] — HARD SEPARATED (§10.5): Numbered-name hard separation: 'Henry County Wildlife Area 1' vs 'Henry County Wildlife Area 2' — same stem 'Henry County Wildlife Area', different ordinal
- **Site** score=83.6: ['Henry County Wildlife Area 1', 'Henry County Wildlife Area 3'] — HARD SEPARATED (§10.5): Numbered-name hard separation: 'Henry County Wildlife Area 1' vs 'Henry County Wildlife Area 3' — same stem 'Henry County Wildlife Area', different ordinal
- **Site** score=83.6: ['Henry County Wildlife Area 2', 'Henry County Wildlife Area 3'] — HARD SEPARATED (§10.5): Numbered-name hard separation: 'Henry County Wildlife Area 2' vs 'Henry County Wildlife Area 3' — same stem 'Henry County Wildlife Area', different ordinal
- **Site** score=87.0: ['Oakwood Park', 'Glenwood Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0045, lon_diff=0.0423 > 0.01
- **Site** score=74.3: ['Oakwood Park', 'Ritter Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0117, lon_diff=0.0457 > 0.01
- **Site** score=79.0: ['Oakwood Park', 'Oberhaus Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0111, lon_diff=0.0343 > 0.01
- **Site** score=74.1: ['Oakwood Park', 'Swearingen Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0063, lon_diff=0.0204 > 0.01
- **Site** score=73.3: ['Oakwood Park', 'East Riverdowns Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0016, lon_diff=0.0173 > 0.01
- **Site** score=74.8: ['Oakwood Park', 'Napoleon Dog Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0010, lon_diff=0.0199 > 0.01
- **Site** score=66.8: ['Oakwood Park', 'Wayne Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0247, lon_diff=0.0542 > 0.01
- **Site** score=75.5: ['Oakwood Park', 'Vorwerk Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0192, lon_diff=0.0111 > 0.01
- **Site** score=69.4: ['Oakwood Park', 'Meyerholtz Wildlife Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0200, lon_diff=0.0525 > 0.01
- **Site** score=50.5: ['Oakwood Park', 'Old School Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.1431, lon_diff=0.0339 > 0.01
- **Site** score=77.2: ['Glenwood Park', 'Ritter Park'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=75.3: ['Glenwood Park', 'Oberhaus Park'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=79.4: ['Glenwood Park', 'Swearingen Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0018, lon_diff=0.0218 > 0.01
- **Site** score=72.8: ['Glenwood Park', 'East Riverdowns Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0061, lon_diff=0.0249 > 0.01
- **Site** score=74.3: ['Glenwood Park', 'Napoleon Dog Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0034, lon_diff=0.0223 > 0.01
- **Site** score=65.9: ['Glenwood Park', 'Wayne Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0202, lon_diff=0.0120 > 0.01
- **Site** score=71.7: ['Glenwood Park', 'Vorwerk Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0236, lon_diff=0.0534 > 0.01
- **Site** score=50.5: ['Glenwood Park', 'Old School Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.1386, lon_diff=0.0084 > 0.01
- **Site** score=80.1: ['Ritter Park', 'Oberhaus Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0006, lon_diff=0.0114 > 0.01
- **Site** score=81.1: ['Ritter Park', 'Swearingen Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0054, lon_diff=0.0253 > 0.01
- **Site** score=79.0: ['Ritter Park', 'East Riverdowns Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0133, lon_diff=0.0284 > 0.01
- **Site** score=67.2: ['Ritter Park', 'Napoleon Dog Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0107, lon_diff=0.0258 > 0.01
- **Site** score=67.9: ['Ritter Park', 'Wayne Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0130, lon_diff=0.0085 > 0.01
- **Site** score=81.8: ['Ritter Park', 'Vorwerk Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0309, lon_diff=0.0568 > 0.01
- **Site** score=70.0: ['Ritter Park', 'Meyerholtz Wildlife Park'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=76.8: ['Oberhaus Park', 'Swearingen Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0049, lon_diff=0.0139 > 0.01
- **Site** score=76.2: ['Oberhaus Park', 'East Riverdowns Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0127, lon_diff=0.0170 > 0.01
- **Site** score=69.9: ['Oberhaus Park', 'Napoleon Dog Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0101, lon_diff=0.0144 > 0.01
- **Site** score=65.9: ['Oberhaus Park', 'Wayne Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0135, lon_diff=0.0199 > 0.01
- **Site** score=77.6: ['Oberhaus Park', 'Vorwerk Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0303, lon_diff=0.0454 > 0.01
- **Site** score=68.7: ['Oberhaus Park', 'Meyerholtz Wildlife Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0089, lon_diff=0.0182 > 0.01
- **Site** score=50.6: ['Oberhaus Park', 'New Bavaria Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.1767, lon_diff=0.0346 > 0.01
- **Site** score=79.9: ['Swearingen Park', 'East Riverdowns Park'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=71.4: ['Swearingen Park', 'Napoleon Dog Park'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=67.4: ['Swearingen Park', 'Wayne Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0184, lon_diff=0.0338 > 0.01
- **Site** score=75.7: ['Swearingen Park', 'Vorwerk Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0254, lon_diff=0.0315 > 0.01
- **Site** score=51.9: ['Swearingen Park', 'New Bavaria Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.1816, lon_diff=0.0485 > 0.01
- **Site** score=73.2: ['East Riverdowns Park', 'Napoleon Dog Park'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=61.0: ['East Riverdowns Park', 'Wayne Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0263, lon_diff=0.0369 > 0.01
- **Site** score=71.4: ['East Riverdowns Park', 'Vorwerk Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0176, lon_diff=0.0284 > 0.01
- **Site** score=68.7: ['East Riverdowns Park', 'Meyerholtz Wildlife Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0217, lon_diff=0.0352 > 0.01
- **Site** score=52.8: ['East Riverdowns Park', 'Veterans Memorial Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0554, lon_diff=0.0984 > 0.01
- **Site** score=65.7: ['Napoleon Dog Park', 'Wayne Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0236, lon_diff=0.0343 > 0.01
- **Site** score=69.8: ['Napoleon Dog Park', 'Vorwerk Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0202, lon_diff=0.0310 > 0.01
- **Site** score=51.0: ['Napoleon Dog Park', 'Old School Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.1421, lon_diff=0.0139 > 0.01
- **Site** score=70.5: ['Wayne Park', 'Vorwerk Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0438, lon_diff=0.0653 > 0.01
- **Site** score=61.5: ['Wayne Park', 'Meyerholtz Wildlife Park'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=52.0: ['Meyerholtz Wildlife Park', 'Holgate Village Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.1209, lon_diff=0.0254 > 0.01
- **Site** score=83.3: ['Deshler Crossroads Park', 'Deshler Reservoir Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0141, lon_diff=0.0080 > 0.01
- **Site** score=57.1: ['Deshler Crossroads Park', 'Old School Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0308, lon_diff=0.2400 > 0.01
- **Site** score=58.1: ['Deshler Crossroads Park', "Liberty Center Firemen's Park"] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=57.3: ['Deshler Crossroads Park', 'Veterans Memorial Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.2310, lon_diff=0.1251 > 0.01
- **Site** score=65.8: ['Deshler Crossroads Park', 'Hamler Memorial Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0135, lon_diff=0.1430 > 0.01
- **Site** score=55.8: ['Deshler Crossroads Park', 'Big Creek Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.1511, lon_diff=0.0462 > 0.01
- **Site** score=54.8: ['Deshler Crossroads Park', 'New Bavaria Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0139, lon_diff=0.2750 > 0.01
- **Site** score=57.9: ['Deshler Reservoir Park', 'Old School Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0449, lon_diff=0.2320 > 0.01
- **Site** score=57.4: ['Deshler Reservoir Park', "Liberty Center Firemen's Park"] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=56.7: ['Deshler Reservoir Park', 'Fredrick Steward Memorial Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.2407, lon_diff=0.1030 > 0.01
- **Site** score=58.2: ['Deshler Reservoir Park', 'Veterans Memorial Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.2450, lon_diff=0.1171 > 0.01
- **Site** score=70.1: ['Deshler Reservoir Park', 'Hamler Memorial Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0276, lon_diff=0.1350 > 0.01
- **Site** score=58.6: ['Deshler Reservoir Park', 'Big Creek Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.1652, lon_diff=0.0382 > 0.01
- **Site** score=53.8: ['Deshler Reservoir Park', 'New Bavaria Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0001, lon_diff=0.2671 > 0.01
- **Site** score=76.3: ['Old School Park', 'Holgate Village Park'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=53.4: ['Old School Park', 'Fredrick Steward Memorial Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.1958, lon_diff=0.1290 > 0.01
- **Site** score=56.9: ['Old School Park', 'Veterans Memorial Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.2001, lon_diff=0.1149 > 0.01
- **Site** score=58.2: ['Old School Park', 'Hamler Memorial Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0173, lon_diff=0.0970 > 0.01
- **Site** score=58.4: ['Old School Park', 'Big Creek Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.1203, lon_diff=0.1938 > 0.01
- **Site** score=57.0: ['Holgate Village Park', "Liberty Center Firemen's Park"] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=54.7: ['Holgate Village Park', 'Fredrick Steward Memorial Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.1936, lon_diff=0.1223 > 0.01
- **Site** score=57.8: ['Holgate Village Park', 'Veterans Memorial Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.1980, lon_diff=0.1082 > 0.01
- **Site** score=61.3: ['Holgate Village Park', 'Hamler Memorial Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0195, lon_diff=0.0903 > 0.01
- **Site** score=60.0: ['Holgate Village Park', 'Big Creek Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.1181, lon_diff=0.1871 > 0.01
- **Site** score=57.4: ['Holgate Village Park', 'New Bavaria Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0469, lon_diff=0.0417 > 0.01
- **Site** score=77.9: ["Liberty Center Firemen's Park", 'Fredrick Steward Memorial Park'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=79.2: ["Liberty Center Firemen's Park", 'Veterans Memorial Park'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=57.7: ["Liberty Center Firemen's Park", 'Hamler Memorial Park'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=57.6: ["Liberty Center Firemen's Park", 'Big Creek Park'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=87.7: ['Fredrick Steward Memorial Park', 'Veterans Memorial Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0043, lon_diff=0.0141 > 0.01
- **Site** score=63.4: ['Fredrick Steward Memorial Park', 'Hamler Memorial Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.2131, lon_diff=0.0320 > 0.01
- **Site** score=50.4: ['Fredrick Steward Memorial Park', 'New Bavaria Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.2405, lon_diff=0.1641 > 0.01
- **Site** score=69.9: ['Veterans Memorial Park', 'Hamler Memorial Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.2174, lon_diff=0.0178 > 0.01
- **Site** score=52.3: ['Veterans Memorial Park', 'New Bavaria Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.2449, lon_diff=0.1499 > 0.01
- **Site** score=61.8: ['Hamler Memorial Park', 'Big Creek Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.1376, lon_diff=0.0968 > 0.01
- **Site** score=59.0: ['Hamler Memorial Park', 'New Bavaria Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.0274, lon_diff=0.1321 > 0.01
- **Site** score=53.2: ['Hamler Memorial Park', 'Hamler Community Park'] — Score between REVIEW and MERGE threshold — requires human review
- **Site** score=60.5: ['Big Creek Park', 'New Bavaria Park'] — HARD SEPARATED (§10.5): GPS hard separation: lat_diff=0.1650, lon_diff=0.2289 > 0.01
- **Site** score=59.0: ['Henry County Historical Society Fairgrounds Historic Complex', 'Henry County Fairgrounds'] — Score between REVIEW and MERGE threshold — requires human review
- **Trail** score=50.5: ['Blue Trail', 'Orange Trail'] — Score between REVIEW and MERGE threshold — requires human review
- **Trail** score=50.5: ['Blue Trail', 'Yellow Trail'] — Score between REVIEW and MERGE threshold — requires human review
- **Trail Segment** score=52.3: ['Renegade Leg — Miami & Erie Canal Towpath', 'Napoleon Leg — Miami & Erie Canal Towpath'] — Score between REVIEW and MERGE threshold — requires human review
- **Trail Segment** score=51.0: ['Renegade Leg — Miami & Erie Canal Towpath', 'Damascus Leg — Miami & Erie Canal Towpath'] — Score between REVIEW and MERGE threshold — requires human review
- **Trail Segment** score=51.0: ['Napoleon Leg — Miami & Erie Canal Towpath', 'Damascus Leg — Miami & Erie Canal Towpath'] — Score between REVIEW and MERGE threshold — requires human review