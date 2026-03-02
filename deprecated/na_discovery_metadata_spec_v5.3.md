# NATURAL AREAS PROJECT
# DISCOVERY METADATA SPECIFICATION v5.3
Authoritative Metadata Structure for Raw Discovery Layer

Discovery Metadata is the audit backbone of the v5.2 Discovery System. It records how each entity was discovered, where it came from, what URLs led to it, what uncertainties remain, and how the raw record fits into the enumerative and recursive discovery model.

This specification defines the required metadata fields, their structure, and their semantics for all six entity types.

This module is referenced only by:

- Discovery Protocol Module v5.x
- Discovery Orchestration Module v5.x
- All Tier Sub-Procedures v5.x
- All Entity Discovery Sub-Procedures v5.x

No other module may reference this specification directly.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.3

- Updated all module references to v5.x.
- Added Organizational Metadata block:
  - ownership_raw
  - governance_raw
  - partner_agencies_raw
  - coordination_raw
- Added Raw Field Preservation section, grouped by entity type and alphabetized within each group.
- Updated Identity Metadata to align with Site Schema v5.2.
- Updated Provenance and Lineage semantics to match v5.2 recursion rules.
- Expanded Conflict Metadata to include partner_agencies_conflicts and geometry_conflicts.
- Updated Uncertainty Metadata rules for v5.2.
- Updated Parent Metadata rules for Access Points.
- Updated Baseline Metadata for v5.2 Tier‑0 integration.
- Added explicit prohibitions for GIS-derived fields during discovery.
- Added placeholders for non‑Site entity types pending schema review.

------------------------------------------------------------
# 1. PURPOSE

This specification defines:

- The metadata fields required for every Raw Discovery Record v5.2
- The structure of metadata for all six entity types
- How provenance, lineage, and recursion must be recorded
- How conflicts and uncertainties must be preserved
- How metadata integrates with the Audit & Logging Module v5.x
- How metadata is passed to the Resolution Engine v5.x

Metadata ensures that discovery is transparent, auditable, reproducible, and non-destructive.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All entities discovered in Tiers 1–8
- All entities discovered via recursive URL propagation
- All entities seeded from Tier‑0 Baseline
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

Each Raw Discovery Record v5.2 must include a Discovery Metadata Object containing:

1. Identity Metadata  
2. Organizational Metadata  
3. Tier Metadata  
4. Source Metadata  
5. Provenance Metadata  
6. Lineage Metadata  
7. Conflict Metadata  
8. Uncertainty Metadata  
9. Parent Metadata (Access Points only)  
10. Boundary Metadata  
11. Baseline Metadata  
12. Raw Field Preservation Rules  
13. Notes  

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
  category_raw: (string, optional — Sites only)
  subtype_raw: (string, optional — Sites only)
  designation_raw: (string, optional — Sites only)
  status_raw: (string, optional — Sites only)
  description_raw: (string, optional — Sites only)
  location_raw: (string, optional — Sites only)
  acres_raw: (string or numeric, optional — Sites only)
  gps_lat_raw: (numeric, optional — discovery-populated when available)
  gps_lon_raw: (numeric, optional — discovery-populated when available)
  features_raw: (string, optional — Sites and Access Points)
  difficulty_raw: (string, optional — Trails and Trail Segments only)
  accessibility_raw: (string, optional — Trails and Trail Segments only)
  url_primary_raw: (string, optional)
  urls_raw: [list of URLs, optional]
  notes_raw: (string, optional)

Rules:

- name_raw must be preserved exactly as discovered.
- entity_type must be one of:
  - Site
  - Trail
  - Trail Segment
  - Trail Network
  - Site Network
  - Access Point
- counties_raw must list all counties exactly as discovered, with no normalization.
- township_raw and municipality_raw must always be blank during discovery. These fields are GIS-derived only.
- parent_site_raw is required for child Sites; optional elsewhere.
- category_raw, subtype_raw, designation_raw, and status_raw must be preserved exactly as discovered. No normalization or vocabulary matching occurs during discovery.
- description_raw must be preserved exactly as discovered. No summarization or rewriting is permitted.
- location_raw must be preserved exactly as discovered. No GIS substitution or inference is permitted.
- acres_raw must be preserved exactly as discovered, including malformed or ambiguous values.
- gps_lat_raw and gps_lon_raw may be populated only when explicitly provided by authoritative sources. No inference or derivation is permitted.
- features_raw must be preserved exactly as discovered. No categorization or vocabulary matching occurs during discovery.
- difficulty_raw and accessibility_raw must only be populated if explicitly stated by an authoritative source. No inference is permitted.
- url_primary_raw and urls_raw must be preserved exactly as discovered, including tracking parameters.
- notes_raw must be preserved exactly as discovered. No interpretation or normalization is permitted.

------------------------------------------------------------
# 5. ORGANIZATIONAL METADATA

organizational:
  ownership_raw: (string, optional)
  governance_raw: (string, optional)
  partner_agencies_raw: (string, optional)
  coordination_raw: (string, optional)

Rules:

- All organizational fields must be preserved exactly as discovered.
- No normalization, no inference, and no deduplication are permitted.
- ownership_raw represents legal title only.
- governance_raw represents operational control only.
- partner_agencies_raw represents formal, documented co‑operator organizations.
- coordination_raw represents informal, community-based, or volunteer partners.
- partner_agencies_raw must not duplicate ownership_raw or governance_raw.
- All organizational fields may appear for any entity type if discovered.
- Conflicts must be recorded in the Conflict Metadata block.
- Organizational fields must never be inferred from context, logos, or implied relationships.

------------------------------------------------------------
# 6. TIER METADATA

tiers:
  discovered_in: [list of tier identifiers, required]
  primary_tier: (tier identifier, required)

Rules:

- discovered_in lists all tiers where the entity appeared.
- primary_tier is the lowest-numbered tier where the entity was discovered.
- Tier‑0 Baseline uses "baseline" as its identifier.
- Access Point-specific workflows may add "AP" as a supplemental identifier.
- Tier metadata must reflect the actual discovery workflow, not inferred or corrected values.

------------------------------------------------------------
# 7. SOURCE METADATA

sources:
  urls: [list of URLs, required if available]
  datasets: [list of dataset names, optional]
  maps: [list of map names or identifiers, optional]
  gis_layers: [list of GIS layers, optional]

Rules:

- All sources must be preserved exactly as discovered.
- No source may be discarded.
- URLs must be stored exactly as discovered — no normalization, no tracking parameter removal.
- GIS layers must be recorded if used.
- Dataset and map names must be preserved exactly as discovered.

------------------------------------------------------------
# 8. PROVENANCE METADATA

provenance:
  parent_url: (string, optional)
  discovery_path: [list of URLs, required]
  extraction_method: (string, required)
  harvested_at: (timestamp, required)
  discovery_run_id: (string, required)

Rules:

- parent_url records the URL from which this entity was discovered during recursive propagation.
- discovery_path records the full ordered chain of URLs that led to the entity.
- extraction_method must be one of:
  - "enumerative"
  - "recursive"
  - "baseline"
  - "manual"
- harvested_at must reflect the actual timestamp of extraction.
- discovery_run_id must uniquely identify the discovery run.
- No URL in discovery_path may be removed, normalized, or rewritten.
- parent_url must be blank for Tier‑0 Baseline entities.
- extraction_method must reflect the actual workflow, not inferred or corrected values.

------------------------------------------------------------
# 9. LINEAGE METADATA

lineage:
  parent_entity_id: (string or null)
  parent_entity_type: (string or null)
  lineage_notes: (string, optional)

Rules:

- lineage metadata records hierarchical relationships discovered during recursive propagation.
- parent_entity_id must reference the raw identifier discovered during extraction, not the normalized site_id.
- parent_entity_type must be one of the six ontology types.
- lineage_notes may record ambiguous or conflicting lineage information.
- Lineage must not be inferred from URL structure alone.
- Lineage must not be inferred from naming conventions.
- Lineage must not be inferred from GIS boundaries.

------------------------------------------------------------
# 10. CONFLICT METADATA

conflicts:
  name_conflicts: [list of conflicting names]
  counties_conflicts: [list of conflicting county lists]
  category_conflicts: [list of conflicting categories]
  subtype_conflicts: [list of conflicting subtypes]
  designation_conflicts: [list of conflicting designations]
  status_conflicts: [list of conflicting statuses]
  ownership_conflicts: [list of conflicting ownership values]
  governance_conflicts: [list of conflicting governance values]
  partner_agencies_conflicts: [list of conflicting partner agency lists]
  coordination_conflicts: [list of conflicting coordination values]
  acres_conflicts: [list of conflicting acreage values]
  gps_conflicts: [list of conflicting coordinate pairs]
  features_conflicts: [list of conflicting feature lists]
  url_conflicts: [list of conflicting URLs]
  notes_conflicts: [list of conflicting notes]

Rules:

- All conflicts must be preserved exactly as discovered.
- No conflict may be resolved during discovery.
- Conflicts must be recorded even if values differ only in punctuation or formatting.
- gps_conflicts must record coordinate pairs exactly as discovered.
- partner_agencies_conflicts must record all conflicting lists, even if differences are minor.
- Conflicts must not be deduplicated or normalized.

------------------------------------------------------------
# 11. UNCERTAINTY METADATA

uncertainty:
  missing_fields: [list of missing fields]
  ambiguous_fields: [list of ambiguous fields]
  partial_fields: [list of partially extracted fields]
  extraction_warnings: [list of warnings]

Rules:

- missing_fields lists fields expected for the entity type but not discovered.
- ambiguous_fields lists fields with unclear or contradictory values.
- partial_fields lists fields where extraction was incomplete.
- extraction_warnings records any issues encountered during extraction.
- Uncertainty metadata must not be inferred or corrected.
- Uncertainty metadata must be preserved exactly as generated by the extraction process.

------------------------------------------------------------
# 12. PARENT METADATA (ACCESS POINTS ONLY)

parent:
  parent_site_raw: (string, required for Access Points)
  parent_site_conflicts: [list of conflicting parent site names]

Rules:

- parent_site_raw must be preserved exactly as discovered.
- parent_site_conflicts must record all conflicting parent site names.
- No inference of parent site is permitted.
- No GIS-based inference is permitted.
- No inference from URL structure is permitted.

------------------------------------------------------------
# 13. BOUNDARY METADATA

boundary:
  boundary_present: (boolean, required)
  boundary_source: (string, optional)
  boundary_conflicts: [list of conflicting boundary indicators]
  boundary_notes: (string, optional)

Rules:

- boundary_present indicates whether the authoritative source explicitly states that the entity has a defined boundary.
- boundary_source records the URL or dataset that provided boundary information.
- boundary_conflicts must record all conflicting statements about boundaries.
- boundary_notes may record ambiguous or unclear boundary descriptions.
- No GIS-derived boundaries may be inferred during discovery.
- No polygon, shapefile, or GIS layer may be used to infer boundary presence.

------------------------------------------------------------
# 14. BASELINE METADATA

baseline:
  seeded_from_baseline: (boolean, required)
  baseline_id: (string, optional)
  baseline_notes: (string, optional)

Rules:

- seeded_from_baseline indicates whether the entity originated from Tier‑0 Baseline.
- baseline_id must reference the baseline identifier exactly as stored in the baseline dataset.
- baseline_notes may record discrepancies between baseline and discovered values.
- Baseline values must never override authoritative discovery values.
- Baseline metadata must be preserved even when discovery provides more complete information.

------------------------------------------------------------
# 15. RAW FIELD PRESERVATION RULES

Raw Field Preservation Rules define how all raw fields must be handled during discovery.  
Rules apply to all entity types unless explicitly restricted.

General Rules:

- All raw fields must be preserved exactly as discovered.
- No normalization, inference, correction, or vocabulary matching is permitted.
- Malformed values must be preserved.
- Missing values must remain blank.
- Conflicts must be recorded in Conflict Metadata.
- GIS-derived fields must remain blank during discovery.
- Raw fields must appear in the Raw Discovery Record even if blank.

------------------------------------------------------------
## 15.1 SITE RAW FIELDS (FULL v5.2 LIST, ALPHABETICAL)

### acres_raw
- Preserve exactly as discovered.
- No unit conversion or numeric normalization.
- Malformed values must be preserved.

### category_raw
- Preserve exactly as discovered.
- No vocabulary matching during discovery.

### counties_raw
- Preserve exactly as discovered.
- No alphabetical sorting during discovery.
- No normalization of county names.

### description_raw
- Preserve exactly as discovered.
- No summarization or rewriting.

### designation_raw
- Preserve exactly as discovered.
- No vocabulary matching.

### features_raw
- Preserve exactly as discovered.
- No categorization or vocabulary matching.

### governance_raw
- Preserve exactly as discovered.
- Must represent operational control only.

### gps_lat_raw
- May be populated only when explicitly provided by authoritative sources.
- No inference or derivation.

### gps_lon_raw
- Same rules as gps_lat_raw.

### location_raw
- Preserve exactly as discovered.
- No GIS substitution or inference.

### name_raw
- Preserve exactly as discovered.
- No title‑case correction or punctuation normalization.

### notes_raw
- Preserve exactly as discovered.

### ownership_raw
- Preserve exactly as discovered.
- Must represent legal title only.

### partner_agencies_raw
- Preserve exactly as discovered.
- Must represent formal, documented co‑operators.
- Must not duplicate ownership_raw or governance_raw.

### status_raw
- Preserve exactly as discovered.
- No vocabulary matching.

### subtype_raw
- Preserve exactly as discovered.
- No vocabulary matching.

### url_primary_raw
- Preserve exactly as discovered.
- No removal of tracking parameters.

### urls_raw
- Preserve exactly as discovered.
- Order must not be changed.

------------------------------------------------------------
## 15.2 TRAIL RAW FIELDS (PENDING v5.2 SCHEMA REVIEW)

Raw field preservation rules for Trail entities will be added after the Trail Schema v5.2 update.

------------------------------------------------------------
## 15.3 TRAIL SEGMENT RAW FIELDS (PENDING v5.2 SCHEMA REVIEW)

Raw field preservation rules for Trail Segment entities will be added after the Trail Segment Schema v5.2 update.

------------------------------------------------------------
## 15.4 TRAIL NETWORK RAW FIELDS (PENDING v5.2 SCHEMA REVIEW)

Raw field preservation rules for Trail Network entities will be added after the Trail Network Schema v5.2 update.

------------------------------------------------------------
## 15.5 SITE NETWORK RAW FIELDS (PENDING v5.2 SCHEMA REVIEW)

Raw field preservation rules for Site Network entities will be added after the Site Network Schema v5.2 update.

------------------------------------------------------------
## 15.6 ACCESS POINT RAW FIELDS (PENDING v5.2 SCHEMA REVIEW)

Raw field preservation rules for Access Point entities will be added after the Access Point Schema v5.2 update.

------------------------------------------------------------
# 16. NOTES

notes:
  general_notes: (string, optional)
  extraction_notes: (string, optional)
  review_notes: (string, optional)

Rules:

- notes fields may contain any additional information relevant to the discovery process.
- general_notes may include contextual information not captured elsewhere.
- extraction_notes may include scraper‑level or parser‑level observations.
- review_notes may include human review comments.
- Notes must never override or reinterpret raw fields or metadata fields.

------------------------------------------------------------
# 17. COMPLETE METADATA OBJECT (TEMPLATE)

metadata:
  identity:
    name_raw:
    entity_type:
    counties_raw:
    township_raw:
    municipality_raw:
    parent_site_raw:
    category_raw:
    subtype_raw:
    designation_raw:
    status_raw:
    description_raw:
    location_raw:
    acres_raw:
    gps_lat_raw:
    gps_lon_raw:
    features_raw:
    difficulty_raw:
    accessibility_raw:
    url_primary_raw:
    urls_raw:
    notes_raw:

  organizational:
    ownership_raw:
    governance_raw:
    partner_agencies_raw:
    coordination_raw:

  tiers:
    discovered_in: []
    primary_tier:

  sources:
    urls: []
    datasets: []
    maps: []
    gis_layers: []

  provenance:
    parent_url:
    discovery_path: []
    extraction_method:
    harvested_at:
    discovery_run_id:

  lineage:
    parent_entity_id:
    parent_entity_type:
    lineage_notes:

  conflicts:
    name_conflicts: []
    counties_conflicts: []
    category_conflicts: []
    subtype_conflicts: []
    designation_conflicts: []
    status_conflicts: []
    ownership_conflicts: []
    governance_conflicts: []
    partner_agencies_conflicts: []
    coordination_conflicts: []
    acres_conflicts: []
    gps_conflicts: []
    features_conflicts: []
    url_conflicts: []
    notes_conflicts: []

  uncertainty:
    missing_fields: []
    ambiguous_fields: []
    partial_fields: []
    extraction_warnings: []

  parent:
    parent_site_raw:
    parent_site_conflicts: []

  boundary:
    boundary_present:
    boundary_source:
    boundary_conflicts: []
    boundary_notes:

  baseline:
    seeded_from_baseline:
    baseline_id:
    baseline_notes:

  raw_fields:
    site:
      acres_raw:
      category_raw:
      counties_raw:
      description_raw:
      designation_raw:
      features_raw:
      governance_raw:
      gps_lat_raw:
      gps_lon_raw:
      location_raw:
      name_raw:
      notes_raw:
      ownership_raw:
      partner_agencies_raw:
      status_raw:
      subtype_raw:
      url_primary_raw:
      urls_raw:

    trail:
      _pending_schema_update: "Raw field preservation rules for Trail entities will be added after the Trail Schema v5.2 update."

    trail_segment:
      _pending_schema_update: "Raw field preservation rules for Trail Segment entities will be added after the Trail Segment Schema v5.2 update."

    trail_network:
      _pending_schema_update: "Raw field preservation rules for Trail Network entities will be added after the Trail Network Schema v5.2 update."

    site_network:
      _pending_schema_update: "Raw field preservation rules for Site Network entities will be added after the Site Network Schema v5.2 update."

    access_point:
      _pending_schema_update: "Raw field preservation rules for Access Point entities will be added after the Access Point Schema v5.2 update."

------------------------------------------------------------
# 18. INTEGRATION POINTS

This module integrates with:

- Discovery Protocol Module v5.x  
- Discovery Orchestration Module v5.x  
- All Tier Sub-Procedures v5.x  
- Discovery Output Specification v5.x  
- Resolution Engine v5.x  
- Normalization Engine v5.x  
- Entity Graph Schema v5.x  
- Audit & Logging Module v5.x  

Metadata must be passed unchanged through all downstream modules until Resolution.

------------------------------------------------------------
# 19. MODULE DEPENDENCIES

This module depends on:

- Site Schema Module v5.2  
- Trail Schema Module v5.x (pending v5.2 update)  
- Trail Segment Schema Module v5.x (pending v5.2 update)  
- Trail Network Schema Module v5.x (pending v5.2 update)  
- Site Network Schema Module v5.x (pending v5.2 update)  
- Access Point Schema Module v5.x (pending v5.2 update)  
- Discovery Output Specification v5.x  
- Discovery Protocol Module v5.x  
- Discovery Orchestration Module v5.x  
- Resolution Engine v5.x  
- Normalization Engine v5.x  
- Audit & Logging Module v5.x  

------------------------------------------------------------
# END OF DISCOVERY METADATA SPECIFICATION v5.3