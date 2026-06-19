# NATURAL AREAS PROJECT
# ENTITY UPSERT ENGINE v6.0
(Bridge from Normalized Entities to the Database Schema v6.x)

This module supersedes Entity Upsert Engine v5.2.

The Entity Upsert Engine v6.0 is the **persistence layer** that takes
**Normalized Entities** and writes them into the database.

It is responsible for:

- ID assignment and stability
- Insert vs. update decisions
- Relationship table population
- Geometry storage
- Provenance storage
- Conflict and uncertainty storage
- Manual Review Queue management
- Held entity tracking

It sits between:

- Normalization Engine v6.x (input)
- TSV Output + Analysis (downstream consumers)

------------------------------------------------------------
# CHANGES FROM v5.2 → v6.0

- **Entity types updated**: Six → four. `trails`, `trail_segments`,
  `trail_networks` tables replaced by `trailthings` for new v6.x entities.
  Legacy trail tables retained for existing DB records (see §5.2 note).

- **Relationship tables updated**: `trail_to_segment`, `trail_to_network`,
  `trail_parents` replaced by `trailthing_hierarchy` for v6.x entities (§6.2).
  Legacy relationship tables retained for existing DB records.

- **`parent_site_network_id` field**: Replaces `external_parent_id` /
  `external_parent_type` throughout. Trailthing → Site Network relationship
  now uses a direct FK to `site_networks.network_id` (§6.4).

- **New Site fields**: `habitat_type`, `access_notes`, `last_verified_date`,
  `field_verified` added to §5.1 Site upsert rules.

- **Trailthing core table rules added** (§5.2): `source_term`,
  `source_hierarchy_context`, `parent_id`, `site_parent_id`,
  `parent_site_network_id` documented. No GPS, Plus Code, township, or
  municipality — Trailthings are multi-location entities.

- **Held entity child rule updated** (§8.3): Trailthing hierarchy holds added —
  a Trailthing whose `parent_id` references a held Trailthing is itself held
  with `hold_reason = "parent_held"`. Site Network holds updated for
  `unresolved_member_ids` scope change (Site Networks only; not Trailthings).

- **AP parent types updated** (§6.5): Allowed parent types are now Site and
  Trailthing (Trail and Trail Segment removed).

- **`hold_reason` canonical values updated** (§8.2): Added
  `cross_county_held`, `cross_county_candidate`, `unconfirmed_baseline_seed`,
  `identity_uncertain`. All eight canonical values documented.

- **DDL table groups documented** (§13): Complete `CREATE TABLE IF NOT EXISTS`
  requirements for all four table groups.

- **All v5.2 core logic carried forward**: upsert strategy, matching logic,
  ID assignment, run isolation, manual review queue, held entity tracking,
  release workflow, geometry, provenance, conflict & uncertainty, error
  handling.

------------------------------------------------------------
# 1. PURPOSE

The Entity Upsert Engine v6.0:

- Ensures each normalized entity is represented exactly once in the database
- Maintains stable IDs across runs (within a database)
- Maintains all cross-entity relationships
- Maintains geometry, provenance, conflicts, and uncertainty
- Routes collision-flagged entities to the Manual Review Queue
- Tracks held entities pending completion
- Prepares the database for TSV export and analysis

It does **not**:

- Discover entities
- Perform fuzzy identity matching or source merging
- Normalize fields
- Generate TSVs directly

------------------------------------------------------------
# 2. INPUTS AND OUTPUTS

## 2.1 Inputs

- Normalized entity objects (all four types) from Normalization Engine v6.x
- Normalization provenance records
- Resolution provenance records
- Discovery provenance records
- Collision-flagged entity pairs (from Normalization Engine deduplication check)
- Held entity records (from Normalization Engine)
- Database schema v6.x

## 2.2 Outputs

- Populated core entity tables
- Populated relationship tables
- Populated geometry tables
- Populated provenance tables
- Populated conflict & uncertainty tables
- Populated Manual Review Queue
- Populated held entity tracking table
- Updated run metadata

------------------------------------------------------------
# 3. UPSERT STRATEGY

## 3.1 Incoming Entity Intent

Each normalized entity arrives from the Normalization Engine with one of the
following intents:

- **insert** — new entity, no match in database
- **update** — entity already exists in database (matched on integrity anchor)
- **hold** — entity is valid but incomplete; defer upsert
- **review** — entity has a collision; route to Manual Review Queue, do not upsert

## 3.2 Matching Logic

Matching is based on Resolution Engine v6.x output combined with the
Normalization Engine deduplication check. Each normalized entity arrives with
a resolved identity key or explicit intent. The Upsert Engine uses the resolved
identity key to find existing rows:
- Insert if no match
- Update if match found (integrity anchor matched existing entity)

## 3.3 ID Assignment

- **New entities (insert):** Receive a new surrogate ID (`site_id`,
  `trailthing_id`, `network_id`, `access_point_id`) in `OH-{COUNTY}-{TYPE}-{SEQ}`
  format.
- **Existing entities (update):** Retain their existing ID. Fields updated
  in place per upsert rules.

## 3.4 Run Isolation

Each upsert run is associated with a `run_id` in `run_metadata`. Entities
inserted or updated in a run must record `run_id` and `updated_at`.

------------------------------------------------------------
# 4. UPSERT WORKFLOW (PER ENTITY)

For each normalized entity received:

1. Read the intent flag (insert / update / hold / review).
2. **If review:** Route to Manual Review Queue (§7). Stop.
3. **If hold:** Write to held entity tracking table (§8). Stop.
4. **If insert or update:**
   a. Determine entity type.
   b. Compute or read the resolved identity key.
   c. Look up existing entity in the appropriate core table.
   d. If found → update fields per upsert rules.
   e. If not found → insert new row.
   f. Upsert relationships (§6).
   g. Upsert geometry (§9).
   h. Upsert provenance (§10).
   i. Upsert conflicts and uncertainty if any (§11).

------------------------------------------------------------
# 5. CORE TABLE UPSERT RULES

## 5.1 Sites

- **Table**: `sites`
- **Match on**: Resolved identity key (from Resolution Engine)
- **Organizational fields** (four-tier model):
  - `ownership` — legal title holder
  - `governance` — managing organization(s); semicolon-delimited
  - `partner_agencies` — formal, documented co-operator organizations;
    semicolon-delimited; must not duplicate ownership or governance
  - `coordination` — community-based, volunteer, advisory, or informal
    partners; semicolon-delimited
- **GPS and spatial fields**:
  - `gps_lat` (float), `gps_lon` (float) — validated numeric coordinates
  - `plus_code` (string) — computed by Normalization Engine from validated GPS;
    blank if GPS is blank
  - `township` (string) — GIS-derived; blank if GPS is blank
  - `municipality` (string) — GIS-derived; blank if GPS is blank
- **New v6.0 fields**:
  - `habitat_type` (text) — open vocabulary; ecological/natural character;
    pass through verbatim from normalization
  - `access_notes` (text) — seasonal access restrictions and access caveats
  - `last_verified_date` (DATE, YYYY-MM-DD) — date record last confirmed
    accurate against authoritative source
  - `field_verified` (boolean, default false) — true only after physical visit
  - `ebird_hotspot_id` (TEXT, nullable) — eBird L-code (e.g. `L123456`);
    pass through verbatim from normalization; blank if no hotspot exists
- **Hierarchy**:
  - `parent_site_id` (FK to sites.site_id) — populated for child Sites
- **Update**: All normalized fields + `updated_at` + `run_id`
- **Insert**: All normalized fields + `created_at` + `updated_at` + `run_id`

## 5.2 Trailthings

- **Table**: `trailthings` (v6.x new entities)

**Note on legacy trail tables**: Existing DB records in `trails`,
`trail_segments`, and `trail_networks` tables are not migrated to `trailthings`
automatically. Legacy tables are retained as-is. New entities discovered under
v6.x protocols are written to `trailthings`. A migration pass will be addressed
after the Trailthing experiment concludes (IMP-007).

- **Match on**: Resolved identity key (from Resolution Engine)
- **Identity fields**:
  - `name` — official name
  - `alternate_names` — semicolon-delimited documented variants
  - `source_term` — verbatim term from authoritative source; pass through
    exactly; never normalize or map to controlled vocabulary
  - `source_hierarchy_context` — verbatim source framing; pass through exactly
- **Hierarchy fields**:
  - `parent_id` (FK to trailthings.trailthing_id) — parent Trailthing;
    null for top-level entities
  - `site_parent_id` (FK to sites.site_id) — parent Site when access-dependent;
    null for extra-limital Trailthings
  - `parent_site_network_id` (FK to site_networks.network_id) — parent Site
    Network when explicitly documented; null if no Site Network parent
- **Organizational fields** (four-tier model):
  - `ownership`, `governance`, `partner_agencies`, `coordination`
- **Character fields**:
  - `use_type`, `surface_type`, `origin_type`, `org_type` — vocabulary-controlled
  - `status`, `difficulty` — vocabulary-controlled
  - `accessibility` — free text
- **Geography**:
  - `counties` — semicolon-delimited; alphabetical
  - `states_included` — semicolon-delimited; blank for Ohio-only
  - `total_length` — numeric; miles
- **No GPS, Plus Code, township, or municipality**: Trailthings are
  multi-location entities. These fields do not apply.
- **Documentation fields**:
  - `description`, `trail_history`, `identity_notes`, `notes`
  - `url` — semicolon-delimited authoritative URLs
  - `maps` — semicolon-delimited map resource URLs
- **Update**: All normalized fields + `updated_at` + `run_id`
- **Insert**: All normalized fields + `created_at` + `updated_at` + `run_id`

## 5.3 Site Networks

- **Table**: `site_networks`
- **Match on**: Resolved identity key (from Resolution Engine)
- **Organizational fields** (four-tier model):
  - `ownership`, `governance`, `partner_agencies`, `coordination`
- **Member fields**:
  - `member_count` — integer; officially published count
  - `member_site_ids` — convenience cache; semicolon-delimited site_id values
    from `site_network_members` relationship table
- **Update**: All normalized fields + `updated_at` + `run_id`
- **Insert**: All normalized fields + `created_at` + `updated_at` + `run_id`

## 5.4 Access Points

- **Table**: `access_points`
- **Match on**: Resolved identity key (from Resolution Engine)
- **GPS and spatial fields**:
  - `gps_lat` (float), `gps_lon` (float) — validated numeric coordinates
  - `plus_code` (string) — computed by Normalization Engine from validated GPS
  - `township` (string) — GIS-derived
  - `municipality` (string) — GIS-derived
- **Verification fields**:
  - `last_verified_date` (DATE, YYYY-MM-DD)
  - `field_verified` (boolean, default false)
- **Update**: All normalized fields + `updated_at` + `run_id`
- **Insert**: All normalized fields + `created_at` + `updated_at` + `run_id`

------------------------------------------------------------
# 6. RELATIONSHIP UPSERT RULES

## 6.1 Site Parent

- **Table**: `site_parent`
- For each Site with a `parent_site_id`:
  - Ensure both `site_id` and `parent_site_id` exist in `sites`
  - Insert if relationship does not exist
  - Do not duplicate identical relationships
  - If parent Site does not yet exist: hold child Site with
    `hold_reason = "unresolved_parent"`

## 6.2 Trailthing Hierarchy

- **Table**: `trailthing_hierarchy`
- For each Trailthing with a `parent_id`:
  - Ensure both parent and child `trailthing_id` values exist in `trailthings`
  - Insert row `(parent_id, child_id)` if not already present
  - If parent Trailthing does not yet exist: hold child Trailthing with
    `hold_reason = "unresolved_parent"`
  - After inserting, verify that the Trailthing's `identity_notes` contains
    the parent reference note; append if missing

## 6.3 Trailthing → Site Parent

- **Table**: `trailthings` (via `site_parent_id` field — no separate table)
- For each Trailthing with a `site_parent_id`:
  - Ensure the referenced `site_id` exists in `sites`
  - If Site does not yet exist: hold Trailthing with
    `hold_reason = "unresolved_parent"`
  - After writing, verify that `identity_notes` contains
    `Contained within [Site Name] ([site_id]).`

## 6.4 Trailthing → Site Network Parent

- **Table**: `trailthings` (via `parent_site_network_id` field — no separate table)
- For each Trailthing with a `parent_site_network_id`:
  - Ensure the referenced `network_id` exists in `site_networks`
  - If Site Network does not yet exist: log as warning; do not hold — Site
    Network parent is not a blocking dependency
  - After writing, verify that `identity_notes` contains the Site Network
    membership note; append if missing

## 6.5 Site → Network (Site Network Members)

- **Table**: `site_network_members`
- Populated from `member_site_ids` on Site Network entities
- Ensure both `network_id` and `site_id` exist before inserting
- If any member `site_id` does not exist: log with
  `hold_reason = "unresolved_member_ids"`; hold the Site Network

## 6.6 Access Point Parents

- **Table**: `access_point_parents`
- For each parent relationship:
  - Ensure parent entity exists in database
  - Insert relationship if not present
  - **Allowed parent entity types in v6.x**: `Site`, `Trailthing`
    (Trail and Trail Segment removed; legacy records referencing those types
    are not modified)
  - If parent entity does not yet exist: hold AP with
    `hold_reason = "unresolved_parent"`

------------------------------------------------------------
# 7. MANUAL REVIEW QUEUE

## 7.1 Purpose

The Manual Review Queue holds entity pairs that the Normalization Engine
flagged as collisions — two normalized entities sharing the same integrity
anchor that could not be automatically merged.

## 7.2 Queue Table: `manual_review_queue`

Fields:
- `review_id` (PK)
- `entity_type`
- `collision_type` — one of:
  - `conflict_flagged` (Resolution flagged but did not merge)
  - `resolution_miss` (Resolution did not detect the duplicate)
  - `existing_graph_entity` (entity already in DB — treated as update candidate)
  - `parent_site_missing` (Trailthing or child Site with unresolvable parent)
- `entity_record_a` (JSON — full normalized entity)
- `entity_record_b` (JSON — full normalized entity, or existing DB record)
- `field_diff` (JSON — field-level diff between A and B)
- `run_id`
- `queued_at`
- `resolution_status` — one of: `pending`, `merged`, `split`, `dismissed`
- `resolved_by`
- `resolved_at`
- `resolution_notes`

## 7.3 Workflow

1. Normalization Engine detects collision → sends both records to Upsert Engine
   with `review` intent
2. Upsert Engine writes both records to `manual_review_queue` with
   `resolution_status = pending`
3. Neither record is upserted to core tables until manually resolved
4. Human reviewer examines field diff and chooses one of:
   - **Merge** — combine into single entity, upsert, mark `merged`
   - **Split** — confirm they are different entities, upsert both with distinct
     anchors, mark `split`
   - **Dismiss** — one record is clearly wrong, discard it, upsert the other,
     mark `dismissed`
5. After resolution, Upsert Engine processes the resolved outcome

## 7.4 Collision Type: Existing DB Entity

When a new normalized entity matches an existing entity in the DB (same
integrity anchor), this is treated as an **update**, not a collision, unless
field values conflict significantly. The engine should:

- Auto-update non-conflicting fields
- Route to Manual Review Queue only if high-confidence fields (name, category,
  GPS) disagree materially

------------------------------------------------------------
# 8. HELD ENTITIES

## 8.1 Purpose

Some entities are valid but incomplete at normalization time and should not
be upserted yet. Rather than rejecting them, the engine holds them pending
completion.

## 8.2 Held Entity Table: `held_entities`

| Column | Notes |
|---|---|
| `record_id` | PK (auto-increment integer) |
| `entity_type` | `site`, `trailthing`, `site_network`, `access_point` |
| `name` | Entity display name |
| `hold_reason` | Canonical value — see table below |
| `hold_detail` | Free-text explanation or JSON detail blob |
| `county` | County name (e.g., `Henry`) |
| `run_id` | FK to `run_metadata.run_id` |
| `created_at` | Timestamp row was inserted |

**Canonical `hold_reason` values:**

| `hold_reason` | Triggering stage | Resolved by |
|---|---|---|
| `gps_missing` | GPS Gate (Stage 4c) | GPS re-run or `gps_unresolvable = true` |
| `parent_held` | Normalization Engine — child of held parent | Parent entity released |
| `unresolved_parent` | Upsert Engine — parent not yet in DB | Parent entity upserted in partner county pipeline run |
| `unresolved_member_ids` | Upsert Engine — Site Network with unresolved member sites | Member sites upserted |
| `cross_county_candidate` | Resolution Engine Phase 0 | Cross-county resolution pass |
| `cross_county_held` | Cross-county resolution Scenario A | Partner county pipeline run |
| `unconfirmed_baseline_seed` | Discovery close-out / baseline reconciliation | Authoritative source confirms active entity, or entity confirmed non-existent |
| `identity_uncertain` | Discovery — source implies existence but individual identity unresolvable | Field verification or authoritative source inventory |

`hold_detail` carries the full normalized entity JSON or a short diagnostic
string depending on context.

## 8.3 Held-Entity Child Rule (IMP-086)

### When It Fires

Immediately after the GPS Gate held list is finalized, before any individual
entity normalization begins. The scan runs once per pipeline run.

### Trigger Condition

Any child entity whose parent reference points to an entity already in
`held_entities` for the current run must itself be held.

### Affected Entity Types

**Access Points** — scan `parent_entity_id` against the held set:

```python
held_ids = {e["entity_id"] for e in held_entities}
for ap in access_points:
    if ap.get("parent_entity_id") in held_ids:
        held_entities.append({
            "entity_type": "access_point",
            "name": ap["name"],
            "hold_reason": "parent_held",
            "hold_detail": f"Parent entity {ap['parent_entity_id']} is held pending resolution",
            "county": ap["county_primary"],
            "run_id": RUN_ID,
        })
        access_points.remove(ap)
```

**Child Sites** — scan `parent_site_id` against the held set using the same
pattern. Any child Site whose parent Site is held is itself moved to
`held_entities` with `hold_reason = "parent_held"`.

**Trailthings with parent_id** — scan `parent_id` against the held set. Any
Trailthing whose parent Trailthing is held is itself moved to `held_entities`
with `hold_reason = "parent_held"`. This ensures child Trailthings are not
normalized against a parent that is not yet in the DB.

### Exempt

**Site Networks** — `member_site_ids` referencing held Sites remain in the
Site Network record. The Site Network is held only if the `unresolved_member_ids`
condition is explicitly triggered (§6.5). Dangling member references are logged
as `INFO`; they resolve when the member Site's county run completes.

### Hold Detail Format

`hold_detail` must identify the parent: `"Parent entity {parent_id} is held
pending resolution"`. This ensures the release workflow (§8.4) can locate the
parent row efficiently.

## 8.4 Release Workflow

On each subsequent normalization run, before normalization begins:

1. **`gps_missing`**: Re-run GPS Acquisition for each held entity name + county.
   If GPS is now resolvable, remove the `held_entities` row and route the entity
   through normalization normally.
2. **`parent_held`**: Check if the parent entity has since been upserted into
   its core table. If so, remove the `held_entities` row and re-process the
   child through normalization.
3. **`unresolved_member_ids`**: Check if all referenced member entity IDs now
   exist in the DB. If so, remove the row and re-process.
4. **`unresolved_parent`**: Check if the parent entity now exists. If so,
   remove the row and re-process.
5. **`cross_county_held`**: Check if the partner county pipeline has run and
   the MC entity is now in the DB. If so, remove the row and re-process.
6. **`unconfirmed_baseline_seed`**: Check for authoritative source confirmation.
   If confirmed active: remove from `held_entities` and route to full pipeline.
   If confirmed non-existent: remove from `held_entities` with disposition note
   in `hold_detail`.
7. Rows held for more than 90 days with no resolution are flagged in the QA
   report for manual review. Delete the row after review if no longer actionable.

------------------------------------------------------------
# 9. GEOMETRY UPSERT RULES

## 9.1 Entity Geometry

- **Table**: `entity_geometry`
- For each entity with geometry:
  - If geometry for (entity_type, entity_id) exists → update if changed
  - Else → insert new geometry row
- GPS coordinates (`gps_lat`, `gps_lon`) are stored in core entity tables
- Full geometry (polygons, linestrings) is stored in `entity_geometry`
- Geometry is populated in the GIS phase — not from discovery

------------------------------------------------------------
# 10. PROVENANCE UPSERT RULES

All provenance tables are **append-only** — prior run records are never
overwritten.

## 10.1 Discovery Provenance

- **Table**: `discovery_provenance`
- Each discovery run may add new provenance rows
- Source mapping (URL → fields) stored here

## 10.2 Resolution Provenance

- **Table**: `resolution_provenance`
- Append-only per resolution run
- Merge decisions and conflict flags recorded here
- MC ID assignments and deprecations recorded here (Cross-County Resolution
  Protocol v6.x §7.5)
- Columns: `(prov_id, entity_id, entity_type, county, resolution_run, notes,
  run_id, created_at)` — use `resolution_run`, NOT `resolution_action`

## 10.3 Normalization Provenance

- **Table**: `normalization_provenance`
- Append-only per normalization run
- GPS parsing results, GIS derivation results, vocabulary mappings recorded here
- `gps_unresolvable = true` flag recorded here for entities that pass the GPS
  Gate without coordinates
- Unmapped vocabulary tokens logged here as `unmapped_token_dropped` (IMP-116)

------------------------------------------------------------
# 11. CONFLICT & UNCERTAINTY UPSERT RULES

## 11.1 Conflicts

- **Table**: `entity_conflicts`
- For each conflict from Resolution or Manual Review:
  - Insert new row if new conflict
  - Update `resolution_status` when resolved

## 11.2 Uncertainty

- **Table**: `entity_uncertainty`
- For each uncertainty flag:
  - Insert new row if new
  - May be updated if uncertainty level changes

------------------------------------------------------------
# 12. ERROR HANDLING

## 12.1 Foreign Key Failures

- If a relationship references a non-existent entity:
  - Log error
  - Skip that relationship row
  - Do not fail the entire run
  - Hold the entity if the missing reference is critical (§8)

## 12.2 Geometry Failures

- If geometry is invalid:
  - Log error
  - Skip geometry insert/update
  - Preserve entity in core table

## 12.3 Provenance Failures

- If provenance cannot be written:
  - Log error
  - Do not roll back entity upsert
  - Flag run in `run_metadata` as provenance-incomplete

## 12.4 Run Metadata

- **Table**: `run_metadata`
- INSERT columns: `(run_id, county, state, run_date, records_input, normalized,
  held, notes, created_at)`
- `state` must be full name ("Ohio") — not a two-character abbreviation ("OH")
  (IMP-101)
- Do NOT use `pipeline_version`, `entity_id`, or `entity_name` columns

------------------------------------------------------------
# 13. REQUIRED DDL TABLE GROUPS

Every upsert script must include `CREATE TABLE IF NOT EXISTS` for all tables
in all four groups before any upsert operations begin.

## 13.1 Primary Entity Tables
```sql
CREATE TABLE IF NOT EXISTS sites (...);
CREATE TABLE IF NOT EXISTS trailthings (...);
CREATE TABLE IF NOT EXISTS site_networks (...);
CREATE TABLE IF NOT EXISTS access_points (...);
```

Legacy tables (for existing v5.x DB records — do not drop):
```sql
CREATE TABLE IF NOT EXISTS trails (...);
CREATE TABLE IF NOT EXISTS trail_segments (...);
CREATE TABLE IF NOT EXISTS trail_networks (...);
```

## 13.2 Relationship Tables
```sql
CREATE TABLE IF NOT EXISTS site_parent (...);
CREATE TABLE IF NOT EXISTS trailthing_hierarchy (...);
CREATE TABLE IF NOT EXISTS site_network_members (...);
CREATE TABLE IF NOT EXISTS access_point_parents (...);
```

Legacy relationship tables (retained for existing records):
```sql
CREATE TABLE IF NOT EXISTS trail_to_segment (...);
CREATE TABLE IF NOT EXISTS trail_network_members (...);
CREATE TABLE IF NOT EXISTS trail_parents (...);
```

## 13.3 Operational Tables
```sql
CREATE TABLE IF NOT EXISTS held_entities (...);
CREATE TABLE IF NOT EXISTS manual_review_queue (...);
CREATE TABLE IF NOT EXISTS entity_conflicts (...);
CREATE TABLE IF NOT EXISTS entity_uncertainty (...);
CREATE TABLE IF NOT EXISTS entity_geometry (...);
```

## 13.4 Provenance Tables
```sql
CREATE TABLE IF NOT EXISTS run_metadata (...);
CREATE TABLE IF NOT EXISTS discovery_provenance (...);
CREATE TABLE IF NOT EXISTS resolution_provenance (...);
CREATE TABLE IF NOT EXISTS normalization_provenance (...);
```

------------------------------------------------------------
# 14. MODULE DEPENDENCIES

This module depends on:

- Site Schema Module v6.x
- Trailthing Schema Module v6.x
- Site Network Schema Module v6.x
- Access Point Schema Module v6.x
- Normalization Engine v6.x
- Resolution Engine v6.x
- GPS Acquisition Module v6.x
- Child Site Rules Module v6.x
- Cross-County Resolution Protocol v6.x
- Audit & Logging Module v6.x

------------------------------------------------------------
# END OF ENTITY UPSERT ENGINE v6.0
