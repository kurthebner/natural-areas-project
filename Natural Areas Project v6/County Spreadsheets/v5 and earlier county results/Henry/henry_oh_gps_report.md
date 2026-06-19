# Henry County, OH — Stage 3 GPS Acquisition Report
**Run ID:** henry_oh_2026_04_20  
**Date:** 2026-04-26  

| ID | Name | GPS Lat | GPS Lon | Confidence | Method |
|---|---|---|---|---|---|
| HEN_S_004 | Dr. John Bloomfield Home & Carriage House Museum | 41.391340 | -84.127327 | HIGH | Nominatim address query: '229 W Clinton St, Napoleon, OH 435 |
| HEN_S_006 | Florida Wildlife Area | 41.321993 | -84.204391 | LOW | LOW: city centroid fallback — 'Florida, Henry County, Ohio' |
| HEN_S_009 | Hamler Community Park | 41.229216 | -84.034111 | LOW | LOW: city centroid fallback — 'Hamler, Henry County, Ohio' |
| HEN_S_011 | Henry County Fairgrounds | 41.381644 | -84.120723 | HIGH | Nominatim address query: '821 S Perry St, Napoleon, OH 43545 |
| HEN_S_012 | Henry County Historical Society Fairgrounds Historic Complex | 41.381644 | -84.120723 | HIGH | Nominatim address query: '821 S Perry St, Napoleon, OH 43545 |
| HEN_S_013 | Henry County Wildlife Area 1 | — | — | NONE | all_queries_failed |
| HEN_S_014 | Henry County Wildlife Area 2 | — | — | NONE | all_queries_failed |
| HEN_S_015 | Henry County Wildlife Area 3 | — | — | NONE | all_queries_failed |
| HEN_S_017 | Liberty Center Firemen's Park | 41.443385 | -84.008835 | LOW | LOW: city centroid fallback — 'Liberty Center, Henry County, |
| HEN_S_018 | Mary Jane Thurston State Park | 41.411925 | -83.884997 | MED | Nominatim query: 'Mary Jane Thurston State Park, Henry Count |
| HEN_S_019 | Maumee State Scenic River | — | — | NONE | linear_feature |
| HEN_S_023 | North Turkeyfoot Wildlife Area | — | — | NONE | all_queries_failed |

## Summary

| HIGH | MED | LOW | NONE |
|------|-----|-----|------|
| 3 | 1 | 3 | 5 |

## Notes

- **HEN_S_004** (Dr. John Bloomfield Home & Carriage House Museum): 229, West Clinton Street, Napoleon, Napoleon Township, Henry County, Ohio, 43545, United States
- **HEN_S_006** (Florida Wildlife Area): No exact park match; using Florida centroid. Florida, Flatrock Township, Henry County, Ohio, United States
- **HEN_S_009** (Hamler Community Park): No exact park match; using Hamler centroid. Hamler, Marion Township, Henry County, Ohio, United States
- **HEN_S_011** (Henry County Fairgrounds): 821, South Perry Street, Napoleon, Napoleon Township, Henry County, Ohio, 43545, United States
- **HEN_S_012** (Henry County Historical Society Fairgrounds Historic Complex): 821, South Perry Street, Napoleon, Napoleon Township, Henry County, Ohio, 43545, United States
- **HEN_S_013** (Henry County Wildlife Area 1): No Nominatim result within county bounds for any query format.
- **HEN_S_014** (Henry County Wildlife Area 2): No Nominatim result within county bounds for any query format.
- **HEN_S_015** (Henry County Wildlife Area 3): No Nominatim result within county bounds for any query format.
- **HEN_S_017** (Liberty Center Firemen's Park): No exact park match; using Liberty Center centroid. Liberty Center, Liberty Township, Henry County, Ohio, United States
- **HEN_S_018** (Mary Jane Thurston State Park): Mary Jane Thurston State Park, Grand Rapids, Damascus Township, Henry County, Ohio, United States
- **HEN_S_019** (Maumee State Scenic River): Linear feature spanning multiple counties; no single GPS point appropriate.
- **HEN_S_023** (North Turkeyfoot Wildlife Area): No Nominatim result within county bounds for any query format.

## GPS Merge Results (Stage 3 → Normalized)

| ID | Name | Action | Confidence | GPS Lat | GPS Lon | Plus Code | Township | Municipality |
|---|---|---|---|---|---|---|---|---|
| HEN_S_004 | Dr. John Bloomfield Home & Carriage House Museum | NORMALIZED | HIGH | 41.391340 | -84.127327 | 86HQ9VRF+G3 | Napoleon | Napoleon |
| HEN_S_006 | Florida Wildlife Area | NORMALIZED | LOW | 41.321993 | -84.204391 | 86HQ8QCW+Q6 | Flatrock | Flatrock |
| HEN_S_009 | Hamler Community Park | NORMALIZED | LOW | 41.229216 | -84.034111 | 86HQ6XH8+M9 | Marion | Marion |
| HEN_S_011 | Henry County Fairgrounds | NORMALIZED | HIGH | 41.381644 | -84.120723 | 86HQ9VJH+MP | Napoleon | Napoleon |
| HEN_S_012 | Henry County Historical Society Fairgrounds Historic Complex | NORMALIZED | HIGH | 41.381644 | -84.120723 | 86HQ9VJH+MP | Napoleon | Napoleon |
| HEN_S_013 | Henry County Wildlife Area 1 | REMAINS_HELD | NONE | — | — | — | — | — |
| HEN_S_014 | Henry County Wildlife Area 2 | REMAINS_HELD | NONE | — | — | — | — | — |
| HEN_S_015 | Henry County Wildlife Area 3 | REMAINS_HELD | NONE | — | — | — | — | — |
| HEN_S_017 | Liberty Center Firemen's Park | NORMALIZED | LOW | 41.443385 | -84.008835 | 86HQCXVR+9F | Liberty | Liberty |
| HEN_S_018 | Mary Jane Thurston State Park | NORMALIZED | MED | 41.411925 | -83.884997 | 86HRC468+Q2 | Damascus | Damascus |
| HEN_S_019 | Maumee State Scenic River | REMAINS_HELD | NONE | — | — | — | — | — |
| HEN_S_023 | North Turkeyfoot Wildlife Area | REMAINS_HELD | NONE | — | — | — | — | — |