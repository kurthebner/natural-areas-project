# NATURAL AREAS PROJECT
# SITE DISCOVERY SUB-PROCEDURE v5.4
(Authoritative Sub-Procedure for Discovering Sites and Child Sites)

This module defines the authoritative, deterministic workflow for discovering
Sites (including child Sites) across all discovery tiers within the v5.x
Raw → Resolution → Normalization → Entity Graph pipeline.

This document supersedes all v4.x and v5.3 Site discovery logic.

------------------------------------------------------------
# CHANGES FROM v5.3 → v5.4

- Expanded `description_raw` guidance: where to look, what constitutes narrative description, verbatim capture rule
- Expanded `features_raw` guidance: where to look, list vs. narrative distinction, raw-only rule
- Added FIRST-PASS CAPTURE RULE: all descriptive fields must be captured in a single page fetch — no deferred return visits
- Added GOVERNANCE_RAW CONTAMINATION RULE: GIS administrative labels (park type, zone classification) must never be written to governance_raw; they belong in category_raw or identity_notes_raw
- Bumped version to v5.4

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.3

- Updated module version to v5.3
- Updated all cross-module references to v5.x
- Updated organizational field cluster to four-field model:
  ownership_raw, governance_raw, partner_agencies_raw, coordination_raw
- Added guidance for collecting partner_agencies_raw (formal partners only)
- Added guidance for collecting coordination_raw (community/volunteer partners only)
- No changes to discovery philosophy or mechanics
- Updated output field model to v5.3:
  gps_raw replaced by gps_lat_raw and gps_lon_raw (split at source)
  geometry_raw removed (GIS-derived geometry prohibited during discovery)
  maps_raw removed; all map URLs recorded in urls_raw
  url_primary renamed to url_primary_raw
  url_all renamed to urls_raw
  notes_raw renamed to identity_notes_raw
- Discovery Output Specification v5.x retired; all references now v5.x
- No changes to required fields or extraction behavior

------------------------------------------------------------
# 1. PURPOSE

The Site Discovery Sub-Procedure v5.3 provides the authoritative workflow for:

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
- Record uncertainty in identity_notes_raw
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
Record a narrative description of the Site exactly as found on the authoritative source. Aim for 1–3 sentences; capture more if the source provides a rich description that would be lost.

Description text is narrative prose — complete sentences that convey the Site’s character, ecology, history, community purpose, or significance. It is almost always in paragraph form on a park webpage, brochure, or PDF.

**Where to find description text:**
- Park homepage: introductory or "About" paragraph
- Brochure or downloadable PDF: opening description section
- Agency website: "About this park," "Overview," or "Park Description" section

**Capture rules:**
- Record verbatim — do not paraphrase, summarize, or combine multiple sources
- If no narrative paragraph is found, leave blank — do not invent or synthesize
- Do not record bullet-point amenity lists here — those belong in features_raw
- Do not record the Site name, address, or acreage here — those have their own fields

### features_raw (OPTIONAL)
Record all amenities, facilities, and physical features exactly as listed by the authoritative source.

Features are items from a list — typically shown as bullet points, icon grids, searchable checkboxes, or a "Park Amenities," "Facilities," or "What’s Here" section. They are NOT narrative sentences.

**Where to find features:**
- Park homepage: amenity icon grid, "Facilities" or "Amenities" section
- Parks search or filter page: checkbox-style feature tags attached to the park record
- Brochure or PDF: amenity list or map legend items
- Interactive park finder: feature tags or icons assigned to the park

**Capture rules:**
- Record verbatim as a comma-separated or semicolon-separated list matching the source’s own formatting: e.g., "Picnic shelter, restrooms, fishing pond, playground"
- Do NOT record narrative sentences — those belong in description_raw
- Do NOT record features that are actually Trails, child Sites, or Access Points
- Do NOT infer or assume features based on category — only record what the source explicitly states
- The Normalization Engine maps features_raw tokens to controlled vocabulary; raw capture is correct and expected — do not attempt to normalize during discovery

### FIRST-PASS CAPTURE RULE ✨ NEW IN v5.4

When fetching a park’s page, capture description_raw AND features_raw in the same page fetch. A single well-executed page fetch from an authoritative source should yield all of the following without a return visit:
- name_raw, category_raw (if stated), designation_raw (if stated)
- ownership_raw, governance_raw (NEVER include GIS park type labels — see rule below)
- description_raw (the narrative paragraph, if present)
- features_raw (the amenity/facility list, if present)
- location_raw, acres_raw (if stated)
- urls_raw (all URLs including PDFs and maps)

**Returning to a source that was already fetched to collect fields that were available on first visit is a process failure. Capture everything in one pass.**

If a page must be fetched twice (e.g., it was initially fetched for entity identification and detail was missed), document this explicitly in identity_notes_raw.

### GOVERNANCE_RAW CONTAMINATION RULE ✨ NEW IN v5.4

governance_raw must contain only the name(s) of the managing or operating organization(s). It must never contain GIS administrative classification labels.

**Never write to governance_raw:**
- GIS park type labels (e.g., "Community Park," "Neighborhood Park," "Mini Park")
- GIS zone or layer classifications (e.g., "Open Space Layer A," "Park Tier 2")
- ArcGIS field values that describe administrative category, not the managing organization

**If a GIS source provides park type metadata alongside the managing organization:**
- governance_raw: `City of Dublin` ✓
- governance_raw: `City of Dublin; GIS park type: Community Park` ✗

GIS park type labels are category hints, not governance. Record them in category_raw or identity_notes_raw if useful, and discard them from governance_raw entirely.

This rule applies to all GIS import sources (MORPC, county auditor GIS, municipal GIS layers, etc.).

### identity_notes_raw (OPTIONAL)
Record anything noteworthy that doesn’t fit elsewhere: identity conflicts, boundary uncertainties, dual-name situations, deferred capture notes, GIS import metadata.

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

### gps_lat_raw (OPTIONAL)
Record latitude only if explicitly provided by authoritative source. Do not infer or derive.

### gps_lon_raw (OPTIONAL)
Record longitude only if explicitly provided by authoritative source. Do not infer or derive.

------------------------------------------------------------
## 7.5 URL and Map Fields

### url_primary_raw (OPTIONAL)
Record the most authoritative URL.

### urls_raw (OPTIONAL)
Record all URLs discovered, including map URLs (PDFs, JPGs, interactive viewers); do not deduplicate.

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
- urls_raw includes all URLs (primary, secondary, and map URLs); not deduplicated
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
# END OF SITE DISCOVERY SUB-PROCEDURE v5.3