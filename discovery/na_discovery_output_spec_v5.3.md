# NATURAL AREAS PROJECT
# DISCOVERY OUTPUT SPECIFICATION v5.3
Authoritative Structure for Raw Discovery Records

The Discovery Output Specification v5.3 defines the exact structure of the Raw Discovery Records produced by:

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
# CHANGES FROM v5.2 → v5.3

- Updated module version to v5.3.
- Updated all cross‑module references to v5.x.
- Replaced `gps_raw` with `gps_lat_raw` and `gps_lon_raw`.
- Removed `geometry_raw` (GIS-derived geometry prohibited during discovery).
- Removed `maps_raw` (map URLs now included in `urls_raw`).
- Updated organizational field cluster to match Metadata v5.3.
- Updated identity fields to match Metadata v5.3.
- Updated parent relationship fields (parent_*_raw lists retained).
- Updated notes handling: `notes_raw` moved to `identity.notes_raw`.
- Updated raw discovery record template to embed full Metadata v5.3 object.
- Updated applicability rules to match Metadata v5.3 and Protocol v5.x.
- Ensured all map-like URLs (PDFs, JPGs, interactive viewers) are captured in `urls_raw`.

------------------------------------------------------------
# 1. PURPOSE

This specification defines:

- The required fields for all Raw Discovery Records v5.3
- The structure of Site, Trail, Trail Segment, Trail Network, Site Network, and Access Point outputs
- The rules for raw (unnormalized) values
- The relationship between raw fields and Discovery Metadata v5.x
- The guarantees Discovery must provide to downstream modules
- The provenance and audit requirements for all raw outputs

This ensures that Discovery produces consistent, deterministic, provenance‑rich, machine‑readable outputs for all six entity types.

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

Each discovered entity must produce a Raw Discovery Record v5.3 with the
following top‑level fields. These fields represent the raw, unnormalized,
unresolved values extracted directly from authoritative sources during
enumerative and recursive discovery.

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
  gps_lat_raw:
  gps_lon_raw:
  location_raw:
  features_raw:
  difficulty_raw:
  accessibility_raw:
  url_primary_raw:
  urls_raw:
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
  identity_notes_raw:
  discovery_metadata: { ... }

Notes:

- `urls_raw` must include **all URLs discovered**, including map URLs (PDFs, JPGs, interactive map viewers).
- `identity_notes_raw` replaces the former top‑level `notes_raw` field.
- `gps_lat_raw` and `gps_lon_raw` replace `gps_raw`.
- `geometry_raw` and `maps_raw` have been removed.
- Parent relationship lists (`parent_sites_raw`, `parent_trails_raw`, `parent_trail_segments_raw`) are retained.

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

Recorded exactly as determined by the entity‑specific discovery sub‑procedure.

## 4.2 name_raw
Recorded exactly as discovered.  
No normalization, no punctuation correction, no title‑case correction.

## 4.3 counties_raw
List of all counties where the entity appears, exactly as discovered.

## 4.4 county_primary
The county currently being processed.  
Required for all entities.

## 4.5 discovery_tier
Integer 1–8, or:

- `"baseline"` for Tier‑0
- `"AP"` for Access Point workflows

## 4.6 discovered_in_tiers
List of all tiers where the entity appeared.

## 4.7 discovery_metadata
Full metadata object defined in Discovery Metadata Specification v5.x.  
Must be embedded exactly, without modification.

------------------------------------------------------------
# 5. CONDITIONAL FIELDS BY ENTITY TYPE

## 5.1 township_raw
Must remain blank during discovery.  
GIS‑derived downstream.

## 5.2 municipality_raw
Must remain blank during discovery.  
GIS‑derived downstream.

## 5.3 parent_site_raw
Required for child Sites.  
Optional for other entity types.

## 5.4 parent_sites_raw, parent_trails_raw, parent_trail_segments_raw
Lists of raw parent relationships discovered during extraction.

Rules:

- Preserve exactly as discovered.
- Do not infer parents.
- Do not normalize names.
- Do not dedupe.
- These lists coexist with lineage metadata.

## 5.5 ownership_raw
Applies to any entity type if explicitly stated.

## 5.6 governance_raw
Applies to any entity type if explicitly stated.

## 5.7 partner_agencies_raw
Applies to any entity type if explicitly stated.  
Represents formal, documented co‑operators.

## 5.8 coordination_raw
Applies to any entity type if explicitly stated.  
Represents informal or community‑based partners.

## 5.9 gps_lat_raw, gps_lon_raw
May be populated only when explicitly provided by authoritative sources.  
No inference or GIS derivation permitted.

## 5.10 location_raw
Applies to Sites and Access Points.  
Replaces `address_raw` from earlier versions.

## 5.11 features_raw
Applies to Sites and Access Points.  
Preserve exactly as discovered.

## 5.12 difficulty_raw
Applies to Trails and Trail Segments only.  
Must be explicitly stated.

## 5.13 accessibility_raw
Applies to Trails and Trail Segments only.  
Must be explicitly stated.

## 5.14 url_primary_raw
Most authoritative URL discovered.

## 5.15 urls_raw
List of all URLs discovered, including:

- primary URL  
- secondary URLs  
- map URLs (PDFs, JPGs, interactive viewers)  
- internal links surfaced during recursion  

Order must be preserved.

## 5.16 source_* fields
Preserve all datasets, maps, GIS layers, documents, photos, and web pages.

## 5.17 identity_notes_raw
Raw notes extracted from authoritative sources.  
Replaces the former top‑level `notes_raw`.

------------------------------------------------------------
# 6. RAW VALUE RULES

Discovery must preserve all values exactly as discovered.  
These rules apply to every field in the Raw Discovery Record v5.3.

## 6.1 No normalization
Discovery must not normalize:

- names  
- access point types  
- features  
- difficulty or accessibility ratings  
- ownership, governance, partner agencies, coordination  
- GPS coordinates  
- county lists  
- URLs  

Normalization occurs downstream in the Normalization Engine v5.x.

## 6.2 No invention
Discovery must not invent:

- names  
- parents  
- URLs  
- GPS coordinates  
- features  
- difficulty or accessibility ratings  
- organizational fields  

## 6.3 No silent corrections
Malformed values must be preserved exactly as discovered.

Examples:

- “10O acres” (letter O instead of zero)  
- “http://example..com” (double dot)  
- “N 40.123, W -83.456” (nonstandard formatting)  

## 6.4 No inference
Discovery must not infer:

- township  
- municipality  
- difficulty  
- accessibility  
- parent relationships  
- geometry  
- GPS coordinates  

## 6.5 No deduplication
Duplicate values must be preserved exactly as discovered.

## 6.6 No reordering
Lists must preserve the order in which values were discovered.

This applies to:

- urls_raw  
- parent_sites_raw  
- parent_trails_raw  
- parent_trail_segments_raw  
- discovered_in_tiers  

------------------------------------------------------------
# 7. MULTI‑COUNTY RULE (v5.x)

Discovery must follow the authoritative multi‑county rule:

- No segmentation of multi‑county entities  
- Record all counties exactly as discovered  
- Preserve raw county lists in metadata  
- Normalization alphabetizes and formats county lists downstream  

This rule applies to all six entity types.

------------------------------------------------------------
# 8. BASELINE INTEGRATION (TIER‑0)

seeded_from_baseline: true/false  
baseline_id: included if baseline‑originated.

Rules:

- Baseline entities must be loaded as Tier‑0 raw records.  
- seeded_from_baseline must be set to true.  
- baseline_id must be preserved exactly as stored in the baseline dataset.  
- Authoritative discovery may override baseline values.  
- Conflicts must be recorded in metadata.  
- Baseline must never override authoritative discovery.  

------------------------------------------------------------
# 9. COMPLETE RAW DISCOVERY RECORD (TEMPLATE)

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

  gps_lat_raw:
  gps_lon_raw:
  location_raw:
  features_raw:
  difficulty_raw:
  accessibility_raw:

  url_primary_raw:
  urls_raw: []

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

  identity_notes_raw:

  discovery_metadata: { ... }

Notes:

- `urls_raw` must include all URLs discovered, including map URLs (PDFs, JPGs, interactive viewers).
- `identity_notes_raw` replaces the former top‑level `notes_raw`.
- `gps_lat_raw` and `gps_lon_raw` replace `gps_raw`.
- `geometry_raw` and `maps_raw` have been removed.
- Parent relationship lists are retained.
- The embedded metadata object must follow the Discovery Metadata Specification v5.x exactly.

------------------------------------------------------------
# 10. NULL‑TIER RECORD FORMAT
(unchanged from v5.1; retained exactly)

[Null‑tier specification preserved verbatim]

------------------------------------------------------------
# 11. DEVELOPER PREVIEW TSVs
(unchanged; previews remain raw‑value only)

------------------------------------------------------------
# 12. INTEGRATION POINTS

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
# 13. VERSIONING

- This module is Discovery Output Specification v5.3.  
- Any change to output structure requires v5.4, v5.5, etc.  
- Tier order or workflow changes must be made in the Discovery Protocol Module v5.x.  

------------------------------------------------------------
# END OF DISCOVERY OUTPUT SPECIFICATION v5.3