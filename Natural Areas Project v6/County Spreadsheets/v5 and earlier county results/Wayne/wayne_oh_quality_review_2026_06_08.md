# Wayne County — Quality Review
**Date:** 2026-06-08  
**Reviewer:** Claude (automated + manual)  
**Pipeline run:** wayne_oh_2026_03_08 (v5.2 schema)  
**DB state at review:** post-remediation run 2026-06-08  

---

## Entity Counts (live DB)

| Entity type | Count | Run metadata |
|---|---|---|
| Sites | 44 | — |
| Trails | 12 (incl. 1 MC) | — |
| Trail segments | 0 | — |
| Trail networks | 1 | — |
| Trailthings | 0 | v5 run — expected |
| Site networks | 0 | — |
| Access points (live) | 13 | was 17; 4 moved to held today |
| Held entities | 9 | 4 new parent_held + 5 pre-existing |

Run metadata: records_input=79, normalized=73, held=6 (original). Post-2026-06-08 remediation:
held=9 (4 Wayne APs moved from access_points to held_entities per IMP-025 fix).

---

## GPS Audit

**Sites:** All 44 live sites have GPS. No out-of-Ohio-bbox values.

**Shared coordinates — two pairs:**

1. `OH-WA-S-0004` (Barnes Preserve) and `OH-WA-S-0005` (Koehler's Pond) share GPS
   (40.781233, -81.89694). WA-S-0005 is a child site within Barnes Preserve; it
   inherits the preserve entrance coordinate. **Acceptable** — child site without
   distinct entrance. Flag for individual GPS at field verification.

2. `OH-WA-AP-0001` (Shreve Lake Boat Launch) and `OH-WA-AP-0002` (Shreve Lake Fishing Pier)
   share GPS (40.68314, -82.04612). Both are at Shreve Lake Wildlife Area. Two distinct
   physical access points are expected to have different coordinates.
   **Action:** Acquire individual GPS for these two APs.

**Access points:** All 13 live APs have GPS. ✓

**Missing data:** `OH-WA-S-0001` (Brown's Lake Bog) has `acres = NULL`. 
PAD-US shows two parcels (83 ac + 19 ac = 102 ac total). Populate acres from PAD-US.

---

## Held Entities — Cross-County Status

| ID | Name | Reason | Partner county | Status |
|---|---|---|---|---|
| OH-WA-S-0045 | Killbuck Marsh Wildlife Area | cross_county_held | Holmes | Holmes not run — **REMAIN HELD** |
| OH-WA-S-0046 | Funk Bottoms Wildlife Area | cross_county_held | Ashland | Ashland not run — **REMAIN HELD** |
| OH-WA-T-0013 | Chippewa Township Nature Preserve trails | identity_uncertain | n/a | Awaiting field verification — **REMAIN HELD** |
| OH-WA-T-0014 | Sippo Valley Trail | cross_county_held | Stark | Stark not run — **REMAIN HELD** |
| OH-WA-T-0015 | Holmes County Trail | cross_county_held | Holmes | Holmes not run — **REMAIN HELD** |
| OH-WA-AP-0003 | Killbuck Marsh — Carrie Lane Parking Area | parent_held | (parent WA-S-0045) | New — **REMAIN HELD** |
| OH-WA-AP-0004 | Killbuck Marsh — Wright Marsh Parking Area | parent_held | (parent WA-S-0045) | New — **REMAIN HELD** |
| OH-WA-AP-0013 | Sippo Valley Trail — Dalton Trailhead | parent_held | (parent WA-T-0014) | New — **REMAIN HELD** |
| OH-WA-AP-0015 | Holmes County Trail — Fredericksburg Trailhead | parent_held | (parent WA-T-0015) | New — **REMAIN HELD** |

All 9 held entities are correctly held. No releases warranted until Holmes, Stark, or Ashland
County pipelines run.

---

## PAD-US Completeness Gate

PAD-US records filtered to Wayne County operators and known Wayne entity names:

| PAD-US name | GAP | Result | Action |
|---|---|---|---|
| Wooster Memorial Park | 4 | **MATCHED** OH-WA-S-0007 | None |
| Johnson Woods Dedicated Nature Preserve | 2 | **MATCHED** OH-WA-S-0002 (name variant — PAD-US adds "Dedicated") | None |
| Shreve Lake Wildlife Area | 2 | **MATCHED** OH-WA-S-0003 | None |
| Funk Bottoms Wildlife Area | 2 | In held (cross_county_held) | None — expected |
| Killbuck Marsh Wildlife Area | 2 | In held (cross_county_held) | None — expected |
| Brown's Lake Bog Fee | 1 | **MATCHED** OH-WA-S-0001 (name variant) | See note below |
| Doylestown Memorial Park | 4 | **MATCHED** OH-WA-S-0035 ("Memorial Park", Village of Doylestown — name variant) | None |
| Shreve Community Park | 4 | **MATCHED** OH-WA-S-0034 (Shreve Village Park — name variant) | None |
| Wayne County Fairgrounds | 4 | **OUT OF SCOPE** — County fairgrounds, no natural area mandate | Close |
| Wooster Country Club | 4 | **OUT OF SCOPE** — Private, no public access | Close |

**NOTE:** The above table reflects the initial limited analysis. The full GDB spatial query results
are documented below — the initial PASS finding was revised.

---

### Full Spatial Analysis (GDB query — na_padus_query.py)

102 PAD-US fee records intersected the Wayne bbox (40.58–40.98°N, −82.33–−81.58°W). Analysis
run against all Wayne live sites plus held entities.

**Confirmed Matched (27 records):**

| PAD-US name | GAP | Acres | NAP record |
|---|---|---|---|
| Brown's Lake Bog Fee (×2 parcels) | 1 | 83+19 | OH-WA-S-0001 |
| Shreve Lake Wildlife Area | 2 | 228 | OH-WA-S-0003 |
| Funk Bottoms Wildlife Area (×2) | 2 | 1038+504 | OH-WA-S-0046 (held) |
| Killbuck Marsh Wildlife Area (×2) | 2 | 4547+1258 | OH-WA-S-0045 (held) |
| Nature Preserve (Massillon mgr) | 2 | 74 | OH-WA-S-0006 (Chippewa Twp Nature Preserve) |
| Central Park (Rittman city of) | 4 | 6 | OH-WA-S-0027 |
| Christmas Run Park | 4 | 35 | OH-WA-S-0010 |
| Diller Park | 4 | 1 | OH-WA-S-0013 |
| Doc Gilcrest Park | 4 | 0 | OH-WA-S-0037 (Gilcrest Park) |
| Doylestown Memorial Park | 4 | 12 | OH-WA-S-0035 |
| E.J. Young Grand View Park | 4 | 2 | OH-WA-S-0028 |
| Freelander Park | 4 | 31 | OH-WA-S-0009 (Freedlander Park — spelling variant) |
| Gailey Park | 4 | 4 | OH-WA-S-0017 |
| Gerstenslager Park | 4 | 28 | OH-WA-S-0014 |
| Grosjean Park | 4 | 65 | OH-WA-S-0011 |
| Harold Miller Memorial Park | 4 | 6 | OH-WA-S-0035 |
| Hilltop Park | 4 | 7 | OH-WA-S-0008 (Oak Hill Park — alt name) |
| Martin Fritz Memorial Park | 4 | 32 | OH-WA-S-0025 |
| Miller Park / Stan Miller Park | 4 | 10+2 | OH-WA-S-0015 |
| Oakhill Park | 4 | 96 | OH-WA-S-0008 (Oak Hill Park — no-space variant; score 72 confirmed) |
| Ohio Veteran's Memorial Park | 4 | 10 | OH-WA-S-0035 |
| Orr Park | 4 | 78 | OH-WA-S-0016 |
| Park (unnamed 765ac) | 4 | 765 | OH-WA-S-0007 (Wooster Memorial Park) |
| Shreve Community Park | 4 | 5 | OH-WA-S-0034 (Shreve Village Park) |
| Village Green Park | 4 | 8 | OH-WA-S-0041 |
| Wooster Memorial Park | 4 | 81 | OH-WA-S-0007 |

**Out of Scope — wrong county (manager or centroid outside Wayne):**

Emmons Field (City of Ashland), Bimeler/Witting/Unknown Parks (Village of Brewster, Stark Co),
Franklin-Clinton Area/Ohio & Erie Canal (Metroparks Serving Summit), Muhlauser Park/Old School
Playground (City of Canal Fulton, Stark Co), The Corner Park (County of Ashland), Canal Corridor
(Cleveland Metroparks, centroid east of bbox), Clays Park (likely Stark Co private resort).

**Confirmed Discovery Misses — in Wayne bbox, eligible, not in DB:**

| PAD-US name | GAP | Acres | Centroid | Tier | Resolution |
|---|---|---|---|---|---|
| Wilderness Center | 2 | 506 | (40.675, −81.640) | T7 | **RESOLVED** — Stark County primary (southwest Stark Co, per Land Trust Alliance); Wayne bbox false positive |
| Beach City Wildlife Area | 2 | 393 | (40.607, −81.614) | T2 | **RESOLVED** — Tuscarawas County (ODNR authoritative); Wayne bbox false positive |
| Mohler Wildlife Area (47ac) | 2 | 47 | (40.644, −82.183) | T2 | **RESOLVED** — Holmes County (ODNR authoritative: "half-mile south of SR-3, 2 miles east of Loudonville"); Wayne bbox false positive |
| Mohican-Memorial State Forest | 2 | 4649 | (40.598, −82.298) | T2 | Ashland/Richland/Knox primary; centroid clips Wayne bbox edge — not a Wayne entity |
| Kinney Trail Park | 4 | 49 | (40.831, −81.942) | T6 | **STAGED** — genuine Wayne miss; City of Wooster trail corridor; added to staging YAML |
| Schellin Park | 4 | 13 | (40.794, −81.934) | T6 | **STAGED** — genuine Wayne miss; City of Wooster; GPS confirmed; added to staging YAML |
| Cohan Park (City of Wooster) | 4 | 6 | (40.827, −81.944) | T6 | **STAGED** — genuine Wayne miss; City of Wooster; GPS confirmed; added to staging YAML |

**Revised PAD-US completeness result: PARTIAL FAIL — 3 T6 city parks confirmed missing and staged.**
The initial concern about GAP2 entities (Wilderness Center, Beach City WA, Mohler WA) resolved to
bbox false positives after ODNR and Land Trust Alliance source verification. No GAP1/GAP2 Wayne
entities are missing. Three T6 City of Wooster parks (Schellin, Kinney Trail, Cohan) were confirmed
absent from the original discovery and staged as supplemental records (2026-06-08).

**Supplemental records staged:** 3 Sites added to `wayne_oh_raw_discovery_15.yaml` on 2026-06-08.
These require pipeline processing (GPS acquisition for Kinney Trail Park, normalization, upsert)
before they appear in the live DB.

**Brown's Lake Bog note:** PAD-US lists two "Brown's Lake Bog Fee" parcels (83 ac + 19 ac = 102 ac,
GAP Status 1) under NGO ownership. Our DB records governance as Ohio DNAP. This is a known pattern
for DNAP preserves where TNC holds fee ownership and DNAP manages under a conservation agreement.
The preserve identity is correct. Acres field updated to 102 this session.

---

## Relationship Table Audit

**trail_network_members:** WA-TN-0001 (Rails to Trails of Wayne County Trail System) correctly
links WA-T-0009 (County Line Trail) and WA-T-0010 (Heartland Trail). ✓

**trail_parents (GAP):** Zero trail-to-site parent relationships recorded for any Wayne County
trail. Several trails clearly reside within parent sites:

| Trail | Expected parent site |
|---|---|
| OH-WA-T-0001 (Brown's Lake Bog Trail) | OH-WA-S-0001 (Brown's Lake Bog SNP) |
| OH-WA-T-0002 (Johnson Woods Boardwalk Trail) | OH-WA-S-0002 (Johnson Woods SNP) |
| OH-WA-T-0003 (Casey's Trails) | OH-WA-S-0004 (Barnes Preserve) |
| OH-WA-T-0004 (WMP Trail System) | OH-WA-S-0007 (Wooster Memorial Park) |
| OH-WA-T-0011 (Vulture's Knob Trail System) | OH-WA-S-0044 (Vulture's Knob) |

This gap is a v5 upsert artifact — the Wayne pipeline did not populate trail_parents.
Logged as a data quality item (see below). These relationships are not required for DB
integrity but should be backfilled during the next Wayne County pipeline pass or when
trail_parents is migrated to the Trailthing model.

**site_parent:** WA-S-0005 (Koehler's Pond) → WA-S-0004 (Barnes Preserve). ✓

**access_point_parents:** All 13 live APs have parent references. All parent entities
confirmed present in live tables. ✓

---

## Data Quality Findings

| # | Severity | Finding | Action |
|---|---|---|---|
| 1 | ~~HIGH~~ RESOLVED | PAD-US — Wilderness Center (Stark County primary, bbox false positive) | Closed — not Wayne entity |
| 2 | ~~HIGH~~ RESOLVED | PAD-US — Beach City Wildlife Area (Tuscarawas County, ODNR authoritative) | Closed — not Wayne entity |
| 3 | ~~HIGH~~ RESOLVED | PAD-US — Mohler Wildlife Area (Holmes County, ODNR authoritative) | Closed — not Wayne entity |
| 4 | MEDIUM | PAD-US — Kinney Trail Park (49ac, City of Wooster) not in DB | **STAGED** 2026-06-08 — needs GPS acquisition + pipeline |
| 5 | MEDIUM | PAD-US — Schellin Park (13ac, City of Wooster, 427 Maple St) not in DB | **STAGED** 2026-06-08 — GPS confirmed (40.7942, -81.9349) |
| 6 | LOW | PAD-US — Cohan Park (6ac, City of Wooster) not in DB | **STAGED** 2026-06-08 — GPS confirmed (40.8272, -81.9440) |
| 7 | MEDIUM | WA-AP-0001/0002 share GPS (boat launch + fishing pier) | Acquire individual GPS |
| 8 | LOW | WA-S-0005 child site GPS = parent GPS | Flag for individual GPS at field verification |
| 9 | LOW | trail_parents empty for Wayne — 5 clear trail-site relationships unrecorded | Backfill when Wayne is next worked |
| 10 | LOW | WA-T-0013 still identity_uncertain | Resolve at field verification or via Chippewa Township contact |

---

## Actions Taken This Session

- Moved 4 APs (WA-AP-0003/0004/0013/0015) from access_points to held_entities (parent_held)
  per IMP-025 fix applied 2026-06-08.
- Populated WA-S-0001 acres = 102 (from PAD-US two-parcel sum).
- Revised PAD-US completeness finding from PASS to FAIL based on full GDB spatial analysis.

## Pending Actions

**Blocking — pipeline required for staged supplemental records:**
- Run GPS acquisition for Kinney Trail Park (no GPS in staging record — PAD-US centroid only)
- Run normalization + upsert for 3 staged records (Schellin Park, Kinney Trail Park, Cohan Park)

**Non-blocking:**
- Flag The Wilderness Center (Stark County primary, TWC) for Stark County T7 discovery
- Flag Mohler Wildlife Area for Holmes County T2 discovery
- Flag Beach City Wildlife Area for Tuscarawas County T2 discovery
- Acquire individual GPS for WA-AP-0001 and WA-AP-0002
- Backfill trail_parents for 5 Wayne trails (WA-T-0001 through 0004, 0011)
- Resolve WA-T-0013 (Chippewa Township trails) — field visit or township contact
- Release WA-S-0045/0046, WA-T-0014/0015 when Holmes, Ashland, Stark County pipelines run

---

## Quality Review Outcome

**Status: PASS with pipeline work required.** PAD-US GAP2 concerns (Wilderness Center,
Beach City WA, Mohler WA) all resolved to bbox false positives — not Wayne entities. Three
T6 City of Wooster parks (Schellin, Kinney Trail, Cohan) confirmed missing and staged as
supplemental records. No FK integrity issues remaining. All held entities correctly held.
Staged records require GPS acquisition and pipeline processing before the county is fully
complete.

*Review completed 2026-06-08 by Claude. PAD-US section revised and supplemental discovery
completed 2026-06-08 after full GDB spatial analysis and source verification.*
