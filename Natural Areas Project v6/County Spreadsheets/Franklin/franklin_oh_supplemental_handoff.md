# Franklin County — Supplemental Discovery Handoff
**Run type**: Supplemental T6/T7/T8 pass
**Date started**: 2026-06-11
**Date completed**: 2026-06-11
**Base pipeline**: 2026-03-25 (1,175 sites in DB as of 2026-06-11)
**Staging file**: `franklin_oh_supplemental_discovery_2026_06_11.yaml`

---

## Status: SUPPLEMENTAL DISCOVERY COMPLETE — ALL HELD ENTITIES RESOLVED

All supplemental tiers worked. 42 new sites added to DB (OH-FR-S-1194 through OH-FR-S-1242).
0 sites in held_entities. All 5 GPS-missing entities resolved 2026-06-11 (see below).

---

## Scope

| Tier | Target | Status |
|---|---|---|
| T6 | Grove City — all parks not yet in DB | COMPLETE |
| T6 | Gahanna — pocket parks (CivicPlus /474/) | COMPLETE |
| T6 | New Albany — district recreation areas | COMPLETE |
| T6 | Westerville — parks.westerville.org | COMPLETE |
| T6 | Upper Arlington — upperarlingtonoh.gov | COMPLETE |
| T6 | Address partials — Obetz/Valleyview/Urbancrest/Lockbourne/Riverlea/Marble Cliff/Whitehall/Grandview Heights | COMPLETE |
| T7 | Central Ohio Land Trust (COLT) | COMPLETE — NULL (no such conservation land trust in Franklin County) |
| T7 | Columbus Audubon | COMPLETE — already in DB as OH-FR-S-1021 (Grange Insurance Audubon Center) |
| T7 | The Nature Conservancy — Darby Creek | COMPLETE — already in DB as OH-FR-S-1183 (Darby Creek Conservation Area) |
| T7 | Franklin SWCD conservation easements | COMPLETE — 2 new sites added (OH-FR-S-1241, OH-FR-S-1242; gps_unresolvable) |
| T8 | GNIS cemetery enumeration | COMPLETE — 28 new cemeteries added (OH-FR-S-1213 through OH-FR-S-1240) |
| T8 | Private golf courses | COMPLETE — 27 already in DB from original pipeline |
| T8 | Private nature reserves | COMPLETE — no additional reserves; PAD-US checked |

---

## DB Baseline Counts (pre-supplemental)
Total Franklin sites: 1,175
Franklin held entities: 1 (OH-FR-S-0608, gps_missing)

## DB Final Counts (post-supplemental)
Total Franklin sites: 1,217
Franklin held entities: 5 → **0 (all resolved 2026-06-11)**

### Held Entity Resolution — 2026-06-11
GPS acquired via GNIS / PAD-US / Google Maps; all 5 removed from held_entities.

| Site ID | Name | GPS Resolved |
|---|---|---|
| OH-FR-S-0608 | Friendship Park Community Garden | 40.01494, -82.87616 |
| OH-FR-S-1209 | Marsh Cemetery | 39.89851, -83.06002 |
| OH-FR-S-1210 | Hoover Cemetery | 39.88794, -83.05719 |
| OH-FR-S-1211 | Goodale Green Space | 39.97666, -83.05158 |
| OH-FR-S-1212 | Mariner's Cove and Wetland | 40.14164, -82.89008 |

Note: OH-FR-S-1241 and OH-FR-S-1242 (SWCD riparian easements) have gps_unresolvable=true
in notes; they are NOT in held_entities — gps_unresolvable exempts them from GPS gate.

---

## New Sites Added This Pass (OH-FR-S-1194 through OH-FR-S-1242)

### T6 Municipal (1194–1212, 19 sites)
| ID | Name | Municipality | GPS |
|---|---|---|---|
| OH-FR-S-1194 | Burr Avenue Park | Grandview Heights | 39.9767,-83.0272 |
| OH-FR-S-1195 | First Avenue Park | Grandview Heights | 39.9816,-83.0404 |
| OH-FR-S-1196 | Virginia Ave Park | Grandview Heights | 39.9836,-83.0331 |
| OH-FR-S-1197 | Yard Street Green Space | Grandview Heights | 39.9818,-83.0273 |
| OH-FR-S-1198 | Grandview Center | Grandview Heights | 39.9769,-83.0458 |
| OH-FR-S-1199 | Burbank Park | Upper Arlington | 40.0530,-83.0841 |
| OH-FR-S-1200 | Sunny 95 Park | Upper Arlington | 40.0466,-83.0617 |
| OH-FR-S-1201 | First Responders Park | Westerville | 40.1253,-82.9438 |
| OH-FR-S-1202 | Hoff Woods Park | Westerville | 40.1382,-82.9214 |
| OH-FR-S-1203 | Millstone Creek Park | Westerville | 40.1433,-82.9018 |
| OH-FR-S-1204 | Olde Town Park | Westerville | 40.1333,-82.9280 |
| OH-FR-S-1205 | Johnston-McVay Park | Westerville | 40.1128,-82.8971 |
| OH-FR-S-1206 | Hanby Park | Westerville | 40.1232,-82.9270 |
| OH-FR-S-1207 | Otterbein Lake | Westerville | 40.1228,-82.9407 |
| OH-FR-S-1208 | Sycamore Trail Park | Westerville | 40.1465,-82.9396 |
| OH-FR-S-1209 | Marsh Cemetery | Grove City | HELD |
| OH-FR-S-1210 | Hoover Cemetery | Grove City | HELD |
| OH-FR-S-1211 | Goodale Green Space | Grandview Heights | HELD |
| OH-FR-S-1212 | Mariner's Cove and Wetland | Westerville | HELD |

### T7 Conservancy (1241–1242, 2 sites)
| ID | Name | Governance | Acres |
|---|---|---|---|
| OH-FR-S-1241 | Hellbranch Run Riparian Corridor Protection | Franklin SWCD | 17 |
| OH-FR-S-1242 | Johnson Road Riparian Protection Area | Franklin SWCD | 84 |

### T8 Private — GNIS Cemeteries (1213–1240, 28 sites)
All have GPS from GNIS. See staging YAML for complete list.

---

## DB Fixes Applied This Pass

| Site ID | Issue | Fix |
|---|---|---|
| OH-FR-S-0974 | Wrong name ("Grandview Heights Skate Park") and wrong municipality | Renamed to "Grove City Skate Park"; municipality → Grove City |
| OH-FR-S-0784 | Wrong municipality (blank/wrong) | municipality → Westerville |
| OH-FR-S-0858 | Wrong municipality | municipality → Grove City |
| OH-FR-S-0856 | Wrong municipality | municipality → Grove City |
| OH-FR-S-1012 | Wrong GPS (placed in UA area) and wrong municipality | GPS → 39.9656076,-83.076766; municipality → Valleyview |

---

## MRQ Items Added This Pass

| Review ID | Entity | Issue |
|---|---|---|
| ~180 | OH-FR-S-1020 Alice Smith Nature Preserve | WRONG COUNTY: governance=Village of Lithopolis; GPS in Fairfield County area — **RESOLVED 2026-06-12: deleted from Franklin DB; staged as FAI-ALICE-SMITH-NP MRQ for Fairfield County run** |
| ~181 | OH-FR-S-0169 Frank Fetch Memorial Park | GPS/MUNICIPALITY MISMATCH: municipality=Grandview Heights but GPS in SE Columbus area — **RESOLVED 2026-06-12: municipality corrected to Columbus; GPS 39.9508,-82.9922 confirmed correct (German Village)** |
| 184 | OH-FR-AP-0067 Three Creeks Park Alum Creek Trailhead | AP_CONSOLIDATION: AP-0067, AP-0074, AP-0079 are the same physical multi-trail hub. All share identical GPS (=site centroid), identical features, identical notes. Consolidate to single AP parented to OH-FR-S-0388 + OH-FR-TT-0001 + OH-FR-TT-0002. Delete AP-0074/0079 after parent links migrated. Resolve individual GPS for consolidated AP. |
| 185 | OH-FR-AP-0074 Three Creeks Park Big Walnut Trailhead | AP_CONSOLIDATION: Duplicate of OH-FR-AP-0067. Delete after consolidation. See MRQ 184. |
| 186 | OH-FR-AP-0079 Three Creeks Park Blacklick Trailhead | AP_CONSOLIDATION: Duplicate of OH-FR-AP-0067. Delete after consolidation. See MRQ 184. |
| 203 | OH-FR-AP-0064 Hayden Park Trailhead | AP_CONSOLIDATION: AP-0064 and AP-0076 share identical GPS, features, and notes. AP-0076 identity_notes says "also serves Alum Creek Trail" — same single-hub pattern as Three Creeks. Consolidate: keep AP-0064, add Big Walnut Trail parent, delete AP-0076. Verify GPS. |
| 204 | OH-FR-AP-0076 Hayden Park Big Walnut Trailhead | AP_CONSOLIDATION: Duplicate of OH-FR-AP-0064. Delete after parent link migrated. See MRQ 203. |
| 205 | OH-FR-AP-0087 Battelle Darby Creek Camp Chase Trailhead | AP_CONSOLIDATION: AP-0087 and AP-0089 share identical GPS, features, notes. AP-0089 is "accessed from Camp Chase Trail" — shared parking area. Consolidate: keep AP-0087, add Darby Creek Trail parent, delete AP-0089. Verify GPS. |
| 206 | OH-FR-AP-0089 Battelle Darby Creek Darby Trail Trailhead | AP_CONSOLIDATION: Duplicate of OH-FR-AP-0087. Delete after parent link migrated. See MRQ 205. |

---

## Open Items / Deferred

| Item | Deferred to |
|---|---|
| MRQ 178: O'Shaughnessy Reservoir | Delaware County pipeline run |
| MRQ 179: Tartan West Open Space | Union County pipeline run |
| MRQ ~180: Alice Smith Nature Preserve wrong county | ~~Fairfield County pipeline run~~ RESOLVED 2026-06-12 |
| MRQ ~181: Frank Fetch Memorial Park GPS mismatch | ~~Manual verification~~ RESOLVED 2026-06-12 |
| GPS for OH-FR-S-1209, 1210, 1211, 1212 | ~~GPS re-acquisition pass~~ RESOLVED 2026-06-11 |
| WRP parcels in Franklin County | Future GDB-layer analysis (5 parcels, ~655ac total, NRCS) |
| MRQ 184–186: Three Creeks Park AP consolidation | Execute AP consolidation: merge 0067/0074/0079 → single AP with 3 Trailthing parents; resolve GPS |

---

## Municipality DB vs MORPC Counts (post-supplemental)
| Municipality | DB pre | DB post | MORPC Public | Status |
|---|---|---|---|---|
| Grove City | 46 | ~50 | 38 | DB > MORPC (expected; DB includes cemeteries, rec facilities) |
| Gahanna | 69 | ~70 | 47 | DB > MORPC |
| New Albany | 28 | ~28 | 15 | DB > MORPC |
| Westerville | 36 | ~45 | 40 | Closed gap |
| Upper Arlington | 30 | ~33 | 21 | DB > MORPC |
| Grandview Heights | 13 | ~18 | 7 | Closed gap |

---

## Session Log
- 2026-06-11: Supplemental pass initiated. Working files created.
- 2026-06-11: T6 complete — Grove City, Gahanna, New Albany, Westerville, Upper Arlington,
  address partials. 19 new T6 sites (1194–1212), 5 DB fixes, 2 new MRQ items.
- 2026-06-11: T7 complete — COLT null, Columbus Audubon already in DB,
  TNC Darby Creek already in DB, 2 SWCD riparian easements added (1241–1242).
- 2026-06-11: T8 complete — 28 GNIS cemeteries added (1213–1240), golf courses
  confirmed 27 in DB, no additional private reserves.
- 2026-06-11: Supplemental discovery complete. 42 new sites total. DB at 1,217 sites.
- 2026-06-12: IMP-019 AP dedup audit flagged OH-FR-AP-0067/0074/0079 as same physical location (Three Creeks Park multi-trail hub). Routed to MRQ 184–186 for consolidation.
