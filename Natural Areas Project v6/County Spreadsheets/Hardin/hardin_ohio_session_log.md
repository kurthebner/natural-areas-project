# Hardin OH — Session Log (v6)
**RUN_ID:** `hardin_ohio_2026_06_01`
**PREFIX:** `OH-HAR`
**County:** Hardin, Ohio
**Run date:** 2026-06-01
**Status:** COMPLETE — UPSERTED 2026-06-02

---

## Discovery — Tier Yield

| Tier | Source Type | Query / Source | Entities Found |
|------|-------------|----------------|----------------|
| T1 | Federal & Tribal | NPS nps.gov/state/oh; VA NCA cem.va.gov; tribal registries | 0 — complete null; no federal/tribal land in Hardin County |
| T2 | State | ODNR DNAP + DOW; SORP CSV; ODOT baseline; water trails; ONAPA | 3 Sites, 1 TT, 3 APs — Lawrence Woods SNP; Lawrence Woods WA (CC/Wyandot); Andreoff WA (CC/Wyandot) |
| T3 | District | Ohio Auditor (unavailable); hardinvetspark.org; hardincountyohio.gov/swcd; Maumee WCD; Upper Scioto DCD | 3 Sites, 2 TTs, 2 APs — Veterans Memorial Park (T3 park district!); Silver Creek Center (SWCD) |
| T4 | County | hardincountyohio.gov; NRHP Hardin County Wikipedia; county financials | 0 — null; Zimmerman Kame = private land; Saulisberry/France Lake → T6 |
| T5 | Township | OTA roster (15 twps); township websites; rootsweb.com cemetery list | 23 Sites — 22 township cemeteries; 1 unconfirmed Roundhead park |
| T6 | Municipal | cityofkenton.com + recdesk; adaoh.gov; villageofforest.com; villageofdunkirk.com; mountvictory.com; limaohio.com | 15 Sites, 1 TT, 1 SN-PROV, 3 APs — 9 municipalities searched; Ray Brown Memorial Park (Alger, opened May 2026) |
| T7 | Conservancy & Land Trust | WCOLC; TNC; BSC; NCOLC; ONAPA preserve map | 0 — null; WCOLC = agricultural easements only; all other LTs outside service area |
| T8 | Private | GolfWeather.com; onu.edu; rootsweb cemetery list | 67 Sites, 1 TT — Memorial Park Golf Club (18-hole); ONU Green Monster Trail; 5 church cems; 59 family/private cems |

**Total raw records: 144 (on disk — IMP-080 verified)**
**Entity records: 111 Sites, 5 Trailthings, 1 Site Network (PROVISIONAL), 8 APs**
**Cross-county holds: 2 (Lawrence Woods WA + Andreoff WA — Wyandot not yet run, Scenario A)**
**Unconfirmed baseline seeds: 8 (see handoff)**

---

## Document Collection

Documents downloaded during discovery. Full log in `hardin_document_log.yaml`.

| Filename | Tier | Type | Description |
|----------|------|------|-------------|

---

## Normalization Decisions

---

## GPS Acquisition

**Nominatim (bounded):** 5 acquired (McKendree, Dunkirk, Hale, Ridgeway, Grove cemeteries)
**OSM Overpass (bounding box):** 37 acquired (exact + variant name matches from 209 county cemetery elements)
**Google Maps / Chrome browser:** 3 acquired (Fairview-McDonald, Huntersville, Fulton confirmed)
**Human-assist (parcel viewer + Street View + pin drops):** 7 acquired (Grassy Point, Hickory Grove, Behler/Speeler, Bunn, Hepburn/Lee, Pfeiffer/Morrison, Dille, Wolf Creek, Pleasant Hill, Woodlawn, Fairview-McDonald Plus Code, Smith, Fulton — cumulative across session)
**GPS unresolvable:** 34 cemeteries — pending GNIS `OH_Features.zip` when USGS server restored
**New discovery during GPS pass:** Westminster Salem Cemetery (40.6788, -83.9614) — confirmed named cemetery, not in dataset

---

## Errors and Fixes

---

## Pipeline Stage Log

| Stage | Result | Notes |
|-------|--------|-------|
| Stage 0 — Module check | PASS | All v6.0 modules present |
| Stage 2 — Baseline load | COMPLETE | 28 unconfirmed seeds held; confirmed seeds already in YAML |
| Stage 3 — Resolution | 125 entity records → 108 Sites, 5 TTs, 1 SN, 6 APs normalized | 3 Sites held CC/uncertain; 2 APs held parent_held |
| Stage 4a — GPS Fill-Forward | 14 entities: GPS from source | No prior DB records for Hardin |
| Stage 4b — GPS Acquisition | 11 Sites + 1 AP acquired | Nominatim + manual fallback; Wharton/Pioneer/Murray/Gormley/etc. |
| Stage 4c — GPS Gate | 88 Sites gps_unresolvable (cemeteries) | All pass gate |
| Stage 5 — Normalization | normalize_hardin.py | Site categories, TT vocab, SN type, AP types all mapped |
| Stage 6 — TSV Output | 4 files written | 108 Sites, 5 TTs, 1 SN, 6 APs |
| Stage 6.5 — Vocab Gate | PASS | No violations; cemetery features_raw unmapped (non-blocking) |
| Stage 7 — Integrity Check | PASS | All delimiter counts correct (30/30/17/19 tabs) |
| Stage 7.5 — Human Review | **COMPLETE** 2026-06-02 | Review spread across 2 sessions; see handoff for full change list |
| Stage 8 — Upsert | **COMPLETE** 2026-06-02 | 108S / 5TT / 1SN / 6AP committed; 33 held; DB schema migrations applied (site_networks + access_points columns) |

---

## Entity ID Assignments

| Entity ID | Name | Type |
|-----------|------|------|

---

## Held Entities

| Entity ID | Name | Hold Reason | Resolution Path |
|-----------|------|-------------|-----------------|

---

## Open Flags

None.

---

## Status

**DISCOVERY COMPLETE — PIPELINE READY**
All 8 tiers complete. 144 records on disk. 111 Sites, 5 Trailthings, 1 Site Network (PROV), 8 APs. 2 cross-county holds. 8 unconfirmed baseline seeds. Ready for Stage 0 pipeline.
