# NATURAL AREAS PROJECT — DISCOVERY OUTPUT SPECIFICATION v3.2.2
(Structure and Requirements for Raw Candidate Records)

The Discovery Output Specification defines the **exact structure** of the Raw
Candidate Records produced by all discovery tiers and by the Access Point
Discovery Sub‑Procedure v3.2.2. These records are the **input** to all six
Normalization Contracts v3.2.2.

This module is referenced **only** by:

- Discovery Protocol Module v3.2.2  
- All tier‑specific discovery sub‑procedures v3.2.2  
- Access Point Discovery Sub‑Procedure v3.2.2  

No other module may reference it directly.

------------------------------------------------------------
# 1. PURPOSE

This specification defines:

- The required fields for all Raw Candidate Records  
- The structure of Site, Trail, Trail Segment, Trail Network, Site Network, and Access Point outputs  
- The rules for raw (unnormalized) values  
- The relationship between output fields and discovery metadata  
- The guarantees Discovery must provide to downstream modules  

This ensures that Discovery produces **consistent, machine‑readable,
deterministic** outputs for all six entity types.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All entities discovered in Tiers 1–8:  
  - Site (including child Sites)  
  - Trail  
  - Trail Segment  
  - Trail Network  
  - Site Network  
  - Access Point  
- All Access Points discovered in the Access Point Discovery Sub‑Procedure v3.2.2  
- All multi‑tier discoveries  
- All baseline‑seeded entities  

It governs:

- Output structure  
- Field requirements  
- Raw value rules  
- Integration with normalization and TSV modules  
- Metadata guarantees  

------------------------------------------------------------
# 3. RAW CANDIDATE RECORD STRUCTURE

Each discovered entity must produce a **Raw Candidate Record** with the following
top‑level fields:

raw_candidate_record:
  entity_type:
  name_raw:
  county:
  counties_raw:
  township:
  municipality:
  parent_site:
  access_point_type_raw:
  role_raw:
  parent_sites:
  parent_trails:
  parent_trail_segments:
  ownership_raw:
  access_level_raw:
  gps_raw:
  address_raw:
  url_primary:
  url_all:
  source_datasets:
  source_maps:
  source_gis_layers:
  discovery_tier:
  discovered_in_tiers:
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

## 4.3 `county`

- Always required  
- Must match the county being processed  

## 4.4 `counties_raw`

- List of **all counties** where the entity appears  
- Must preserve raw spelling and order  
- Must not be normalized  

## 4.5 `discovery_tier`

- For Sites, Trails, Trail Segments, Trail Networks, Site Networks: integer 1–8  
- For Access Points: integer 1–8 or `"AP"` if discovered via AP‑specific workflows  

## 4.6 `discovered_in_tiers`

- List of all tiers where the entity appeared  
- Must include `"AP"` for Access Points discovered via AP‑specific workflows  

## 4.7 `discovery_metadata`

- Must embed the full metadata object defined in the Discovery Metadata Specification v3.2.2  
- Must include:  
  - Source URLs  
  - GIS layer identifiers  
  - Raw county list  
  - Parent relationships  
  - Conflict and uncertainty metadata  

------------------------------------------------------------
# 5. CONDITIONAL FIELDS BY ENTITY TYPE

## 5.1 `township`

Include if known (Sites, Trails, Trail Segments, Access Points).

## 5.2 `municipality`

Include if known (Sites, Trails, Trail Segments, Access Points).

## 5.3 `parent_site`

- Required for child Sites  
- Optional for all other entity types  

## 5.4 `ownership_raw`

Applies to:

- Site  
- Trail (if ownership is explicit)  
- Trail Segment (if ownership is explicit)  
- Site Network (if ownership is explicit)  

Values must be raw and unnormalized.

## 5.5 `gps_raw`

Applies to all entity types **if available**.

- May be point or polygon centroid  
- Must not be normalized  

## 5.6 `address_raw`

Include if available (Sites, Access Points).

## 5.7 `url_primary`

- The most authoritative URL  
- Must not be invented  

## 5.8 `url_all`

- List of all URLs used  
- Must preserve order of discovery  

## 5.9 `source_datasets`, `source_maps`, `source_gis_layers`

- Lists of all sources used  
- Must preserve all values  
- Must not be deduplicated unless identical  

## 5.10 `notes_raw`

- Any raw notes discovered  
- Must not be interpreted or normalized  

------------------------------------------------------------
# 6. CONDITIONAL FIELDS (ACCESS POINTS)

## 6.1 `access_point_type_raw`

Examples:

- Trailhead  
- Parking  
- Boat Launch  
- Fishing Access  
- Hunting Access  
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

## 6.3 `parent_sites`

- List of Site names or IDs  
- Multiple allowed  

## 6.4 `parent_trails`

- List of Trail names or IDs  
- Multiple allowed  

## 6.5 `parent_trail_segments`

- List of Trail Segment names or IDs  
- Multiple allowed  

## 6.6 `access_level_raw`

Examples:

- Public  
- Limited Public  
- Fee‑Based  
- Seasonal  
- Reservation‑Only  
- Program‑Only  
- Private (No Access)  

## 6.7 `gps_raw`

Required if available.

## 6.8 `address_raw`

Include if available.

## 6.9 `url_primary`, `url_all`, `source_*`

Same rules as Sites.

## 6.10 `notes_raw`

Include:

- Access limitations  
- Signage notes  
- Trail system integration notes  

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
- URLs  

## 7.2 No Invention

Discovery must not invent:

- Names  
- Access Point Types  
- Parents  
- URLs  
- GPS  
- Ownership  
- Access levels  

## 7.3 No Silent Corrections

If a value is malformed:

- Preserve it exactly  
- Log the issue in metadata  
- Let normalization and resolution handle it  

------------------------------------------------------------
# 8. MULTI‑COUNTY RULE (UPDATED)

Discovery outputs must follow the authoritative multi‑county rule:

- **No segmentation** of multi‑county entities  
- **Record all counties** in `counties_raw`  
- `county` = primary county (first discovered or highest‑authority source)  
- Normalization writes the county list as a **semicolon‑delimited, alphabetized list**  

------------------------------------------------------------
# 9. BASELINE INTEGRATION

## 9.1 `seeded_from_baseline`

true / false

## 9.2 `baseline_id`

Include if the entity originated from the baseline.

------------------------------------------------------------
# 10. COMPLETE RAW CANDIDATE RECORD (TEMPLATE)

raw_candidate_record:
  entity_type:
  name_raw:
  county:
  counties_raw: []
  township:
  municipality:
  parent_site:
  access_point_type_raw:
  role_raw:
  parent_sites: []
  parent_trails: []
  parent_trail_segments: []
  ownership_raw:
  access_level_raw:
  gps_raw:
  address_raw:
  url_primary:
  url_all: []
  source_datasets: []
  source_maps: []
  source_gis_layers: []
  discovery_tier:
  discovered_in_tiers: []
  seeded_from_baseline:
  baseline_id:
  notes_raw:
  discovery_metadata: { ... }

------------------------------------------------------------
# 11. DEVELOPER PREVIEW TSVs

Discovery may output TSV‑formatted previews of Raw Candidate Records upon explicit user request. These previews:

- Use raw values only  
- Follow the TSV field order for the entity type  
- Must not be interpreted as normalized TSV output  
- Are not part of the official Discovery → Normalization pipeline  
- Are intended solely for debugging and inspection  

------------------------------------------------------------
# 12. INTEGRATION POINTS

This specification integrates with:

- Discovery Protocol Module v3.2.2  
- All tier‑specific discovery sub‑procedures v3.2.2  
- Access Point Discovery Sub‑Procedure v3.2.2  
- Discovery Metadata Specification v3.2.2  
- All six Normalization Contracts v3.2.2  
- All six TSV Output Specifications v3.2.2  
- Audit & Logging Module v3.2.2  
- County Baseline Module v3.2.2  
- Resolution Module v3.2.2  

No other module may reference this specification directly.

------------------------------------------------------------
# 13. VERSIONING

- This module is **Discovery Output Specification v3.2.2**.  
- Any change to output structure requires v3.3, v4.0, etc.  
- Any change to tier order or workflow must be made in the Discovery Protocol Module v3.2.2.

------------------------------------------------------------
# END OF DISCOVERY OUTPUT SPECIFICATION v3.2.2