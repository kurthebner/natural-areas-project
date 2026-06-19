# Henry County, OH — Stage 2 Normalization Report
**Run ID:** henry_oh_2026_04_20  
**Date:** 2026-04-26  
**Engine:** Normalization Engine v5.8 + Site v5.9 + Trail v5.2 + TS v5.1 + AP v5.1

## Summary

| | Count |
|---|---|
| Normalized entities | 38 |
| Held (GPS missing, IMP-069) | 12 |
| Fatal rejects | 0 |
| Vocabulary gate violations | 0 |

## Normalized Entities

### Sites

| ID | Name | Category | Subtype | Status | GPS |
|---|---|---|---|---|---|
| HEN_S_001 | Big Creek Park | Park |  | Active | 41.368215, -83.93994 |
| HEN_S_002 | Deshler Crossroads Park | Park |  | Active | 41.217095, -83.893776 |
| HEN_S_003 | Deshler Reservoir Park | Park |  | Active | 41.20304, -83.901743 |
| HEN_S_005 | East Riverdowns Park | Park |  | Active | 41.392628, -84.117267 |
| HEN_S_007 | Fredrick Steward Memorial Park | Park |  | Active | 41.443713, -84.004747 |
| HEN_S_008 | Glenwood Park | Park |  | Active | 41.386553, -84.142184 |
| HEN_S_010 | Hamler Memorial Park | Park |  | Active | 41.230605, -84.036733 |
| HEN_S_016 | Holgate Village Park | Park |  | Active | 41.250101, -84.127079 |
| HEN_S_020 | Meyerholtz Wildlife Park | Park |  | Active | 41.370975, -84.152449 |
| HEN_S_021 | Napoleon Dog Park | Park | Dog Park | Active | 41.390001, -84.119848 |
| HEN_S_022 | New Bavaria Park | Park |  | Active | 41.20317, -84.168809 |
| HEN_S_024 | Oakwood Park | Park |  | Active | 41.391007, -84.099919 |
| HEN_S_025 | Oberhaus Park | Park |  | Active | 41.379899, -84.134252 |
| HEN_S_026 | Old School Park | Park |  | Active | 41.247915, -84.133775 |
| HEN_S_027 | Ritter Park | Park |  | Active | 41.37933, -84.145657 |
| HEN_S_028 | Swearingen Park | Park |  | Active | 41.384757, -84.120347 |
| HEN_S_029 | Veterans Memorial Park | Park |  | Active | 41.448054, -84.018893 |
| HEN_S_030 | Vorwerk Park | Park |  | Active | 41.410194, -84.088819 |
| HEN_S_031 | Wayne Park | Park |  | Active | 41.366357, -84.154157 |

### Trails

| ID | Name | Use Type | Surface | Origin | Difficulty |
|---|---|---|---|---|---|
| HEN_T_001 | Blue Trail |  |  |  | Easy |
| HEN_T_002 | Miami & Erie Canal Towpath Hiking Trail |  |  | Canal Towpath |  |
| HEN_T_003 | Orange Trail |  |  |  | Easy |
| HEN_T_004 | Storybook Trail | Hiking |  |  | Easy |
| HEN_T_005 | Tow Path |  |  | Canal Towpath | Easy |
| HEN_T_006 | Wabash Cannonball Trail |  |  | Rail Trail |  |
| HEN_T_007 | Yellow Trail |  |  |  | Easy |

### Trail Segments

| ID | Name | Parent Trail | Surface | Counties |
|---|---|---|---|---|
| HEN_TS_001 | Damascus Leg | HEN_T_002 |  | Henry |
| HEN_TS_002 | Independence Leg | HEN_T_002 |  | Defiance;Henry |
| HEN_TS_003 | Napoleon Leg | HEN_T_002 |  | Henry |
| HEN_TS_004 | Renegade Leg | HEN_T_002 |  | Henry |
| HEN_TS_005 | Wabash Cannonball Trail - South Fork | HEN_T_006 | Natural Surface | Henry;Lucas |
| HEN_TS_006 | WideWater Section | HEN_T_002 |  | Henry;Wood |

### Access Points

| ID | Name | Type | Parent | GPS |
|---|---|---|---|---|
| HEN_AP_001 | Mary Jane Thurston State Park Boat Launch Ramp | Boat Ramp | HEN_S_018 | — |
| HEN_AP_002 | Mary Jane Thurston State Park Marina | Boat Launch | HEN_S_018 | — |
| HEN_AP_003 | Oberhaus Park Boat Dock | Boat Launch | HEN_S_025 | 41.379899, -84.134252 |
| HEN_AP_004 | Ritter Park Boat Launch | Boat Launch | HEN_S_027 | 41.37933, -84.145657 |
| HEN_AP_005 | WCT Henry CR 6C Trailhead | Trailhead | HEN_T_006 | 41.450715, -83.990451 |
| HEN_AP_006 | Wabash Cannonball Trail Liberty Center Depot Trailhead | Trailhead | HEN_T_006 | 41.443728, -84.009326 |

## Held Entities (GPS Missing — IMP-069)

| ID | Name | Hold Reason |
|---|---|---|
| HEN_S_004 | Dr. John Bloomfield Home & Carriage House Museum | gps_missing |
| HEN_S_006 | Florida Wildlife Area | gps_missing |
| HEN_S_009 | Hamler Community Park | gps_missing |
| HEN_S_011 | Henry County Fairgrounds | gps_missing |
| HEN_S_012 | Henry County Historical Society Fairgrounds Historic Complex | gps_missing |
| HEN_S_013 | Henry County Wildlife Area 1 | gps_missing |
| HEN_S_014 | Henry County Wildlife Area 2 | gps_missing |
| HEN_S_015 | Henry County Wildlife Area 3 | gps_missing |
| HEN_S_017 | Liberty Center Firemen's Park | gps_missing |
| HEN_S_018 | Mary Jane Thurston State Park | gps_missing |
| HEN_S_019 | Maumee State Scenic River | gps_missing |
| HEN_S_023 | North Turkeyfoot Wildlife Area | gps_missing |

## Normalization Decisions

### Category Inference

| Entity ID | Name | Category | Subtype | Source |
|---|---|---|---|---|
| HEN_S_001 | — | Park |  | default_Park |
| HEN_S_002 | — | Park |  | default_Park |
| HEN_S_003 | — | Park |  | default_Park |
| HEN_S_005 | — | Park |  | default_Park |
| HEN_S_007 | — | Park |  | default_Park |
| HEN_S_008 | — | Park |  | default_Park |
| HEN_S_010 | — | Park |  | default_Park |
| HEN_S_016 | — | Park |  | default_Park |
| HEN_S_020 | — | Park |  | default_Park |
| HEN_S_021 | — | Park | Dog Park | default_Park |
| HEN_S_022 | — | Park |  | default_Park |
| HEN_S_024 | — | Park |  | default_Park |
| HEN_S_025 | — | Park |  | default_Park |
| HEN_S_026 | — | Park |  | default_Park |
| HEN_S_027 | — | Park |  | default_Park |
| HEN_S_028 | — | Park |  | default_Park |
| HEN_S_029 | — | Park |  | default_Park |
| HEN_S_030 | — | Park |  | default_Park |
| HEN_S_031 | — | Park |  | default_Park |

### Vocabulary Gate

Stage 4.5 PASSED — 0 violations.
