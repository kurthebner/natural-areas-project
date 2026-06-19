# NATURAL AREAS PROJECT
# DATABASE MIGRATION LOG
Historical record of structural migrations applied to natural_areas_v5.db.

This file is a **historical record only** — not a rules or protocol document.
It documents what happened to the live database during specific migration events.
For current cross-county resolution rules, see:
`processing/na_cross_county_resolution_v6.x.md`

------------------------------------------------------------
# IMP-104 — MC ID SCHEME INAUGURAL MIGRATION (2026-05-07)

## Purpose
Two confirmed collision cases existed in the live DB where the same physical
entity had been independently discovered and recorded by multiple county runs
under different county-prefixed IDs. IMP-104 established the MC (multi-county)
ID scheme and resolved both collisions.

## Migration 1: Maumee River Water Trail → OH-MC-T-0001

Source records (all confirmed duplicates of the same water trail):

| Old ID      | County   | counties field                         |
|-------------|----------|----------------------------------------|
| DEF-T-002   | Defiance | Defiance; Henry; Lucas; Paulding; Wood |
| LUC-T-013   | Lucas    | Defiance;Henry;Lucas;Wood              |
| PAU-TR-002  | Paulding | Paulding; Defiance; Henry; Wood; Lucas |
| WOD-TR-003  | Wood     | Defiance; Henry; Lucas; Williams; Wood |

**Canonical ID**: OH-MC-T-0001 (renamed from MC-T-0001 by IMP-107)
**Name**: Maumee River Water Trail
**Canonical counties**: Defiance; Henry; Lucas; Paulding; Williams; Wood

IMP-107 action: All four source records deleted (Category 2 — confirmed true
duplicates with no unique data). Access points parented to these records were
reparented to OH-MC-T-0001.

---

## Migration 2: Wabash Cannonball Trail → OH-MC-T-0002

Source records (all confirmed duplicates):

| Old ID     | County   | counties field              |
|------------|----------|-----------------------------|
| HEN_T_006  | Henry    | Fulton;Henry;Lucas;Williams |
| LUC-T-010  | Lucas    | Fulton;Henry;Lucas;Williams |
| WIL-TR-003 | Williams | Williams; Fulton; Henry; Lucas |

**Canonical ID**: OH-MC-T-0002 (renamed from MC-T-0002 by IMP-107)
**Name**: Wabash Cannonball Trail
**Canonical counties**: Fulton; Henry; Lucas; Williams

IMP-107 action: All three source records deleted (Category 2). Access points
reparented to OH-MC-T-0002.

**Note on OH-MC-TR-007**: "Wabash Cannonball Trail (North Fork)" — a name variant
suggesting a distinct fork or segment, not the canonical main trail. Retained as
OH-MC-TR-007 (multi-county Fulton;Henry;Lucas;Williams). Held pending evaluation
at Fulton County pipeline run: if confirmed as a segment, set
`parent_trailthing_id = OH-MC-T-0002` and reclassify. If confirmed as a distinct
named trail, retains OH-MC-TR-007.

---

## Category 2 Deletion Rule (IMP-104/IMP-107)

The standard IMP-104 procedure called for deprecating duplicate records (updating
`notes` field with `DEPRECATED: superseded by {OH-MC-ID}`; do not delete).
IMP-107 introduced a deletion exception:

**Category 2 — Confirmed true duplicates**: A duplicate record is Category 2
when it represents the exact same physical entity as the canonical record AND
contains no unique data not already present in the canonical record (no unique
APs, no distinct description, no unique GPS or acreage).

Category 2 duplicates were DELETED from entity tables and all FK tables.
This exception does NOT apply to records carrying any unique field values —
those must be deprecated, not deleted.

------------------------------------------------------------
# IMP-107 — GLOBAL ID FORMAT MIGRATION (2026-05-12)

## Purpose
All entity IDs migrated from `{COUNTY}-{TYPE}-{SEQ}` to `OH-{COUNTY}-{TYPE}-{SEQ}`.
Multi-county entities (any entity whose `counties` field contained more than one
value) were simultaneously migrated to `OH-MC-{TYPE}-{SEQ}`.

**Scope**: 2,245 entity IDs renamed across all entity tables, relationship tables,
provenance tables, and 34 TSV files across 12 county directories.

## Category 1 Collision Renumbers

Four entities had sequence collisions when projected into the OH-MC namespace.
The lower-priority entity was renumbered to the next available sequence:

| Old ID    | Name                              | Collision With | New ID       |
|-----------|-----------------------------------|----------------|--------------|
| SC-S-0004 | Shawnee State Forest              | FR-S-0004      | OH-MC-S-0002 |
| SC-S-0012 | Scioto Brush Creek State Scenic R | FR-S-0012      | OH-MC-S-0003 |
| FR-T-0002 | Camp Chase Trail                  | MC-T-0002      | OH-MC-T-0003 |
| SC-T-0001 | Shawnee Backpack Trail            | MC-T-0001      | OH-MC-T-0006 |

Priority rule applied: existing canonical OH-MC records > Franklin (FR) > Scioto (SC) > others.

## Non-Migration Entities (Multi-County, Single Record)

The following entities listed multiple counties and had a single canonical record.
They received OH-MC-* IDs during IMP-107 (multi-county determination made by
`counties` field having >1 value):

| Current ID    | Name                             | Counties                                | Notes |
|---------------|----------------------------------|-----------------------------------------|-------|
| OH-MC-TN-0003 | Central Ohio Blueways            | Delaware;Franklin;Pickaway              | Franklin discovery |
| OH-PAU-TN-001 | North Country NST (network)      | Multi-state                             | Paulding discovery; retained PAU prefix — single-record multi-state entity |
| OH-MC-TN-0001 | Shawnee Bridle Trail Network     | Scioto;Adams                            | Scioto discovery |
| OH-MC-SN-0001 | Metro Parks Serving Franklin Co. | Delaware;Fairfield;Franklin;Pickaway    | Franklin discovery |
| OH-MC-T-001   | North Country NST (trail)        | Defiance;Henry;Lucas;Paulding;Putnam    | Defiance discovery; 3-digit seq inherited; OH-WIL-TR-001 held — Scenario A pending Williams run |
| OH-MC-T-0003  | Camp Chase Trail                 | Franklin;Madison                        | IMP-107 renumber from FR-T-0002 |
| OH-MC-T-0004  | Heritage Trail                   | Franklin;Madison                        | Franklin primary |
| OH-MC-T-0108  | Olentangy Trail                  | Delaware;Franklin                       | Franklin primary |
| OH-MC-T-0006  | Shawnee Backpack Trail           | Adams;Scioto                            | IMP-107 renumber from SC-T-0001 |
| OH-MC-T-0012  | Killbuck Marsh Wildlife Obs. Tr. | Wayne;Holmes                            | Wayne primary; Scenario A pending Holmes run |
| OH-MC-TR-001  | Miami and Erie Canal Towpath     | many counties                           | Paulding discovery; Scenario A |
| OH-MC-TR-003  | Buckeye Trail — Delphos Section  | Paulding;Putnam;Allen;Auglaize          | Paulding discovery; Scenario A |
| OH-MC-TR-004  | Buckeye Trail — Defiance Section | Paulding;Defiance;Williams              | Paulding discovery; Scenario A |

Note: OH-PAU-TN-001 retains a county-prefixed OH-PAU prefix despite being
multi-state/multi-county. It is a single-record entity with a clear single-discovery
anchor. The MC prefix is not applied unless a collision or no-primary-county
condition is met.

## Other IMP-107 Actions
- 15 held_entities records renamed to OH- format
- 8 orphan trail_parents rows deleted
- "Lucas, Ohio" → "Lucas" corrected in 7 sites.counties values
- 7 Category 2 duplicate trails deleted; APs reparented to canonical OH-MC records

------------------------------------------------------------
# HELD ENTITY SNAPSHOT — POST IMP-104/IMP-107 (2026-05-12)

**Note**: This snapshot was accurate as of 2026-05-12. The `held_entities` DB table
is the authoritative current source. Run the bootstrap pre-discovery query
(na_cross_county_resolution.md §5) for current state.

| held_id | record_id         | Name (truncated)                         | Hold Reason                        |
|---------|-------------------|------------------------------------------|------------------------------------|
| 1       | OH-WA-S-0045      | Killbuck Marsh Wildlife Area             | multi_county                       |
| 3       | OH-WA-S-0046      | Funk Bottoms Wildlife Area               | multi_county                       |
| 4       | OH-WA-T-0013      | Chippewa Township Nature Preserve trails | identity_uncertain                 |
| 5       | OH-WA-T-0014      | Sippo Valley Trail                       | multi_county (Scenario A, Holmes)  |
| 6       | OH-WA-T-0015      | Holmes County Trail                      | multi_county (Scenario A, Holmes)  |
| 15      | OH-PAU-S-001      | Lake Wayne R. Carr Wildlife Area         | gps_missing                        |
| 16      | OH-PAU-S-009      | Guilda H. Culler Memorial Park           | gps_missing                        |
| 17      | OH-PAU-S-021      | Flat Rock Creek Nature Preserve          | gps_missing                        |
| 18      | OH-PAU-AP-005     | Viall's Lock Campsite                    | gps_missing                        |
| 19      | OH-WIL-TR-001     | North Country NST                        | multi_state_federal (Scenario A)   |
| 21      | OH-MC-SI-003      | Maumee State Forest                      | cross_county_or_access_unconfirmed |
| 22      | OH-MC-SI-006      | Oak Openings Corridor (MT)               | cross_county_or_access_unconfirmed |
| 23      | OH-MC-TR-005      | Stewardship Trail                        | cross_county_or_access_unconfirmed |
| 24      | OH-MC-TR-007      | Wabash Cannonball Trail (North Fork)     | cross_county_or_access_unconfirmed |
| 29–35   | OH-WOD-SI-*/SEED-*| Various Wood County entities             | verification_required / unconfirmed_baseline_seed |
| 36–40   | OH-HEN-S-*        | Henry County wildlife areas              | gps_missing                        |

------------------------------------------------------------
# END OF DATABASE MIGRATION LOG
