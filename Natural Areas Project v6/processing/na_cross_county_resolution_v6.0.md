# NATURAL AREAS PROJECT
# CROSS-COUNTY RESOLUTION PROTOCOL v6.0
Natural Areas Project — v6.x Pipeline

This module supersedes Cross-County Resolution Protocol v5.2.

Historical migration records (IMP-104, IMP-107) have been moved to:
`na_db_migration_log.md` at the project root.

------------------------------------------------------------
# CHANGES FROM v5.2 → v6.0

- **Entity types updated**: Trail (T), Trail Segment (TS), Trail Network (TN)
  consolidated into Trailthing (TT) throughout. Type code table updated (§3.2).
  SQL queries updated to query the `trailthings` table (§3.3, §5.1).

- **Legacy type codes retained with explanation** (§3.2): Existing DB entities
  carrying TR, SI, T, TN, TS type codes are preserved as-is. New Trailthing
  entities discovered under v6.x receive TT codes. The coexistence of legacy
  and new codes is expected and intentional — the Trailthing consolidation is
  a data-gathering experiment pending reclassification after sufficient county
  runs (IMP-007). A future revision will address how legacy-coded entities
  are reclassified when the experiment concludes.

- **Relationship table updates simplified** (§7.4): `trail_network_members`,
  `trail_to_segment`, `trail_parents` replaced with `trailthing_hierarchy`
  for new Trailthing entities. Legacy relationship tables retained for
  legacy-coded entities.

- **Migration history removed from module**: IMP-104 and IMP-107 migration
  records, Category 2 deletion rule, and held entity snapshot moved to
  `na_db_migration_log.md`. This module is forward-looking only.

- **All v5.2 core protocol rules carried forward**: MC ID scheme, three
  cross-county scenarios, bootstrap pre-discovery check, discovery-time
  flagging, Phase 0 Resolution Engine extension, field authority rules,
  provenance recording, anti-patterns.

------------------------------------------------------------
# 1. PURPOSE

This module governs how entities that span multiple Ohio counties are
identified, recorded, and resolved across county discovery runs. It
establishes the MC (multi-county) ID scheme, defines when MC IDs apply,
and specifies the procedures that discovery, the Resolution Engine, and
the bootstrap process must follow.

The core problem this module solves: as the Natural Areas Project builds
up county by county, the same physical entity will be encountered
independently by multiple county runs. Without a formal protocol, the
same entity accumulates duplicate county-prefixed records that cannot be
automatically resolved and that obscure the true entity count.

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
runs. The entity appears in the DB multiple times with different IDs.
This condition requires immediate resolution; it cannot be deferred.

**Condition B — No Primary County**: The entity spans multiple counties
with no clear single-county managing authority — for example, an ODNR or
federal land unit where assigning any county prefix would be arbitrary.

## 2.2 MC ID Not Required (County-Prefixed ID Retained)

An entity retains its county-prefixed ID when:

- It was discovered by one county and extends into a neighboring county,
  but the primary managing entity is clearly county-based (e.g., a Metro
  Parks trail system that has one trail crossing a county line).
- It is a held entity pending a partner county run (Scenario A). The
  county-prefixed ID is kept as a provisional anchor; MC ID is assigned
  when the partner county runs and Collision or Known conditions are
  confirmed.

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

- `OH-` prefix: mandatory state prefix for all Ohio entities.
- `{COUNTY}`: county abbreviation (e.g., `FR` for Franklin, `LUC` for
  Lucas), OR `MC` for entities that span multiple counties with no
  single-county governance anchor (see §2.1).
- `{TYPE}`: entity type code (see §3.2).
- `{SEQ}`: sequence number, zero-padded, assigned per county+type
  namespace in order of discovery.

Examples (multi-county entities):
  OH-MC-TT-0001   (new v6.x Trailthing — multi-county)
  OH-MC-S-0001    (multi-county Site)
  OH-MC-SN-0001   (multi-county Site Network)

Examples (single-county entities):
  OH-FR-S-0001    (Franklin County Site)
  OH-FR-TT-0001   (Franklin County Trailthing, v6.x)
  OH-WA-AP-0001   (Wayne County Access Point)

## 3.2 Entity Type Codes

| Entity Type  | Code | MC Example ID  | County Example ID | Notes |
|---|---|---|---|---|
| Site         | S    | OH-MC-S-0001   | OH-FR-S-0001      | |
| Trailthing   | TT   | OH-MC-TT-0001  | OH-FR-TT-0001     | v6.x new entities |
| Site Network | SN   | OH-MC-SN-0001  | OH-FR-SN-0001     | |
| Access Point | AP   | OH-MC-AP-0001  | OH-FR-AP-0001     | |

**Legacy type codes (existing DB entities — retained as-is):**

| Legacy Code | Former Entity Type | Example ID    | Notes |
|---|---|---|---|
| T           | Trail              | OH-MC-T-0001  | Retained from v5.x |
| TR          | Trail (variant)    | OH-MC-TR-001  | Some county conventions used TR |
| TS          | Trail Segment      | OH-FR-TS-001  | |
| TN          | Trail Network      | OH-MC-TN-0001 | |
| SI          | Site (variant)     | OH-MC-SI-003  | Some county conventions used SI |

**Why legacy codes coexist with TT**: The Trailthing (TT) entity type is a
working consolidation of Trail, Trail Segment, and Trail Network introduced
in v6.x as a data-gathering experiment (IMP-007, IMP-009). Existing DB
entities retain their original type codes. New entities discovered under
v6.x receive TT codes. After sufficient county runs, the project will
evaluate whether to reclassify Trailthings into sub-types (which may
reintroduce T, TS, TN as distinct types) or maintain the unified model.
At that point, a migration pass will address legacy-coded entity IDs.
Until then, legacy codes and TT codes coexist intentionally.

Access Points rarely span county lines; MC-AP is reserved for unusual cases.

## 3.3 Sequence Management

Sequences are managed per `(COUNTY, TYPE)` namespace. For OH-MC-* entities
the namespace is `(MC, TYPE)`. The next available sequence number is
MAX(existing IDs in that namespace) + 1. Sequence numbers are never reused,
even if a record is deleted or deprecated.

To query next available sequences for OH-MC-* entities:

```sql
-- New Trailthing entities (v6.x)
SELECT MAX(CAST(REPLACE(trailthing_id, 'OH-MC-TT-', '') AS INTEGER)) AS next_TT
FROM trailthings WHERE trailthing_id LIKE 'OH-MC-TT-%';

-- Legacy trail entities (existing DB)
SELECT MAX(CAST(REPLACE(trail_id, 'OH-MC-T-', '') AS INTEGER)) AS next_T
FROM trails WHERE trail_id LIKE 'OH-MC-T-%';

-- Site Networks
SELECT MAX(CAST(REPLACE(network_id, 'OH-MC-SN-', '') AS INTEGER)) AS next_SN
FROM site_networks WHERE network_id LIKE 'OH-MC-SN-%';

-- Sites
SELECT MAX(CAST(REPLACE(site_id, 'OH-MC-S-', '') AS INTEGER)) AS next_S
FROM sites WHERE site_id LIKE 'OH-MC-S-%';
```

When assigning new OH-MC-* sequences, always use 4-digit zero-padded format
(e.g., 0003, 0004). Some legacy entities use 3-digit sequences inherited from
prior county conventions — 4-digit padding distinguishes new assignments.

**Sequence gaps are expected** (IMP-117): Do not infer missing entities from
gaps in sequence numbers. Gaps arise from provisional IDs superseded during
resolution, entities merged into existing records, or sequence numbers
withdrawn during QA.

------------------------------------------------------------
# 4. THREE CROSS-COUNTY SCENARIOS

## 4.1 Scenario A — Held (Partner County Not Yet Run)

**Situation**: County A discovers an entity that clearly extends into County B,
but County B has not yet been run.

**Discovery-time action (County A)**:
1. Create a provisional record with a County A-prefixed ID.
2. Add `CROSS_COUNTY_CANDIDATE` to `identity_notes_raw`.
3. Route to `held_entities` with `hold_reason = "cross_county_held"` and
   a note naming the partner county/counties.
4. Note the partner counties in the `counties` field.

**Pipeline action**: The Resolution Engine sees the hold flag and defers
MC ID assignment. The county-prefixed ID is used as a provisional anchor.

**When County B runs**: County B's bootstrap check (§5) finds the held
entity. County B's discovery must reference the existing provisional record.
When County B's pipeline runs, the Resolution Engine executes Scenario B
(Collision) or Scenario C (Known), whichever applies, and assigns an MC ID
if warranted.

**Key rule**: Held multi-county entities are never upserted with their
provisional county-prefixed ID as permanent. They must pass through MC
resolution before final DB write.

## 4.2 Scenario B — Collision (Multiple Independent Discoveries)

**Situation**: County A and County B have each independently discovered and
recorded the same entity under different county-prefixed IDs.

**Detection**: The Resolution Engine detects collision when two records from
different county runs produce a high-confidence identity match (anchor match
+ similarity score above the merge threshold) AND both records have
multi-county `counties` fields that overlap.

A collision may also be flagged manually during discovery when a discoverer
finds an entity already in the DB under a different county's ID.

**Resolution Engine action**:
1. Assign an MC ID (§7.2) to the canonical merged record.
2. Select field values from the canonical record (§7.3).
3. Write the merged record to the DB with the MC ID.
4. Deprecate all county-prefixed records by updating their `notes` field
   with `DEPRECATED: superseded by {MC-ID}` and recording in
   `resolution_provenance`.
5. Update all relationship tables to reference the MC ID (§7.4).
6. Remove the `held_entities` entries for all deprecated records.
7. Log the full merge in `resolution_provenance`.

**Manual collision flag**: If a discoverer finds a collision before the
pipeline runs, they add `COLLISION:{existing-id}` to `identity_notes_raw`
alongside `CROSS_COUNTY_CANDIDATE`. The Resolution Engine uses this as a
strong match hint.

## 4.3 Scenario C — Known (MC ID Already in DB)

**Situation**: An entity already exists in the DB with an MC ID. County B
encounters the same entity during discovery.

**Discovery-time action (County B)**:
1. The bootstrap pre-check (§5) must have already surfaced the MC entity.
2. During discovery, note the existing MC ID in `identity_notes_raw`:
   `KNOWN_MC:{oh-mc-id}` (e.g., `KNOWN_MC:OH-MC-TT-0001`).
3. Do NOT create a new county-prefixed record for this entity.
4. If County B has new data (additional APs, corrected length, updated URL),
   flag it as `MC_SUPPLEMENTAL:{oh-mc-id}` and record the updated fields
   in the raw discovery file for the pipeline to merge.

**Pipeline action**: The Resolution Engine sees `KNOWN_MC:{oh-mc-id}`,
skips ID assignment, and applies any supplemental field updates to the
existing MC record using the field authority rules in §7.3.

------------------------------------------------------------
# 5. BOOTSTRAP PRE-DISCOVERY CHECK

Before any discovery work begins for a new county, the bootstrap step must
query the live DB for existing MC entities that are known to include or
likely include the target county.

## 5.1 Procedure

Execute the following queries at bootstrap time (substitute the target
county name for `{COUNTY}`):

```sql
-- MC Trailthings that list the target county (v6.x entities)
SELECT trailthing_id, name, counties FROM trailthings
WHERE trailthing_id LIKE 'OH-MC-TT-%'
AND counties LIKE '%{COUNTY}%';

-- Legacy MC trails (existing DB — v5.x entities)
SELECT trail_id, name, counties FROM trails
WHERE trail_id LIKE 'OH-MC-%'
AND counties LIKE '%{COUNTY}%';

-- Legacy MC trail networks (existing DB)
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
in the county's session files listing:
- All MC entities found by the queries above (ID, name, counties, type)
- All held entities from other counties that name the target county

This section is an explicit discovery input. During discovery, if any
entity on this list is encountered, the discoverer applies Scenario C (§4.3).
The entity must not be re-created with a county-prefixed ID.

## 5.3 Empty Result

If the bootstrap queries return no results, note "No existing MC entities
found for {COUNTY}" in the session files and proceed normally.

------------------------------------------------------------
# 6. DISCOVERY-TIME FLAGGING

## 6.1 CROSS_COUNTY_CANDIDATE Flag

When a discoverer encounters an entity that appears to span into one or
more counties beyond the current county run:

1. Add `CROSS_COUNTY_CANDIDATE` to the `identity_notes_raw` field.
2. List all known counties in the `counties` field (semicolon-separated).
3. If a matching entity already exists in the DB under a different ID,
   add `COLLISION:{existing-oh-id}` after `CROSS_COUNTY_CANDIDATE`.
4. If the entity matches a known MC entity from the bootstrap check, use
   Scenario C (§4.3) instead — do not create a new record.

## 6.2 Conditions Triggering the Flag

Apply `CROSS_COUNTY_CANDIDATE` when:
- The entity's physical extent is described in source materials as crossing
  a county line.
- The entity's managing authority operates across multiple counties without
  a county-specific anchor.
- The entity's name or description matches a known multi-county entity.
- The entity appears in the bootstrap "Known Multi-County Entities" list
  but the source for the current county has new information.

## 6.3 Conditions Not Triggering the Flag

Do NOT apply `CROSS_COUNTY_CANDIDATE` when:
- A trail loops briefly into a neighboring county on a single parcel managed
  entirely by the current county's entity.
- The entity name is generic (e.g., "Storybook Trail") and the county's
  instance is a distinct physical installation unrelated to same-named
  installations in other counties. Each installation is a separate entity.
- GPS coordinates confirm the entity is entirely within the current county,
  despite source language suggesting otherwise.

------------------------------------------------------------
# 7. RESOLUTION ENGINE EXTENSION — MC ID ASSIGNMENT

This section extends the Resolution Engine (na_resolution_engine.md) with
a Phase 0 step that runs before Phase 1 Grouping. All existing Phase 1–4
rules remain unchanged.

## 7.1 Phase 0: MC Candidate Detection

Before the standard Phase 1 Grouping step, the Resolution Engine scans all
raw discovery records for the current county run:

**Step 0.1 — Inbound collision check**: For each record with
`CROSS_COUNTY_CANDIDATE` in `identity_notes_raw`, query the DB for entities
of the same type with overlapping county values and a fuzzy-normalized name
match (token-set ratio ≥ 85). If a match is found:
- If the existing record has an MC ID → apply Scenario C (§4.3).
- If the existing record has a county-prefixed ID → escalate to Scenario B
  (§4.2). Assign an MC ID and proceed to §7.2.

**Step 0.2 — Explicit collision hint**: For each record with
`COLLISION:{id}` in `identity_notes_raw`, the cited ID is treated as a
confirmed collision. Proceed directly to §7.2.

**Step 0.3 — Known MC hint**: For each record with `KNOWN_MC:{oh-mc-id}`,
no new ID is assigned. The existing MC record is updated using §7.3 field
authority rules with any `MC_SUPPLEMENTAL:{oh-mc-id}` data.

**Step 0.4 — Pass-through**: Records without any of the above flags proceed
to Phase 1 Grouping unchanged.

## 7.2 MC ID Assignment Algorithm

When an MC ID must be assigned (Scenario B or new no-primary-county case):

1. Determine the entity type code from §3.2. New v6.x Trailthings use TT;
   legacy trail entities retain their existing code family.
2. Query the current maximum sequence number for that type in the OH-MC
   namespace (§3.3).
3. Assign the next sequence number: `OH-MC-{TYPE}-{MAX+1:04d}`.
   Always use 4-digit zero-padding for new assignments.
4. Record the assignment in `resolution_provenance` with:
   - `run_id`: current pipeline run ID
   - `resolution_type`: `mc_assignment`
   - `source_ids`: comma-separated list of all county-prefixed IDs being merged
   - `canonical_id`: the new MC ID
   - `reason`: `collision` | `no_primary_county`

## 7.3 Field Authority Rules (Canonical Record Selection)

When merging multiple county-prefixed records into one MC record:

**Priority 1 — Primary managing entity's county record**: The record from
the county where the primary managing entity is headquartered or where the
majority of the entity's physical extent lies.

**Priority 2 — Most recently updated record**: If Priority 1 is ambiguous,
use the record with the most recent `updated_at` timestamp.

**Priority 3 — Most complete record**: If Priority 2 is tied, use the record
with the fewest null fields.

**Field-level merge rules:**

| Field Category              | Rule |
|---|---|
| Identity fields (name, type)| Use canonical record; flag conflicts for review |
| `counties`                  | Union all values from all source records (deduplicated, semicolon-separated, alphabetical) |
| `total_length` / `acres`    | Use canonical record; note discrepancies in notes |
| `url_primary`               | Use canonical record; add others to `urls` or `maps` |
| `governance`, `ownership`   | Use canonical record; note others in notes |
| `partner_agencies`          | Union all values (deduplicated) |
| `description`               | Use canonical record |
| `notes`                     | Concatenate all unique notes |
| `identity_notes`            | Use canonical record; strip CROSS_COUNTY_CANDIDATE flags |
| `status`                    | Use canonical record; flag conflicts for review |
| GPS fields                  | Use canonical record if present; else use best-sourced record |
| `source_term`               | Use canonical record; if source_term_conflicts exist, log and flag |

**Conflict flags**: If identity fields (name, type, status) differ between
source records, add a `MERGE_CONFLICT:{field}` note to the MC record's
`notes` field and route to the manual review queue.

## 7.4 Relationship Table Updates

After assigning an MC ID, update all relationship tables to replace deprecated
county-prefixed IDs with the canonical MC ID.

**For new v6.x Trailthing entities:**

```sql
UPDATE trailthing_hierarchy SET parent_id = '{OH-MC-TT-ID}'
  WHERE parent_id IN ({deprecated-ids});

UPDATE trailthing_hierarchy SET child_id = '{OH-MC-TT-ID}'
  WHERE child_id IN ({deprecated-ids});

UPDATE access_point_parents SET parent_entity_id = '{OH-MC-TT-ID}'
  WHERE parent_entity_id IN ({deprecated-ids});
```

**For legacy trail entities (existing DB):**

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

## 7.5 Provenance Recording

Every MC ID assignment and every county-prefixed ID deprecation must be
logged in `resolution_provenance`:

```
run_id           : pipeline run ID
resolution_type  : 'mc_assignment' | 'mc_deprecation' | 'mc_supplemental'
entity_type      : trailthing | site | site_network | access_point
source_id        : the county-prefixed OH-* ID being deprecated or supplemented
canonical_id     : the OH-MC-* ID
reason           : collision | no_primary_county | known_mc
notes            : free text describing the merge decision
timestamp        : UTC ISO-8601
```

------------------------------------------------------------
# 8. ANTI-PATTERNS

| Anti-Pattern | Correct Action |
|---|---|
| Creating a county-prefixed OH-* ID for an entity with KNOWN_MC in identity_notes_raw | Use Scenario C; reference existing OH-MC-* ID; do not create new record |
| Assigning OH-MC-* IDs to entities that merely cross a county line with a single managing county | OH-MC-* IDs are for collisions and no-primary-county cases only |
| Merging "Storybook Trail" instances across counties as one entity | Generic names are not identity anchors; verify physical location — separate installations are separate entities |
| Leaving collision records in the DB without MC resolution | All detected collisions must be resolved; they cannot be deferred indefinitely |
| Assigning OH-MC-* IDs at discovery time (before pipeline) | OH-MC-* IDs are assigned by the Resolution Engine only; discoverers use CROSS_COUNTY_CANDIDATE flags |
| Deleting deprecated records that carry unique data | Deprecate with `DEPRECATED: superseded by {OH-MC-ID}` note; only delete confirmed true duplicates with no unique data |
| Updating relationship tables without logging | All relationship table updates require resolution_provenance entries |
| Writing entity IDs without the OH- state prefix | All Ohio entity IDs must begin with OH-; bare {COUNTY}-{TYPE}-{SEQ} format is obsolete |
| Assuming gaps in sequence numbers indicate missing entities | Sequence gaps are expected (IMP-117); do not infer missing entities from gaps |

------------------------------------------------------------
# 9. CROSS-REFERENCES

- Resolution Engine v6.x — Phase 0 inserted before Phase 1 Grouping.
  All Phases 1–4 run unchanged.
- County Baseline Module v6.x — bootstrap pre-discovery check (§5 of
  this module) is a mandatory bootstrap step.
- Audit & Logging Module v6.x — MC ID assignments and deprecations are
  logged in `resolution_provenance` per §7.5.
- Database Migration Log (`na_db_migration_log.md`) — historical record
  of IMP-104 and IMP-107 migrations; specific entity migration records.

------------------------------------------------------------
# END OF CROSS-COUNTY RESOLUTION PROTOCOL v6.0
