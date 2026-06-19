# NATURAL AREAS PROJECT
# SITE DISCOVERY SUB-PROCEDURE v5.0
(Authoritative Sub-Procedure for Discovering Sites and Child Sites)

This module defines the authoritative, deterministic workflow for discovering
**Sites** (including **child Sites**) across all discovery tiers within the
v5.0 Raw → Resolution → Normalization → Entity Graph pipeline.

This document supersedes all v4.x Site discovery logic.

------------------------------------------------------------
# CHANGES FROM v4.0

- **Philosophy clarified**: Discovery = Collection, Normalization = Decisions
- **Source mapping added**: Track which fields came from which URLs
- **Tier context fields added**: Distinguish discovery context from actual location
- **Field changes**: Removed network_affiliation, municipality/township (GIS-derived), added features, maps array, location
- **Governance terminology**: management_raw → governance_raw
- **Complete rewrite**: Enhanced practical guidance for discoverers
- All version references updated to v5.0

------------------------------------------------------------
# 1. PURPOSE

The Site Discovery Sub-Procedure v5.0 provides the authoritative workflow for:

- Identifying Site and child Site candidates
- Extracting raw, unnormalized metadata
- Supporting enumerative and recursive discovery
- Preventing misclassification across the six-entity ontology
- Recording tier and URL provenance with field-level source mapping
- Emitting Raw Discovery Records v5.0
- Emitting Discovery Metadata v5.0
- Integrating cleanly with Resolution Engine v5.0

A **Site** is:

- A named, identity-bearing land unit
- Documented in authoritative sources
- May be a top-level Site or a child Site
- Distinct from Trails, Trail Segments, Trail Networks, Site Networks, and Access Points
- Not an amenity, feature, or temporary management zone

A **child Site** is an internal identity-bearing unit that meets the criteria in
the **Child Site Rules Module v5.0** and is represented as a **Site with a Parent Site**.

This module is authoritative for Site discovery.

------------------------------------------------------------
# 2. DISCOVERY PHILOSOPHY (v5.0)

## 2.1 Core Principle: Discovery = Collection, Normalization = Decisions

**Discovery Phase (YOU ARE HERE):**
- Collect everything you find
- Record exactly as found
- Don't normalize, standardize, or choose between values
- Don't deduplicate URLs or map links
- Don't make vocabulary decisions
- Don't make presentation decisions
- Fast, mechanical extraction

**Why?**
- Discovery is expensive (web research time)
- Normalization is cheap (data processing)
- Better to over-collect than under-collect
- Can't go back to website during normalization

**Normalization Phase (LATER):**
- Standardize vocabulary ("bathroom" → "restrooms")
- Deduplicate URLs
- Choose canonical values
- Validate and clean
- Make decisions WITHOUT revisiting websites

## 2.2 When in Doubt: Collect It

If you're unsure whether to include something:
- Include it
- Record it in notes_raw if uncertain
- Let Resolution/Normalization decide

## 2.3 Multiple Sources = Multiple Records

If you find the same Site at multiple URLs:
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

Each tier must surface Site candidates when applicable.

------------------------------------------------------------
# 4. REQUIRED SOURCES

Each tier must check the following for Site references:

- Official agency websites
- Authoritative listing/index pages (e.g., `/parks/`, `/properties/`)
- GIS systems and parcel-level data
- Park district site lists
- State and federal inventories
- Planning and stewardship documents
- County auditor parcel data
- Brochures and downloadable maps
- Historic district or cultural landscape documentation
- Land trust preserve lists
- Private organization site lists
- Partnership announcements

All sources must be logged in **Discovery Metadata v5.0** and **source_map**.

------------------------------------------------------------
# 5. IDENTITY RULES FOR SITE CANDIDATES

A Site candidate is valid only if:

1. It is explicitly documented as an identity-bearing land unit.
2. It has a stable, identity-bearing name.
3. It is not a Trail, Trail Segment, Trail Network, or Site Network.
4. It is not an Access Point.
5. It is not an amenity or feature (e.g., playground, overlook, shelter).
6. It is not a temporary or unnamed management zone.
7. It is not a parcel unless documented as a Site.

A candidate may be a **child Site** if:

- It is an internal identity-bearing unit within a larger Site, AND
- It meets the criteria in the **Child Site Rules Module v5.0**.

If any required condition fails, the candidate must not be created.

------------------------------------------------------------
# 6. DISCOVERY WORKFLOW

## 6.1 Step 1 — Identify Named Identity-Bearing Land Units

Search all required sources for:

- Parks
- Preserves
- Natural areas
- Wildlife areas
- Forests
- Conservation areas
- Historic sites
- Cemeteries
- Campuses
- Recreation areas
- Cultural or heritage sites
- Multi-parcel conservation lands

Record each appearance as a raw Site candidate.

## 6.2 Step 2 — Verify Identity-Bearing Name

A Site must have:

- A documented, stable name
- Not a temporary project name
- Not a marketing slogan
- Not a generic label unless officially used

If ambiguous, flag for review in notes_raw.

## 6.3 Step 3 — Determine Whether the Candidate Is a Child Site

If the candidate appears to be an internal unit:

- Evaluate using the **Child Site Rules Module v5.0**
- If valid → record Parent Site relationship in parent_site_raw
- If not valid → treat as a feature or ignore

## 6.4 Step 4 — Confirm Site-Level Identity

The candidate must:

- Represent a full identity-bearing land unit
- Not be a Trail or Trail Network
- Not be a Site Network
- Not be an amenity or feature

If unclear, flag for review in notes_raw.

------------------------------------------------------------
# 7. FIELD-BY-FIELD EXTRACTION GUIDE

## 7.1 Core Identity Fields

### `name_raw` (REQUIRED)
**What to collect:**
- Official published name exactly as written
- Don't normalize capitalization
- Don't add or remove words

**Examples:**
- "Carter Historic Farm" ✅
- "carter historic farm" ✅ (record as shown)
- "Carter Farm (Historic)" ✅ (if that's what site says)

**What NOT to do:**
- ❌ Don't standardize: "Carter Farm" when site says "Carter Historic Farm"
- ❌ Don't add category: "Carter Historic Farm Park" when just "Carter Historic Farm"

### `category_raw` (OPTIONAL)
**What to collect:**
- Park, Preserve, Natural Area, Wildlife Area, Forest, Historic Site, Cemetery, Campus, Recreation Area

**Record exactly as site describes it:**
- Site says "nature preserve" → record "nature preserve"
- Site says "park" → record "park"
- Don't choose or normalize

### `subtype_raw` (OPTIONAL)
**What to collect:**
- More specific classification if explicitly stated
- Examples: "County Park", "State Nature Preserve", "Township Cemetery"

**Only if explicitly stated:**
- ✅ Site says "community park" → record it
- ❌ You think it's a community park → leave blank

### `designation_raw` (OPTIONAL)
**What to collect:**
- Official legal/administrative designations
- Examples: "National Historic Landmark", "State Nature Preserve", "Local Historic District"

**Only if explicitly documented:**
- Must be formal designation
- Not marketing language

### `status_raw` (OPTIONAL)
**What to collect:**
- Active, Proposed, Under Development, Closed

**Only if explicitly stated:**
- Don't infer from appearance
- Don't guess

## 7.2 Governance Fields

### `ownership_raw` (OPTIONAL)
**What to collect:**
- Legal owner's actual name
- "Wood County", "State of Ohio", "Black Swamp Conservancy", "City of Bowling Green"

**Record exactly as stated:**
- Site says "owned by Wood County" → record "Wood County"
- Site says "county-owned" → record "county-owned" (normalization will clean)

**What NOT to do:**
- ❌ Don't infer from manager
- ❌ Don't use generic categories you create

### `governance_raw` (OPTIONAL)
**What to collect:**
- Who manages/operates the site
- "Wood County Park District", "Ohio Department of Natural Resources", "Bowling Green Parks & Recreation"

**Can be different from owner:**
- Owner: "Wood County"
- Governance: "Wood County Park District"

**Multiple managers:**
- Collect all: "Wood County Park District;Black Swamp Conservancy"
- Don't choose - collect all mentioned

### `coordination_raw` (OPTIONAL)
**What to collect:**
- Partner organizations explicitly mentioned
- "in partnership with...", "managed jointly with..."

**Only if explicitly documented:**
- Don't infer partnerships

## 7.3 Descriptive Fields

### `description_raw` (OPTIONAL)
**What to collect:**
- 1-3 sentence description of the site's identity and character
- Ecological, cultural, historical, or physical characteristics

**Copy directly or summarize minimally:**
- Site's own description is best
- Keep it focused on WHAT the site IS, not amenities

**What NOT to include:**
- ❌ Governance information (goes in governance_raw)
- ❌ Ownership (goes in ownership_raw)
- ❌ Amenities list (goes in features_raw)

### `features_raw` (OPTIONAL)
**What to collect:** ✨ NEW IN v5.0
- Semicolon-delimited list of features/amenities/activities
- Record exactly as site describes them

**Examples:**
- "hiking;fishing;camping;restrooms;playground;picnic shelter"
- "nature trails;bird watching;historic buildings;visitor center"
- "Hiking, Fishing, Boating, Restrooms" → record as found, normalization will clean

**IMPORTANT - Just collect, don't normalize:**
- Site says "bathroom" → record "bathroom" (not "restrooms")
- Site says "trails" → record "trails" (not "hiking")
- Site says "pavilion" → record "pavilion" (not "picnic shelter")
- Normalization will standardize these

**Look for feature lists on:**
- Amenities section
- Activities section
- Facilities section
- Recreation opportunities
- "What's here" or similar sections

### `notes_raw` (OPTIONAL)
**What to collect:**
- Anything noteworthy that doesn't fit other fields
- Seasonal information
- Access restrictions
- Unusual characteristics
- Clarifications or uncertainties

## 7.4 Location Fields

### `location_raw` (OPTIONAL) ✨ REPLACES address_raw IN v5.0
**What to collect (in order of preference):**

**1. Full street address if available:**
- "18331 Carter Road, Bowling Green, OH 43402" ✅
- "350 West Poe Road, Bowling Green, OH" ✅

**2. Nearest cross-street or landmark:**
- "State Route 6 at Metzger Marsh Road"
- "Corner of Main Street and Wooster Street"
- "0.5 miles north of Bowling Green on SR 25"

**3. General geographic description:**
- "East shore of Metzger Marsh, 2 miles north of Crane Creek"
- "Between Perrysburg and Bowling Green on the Maumee River"

**Record exactly as found:**
- Don't standardize formatting
- Don't add or remove information
- Copy directly from site

### `acres_raw` (OPTIONAL)
**What to collect:**
- Number only: "85", "450.5", "1200"
- If site says "85 acres" → record "85"

**What NOT to do:**
- ❌ Don't estimate from maps
- ❌ Don't guess
- ❌ Don't include ranges: "85-90" (pick one or leave blank)

### `counties_raw` (REQUIRED)
**What to collect:**
- All counties mentioned
- Multiple counties: semicolon-delimited

**Examples:**
- "Wood" ✅
- "Wood;Lucas" ✅
- "Wood County" → record "Wood County" (normalization removes "County")

### `county_primary` (REQUIRED)
**What to record:**
- The county YOU are currently discovering in
- This is your discovery tier context, not necessarily where site is located

**Example:**
- You're discovering in Wood County → "Wood"
- Even if site crosses into Lucas County

### `township_raw` (LEAVE BLANK) ⚠️ CRITICAL
**DO NOT attempt to discover township during web research.**

- NOT discoverable from web sources
- Populated via GIS spatial lookup during normalization
- Leave this field blank

**Why you know township but shouldn't record it here:**
- You know which township TIER you're discovering in (Tier 5)
- That's recorded in discovery metadata as tier_context_township
- But the SITE's actual township requires GIS validation
- These might differ!

### `municipality_raw` (LEAVE BLANK) ⚠️ CRITICAL  
**DO NOT attempt to discover municipality during web research.**

- NOT discoverable from web sources
- Populated via GIS spatial lookup during normalization
- Leave this field blank

**Why you know municipality but shouldn't record it here:**
- You know which municipality TIER you're discovering in (Tier 6)
- That's recorded in discovery metadata as tier_context_municipality
- But the SITE's actual municipality requires GIS validation
- These might differ!

### `gps_raw` (OPTIONAL)
**What to collect:**
- GPS coordinates if provided by site
- Format: "lat,lon" (comma-separated)
- Example: "41.3734,-83.6501"

**What NOT to do:**
- ❌ Don't extract from embedded maps (unreliable)
- ❌ Don't look up addresses (that's geocoding, done later)
- ❌ Don't guess

**When to collect:**
- Site explicitly provides coordinates
- GIS layer has coordinate data
- Map page shows coordinates

### `geometry_raw` (OPTIONAL)
**What to collect:**
- If site provides GIS data: polygons, boundaries
- Only if explicitly available for download
- Record as WKT, GeoJSON, or note KML/GPX file URL

**What NOT to do:**
- ❌ Don't trace from visual maps
- ❌ Don't infer boundaries

## 7.5 URL and Map Fields

### `url_primary` (OPTIONAL)
**What to collect:**
- The single most authoritative URL for this site
- Usually the site's dedicated page

**Example:**
- Main page: https://wcparks.org/carter/ ✅

### `url_all` (OPTIONAL)
**What to collect:**
- ALL URLs you find for this site
- Don't deduplicate, don't choose, collect all

**Examples:**
- https://wcparks.org/carter/
- https://wcparks.org/parks/#carter
- https://visitbowlinggreen.com/carter-farm
- https://ohiohistory.org/sites/carter

**Semicolon-delimited:**
- "https://wcparks.org/carter/;https://visitbowlinggreen.com/carter-farm"

### `maps_raw` (OPTIONAL) ✨ NEW IN v5.0
**What to collect:**
- ALL map URLs you find
- PDF maps, interactive maps, GIS viewers, GPX downloads, KML files

**Don't deduplicate, just collect:**
- System overview map: collect it
- Individual site map: collect it
- Interactive GIS viewer: collect it
- PDF download: collect it
- GPX file: collect it

**Examples:**
- https://wcparks.org/maps/system-map.pdf
- https://wcparks.org/maps/carter-detail.pdf
- https://gis.woodcountyohio.gov/parks/viewer

**Semicolon-delimited:**
- "https://wcparks.org/maps/carter.pdf;https://gis.woodcountyohio.gov/parks/viewer"

## 7.6 Parent Site Field

### `parent_site_raw` (OPTIONAL - Child Sites Only)
**What to collect:**
- Name of parent site if this is a child site
- Only if explicitly documented

**Use Child Site Rules Module v5.0:**
- Must be identity-bearing internal unit
- Must be documented
- Must not be a feature

**Example:**
- Site: "Blacksmith District"
- Parent: "Heritage Village Historic Park"

------------------------------------------------------------
# 8. PROVENANCE TRACKING (v5.0)

## 8.1 Source Mapping (REQUIRED) ✨ NEW IN v5.0

**For each discovery record, maintain source_map:**

Track which fields came from which URLs.

**Format:**
```json
{
  "source_map": {
    "https://wcparks.org/parks/": ["name", "ownership", "governance", "url_primary"],
    "https://wcparks.org/carter/": ["acres", "features", "description", "location", "maps"],
    "https://wcparks.org/about/": ["coordination"]
  }
}
```

**Guidelines:**
- Group fields by the URL they came from
- Don't need to track which paragraph or sentence
- URL-level granularity is sufficient
- Useful for debugging normalization issues

## 8.2 Discovery Tier Context

**Record in discovery_metadata:**

```json
{
  "discovery_tier": 5,
  "tier_context_township": "Troy Township",  // Which township you're discovering IN
  "tier_context_municipality": null,
  "county_primary": "Wood"
}
```

**This is different from the site's actual township/municipality:**
- tier_context = where you FOUND it (discovery context)
- township/municipality fields = where it actually IS (GIS-derived later)

## 8.3 Multiple Sources = Multiple Records

**If you encounter the same site at multiple URLs:**

- Emit SEPARATE discovery records
- Each with its own source_map
- Do NOT attempt to merge
- Do NOT detect conflicts
- Resolution engine will handle merging

**Example:**
```
Record 1: From Wood County Parks site
  - name, ownership, governance
  - source_map: {"https://wcparks.org/parks/": [...]}

Record 2: From site's detail page
  - name, acres, features, description
  - source_map: {"https://wcparks.org/carter/": [...]}

Record 3: From historical society
  - name, acres (different value!), historical notes
  - source_map: {"https://historicalsociety.org/farms/": [...]}

Resolution will merge these 3 records and handle the acres conflict.
```

------------------------------------------------------------
# 9. WHAT NOT TO DO (CRITICAL)

## 9.1 Don't Discover These Fields
- ❌ `township_raw` - Leave blank, GIS-derived
- ❌ `municipality_raw` - Leave blank, GIS-derived

## 9.2 Don't Normalize or Standardize
- ❌ Don't change capitalization
- ❌ Don't fix typos in site names
- ❌ Don't standardize terminology ("bathroom" → "restrooms")
- ❌ Don't choose between synonyms
- Record exactly as found

## 9.3 Don't Deduplicate
- ❌ Don't deduplicate URLs
- ❌ Don't deduplicate map links
- ❌ Don't choose "best" URL
- Collect everything, normalization decides

## 9.4 Don't Merge or Detect Conflicts
- ❌ Don't merge records from multiple sources
- ❌ Don't try to detect if values conflict
- ❌ Don't choose between conflicting values
- Emit separate records, Resolution handles merging

## 9.5 Don't Infer or Guess
- ❌ Don't infer ownership from governance
- ❌ Don't guess GPS coordinates
- ❌ Don't infer parent sites
- ❌ Don't trace boundaries from visual maps
- Only record explicitly documented information

## 9.6 Don't Make Category Decisions
- ❌ Don't decide if something is a "Park" vs "Natural Area"
- ❌ Don't categorize features
- Record as site describes itself

------------------------------------------------------------
# 10. TIER-SPECIFIC EXPECTATIONS

## 10.1 Federal Tier (Tier 1)
Must surface:
- National parks
- National wildlife refuges
- National forests
- National historic sites
- Federally managed recreation areas

## 10.2 State Tier (Tier 2)
Must surface:
- State parks
- State forests
- State wildlife areas
- State nature preserves
- State historic sites

## 10.3 District Tier (Tier 3)
Must surface:
- All district-managed parks
- All district-managed preserves
- All district-managed natural areas

## 10.4 County Tier (Tier 4)
May surface:
- County-managed parks
- County-managed natural areas

## 10.5 Township Tier (Tier 5)
Must surface:
- Township parks
- Township preserves
- Township cemeteries

## 10.6 Municipal Tier (Tier 6)
Must surface:
- Municipal parks
- Municipal natural areas
- Municipal historic sites
- Municipal recreation areas

## 10.7 Conservancy Tier (Tier 7)
Must surface:
- Land trust preserves
- Conservation areas
- Natural areas under nonprofit management

## 10.8 Private Tier (Tier 8)
May surface:
- Privately managed natural areas open to public
- Privately managed historic sites open to public
- Campus-scale identity-bearing land units

------------------------------------------------------------
# 11. OUTPUT REQUIREMENTS

Each Site candidate must output:

**Raw Discovery Record conforming to:**
- **Discovery Output Specification v5.0**
- **Site Schema Module v5.0**
- **Discovery Metadata Specification v5.0**

**Must include:**
- All extracted fields (raw, unnormalized)
- Complete source_map
- Discovery tier context (tier_context_township, tier_context_municipality if applicable)
- Source references
- Non-authoritative child Site references
- Non-authoritative Trail and Access Point references
- Geometry (if available)

**Must NOT include:**
- Normalized values
- Merged data from multiple sources
- Inferred or guessed values
- Municipality or township values (leave blank)

------------------------------------------------------------
# 12. QUALITY CHECKLIST

Before emitting a discovery record, verify:

- ✅ name_raw is recorded exactly as found
- ✅ All available fields extracted
- ✅ source_map populated with URL → fields mapping
- ✅ township_raw and municipality_raw left blank
- ✅ No normalization or standardization applied
- ✅ Multiple URLs collected, not deduplicated
- ✅ Multiple maps collected, not deduplicated
- ✅ Features recorded exactly as site describes
- ✅ Location field has address OR general description
- ✅ GPS only included if explicitly provided
- ✅ No inferred or guessed values
- ✅ Discovery tier context documented if Tier 5 or 6

------------------------------------------------------------
# 13. INTEGRATION POINTS

This module integrates with:

- **Discovery Protocol Module v5.0**
- **Tier Sub-Procedure Template v5.0**
- **Site Schema Module v5.0**
- **Site Vocabulary Module v5.0**
- **Child Site Rules Module v5.0**
- **Trail Discovery Sub-Procedure v5.0**
- **Trail Segment Discovery Sub-Procedure v5.0**
- **Access Point Discovery Sub-Procedure v5.0**
- **Site Network Discovery Sub-Procedure v5.0**
- **Discovery Output Specification v5.0**
- **Discovery Metadata Specification v5.0**
- **Resolution Engine v5.0**
- **Normalization Engine v5.0**
- **TSV Output Specifications v5.0**
- **Audit & Logging Module v5.0**

------------------------------------------------------------
# END OF SITE DISCOVERY SUB-PROCEDURE v5.0
