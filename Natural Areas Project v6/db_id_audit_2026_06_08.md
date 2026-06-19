# Natural Areas DB — ID Integrity Audit
**Date:** 2026-06-08  
**Database:** NASqlite/natural_areas_v6.db  
**Total entity records:** 3,049 across 7 tables + 58 held  
**County runs on record:** 21 (across 17 counties)

---

## Summary

The database contains 12 distinct ID integrity issues spanning wrong formats,
wrong type codes, wrong tables, non-standard ID schemes, and one category of
genuine numeric collision. Issues are grouped by severity.

---

## CRITICAL — Genuine Numeric Collision

### Issue 1: MC-T dual-format numeric overlap (10 collisions)

The multi-county trail sequence has **two parallel ID sets** — a 3-digit set from
older runs and a 4-digit zero-padded set from newer runs — that claim the same
sequence numbers for different entities.

| # | 3-digit ID | Entity | 4-digit ID | Entity |
|---|---|---|---|---|
| 1 | OH-MC-T-001 | North Country National Scenic Trail | OH-MC-T-0001 | Maumee River Water Trail |
| 2 | OH-MC-T-002 | Miami & Erie Canal Towpath Hiking Trail | OH-MC-T-0002 | Wabash Cannonball Trail |
| 23 | OH-MC-T-023 | Oak Openings Hiking Trail | OH-MC-T-0023 | Coyote Run Trail |
| 24 | OH-MC-T-024 | Oak Openings Horse Trail | OH-MC-T-0024 | Scenic River Trail |
| 25 | OH-MC-T-025 | Oak Openings Foxfire Trail | OH-MC-T-0025 | Nature Center Loop Trail |
| 26 | OH-MC-T-026 | Oak Openings Mallard Lake Loop | OH-MC-T-0026 | Big Meadows Path |
| 27 | OH-MC-T-027 | Oak Openings Ridge Trail | OH-MC-T-0027 | Dripping Rock Trail |
| 28 | OH-MC-T-028 | Oak Openings Sand Dunes Trail | OH-MC-T-0028 | Overlook Trail |
| 29 | OH-MC-T-029 | Oak Openings Ski Trails | OH-MC-T-0029 | Wetland Spur Trail |
| 30 | OH-MC-T-030 | Oak Openings Springbrook Lake Trail | OH-MC-T-0030 | Alder Trail |

SQLite treats these as distinct strings, so no row-level collision exists. But any
code that normalizes padding (e.g., `int("023") == int("0023")`) will silently
misfetch. Cross-references in relationship tables are also ambiguous by inspection.

**3-digit MC-T records (16 total):** from Ottawa (Oak Openings trails), Lucas
(North Country NST, Towpath trails), and other early county runs.  
**4-digit MC-T records (37 total):** from Franklin, Wayne, and later county runs.

---

## HIGH — Wrong Table or Wrong Record

### Issue 2: OTT-AP-006 in sites table

`OH-OTT-AP-006` ("West Harbor Boat Launch") is stored in the **sites** table,
not in access_points. It does not appear in access_points at all. The AP-type ID
makes this a misfiled entity.

---

## MEDIUM — Wrong Type Codes

These use legacy or incorrect type-code segments that deviate from current protocol
(`S` for sites, `T` for trails, `AP` for access points, `TN` for trail networks,
`TT` for trailthings, `SN` for site networks).

### Issue 3: MC-TR legacy type code (6 trails)
Multi-county trails with `TR` type code (v5 "trail variant") instead of `T`:

| ID | Name |
|---|---|
| OH-MC-TR-001 | Miami and Erie Canal Towpath |
| OH-MC-TR-002 | Portage River Water Trail |
| OH-MC-TR-003 | Buckeye Trail — Delphos Section |
| OH-MC-TR-004 | Buckeye Trail — Defiance Section |
| OH-MC-TR-005 | Stewardship Trail |
| OH-MC-TR-007 | Wabash Cannonball Trail (North Fork) |

### Issue 4: MC-SI legacy type code in sites (3 records)
Multi-county sites with `SI` type code (v5 "site variant") instead of `S`:

| ID | Name |
|---|---|
| OH-MC-SI-001 | Mary Jane Thurston State Park |
| OH-MC-SI-003 | Maumee State Forest |
| OH-MC-SI-006 | Oak Openings Corridor (Metroparks Toledo — Fulton County parcels) |

### Issue 5: WOD-SI legacy type code in sites (71 records)
Wood County sites with `SI` type code instead of `S`.  
Range: OH-WOD-SI-002 through OH-WOD-SI-077 (with gaps).

### Issue 6: FUL-SI legacy type code in sites (35 records)
Fulton County sites with `SI` type code instead of `S`.  
Range: OH-FUL-SI-001 through OH-FUL-SI-037 (with gaps).

### Issue 7: Single-county TR type code (8 trails)
Three counties used `TR` ("trail variant") instead of `T`:

| County | Count | Range |
|---|---|---|
| WIL (Williams) | 1 | OH-WIL-TR-002 |
| WOD (Wood) | 2 | OH-WOD-TR-001, OH-WOD-TR-002 |
| FUL (Fulton) | 5 | OH-FUL-TR-001 through OH-FUL-TR-006 |

### Issue 8: PUT-A wrong type code in access_points (3 records)
Putnam County access points stored with `A` type code instead of `AP`:

| ID | Name |
|---|---|
| OH-PUT-A-001 | Arrowhead Landing |
| OH-PUT-A-002 | Reservoir Landing |
| OH-PUT-A-003 | Fort Jennings Park River Access |

---

## MEDIUM — Non-Standard ID Schemes

### Issue 9: SEED- prefix IDs in held_entities (25 records)
Twenty-five Hardin County held entities use a `SEED-{name}` ID format with no
`OH-` prefix and no type code. This is outside the entity ID standard entirely.
All are Sites for Hardin County. Examples:

- `SEED-Scioto_Marsh_Complex`
- `SEED-AEP_Transmission_Corridor_â€"_Ada_Segment` *(also has a UTF-8 encoding artifact)*
- `SEED-Blanchard_River_Corridor`

### Issue 10: OH-WOD-SEED pseudo-type in held_entities (4 records)
Four Wood County held entities use `SEED` as the type code:  
OH-WOD-SEED-001 through OH-WOD-SEED-004.

---

## LOW — Format Inconsistency Across County Runs

### Issue 11: 3-digit vs. 4-digit split for single-county entities

The CLAUDE.md standard example shows 3-digit for single-county (`OH-OTT-S-001`)
and 4-digit for multi-county (`OH-MC-TT-0001`). However, two early runs used
4-digit for single-county entities:

| County | Format | Entity tables affected |
|---|---|---|
| Wayne (WA) | 4-digit | sites, trails, access_points |
| Franklin (FR) | 4-digit | sites, trails, trail_segments, trail_networks, site_networks, access_points |
| Scioto (SC) | 4-digit | sites, trails, access_points, site_networks |

All other county runs used the standard 3-digit format. This is a cosmetic
inconsistency — no collision is possible within a single county's namespace —
but it creates visual inconsistency in the ID space.

### Issue 12: Cross-county spill records with high sequence numbers (5 records)
Five records from adjacent counties were upserted during the Franklin County run
with Franklin-era sequential IDs (not starting at 001). These are legitimate
entities in their correct county namespace, just with high numbers that suggest
they were numbered mid-Franklin run:

| ID | Name | County |
|---|---|---|
| OH-DEL-S-0456 | Hoover Meadows Nature Preserve | Delaware |
| OH-DEL-S-1041 | O'Shaughnessy Reservoir | Delaware |
| OH-FAI-S-0392 | Turnberry Golf Course | Fairfield |
| OH-PKW-S-0043 | Scioto Bend Preserve | Pickaway |
| OH-UNI-S-0547 | Red Stone Loop Open Space | Union |

These will create a discontinuous sequence when those counties are run properly,
but per IMP-117 sequence gaps are expected and this is not a data error.

---

## Issue Count by Table

| Table | Records | Issues touching this table |
|---|---|---|
| sites | 2,452 | #2, #4, #5, #6, #11, #12 |
| trails | 352 | #1, #3, #7, #11 |
| trail_segments | 9 | none |
| trail_networks | 6 | none |
| trailthings | 5 | none |
| site_networks | 21 | none |
| access_points | 204 | #2 (missing), #8, #11 |
| held_entities | 58 | #9, #10 |

---

## Recommended Remediation Sequence

Listed in priority order (not prescriptive — to be reviewed before any action):

1. **Fix Issue 1 (MC-T collision)** — rebase all 3-digit MC-T records to a
   non-colliding range; update all foreign key references in relationship tables.
2. **Fix Issue 2 (OTT-AP-006 wrong table)** — move to access_points; delete from sites.
3. **Fix Issues 3–8 (wrong type codes)** — rename IDs; update relationship tables.
4. **Fix Issues 9–10 (non-standard held IDs)** — assign proper OH-HAR-S-xxx /
   OH-WOD-S-xxx IDs; re-check whether any can be released from held status.
5. **Issue 11 (3-digit vs 4-digit)** — decision needed: normalize everything to
   3-digit (standard) or accept the inconsistency since no collision is possible.
6. **Issue 12 (spill records)** — no action required; document for Delaware,
   Fairfield, Pickaway, Union county runs.

---

*Audit generated by Claude, 2026-06-08. Source: natural_areas_v6.db.*
