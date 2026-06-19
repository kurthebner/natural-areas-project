# SENECA OH — Session Log
**RUN_ID:** `seneca_oh_2026_05_25`
**PREFIX:** `SEN`
**County:** Seneca, Ohio
**Run date:** 2026-05-25
**Status:** DISCOVERY COMPLETE — ready for pipeline

---

## Discovery — Tier Yield

| Tier | Source Type | Query / Source | Entities Found |
|------|-------------|----------------|----------------|
| T1 | Federal / Tribal | USFS, NPS, USFWS, USACE, BLM, DoD, VNCA | 0 (8 null blocks) |
| T2 | State | ODNR DNAP, ODNR DOW, OHC, Scenic Rivers | 10 (9 Sites + Sandusky Scenic River Trail; 8 null blocks) |
| T3 | District | Ohio Auditor + SCPD website | 15 (13 Sites + 2 Trails; incl. 3 late Clary-Boulee; 6 null blocks) |
| T4 | County | Seneca County parks/rec, NRHP | 0 (5 null blocks) |
| T5 | Township | OTA 15 townships + OGE GNIS cemeteries | 16 (all Sites: 1 park + 11 township cems + 4 late cems; 24 null blocks) |
| T6 | Municipal | Cities/villages — Tiffin, Fostoria, Attica, Bloomville, NR, Bellevue, Bettsville, GS, Republic | 27 (26 Sites + Rock Creek Trail; 10 null blocks) |
| T7 | Conservancy / Land Trust | BSC, TNC, NORTA, WCOLC, WRLC, Cardinal, NCOLC, ONAPA, FELC, LTA | 0 (11 null blocks; Clary-Boulee re-tiered T3) |
| T8 | Private | PGA+DSC golf, OGE GNIS cemeteries (73), direct searches | 78 (all Sites: 5 golf + 4 nature/camp + 3 named cems + 66 OGE cems; 11 null blocks) |

**Total raw records (discovery complete):** 146
- T2: 10 | T3: 15 | T5: 16 | T6: 27 | T8: 78
**Entity types:** 141 Sites + 3 Trails + 0 APs + 0 Trail Segments + 0 Trail Networks + 0 Site Networks
**Null blocks:** 83 total
**Cross-county candidates:** 1 (Sandusky State Scenic River — T2)
**Post-resolution:** to be determined during pipeline

---

## Normalization Decisions

*(to be filled during pipeline)*

---

## GPS Acquisition

*(to be filled during pipeline)*

---

## Errors and Fixes

| Error | Fix |
|-------|-----|
| BSC URL changed (blackswampconservancy.org → blackswamp.org) | Used correct URL; all BSC content confirmed |
| DSC golf page 404 (sports-outdoors/golf/ and sports-recreation/golf/) | Used Google cache / search results for golf enumeration |
| Seneca Caverns URL confusion (senecacaverns.com → WV cave) | Used correct URL senecacavernsohio.com |
| GolfPass Seneca Hills returned Coyote Run GC (Perry Co.) | Used search results directly for Seneca Hills |
| Fostoria Country Club county conflict (GolfPass said Seneca; chamber said Hancock) | Confirmed Hancock Co. via Findlay-Hancock Chamber; staged null block |
| Cross Oak Camp wrong county (WebFetch said Seneca County; address = Auglaize Co.) | Confirmed Auglaize Co. (St. Marys 45885); staged null block |
| FELC visit page 404 (felctiffin.org/visit/) | Used homepage instead; sufficient detail obtained |
| campfirenwohio.com redirect → spam site | Used ACA and campfiresc.org for Camp Glen instead |

---

## Pipeline Stage Log

| Stage | Result | Notes |
|-------|--------|-------|
| Stage 1 — Resolution | COMPLETE 2026-05-28 | 142 sites, 4 trails normalized; 1 vocab fix (FELC subtype Stewardship Area → Habitat Management Area) |
| Stage 2 — Normalization | COMPLETE 2026-05-28 | normalize_seneca.py; 2 bugs fixed (OGE cem ownership/gov parsing, Liberty Cemetery subtype guard) |
| Stage 2b — GPS Acquisition | COMPLETE 2026-05-28 | 131/142 sites (92.3%); 11 held gps_missing; 2-pass Nominatim + manual web sources |
| Stage 2c — GPS Gate | COMPLETE 2026-05-28 | 11 sites held gps_missing; 1 trail held cross_county_held (Sandusky SSR) |
| Stage 3 — GPS in pipeline | COMPLETE 2026-05-28 | 131/131 active sites confirmed GPS; pass-through (already acquired) |
| Stage 4 — TSV Output | COMPLETE 2026-05-28 | 131 sites, 3 trails; seneca_oh_2026_05_28_*.tsv |
| Stage 4.5 — Vocab Gate | PASSED 2026-05-28 | All checks passed after FELC subtype fix |
| Stage 5 — Integrity Check | PASSED 2026-05-28 | No issues |
| Stage 5.5 — Human Review | CONFIRMED 2026-05-28 | 2 near-boundary GPS sites noted (Fostoria) for post-upsert parcel verification |
| Stage 6 — DB Upsert | COMPLETE 2026-05-28 | 131 sites, 3 trails, 12 held_entities committed to natural_areas_v5.db |
| GPS Re-run — WPAs (S-006–009) | COMPLETE 2026-05-28 | ODNR GIS polygon centroids via REST API; 4 WPAs released; 135 active, 8 held |
| GPS Re-run — Cemeteries (S-024, S-025) | COMPLETE 2026-05-28 | County Auditor parcel centroids; Disinger (41.2267, -83.3862) + Rock Run (41.0780, -83.1322); 137 active, 6 held |
| S-029–033 Attribution Error | FLAGGED 2026-05-28 | 5 Pleasant Township cemeteries confirmed as Franklin County (not Seneca); reclassified identity_uncertain in held_entities |
| Dedup Resolution | COMPLETE 2026-05-28 | S-098 (Zion Lutheran Cem) removed — duplicate of S-023 (Zion Cemetery, T5); S-100 (Attica Cemetery) removed — duplicate of S-026 (Attica-Venice Joint Cemetery, T5); identical GPS (0.0m) confirmed duplicates. S-104 renamed M.E. Church Cemetery (parcel PIN C13005146360000 confirms M E CHURCH CEMETERY ownership; Bloomville Cemetery is GNIS alt name; village does not manage; stays T8). S-109 (County Home Cemetery) re-tiered T4: parcel PIN E19000298260200 BOARD OF COMMISSIONERS OF SENECA COUNTY OHIO, 1.113 ac Eden Twp Section 5; GPS updated to parcel centroid (41.0754, -83.1537). Active Seneca sites: 137→135 |

---

## Entity ID Assignments

*(to be filled during pipeline)*

---

## Open Flags

| Flag | Entity | Notes |
|------|--------|-------|
| Governance uncertain | H.P. Eells Park (T3) | Bettsville Recreation Board last audited 2009 — possibly dissolved; may re-tier T6 (Village of Bettsville) |
| Unresolved baseline | Attica Upground Reservoirs (×2) | Village water supply; no confirmed public recreation; pending human verification |
| Unresolved baseline | Lake Lepomis WA | Not found in OAC or ODNR — unconfirmed_baseline_seed |
| Unresolved baseline | Wildlife Production Area 64 | Not found in OAC or ODNR — unconfirmed_baseline_seed |
| Deduplication | Attica Cemetery (T8) | May = T5 Attica-Venice Joint Cemetery; verify before pipeline |
| Deduplication | Zion Lutheran Cemetery (T8) | May = T5 Zion Cemetery (Jackson Twp); verify before pipeline |
| Governance check | County Home Cemetery (T8) | Possible T4 (county-owned poorhouse cemetery); verify with parcel data |
| Governance check | Bloomville Cemetery (T8) | Possible T6 (Village of Bloomville); verify before pipeline |
| Status conflicting | Seneca Hills Golf Course (T8) | Golf Digest = Closed; GolfNow = Active; needs field verification |
| Pleasant Twp overlap | Pleasant Ridge/Union/View (T8) | Names don't match T5-staged Twp cemeteries; treating as separate T8 entities |

---

## Status

**DISCOVERY COMPLETE** — All 8 tiers finished 2026-05-26. IMP-080 verified. Ready for pipeline.
146 raw records | 83 tier_nulls | 1 cross-county candidate (Sandusky State Scenic River)
