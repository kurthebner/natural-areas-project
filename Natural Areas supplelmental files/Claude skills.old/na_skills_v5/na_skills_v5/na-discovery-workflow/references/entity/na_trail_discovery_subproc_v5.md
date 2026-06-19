# NATURAL AREAS PROJECT
# TRAIL DISCOVERY SUB-PROCEDURE v5.0
(Authoritative Sub-Procedure for Discovering Trails)

This module defines the authoritative, deterministic workflow for discovering
**Trails** across all discovery tiers within the v5.0
Raw → Resolution → Normalization → Entity Graph pipeline.

This document supersedes all v4.x Trail discovery logic.

------------------------------------------------------------
# CHANGES FROM v4.0

- **Philosophy clarified**: Discovery = Collection, Normalization = Decisions
- **Source mapping added**: Track which fields came from which URLs
- **Field changes**: Removed network_affiliation, added difficulty, accessibility, maps array
- **Governance terminology**: managing_agency_raw → governance_raw, added partner_agencies_raw
- **Complete rewrite**: Enhanced practical guidance for discoverers
- All version references updated to v5.0

------------------------------------------------------------
# 1. PURPOSE

The Trail Discovery Sub-Procedure v5.0 provides the authoritative workflow for:

- Identifying Trail candidates
- Extracting raw, unnormalized metadata
- Supporting enumerative and recursive discovery
- Preventing misclassification across the six-entity ontology
- Recording tier and URL provenance with field-level source mapping
- Emitting Raw Discovery Records v5.0
- Emitting Discovery Metadata v5.0
- Integrating cleanly with Trail Segment, Trail Network, and Access Point discovery
- Feeding the Resolution Engine v5.0

A **Trail** is:

- A named, identity-bearing linear corridor
- Documented in authoritative sources
- Distinct from Trail Segments
- Distinct from Trail Networks
- Distinct from Sites and child Sites
- Not an Access Point or amenity
- Not a temporary or unnamed connector

This module is authoritative for Trail discovery.

------------------------------------------------------------
# 2. DISCOVERY PHILOSOPHY (v5.0)

## 2.1 Core Principle: Discovery = Collection, Normalization = Decisions

**Discovery Phase (YOU ARE HERE):**
- Collect everything you find
- Record exactly as found
- Don't normalize, standardize, or choose between values
- Don't deduplicate URLs or map links
- Don't make vocabulary decisions
- Fast, mechanical extraction

**Normalization Phase (LATER):**
- Standardize vocabulary ("bike trail" → proper trail_use_type)
- Deduplicate URLs and maps
- Choose canonical values
- Validate and clean

## 2.2 When in Doubt: Collect It

If you're unsure whether to include something:
- Include it
- Record it in notes_raw if uncertain
- Let Resolution/Normalization decide

## 2.3 Multiple Sources = Multiple Records

If you find the same Trail at multiple URLs:
- Emit SEPARATE discovery records
- Do NOT attempt to merge
- Do NOT detect conflicts
- Resolution engine handles merging

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
9. Tier-0 Baseline (non-authoritative; runs last)

Each tier must surface Trail candidates when applicable.

------------------------------------------------------------
# 4. REQUIRED SOURCES

Each tier must check the following for Trail references:

- Official agency websites
- Authoritative listing/index pages (e.g., `/trails/`, `/bikeways/`)
- GIS systems and interactive trail maps
- Trail brochures and downloadable maps
- Park district trail pages
- Statewide trail inventories
- Federal trail inventories
- Regional greenway or bikeway plans
- Trail signage programs
- Digitally documented trailhead kiosks
- Planning documents (master plans, corridor plans)
- Multi-trail system documents (for individual trail extraction)
- GPX/KML download pages

All sources must be logged in **Discovery Metadata v5.0** and **source_map**.

------------------------------------------------------------
# 5. IDENTITY RULES FOR TRAIL CANDIDATES

A Trail candidate is valid only if:

1. It is explicitly documented as a **named linear corridor**.
2. It has a **stable, identity-bearing name**.
3. It is **not merely a segment** of a larger Trail.
4. It is **not a Trail Network** (umbrella over multiple Trails).
5. It is **not a Site or child Site**.
6. It is **not an Access Point or amenity**.
7. It is **not a temporary or unnamed connector**.

If any condition fails, the candidate must not be created.

------------------------------------------------------------
# 6. DISCOVERY WORKFLOW

## 6.1 Step 1 — Identify Named Trails

Search all required sources for:

- Named trails
- Named loops
- Named linear corridors
- Named bikeways or greenways
- Named water trails
- Named equestrian trails
- Named multi-use trails
- Named rail trails
- Named canal towpath trails

Record each appearance as a raw Trail candidate.

## 6.2 Step 2 — Verify Identity-Bearing Name

A Trail must have:

- A documented, stable name
- Not a temporary project name
- Not a marketing slogan
- Not a generic label unless officially used

If ambiguous, flag for review in notes_raw.

## 6.3 Step 3 — Confirm Trail-Level Identity

The candidate must:

- Represent a full linear corridor
- Not be a single segment
- Not be a cluster of segments
- Not be a Trail Network

If unclear, flag for review in notes_raw.

------------------------------------------------------------
# 7. FIELD-BY-FIELD EXTRACTION GUIDE

## 7.1 Core Identity Fields

### `name_raw` (REQUIRED)
**What to collect:**
- Official published trail name exactly as written
- Don't normalize capitalization
- Don't add or remove words

**Examples:**
- "Slippery Elm Trail" ✅
- "slippery elm trail" ✅ (record as shown)
- "Slippery Elm Bike Trail" ✅ (if that's what source says)

**What NOT to do:**
- ❌ Don't standardize: "Elm Trail" when source says "Slippery Elm Trail"
- ❌ Don't add type: "Slippery Elm Trail (Multi-Use)" when just "Slippery Elm Trail"

### `alternate_names_raw` (OPTIONAL) ✅ KEPT IN v5.0
**What to collect:**
- Official abbreviations: "North Country National Scenic Trail" → "NCT"
- Former names documented in sources
- Local names if officially recognized
- Variant names from different sources

**Semicolon-delimited:**
- "NCT;North Country Trail;North Country NST"

**What NOT to do:**
- ❌ Don't invent abbreviations
- ❌ Don't include nicknames unless officially used
- ❌ Only record documented alternate names

### `trail_use_type_raw` (OPTIONAL)
**What to collect:**
- Multi-Use, Hiking, Mountain Biking, Bridle, Water, Cross-Country Ski

**Record exactly as source describes:**
- Source says "multi-use trail" → record "multi-use"
- Source says "bike trail" → record "bike trail"
- Don't normalize vocabulary

### `trail_surface_type_raw` (OPTIONAL)
**What to collect:**
- Paved, Crushed Stone, Gravel, Natural Surface, Boardwalk, Water

**Record exactly as found:**
- "asphalt" → record "asphalt" (normalization standardizes to "Paved")
- "gravel and dirt" → record "gravel and dirt"
- Don't choose or normalize

### `trail_origin_type_raw` (OPTIONAL)
**What to collect:**
- Rail Trail, Canal Towpath, Purpose-Built, Historic Route

**Only if explicitly stated:**
- Source says "former railroad corridor" → record "former railroad corridor"
- Source says "canal towpath" → record "canal towpath"
- Don't guess from context

### `status_raw` (OPTIONAL)
**What to collect:**
- Active, Planned, Under Construction, Closed, Seasonal

**Only if explicitly stated:**
- Don't infer from maps or imagery

## 7.2 Physical Characteristics

### `total_length_miles_raw` (OPTIONAL)
**What to collect:**
- Number only: "12.5", "3.2", "45"
- If source says "12.5 miles" → record "12.5"

**What NOT to do:**
- ❌ Don't estimate from maps
- ❌ Don't calculate from segments
- ❌ Only record if explicitly stated

### `counties_raw` (REQUIRED)
**What to collect:**
- All counties the trail traverses
- Multiple counties: semicolon-delimited

**Examples:**
- "Wood" ✅
- "Wood;Lucas;Ottawa" ✅
- "Wood County" → record "Wood County" (normalization removes "County")

### `county_primary` (REQUIRED)
**What to record:**
- The county YOU are currently discovering in
- This is your discovery tier context

## 7.3 NEW v5.0 Fields

### `difficulty_raw` (OPTIONAL) ✨ NEW
**What to collect:**
- Difficulty rating ONLY if explicitly stated by trail manager
- Easy, Moderate, Difficult, Strenuous, Expert

**CRITICAL - Do NOT assess difficulty yourself:**
- ✅ Source says "Easy" → record "Easy"
- ✅ Source says "Moderate to Difficult" → record "Moderate to Difficult"
- ❌ Trail looks easy to you → leave blank
- ❌ You think it should be rated Difficult → leave blank

**Only record what authoritative sources state.**

### `accessibility_raw` (OPTIONAL) ✨ NEW
**What to collect:**
- Accessibility information ONLY if explicitly stated
- ADA accessible, wheelchair accessible, paved surface suitable for wheelchairs

**Record exactly as stated:**
- "ADA compliant" → record "ADA compliant"
- "Wheelchair accessible for first mile" → record "Wheelchair accessible for first mile"
- "Paved, flat surface, suitable for wheelchairs" → record as found

**What NOT to do:**
- ❌ Don't infer from surface type ("paved" ≠ "accessible")
- ❌ Don't assess yourself
- ❌ Only record what source explicitly states

## 7.4 Governance Fields

### `governance_raw` (OPTIONAL)
**What to collect:**
- Primary managing agency/organization
- "Wood County Park District", "Ohio Department of Natural Resources", "Buckeye Trail Association"

**Record exactly as stated:**
- Source says "managed by WCPD" → record "WCPD" (or full name if available)
- Source says "Ohio DNR" → record "Ohio DNR"

### `partner_agencies_raw` (OPTIONAL) ✨ NEW
**What to collect:**
- Secondary managing agencies or land managers
- Important for trails crossing multiple jurisdictions

**Semicolon-delimited:**
- "Cleveland Metroparks;Summit Metro Parks;Ohio & Erie Canal Towpath Coalition"

**Only if explicitly documented:**
- Look for "in partnership with...", "co-managed by..."
- Don't infer partnerships

## 7.5 Descriptive Fields

### `description_raw` (OPTIONAL)
**What to collect:**
- 1-3 sentence description of the trail
- Focus on WHAT the trail IS, not amenities

**Copy directly or summarize minimally:**
- Trail's own description is best

**What NOT to include:**
- ❌ List of access points (that's different entity type)
- ❌ Amenities (surfaces are in surface_type)
- ❌ Governance (goes in governance_raw)

### `trail_history_raw` (OPTIONAL) ✅ KEPT IN v5.0
**What to collect:**
- Historical context about the trail
- Railroad history for rail trails
- Canal history for towpath trails
- Historic route information
- Establishment date

**Examples:**
- "Former Penn Central Railroad corridor, converted to trail in 1985"
- "Follows historic Miami & Erie Canal towpath from 1845"
- "Designated National Scenic Trail in 1968"

**Only if explicitly documented:**
- Don't research history yourself
- Record what sources state

### `notes_raw` (OPTIONAL)
**What to collect:**
- Anything noteworthy that doesn't fit other fields
- Seasonal closures
- Access restrictions
- Construction updates
- Uncertainties or clarifications

## 7.6 URL and Map Fields

### `url_primary` (OPTIONAL)
**What to collect:**
- The single most authoritative URL for this trail
- Usually the trail's dedicated page

**Example:**
- https://wcparks.org/trails/slippery-elm-trail/ ✅

### `url_all` (OPTIONAL)
**What to collect:**
- ALL URLs you find for this trail
- Don't deduplicate, don't choose, collect all

**Examples:**
- https://wcparks.org/trails/slippery-elm-trail/
- https://traillink.com/trail/slippery-elm-trail/
- https://alltrails.com/trail/slippery-elm-trail

**Semicolon-delimited:**
- "https://wcparks.org/trails/slippery-elm-trail/;https://traillink.com/trail/slippery-elm-trail/"

### `maps_raw` (OPTIONAL) ✨ NEW - RICH ARRAY
**What to collect:**
- ALL map URLs you find
- PDF maps, interactive maps, GIS viewers, GPX downloads, KML files, elevation profiles

**Don't deduplicate, just collect:**
- Trail map PDF: collect it
- Interactive GIS viewer: collect it
- GPX file download: collect it
- Elevation profile: collect it
- Turn-by-turn guide: collect it

**Examples:**
- https://wcparks.org/maps/slippery-elm-trail.pdf
- https://wcparks.org/trails/interactive-map
- https://wcparks.org/gpx/slippery-elm.gpx
- https://ridewithgps.com/routes/slippery-elm-trail

**Semicolon-delimited:**
- "https://wcparks.org/maps/trail.pdf;https://wcparks.org/gpx/trail.gpx;https://gis.county.gov/trails/"

**IMPORTANT - Collect all map types:**
- Static PDF maps
- Interactive web viewers
- GPX/KML files
- Elevation profiles
- Route guides
- Trail condition maps

------------------------------------------------------------
# 8. PROVENANCE TRACKING (v5.0)

## 8.1 Source Mapping (REQUIRED) ✨ NEW IN v5.0

**For each discovery record, maintain source_map:**

Track which fields came from which URLs.

**Format:**
```json
{
  "source_map": {
    "https://wcparks.org/trails/": ["name", "governance", "url_primary"],
    "https://wcparks.org/trails/slippery-elm/": [
      "total_length_miles", "surface_type", "description", 
      "trail_history", "difficulty", "accessibility", "maps"
    ],
    "https://traillink.com/trail/slippery-elm/": ["alternate_names", "trail_use_type"]
  }
}
```

**Guidelines:**
- Group fields by the URL they came from
- Don't need to track which paragraph
- URL-level granularity is sufficient

## 8.2 Multiple Sources = Multiple Records

**If you encounter the same trail at multiple URLs:**

- Emit SEPARATE discovery records
- Each with its own source_map
- Do NOT attempt to merge
- Do NOT detect conflicts
- Resolution engine will handle merging

**Example:**
```
Record 1: From Wood County Parks site
  - name, governance, length, surface
  
Record 2: From TrailLink
  - name, length (different value!), description
  
Resolution will merge these 2 records and handle the length conflict.
```

------------------------------------------------------------
# 9. WHAT NOT TO DO (CRITICAL)

## 9.1 Don't Normalize or Standardize
- ❌ Don't change capitalization
- ❌ Don't fix typos in trail names
- ❌ Don't standardize terminology ("bike path" → "Multi-Use Trail")
- ❌ Don't choose between synonyms
- Record exactly as found

## 9.2 Don't Deduplicate
- ❌ Don't deduplicate URLs
- ❌ Don't deduplicate map links
- ❌ Don't choose "best" URL or map
- Collect everything, normalization decides

## 9.3 Don't Merge or Detect Conflicts
- ❌ Don't merge records from multiple sources
- ❌ Don't try to detect if values conflict
- ❌ Don't choose between conflicting values
- Emit separate records, Resolution handles merging

## 9.4 Don't Assess or Judge
- ❌ Don't assess difficulty yourself
- ❌ Don't judge accessibility yourself
- ❌ Don't rate trail quality
- ❌ Only record what sources explicitly state

## 9.5 Don't Infer or Guess
- ❌ Don't infer origin type from name ("Elm Trail" ≠ rail trail)
- ❌ Don't guess GPS coordinates
- ❌ Don't calculate length from maps
- ❌ Don't estimate difficulty
- Only record explicitly documented information

## 9.6 Don't Create Segments or Access Points
- ❌ Don't create Trail Segments here
- ❌ Don't create Access Points here
- ❌ Just note them in raw references
- They have their own discovery sub-procedures

------------------------------------------------------------
# 10. TRAIL SEGMENTS AND ACCESS POINTS

## 10.1 Trail Segments (Non-Authoritative)
**If source mentions trail segments:**
- Record segment names in notes_raw as raw references only
- Do NOT create Trail Segment entities here
- Trail Segment Discovery Sub-Procedure v5.0 handles these

## 10.2 Trail Network Membership (Non-Authoritative)
**If source mentions the trail is part of a network:**
- Record network name in notes_raw
- Do NOT create network relationships here
- Resolution/Normalization handles network membership

## 10.3 Access Points (Non-Authoritative)
**If source shows trailheads or access points:**
- Record access point names in notes_raw as raw references
- Do NOT create Access Point entities here
- Access Point Discovery Sub-Procedure v5.0 handles these

------------------------------------------------------------
# 11. TIER-SPECIFIC EXPECTATIONS

## 11.1 Federal Tier (Tier 1)
Must surface:
- National Scenic Trails
- National Historic Trails
- National Recreation Trails
- Federally documented water trails

## 11.2 State Tier (Tier 2)
Must surface:
- State-designated trails
- Statewide trail corridors
- State water trails
- State greenway or bikeway systems (individual trails)

## 11.3 District Tier (Tier 3)
Must surface:
- All named trails within district boundaries
- All named loops
- All named multi-use trails

## 11.4 County Tier (Tier 4)
May surface:
- Countywide bikeways
- Countywide greenways
- County-managed trail corridors

## 11.5 Township & Municipal Tiers (Tiers 5-6)
May surface:
- Local named trails
- Local greenways
- Local bikeways
- Municipal trail systems

## 11.6 Conservancy Tier (Tier 7)
May surface:
- Named trails within preserves
- Named loops
- Named access corridors

## 11.7 Private Tier (Tier 8)
May surface:
- Privately managed named trails open to public
- Campus-scale trail systems (individual trails)

------------------------------------------------------------
# 12. OUTPUT REQUIREMENTS

Each Trail candidate must output:

**Raw Discovery Record conforming to:**
- **Discovery Output Specification v5.0**
- **Trail Schema Module v5.0**
- **Discovery Metadata Specification v5.0**

**Must include:**
- All extracted fields (raw, unnormalized)
- Complete source_map
- Raw segment references (in notes)
- Raw network membership references (in notes)
- Raw Access Point references (in notes)

**Must NOT include:**
- Normalized values
- Merged data from multiple sources
- Inferred or guessed values
- Assessed difficulty or accessibility (only recorded if stated)
- Created Trail Segments or Access Points

------------------------------------------------------------
# 13. QUALITY CHECKLIST

Before emitting a discovery record, verify:

- ✅ name_raw is recorded exactly as found
- ✅ All available fields extracted
- ✅ source_map populated with URL → fields mapping
- ✅ No normalization or standardization applied
- ✅ Multiple URLs collected, not deduplicated
- ✅ Multiple maps collected, not deduplicated
- ✅ difficulty_raw only included if explicitly stated by source
- ✅ accessibility_raw only included if explicitly stated by source
- ✅ No inferred or guessed values
- ✅ No created segments or access points (just raw references)
- ✅ alternate_names recorded if documented
- ✅ trail_history recorded if available

------------------------------------------------------------
# 14. INTEGRATION POINTS

This module integrates with:

- **Discovery Protocol Module v5.0**
- **Tier Sub-Procedure Template v5.0**
- **Trail Schema Module v5.0**
- **Trail Vocabulary Module v5.0**
- **Trail Segment Discovery Sub-Procedure v5.0**
- **Trail Network Discovery Sub-Procedure v5.0**
- **Access Point Discovery Sub-Procedure v5.0**
- **Discovery Output Specification v5.0**
- **Discovery Metadata Specification v5.0**
- **Resolution Engine v5.0**
- **Normalization Engine v5.0**
- **TSV Output Specifications v5.0**
- **Audit & Logging Module v5.0**

------------------------------------------------------------
# END OF TRAIL DISCOVERY SUB-PROCEDURE v5.0
