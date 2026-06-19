# Wood County, Ohio — Discovery Handoff Document
# Natural Areas Project v5.2
# Discovery completed: 2026-04-14
# Last updated: 2026-05-16 (supplemental upsert complete — BSC properties in DB)
# Pipeline status: COMPLETE (supplemental upsert 2026-05-16; 73 sites, 4 trails in DB)
# Maintenance: 2026-05-23 — phantom deletion (SI-028) + address/GPS corrections (15 sites)

---

## ⚠️ T7 DEFECT — REMEDIATED 2026-05-16

**Root cause:** BSC "Land We Own" portfolio was never enumerated per IMP-029 during Wood County T7. Only BSC's conservation *interest* in WCPD's Black Swamp Preserve was noted; BSC-owned properties were not individually checked.

**Identified via:** Hancock County T7 cross-county audit (2026-05-16). The Hancock T7 pass exhaustively enumerated all 16 BSC-owned preserves; two were found to be in Wood County and absent from Wood County staging.

**Remediation:** Three records added to `wood_oh_raw_discovery.yaml` on 2026-05-16:
- `Bell Woods Nature Preserve` — T7 Site, BSC-owned, 80 ac, guided tours only, Pemberville
- `Pat & Clint Mauk's Prairie` — T7 Site, BSC-owned, 30 ac, public access dawn–dusk, Pemberville
- `Pat & Clint Mauk's Prairie Trail` — T7 Trail, 1-mile public trail with Storybook Trail, BSC

**Resolution (2026-05-16):** Supplemental upsert complete. Three records normalized and inserted directly to `natural_areas_v5.db` using next available IDs in the OH-WOD-* series:
- `OH-WOD-SI-076` — Bell Woods Nature Preserve (Nature Preserve / Private Nature Preserve, 80 ac, GPS null — not in OSM)
- `OH-WOD-SI-077` — Pat & Clint Mauk's Prairie (Natural Area / Prairie, 30 ac, GPS null — not in OSM)
- `OH-WOD-TR-002` — Pat & Clint Mauk's Prairie Trail (Hiking, 1.0 mi, Natural Surface)

`run_metadata` updated: records_input and normalized both incremented by 3. TSV files (wood_oh_sites.tsv, wood_oh_trails.tsv) regenerated from DB — now current.

---

## Discovery Complete — 100 Entity Records (post-remediation)

| Type | Count |
|------|-------|
| Sites | 93 *(+2 BSC: Bell Woods NP + Pat & Clint Mauk's Prairie)* |
| Trails | 4 *(+1 BSC: Pat & Clint Mauk's Prairie Trail)* |
| Access Points | 3 |
| **Total** | **100** |

All records written to: `wood_oh_raw_discovery.yaml`

**DB state after 2026-05-23 maintenance:** 73 active sites (3 phantoms/duplicates deleted: SI-028 phantom, SI-034 Huron County entity, SI-035 Sandusky County duplicate), 4 held SEED entities in `held_entities`, 4 trails.

**⚠️ TSV files stale as of 2026-05-23** — `wood_oh_sites.tsv` reflects pre-maintenance DB state. Needs regeneration to incorporate: SI-028 deletion, 15 address/GPS/notes corrections. Regenerate by re-running Stage 4 of the Wood County pipeline, or via targeted SQL export.

---

## Tier Results Summary

| Tier | Governance | Result |
|------|-----------|--------|
| 1 | Federal / Tribal | **NULL** — no federal lands in Wood County |
| 2 | State | 15 sites, 2 trails, 1 AP |
| 3 | District (Metroparks Toledo) | **NULL** — all Lucas County |
| 4 | County (WCPD) | 22 sites, 1 trail |
| 5 | Township | **NULL** — no township parks |
| 6 | Municipal | 51 sites, 2 APs |
| 7 | Conservancy | 3 records *(1 original: Mishe Monoto Preserve; +2 BSC sites + 1 BSC trail added 2026-05-16 defect remediation)* |
| 8 | Private | 2 sites |

---

## Pre-Pipeline Manual Review Required

The following 7 records are flagged and should be reviewed before or during normalization:

### Hold / Verify Before Pipeline — RESOLVED 2026-05-23

1. **Nature Trails Park (WCPD)** — DELETED (OH-WOD-SI-028, 2026-05-23). Confirmed AutoRecovered phantom. Exhaustive review of wcparks.org shows no WCPD property by this name. The astronomical observation program (large telescope, observation deck) cited in the original discovery record belongs to **Beaver Creek Preserve** (OH-WOD-SI-019), confirmed via wcparks.org. Birding tour citations of "Cedar Creeks Preserve and Nature Trails Park" refer to the City of Northwood park at 4950 Curtice Rd (OH-WOD-SI-064), not a WCPD entity.

2. **Wakeman Preserve** — DELETED from sites (OH-WOD-SI-034). AutoRecovered baseline phantom. Zero web evidence of a WCPD property by this name. "Wakeman" refers to Wakeman, Ohio in **Huron County** — outside WCPD service territory. Real Wakeman entities to discover during Huron County pipeline run: **Wakeman Community Park** (Tier 6 — municipal) and **Augusta-Anne Olsen Nature Preserve** (Tier 7 — land trust/conservancy). Neither is currently in the DB.

3. **White Star Park** — DELETED from sites (OH-WOD-SI-035). Duplicate of **OH-SAN-S-023** (White Star Park, Sandusky County Park District, ~797 acres, Gibsonburg OH 44833). AutoRecovered baseline incorrectly attributed this Sandusky County property to WCPD.

### Unconfirmed Baseline Seeds — UPDATED 2026-05-23
All four retained in `held_entities` as GNIS geographic/historical place names with no managing agency. `hold_detail` updated to clarify GNIS status and confirmed absence from all public land inventories.

4. **Devils Hole Prairie** (OH-WOD-SEED-001) — GNIS feature, Webster Township, N41.4501 W83.5624 (USGS Dunbridge quad). No managing agency.
5. **Hulls Prairie** (OH-WOD-SEED-002) — GNIS feature. Location now "Hull Prairie Farms" residential subdivision; prairie likely extirpated. No managing agency.
6. **Tontogany Prairie** (OH-WOD-SEED-003) — GNIS feature near Tontogany village. No managed access found. No managing agency.
7. **North Baltimore Reservoir** (OH-WOD-SEED-004) — Municipal water utility reservoir. Not a natural area. No managing agency.

---

## Identity Conflicts to Resolve During Normalization

| Conflict | Action |
|----------|--------|
| Black Swamp Preserve (3 records: WCPD, City of BG, BSC) | Keep WCPD as primary; link City of BG; BSC = conservation interest only |
| Carter Historic Farm / Carter Park (same address) | Keep as 2 distinct entities — different governance, different programs |
| Fort Meigs / Fort Meigs State Memorial (2 baseline seeds) | Merge to single record |
| Rossford City Park and Marina / Veterans Memorial Park | Probable same — confirm and merge if so |
| Saint Johns Woods / Wintergarden/St. John's Nature Preserve | Probable same — confirm and merge if so |
| BGSU Native Prairie Garden (4 sub-sites) | Decide: single parent record or 4 child sites |

---

## New Entities vs. AutoRecovered Baseline

| Entity | Tier | Notes |
|--------|------|-------|
| Arrowwood Archery Range | 4 (WCPD) | On current WCPD site; not in AutoRecovered |
| Wood County Museum | 4 (WCPD) | On current WCPD site; not in AutoRecovered |
| Van Tassel Wildlife Area | 2 (State) | ODNR DOW; not in AutoRecovered |
| Beech Street Park (Rossford) | 6 (Municipal) | Not in AutoRecovered |
| All 4 Northwood parks | 6 (Municipal) | Not in AutoRecovered |
| Railway Park (Walbridge) | 6 (Municipal) | Not in AutoRecovered |
| Mehring Park + Centennial Park (Tontogany) | 6 (Municipal) | Not in AutoRecovered |
| Grand Rapids Park | 6 (Municipal) | Not in AutoRecovered |
| Pemberville Memorial Park | 6 (Municipal) | Not in AutoRecovered |
| Mishe Monoto Preserve | 7 (Conservancy) | Baseline seed confirmed; not in AutoRecovered |

---

## GPS Acquisition Priority

### Resolved 2026-05-23 (wod_address_gps_update_v1.py)
The following GPS gaps were closed and addresses confirmed via wcparks.org and northwoodoh.gov:
- OH-WOD-SI-017 Arrowwood Archery Range — `11126 Linwood Rd, Bowling Green` — GPS acquired
- OH-WOD-SI-018 Baldwin Woods Preserve — `14080 Range Line Rd, Weston` — GPS acquired
- OH-WOD-SI-019 Beaver Creek Preserve — `23028 Long Judson Rd, Grand Rapids` — GPS acquired
- OH-WOD-SI-020 Black Swamp Preserve — address corrected to `1014 S Maple St, Bowling Green`; GPS acquired
- OH-WOD-SI-024 Cedar Creeks Preserve — `4575 Walbridge Rd, Northwood` — GPS acquired
- OH-WOD-SI-025 Cricket Frog Cove — `14810 Freyman Rd, Cygnet` — GPS acquired
- OH-WOD-SI-026 Fuller Preserve — address corrected to `12153 Cross Creek Rd, Bowling Green`; GPS acquired
- OH-WOD-SI-030 Rudolph Bike Park — address corrected to `14045 Mermill Rd, Rudolph`; GPS corrected
- OH-WOD-SI-031 Rudolph Savanna — `10330 Rudolph Rd, Rudolph` — GPS acquired
- OH-WOD-SI-063 Ranger Park (Northwood) — `3201 Curtice Rd, Northwood` — GPS acquired
- OH-WOD-SI-064 Nature Trails Park (Northwood) — `4950 Curtice Rd, Northwood` — GPS acquired (user-provided)
- OH-WOD-SI-065 Central Park (Northwood) — `Oram Rd, Northwood` — GPS acquired
- OH-WOD-SI-066 Brentwood Park (Northwood) — `320 Brentwood Dr, Northwood` — GPS acquired
- OH-WOD-SI-016 Adam Phillips Pond — address corrected to `1740 E Gypsy Lane Rd, Bowling Green` (GPS preserved)

### Resolved Batch 2 — `wod_gps_batch2_v1.py` (2026-05-23)
Nominatim/OSM geocoding for 23 additional sites (Bowling Green, Perrysburg, Rossford,
Tontogany, Walbridge, Grand Rapids, Pemberville, BGSU). Run to close these gaps:
- SI-039 Bellard Park / SI-043 Conneaut Haskins Park / SI-045 Raney Park / SI-046 Ridge Park (Bowling Green)
- SI-048 through SI-057 (all 10 City of Perrysburg parks except Woodland Park)
- SI-059 Veterans Memorial Park / SI-060 Island View Park / SI-062 Beech Street Park (Rossford)
- SI-068 Railway Park (Walbridge) / SI-069 Mehring Park / SI-070 Centennial Park (Tontogany)
- SI-071 Grand Rapids Park / SI-072 Memorial Park (Pemberville)
- SI-075 BGSU Native Prairie Garden (approximate — Wintergarden Rd)

### Still GPS-missing (20 sites after both batches)
- **ODNR DOW Wildlife Areas** SI-003,004,005,006,007,008,009,010,011 (WCA 1,2,4-10) → ODNR GIS layer (wildohio.gov/maps)
- **SI-012** Bairdstown Wildlife Production Area → ODNR GIS
- **SI-013** Dry Creek Wildlife Area → ODNR GIS (~US-24 & Township Rd 6C)
- **SI-015** Van Tassel Wildlife Area → ODNR GIS
- **SI-029** Otsego Park (WCPD) — address confirmed `20000 W River Rd, Bowling Green`; not in OSM; needs WCPD contact or field GPS
- **SI-044** Dunbridge Road Soccer Fields (BG) — location `behind Municipal Court` is approximate; needs confirmation
- **SI-058** Woodland Park (Perrysburg) — not in OSM
- **SI-061** Ed Ford Memorial Park (Rossford) — not in OSM
- **SI-067** Village Park (North Baltimore) — not in OSM
- **SI-073** Mishe Monoto Preserve — no street address in any source
- **SI-076** Bell Woods Nature Preserve (BSC) — GPS null noted at discovery
- **SI-077** Pat & Clint Mauk's Prairie (BSC) — GPS null noted at discovery

---

## Features Vocabulary Notes

The following raw features strings will need FEATURE_MAP processing:
- "Boat launch" → "Watercraft Access"
- "Boat dock" → "Watercraft Access"
- "Disc golf" → "Disc Golf Course" (confirm in vocabulary)
- "Rock climbing / bouldering / rappelling" → confirm vocabulary terms
- "Pump track / BMX" → confirm vocabulary terms
- "Sledding hill" → confirm vocabulary term
- "Fossil dig" → check if vocabulary has a term
- "Astronomical telescope" → check vocabulary

Run Stage 4.5 vocabulary validation gate carefully — Wood County has more diverse features than Fulton County.

---

## Municipalities Unresolved (for future session)
- **Luckey** (village) — no parks confirmed; small rural village
- **Weston** (village) — no parks confirmed; Fuller Preserve (WCPD) is nearby but not a Weston municipal entity

---
## 2026-06-09 Batch Resolution Update

### Completed
- Deleted OH-WOD-S-0015 (Van Tassel WA single-county dup, superseded by MC-S-0029) ✓
- Deleted OH-LUC-S-0045 (Maumee State Forest single-county dup, superseded by MC-S-0031) ✓
- Removed OH-WOD-SI-0073 (Mishe Monoto Preserve) from held_entities; flagged for Pickaway/Hocking T7 ✓
- trail_parents: T-0002→S-0077, T-0038→MC-S-0027, T-0039→MC-S-0027 inserted ✓
- GPS updated (PAD-US centroids): S-0002,S-0010,S-0014,S-0016,S-0022,S-0037,S-0038,S-0041,S-0074 ✓
  - S-0016/S-0037 shared coordinate resolved (S-0016 now 41.354428,-83.617008; S-0037 now 41.351261,-83.616104)
  - S-0014 Maumee River Weir Rapids: large delta corrected (41.402,-83.876 → 41.459963,-83.766867)
  - S-0022 Buttonwood: large delta corrected (41.545,-83.5795 → 41.546992,-83.67248)
- Acreages populated for S-0003(38ac),S-0004(77ac),S-0005(73ac),S-0008(39ac),S-0010(64ac),S-0014(6ac) ✓
- Held seeds deleted: S-0079 Hulls Prairie, S-0080 Tontogany Prairie, S-0081 North Baltimore Reservoir ✓
  (all three: historical place names with no managed public natural area)
- Wood County Historical Center = Wood County Museum (S-0037, same address/governance); no new entity ✓
- Providence/Bend View/Farnsworth 451ac: Bend View + Farnsworth already in DB as Lucas County entities;
  no additional Wood County land beyond MC-S-0027 ✓

### Remaining / Manual Review Queue
- ~~T-0001 Slippery Elm Trail: trail_parent not assigned~~ RESOLVED 2026-06-12: T-0001 → OH-WOD-S-0029 (Otsego Park). (MRQ 2)
- ~~MC trails (T-0001/0201/0202/0204/0217): Wood County site parents not assigned~~ RESOLVED 2026-06-12: T-0001→S-0069+S-0071 (Mehring+Grand Rapids); T-0201/T-0202→MC-S-0027 (Providence Metropark); T-0204→S-0022 (Buttonwood); T-0217→S-0072 (Pemberville Mem Park). (MRQs 3–7)
- ~~WOD-FIREMANS-PARK~~ RESOLVED 2026-06-12: Inserted as OH-WOD-S-0078 (Fireside Park, Lake Township, 1909 Ayers Rd, Millbury, 5ac, GPS 41.5731755,-83.4300309). (MRQ 186)
- ~~WOD-BRADNER-PRESERVE~~ RESOLVED 2026-06-12: Already in DB as OH-WOD-S-0021 (Bradner Preserve & Community Center, 233ac). PAD-US 124ac centroid is subset parcel. (MRQ 189)
- S-0078 Devils Hole Prairie: in manual_review_queue; check BSC or WCPD for managed public access
- Supplemental T3: Nona Park Stone Quarry and Ball Fields (80ac, Metroparks of Toledo) — not yet staged
- Supplemental T6 municipal parks (9 items) — not yet staged; lower priority
- T-0038/0039 sequence gap (v5.2 pipeline artifact) — note documented in review doc; log in session log
- WA sites S-0006/0007/0009/0011/0012: GPS coords fall outside Wood County bbox — verify county assignment
