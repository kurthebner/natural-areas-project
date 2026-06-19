# NATURAL AREAS PROJECT
# ENTITY UPSERT ENGINE v5.2
(Bridge from Normalized Entities to the Entity Graph Schema v5.x)

The Entity Upsert Engine v5.2 is the **persistence layer** that takes
**Normalized Entities** and writes them into the **Entity Graph Schema v5.x**.

It is responsible for:

- ID assignment and stability
- Insert vs. update decisions
- Relationship table population
- Geometry storage
- Provenance storage
- Conflict and uncertainty storage
- Manual Review Queue management ✨ NEW
- Held entity tracking ✨ NEW

It sits between:

- Normalization Engine v5.x (input)
- TSV Output + Analysis (downstream consumers)

------------------------------------------------------------
# CHANGES FROM v4.0

- **GPS storage**: `gps_primary` string column replaced by `gps_lat` + `gps_lon` numeric columns
- **Township/municipality**: Now populated via GIS derivation — upsert engine writes these as GIS-derived values, not source-collected values
- **County field renamed**: `county_list` → `counties` throughout
- **Governance renamed**: `managing_agency` → `governance`; `secondary_managing_agencies` → `partner_agencies`
- **Removed fields**: `access_level`, `role` (Access Points); `network_affiliation` (Sites/Trails/Trail Segments); `source_primary`, `source_all`, `geometry` from normalized schema
- **Manual Review Queue**: New table and workflow for collision-flagged entities from Normalization Engine
- **Held entities**: New tracking for entities valid but incomplete (missing GPS, unresolved member IDs)

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- **IMP-054 — §6.6 Trail → Parent Site relationship handling added**: The Upsert Engine
  now handles the `trail_parents` relationship table. When a normalized Trail entity
  carries a `parent_site_id` value (set by the Trail Normalization Contract v5.2 §5.20
  containment determination pass), the engine inserts a row into `trail_parents`
  (trail_id, parent_site_id). Parent Site must exist in the Entity Graph before the
  row is inserted; if not yet present, the Trail is flagged as a Held Entity pending
  Site upsert. See §6.6 below.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **Version references updated**: Normalization Engine reference updated to v5.x; Resolution Engine reference updated to v5.x
- **Four-tier organizational model**: All entity sections updated to reflect the ownership → governance → partner_agencies → coordination model per Site Schema v5.x and Normalization Engine v5.x
- **`partner_agencies` semantics clarified**: Per Site Schema v5.x, `partner_agencies` represents formal, documented co-operator organizations; must not duplicate Ownership or Governance; must not include informal volunteer groups
- **`coordination` field added**: Sections 5.1–5.5 updated to include `coordination` (community-based, volunteer, advisory, or informal partners) as a distinct stored field
- **`plus_code` added to core table sections**: Sites (5.1) and Access Points (5.6) now explicitly list `plus_code` as a GIS-derived field written by the upsert engine

------------------------------------------------------------
# 1. PURPOSE

The Entity Upsert Engine v5.1:

- Ensures each normalized entity is represented exactly once in the graph
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

- Normalized entity objects (all six types) from Normalization Engine v5.x
- Normalization provenance records
- Resolution provenance records
- Discovery provenance records
- Collision-flagged entity pairs (from Normalization Engine deduplication check)
- Held entity records (from Normalization Engine)
- Entity Graph Schema v5.x

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

Each normalized entity arrives from the Normalization Engine with one of the following intents:

- **insert** — new entity, no match in Entity Graph
- **update** — entity already exists in Entity Graph (matched on integrity anchor)
- **hold** — entity is valid but incomplete; defer upsert
- **review** — entity has a collision; route to Manual Review Queue, do not upsert

## 3.2 Matching Logic

- Matching is based on **Resolution Engine v5.x** output combined with the **Normalization Engine deduplication check**:
  - Each normalized entity arrives with a resolved identity key or explicit intent
- The Upsert Engine uses the resolved identity key to find existing rows
  - Insert if no match
  - Update if match found (integrity anchor matched existing entity)

## 3.3 ID Assignment

- **New entities (insert):**
  - Receive a new surrogate ID (`site_id`, `trail_id`, etc.)
- **Existing entities (update):**
  - Retain their existing ID
  - Fields updated in place per upsert rules

## 3.4 Run Isolation

- Each upsert run is associated with a `run_id` in `run_metadata`
- Entities inserted or updated in a run must record:
  - `run_id`
  - `updated_at`

------------------------------------------------------------
# 4. UPSERT WORKFLOW (PER ENTITY)

For each normalized entity received:

1. Read the intent flag (insert / update / hold / review).
2. **If review:** Route to Manual Review Queue (Section 7). Stop.
3. **If hold:** Write to held entity tracking table (Section 8). Stop.
4. **If insert or update:**
   a. Determine entity type.
   b. Compute or read the resolved identity key.
   c. Look up existing entity in the appropriate core table.
   d. If found → update fields per upsert rules.
   e. If not found → insert new row.
   f. Upsert relationships.
   g. Upsert geometry.
   h. Upsert provenance.
   i. Upsert conflicts and uncertainty (if any).

------------------------------------------------------------
# 5. CORE TABLE UPSERT RULES

## 5.1 Sites

- Table: `sites`
- Match on: Resolved identity key (from Resolution Engine)
- Key v5.0 field changes:
  - `gps_lat` (float) and `gps_lon` (float) replace `gps_primary` string
  - `counties` replaces `county_list`
  - `governance` replaces `managing_agency`
  - `partner_agencies` replaces `secondary_managing_agencies`
  - `network_affiliation` column removed
  - `source_primary`, `source_all` columns removed (tracked in provenance tables)
- Organizational fields (four-tier model per Site Schema v5.x):
  - `ownership` — legal title holder
  - `governance` — managing organization(s); semicolon-delimited
  - `partner_agencies` — formal, documented co-operator organizations; semicolon-delimited; must not duplicate ownership or governance; must not include informal volunteer groups
  - `coordination` — community-based, volunteer, advisory, or informal partners; semicolon-delimited
- GPS and spatial fields:
  - `gps_lat` (float), `gps_lon` (float) — validated numeric coordinates from Normalization Engine
  - `plus_code` (string) — GIS-derived Open Location Code; computed by Normalization Engine v5.x from validated GPS; blank if GPS is blank
  - `township` (string) — GIS-derived; blank if GPS is blank
  - `municipality` (string) — GIS-derived; blank if GPS is blank or entity is not within a municipality
- Update: All normalized fields + `updated_at` + `run_id`
- Insert: All normalized fields + `created_at` + `updated_at` + `run_id`

## 5.2 Trails

- Table: `trails`
- Same pattern as Sites
- Key v5.0 field changes:
  - `governance` replaces `managing_agency`
  - `partner_agencies` replaces `secondary_managing_agencies`
  - `network_affiliation` column removed
  - `maps` stored as JSON array (replaces `map_url` string)
- Organizational fields (four-tier model):
  - `ownership`, `governance`, `partner_agencies`, `coordination`

## 5.3 Trail Segments

- Table: `trail_segments`
- Must ensure `trail_id` exists before inserting/updating
- Key v5.0 field changes:
  - `governance` replaces `managing_agency`
  - `geometry` stored in `entity_geometry` table only (not in `trail_segments` core table)
  - `maps` stored as JSON array
- Organizational fields: `governance` (primary); `coordination` if applicable

## 5.4 Trail Networks

- Table: `trail_networks`
- Key v5.0 field changes:
  - `governance` replaces `managing_agency`
  - `partner_agencies` replaces `secondary_managing_agencies`
  - `member_trail_ids` stored as relationship rows in `trail_to_network`
  - `maps` stored as JSON array
- Organizational fields (four-tier model):
  - `ownership`, `governance`, `partner_agencies`, `coordination`

## 5.5 Site Networks

- Table: `site_networks`
- Key v5.0 field changes:
  - `governance` replaces `managing_agency`
  - `partner_agencies` replaces `secondary_managing_agencies`
  - `member_site_ids` stored as relationship rows in `site_to_network`
- Organizational fields (four-tier model):
  - `ownership`, `governance`, `partner_agencies`, `coordination`

## 5.6 Access Points

- Table: `access_points`
- Key v5.0 field changes:
  - `gps_lat` (float) and `gps_lon` (float) replace `gps_primary` string
  - `access_level` column removed
  - `role` column removed
  - `features` stored as semicolon-delimited text
  - Township and municipality populated from GIS derivation
- GPS and spatial fields:
  - `gps_lat` (float), `gps_lon` (float) — validated numeric coordinates from Normalization Engine
  - `plus_code` (string) — GIS-derived Open Location Code; computed by Normalization Engine v5.x from validated GPS; blank if GPS is blank
  - `township` (string) — GIS-derived; blank if GPS is blank
  - `municipality` (string) — GIS-derived; blank if GPS is blank or entity is not within a municipality

------------------------------------------------------------
# 6. RELATIONSHIP UPSERT RULES

## 6.1 Site Parent

- Table: `site_parent`
- For each Site with a parent:
  - Ensure both `site_id` and `parent_site_id` exist
  - Insert if relationship does not exist
  - Do not duplicate identical relationships

## 6.2 Trail → Segment

- Table: `trail_to_segment`
- Ensure both `trail_id` and `trail_segment_id` exist
- Insert if relationship does not exist

## 6.3 Trail → Network

- Table: `trail_to_network`
- Populated from `member_trail_ids` on Trail Network entities
- Ensure both `trail_network_id` and `trail_id` exist before inserting

## 6.4 Site → Network

- Table: `site_to_network`
- Populated from `member_site_ids` on Site Network entities
- Ensure both `site_network_id` and `site_id` exist before inserting

## 6.5 Access Point Parents

- Table: `access_point_parents`
- For each parent relationship:
  - Ensure parent entity exists in Entity Graph
  - Insert relationship if not present
  - Allowed parent types: Site, Trail, Trail Segment only

## 6.6 Trail → Parent Site (IMP-054)

- Table: `trail_parents`
- Populated from the containment determination pass in Trail Normalization Contract v5.2 §5.20.
- Not all Trails have a `trail_parents` row — extra-limital Trails are excluded.

**Upsert behavior:**
- If the normalized Trail entity has a `parent_site_id` value:
  - Verify `parent_site_id` exists in the Entity Graph `sites` table.
  - If Site exists: insert row `(trail_id, parent_site_id)` into `trail_parents` if not already present. No update on conflict (relationship is idempotent).
  - If Site does not yet exist: add Trail to Held Entities with hold reason `parent_site_missing`; release and insert `trail_parents` row when the Site is upserted.
- If the normalized Trail entity has no `parent_site_id`: no `trail_parents` action — skip silently.

**Identity Notes enforcement:**
- After inserting a `trail_parents` row, verify that the Trail's `identity_notes` field contains
  `Contained within [Site Name] ([site_id]).` If not present, append it.

**Error condition:**
- If `identity_notes_raw` at discovery contained "Parent site: [Name]" but no matching Site
  can be found in the Entity Graph, add to Manual Review Queue with collision type `parent_site_missing`.

------------------------------------------------------------
# 7. MANUAL REVIEW QUEUE ✨ NEW IN v5.0

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
  - `existing_graph_entity` (entity already in graph — treated as update candidate)
- `entity_record_a` (JSON — full normalized entity)
- `entity_record_b` (JSON — full normalized entity, or existing graph record)
- `field_diff` (JSON — field-level diff between A and B)
- `run_id`
- `queued_at`
- `resolution_status` — one of: `pending`, `merged`, `split`, `dismissed`
- `resolved_by`
- `resolved_at`
- `resolution_notes`

## 7.3 Workflow

1. Normalization Engine detects collision → sends both records to Upsert Engine with `review` intent
2. Upsert Engine writes both records to `manual_review_queue` with `resolution_status = pending`
3. Neither record is upserted to core tables until manually resolved
4. Human reviewer examines field diff and chooses one of:
   - **Merge** — combine into single entity, upsert, mark `merged`
   - **Split** — confirm they are different entities, upsert both with distinct anchors, mark `split`
   - **Dismiss** — one record is clearly wrong, discard it, upsert the other, mark `dismissed`
5. After resolution, Upsert Engine processes the resolved outcome

## 7.4 Collision Type: Existing Graph Entity

When a new normalized entity matches an existing entity in the graph (same integrity anchor), this is treated as an **update**, not a collision, unless field values conflict significantly. The engine should:

- Auto-update non-conflicting fields
- Route to Manual Review Queue only if high-confidence fields (name, category, GPS) disagree materially

------------------------------------------------------------
# 8. HELD ENTITIES ✨ NEW IN v5.0

## 8.1 Purpose

Some entities are valid but incomplete at normalization time and should not
be upserted yet. Rather than rejecting them, the engine holds them pending
completion.

## 8.2 Held Entity Table: `held_entities`

Fields:
- `hold_id` (PK)
- `entity_type`
- `hold_reason` — one of:
  - `missing_gps` (Access Point without GPS coordinates)
  - `unresolved_member_ids` (Network with member IDs not yet in graph)
  - `unresolved_parent` (entity with parent not yet in graph)
- `entity_record` (JSON — full normalized entity)
- `run_id`
- `held_at`
- `release_status` — one of: `held`, `released`, `abandoned`
- `released_at`
- `release_run_id`

## 8.3 Release Workflow

On each subsequent normalization run:
1. Check all held entities with `hold_reason = missing_gps` — if GPS has since been acquired, release and upsert
2. Check all held entities with `hold_reason = unresolved_member_ids` — if member entities are now in graph, release and upsert
3. Check all held entities with `hold_reason = unresolved_parent` — if parent now exists, release and upsert
4. Entities held for more than a configurable threshold (e.g., 90 days) are flagged for review and potential abandonment

------------------------------------------------------------
# 9. GEOMETRY UPSERT RULES

## 9.1 Entity Geometry

- Table: `entity_geometry`
- For each entity with geometry:
  - If geometry for (entity_type, entity_id) exists → update if changed
  - Else → insert new geometry row
- GPS coordinates (`gps_lat`, `gps_lon`) are stored in core entity tables
- Full geometry (polygons, linestrings) is stored in `entity_geometry`
- Geometry is populated in the GIS phase — not from discovery

------------------------------------------------------------
# 10. PROVENANCE UPSERT RULES

All provenance tables are **append-only** — prior run records are never overwritten.

## 10.1 Discovery Provenance

- Table: `discovery_provenance`
- Each discovery run may add new provenance rows
- Source mapping (URL → fields) stored here

## 10.2 Resolution Provenance

- Table: `resolution_provenance`
- Append-only per resolution run
- Merge decisions and conflict flags recorded here

## 10.3 Normalization Provenance

- Table: `normalization_provenance`
- Append-only per normalization run
- GPS parsing results, GIS derivation results, vocabulary mappings recorded here

------------------------------------------------------------
# 11. CONFLICT & UNCERTAINTY UPSERT RULES

## 11.1 Conflicts

- Table: `entity_conflicts`
- For each conflict from Resolution or Manual Review:
  - Insert new row if new conflict
  - Update `resolution_status` when resolved

## 11.2 Uncertainty

- Table: `entity_uncertainty`
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
  - Consider holding the entity if the missing reference is critical

## 12.2 Geometry Failures

- If geometry is invalid:
  - Log error
  - Skip geometry insert/update
  - Preserve entity in core table

## 12.3 Provenance Failures

- If provenance cannot be written:
  - Log error
  - Do not roll back entity upsert
  - Flag for manual provenance reconciliation

## 12.4 GPS Storage Failures

- If gps_lat or gps_lon cannot be written (type mismatch, constraint violation):
  - Log error
  - Write entity without GPS
  - Flag for review

------------------------------------------------------------
# 13. INTEGRATION POINTS

The Entity Upsert Engine v5.1 integrates with:

- **Normalization Engine v5.x** (input)
- **Entity Graph Schema v5.x** (target tables)
- **TSV Output Specifications v5.x** (downstream consumer)
- **Audit & Logging Module v5.x** (run metadata, error logging)
- **Run Metadata** (`run_metadata` table)

------------------------------------------------------------
# 14. VERSIONING

- This module is **Entity Upsert Engine v5.1**
- Any change to upsert rules, ID stability, or organizational field structure requires v5.2, v5.3, etc.

------------------------------------------------------------
# END OF ENTITY UPSERT ENGINE v5.1
