# NATURAL AREAS PROJECT
# SITE DISCOVERY SUB-PROCEDURE v5.2
(Authoritative Sub-Procedure for Discovering Sites and Child Sites)

This module defines the authoritative, deterministic workflow for discovering
Sites (including child Sites) across all discovery tiers within the v5.x
Raw → Resolution → Normalization → Entity Graph pipeline.

This document supersedes all v4.x Site discovery logic.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.2

- Updated module version to v5.2
- Updated all cross-module references to v5.x
- Updated organizational field cluster to four-field model:
  ownership_raw, governance_raw, partner_agencies_raw, coordination_raw
- Added guidance for collecting partner_agencies_raw (formal partners only)
- Added guidance for collecting coordination_raw (community/volunteer partners only)
- No changes to discovery philosophy or mechanics
- No changes to required fields or extraction behavior

------------------------------------------------------------
# 1. PURPOSE

The Site Discovery Sub-Procedure v5.2 provides the authoritative workflow for:

- Identifying Site and child Site candidates
- Extracting raw, unnormalized metadata
- Supporting enumerative and recursive discovery
- Preventing misclassification across the six-entity ontology
- Recording tier and URL provenance with field-level source mapping
- Emitting Raw Discovery Records v5.x
- Emitting Discovery Metadata v5.x
- Integrating cleanly with Resolution Engine v5.x

A Site is:
- A named, identity-bearing land unit
- Documented in authoritative sources
- May be a top-level Site or a child Site
- Distinct from Trails, Trail Segments, Trail Networks, Site Networks, and Access Points
- Not an amenity, feature, or temporary management zone

A child Site is an internal identity-bearing unit that meets the criteria in
the Child Site Rules Module v5.x and is represented as a Site with a Parent Site.

This module is authoritative for Site discovery.

------------------------------------------------------------
# 2. DISCOVERY PHILOSOPHY (v5.x)

## 2.1 Core Principle: Discovery = Collection, Normalization = Decisions

Discovery Phase:
- Collect everything you find
- Record exactly as found
- Do not normalize, standardize, or choose between values
- Do not deduplicate URLs or map links
- Do not make vocabulary decisions
- Do not make presentation decisions

Normalization Phase:
- Standardizes vocabulary
- Deduplicates URLs
- Chooses canonical values
- Validates and cleans
- Makes decisions without revisiting websites

## 2.2 When in Doubt: Collect It
If unsure whether to include something:
- Include it
- Record uncertainty in notes_raw
- Let Resolution/Normalization decide

## 2.3 Multiple Sources = Multiple Records
If the same Site appears at multiple URLs:
- Emit separate discovery records
- Do not merge
- Do not detect conflicts
- Resolution handles merging

------------------------------------------------------------
# 3. SCOPE

This sub-procedure applies to all discovery tiers:

1. Federal
2. State
3. District
4. County
5. Township
6. Municipal
7. Conservancy
8. Private
9. Tier-0 Baseline

Each tier must surface Site candidates when applicable.

------------------------------------------------------------
# 4. REQUIRED SOURCES

Each tier must check:

- Official agency websites
- Listing/index pages
- GIS systems and parcel-level data
- Park district site lists
- State and federal inventories
- Planning/stewardship documents
- County auditor parcel data
- Brochures and downloadable maps
- Historic district documentation
- Land trust preserve lists
- Private organization site lists
- Partnership announcements

All sources must be logged in discovery_metadata and source_map.

------------------------------------------------------------
# 5. IDENTITY RULES FOR SITE CANDIDATES

A Site candidate is valid only if:

1. It is explicitly documented as an identity-bearing land unit.
2. It has a stable, identity-bearing name.
3. It is not a Trail, Trail Segment, Trail Network, or Site Network.
4. It is not an Access Point.
5. It is not an amenity or feature.
6. It is not a temporary or unnamed management zone.
7. It is not a parcel unless documented as a Site.

A candidate may be a child Site if:
- It is an internal identity-bearing unit within a larger Site, and
- It meets the criteria in the Child Site Rules Module v5.x.

------------------------------------------------------------
# 6. DISCOVERY WORKFLOW

## 6.1 Step 1 — Identify Named Identity-Bearing Land Units
Search all required sources for:
- Parks, preserves, natural areas, wildlife areas, forests
- Conservation areas, historic sites, cemeteries
- Campuses, recreation areas, cultural/heritage sites
- Multi-parcel conservation lands

## 6.2 Step 2 — Verify Identity-Bearing Name
A Site must have:
- A documented, stable name
- Not a temporary project name
- Not a marketing slogan

## 6.3 Step 3 — Determine Whether Candidate Is a Child Site
If internal unit:
- Evaluate using Child Site Rules Module v5.x
- If valid → record parent_site_raw
- If not → treat as feature or ignore

## 6.4 Step 4 — Confirm Site-Level Identity
Candidate must represent a full identity-bearing land unit.

------------------------------------------------------------
# 7. FIELD-BY-FIELD EXTRACTION GUIDE

## 7.1 Core Identity Fields

### name_raw (REQUIRED)
Record exactly as written.

### category_raw (OPTIONAL)
Record exactly as stated; do not normalize.

### subtype_raw (OPTIONAL)
Record only if explicitly stated.

### designation_raw (OPTIONAL)
Record formal designations only.

### status_raw (OPTIONAL)
Record only if explicitly stated.

------------------------------------------------------------
## 7.2 Organizational Fields

### ownership_raw (OPTIONAL)
Record legal owner exactly as stated.

### governance_raw (OPTIONAL)
Record managing/operating organization(s).

### partner_agencies_raw (OPTIONAL) ✨ NEW IN v5.2
Record **formal, documented partner organizations**.
Examples:
- ODNR partnering with USACE
- County park district partnering with a state agency

Do NOT record:
- Volunteer groups
- Informal partners
- Community groups (those go in coordination_raw)

### coordination_raw (OPTIONAL)
Record **community-based, volunteer, or informal partners**.
Examples:
- Friends groups
- Volunteer trail associations

Do NOT record:
- Formal co-operators (those go in partner_agencies_raw)

------------------------------------------------------------
## 7.3 Descriptive Fields

### description_raw (OPTIONAL)
Record 1–3 sentence description as found.

### features_raw (OPTIONAL)
Record all features/amenities exactly as written.

### notes_raw (OPTIONAL)
Record anything noteworthy that doesn’t fit elsewhere.

------------------------------------------------------------
## 7.4 Location Fields

### location_raw (OPTIONAL)
Record address or geographic description exactly as found.

### acres_raw (OPTIONAL)
Record numeric value only.

### counties_raw (REQUIRED)
Record all counties mentioned.

### county_primary (REQUIRED)
Record the county you are discovering in.

### township_raw (LEAVE BLANK)
GIS-derived later.

### municipality_raw (LEAVE BLANK)
GIS-derived later.

### gps_raw (OPTIONAL)
Record only if explicitly provided.

### geometry_raw (OPTIONAL)
Record only if explicitly provided.

------------------------------------------------------------
## 7.5 URL and Map Fields

### url_primary (OPTIONAL)
Record the most authoritative URL.

### url_all (OPTIONAL)
Record all URLs; do not deduplicate.

### maps_raw (OPTIONAL)
Record all map URLs; do not deduplicate.

------------------------------------------------------------
## 7.6 Parent Site Field

### parent_site_raw (OPTIONAL)
Record parent Site name if explicitly documented.

------------------------------------------------------------
# 8. PROVENANCE TRACKING (v5.x)

## 8.1 Source Mapping (REQUIRED)
Track which fields came from which URLs.

## 8.2 Discovery Tier Context
Record tier_context_township, tier_context_municipality, county_primary.

## 8.3 Multiple Sources = Multiple Records
Emit separate records for each URL.

------------------------------------------------------------
# 9. WHAT NOT TO DO (CRITICAL)

- Do not discover township_raw or municipality_raw
- Do not normalize or standardize
- Do not deduplicate URLs or maps
- Do not merge or detect conflicts
- Do not infer ownership, governance, partner agencies, or parent sites
- Do not make category decisions

------------------------------------------------------------
# 10. TIER-SPECIFIC EXPECTATIONS
(unchanged from v5.0; all tiers remain required or optional as defined)

------------------------------------------------------------
# 11. OUTPUT REQUIREMENTS

Each Site candidate must output a Raw Discovery Record conforming to:
- Discovery Output Specification v5.x
- Site Schema Module v5.x
- Discovery Metadata Specification v5.x

------------------------------------------------------------
# 12. QUALITY CHECKLIST

- name_raw recorded exactly
- All available fields extracted
- source_map populated
- township_raw and municipality_raw blank
- No normalization applied
- URLs and maps not deduplicated
- Features recorded exactly
- GPS only if explicitly provided
- No inferred values
- Tier context documented

------------------------------------------------------------
# 13. INTEGRATION POINTS

This module integrates with:

- Discovery Protocol Module v5.x
- Tier Sub-Procedure Template v5.x
- Site Schema Module v5.x
- Site Vocabulary Module v5.x
- Child Site Rules Module v5.x
- Trail Discovery Sub-Procedure v5.x
- Trail Segment Discovery Sub-Procedure v5.x
- Access Point Discovery Sub-Procedure v5.x
- Site Network Discovery Sub-Procedure v5.x
- Discovery Output Specification v5.x
- Discovery Metadata Specification v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- TSV Output Specifications v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF SITE DISCOVERY SUB-PROCEDURE v5.2