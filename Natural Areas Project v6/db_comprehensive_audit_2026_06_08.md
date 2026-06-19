# Natural Areas DB — Comprehensive Audit Report
**Date:** 2026-06-08 (post-remediation run)  
**Database:** NASqlite/natural_areas_v6.db  
**Scope:** Full data quality audit — ID formats, FK integrity, held entities, duplicates, GPS quality, schema gaps  

---

## Summary

The prior remediation script (`db_remediation_2026_06_08.py`) successfully resolved all 12 issues
documented in `db_id_audit_2026_06_08.md`. This fresh audit finds **16 distinct issues** across
six categories. No issues are identical to the prior audit's findings.

Severity tiers:
- **HIGH** — data integrity problem requiring action before next pipeline run
- **MEDIUM** — correctness or quality issue; fix when county is revisited
- **LOW** — informational; no blocking consequence

---

## Category A: ID Format — Remaining Gaps

### A-1 (HIGH): trail_segments — 3 records still have 3-digit IDs

The prior remediation did not cover `trail_segments`. Three multi-county segment IDs remain
non-canonical:

| ID | Name | Counties |
|---|---|---|
| OH-MC-TS-002 | Independence Leg | Defiance;Henry |
| OH-MC-TS-005 | Wabash Cannonball Trail - South Fork | Henry;Lucas |
| OH-MC-TS-006 | WideWater Section | Henry;Wood |

Should be OH-MC-TS-0002, OH-MC-TS-0005, OH-MC-TS-0006. No `trail_to_segment` entries exist
for these three records (see A-3), so the FK cascade is simpler — rename in `trail_segments` only.

### A-2 (MEDIUM): held_entities — OH-WIL-TR-0001 uses legacy TR type code

The held Williams County North Country NST record uses `TR` (v5 legacy) instead of `T`.
It should be OH-WIL-T-0001. This was missed by the prior remediation because the remediation
script's Phase 7 (held TR→T rename) looked for `OH-WIL-TR-*` in the trails table, but this
entity is in held_entities, not trails.

No FK tables reference this held ID, so the fix is a single UPDATE to held_entities.record_id.

---

## Category B: Referential Integrity

### B-1 (HIGH): site_network_members — OH-FR-S-1040 referenced but missing

`OH-FR-SN-0003` (Columbus Recreation and Parks network) has a membership row for `OH-FR-S-1040`,
but that site does not exist in the `sites` table or in `held_entities`. It is a true orphan FK.

The Franklin run_metadata shows `records_input=1174, normalized=1174, held=0`. The max Franklin
site sequence in the DB is OH-FR-S-1181, so FR-S-1040 should exist. It was likely deleted or
never upserted. The site_network_members row should be removed until the entity is recovered
or the Franklin data is re-examined.

**Recommended action:** DELETE the orphan row from site_network_members. Log in improvement
tracker as a Franklin County data gap — OH-FR-S-1040 may need recovery from the Franklin
discovery YAML.

### B-2 (HIGH): access_point_parents — 4 APs reference held entities but are not themselves held

Four Wayne County access points are in the live `access_points` table with parents that are
in `held_entities`:

| AP ID | AP Name | Parent ID | Parent Status |
|---|---|---|---|
| OH-WA-AP-0003 | Killbuck Marsh — Carrie Lane Parking Area | OH-WA-S-0045 | cross_county_held |
| OH-WA-AP-0004 | Killbuck Marsh — Wright Marsh Parking Area | OH-WA-S-0045 | cross_county_held |
| OH-WA-AP-0013 | Sippo Valley Trail — Dalton Trailhead | OH-WA-T-0014 | cross_county_held |
| OH-WA-AP-0015 | Holmes County Trail — Fredericksburg Trailhead | OH-WA-T-0015 | cross_county_held |

Per protocol, these APs should be in `held_entities` with `hold_reason = parent_held`. The Wayne
County upsert script's normalization did not cascade the hold to child APs when their parents
were held. This is a pipeline bug in the Wayne County run.

**Recommended action:** Move these 4 APs from `access_points` to `held_entities` with
`hold_reason = parent_held`. Remove their `access_point_parents` rows.

### B-3 (MEDIUM): trail_to_segment — 3 MC-TS segments have no parent trail registered

OH-MC-TS-002, OH-MC-TS-005, OH-MC-TS-006 (the 3-digit segments from A-1) have no entries
in `trail_to_segment`. Their parent trails are identifiable by name:

| Segment | Likely parent |
|---|---|
| Independence Leg (DEF;HEN) | OH-MC-T-0221 (Wabash Cannonball Trail, North Fork) |
| Wabash Cannonball Trail - South Fork (HEN;LUC) | OH-MC-T-0002 (Wabash Cannonball Trail) |
| WideWater Section (HEN;WOD) | Unknown — verify against Henry County records |

**Recommended action:** After renaming segments to 4-digit (A-1), add the appropriate
`trail_to_segment` rows. Verify WideWater Section parent trail against Henry County
discovery YAML.

---

## Category C: Held Entity Release Candidates

### C-1 (HIGH): 4 Sandusky held entities — Ottawa County has now been run

These Sandusky County held records were held with `hold_reason = cross_county_held,
county_primary = Ottawa`. Ottawa County was run on 2026-05-18. All four entities
already exist as primary Ottawa County records:

| Held ID | Name | Ottawa primary |
|---|---|---|
| OH-SAN-S-0079 | Walter Ory Park | OH-OTT-S-0084 |
| OH-SAN-S-0080 | Well Park | OH-OTT-S-0088 |
| OH-SAN-S-0081 | Witty Park | OH-OTT-S-0089 |
| OH-SAN-S-0107 | Schedel Arboretum and Gardens | OH-OTT-S-0109 |

**Recommended action:** Delete these 4 rows from `held_entities`. Verify that the
Sandusky discovery YAML captures these as cross-county references to their Ottawa primaries
(add `KNOWN_MC` notes if applicable). Check whether Sandusky's `site_parent` or
`site_network_members` rows need updating to point to the OTT IDs.

### C-2 (MEDIUM): OH-SAN-S-0105 (Sugar Creek Golf Course) — Ottawa not found

This entity was held with `county_primary = Ottawa`, but no matching record appears in the
Ottawa County run. It may have been omitted from the Ottawa discovery, may be primarily in
Sandusky County despite the cross-county hold, or may have been captured under a different
name.

**Recommended action:** Investigate during Ottawa or Sandusky County review. If it is
Sandusky-primary, release from held and upsert as a Sandusky site.

---

## Category D: Duplicate Entity Names

### D-1 (HIGH): Ottawa Wildlife Refuge — 2 Lucas records, identical GPS

OH-LUC-S-0229 and OH-LUC-S-0230 are both "Ottawa Wildlife Refuge", same governance
(Howard Farms Conservancy District), same GPS (41.652664, -83.242914), but different
addresses (12581 vs 12291 Lagoon Dr) and slightly different acreage (1.0 vs 1.1 acres).
Both are subtype "Wetland Management Area".

The identical GPS on physically distinct addresses indicates a centroid fallback (both
resolved to the same point). These could be two adjacent 1-acre parcels of the same refuge
managed as distinct units, OR a true duplicate.

**Recommended action:** Verify during Lucas County quality review. If they are distinct
parcels, acquire individual GPS. If they are duplicates, merge to single record.

### D-2 (MEDIUM): Muffin Township Cemetery — 2 Franklin records

OH-FR-S-1114 and OH-FR-S-1115 are both "Muffin Township" Cemetery, City of Gahanna.
Acreage differs substantially (0.73 vs 8.45 acres) and GPS differs slightly (~100m).
This pattern is consistent with two separately platted cemetery parcels at the same
named cemetery. Likely legitimate — verify during Franklin quality review.

### D-3 (LOW): Greenspace (Ottawa Hills, Lucas) — 4 records, all same GPS

OH-LUC-S-0219 through OH-LUC-S-0222 are distinct parcels of Ottawa Hills village
greenspace at four different addresses. All carry the same GPS centroid (41.663846,
-83.633009), indicating a municipality-centroid GPS fallback. The entities themselves
appear legitimate (distinct parcels), but individual GPS coordinates are needed.

**Recommended action:** Flag for individual GPS acquisition during Lucas County review.

---

## Category E: GPS Quality Issues

### E-1 (HIGH): Paulding County — 7 sites sharing one centroid

Seven Paulding sites share GPS (41.137, -84.573) despite having different addresses
across the Village of Paulding:

- OH-PAU-S-0006 — Flat Rock Trail Park (12600 Rd. 119)
- OH-PAU-S-0010 — Black Swamp Nature Center (753 Fairground Dr)
- OH-PAU-S-0012 — Lela McGuire-Jeffery Park (Village of Paulding)
- OH-PAU-S-0013 — Herb Monroe Community Park (122 E. Jackson St.)
- OH-PAU-S-0014 — Paulding Water Park (Village of Paulding)
- OH-PAU-S-0015 — Paulding Skate Park (Village of Paulding)
- OH-PAU-S-0016 — Reservoir Park (901 McDonald Pike)

The shared coordinate is the Paulding county/village centroid. These all need individual
GPS acquisition.

**Recommended action:** Run targeted GPS re-acquisition for these 7 records during the
next Paulding County quality review. Per IMP-031 (GPS fill-forward), do not overwrite
any that already have high-confidence GPS.

### E-2 (MEDIUM): 47 sites in the sites table have no GPS

All 47 are from Hardin County (45) and two multi-county entities (OH-MC-S-0028,
OH-MC-S-0032). The Hardin run_metadata notes "34 cemeteries gps_unresolvable pending
GNIS acquisition." 

These entities appear to have been upserted to the sites table without GPS rather than
being routed through held_entities. This bypasses the Stage 4c GPS Gate. Two possible
explanations:
1. The Hardin pipeline ran with `gps_unresolvable = true` set inline, allowing direct
   upsert to sites — intended behavior.
2. The GPS Gate was bypassed — a protocol deviation.

**Recommended action:** Review Hardin County pipeline config and upsert script to confirm
whether gps_unresolvable was properly set for each record. If not, these should be moved
to held_entities. Also: run GNIS GPS acquisition for the cemetery subset.

---

## Category F: Data Quality

### F-1 (MEDIUM): UTF-8 encoding artifact in held_entities name

OH-HAR-S-0112 has `â€"` in its name where `—` (em dash) should appear:
`AEP Transmission Corridor â€" Ada Segment`

This is a UTF-8 double-encoding artifact. The `hold_detail` field for the same record
contains the same artifact. The same artifact was noted in the original audit for the
SEED-prefixed Hardin records (Issue #9 in db_id_audit_2026_06_08.md) — those were
never fixed because the prior remediation focused on ID formats.

**Recommended action:** Direct UPDATE to held_entities for this row's `name` and
`hold_detail` fields. Also check whether the Hardin discovery YAML has the same artifact
at source.

### F-2 (LOW): identity_notes column absent from sites table

The entity schema and CLAUDE.md raw record template include `identity_notes_raw` as a
discovery field, and the normalization contract maps it to `identity_notes` in the
normalized output. However, the `sites` table has no `identity_notes` column. The field
may have been dropped or renamed during schema evolution.

All other entity tables (trails, access_points) should be checked for the same gap.
This should be tracked as an improvement item.

---

## Issue Count Summary

| Category | Count | Severity breakdown |
|---|---|---|
| A — ID format gaps | 2 | 1 HIGH, 1 MEDIUM |
| B — Referential integrity | 3 | 2 HIGH, 1 MEDIUM |
| C — Held release candidates | 2 | 1 HIGH, 1 MEDIUM |
| D — Duplicate names | 3 | 1 HIGH, 2 MEDIUM/LOW |
| E — GPS quality | 2 | 1 HIGH, 1 MEDIUM |
| F — Data quality | 2 | 1 MEDIUM, 1 LOW |
| **Total** | **16** | **6 HIGH, 7 MEDIUM, 3 LOW** |

---

## Recommended Action Sequence

Listed by priority for the next work session:

1. **A-1 + A-2** — Rename 3 trail_segment IDs to 4-digit; rename WIL-TR-0001 in held.
   Simple UPDATEs; do before any FK work.
2. **B-1** — Delete the orphan site_network_members row for OH-FR-S-1040. Flag Franklin
   data gap in improvement tracker.
3. **B-2** — Move 4 Wayne APs from access_points to held_entities (parent_held). Remove
   their access_point_parents rows.
4. **B-3** — After A-1, add trail_to_segment rows for the 3 renamed segments.
5. **C-1** — Delete 4 resolved Sandusky cross_county_held records (Ottawa now run).
6. **E-1** — Queue Paulding GPS re-acquisition (7 sites at county centroid).
7. **D-1** — Verify Ottawa Wildlife Refuge duplicate during Lucas review; merge or GPS-fix.
8. **E-2 / F-2** — Investigate Hardin GPS gate bypass; add improvement tracker items.
9. **F-1** — Fix UTF-8 artifact in OH-HAR-S-0112.
10. **C-2 / D-2 / D-3** — Investigate during respective county quality reviews.

---

## Prior Audit Confirmation

All 12 issues documented in `db_id_audit_2026_06_08.md` have been resolved. The
remediation script ran successfully. The only residual ID-format gap is trail_segments
(A-1 above), which was outside the script's scope, and the WIL-TR-0001 held record
(A-2 above), which was missed due to phase ordering.

---

*Audit generated by Claude, 2026-06-08. Source: natural_areas_v6.db.*
