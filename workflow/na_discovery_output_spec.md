# NATURAL AREAS PROJECT
# DISCOVERY OUTPUT SPECIFICATION v4.0
(Authoritative Structure for Raw Discovery Records)

The Discovery Output Specification v4.0 defines the **exact structure** of the
Raw Discovery Records produced by:

- All eight discovery tiers (Federal → Private)
- Tier‑0 Baseline integration
- All six entity‑specific discovery sub‑procedures
- All recursive discovery paths
- All Access Point discovery workflows

These records form the **raw layer** of the v4.0 pipeline and are the sole input
to:

- Resolution Engine v4.0
- Normalization Engine v4.0
- Entity Upsert Engine v4.0
- TSV Output Specifications v4.0

This module is referenced only by:

- Discovery Protocol Module v4.0
- Discovery Orchestration Module v4.0
- All Tier Sub‑Procedures v4.0
- All Entity Discovery Sub‑Procedures v4.0
- Discovery Metadata Specification v4.0

No other module may reference it directly.

------------------------------------------------------------
# 1. PURPOSE

This specification defines:

- The required fields for all Raw Discovery Records
- The structure of Site, Trail, Trail Segment, Trail Network, Site Network, and Access Point outputs
- The rules for raw (unnormalized) values
- The relationship between raw fields and Discovery Metadata v4.0
- The guarantees Discovery must provide to downstream modules
- The provenance and audit requirements for all raw outputs

This ensures that Discovery produces **consistent, deterministic, provenance‑rich,
machine‑readable** outputs for all six entity types.

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

Each discovered entity must produce a **Raw Discovery Record v4.0** with the
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
  role_raw:
  ownership_raw:
  access_level_raw:
  gps_raw:
  geometry_raw:
  address_raw:
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

## 4.1 `entity_type`
Must be one of the six ontology types:

- Site
- Trail
- Trail Segment
- Trail Network
- Site Network
- Access Point

## 4.2 `name_raw`
- Must be the name as discovered
- Must not be normalized, corrected, or altered

## 4.3 `counties_raw`
- List of **all counties** where the entity appears
- Must preserve raw spelling and order
- Must not be normalized

## 4.4 `county_primary`
- The county currently being processed
- Must match the county context of the discovery run

## 4.5 `discovery_tier`
- Integer 1–8 for authoritative tiers
- `"0"` for baseline‑seeded entities
- `"AP"` for Access Point–specific workflows

## 4.6 `discovered_in_tiers`
- List of all tiers where the entity appeared
- Must include `"AP"` for AP‑specific workflows

## 4.7 `discovery_metadata`
Must embed the full metadata object defined in the Discovery Metadata Specification v4.0, including:

- Source URLs
- GIS layer identifiers
- Raw county list
- Parent relationships
- Conflict and uncertainty metadata
- Recursion provenance
- Boundary flags
- Extraction method
- Tier authority

------------------------------------------------------------
# 5. CONDITIONAL FIELDS BY ENTITY TYPE

## 5.1 `township_raw`
Include if known (Sites, Trails, Trail Segments, Access Points).

## 5.2 `municipality_raw`
Include if known (Sites, Trails, Trail Segments, Access Points).

## 5.3 `parent_site_raw`
- Required for child Sites
- Optional for all other entity types

## 5.4 `parent_sites_raw`, `parent_trails_raw`, `parent_trail_segments_raw`
Lists of raw parent relationships discovered during:

- Tier discovery
- Entity‑specific discovery
- Recursive discovery

## 5.5 `ownership_raw`
Applies to:

- Site
- Trail (if ownership is explicit)
- Trail Segment (if ownership is explicit)
- Site Network (if ownership is explicit)

Values must be raw and unnormalized.

## 5.6 `gps_raw`
Applies to all entity types **if available**.

- May be point, centroid, or raw geometry anchor
- Must not be normalized

## 5.7 `geometry_raw`
- Raw geometry if discovered (polygon, polyline, multipoint)
- Must not be simplified or normalized

## 5.8 `address_raw`
Include if available (Sites, Access Points).

## 5.9 `url_primary`
- The most authoritative URL
- Must not be invented

## 5.10 `url_all`
- List of all URLs used
- Must preserve order of discovery

## 5.11 `source_*` fields
Discovery must preserve:

- All datasets
- All maps
- All GIS layers
- All documents
- All photos
- All web pages

No deduplication unless identical.

## 5.12 `notes_raw`
- Any raw notes discovered
- Must not be interpreted or normalized

------------------------------------------------------------
# 6. ACCESS POINT–SPECIFIC FIELDS

## 6.1 `access_point_type_raw`
Examples:

- Trailhead
- Parking
- Boat Launch
- Fishing Access
- Scenic Overlook
- Roadside Access
- Camp Entrance
- Program Entrance
- Multi‑Use Access
- Unspecified Access

## 6.2 `role_raw`
Examples:

- Primary
- Secondary
- Connector
- Unknown

## 6.3 `access_level_raw`
Examples:

- Public
- Limited Public
- Fee‑Based
- Seasonal
- Reservation‑Only
- Program‑Only
- Private (No Access)

## 6.4 Parent relationships
Access Points may include:

- `parent_sites_raw`
- `parent_trails_raw`
- `parent_trail_segments_raw`

## 6.5 GPS and address
Required if available.

------------------------------------------------------------
# 7. RAW VALUE RULES

## 7.1 No Normalization
Discovery must not normalize:

- Names
- Access Point Types
- Roles
- Ownership
- Access levels
- Addresses
- GPS
- Geometry
- URLs

## 7.2 No Invention
Discovery must not invent:

- Names
- Access Point Types
- Parents
- URLs
- GPS
- Geometry
- Ownership
- Access levels

## 7.3 No Silent Corrections
Malformed values must be:

- Preserved exactly
- Logged in metadata
- Resolved downstream

------------------------------------------------------------
# 8. MULTI‑COUNTY RULE (v4.0)

Discovery outputs must follow the authoritative multi‑county rule:

- **No segmentation** of multi‑county entities
- **Record all counties** in `counties_raw`
- `county_primary` = county currently being processed
- Normalization alphabetizes and semicolon‑delimits the county list
- Resolution determines final county list if sources conflict

------------------------------------------------------------
# 9. BASELINE INTEGRATION (TIER‑0)

## 9.1 `seeded_from_baseline`
true / false

## 9.2 `baseline_id`
Include if the entity originated from the baseline.

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
  role_raw:
  ownership_raw:
  access_level_raw:
  gps_raw:
  geometry_raw:
  address_raw:
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
# 11. DEVELOPER PREVIEW TSVs

Discovery may output TSV‑formatted previews of Raw Discovery Records upon explicit
user request. These previews:

- Use raw values only
- Follow the TSV field order for the entity type
- Must not be interpreted as normalized TSV output
- Are not part of the official Discovery → Resolution → Normalization pipeline
- Are intended solely for debugging and inspection

------------------------------------------------------------
# 12. INTEGRATION POINTS

This specification integrates with:

- Discovery Protocol Module v4.0
- Discovery Orchestration Module v4.0
- All Tier Sub‑Procedures v4.0
- All Entity Discovery Sub‑Procedures v4.0
- Discovery Metadata Specification v4.0
- Resolution Engine v4.0
- Normalization Engine v4.0
- Entity Upsert Engine v4.0
- TSV Output Specifications v4.0
- Audit & Logging Module v4.0
- County Baseline Module v4.0

No other module may reference this specification directly.

------------------------------------------------------------
# 13. VERSIONING

- This module is **Discovery Output Specification v4.0**.
- Any change to output structure requires v4.1, v4.2, etc.
- Any change to tier order or workflow must be made in the Discovery Protocol Module v4.0.

------------------------------------------------------------
# END OF DISCOVERY OUTPUT SPECIFICATION v4.0