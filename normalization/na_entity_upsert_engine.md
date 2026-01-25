# NATURAL AREAS PROJECT
# ENTITY UPSERT ENGINE v4.0
(Bridge from Normalized Entities to the Entity Graph Schema v4.0)

The Entity Upsert Engine v4.0 is the **persistence layer** that takes
**Normalized Entities** and writes them into the **Entity Graph Schema v4.0**.

It is responsible for:

- ID assignment and stability
- Insert vs. update decisions
- Relationship table population
- Geometry storage
- Provenance storage
- Conflict and uncertainty storage

It sits between:

- Normalization Engine v4.0 (input)
- TSV Output + Analysis (downstream consumers)

------------------------------------------------------------
# 1. PURPOSE

The Entity Upsert Engine v4.0:

- Ensures each normalized entity is represented exactly once in the graph
- Maintains stable IDs across runs (within a database)
- Maintains all cross‑entity relationships
- Maintains geometry, provenance, conflicts, and uncertainty
- Prepares the database for TSV export and analysis

It does **not**:

- Discover entities
- Resolve identity conflicts
- Normalize fields
- Generate TSVs directly

------------------------------------------------------------
# 2. INPUTS AND OUTPUTS

## 2.1 Inputs

- Normalized entity objects (all six types)
- Normalization provenance
- Resolution provenance
- Discovery provenance
- Entity Graph Schema v4.0

## 2.2 Outputs

- Populated core entity tables
- Populated relationship tables
- Populated geometry tables
- Populated provenance tables
- Populated conflict & uncertainty tables
- Updated run metadata

------------------------------------------------------------
# 3. UPSERT STRATEGY

## 3.1 Matching Logic

- Matching is based on **Resolution Engine v4.0** output:
  - Each normalized entity arrives with a **resolved identity key** (or explicit instruction: new vs. existing).
- The Upsert Engine must:
  - Use the resolved identity key to find existing rows
  - Insert if no match
  - Update if match

## 3.2 ID Assignment

- New entities:
  - Receive a new surrogate ID (`site_id`, `trail_id`, etc.)
- Existing entities:
  - Retain their existing ID
  - Are updated in place

## 3.3 Run Isolation

- Each upsert run is associated with a `run_id` in `run_metadata`.
- Entities updated in a run must record:
  - `run_id`
  - `updated_at`

------------------------------------------------------------
# 4. UPSERT WORKFLOW (PER ENTITY)

For each normalized entity:

1. Determine entity type.
2. Compute or read the **resolved identity key**.
3. Look up existing entity in the appropriate core table.
4. If found:
   - Update fields according to upsert rules.
5. If not found:
   - Insert a new row.
6. Upsert relationships.
7. Upsert geometry.
8. Upsert provenance.
9. Upsert conflicts and uncertainty (if any).

------------------------------------------------------------
# 5. CORE TABLE UPSERT RULES

## 5.1 Sites

- Table: `sites`
- Match on:
  - Resolved identity key (from Resolution Engine)
- Update:
  - All normalized fields
  - `updated_at`
  - `run_id`
- Insert:
  - All normalized fields
  - `created_at`, `updated_at`, `run_id`

## 5.2 Trails

- Table: `trails`
- Same pattern as Sites.

## 5.3 Trail Segments

- Table: `trail_segments`
- Must ensure `trail_id` exists before inserting/updating.

## 5.4 Trail Networks

- Table: `trail_networks`

## 5.5 Site Networks

- Table: `site_networks`

## 5.6 Access Points

- Table: `access_points`

------------------------------------------------------------
# 6. RELATIONSHIP UPSERT RULES

## 6.1 Site Parent

- Table: `site_parent`
- For each Site with a parent:
  - Ensure both `site_id` and `parent_site_id` exist.
  - Insert if relationship does not exist.
  - Do not duplicate identical relationships.

## 6.2 Trail → Segment

- Table: `trail_to_segment`
- Ensure both `trail_id` and `trail_segment_id` exist.

## 6.3 Trail → Network

- Table: `trail_to_network`

## 6.4 Site → Network

- Table: `site_to_network`

## 6.5 Access Point Parents

- Table: `access_point_parents`
- For each parent:
  - Ensure parent entity exists.
  - Insert relationship if not present.

------------------------------------------------------------
# 7. GEOMETRY UPSERT RULES

## 7.1 Entity Geometry

- Table: `entity_geometry`
- For each entity with geometry:
  - If geometry for (entity_type, entity_id) exists:
    - Update geometry if changed.
  - Else:
    - Insert new geometry row.

------------------------------------------------------------
# 8. PROVENANCE UPSERT RULES

## 8.1 Discovery Provenance

- Table: `discovery_provenance`
- Append‑only:
  - Each discovery run may add new provenance rows.
  - Do not overwrite previous runs.

## 8.2 Resolution Provenance

- Table: `resolution_provenance`
- Append‑only per resolution run.

## 8.3 Normalization Provenance

- Table: `normalization_provenance`
- Append‑only per normalization run.

------------------------------------------------------------
# 9. CONFLICT & UNCERTAINTY UPSERT RULES

## 9.1 Conflicts

- Table: `entity_conflicts`
- For each conflict:
  - Insert new row if new conflict.
  - Update `resolution_status` when resolved.

## 9.2 Uncertainty

- Table: `entity_uncertainty`
- For each uncertainty:
  - Insert new row if new.
  - May be updated if uncertainty level changes.

------------------------------------------------------------
# 10. ERROR HANDLING

## 10.1 Foreign Key Failures

- If a relationship references a non‑existent entity:
  - Log error
  - Skip that relationship
  - Do not fail the entire run

## 10.2 Geometry Failures

- If geometry is invalid:
  - Log error
  - Skip geometry insert/update
  - Preserve entity

## 10.3 Provenance Failures

- If provenance cannot be written:
  - Log error
  - Do not roll back entity upsert

------------------------------------------------------------
# 11. INTEGRATION POINTS

The Entity Upsert Engine v4.0 integrates with:

- Normalization Engine v4.0 (input)
- Entity Graph Schema v4.0 (target)
- TSV Output Specifications v4.0 (downstream)
- TSV Integrity Check Module v4.0
- Audit & Logging Module v4.0
- Run Metadata (`run_metadata` table)

------------------------------------------------------------
# 12. VERSIONING

- This module is **Entity Upsert Engine v4.0**.
- Any change to upsert rules or ID stability requires v4.1, v4.2, etc.

------------------------------------------------------------
# END OF ENTITY UPSERT ENGINE v4.0