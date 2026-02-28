# NATURAL AREAS PROJECT
# DISCOVERY OUTPUT SPECIFICATION v5.1
(Authoritative Structure for Raw Discovery Records)

The Discovery Output Specification v5.1 defines the **exact structure** of the
Raw Discovery Records produced by:

- All eight discovery tiers (Federal → Private)
- Tier-0 Baseline integration
- All six entity-specific discovery sub-procedures
- All recursive discovery paths
- All Access Point discovery workflows

These records form the **raw layer** of the v5.0 pipeline and are the sole input to:

- Resolution Engine v5.0
- Normalization Engine v5.0
- Entity Upsert Engine v5.0
- TSV Output Specifications v5.0

This module is referenced only by:

- Discovery Protocol Module v5.0
- Discovery Orchestration Module v5.0
- All Tier Sub-Procedures v5.0
- All Entity Discovery Sub-Procedures v5.0
- Discovery Metadata Specification v5.0

No other module may reference it directly.

------------------------------------------------------------
# CHANGES FROM v5.0

- `role_raw` removed — role field deleted from Access Point schema
- `access_level_raw` removed — access_level field deleted from Access Point schema
- `features_raw` added — for Access Point features (restrooms, parking, water, etc.)
- `difficulty_raw` added — for Trail and Trail Segment difficulty ratings
- `accessibility_raw` added — for Trail and Trail Segment accessibility info
- `maps_raw` added — for multiple map URLs (Trails, Trail Segments, Networks)
- `township_raw` and `municipality_raw` clarified — leave blank during discovery; populated via GIS spatial lookup in normalization phase
- All version references updated to v5.0

**CHANGES FROM v5.0 (Clinton County session):**
- **OBS-007**: `maps_raw` extended to Sites — §5.12 updated; Sites commonly have
  map URLs (ODNR park maps, nature preserve pages, trail system maps on a site page)
- **OBS-017**: Null-tier record format added to §11 — when a tier yields zero entities,
  a structured null-tier record must still be written to the staging file

------------------------------------------------------------
# 1. PURPOSE

This specification defines:

- The required fields for all Raw Discovery Records
- The structure of Site, Trail, Trail Segment, Trail Network, Site Network, and Access Point outputs
- The rules for raw (unnormalized) values
- The relationship between raw fields and Discovery Metadata v5.0
- The guarantees Discovery must provide to downstream modules
- The provenance and audit requirements for all raw outputs

This ensures that Discovery produces **consistent, deterministic, provenance-rich,
machine-readable** outputs for all six entity types.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All entities discovered in Tiers 1–8
- All entities surfaced via recursive discovery
- All entities surfaced via entity-specific discovery sub-procedures
- All baseline-seeded entities (Tier-0)
- All multi-tier discoveries
- All Access Points discovered via AP-specific workflows

It governs:

- Output structure
- Field requirements
- Raw value rules
- Provenance guarantees
- Integration with Resolution, Normalization, and Entity Graph modules

------------------------------------------------------------
# 3. RAW DISCOVERY RECORD STRUCTURE (TOP-LEVEL)

Each discovered entity must produce a **Raw Discovery Record v5.0** with the
following top-level fields:

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
  gps_raw:
  geometry_raw:
  address_raw:
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
- `"0"` for baseline-seeded entities
- `"AP"` for Access Point-specific workflows

## 4.6 `discovered_in_tiers`
- List of all tiers where the entity appeared
- Must include `"AP"` for AP-specific workflows

## 4.7 `discovery_metadata`
Must embed the full metadata object defined in the Discovery Metadata Specification v5.0, including:

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
**CRITICAL: Leave blank during web discovery.**
- Applies to: Sites, Trails, Trail Segments, Access Points
- Not discoverable from web sources
- Populated via GIS spatial lookup during normalization phase
- Discoverers must not attempt to determine township from web research

## 5.2 `municipality_raw`
**CRITICAL: Leave blank during web discovery.**
- Applies to: Sites, Trails, Trail Segments, Access Points
- Not discoverable from web sources
- Populated via GIS spatial lookup during normalization phase
- Discoverers must not attempt to determine municipality from web research

## 5.3 `parent_site_raw`
- Required for child Sites
- Optional for all other entity types

## 5.4 `parent_sites_raw`, `parent_trails_raw`, `parent_trail_segments_raw`
Lists of raw parent relationships discovered during:

- Tier discovery
- Entity-specific discovery
- Recursive discovery

## 5.5 `ownership_raw`
Applies to:

- Site
- Site Network
- Trail Network
- Trail (if ownership is explicit)
- Trail Segment (if ownership is explicit)

Values must be raw and unnormalized.

## 5.6 `gps_raw`
Applies to all entity types **if available**.

- May be point, centroid, or raw geometry anchor
- Must not be normalized
- Format: "lat,lon" string during discovery
- Converted to numeric gps_lat/gps_lon during normalization

## 5.7 `geometry_raw`
- Raw geometry if discovered (polygon, polyline, multipoint)
- Must not be simplified or normalized

## 5.8 `address_raw`
Include if available (Sites, Access Points).

## 5.9 `features_raw`
- Applies to: Sites, Access Points
- List or semicolon-delimited string of features/amenities discovered
- Examples: "restrooms;water fountain;parking (50 spaces);picnic tables"
- Must not be normalized or categorized
- Record exactly as discovered

## 5.10 `difficulty_raw`
- Applies to: Trails, Trail Segments
- Raw difficulty rating as stated by authoritative source
- Examples: "Easy", "Moderate", "Difficult", "Strenuous"
- Must not be assessed or inferred by discoverer
- Leave blank if not explicitly stated

## 5.11 `accessibility_raw`
- Applies to: Trails, Trail Segments
- Raw accessibility information as stated by authoritative source
- Examples: "ADA accessible", "Wheelchair accessible", "Paved surface suitable for wheelchairs"
- Must not be inferred from surface type alone
- Leave blank if not explicitly stated

## 5.12 `maps_raw`
- Applies to: **Sites**, Trails, Trail Segments, Trail Networks, Site Networks
- List of map URLs discovered
- May include: PDF maps, interactive maps, GPX files, KML files
- Preserve all discovered map URLs
- Do not deduplicate

Sites commonly have map URLs — ODNR park maps, nature preserve pages with embedded
trail maps, USACE project maps, county park PDF brochures. Capture these in
`maps_raw` for Sites just as you would for Trails.

## 5.13 `url_primary`
- The most authoritative URL
- Must not be invented

## 5.14 `url_all`
- List of all URLs used
- Must preserve order of discovery

## 5.15 `source_*` fields
Discovery must preserve:

- All datasets
- All maps
- All GIS layers
- All documents
- All photos
- All web pages

No deduplication unless identical.

## 5.16 `notes_raw`
- Any raw notes discovered
- Must not be interpreted or normalized

------------------------------------------------------------
# 6. ACCESS POINT-SPECIFIC FIELDS

## 6.1 `access_point_type_raw`
Examples:

- Trailhead
- Parking Area
- Boat Ramp
- Boat Launch
- Watercraft Access Point
- River Access
- Fishing Access
- Bicycle Access
- Snowmobile Access
- Cross Country Ski Access
- Equestrian Access
- Roadside Pull-Off
- Pedestrian Entrance
- Vehicle Entrance
- Transit Access
- Ferry Access
- Shuttle Access
- Administrative Access
- Other (explicitly named only)

## 6.2 `features_raw`
- Semicolon-delimited list of facilities and amenities at the access point
- Examples: "paved parking (50 spaces, 4 ADA);restrooms (ADA accessible);water fountain;bike racks;picnic tables (6);trail map kiosk"
- Must not be normalized
- Record exactly as discovered

## 6.3 Parent relationships
Access Points may include:

- `parent_sites_raw`
- `parent_trails_raw`
- `parent_trail_segments_raw`

## 6.4 GPS and address
Include if available during discovery.

------------------------------------------------------------
# 7. RAW VALUE RULES

## 7.1 No Normalization
Discovery must not normalize:

- Names
- Access Point Types
- Features
- Difficulty
- Accessibility
- Ownership
- Addresses
- GPS
- Geometry
- URLs
- Maps

## 7.2 No Invention
Discovery must not invent:

- Names
- Access Point Types
- Features
- Parents
- URLs
- GPS
- Geometry
- Ownership
- Difficulty
- Accessibility

## 7.3 No Silent Corrections
Malformed values must be:

- Preserved exactly
- Logged in metadata
- Resolved downstream

## 7.4 No Inference
Discovery must not infer:

- Township (leave blank — GIS-derived)
- Municipality (leave blank — GIS-derived)
- Difficulty (only record if explicitly stated)
- Accessibility (only record if explicitly stated)
- Parent relationships (must be documented)

------------------------------------------------------------
# 8. MULTI-COUNTY RULE (v5.0)

Discovery outputs must follow the authoritative multi-county rule:

- **No segmentation** of multi-county entities
- **Record all counties** in `counties_raw`
- `county_primary` = county currently being processed
- Normalization alphabetizes and converts to array format
- Resolution determines final county list if sources conflict

------------------------------------------------------------
# 9. BASELINE INTEGRATION (TIER-0)

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
  township_raw:              # Leave blank - GIS-derived
  municipality_raw:          # Leave blank - GIS-derived
  parent_site_raw:
  parent_sites_raw: []
  parent_trails_raw: []
  parent_trail_segments_raw: []
  access_point_type_raw:
  ownership_raw:
  gps_raw:
  geometry_raw:
  address_raw:
  features_raw:              # NEW in v5.0
  difficulty_raw:            # NEW in v5.0
  accessibility_raw:         # NEW in v5.0
  maps_raw: []               # NEW in v5.0; applies to Sites, Trails, Trail Segments, Trail Networks, Site Networks
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
# 11. NULL-TIER RECORD FORMAT

When a discovery tier yields zero entities, the tier must still be documented in
the staging file. A null-tier record is NOT a Raw Discovery Record — it is a
tier-level audit entry. It must be written to the staging file immediately after
completing the tier's search.

## 11.1 Required Format

```yaml
tier_result:
  tier: [integer 1–8]
  category: [tier category name, e.g., "Federal & Tribal"]
  result: null
  entities_count: 0
  sources_checked:
    - [URL or source description]
    - [URL or source description]
  search_queries:
    - "[query text]"
    - "[query text]"
  notes: >
    [Narrative: what was searched, what was found, why the tier is null.
    Include any redirects, 404s, or authoritative "no results" confirmations.]
  date: [ISO date, e.g., 2026-02-28]
  discoverer_session: [session ID]
```

## 11.2 Rules

- A null-tier record is **mandatory** — a tier with no record is a discovery defect
- The null-tier record must appear in the staging file in tier order
- `sources_checked` must list every URL or source that was consulted
- `search_queries` must list every search string used
- `notes` must explain the null result — "no federal land in county" is acceptable
  when supported by sources; "not searched" is a defect
- Null-tier records are not passed to the Resolution Engine (they are audit artifacts)

## 11.3 Example

```yaml
tier_result:
  tier: 1
  category: Federal & Tribal
  result: null
  entities_count: 0
  sources_checked:
    - https://www.fs.usda.gov/wayne (checked — no Clinton County units)
    - https://www.nps.gov/findapark (checked — no NPS units in Clinton County)
    - https://fws.gov/refuges (checked — no USFWS refuges in Clinton County)
    - https://www.usace.army.mil (checked — no USACE projects in Clinton County)
  search_queries:
    - "Clinton County Ohio federal land"
    - "Clinton County Ohio national park forest wildlife refuge"
  notes: >
    No federal land units confirmed in Clinton County. Wayne National Forest
    does not extend to Clinton County. No NPS, USFWS, USACE, or BLM holdings
    confirmed by federal agency websites or county GIS.
  date: 2026-01-15
  discoverer_session: CLINTON-OH-20260115-001
```

------------------------------------------------------------
# 12. DEVELOPER PREVIEW TSVs

Discovery may output TSV-formatted previews of Raw Discovery Records upon explicit
user request. These previews:

- Use raw values only
- Follow the TSV field order for the entity type
- Must not be interpreted as normalized TSV output
- Are not part of the official Discovery → Resolution → Normalization pipeline
- Are intended solely for debugging and inspection

------------------------------------------------------------
# 13. INTEGRATION POINTS

This specification integrates with:

- Discovery Protocol Module v5.0
- Discovery Orchestration Module v5.0
- All Tier Sub-Procedures v5.0
- All Entity Discovery Sub-Procedures v5.0
- Discovery Metadata Specification v5.0
- Resolution Engine v5.0
- Normalization Engine v5.0
- Entity Upsert Engine v5.0
- TSV Output Specifications v5.0
- Audit & Logging Module v5.0
- County Baseline Module v5.0

No other module may reference this specification directly.

------------------------------------------------------------
# 14. VERSIONING

- This module is **Discovery Output Specification v5.0**.
- Any change to output structure requires v5.1, v5.2, etc.
- Any change to tier order or workflow must be made in the Discovery Protocol Module v5.0.

------------------------------------------------------------
# END OF DISCOVERY OUTPUT SPECIFICATION v5.0
