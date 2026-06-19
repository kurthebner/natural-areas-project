# NATURAL AREAS PROJECT — README v5.2

A statewide, document-driven, tier-ordered system for discovering, classifying,
normalizing, relating, and exporting natural areas, parks, trails, trail
segments, networks, and access infrastructure across all 88 Ohio counties,
with a designed path to national expansion.

The Natural Areas System v5.x is fully modular, deterministic, and audit-ready.
Every rule lives in exactly one authoritative module.
Every module is versioned.
Every run is reproducible.

------------------------------------------------------------
# CORE PRINCIPLE

**Discovery = Collection. Normalization = Decisions.**

Raw data is collected during discovery exactly as found. No normalization,
vocabulary enforcement, or GPS parsing occurs during discovery. All decisions
— field selection, vocabulary mapping, GPS derivation, township and municipality
assignment — happen during normalization.

------------------------------------------------------------
# PROJECT OVERVIEW

The Natural Areas Project builds a complete, statewide dataset of:

- Natural areas
- Parks and preserves
- Sites and Child Sites (via Child Site Rules v5.x)
- Trail systems
- Trail segments
- Trail networks
- Site networks
- Visitor access points (trailheads, parking, boat launches, etc.)

The system emphasizes:

- Identity-first ontology
- Tier-ordered discovery (Federal → State → District → County → Township →
  Municipal → Conservancy → Private → Baseline)
- Governance and ecological clarity
- Public access accuracy
- Deterministic, repeatable processing
- Zero invented data
- Full auditability
- Cross-entity relationships
- Perfect TSV delimiter integrity

------------------------------------------------------------
# SYSTEM ARCHITECTURE v5.x

The system is composed of 55 authoritative modules in eight domains.

## 1. Schema Modules (6)
Define field structure, identity rules, and relationship rules for each
entity type.

`schemas/na_site_schema_v5.x.md`
`schemas/na_trail_schema_v5.x.md`
`schemas/na_trail_segment_schema_v5.x.md`
`schemas/na_access_point_schema_v5.x.md`
`schemas/na_site_network_schema_v5.x.md`
`schemas/na_trail_network_schema_v5.x.md`

## 2. Vocabulary Modules (6)
Controlled vocabularies for all vocabulary-governed fields.

`vocabularies/na_site_vocabulary_v5.x.md`
`vocabularies/na_trail_vocabulary_v5.x.md`
`vocabularies/na_trail_segment_vocabulary_v5.x.md`
`vocabularies/na_access_point_vocabulary_v5.x.md`
`vocabularies/na_site_network_vocabulary_v5.x.md`
`vocabularies/na_trail_network_vocabulary_v5.x.md`

## 3. Normalization Modules (8)
Entity-specific normalization contracts and engines.

`normalization/na_site_normalization_v5.x.md`
`normalization/na_trail_normalization_v5.x.md`
`normalization/na_trail_segment_normalization_v5.x.md`
`normalization/na_access_point_normalization_v5.x.md`
`normalization/na_site_network_normalization_v5.x.md`
`normalization/na_trail_network_normalization_v5.x.md`
`normalization/na_normalization_engine_v5.x.md`
`normalization/na_entity_upsert_engine_v5.x.md`

## 4. Discovery Modules (19)

### Core Discovery Modules (5)
`discovery/na_discovery_protocol_v5.x.md`
`discovery/na_discovery_orchestration_v5.x.md`
`discovery/na_discovery_output_spec_v5.x.md`
`discovery/na_discovery_metadata_spec_v5.x.md`
`discovery/na_gps_acquisition_v5.x.md`

### Tier Discovery Sub-Procedures (8)
Federal/Tribal, State, District, County, Township, Municipal,
Conservancy, Private

### Entity Discovery Sub-Procedures (6)
Site, Trail, Trail Segment, Trail Network, Site Network, Access Point

## 5. Output Modules (7)
TSV specifications for all six entity types plus integrity check.

`output/na_tsv_output_site_v5.x.md`
`output/na_tsv_output_trail_v5.x.md`
`output/na_tsv_output_trail_segment_v5.x.md`
`output/na_tsv_output_access_point_v5.x.md`
`output/na_tsv_output_site_network_v5.x.md`
`output/na_tsv_output_trail_network_v5.x.md`
`output/na_tsv_integrity_check_v5.x.md`

## 6. Processing Modules (5)
`processing/na_processing_orchestration_v5.x.md`  ← End-to-end pipeline
`processing/na_resolution_engine_v5.x.md`         ← Identity resolution
`processing/na_resolution_rules_v5.x.md`          ← Resolution decision rules
`processing/na_child_site_rules_v5.x.md`          ← Parent/child site rules
`processing/na_county_baseline_v5.x.md`           ← Tier-0 baseline management

## 7. Audit Module (1)
`audit/na_audit_and_logging_v5.x.md`

## 8. Root Documents
`README_v5.x.md`, `CONTRIBUTING_v5.x.md`, `na_module_manifest_v5.x.md`

------------------------------------------------------------
# KEY v5.1 CHANGES FROM v5.0

**Derived Label removed from all entities** — Derived Label is no longer
computed or stored at any stage. It is a presentation-layer concern only
and does not belong in the data architecture.

**identity_notes added to all entities** — A new normalized field for
identity clarifications, distinct from the operational notes field. Sourced
from identity_notes_raw at discovery. Used for entity boundary questions,
name conflicts, membership uncertainty, and vocabulary type flags.

**maps field simplified across all entities** — The rich array format
(url/type/description objects) has been replaced by a plain semicolon-
delimited URL list at all stages. Type and description metadata are dropped.
File extensions and domains make type obvious; the simpler format is
consistent across all entities.

**Raw field renames** — Three raw field names standardized across all entity
discovery sub-procedures:
- `notes_raw` → `identity_notes_raw` (identity clarifications)
- `url_all` → `urls_raw` (all URLs)
- `url_primary` → `url_primary_raw`

**GPS Acquisition Module added** — A new Stage 3 module between Resolution
Pass 1 and Normalization. Provides an 11-step, 5-stage workflow for acquiring
gps_lat and gps_lon for entities missing GPS coordinates. Applies to Site,
Trail, and Access Point. Does not apply to Trail Segment (LineString geometry),
Trail Network, or Site Network.

**Parent Trail Network removed from Trail and Trail Segment output** — Network
membership is managed exclusively through the trail_network_members
relationship table. Storing it in Trail and Trail Segment TSV output created
redundancy and drift risk.

------------------------------------------------------------
# KEY v5.0 CHANGES FROM v4.0

**Discovery = Collection principle formalized** — Discovery modules strictly
prohibit normalization, inference, or field decisions during collection.

**Township and Municipality are GIS-derived** — Never populated from web
sources during discovery; GIS spatial lookup occurs during normalization.

**GPS split** — `gps_primary` string field replaced by `gps_lat_raw` and
`gps_lon_raw` at discovery; normalized to `gps_lat` and `gps_lon` (numeric,
WGS84 decimal degrees).

**Access Point fields removed** — `role_raw`, `access_level_raw`, and their
normalized counterparts removed from Access Point schema.

**Network member tracking** — `member_count` + `member_site_ids` added to
Site Networks; `member_trail_count` + `member_trail_ids` added to Trail
Networks.

**County Baseline runs last** — Baseline is Tier-0 and runs after Tiers 1–8.
It provides candidate seeds, not authoritative data.

**Resolution Engine redesigned** — Detects conflicts and merges duplicates
but does not resolve conflicts. Normalization resolves conflicts.

**Resolution Rules Module added** — Extracts the entity-type and category
edge case catalog from the Resolution Engine into its own authoritative
reference.

**Skills system** — Module loading is handled by the custom skills system.

------------------------------------------------------------
# END-TO-END WORKFLOW (v5.x PIPELINE)

Each county is processed through a deterministic pipeline:

1.  Verify all v5.x modules are available
2.  Run Tiers 1–8 Discovery
3.  Load County Baseline (Tier-0)
4.  Apply Resolution Engine + Resolution Rules (Pass 1)
5.  Run GPS Acquisition for entities missing gps_lat/gps_lon
6.  Normalize all six entity types
7.  Apply Resolution Engine + Resolution Rules (Pass 2)
8.  Upsert into Entity Graph
9.  Generate six TSV files
10. Run TSV Integrity Check
11. Validate cross-entity relationships
12. Produce output bundle
13. Complete audit logs

See `processing/na_processing_orchestration_v5.x.md` for the full
pipeline specification.

------------------------------------------------------------
# RUNNING A COUNTY

The skills system handles module loading automatically. To run a county:

1. Use the `na-complete-system` skill (or start with `na-discovery-workflow`)
2. Specify the target county and state
3. Follow the 8-tier discovery sequence
4. Normalize and generate output

------------------------------------------------------------
# REPOSITORY STRUCTURE

```
natural-areas-project/
├── schemas/           (6 modules)
├── vocabularies/      (6 modules)
├── normalization/     (8 modules)
├── discovery/         (19 modules)
├── output/            (7 modules)
├── processing/        (5 modules)
├── audit/             (1 module)
├── skills/            (operational tools — not modules)
├── README_v5.x.md
├── CONTRIBUTING_v5.x.md
└── na_module_manifest_v5.x.md
```

------------------------------------------------------------
# DESIGN PRINCIPLES

- **Determinism** — same inputs → same outputs
- **Transparency** — every decision logged
- **Non-invention** — no fabricated data
- **Strict formatting** — TSVs with perfect delimiter integrity
- **Modularity** — each rule lives in exactly one place
- **Auditability** — every step traceable
- **Ontology-driven design** — identity first, amenities second
- **Tier-ordered discovery** — authoritative sources always win
- **Collection-decision separation** — discovery collects,
  normalization decides

------------------------------------------------------------
# STATUS

All 56 modules listed in the Module Manifest are active,
authoritative, and aligned with the Natural Areas System v5.x.

------------------------------------------------------------
# END OF README v5.2
