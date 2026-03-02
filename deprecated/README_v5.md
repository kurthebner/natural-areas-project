# NATURAL AREAS PROJECT — README v5.0

A statewide, document-driven, tier-ordered system for discovering, classifying,
normalizing, relating, and exporting natural areas, parks, trails, trail
segments, networks, and access infrastructure across all 88 Ohio counties,
with a designed path to national expansion.

The Natural Areas System v5.0 is fully modular, deterministic, and audit-ready.
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
- Sites and Child Sites (via Child Site Rules v5.0)
- Trail systems
- Trail segments
- Trail networks
- Site networks
- Visitor access points (trailheads, parking, boat launches, etc.)

The system emphasizes:

- Identity-first ontology
- Tier-ordered discovery (Federal → State → District → County → Township → Municipal → Conservancy → Private → Baseline)
- Governance and ecological clarity
- Public access accuracy
- Deterministic, repeatable processing
- Zero invented data
- Full auditability
- Cross-entity relationships
- Perfect TSV delimiter integrity

------------------------------------------------------------
# SYSTEM ARCHITECTURE v5.0

The system is composed of 55 authoritative modules in nine domains.

## 1. Schema Modules (6)
Define field structure, identity rules, and relationship rules for each entity type.

`schemas/na_site_schema_v5.md`
`schemas/na_access_point_schema_v5.md`
`schemas/na_trail_schema_v5.md`
`schemas/na_trail_segment_schema_v5.md`
`schemas/na_trail_network_schema_v5.md`
`schemas/na_site_network_schema_v5.md`

## 2. Vocabulary Modules (6)
Controlled vocabularies for all vocabulary-governed fields.

`vocabularies/na_site_vocabulary_v5.md`
`vocabularies/na_access_point_vocabulary_v5.md`
`vocabularies/na_trail_vocabulary_v5.md`
`vocabularies/na_trail_segment_vocabulary_v5.md`
`vocabularies/na_trail_network_vocabulary_v5.md`
`vocabularies/na_site_network_vocabulary_v5.md`

## 3. Normalization Modules (8)
Entity-specific normalization contracts and engines.

`normalization/na_normalization_engine_v5.md`
`normalization/na_entity_upsert_engine_v5.md`
`normalization/na_site_normalization_v5.md`
`normalization/na_access_point_normalization_v5.md`
`normalization/na_trail_normalization_v5.md`
`normalization/na_trail_segment_normalization_v5.md`
`normalization/na_trail_network_normalization_v5.md`
`normalization/na_site_network_normalization_v5.md`

## 4. Discovery System (19 modules)

### Wrapper Modules (5)
`discovery/na_discovery_protocol_v5.md`
`discovery/na_discovery_metadata_spec_v5.md`
`discovery/na_discovery_output_spec_v5.md`
`discovery/na_discovery_orchestration_v5.md`
`discovery/na_resolution_engine_v5.md`

### Jurisdictional Discovery Sub-Procedures (8)
Federal/Tribal, State, District, County, Township, Municipal, Conservancy, Private

### Entity Discovery Sub-Procedures (6)
Site, Trail, Trail Segment, Trail Network, Site Network, Access Point

## 5. Output Modules (7)
TSV specifications for all six entity types plus integrity check.

`output/na_tsv_output_[entity]_v5.md` × 6
`output/na_tsv_integrity_check_v5.md`

## 6. Processing & Logic Modules (4)
`processing/na_processing_v5.md`        ← End-to-end pipeline orchestration
`processing/na_resolution_rules_v5.md`  ← Entity-type and category decision rules
`processing/na_county_baseline_v5.md`   ← Tier-0 baseline management
`processing/na_child_site_rules_v5.md`  ← Parent/child site assignment rules

## 7. Audit Module (1)
`audit/na_audit_and_logging_v5.md`

## 8. Best Practices (1)
`best-practices/improved_discovery_methodology.md`

## 9. Project Documents + Manifest
`README_v5.md`, `CONTRIBUTING_v5.md`, `na_module_manifest_v5.md`

------------------------------------------------------------
# KEY v5.0 CHANGES FROM v4.0

**Discovery = Collection principle formalized** — discovery modules now strictly
prohibit any normalization, inference, or field decisions during collection.

**Township and Municipality are GIS-derived** — never populated from web sources
during discovery; GIS spatial lookup occurs during normalization.

**GPS split** — `gps_primary` string field replaced by `gps_lat` + `gps_lon`
numeric fields (WGS84 decimal degrees).

**New raw fields** — `features_raw`, `difficulty_raw`, `accessibility_raw`,
`maps_raw` added for Trails, Trail Segments, Trail Networks, and/or Access Points.

**Access Point fields removed** — `role_raw`, `access_level_raw`, and their
normalized counterparts removed from Access Point schema.

**Network member tracking** — `member_count` + `member_site_ids` added to Site
Networks; `member_trail_count` + `member_trail_ids` added to Trail Networks.

**Trail Segment type** — `segment_type` added as optional field.

**County Baseline runs last** — Baseline is Tier-0 and runs after Tiers 1–8,
not before. It provides candidate seeds, not authoritative data.

**Resolution Engine redesigned** — Resolution detects conflicts and merges
duplicates but does not resolve conflicts. Normalization resolves conflicts.

**Resolution Rules Module added** — New module extracts the entity-type and
category edge case catalog from the v4.0 Resolution Module into its own
authoritative reference.

**Skills system replaces bootstrap** — Module loading is handled by the custom
skills system; the v4.0 bootstrap upload sequence is retired.

------------------------------------------------------------
# END-TO-END WORKFLOW (v5.0 TIERED PIPELINE)

Each county is processed through a deterministic pipeline:

1. Verify all v5.0 modules available
2. Run Tiers 1–8 Discovery
3. Load County Baseline (Tier-0)
4. Apply Resolution Engine + Resolution Rules
5. Normalize all six entity types
6. Upsert into entity graph
7. Generate six TSV files
8. Run TSV Integrity Check
9. Validate cross-entity relationships
10. Produce output bundle
11. Complete audit logs

See `processing/na_processing_v5.md` for the full pipeline specification.

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
├── processing/        (4 modules)
├── audit/             (1 module)
├── best-practices/    (1 module)
├── README_v5.md
├── CONTRIBUTING_v5.md
└── na_module_manifest_v5.md
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
- **Collection-decision separation** — discovery collects, normalization decides

------------------------------------------------------------
# STATUS

All 55 modules listed in the Module Manifest v5.0 are active, authoritative,
and aligned with the Natural Areas System v5.0.

------------------------------------------------------------
# END OF README v5.0
