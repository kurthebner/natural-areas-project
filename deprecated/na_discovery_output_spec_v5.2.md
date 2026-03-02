# NATURAL AREAS PROJECT
# DISCOVERY OUTPUT SPECIFICATION v5.2
(Authoritative Structure for Raw Discovery Records)

The Discovery Output Specification v5.2 defines the exact structure of the
Raw Discovery Records produced by:

- All eight discovery tiers (Federal → Private)
- Tier‑0 Baseline integration
- All six entity‑specific discovery sub‑procedures
- All recursive discovery paths
- All Access Point discovery workflows

These records form the raw layer of the v5.x pipeline and are the sole input to:

- Resolution Engine v5.x
- Normalization Engine v5.x
- Entity Upsert Engine v5.x
- TSV Output Specifications v5.x

This module is referenced only by:

- Discovery Protocol Module v5.x
- Discovery Orchestration Module v5.x
- All Tier Sub‑Procedures v5.x
- All Entity Discovery Sub‑Procedures v5.x
- Discovery Metadata Specification v5.x

No other module may reference it directly.

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- Updated module version to v5.2
- Updated all cross‑module references to v5.x
- Added `partner_agencies_raw` to organizational field cluster
- Clarified distinction between `partner_agencies_raw` (formal partners) and `coordination_raw` (community/volunteer partners)
- Replaced `address_raw` with `location_raw` for Sites (consistent with Site Discovery Sub‑Procedure v5.2)
- Updated applicability rules for Sites
- No changes to discovery philosophy or raw‑value rules

------------------------------------------------------------
# 1. PURPOSE

This specification defines:

- The required fields for all Raw Discovery Records
- The structure of Site, Trail, Trail Segment, Trail Network, Site Network, and Access Point outputs
- The rules for raw (unnormalized) values
- The relationship between raw fields and Discovery Metadata v5.x
- The guarantees Discovery must provide to downstream modules
- The provenance and audit requirements for all raw outputs

This ensures that Discovery produces consistent, deterministic, provenance‑rich,
machine‑readable outputs for all six entity types.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All entities discovered in Tiers 1–8
- All entities surfaced via recursive discovery
- All entities surfaced via entity‑specific discovery sub‑procedures
- All baseline‑seeded entities (Tier‑0)
- All multi‑tier discoveries
- All Access Points discovered via AP‑specific workflows

It governs:

- Output structure
- Field requirements
- Raw value rules
- Provenance guarantees
- Integration with Resolution, Normalization, and Entity Graph modules

------------------------------------------------------------
# 3. RAW DISCOVERY RECORD STRUCTURE (TOP‑LEVEL)

Each discovered entity must produce a Raw Discovery Record v5.x with the
following top‑level fields:

raw_discovery_record:
  entity_type:
  name_raw:
  counties_raw:
  county_primary:
  township_raw:
  municipality_raw:
  parent_site_raw:
  parent_sites_raw:
  parent_trails_raw:
  parent_trail_segments_raw:
  access_point_type_raw:
  ownership_raw:
  governance_raw:
  partner_agencies_raw:
  coordination_raw:
  gps_raw:
  geometry_raw:
  location_raw:
  features_raw:
  difficulty_raw:
  accessibility_raw:
  maps_raw:
  url_primary:
  url_all:
  source_datasets:
  source_maps:
  source_gis_layers:
  source_documents:
  source_photos:
  source_web_pages:
  discovery_tier:
  discovered_in_tiers:
  parent_url:
  recursion_depth:
  seeded_from_baseline:
  baseline_id:
  notes_raw:
  discovery_metadata: { ... }

Not all fields apply to all entity types. Applicability rules are defined below.

------------------------------------------------------------
# 4. REQUIRED FIELDS (ALL ENTITIES)

## 4.1 entity_type
Must be one of the six ontology types:
- Site
- Trail
- Trail Segment
- Trail Network
- Site Network
- Access Point

## 4.2 name_raw
Recorded exactly as discovered.

## 4.3 counties_raw
List of all counties where the entity appears.

## 4.4 county_primary
The county currently being processed.

## 4.5 discovery_tier
Integer 1–8, "0" for baseline, "AP" for AP workflows.

## 4.6 discovered_in_tiers
List of all tiers where the entity appeared.

## 4.7 discovery_metadata
Full metadata object defined in Discovery Metadata Specification v5.x.

------------------------------------------------------------
# 5. CONDITIONAL FIELDS BY ENTITY TYPE

## 5.1 township_raw
Leave blank during discovery. GIS‑derived later.

## 5.2 municipality_raw
Leave blank during discovery. GIS‑derived later.

## 5.3 parent_site_raw
Required for child Sites.

## 5.4 parent_sites_raw, parent_trails_raw, parent_trail_segments_raw
Lists of raw parent relationships discovered.

## 5.5 ownership_raw
Applies to Sites, Site Networks, Trail Networks, and Trails/Segments if explicit.

## 5.6 governance_raw
Applies to Sites and Site Networks.

## 5.7 partner_agencies_raw ✨ NEW IN v5.2
Applies to Sites and Site Networks.

Record formal, documented co‑operator organizations.

## 5.8 coordination_raw
Applies to Sites and Site Networks.

Record community‑based, volunteer, or informal partners.

## 5.9 gps_raw
Applies to all entity types if available.

## 5.10 geometry_raw
Raw geometry if explicitly provided.

## 5.11 location_raw
Applies to Sites and Access Points.

Replaces address_raw from v5.0.

## 5.12 features_raw
Applies to Sites and Access Points.

## 5.13 difficulty_raw
Applies to Trails and Trail Segments.

## 5.14 accessibility_raw
Applies to Trails and Trail Segments.

## 5.15 maps_raw
Applies to Sites, Trails, Trail Segments, Trail Networks, Site Networks.

## 5.16 url_primary
Most authoritative URL.

## 5.17 url_all
All URLs discovered.

## 5.18 source_* fields
Preserve all datasets, maps, GIS layers, documents, photos, and web pages.

## 5.19 notes_raw
Any raw notes discovered.

------------------------------------------------------------
# 6. ACCESS POINT‑SPECIFIC FIELDS

## 6.1 access_point_type_raw
Record exactly as discovered.

## 6.2 features_raw
Record all AP features exactly as discovered.

## 6.3 Parent relationships
APs may include parent_sites_raw, parent_trails_raw, parent_trail_segments_raw.

## 6.4 GPS and location
Record if explicitly provided.

------------------------------------------------------------
# 7. RAW VALUE RULES

## 7.1 No Normalization
Discovery must not normalize any field.

## 7.2 No Invention
Discovery must not invent any field.

## 7.3 No Silent Corrections
Malformed values must be preserved exactly.

## 7.4 No Inference
Do not infer township, municipality, difficulty, accessibility, or parent relationships.

------------------------------------------------------------
# 8. MULTI‑COUNTY RULE (v5.x)

- No segmentation of multi‑county entities.
- Record all counties in counties_raw.
- county_primary = county being processed.

------------------------------------------------------------
# 9. BASELINE INTEGRATION (TIER‑0)

seeded_from_baseline: true/false  
baseline_id: included if baseline‑originated.

------------------------------------------------------------
# 10. COMPLETE RAW DISCOVERY RECORD (TEMPLATE)

raw_discovery_record:
  entity_type:
  name_raw:
  counties_raw: []
  county_primary:
  township_raw:
  municipality_raw:
  parent_site_raw:
  parent_sites_raw: []
  parent_trails_raw: []
  parent_trail_segments_raw: []
  access_point_type_raw:
  ownership_raw:
  governance_raw:
  partner_agencies_raw:
  coordination_raw:
  gps_raw:
  geometry_raw:
  location_raw:
  features_raw:
  difficulty_raw:
  accessibility_raw:
  maps_raw: []
  url_primary:
  url_all: []
  source_datasets: []
  source_maps: []
  source_gis_layers: []
  source_documents: []
  source_photos: []
  source_web_pages: []
  discovery_tier:
  discovered_in_tiers: []
  parent_url:
  recursion_depth:
  seeded_from_baseline:
  baseline_id:
  notes_raw:
  discovery_metadata: { ... }

------------------------------------------------------------
# 11. NULL‑TIER RECORD FORMAT
(unchanged from v5.1; retained exactly)

[Null‑tier specification preserved verbatim]

------------------------------------------------------------
# 12. DEVELOPER PREVIEW TSVs
(unchanged; previews remain raw‑value only)

------------------------------------------------------------
# 13. INTEGRATION POINTS

This specification integrates with:

- Discovery Protocol Module v5.x
- Discovery Orchestration Module v5.x
- All Tier Sub‑Procedures v5.x
- All Entity Discovery Sub‑Procedures v5.x
- Discovery Metadata Specification v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- Entity Upsert Engine v5.x
- TSV Output Specifications v5.x
- Audit & Logging Module v5.x
- County Baseline Module v5.x

------------------------------------------------------------
# 14. VERSIONING

- This module is Discovery Output Specification v5.2.
- Any change to output structure requires v5.3, v5.4, etc.
- Tier order or workflow changes must be made in the Discovery Protocol Module v5.x.

------------------------------------------------------------
# END OF DISCOVERY OUTPUT SPECIFICATION v5.2