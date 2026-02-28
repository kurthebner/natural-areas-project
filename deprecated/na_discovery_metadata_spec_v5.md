# NATURAL AREAS PROJECT
# DISCOVERY METADATA SPECIFICATION v5.0
(Authoritative Metadata Structure for Raw Discovery Layer)

Discovery Metadata is the **audit backbone** of the v5.0 Discovery System.
It records *how* each entity was discovered, *where it came from*, *what URLs led
to it*, *what uncertainties remain*, and *how the raw record fits into the
enumerative + recursive discovery model*.

This specification defines the **required metadata fields**, their structure,
and their semantics for all six entity types.

This module is referenced only by:

- Discovery Protocol Module v5.0
- Discovery Orchestration Module v5.0
- All Tier Sub-Procedures v5.0
- All Entity Discovery Sub-Procedures v5.0

No other module may reference this specification directly.

------------------------------------------------------------
# CHANGES FROM v4.0

- `access_level_raw` removed from Identity Metadata — field deleted from Access Point schema
- `features_raw` added to Identity Metadata — captures Access Point and Site amenities as discovered
- `difficulty_raw` added to Identity Metadata — for Trail and Trail Segment discovery
- `accessibility_raw` added to Identity Metadata — for Trail and Trail Segment discovery
- `township_raw` and `municipality_raw` explicitly prohibited — must remain blank; GIS-derived only
- Parent Metadata expanded: `identity_parent_type` and `identity_parent_name` added to Access Point metadata
- All version references updated to v5.0

------------------------------------------------------------
# 1. PURPOSE

This specification defines:

- The metadata fields required for every Raw Discovery Record
- The structure of metadata for all six entity types
- How provenance, lineage, and recursion must be recorded
- How conflicts and uncertainties must be preserved
- How metadata integrates with the Audit & Logging Module v5.0
- How metadata is passed to the Resolution Engine v5.0

Metadata ensures that discovery is **transparent, auditable, reproducible, and
non-destructive**.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All entities discovered in Tiers 1–8
- All entities discovered via recursive URL propagation
- All entities seeded from Tier-0 Baseline
- All multi-tier discoveries
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

1. **Identity Metadata**
2. **Tier Metadata**
3. **Source Metadata**
4. **Provenance Metadata**
5. **Lineage Metadata**
6. **Conflict Metadata**
7. **Uncertainty Metadata**
8. **Parent Metadata** (Access Points only)
9. **Boundary Metadata**
10. **Baseline Metadata**
11. **Notes**

All fields are required unless explicitly marked optional.

------------------------------------------------------------
# 4. IDENTITY METADATA

identity:
  name_raw: (string, required)
  entity_type: (one of 6 ontology types, required)
  counties_raw: [list of counties, required]
  township_raw: (must be blank — GIS-derived only)
  municipality_raw: (must be blank — GIS-derived only)
  parent_site_raw: (string, optional — required for child Sites)
  features_raw: (string, optional — Access Points and Sites)
  difficulty_raw: (string, optional — Trails and Trail Segments only)
  accessibility_raw: (string, optional — Trails and Trail Segments only)

Rules:

- `name_raw` must be preserved exactly as discovered.
- `entity_type` must be one of:
  - Site
  - Trail
  - Trail Segment
  - Trail Network
  - Site Network
  - Access Point
- `counties_raw` must list **all counties exactly as discovered**, with no normalization.
- `township_raw` must always be blank during discovery. Must never be populated
  from web sources. Populated via GIS spatial lookup during normalization.
- `municipality_raw` must always be blank during discovery. Must never be populated
  from web sources. Populated via GIS spatial lookup during normalization.
- `parent_site_raw` is required for child Sites; optional elsewhere.
- `features_raw` is for facilities and amenities as discovered — preserve exactly,
  do not normalize or categorize.
- `difficulty_raw` must only be populated if explicitly stated by an authoritative
  source. Must never be assessed or inferred.
- `accessibility_raw` must only be populated if explicitly stated by an authoritative
  source. Must never be inferred from surface type or other characteristics.

------------------------------------------------------------
# 5. TIER METADATA

tiers:
  discovered_in: [list of tier identifiers, required]
  primary_tier: (tier identifier, required)

Rules:

- `discovered_in` lists all tiers where the entity appeared.
- `primary_tier` is the **lowest-numbered tier** where the entity was discovered.
- Tier-0 Baseline uses `"baseline"` as its identifier.
- Access Point-specific workflows use `"AP"` as a supplemental identifier.

------------------------------------------------------------
# 6. SOURCE METADATA

sources:
  urls: [list of URLs, required if available]
  datasets: [list of dataset names, optional]
  maps: [list of map names or identifiers, optional]
  gis_layers: [list of GIS layers, optional]

Rules:

- All sources must be preserved exactly as discovered.
- No source may be discarded.
- URLs must be stored exactly as discovered — no normalization, no tracking parameter removal.
  (Tracking parameter removal is a Normalization decision.)
- GIS layers must be recorded if used.

------------------------------------------------------------
# 7. PROVENANCE METADATA

provenance:
  source_url: (string, required)
  parent_url: (string, optional)
  extraction_method: (enum: "enumerative" | "recursive" | "baseline", required)
  extraction_context: (string, optional)
  source_system: (string, required)
  harvested_at: (ISO timestamp, required)
  discovery_run_id: (string, required)

Definitions:

- **source_url** — the URL of the page where the entity was discovered.
- **parent_url** — the URL that led to this page during recursive discovery.
  Blank for enumerative discovery.
- **extraction_method** — how the entity was surfaced:
  - `enumerative` — from listing/index pages
  - `recursive` — from URL propagation
  - `baseline` — from Tier-0 baseline
- **source_system** — the system or domain (e.g., "ODNR", "Wood County Park District").
- **harvested_at** — ISO 8601 timestamp of extraction.
- **discovery_run_id** — unique ID for the discovery run. Used to correlate all
  records from a single county discovery session.

Rules:

- Provenance must preserve the **exact discovery path**.
- No inference or normalization is permitted.
- `discovery_run_id` must be generated at the start of each county session and
  applied to all records produced in that session.

------------------------------------------------------------
# 8. LINEAGE METADATA

lineage:
  discovery_path: [list of URLs, required]
  recursion_depth: (integer, required)
  recursion_allowed: (boolean, required)
  recursion_reason: (string, optional)

Rules:

- `discovery_path` must list every URL from the entry point to the final page.
- `recursion_depth` increments with each propagation step. Enumerative discovery
  sets this to 0.
- `recursion_allowed` indicates whether recursion was permitted for this domain.
- `recursion_reason` documents why recursion occurred (e.g., "internal links
  allowed per tier sub-procedure").

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
- Resolution Engine v5.0 resolves conflicts downstream.
- Discovery must preserve all conflicting values exactly as discovered.
- No conflict may be silently discarded.

------------------------------------------------------------
# 10. UNCERTAINTY METADATA

uncertainty:
  requires_review: (boolean, required)
  reason: (string, optional)
  notes: (string, optional)

Examples:

- "Access Point appears on map but not in text."
- "Trail name inconsistent across sources."
- "Segment boundary unclear; GIS conflict."
- "Difficulty not explicitly stated — left blank."
- "Municipality not determinable from web sources — left blank per v5.0 rules."

------------------------------------------------------------
# 11. PARENT METADATA (ACCESS POINTS ONLY)

parents:
  identity_parent_type: (one of: Site, Trail, Trail Segment — required)
  identity_parent_name: (string, required — exact name as discovered)
  additional_sites: [list of Site names, optional]
  additional_trails: [list of Trail names, optional]
  additional_trail_segments: [list of Trail Segment names, optional]

Rules:

- `identity_parent_type` and `identity_parent_name` identify the single
  identity-defining parent — the entity that gives the Access Point its primary
  navigational purpose.
- `additional_sites`, `additional_trails`, `additional_trail_segments` record
  any additional parent relationships discovered.
- All parent values must be preserved **exactly as discovered** — no normalization,
  no ID resolution. Resolution Engine resolves names to IDs downstream.
- Site Networks and Trail Networks must **not** appear as parents.
- If no identity parent can be identified:
  - `identity_parent_type` and `identity_parent_name` are blank
  - `uncertainty.requires_review = true`

------------------------------------------------------------
# 12. BOUNDARY METADATA

boundary:
  multi_county: (boolean, required)
  counties_raw: [list of counties, required]
  boundary_notes: (string, optional)

Rules:

- Multi-county entities must be flagged.
- Discovery must **never segment** multi-county entities.
- All counties must be recorded exactly as discovered.
- Normalization alphabetizes and formats the county list later.

------------------------------------------------------------
# 13. BASELINE METADATA

baseline:
  seeded_from_baseline: (boolean, required)
  baseline_id: (string, optional)

Rules:

- If the entity originated from Tier-0 Baseline → `seeded_from_baseline = true`.
- If discovered independently → `seeded_from_baseline = false`.
- Baseline ID is included if available from the operator-provided spreadsheet.

------------------------------------------------------------
# 14. NOTES

notes:
  general: (string, optional)
  discovery_raw: (string, optional)

Notes may include:

- Access limitations
- Seasonal closures
- Co-management details
- Stewardship notes
- Trail system integration notes
- Raw discovery notes from tier modules
- Anything that does not fit the structured fields above

Notes must not be interpreted, normalized, or used for inference.

------------------------------------------------------------
# 15. COMPLETE METADATA OBJECT (TEMPLATE)

discovery_metadata:
  identity:
    name_raw:
    entity_type:
    counties_raw: []
    township_raw:              # Must be blank — GIS-derived only
    municipality_raw:          # Must be blank — GIS-derived only
    parent_site_raw:
    features_raw:              # NEW in v5.0
    difficulty_raw:            # NEW in v5.0 — Trails and Trail Segments only
    accessibility_raw:         # NEW in v5.0 — Trails and Trail Segments only
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
  parents:                     # Access Points only
    identity_parent_type:      # NEW in v5.0
    identity_parent_name:      # NEW in v5.0
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

- Discovery Protocol Module v5.0
- Discovery Orchestration Module v5.0
- All Tier Sub-Procedures v5.0
- All Entity Discovery Sub-Procedures v5.0
- Audit & Logging Module v5.0
- Discovery Output Specification v5.0
- Resolution Engine v5.0
- County Baseline Module v5.0

No other module may reference this specification directly.

------------------------------------------------------------
# 17. MODULE DEPENDENCIES

This module depends on:

- Discovery Output Specification v5.0
- Audit & Logging Module v5.0

------------------------------------------------------------
# END OF DISCOVERY METADATA SPECIFICATION v5.0
