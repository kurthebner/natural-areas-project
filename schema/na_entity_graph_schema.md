# NATURAL AREAS PROJECT
# ENTITY GRAPH SCHEMA v4.0
(Multi‑Table SQLite Schema for Normalized Entities, Relationships, Geometry, Provenance, and Conflicts)

Authoritative schema for the **normalized, post‑resolution** representation of all
six entity types and their relationships in a multi‑table SQLite database.

This module defines:

- Core entity tables
- Relationship tables
- Geometry tables
- Provenance tables
- Conflict & uncertainty tables
- Run‑level metadata tables
- ID and key rules
- Integration points with Normalization Engine v4.0 and Entity Upsert Engine v4.0

This schema is **downstream** of:

- Discovery Protocol Module v4.0
- Discovery Output Specification v4.0
- Resolution Engine v4.0
- Normalization Engine v4.0

------------------------------------------------------------
# 1. PURPOSE

The Entity Graph Schema v4.0 provides:

- A stable, queryable representation of all normalized entities
- A normalized structure for cross‑entity relationships
- A home for geometry, provenance, conflicts, and uncertainty
- A durable backing store for TSV export and analysis

It is the **single source of truth** for:

- Sites
- Trails
- Trail Segments
- Trail Networks
- Site Networks
- Access Points
- Their relationships and provenance

------------------------------------------------------------
# 2. GLOBAL RULES

## 2.1 Primary Keys

- Every core entity table uses a **surrogate primary key**:
  - `site_id`, `trail_id`, `trail_segment_id`, `trail_network_id`, `site_network_id`, `access_point_id`
- IDs are:
  - Stable within a database
  - Opaque (no semantic meaning)
  - Assigned by the Entity Upsert Engine v4.0

## 2.2 Natural Keys

- Natural keys (e.g., name + county + governance) are used for **matching**, not as primary keys.
- Matching logic is defined in Resolution Engine v4.0, not here.

## 2.3 Foreign Keys

- All relationship tables use foreign keys referencing core entity tables.
- Foreign key constraints must be enforced.

## 2.4 Timestamps

- All core tables include:
  - `created_at`
  - `updated_at`
  - `run_id` (foreign key to `run_metadata`)

------------------------------------------------------------
# 3. CORE ENTITY TABLES

## 3.1 `sites`

Represents normalized Site entities (including child Sites).

Columns (selected, not exhaustive):

- `site_id` (PK)
- `name`
- `derived_label`
- `category`
- `subtype`
- `governance`
- `ownership`
- `access_level`
- `county_list` (semicolon‑delimited, alphabetized)
- `township`
- `municipality`
- `parent_site_id` (nullable FK to `sites.site_id`)
- `features`
- `description`
- `gps_primary`
- `plus_code`
- `source_primary`
- `created_at`
- `updated_at`
- `run_id` (FK to `run_metadata.run_id`)

## 3.2 `trails`

- `trail_id` (PK)
- `name`
- `derived_label`
- `trail_type`
- `use`
- `surface`
- `origin`
- `governance`
- `county_list`
- `length_mi`
- `gps_primary`
- `plus_code`
- `source_primary`
- `created_at`
- `updated_at`
- `run_id`

## 3.3 `trail_segments`

- `trail_segment_id` (PK)
- `trail_id` (FK to `trails.trail_id`)
- `name`
- `derived_label`
- `segment_type`
- `segment_role`
- `county_list`
- `length_mi`
- `gps_primary`
- `plus_code`
- `source_primary`
- `created_at`
- `updated_at`
- `run_id`

## 3.4 `trail_networks`

- `trail_network_id` (PK)
- `name`
- `derived_label`
- `network_type`
- `county_list`
- `governance`
- `gps_primary`
- `source_primary`
- `created_at`
- `updated_at`
- `run_id`

## 3.5 `site_networks`

- `site_network_id` (PK)
- `name`
- `derived_label`
- `network_type`
- `county_list`
- `governance`
- `gps_primary`
- `source_primary`
- `created_at`
- `updated_at`
- `run_id`

## 3.6 `access_points`

- `access_point_id` (PK)
- `name`
- `derived_label`
- `access_point_type`
- `access_level`
- `county_list`
- `address`
- `gps_primary`
- `plus_code`
- `source_primary`
- `created_at`
- `updated_at`
- `run_id`

------------------------------------------------------------
# 4. RELATIONSHIP TABLES

## 4.1 `site_parent`

Represents Site → parent Site relationships (including child Sites).

- `site_id` (FK to `sites.site_id`)
- `parent_site_id` (FK to `sites.site_id`)
- `relationship_type` (e.g., `child_site`)
- `created_at`
- `run_id`

## 4.2 `trail_to_segment`

- `trail_id` (FK to `trails.trail_id`)
- `trail_segment_id` (FK to `trail_segments.trail_segment_id`)
- `created_at`
- `run_id`

## 4.3 `trail_to_network`

- `trail_network_id` (FK to `trail_networks.trail_network_id`)
- `trail_id` (FK to `trails.trail_id`)
- `created_at`
- `run_id`

## 4.4 `site_to_network`

- `site_network_id` (FK to `site_networks.site_network_id`)
- `site_id` (FK to `sites.site_id`)
- `created_at`
- `run_id`

## 4.5 `access_point_parents`

Access Point → parent entities (multiple allowed).

- `access_point_id` (FK to `access_points.access_point_id`)
- `parent_entity_type` (`Site`, `Trail`, `Trail Segment`)
- `parent_entity_id` (FK to appropriate table)
- `created_at`
- `run_id`

------------------------------------------------------------
# 5. GEOMETRY TABLES

## 5.1 `entity_geometry`

Stores normalized geometry for any entity.

- `geometry_id` (PK)
- `entity_type` (`Site`, `Trail`, `Trail Segment`, `Trail Network`, `Site Network`, `Access Point`)
- `entity_id` (FK to appropriate table)
- `geometry_type` (`POINT`, `LINESTRING`, `POLYGON`, etc.)
- `geometry_wkt` (or `geometry_blob` if using SpatiaLite)
- `source_primary`
- `created_at`
- `updated_at`
- `run_id`

------------------------------------------------------------
# 6. PROVENANCE TABLES

## 6.1 `discovery_provenance`

- `provenance_id` (PK)
- `entity_type`
- `entity_id`
- `discovery_run_id`
- `discovery_tier`
- `discovered_in_tiers` (semicolon‑delimited)
- `raw_record_id` (if tracked)
- `source_urls`
- `source_datasets`
- `source_maps`
- `source_gis_layers`
- `parent_url`
- `recursion_depth`
- `created_at`

## 6.2 `resolution_provenance`

- `resolution_id` (PK)
- `entity_type`
- `entity_id`
- `resolution_run_id`
- `rules_applied`
- `conflicts_resolved`
- `notes`
- `created_at`

## 6.3 `normalization_provenance`

- `normalization_id` (PK)
- `entity_type`
- `entity_id`
- `normalization_run_id`
- `fields_modified`
- `vocabularies_applied`
- `formatting_corrections`
- `notes`
- `created_at`

------------------------------------------------------------
# 7. CONFLICT & UNCERTAINTY TABLES

## 7.1 `entity_conflicts`

- `conflict_id` (PK)
- `entity_type`
- `entity_id`
- `field_name`
- `conflicting_values`
- `sources`
- `resolution_status` (`unresolved`, `resolved`, `deferred`)
- `created_at`
- `updated_at`
- `run_id`

## 7.2 `entity_uncertainty`

- `uncertainty_id` (PK)
- `entity_type`
- `entity_id`
- `field_name`
- `uncertainty_reason`
- `uncertainty_level` (e.g., `low`, `medium`, `high`)
- `notes`
- `created_at`
- `run_id`

------------------------------------------------------------
# 8. RUN‑LEVEL METADATA

## 8.1 `run_metadata`

- `run_id` (PK)
- `run_type` (`discovery`, `resolution`, `normalization`, `upsert`, `tsv_export`)
- `county`
- `started_at`
- `completed_at`
- `modules_versions`
- `notes`

------------------------------------------------------------
# 9. INTEGRATION POINTS

This schema is used by:

- Normalization Engine v4.0 (writes normalized entities)
- Entity Upsert Engine v4.0 (inserts/updates rows)
- TSV Output Specifications v4.0 (read from core tables)
- TSV Integrity Check Module v4.0
- Audit & Logging Module v4.0

------------------------------------------------------------
# 10. VERSIONING

- This module is **Entity Graph Schema v4.0**.
- Any structural change requires v4.1, v4.2, etc.

------------------------------------------------------------
# END OF ENTITY GRAPH SCHEMA v4.0