# NATURAL AREAS PROJECT
# DISCOVERY METADATA SPECIFICATION v5.2
(Authoritative Metadata Structure for Raw Discovery Layer)

Discovery Metadata is the audit backbone of the v5.x Discovery System.  
It records how each entity was discovered, where it came from, what URLs led to it, what uncertainties remain, and how the raw record fits into the enumerative + recursive discovery model.

This specification defines the required metadata fields, their structure, and their semantics for all six entity types.

This module is referenced only by:
- Discovery Protocol Module v5.x
- Discovery Orchestration Module v5.x
- All Tier Sub‑Procedures v5.x
- All Entity Discovery Sub‑Procedures v5.x

No other module may reference this specification directly.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.2

- Updated module version to v5.2
- Updated all cross‑module references to v5.x
- Added `partner_agencies_raw` to Identity Metadata (formal partners)
- Added `coordination_raw` to Identity Metadata (community/volunteer partners)
- Clarified organizational field cluster alignment with v5.2 schema
- No changes to discovery philosophy or metadata semantics

------------------------------------------------------------
# 1. PURPOSE

This specification defines:

- The metadata fields required for every Raw Discovery Record
- The structure of metadata for all six entity types
- How provenance, lineage, and recursion must be recorded
- How conflicts and uncertainties must be preserved
- How metadata integrates with the Audit & Logging Module v5.x
- How metadata is passed to the Resolution Engine v5.x

Metadata ensures that discovery is transparent, auditable, reproducible, and non‑destructive.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All entities discovered in Tiers 1–8
- All entities discovered via recursive URL propagation
- All entities seeded from Tier‑0 Baseline
- All multi‑tier discoveries
- All conflict cases
- All uncertainty cases

It governs:

- Metadata structure
- Metadata semantics
- Metadata completeness requirements
- Metadata integration with logs

------------------------------------------------------------
# 3. METADATA STRUCTURE OVERVIEW

Each Raw Discovery Record must include a **Discovery Metadata Object** containing:

1. Identity Metadata  
2. Tier Metadata  
3. Source Metadata  
4. Provenance Metadata  
5. Lineage Metadata  
6. Conflict Metadata  
7. Uncertainty Metadata  
8. Parent Metadata (Access Points only)  
9. Boundary Metadata  
10. Baseline Metadata  
11. Notes  

All fields are required unless explicitly marked optional.

------------------------------------------------------------
# 4. IDENTITY METADATA

identity:
  name_raw:
  entity_type:
  counties_raw: []
  township_raw:              # Must be blank — GIS-derived only
  municipality_raw:          # Must be blank — GIS-derived only
  parent_site_raw:
  ownership_raw:
  governance_raw:
  partner_agencies_raw:      # NEW in v5.2
  coordination_raw:          # NEW in v5.2
  features_raw:
  difficulty_raw:
  accessibility_raw:

Rules:

- `name_raw` must be preserved exactly as discovered.
- `entity_type` must be one of the six ontology types.
- `counties_raw` must list all counties exactly as discovered.
- `township_raw` and `municipality_raw` must remain blank during discovery.
- `parent_site_raw` required for child Sites.
- `ownership_raw` and `governance_raw` preserved exactly as discovered.
- `partner_agencies_raw` records formal, documented co‑operators.
- `coordination_raw` records community‑based or volunteer partners.
- `features_raw` preserved exactly as discovered.
- `difficulty_raw` and `accessibility_raw` only if explicitly stated.

------------------------------------------------------------
# 5. TIER METADATA

tiers:
  discovered_in: []
  primary_tier:

Rules:

- `discovered_in` lists all tiers where the entity appeared.
- `primary_tier` is the lowest‑numbered tier where discovered.
- Tier‑0 Baseline uses `"baseline"`.
- Access Point workflows include `"AP"`.

------------------------------------------------------------
# 6. SOURCE METADATA

sources:
  urls: []
  datasets: []
  maps: []
  gis_layers: []

Rules:

- All sources preserved exactly as discovered.
- No normalization or deduplication.
- URLs must retain tracking parameters.
- GIS layers recorded if used.

------------------------------------------------------------
# 7. PROVENANCE METADATA

provenance:
  source_url:
  parent_url:
  extraction_method:
  extraction_context:
  source_system:
  harvested_at:
  discovery_run_id:

Definitions:

- `source_url` — page where entity was discovered.
- `parent_url` — URL that led to this page during recursion.
- `extraction_method` — enumerative, recursive, or baseline.
- `source_system` — agency or domain (e.g., “ODNR”).
- `harvested_at` — ISO timestamp.
- `discovery_run_id` — unique ID for the county session.

Rules:

- Provenance must preserve the exact discovery path.
- No inference or normalization permitted.

------------------------------------------------------------
# 8. LINEAGE METADATA

lineage:
  discovery_path: []
  recursion_depth:
  recursion_allowed:
  recursion_reason:

Rules:

- `discovery_path` lists every URL from entry to final page.
- `recursion_depth` increments per propagation step.
- `recursion_allowed` indicates whether recursion was permitted.
- `recursion_reason` documents why recursion occurred.

------------------------------------------------------------
# 9. CONFLICT METADATA

conflicts:
  name_conflicts: []
  type_conflicts: []
  location_conflicts: []
  parent_conflicts: []
  governance_conflicts: []
  geometry_conflicts: []

Rules:

- Conflicts must be recorded, not resolved.
- Discovery preserves all conflicting values.

------------------------------------------------------------
# 10. UNCERTAINTY METADATA

uncertainty:
  requires_review:
  reason:
  notes:

Examples:
- “Trail name inconsistent across sources.”
- “Difficulty not explicitly stated — left blank.”
- “Municipality not determinable — left blank per v5.x rules.”

------------------------------------------------------------
# 11. PARENT METADATA (ACCESS POINTS ONLY)

parents:
  identity_parent_type:
  identity_parent_name:
  additional_sites: []
  additional_trails: []
  additional_trail_segments: []

Rules:

- `identity_parent_type` and `identity_parent_name` identify the primary parent.
- Additional parents recorded exactly as discovered.
- Site Networks and Trail Networks must not appear as parents.
- If no identity parent can be identified → requires_review = true.

------------------------------------------------------------
# 12. BOUNDARY METADATA

boundary:
  multi_county:
  counties_raw: []
  boundary_notes:

Rules:

- Multi‑county entities must be flagged.
- Discovery must never segment multi‑county entities.

------------------------------------------------------------
# 13. BASELINE METADATA

baseline:
  seeded_from_baseline:
  baseline_id:

Rules:

- `seeded_from_baseline = true` if entity originated from Tier‑0.
- `baseline_id` included if provided.

------------------------------------------------------------
# 14. NOTES

notes:
  general:
  discovery_raw:

Notes may include:
- Access limitations
- Seasonal closures
- Stewardship notes
- Raw discovery notes
- Anything not fitting structured fields

Notes must not be interpreted or normalized.

------------------------------------------------------------
# 15. COMPLETE METADATA OBJECT (TEMPLATE)

discovery_metadata:
  identity:
    name_raw:
    entity_type:
    counties_raw: []
    township_raw:
    municipality_raw:
    parent_site_raw:
    ownership_raw:
    governance_raw:
    partner_agencies_raw:
    coordination_raw:
    features_raw:
    difficulty_raw:
    accessibility_raw:
  tiers:
    discovered_in: []
    primary_tier:
  sources:
    urls: []
    datasets: []
    maps: []
    gis_layers: []
  provenance:
    source_url:
    parent_url:
    extraction_method:
    extraction_context:
    source_system:
    harvested_at:
    discovery_run_id:
  lineage:
    discovery_path: []
    recursion_depth:
    recursion_allowed:
    recursion_reason:
  conflicts:
    name_conflicts: []
    type_conflicts: []
    location_conflicts: []
    parent_conflicts: []
    governance_conflicts: []
    geometry_conflicts: []
  uncertainty:
    requires_review:
    reason:
    notes:
  parents:
    identity_parent_type:
    identity_parent_name:
    additional_sites: []
    additional_trails: []
    additional_trail_segments: []
  boundary:
    multi_county:
    counties_raw: []
    boundary_notes:
  baseline:
    seeded_from_baseline:
    baseline_id:
  notes:
    general:
    discovery_raw:

------------------------------------------------------------
# 16. INTEGRATION POINTS

This specification integrates with:

- Discovery Protocol Module v5.x
- Discovery Orchestration Module v5.x
- All Tier Sub‑Procedures v5.x
- All Entity Discovery Sub‑Procedures v5.x
- Audit & Logging Module v5.x
- Discovery Output Specification v5.x
- Resolution Engine v5.x
- County Baseline Module v5.x

No other module may reference this specification directly.

------------------------------------------------------------
# 17. MODULE DEPENDENCIES

This module depends on:

- Discovery Output Specification v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF DISCOVERY METADATA SPECIFICATION v5.2