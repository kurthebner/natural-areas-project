# NATURAL AREAS PROJECT
# PROCESSING ORCHESTRATION MODULE v5.0
(Authoritative End-to-End Execution Pipeline)

This module defines the authoritative, deterministic, multi-stage processing
pipeline for transforming county-scoped discovery outputs into fully resolved,
normalized, audit-ready datasets for all six entity types:

- Site
- Trail
- Trail Segment
- Trail Network
- Site Network
- Access Point

Child Sites are represented as Sites with a `parent_site_id` value, governed
by the Child Site Rules Module v5.0.

This module contains no controlled vocabularies.
All vocabularies are defined in the respective Vocabulary Modules v5.0.

------------------------------------------------------------
# CHANGES FROM v4.0

- `county_list` → `counties` field name throughout
- `managing_agency` → `governance` field name throughout
- `access_level` and `role` removed from Access Point normalization stage
- `gps_primary` split into `gps_lat` + `gps_lon` noted in Stage 4
- `township` and `municipality` now GIS-derived in Stage 4, never from discovery
- County Baseline (Tier-0) now runs AFTER tiers 1–8, not before
- Stage 0 updated to v5.0 module list
- Resolution Engine v5.0 philosophy noted: detect conflicts, don't resolve them
- Resolution Rules Module v5.0 added as dependency
- All version references updated to v5.0

------------------------------------------------------------
# 1. PURPOSE

The Processing Orchestration Module v5.0 defines:

- The full end-to-end processing pipeline
- The order in which modules execute
- How raw discovery outputs flow through Resolution and Normalization
- How conflicts are surfaced, preserved, and resolved
- How final TSV outputs are produced, validated, and packaged
- How audit logs and provenance are generated
- How deterministic, reproducible processing is enforced

This module ensures:

- Deterministic execution
- Zero skipped steps
- Zero improvisation
- Strict alignment across all v5.0 modules
- Full delimiter-integrity compliance
- Full auditability
- Full preservation of raw discovery values

------------------------------------------------------------
# 2. CORE PRINCIPLE

**Discovery = Collection. Normalization = Decisions.**

Raw discovery values are preserved exactly as found. No normalization, no
vocabulary enforcement, no GPS parsing, no township or municipality derivation
occurs during discovery. All decisions happen in Stages 3 and 4.

------------------------------------------------------------
# 3. MODULE HIERARCHY AND AUTHORITY

The following hierarchy governs all processing:

1. Schema Modules v5.0 (all six)
2. Vocabulary Modules v5.0 (all six)
3. County Baseline Module v5.0
4. Discovery Protocol Module v5.0
5. Discovery Orchestration Module v5.0
6. Resolution Engine v5.0
7. Resolution Rules Module v5.0
8. Normalization Engine v5.0 (all six entity types)
9. Entity Upsert Engine v5.0
10. TSV Output Specifications v5.0 (all six)
11. TSV Integrity Check Module v5.0
12. Audit & Logging Module v5.0

Authority rules:

- Schema defines ontology and field definitions
- Baseline provides Tier-0 identity seeds
- Discovery expands the candidate list (raw, unnormalized)
- Resolution detects conflicts and merges duplicates
- Resolution Rules determines entity type and category in ambiguous cases
- Normalization makes all field decisions and applies vocabulary
- Entity Upsert writes entities into the entity graph
- TSV Output serializes each entity type
- TSV Integrity Check overrides TSV Output on format issues
- Audit & Logging records all actions

If modules conflict:
- Resolution Engine overrides Discovery on identity questions
- Resolution Rules override all other modules on entity-type and category questions
- Schema overrides all modules except Resolution Rules
- Normalization Engine overrides Baseline formatting but not Baseline identity
- TSV Integrity Check overrides TSV Output

------------------------------------------------------------
# 4. END-TO-END PROCESSING PIPELINE

The pipeline consists of ten deterministic stages, applied to all six entity types.

------------------------------------------------------------
# STAGE 0 — MODULE AVAILABILITY CHECK

Before any county processing begins, verify all required v5.0 modules are available.

### 0.1 Required modules

- All six Schema Modules v5.0
- All six Vocabulary Modules v5.0
- All six Normalization Modules v5.0
- Discovery Protocol Module v5.0
- Discovery Orchestration Module v5.0
- Resolution Engine v5.0
- Resolution Rules Module v5.0
- County Baseline Module v5.0
- Child Site Rules Module v5.0
- Entity Upsert Engine v5.0
- TSV Output Specifications v5.0 (all six)
- TSV Integrity Check Module v5.0
- Audit & Logging Module v5.0

### 0.2 If any module is missing
- Halt processing
- Report which module is missing
- Do not proceed until resolved

**Output:** Verified v5.0 module environment.

------------------------------------------------------------
# STAGE 1 — RUN DISCOVERY ORCHESTRATION (TIERS 1–8)

Discovery runs first. Baseline loads after discovery is complete (Stage 2).

### 1.1 Execute tiers in order
Tier 1 (Federal/Tribal) → Tier 2 (State) → Tier 3 (District) →
Tier 4 (County) → Tier 5 (Township) → Tier 6 (Municipal) →
Tier 7 (Conservancy) → Tier 8 (Private)

Complete each tier 100% before advancing to the next.

### 1.2 Discovery rules (strictly enforced)
- No normalization during discovery
- No invention
- No inference
- No silent correction
- `township` and `municipality` must not be populated — GIS-derived only
- All values captured as `_raw` fields

### 1.3 For each tier, execute entity discovery
Sites → Trails → Trail Segments → Trail Networks → Site Networks → Access Points

### 1.4 Preserve all raw values exactly as found
### 1.5 Record source URL, discovery tier, and discovery date for every entity

**Output:** Raw Discovery Layer (all six entity types across all 8 tiers).

------------------------------------------------------------
# STAGE 2 — LOAD COUNTY BASELINE (TIER-0)

Baseline loads after discovery is complete. It provides Tier-0 candidate seeds.

### 2.1 Load all baseline rows exactly as written
### 2.2 Mark all entries `seeded_from_baseline = true`
### 2.3 Assign a `baseline_id` per row
### 2.4 Preserve all raw field values
### 2.5 Do not populate `township` or `municipality` from baseline values
### 2.6 Log any baseline anomalies (township/municipality value attempts, etc.)

Baseline is the lowest-authority source. It never overrides Tiers 1–8.

**Output:** Baseline identity seed list (raw, unnormalized).

------------------------------------------------------------
# STAGE 3 — APPLY RESOLUTION ENGINE

Resolution receives raw discovery entities (Tiers 1–8) plus baseline seeds (Tier-0).

### 3.1 Group candidate entities
Group raw records that likely represent the same real-world entity using
entity-specific identity anchors (see Resolution Engine v5.0).

### 3.2 Match and merge
- Merge complementary information across sources
- Detect conflicts (different values for same field from different tiers)
- Preserve all conflicting values — do not choose between them
- Flag conflicts for normalization to resolve

### 3.3 Resolve entity type and category ambiguity
Apply Resolution Rules Module v5.0 for any ambiguous entity-type or
category decisions.

### 3.4 Resolve parent relationships
- Match parent names to IDs where possible
- Create placeholder entities for parents not yet discovered
- See Resolution Engine v5.0 Section 14

### 3.5 Match baseline seeds to discovered entities
- Matched baseline entries become supporting claims
- Unmatched baseline entries become low-confidence candidates
- All conflicts are logged

### 3.6 Surface unresolved conflicts for normalization review

**Output:** Resolved Entity Layer (six entity types, conflict-aware, with provenance).

------------------------------------------------------------
# STAGE 4 — NORMALIZATION ENGINE (ENTITY-SPECIFIC)

Normalization is where all decisions are made. Applied separately per entity type.

### 4A — Normalize Sites
### 4B — Normalize Trails
### 4C — Normalize Trail Segments
### 4D — Normalize Trail Networks
### 4E — Normalize Site Networks
### 4F — Normalize Access Points

Each normalization step includes:

- Vocabulary validation and enforcement
- Formatting validation
- GPS parsing: `gps_primary` string → `gps_lat` + `gps_lon` (numeric, WGS84)
- Plus Code computation from `gps_lat` + `gps_lon`
- GIS spatial lookup: derive `township` and `municipality` (never from raw sources)
- Conflict resolution: choose canonical values using tier authority rules
- Derived Label computation
- `counties` normalization (semicolon-delimited, alphabetized)
- Parent/child validation (Child Site Rules Module v5.0)
- Governance field normalization
- Network member count and ID population

**Output:** Six fully normalized datasets.

------------------------------------------------------------
# STAGE 5 — ENTITY UPSERT ENGINE

### 5.1 Insert or update entities in the entity graph
### 5.2 Maintain entity IDs across runs
### 5.3 Maintain relationship tables (network membership, parent/child)
### 5.4 Maintain provenance tables
### 5.5 Maintain conflict and uncertainty tables

**Output:** Updated entity graph.

------------------------------------------------------------
# STAGE 6 — GENERATE TSV OUTPUT

### 6.1 Assemble records in exact field order per TSV specification
### 6.2 Apply format rules
- Tab-separated values
- UTF-8 encoding
- Empty string for NULL values (not "NULL", not blank-with-space)
- No embedded tabs in field content
- No embedded newlines in field content
- Arrays serialized as semicolon-delimited strings

### 6.3 Generate six files
- Sites.tsv
- Trails.tsv
- Trail_Segments.tsv
- Access_Points.tsv
- Trail_Networks.tsv
- Site_Networks.tsv

**Output:** Six TSV datasets.

------------------------------------------------------------
# STAGE 7 — TSV INTEGRITY CHECK

### 7.1 Validate delimiter count per row
### 7.2 Validate blank-field representation
### 7.3 Validate field alignment (no shifted columns)
### 7.4 Validate Derived Label placement
### 7.5 Validate integrity-anchor placement
### 7.6 Validate multi-county formatting (semicolon-delimited, alphabetized)
### 7.7 Surface anomalies
### 7.8 Halt finalization if integrity fails

**Output:** Delimiter-validated TSV datasets.

------------------------------------------------------------
# STAGE 8 — RELATIONSHIP VALIDATION (CROSS-ENTITY)

### 8.1 Validate
- Site → Parent Site (parent_site_id references existing Site)
- Trail → Trail Segment (segment parent_trail_id references existing Trail)
- Trail → Trail Network (trail_network_members references existing Trail Network)
- Site → Site Network (site_network_members references existing Site Network)
- Access Point → Site / Trail / Segment (identity_parent references existing entity)

### 8.2 Surface relationship anomalies (orphaned references, missing parents)

**Output:** Relationship-validated datasets.

------------------------------------------------------------
# STAGE 9 — FINAL OUTPUT BUNDLE

### 9.1 Package all six TSVs
### 9.2 Package audit log
### 9.3 Package metadata (module versions, timestamps, session ID)
### 9.4 Package discovery summary (tier results, entity counts)

**Output:** County Output Bundle v5.0.

------------------------------------------------------------
# STAGE 10 — LOGGING & AUDIT TRAIL

### 10.1 Discovery Log records
- All tiers executed
- All sources fetched
- All entities found per tier
- All negative findings with evidence

### 10.2 Normalization Log records (separate from Discovery Log)
- All field decisions
- All vocabulary mappings
- All conflict resolutions with rationale
- All GIS derivations (township, municipality)
- All GPS parsing results

### 10.3 Resolution Log records
- All merge decisions
- All conflicts detected
- All entity-type determinations
- All parent resolutions

### 10.4 Metadata records
- Module versions
- Session ID
- Timestamps
- County baseline version
- Discovery run ID

**Output:** Complete, separated audit logs for the county processing run.

------------------------------------------------------------
# 5. PIPELINE SUMMARY

1. Verify all v5.0 modules available (Stage 0)
2. Run tiers 1–8 discovery (Stage 1)
3. Load county baseline as Tier-0 (Stage 2)
4. Apply Resolution Engine (Stage 3)
5. Normalize all six entity types (Stage 4)
6. Upsert into entity graph (Stage 5)
7. Generate six TSVs (Stage 6)
8. Run TSV Integrity Check (Stage 7)
9. Validate cross-entity relationships (Stage 8)
10. Package output bundle (Stage 9)
11. Complete audit logs (Stage 10)

------------------------------------------------------------
# 6. MODULE DEPENDENCIES

This module depends on:

- All six Schema Modules v5.0
- All six Vocabulary Modules v5.0
- All six Normalization Modules v5.0
- Discovery Protocol Module v5.0
- Discovery Orchestration Module v5.0
- Resolution Engine v5.0
- Resolution Rules Module v5.0
- County Baseline Module v5.0
- Child Site Rules Module v5.0
- Entity Upsert Engine v5.0
- TSV Output Specifications v5.0 (all six)
- TSV Integrity Check Module v5.0
- Audit & Logging Module v5.0

------------------------------------------------------------
# END OF PROCESSING ORCHESTRATION MODULE v5.0
