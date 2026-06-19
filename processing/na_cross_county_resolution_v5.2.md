# CROSS-COUNTY RESOLUTION PROTOCOL v5.2
# NATURAL AREAS PROJECT
# IMP-104 — 2026-05-07 | IMP-107 — 2026-05-12

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2 (IMP-107)

IMP-107 migrated all entity IDs in the live DB from the old
`{COUNTY}-{TYPE}-{SEQ}` format to a new `OH-{COUNTY}-{TYPE}-{SEQ}`
format. Key effects on this module:

- §3.1: ID format updated. The state prefix `OH-` is now mandatory for
  all Ohio entities. Multi-county entities use `OH-MC-{TYPE}-{SEQ}`.
  Single-county entities use `OH-{ABBREV}-{TYPE}-{SEQ}`.
- §3.2: Example IDs updated throughout.
- §3.3: SQL LIKE patterns updated to `'OH-MC-T-%'` etc.
- §5.1: Bootstrap query patterns updated.
- §7.2: Assignment algorithm updated.
- §8.3: Migration records updated with current canonical IDs.
  Category 2 duplicate records (confirmed true duplicates with no
  unique data) were DELETED rather than deprecated — see §8.5.
- §8.4: Held entity table updated with current record IDs.
- Non-Migration Entities table updated with current IDs.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1 (IMP-104)

This was the inaugural version. IMP-104 established:
- MC ID scheme for multi-county entities
- Three cross-county scenarios with formal handling procedures
- Bootstrap pre-discovery DB check requirement
- Discovery-time CROSS_COUNTY_CANDIDATE flagging
- Resolution Engine extension for MC ID assignment
- Migration procedure and records for existing collision entities

------------------------------------------------------------
# 1. PURPOSE

This module governs how entities that span multiple Ohio counties are
identified, recorded, and resolved across county discovery runs. It
establishes the MC (multi-county) ID scheme, defines when MC IDs apply,
and specifies the procedures that discovery, the Resolution Engine, and
the bootstrap process must follow.

The core problem this module solves: as the Natural Areas Project builds
up county by county, the same physical entity (a trail, a network, a
site) will be encountered independently by multiple county runs. Without
a formal protocol, the same entity accumulates duplicate county-prefixed
records that cannot be automatically resolved and that obscure the true
entity count.

MC IDs solve this by giving genuinely multi-county entities a canonical
identifier that is not anchored to any single county, making duplicate
detection trivial and enabling clean cross-county searches.

------------------------------------------------------------
# 2. SCOPE: WHEN MC IDs APPLY

## 2.1 MC ID Required

An entity must receive an MC ID when either of the following conditions
is true:

**Condition A — Collision**: The entity has been independently discovered
and recorded under different county-prefixed IDs by two or more county
runs. The entity is literally present in the DB multiple times with
different IDs. This condition requires immediate resolution; it cannot
be deferred.

**Condition B — No Primary County**: The entity spans multiple counties
with no clear single-county managing authority. For example, an ODNR or
federal land unit with no county-specific governance anchor where
assigning any county prefix would be arbitrary.

## 2.2 MC ID Not Required (County-Prefixed ID Retained)

An entity retains its county-prefixed ID when:

- It was discovered by one county and extends into a neighboring county,
  but the primary managing entity is clearly county-based (e.g., a Metro
  Parks trail system that has one trail crossing a county line).
- It is a held entity pending a partner county run (Scenario A below).
  The county-prefixed ID is kept as a provisional anchor; MC ID is
  assigned when the partner county runs and Collision or Known conditions
  are confirmed.

## 2.3 Determining the Primary County

If Condition B is the trigger, the primary county is determined by the
managing entity's primary operating county. If the managing entity is
state or federal (ODNR, USFS, NPS), the county where the largest portion
of the entity is physically located is the tiebreaker, using the first
listed county in the `counties` field as the canonical county if no
other authority exists.

------------------------------------------------------------
# 3. ENTITY ID FORMAT

## 3.1 Format

All Ohio entity IDs follow this universal format:

  OH-{COUNTY}-{TYPE}-{SEQ}

- `OH-` prefix: fixed state prefix, mandatory for all Ohio entities.
- `{COUNTY}`: county abbreviation (e.g., `FR` for Franklin, `LUC` for
  Lucas), OR `MC` for entities that span multiple counties with no
  single-county governance anchor (see §2.1 for when MC applies).
- `{TYPE}`: entity type code (see §3.2).
- `{SEQ}`: sequence number, zero-padded, assigned per county+type
  namespace in order of discovery or migration.

Examples (multi-county entities):
  OH-MC-T-0001    (Maumee River Water Trail)
  OH-MC-TN-0001   (Shawnee Bridle Trail Network)
  OH-MC-S-0001    (first multi-county Site)

Examples (single-county entities):
  OH-FR-S-0001    (Franklin County site)
  OH-LUC-T-001    (Lucas County trail)
  OH-WA-AP-0001   (Wayne County access point)

## 3.2 Entity Type Codes

| Entity Type    | Code | MC Example ID    | County Example ID |
|----------------|------|------------------|-------------------|
| Trail          | T    | OH-MC-T-0001     | OH-FR-T-0001      |
| Trail Segment  | TS   | OH-MC-TS-0001    | OH-FR-TS-0001     |
| Trail Network  | TN   | OH-MC-TN-0001    | OH-FR-TN-0001     |
| Site           | S    | OH-MC-S-0001     | OH-FR-S-0001      |
| Site Network   | SN   | OH-MC-SN-0001    | OH-FR-SN-0001     |
| Access Point   | AP   | OH-MC-AP-0001    | OH-FR-AP-0001     |

Note: Some counties (Fulton, Wood, Paulding, Williams) use `TR` instead
of `T` for trails and `SI` instead of `S` for sites due to historical
county-run conventions. These type codes are preserved in their entity
IDs (e.g., OH-FUL-TR-001, OH-WOD-SI-001).

Trail Segments inherit the MC prefix from their parent Trail when the
parent receives an MC ID. A Trail Segment that itself spans counties
but whose parent trail does not may receive its own MC-TS ID.

Access Points rarely span county lines as physical access points are
discrete locations; MC-AP is reserved for unusual cases.

## 3.3 Sequence Management

Sequences are managed per `(COUNTY, TYPE)` namespace. For OH-MC-*
entities the namespace is `(MC, TYPE)`. The next available sequence
number is MAX(existing IDs in that namespace) + 1. Sequence numbers
are never reused, even if a record is deleted or deprecated.

To query next available sequences for OH-MC-* entities:

```sql
SELECT
  MAX(CAST(REPLACE(trail_id, 'OH-MC-T-', '') AS INTEGER)) AS next_T
FROM trails WHERE trail_id LIKE 'OH-MC-T-%';

SELECT
  MAX(CAST(REPLACE(network_id, 'OH-MC-TN-', '') AS INTEGER)) AS next_TN
FROM trail_networks WHERE network_id LIKE 'OH-MC-TN-%';

SELECT
  MAX(CAST(REPLACE(network_id, 'OH-MC-SN-', '') AS INTEGER)) AS next_SN
FROM site_networks WHERE network_id LIKE 'OH-MC-SN-%';

SELECT
  MAX(CAST(REPLACE(site_id, 'OH-MC-S-', '') AS INTEGER)) AS next_S
FROM sites WHERE site_id LIKE 'OH-MC-S-%';
```

Note: Some legacy MC entities use 3-digit sequences inherited from their
source county runs (e.g., OH-MC-T-001 from DEF-T-001 via 3-digit
padding). When assigning new OH-MC-* sequences, always use 4-digit
zero-padded format (e.g., 0003, 0004) to distinguish new assignments
from legacy 3-digit inherited sequences.

------------------------------------------------------------
# 4. THREE CROSS-COUNTY SCENARIOS

## 4.1 Scenario A — Held (Partner County Not Yet Run)

**Situation**: County A discovers an entity that clearly extends into
County B, but County B has not yet been run. County A cannot confirm
the entity's full extent or governance without County B's data.

**Discovery-time action (County A)**:
1. Create a provisional record with a County A-prefixed ID (e.g.,
   `OH-WA-T-0014`).
2. Add `CROSS_COUNTY_CANDIDATE` to `identity_notes_raw`.
3. Add `hold_reason: multi_county` to the held_entities table with a
   note naming the partner county/counties.
4. Note the partner counties in the `counties` field.

**Pipeline action**: The Resolution Engine sees the hold flag and defers
MC ID assignment. The county-prefixed ID is used as a provisional anchor.

**When County B runs**: County B's bootstrap check (§5) finds the held
entity in the DB. County B's discovery must reference the existing
provisional record. When County B's pipeline runs, the Resolution Engine
executes the Scenario B (Collision) or Scenario C (Known) procedure,
whichever applies, and assigns an MC ID if warranted.

**Key rule**: Held multi-county entities are never upserted with their
provisional county-prefixed ID as permanent. They must pass through MC
resolution before final DB write.

## 4.2 Scenario B — Collision (Multiple Independent Discoveries)

**Situation**: County A and County B have each independently discovered
and recorded the same entity under different county-prefixed IDs. The
entity appears in the DB (or in County B's current run's raw records)
as two distinct records.

**Detection**: The Resolution Engine detects collision when, during
Phase 1 Grouping or Phase 2 Identity Matching, two records from
different county runs produce a high-confidence identity match (anchor
match + similarity score above the merge threshold) AND both records
have multi-county `counties` fields that overlap.

A collision may also be flagged manually during discovery when a
discoverer finds an entity already in the DB under a different county's
ID.

**Resolution Engine action**:
1. Assign an MC ID (§7.2) to the canonical merged record.
2. Select field values from the canonical record (§7.3).
3. Write the merged record to the DB with the MC ID.
4. Deprecate all county-prefixed records by updating their `notes` field
   with `DEPRECATED: superseded by {MC-ID}` and recording in
   `resolution_provenance`.
5. Update all relationship tables (`trail_network_members`,
   `trail_to_segment`, `access_point_parents`, etc.) to reference the
   MC ID.
6. Remove the held_entities entries for all deprecated records.
7. Log the full merge in `resolution_provenance`.

**Manual collision flag**: If a discoverer finds a collision before the
pipeline runs, they add `COLLISION:{existing-id}` to `identity_notes_raw`
alongside `CROSS_COUNTY_CANDIDATE`. The Resolution Engine uses this as
a strong match hint.

## 4.3 Scenario C — Known (MC ID Already in DB)

**Situation**: An entity already exists in the DB with an MC ID (either
from a prior migration or from a prior county run's Scenario B
resolution). County B encounters the same entity during discovery.

**Discovery-time action (County B)**:
1. The bootstrap pre-check (§5) must have already surfaced the MC entity.
2. During discovery, if the discoverer encounters the entity, they note
   the existing MC ID in `identity_notes_raw`: `KNOWN_MC:{oh-mc-id}`
   (e.g., `KNOWN_MC:OH-MC-T-0001`).
3. Do NOT create a new county-prefixed record for this entity.
4. If County B has new data (additional APs, corrected length, updated
   URL), flag it as `MC_SUPPLEMENTAL:{oh-mc-id}` and record the updated
   fields in the raw discovery file for the pipeline to merge.

**Pipeline action**: The Resolution Engine sees `KNOWN_MC:{oh-mc-id}`,
skips ID assignment, and applies any supplemental field updates to the
existing MC record using the field authority rules in §7.3.

------------------------------------------------------------
# 5. BOOTSTRAP PRE-DISCOVERY CHECK

Before any discovery work begins for a new county, the bootstrap step
must query the live DB for existing MC entities that are known to include
or likely include the target county.

## 5.1 Procedure

Execute the following queries at bootstrap time (substitute the target
county name for `{COUNTY}`):

```sql
-- MC trails that list the target county
SELECT trail_id, name, counties FROM trails
WHERE trail_id LIKE 'OH-MC-T-%'
AND counties LIKE '%{COUNTY}%';

-- MC trail networks
SELECT network_id, name, counties FROM trail_networks
WHERE network_id LIKE 'OH-MC-TN-%'
AND counties LIKE '%{COUNTY}%';

-- MC site networks
SELECT network_id, name, counties FROM site_networks
WHERE network_id LIKE 'OH-MC-SN-%'
AND counties LIKE '%{COUNTY}%';

-- MC sites
SELECT site_id, name, counties FROM sites
WHERE site_id LIKE 'OH-MC-S-%'
AND counties LIKE '%{COUNTY}%';

-- Held entities from OTHER counties that name the target county
SELECT h.record_id, h.name, h.county, h.hold_detail
FROM held_entities h
WHERE h.hold_detail LIKE '%{COUNTY}%'
AND h.county != '{COUNTY}';
```

## 5.2 Output

The bootstrap step must produce a "Known Multi-County Entities" section
in the county's baseline document listing:
- All MC entities found by the queries above (ID, name, counties, type)
- All held entities from other counties that name the target county

This section is an explicit discovery input. During discovery, if any
entity on this list is encountered, the discoverer applies Scenario C
(§4.3). The entity must not be re-created with a county-prefixed ID.

## 5.3 Empty Result

If the bootstrap queries return no results, note "No existing MC entities
found for {COUNTY}" in the baseline document and proceed normally.

------------------------------------------------------------
# 6. DISCOVERY-TIME FLAGGING

## 6.1 CROSS_COUNTY_CANDIDATE Flag

When a discoverer encounters an entity that appears to span into one or
more counties beyond the current county run, they must:

1. Add `CROSS_COUNTY_CANDIDATE` to the `identity_notes_raw` field of
   the entity's raw discovery record.
2. List all known counties in the `counties` field (semicolon-separated).
3. If a matching entity already exists in the DB under a different ID,
   add `COLLISION:{existing-oh-id}` after `CROSS_COUNTY_CANDIDATE`
   (e.g., `COLLISION:OH-PAU-TR-001`).
4. If the entity matches a known MC entity from the bootstrap check, use
   Scenario C (§4.3) instead; do not create a new record.

## 6.2 Conditions Triggering the Flag

Apply `CROSS_COUNTY_CANDIDATE` when:
- The entity's physical extent is described in source materials as
  crossing a county line.
- The entity's managing authority operates across multiple counties
  without a county-specific anchor.
- The entity's name or description matches a known multi-county entity
  (e.g., a named water trail, a national scenic trail, a rail-trail
  system with published multi-county extent).
- The entity appears in the bootstrap "Known Multi-County Entities" list
  but the source for the current county has new information.

## 6.3 Conditions Not Triggering the Flag

Do NOT apply `CROSS_COUNTY_CANDIDATE` when:
- A trail loops briefly into a neighboring county on a single parcel
  managed entirely by the current county's entity (a park that happens
  to straddle a county line with one uniform managing authority).
- The entity name is generic (e.g., "Storybook Trail") and the county's
  instance is a distinct physical installation unrelated to same-named
  installations in other counties. Each installation is a separate entity.
- GPS coordinates confirm the entity is entirely within the current county,
  despite source language suggesting otherwise.

------------------------------------------------------------
# 7. RESOLUTION ENGINE EXTENSION — MC ID ASSIGNMENT

This section extends the Resolution Engine (na_resolution_engine.md)
with a Phase 0 step that runs before Phase 1 Grouping. All existing
Phase 1–4 rules remain unchanged.

## 7.1 Phase 0: MC Candidate Detection (New)

Before the standard Phase 1 Grouping step, the Resolution Engine scans
all raw discovery records for the current county run and checks the live
DB for:

**Step 0.1 — Inbound collision check**: For each record with
`CROSS_COUNTY_CANDIDATE` in `identity_notes_raw`, query the DB for
entities of the same type with overlapping county values and a
fuzzy-normalized name match (token-set ratio ≥ 85). If a match is found:
- If the existing record has an MC ID → apply Scenario C (§4.3).
- If the existing record has a county-prefixed ID → escalate to
  Scenario B (§4.2). Assign an MC ID and proceed to §7.2.

**Step 0.2 — Explicit collision hint**: For each record with
`COLLISION:{id}` in `identity_notes_raw`, the cited ID is treated as a
confirmed collision. Proceed directly to §7.2.

**Step 0.3 — Known MC hint**: For each record with `KNOWN_MC:{oh-mc-id}`,
no new ID is assigned. The existing MC record is updated using §7.3
field authority rules with any `MC_SUPPLEMENTAL:{oh-mc-id}` data.

**Step 0.4 — Pass-through**: Records without any of the above flags
proceed to Phase 1 Grouping unchanged.

## 7.2 MC ID Assignment Algorithm

When an MC ID must be assigned (Scenario B or manual migration):

1. Determine the entity type code from §3.2.
2. Query the current maximum sequence number for that type in the
   OH-MC namespace (§3.3).
3. Assign the next sequence number: `OH-MC-{TYPE}-{MAX+1:04d}`.
   Always use 4-digit zero-padding for new assignments.
4. Record the assignment in `resolution_provenance` with:
   - `run_id`: current pipeline run ID
   - `resolution_type`: `mc_assignment`
   - `source_ids`: comma-separated list of all county-prefixed IDs being
     merged
   - `canonical_id`: the new MC ID
   - `reason`: `collision` or `migration` or `no_primary_county`

## 7.3 Field Authority Rules (Canonical Record Selection)

When merging multiple county-prefixed records into one MC record, field
values are selected using the following priority:

**Priority 1 — Primary managing entity's county record**: The record from
the county where the primary managing entity is headquartered or where
the majority of the entity's physical extent lies. For trails, this is
the county that contributed the most trail miles or the county listed
first in the official managing entity's own published materials.

**Priority 2 — Most recently updated record**: If Priority 1 is
ambiguous, use the record with the most recent `updated_at` timestamp.

**Priority 3 — Most complete record**: If Priority 2 is tied, use the
record with the fewest null fields.

**Field-level merge rules** (applied after canonical record is selected):

| Field Category              | Rule                                          |
|-----------------------------|-----------------------------------------------|
| Identity fields (name, type)| Use canonical record; flag conflicts for review |
| `counties`                  | Union all values from all source records (deduplicated, semicolon-separated) |
| `length_mi`                 | Use canonical record; note discrepancies in notes |
| `url_primary`               | Use canonical record; add others to `urls` or `maps` |
| `governance`, `ownership`   | Use canonical record; note others in `governance` |
| `partner_agencies`          | Union all values (deduplicated)               |
| `description`               | Use canonical record                          |
| `notes`                     | Concatenate all unique notes                  |
| `identity_notes`            | Use canonical record; strip CROSS_COUNTY_CANDIDATE flags |
| `status`                    | Use canonical record; flag conflicts for review |
| GPS fields                  | Use canonical record if present; else use best-sourced record |

**Conflict flags**: If identity fields (name, type, status) differ
between source records, add a `MERGE_CONFLICT:{field}` note to the MC
record's `notes` field and route to the manual review queue.

## 7.4 Relationship Table Updates

After assigning an MC ID, update all relationship tables to replace
the deprecated county-prefixed IDs with the canonical MC ID:

```sql
UPDATE trail_network_members SET trail_id = '{OH-MC-ID}' 
  WHERE trail_id IN ({deprecated-ids});

UPDATE trail_to_segment SET trail_id = '{OH-MC-ID}'
  WHERE trail_id IN ({deprecated-ids});

UPDATE access_point_parents SET parent_entity_id = '{OH-MC-ID}'
  WHERE parent_entity_id IN ({deprecated-ids});

UPDATE trail_parents SET trail_id = '{OH-MC-ID}'
  WHERE trail_id IN ({deprecated-ids});
```

For For Trail Segments of a merged trail: if segments carry county-prefixed
IDs (e.g., OH-HEN-TS-005 as a segment of the merged Wabash Cannonball
Trail), the segment retains its county-prefixed ID for the segment
portion unless the segment itself is involved in a collision. The
segment's `parent_trail_id` is updated to the OH-MC Trail ID.

## 7.5 Provenance Recording

Every MC ID assignment and every county-prefixed ID deprecation must be
logged in `resolution_provenance`. The minimum required fields:

```
run_id            : pipeline run ID or 'IMP-104-migration' or 'IMP-107-migration'
resolution_type   : 'mc_assignment' | 'mc_deprecation' | 'mc_supplemental'
entity_type       : trail | trail_network | site | ...
source_id         : the county-prefixed OH- ID being deprecated or supplemented
canonical_id      : the OH-MC-* ID
reason            : collision | migration | known_mc | no_primary_county
notes             : free text describing the merge decision
timestamp         : UTC ISO-8601
```

------------------------------------------------------------
# 8. EXISTING ENTITY MIGRATIONS

## 8.1 Migration Criteria

**IMP-104 (2026-05-07)**: Two confirmed collision cases existed in the
live DB where the same entity had been independently discovered and
recorded by multiple county runs under different county-prefixed IDs.
These were resolved immediately. All other multi-county entities with
a single record were not collisions; they retained their county-prefixed
IDs at that time (see Non-Migration Entities table below).

**IMP-107 (2026-05-12)**: Global ID format migration. All entity IDs
converted from `{COUNTY}-{TYPE}-{SEQ}` to `OH-{COUNTY}-{TYPE}-{SEQ}`.
Multi-county entities (any entity whose `counties` field contains more
than one value) were simultaneously migrated to `OH-MC-{TYPE}-{SEQ}`.
This affected all entities in all entity tables, all FK tables, all
provenance tables, and all TSV output files across 12 county directories.
7 confirmed Category 2 duplicate trails were DELETED (see §8.5).
4 Category 1 sequence collisions were resolved by renumbering (see §8.3).

## 8.2 Migration Procedure (IMP-104 and future collisions)

For each collision:
1. Identify all county-prefixed OH-* records that represent the same entity.
2. Select the canonical record per §7.3 Priority rules.
3. Assign the next OH-MC-* ID per §7.2.
4. Write the merged record to the DB.
5. If the duplicate records have unique data not present in the canonical
   record: deprecate (update `notes` with `DEPRECATED: superseded by
   {OH-MC-ID}`; do not delete). If the duplicate records are confirmed
   true duplicates with zero unique data: delete (see §8.5).
6. Update relationship tables per §7.4.
7. Update `held_entities`: remove hold records for all deprecated IDs;
   if the held entity was waiting on a partner county, that hold is
   resolved by the MC record.
8. Log in `resolution_provenance`.

## 8.3 Migration Records

### Migration 1: Maumee River Water Trail → OH-MC-T-0001

**IMP-104 source records** (all were confirmed duplicates of the same water trail):

| Old ID      | County    | counties field                              |
|-------------|-----------|---------------------------------------------|
| DEF-T-002   | Defiance  | Defiance; Henry; Lucas; Paulding; Wood      |
| LUC-T-013   | Lucas     | Defiance;Henry;Lucas;Wood                   |
| PAU-TR-002  | Paulding  | Paulding; Defiance; Henry; Wood; Lucas      |
| WOD-TR-003  | Wood      | Defiance; Henry; Lucas; Williams; Wood      |

**IMP-107 action**: All four source records were deleted (Category 2 —
confirmed true duplicates with no unique data relative to canonical).
Access points parented to these records were reparented to OH-MC-T-0001.

**Canonical ID**: OH-MC-T-0001 (renamed from MC-T-0001 by IMP-107)

**Name**: Maumee River Water Trail

**Canonical counties**: Defiance; Henry; Lucas; Paulding; Williams; Wood

---

### Migration 2: Wabash Cannonball Trail → OH-MC-T-0002

**IMP-104 source records** (all were confirmed duplicates):

| Old ID      | County    | counties field                      |
|-------------|-----------|-------------------------------------|
| HEN_T_006   | Henry     | Fulton;Henry;Lucas;Williams         |
| LUC-T-010   | Lucas     | Fulton;Henry;Lucas;Williams         |
| WIL-TR-003  | Williams  | Williams; Fulton; Henry; Lucas      |

**IMP-107 action**: All three source records were deleted (Category 2).
Access points parented to these records were reparented to OH-MC-T-0002.

**Canonical ID**: OH-MC-T-0002 (renamed from MC-T-0002 by IMP-107)

**Name**: Wabash Cannonball Trail

**Canonical counties**: Fulton; Henry; Lucas; Williams

**Note on FUL-TR-007 / OH-MC-TR-007**: "Wabash Cannonball Trail (North
Fork)" — a name variant suggesting a distinct fork or segment, not the
canonical main trail. Retained as OH-MC-TR-007 (multi-county
Fulton;Henry;Lucas;Williams). Currently held
(cross_county_or_access_unconfirmed). Evaluate at Fulton County pipeline:
if confirmed as a segment, set `parent_trail_id = OH-MC-T-0002` and
convert to a Trail Segment entity. If confirmed as a distinct named
trail, it retains OH-MC-TR-007.

---

### IMP-107 Category 1 Collision Renumbers

During IMP-107, four entities had sequence collisions when projected
into the OH-MC namespace. The lower-priority entity was renumbered to
the next available sequence:

| Old ID     | Name                             | Collision With  | New ID          |
|------------|----------------------------------|-----------------|-----------------|
| SC-S-0004  | Shawnee State Forest             | FR-S-0004       | OH-MC-S-0002    |
| SC-S-0012  | Scioto Brush Creek State Scenic R| FR-S-0012       | OH-MC-S-0003    |
| FR-T-0002  | Camp Chase Trail                 | MC-T-0002       | OH-MC-T-0003    |
| SC-T-0001  | Shawnee Backpack Trail           | MC-T-0001       | OH-MC-T-0006    |

Priority rule: existing canonical OH-MC records > Franklin (FR) > Scioto
(SC) > others. The winning entity keeps its sequence; the losing entity
is renumbered.

---

### Non-Migration Entities (Multi-County, Single Record — Current IDs)

The following entities list multiple counties and have a single canonical
record. They received OH-MC-* IDs during IMP-107 (multi-county
determination made by `counties` field having >1 value):

| Current ID        | Name                             | Counties                      | Notes                              |
|-------------------|----------------------------------|-------------------------------|------------------------------------|
| OH-MC-TN-0003     | Central Ohio Blueways            | Delaware;Franklin;Pickaway    | Franklin discovery                 |
| OH-PAU-TN-001     | North Country NST (network)      | Multi-state                   | Paulding discovery; retained PAU prefix as single-record multi-state entity |
| OH-MC-TN-0001     | Shawnee Bridle Trail Network     | Scioto;Adams                  | Scioto discovery                   |
| OH-MC-SN-0001     | Metro Parks Serving Franklin Co. | Delaware;Fairfield;Franklin;Pickaway | Franklin discovery            |
| OH-MC-T-001       | North Country NST (trail)        | Defiance;Henry;Lucas;Paulding;Putnam | Defiance discovery; 3-digit seq inherited; OH-WIL-TR-001 held — Scenario A pending Williams run |
| OH-MC-T-0003      | Camp Chase Trail                 | Franklin;Madison              | IMP-107 renumber from FR-T-0002 (seq collision) |
| OH-MC-T-0004      | Heritage Trail                   | Franklin;Madison              | Franklin primary                   |
| OH-MC-T-0108      | Olentangy Trail                  | Delaware;Franklin             | Franklin primary                   |
| OH-MC-T-0006      | Shawnee Backpack Trail           | Adams;Scioto                  | IMP-107 renumber from SC-T-0001 (seq collision) |
| OH-MC-T-0012      | Killbuck Marsh Wildlife Obs. Tr. | Wayne;Holmes                  | Wayne primary; Scenario A pending Holmes run |
| OH-MC-TR-001      | Miami and Erie Canal Towpath     | many counties                 | Paulding discovery; Scenario A — candidate for no further ID change unless second county run independently discovers it |
| OH-MC-TR-003      | Buckeye Trail — Delphos Section  | Paulding;Putnam;Allen;Auglaize| Paulding discovery; Scenario A     |
| OH-MC-TR-004      | Buckeye Trail — Defiance Section | Paulding;Defiance;Williams    | Paulding discovery; Scenario A     |

Note: OH-PAU-TN-001 is the sole entity that retains a county-prefixed
OH-PAU prefix despite being multi-state/multi-county. It is a single-
record entity and its governance anchor is the Paulding County discovery.
The MC prefix is not applied to entities with a clear single-discovery
anchor unless a collision or no-primary-county condition is met.

---

## 8.4 Held Entity Status (Current)

Current held_entities records after IMP-104 and IMP-107:

| held_id | record_id         | Name (truncated)                    | Hold Reason                         |
|---------|-------------------|-------------------------------------|-------------------------------------|
| 1       | OH-WA-S-0045      | Killbuck Marsh Wildlife Area        | multi_county                        |
| 3       | OH-WA-S-0046      | Funk Bottoms Wildlife Area          | multi_county                        |
| 4       | OH-WA-T-0013      | Chippewa Township Nature Preserve trails | identity_uncertain             |
| 5       | OH-WA-T-0014      | Sippo Valley Trail                  | multi_county (Scenario A, Holmes)   |
| 6       | OH-WA-T-0015      | Holmes County Trail                 | multi_county (Scenario A, Holmes)   |
| 15      | OH-PAU-S-001      | Lake Wayne R. Carr Wildlife Area    | gps_missing                         |
| 16      | OH-PAU-S-009      | Guilda H. Culler Memorial Park      | gps_missing                         |
| 17      | OH-PAU-S-021      | Flat Rock Creek Nature Preserve     | gps_missing                         |
| 18      | OH-PAU-AP-005     | Viall's Lock Campsite               | gps_missing                         |
| 19      | OH-WIL-TR-001     | North Country NST                   | multi_state_federal (Scenario A)    |
| 21      | OH-MC-SI-003      | Maumee State Forest                 | cross_county_or_access_unconfirmed  |
| 22      | OH-MC-SI-006      | Oak Openings Corridor (MT)          | cross_county_or_access_unconfirmed  |
| 23      | OH-MC-TR-005      | Stewardship Trail                   | cross_county_or_access_unconfirmed  |
| 24      | OH-MC-TR-007      | Wabash Cannonball Trail (North Fork)| cross_county_or_access_unconfirmed  |
| 29–35   | OH-WOD-SI-*/SEED-*| Various Wood County entities        | verification_required / unconfirmed_baseline_seed |
| 36–40   | OH-HEN-S-*        | Henry County wildlife areas         | gps_missing                         |

## 8.5 Category 2 Deletion Rule

The standard IMP-104 procedure called for deprecating duplicate records
(updating `notes` field; do not delete). IMP-107 introduced an exception:

**Category 2 — Confirmed true duplicates**: A duplicate record is
Category 2 when it represents the exact same physical entity as the
canonical record AND contains no unique data not already present in the
canonical record (no unique APs, no distinct description, no unique GPS
or acreage).

Category 2 duplicates were DELETED from the `trails` table and all FK
tables during IMP-107. Their associated access points were reparented
to the canonical OH-MC-* record.

This exception does NOT apply to records that carry any unique field
values (different AP references, unique description, different acreage
measurement, etc.). Those records must be deprecated per the standard
procedure, not deleted.

------------------------------------------------------------
# 9. CROSS-REFERENCES

- Resolution Engine: `na_resolution_engine.md` — Phase 0 inserted
  before Phase 1 Grouping (§8). MC candidate detection is a pre-grouping
  step only; all Phases 1–4 run as documented.
- Resolution Rules: `na_resolution_rules.md` §4.11 — "Multi-County
  Entities Are Single Entities" is the governing principle that this
  protocol operationalizes.
- Bootstrap skill: `na-bootstrap.md` — Bootstrap Step 3 must include the
  Known Multi-County Entities DB check (§5 of this module).
- Discovery skill: `na-discovery.md` — Tier transition checkpoints must
  note the CROSS_COUNTY_CANDIDATE flagging requirement (§6 of this
  module).
- Pipeline skill: `na-pipeline.md` — Stage 1a (Resolution Pass 1) must
  reference this module for MC candidate detection (Phase 0).
- Audit logging: `audit/na_audit_and_logging.md` — MC ID assignments and
  deprecations are logged in `resolution_provenance` per §7.5.
- Water trail sub-procedure: `discovery/na_water_trail_discovery_subproc.md`
  §8 — multi-county water trail handling follows this protocol.

------------------------------------------------------------
# 10. ANTI-PATTERNS

| Anti-Pattern                                                      | Correct Action                                              |
|-------------------------------------------------------------------|-------------------------------------------------------------|
| Creating a county-prefixed OH-* ID for an entity with KNOWN_MC in identity_notes_raw | Use Scenario C; reference existing OH-MC-* ID; do not create new record |
| Assigning OH-MC-* IDs to entities that merely cross a county line with a single managing county | OH-MC-* IDs are for collisions and no-primary-county cases; single-discovery cross-border entities keep OH-{COUNTY}-* prefix |
| Merging "Storybook Trail" instances across counties as one entity | Generic names are not identity anchors; verify physical location — separate installations are separate entities |
| Leaving collision records in the DB without MC resolution         | All detected collisions must be resolved; they cannot be deferred indefinitely |
| Assigning OH-MC-* IDs at discovery time (before pipeline)        | OH-MC-* IDs are assigned by the Resolution Engine at pipeline time only; discoverers use CROSS_COUNTY_CANDIDATE flags |
| Deleting deprecated records that carry unique data                | Deprecate with `DEPRECATED: superseded by {OH-MC-ID}` note; only delete confirmed Category 2 true duplicates (see §8.5) |
| Updating relationship tables to remove deprecated IDs without logging | All relationship table updates require resolution_provenance entries |
| Writing entity IDs without the OH- state prefix                  | All Ohio entity IDs must begin with OH-; bare {COUNTY}-{TYPE}-{SEQ} format is obsolete |

------------------------------------------------------------
# END OF CROSS-COUNTY RESOLUTION PROTOCOL v5.2
