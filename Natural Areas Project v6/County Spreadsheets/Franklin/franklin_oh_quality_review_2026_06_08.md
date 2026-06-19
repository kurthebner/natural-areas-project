# Franklin County — Quality Review
**Date:** 2026-06-08
**Reviewer:** Claude (automated + manual)
**Pipeline runs:** franklin_oh_2026_03_25 (initial); franklin_oh_2026_05_11_pos_supplement (IMP-097/099 P&OS remediation)
**DB state at review:** post both pipeline runs

---

## Entity Counts (live DB)

| Entity type | Count | Notes |
|---|---|---|
| Sites | 1,164 | OH-FR-S- prefix: 1,157; OH-MC-S- prefix: 7 |
| Trails | 120 | Includes OH-MC-T- multi-county trails |
| Trail segments | 3 | All under OH-FR-T-0001 (Olentangy River Water Trail) |
| Trail networks | 3 | OH-FR-TN-0001/0002, OH-MC-TN-0003 |
| Trailthings | 0 | v5 run — expected |
| Site networks | 17 (live) + 1 (MC) | 17 county + OH-MC-SN-0001 |
| Access points | 0 | None in Franklin |
| Held entities | 0 | None |

Run metadata:
- `franklin_oh_2026_03_25`: input=1174, normalized=1174, held=0
- `franklin_oh_2026_05_11_pos_supplement`: input=137, normalized=137, held=0

Max site sequence number: OH-FR-S-1181. Total OH-FR-S- sites: 1,157 → 24 ID gaps expected from retired discovery candidates (IMP-117).

---

## GPS Audit

**Sites:** All 1,164 sites have GPS coordinates. No nulls. No out-of-Ohio bounding-box values.

**Apparent GPS clusters at 3-decimal rounding** — three groups of 4 sites that round to the same coordinates. Full-precision inspection confirms each site has distinct coordinates; the visual clustering reflects genuine dense geographic proximity, not centroid fallbacks:

| Cluster | Sites (rounded coords) | Character |
|---|---|---|
| (39.948, -82.911) | Park Place Park, Cooper Park, Mock Road Park, Cross Creek Park | Mixed-governance parks in Columbus/Hilliard/Dublin boundary zone |
| (39.951, -82.914) | John Burroughs Park, Madison Mills Park, Sammons Park, Scioto Audubon Park | Columbus R&P parks along Scioto corridor |
| (40.127, -83.069) | 190 N High Open Space, Bishop's Crossing Open Space, Gorden Farms Open Space, Maroa Wilcox Open Space | Dublin micro-open-spaces (<0.01ac) in same development |

All three clusters are **acceptable** — legitimate small parks physically near each other. No GPS action needed.

**Held entities:** None (nothing to audit here).

---

## Held Entities

None. Correct — Franklin had no cross-county candidates requiring hold.

---

## PAD-US Completeness Gate

**Full GDB spatial query** run via `na_padus_query.py Franklin` on 2026-06-08.

- PAD-US records in Franklin bbox: 1,043
- Matched (score ≥ 80): 828
- Unmatched: 179
- Skipped (private/closed/excluded): 36

**Skipped correctly:** Private golf courses and country clubs, closed reservoirs (Hoover Reservoir Park, O'Shaughnessy Reservoir Park — both marked "Closed" in PAD-US; O'Shaughnessy is Delaware County primary anyway), Sharon Woods and Three Creeks Metroparks (closed access — have Open Access counterparts matched under different PAD-US records).

### Unmatched breakdown

**Out of scope — not natural areas/parks:**
- ~70 Columbus City Schools and suburban school campuses (PAD-US includes school grounds as public land; school grounds are not NAP scope)
- Athletic complexes used exclusively for organized sports (Galloway Rd Sports Complex, Pickerington Youth Athletic Association)
- Pure infrastructure (trail connectors at 0ac, amphitheaters, levee gates)
- Golf courses (Turnberry, Blacklick Golf Course)
- County office land / administrative parcels

**Near-miss false misses (in DB, just below threshold):**

| PAD-US name | Score | DB record | Notes |
|---|---|---|---|
| Brobst Memorial (15ac) | 76 | OH-FR-S-1181 Robert M. Brobst Park | Name variant — Madison Township park |
| Paul S. Metzger (31ac) | 74 | OH-FR-S-0777 Metzger Park | Formal name vs. common name |
| Camp Chase Trail (74ac) | 77 | OH-MC-T-0003 (trails table) | Trail in trails table, not sites table |

**Confirmed genuine discovery gaps:**

| PAD-US name | GAP | Acres | Owner | Tier | Status |
|---|---|---|---|---|---|
| O'Shaugnessy Reservoir | 4 | 1,279 | City Land (Columbus) | T2 | **RESOLVED** — Delaware County primary; dam area clips Franklin bbox southern edge — bbox false positive; no Franklin action |
| Darby Creek Conservation Tnc | 2 | 105 | City Land (filed under Columbus) | T7 | **MISS** — TNC not represented as governance in Franklin DB; conservation land along Big Darby Creek corridor |
| River Bluffs | 4 | 45 | City Land | T6 | **MISS** — no match in DB; Columbus park |
| Glen Echo Ravine Restoration & Protection | 2 | 10 | City Land | T6 | **MISS** — distinct from OH-FR-S-0180 Glen Echo Park; separate conservation area |
| Brandon Open Space A/B | 2 | 6+9=15 | City Land (Dublin) | T6 | **MISS** — Dublin open spaces not in DB (Dublinshire Greenway cataloged but not Brandon parcel group) |
| Hawks Nest Open Space A/D/E | 2 | ~15 combined | City Land (Dublin) | T6 | **MISS** — Dublin subdivision open spaces not in DB |
| Tartan West Open Space (A–W, 17 parcels) | 2 | ~60 total | City Land (Dublin) | T6 | **MISS** — subdivision open spaces; we have Tartan Ridge Park (OH-FR-S-0516) but not Tartan West separately |
| Riverside Woods Open Space A/B | 2 | 2+19=21 | City Land (Dublin) | T6 | **MISS** — Dublin open spaces not in DB |
| Woerner-Temple Open Space A/B/C | 2 | ~5 combined | City Land (Dublin) | T6 | **MISS** — Dublin open spaces not in DB |

**Note on Dublin GAP2 open spaces:** PAD-US treats each lettered Dublin subdivision open space parcel as a distinct record. These may be sub-parcels of existing Dublin parks we already catalog, or they may be genuinely distinct open spaces not yet discovered. The IMP-097/099 P&OS remediation run (2026-05-11) added sites from the MORPC ArcGIS layer; these Dublin parcels were apparently not in that layer or were absorbed into parent park records. Low-to-medium priority for supplemental T6 Dublin discovery.

**PAD-US result: PARTIAL PASS.** Key natural area tiers (T1–T5, T7) appear complete. T6 has genuine gaps: several Dublin GAP2 open space parcel groups, River Bluffs (45ac), and TNC conservation land along Darby Creek. O'Shaughnessy Reservoir (1,279ac) resolved as Delaware County primary — bbox false positive; flag for Delaware T2 discovery.

---

## Relationship Table Audit

**site_network_members:** All FK references valid — no orphaned membership records. ✓

**Site network membership anomalies (systemic, not integrity failures):**
The Columbus Recreation and Parks SN (OH-FR-SN-0003) contains 548 members — roughly 47% of all Franklin sites. This includes many sites governed by Dublin, Gahanna, Hilliard, Westerville, Upper Arlington, Metro Parks, and townships, not just Columbus-governed sites. Similarly, the Dublin SN (OH-FR-SN-0004) contains 5 sites with non-Dublin governance (Scioto Audubon Metro Park, Hickory Woods Nature Preserve, Kiwanis Riverway Nature Preserve, Northeast Park, Scioto Shores Parkland).

This appears to be a systemic artifact of the original Franklin pipeline treating Columbus R&P as a regional umbrella and Dublin as a geographic rather than governance-based network. Specific anomalies:
- OH-FR-S-0825 (Cross Creek Park, Hilliard governance) appears in BOTH Columbus SN and Hilliard SN — duplicate membership
- OH-FR-S-0797 (First Responders Park, Westerville governance) in Hilliard SN — wrong network

Correcting these systematically would require a full SN membership re-derivation pass. Logged as LOW severity — cosmetic issue, does not affect site discovery completeness.

**trail_parents:** 90/120 Franklin trails have trail_parents entries. 30 trails without:
- All 30 are greenway trails, water trails, multi-county trail corridors, and trail connectors — entity types that by nature span multiple sites and have no single parent site
- No integrity violation; these are expected structural gaps

**site_parent:** Franklin has no parent-child site relationships in the `site_parent` table — consistent with discovery record (no v6 child sites discovered).

**access_point_parents:** No Franklin access points exist — nothing to audit.

---

## Duplicate / Ambiguous Site Records

| Finding | Sites | Evidence | Severity |
|---|---|---|---|
| Friendship Park — same name, same acreage, different governance | OH-FR-S-0047 (Prairie Township, 22.67ac) and OH-FR-S-1026 (Gahanna, 22.67ac) | GPS ~200m apart, identical acreage; park likely straddles Prairie Township / Gahanna boundary or was transferred. S-1026 is parent of Friendship Park Community Garden, Gazebo, Shelter. | MEDIUM — possible duplicate; requires field verification or city/township records to determine if one entity or two |
| "Muffin Township" name corruption — typo for Mifflin Township | OH-FR-S-1114 (0.73ac) and OH-FR-S-1115 (8.45ac) | Both records were stored with name "Muffin Township" — a corruption of "Mifflin Township" (no Muffin Township exists in Franklin County). A third record OH-FR-S-1077 (12.42ac) was correctly named "Mifflin Township." All three are Gahanna-governed cemetery parcels within ~180m of each other — sections of the same Mifflin Township Cemetery complex. | **FIXED 2026-06-08** — renamed S-1114 and S-1115 to "Mifflin Township" in DB. Three co-named parcels remain; disambiguation by acreage or section label deferred pending MORPC parcel name verification. |
| Tanglebrook Park — same name, distinct entities | OH-FR-S-0867 (Grove City, 5.33ac) and OH-FR-S-1180 (Jackson Township, null acres) | GPS ~400m apart, different governance. Two parks with same name in adjacent jurisdictions. | NOT a duplicate — distinct entities, accept as-is |

---

## Known Pre-Existing Issues

**IMP-024 — OH-FR-S-1040 underlying site gap:** Site ID OH-FR-S-1040 does not exist in the DB. This ID was noted during the original pipeline run as a gap between a parent entity and a linked underlying site. With max sequence 1181 and 1157 sites, 24 ID gaps exist in the Franklin sequence — consistent with discovery retirements during pipeline processing. OH-FR-S-1040 was apparently retired. The ID gap is expected per IMP-117.

---

## Data Quality Findings

| # | Severity | Finding | Action |
|---|---|---|---|
| 1 | ~~MEDIUM~~ RESOLVED | PAD-US — O'Shaughnessy Reservoir (1,279ac) | Delaware County primary; dam clips Franklin bbox — bbox false positive. Flag for Delaware County T2 discovery. |
| 2 | MEDIUM | PAD-US — Darby Creek Conservation TNC (105ac, GAP2) not in DB | Supplemental T7 discovery — confirm TNC Franklin County presence; verify if separate from Big Darby Creek S&NSR or Battelle Darby |
| 3 | MEDIUM | PAD-US — River Bluffs (45ac, Columbus) not in DB | Supplemental T6 discovery |
| 4 | MEDIUM | Friendship Park possible duplicate (S-0047 vs S-1026, same acreage) | Field verify or check Prairie Township/Gahanna records; if same entity, retire S-0047 (older record, no children) and merge notes |
| 5 | LOW | PAD-US — Glen Echo Ravine Restoration & Protection (10ac, GAP2) not in DB | Supplemental T6 discovery — may be a conservation corridor separate from Glen Echo Park |
| 6 | LOW | PAD-US — Dublin GAP2 open space parcels (Brandon, Hawks Nest, Tartan West, Riverside Woods, Woerner-Temple) not in DB | Supplemental T6 Dublin discovery pass — determine if sub-parcels of existing parks or distinct entities |
| 7 | ~~LOW~~ FIXED | "Muffin Township" name corruption in S-1114/S-1115 (no Muffin Township exists; should be Mifflin Township) | **Fixed 2026-06-08** — renamed to "Mifflin Township" in DB. Three co-named Mifflin Township cemetery parcels now exist (S-1077/1114/1115); verify MORPC parcel names for disambiguation |
| 8 | LOW | Columbus SN (OH-FR-SN-0003) contains ~60 non-Columbus sites; Dublin SN (OH-FR-SN-0004) contains 5 non-Dublin sites | SN membership re-derivation during next Franklin pipeline pass; Cross Creek Park (S-0825) has duplicate membership in Columbus + Hilliard SN — remove from Columbus SN |

---

## Actions Taken This Session

- Renamed OH-FR-S-1114 and OH-FR-S-1115 from "Muffin Township" to "Mifflin Township" (name corruption — no Muffin Township exists in Franklin County). Three Mifflin Township cemetery parcels now correctly named in DB (S-1077, S-1114, S-1115).

---

## Pending Actions

**Supplemental discovery (batch with other counties):**
- Flag O'Shaughnessy Reservoir for Delaware County T2 discovery (bbox false positive in Franklin — reservoir is Delaware County primary)
- T7: Investigate Darby Creek Conservation TNC (105ac) — confirm identity vs. existing Darby Creek records
- T6: Stage River Bluffs (45ac, Columbus)
- T6: Dublin open space supplemental pass (Brandon, Hawks Nest, Tartan West, Riverside Woods, Woerner-Temple parcel groups)

**Data corrections (batch):**
- Resolve Friendship Park possible duplicate (S-0047 / S-1026)
- Verify MORPC parcel names for three Mifflin Township cemetery parcels (S-1077/1114/1115) to disambiguate co-named records
- Correct OH-FR-S-0825 Cross Creek Park: remove from Columbus SN (OH-FR-SN-0003) — keep in Hilliard SN only
- Correct OH-FR-S-0797 First Responders Park (Westerville): remove from Hilliard SN (OH-FR-SN-0008) — reassign to Westerville SN (OH-FR-SN-0015)

---

## Quality Review Outcome

**Status: PASS with supplemental work needed.** All GPS present, no FK integrity issues, no held entities, no cross-county conflicts. Trail and site network counts are consistent with Franklin County's scale (1,164 sites, 120 trails). PAD-US reveals a small number of T6 discovery gaps — most significantly O'Shaughnessy Reservoir (1,279ac) and TNC conservation land along Darby Creek. Several Dublin GAP2 open space parcel groups are unmatched and require supplemental T6 discovery. No blocking pipeline issues; all gaps are supplemental discovery and minor data correction items.

*Review completed 2026-06-08 by Claude.*
