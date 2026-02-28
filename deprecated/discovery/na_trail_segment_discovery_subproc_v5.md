# NATURAL AREAS PROJECT
# TRAIL SEGMENT DISCOVERY SUB-PROCEDURE v5.0
(Authoritative Sub-Procedure for Discovering Trail Segments)

This module defines the authoritative, deterministic workflow for discovering
**Trail Segments** across all discovery tiers within the v5.0
Raw → Resolution → Normalization → Entity Graph pipeline.

This document supersedes all v4.x Trail Segment discovery logic.

------------------------------------------------------------
# CHANGES FROM v4.0

- **Philosophy clarified**: Discovery = Collection, Normalization = Decisions
- **Source mapping added**: Track which fields came from which URLs
- **Field changes**: Added segment_type, difficulty, accessibility, maps array
- **Governance terminology**: managing_agency_raw → governance_raw
- **Complete rewrite**: Enhanced practical guidance for discoverers
- All version references updated to v5.0

------------------------------------------------------------
# 1. PURPOSE

The Trail Segment Discovery Sub-Procedure v5.0 provides the authoritative workflow for:

- Identifying Trail Segment candidates
- Extracting raw, unnormalized metadata
- Supporting enumerative and recursive discovery
- Preventing misclassification across the six-entity ontology
- Recording tier and URL provenance with field-level source mapping
- Emitting Raw Discovery Records v5.0
- Emitting Discovery Metadata v5.0
- Integrating cleanly with Trail, Trail Network, and Access Point discovery
- Feeding the Resolution Engine v5.0

A **Trail Segment** is:

- An identity-bearing operational portion of a Trail
- Documented in authoritative sources
- Distinct from the Trail itself
- Distinct from Access Points
- Distinct from Trail Networks
- Not a Site or child Site
- Not a temporary or unnamed connector
- Has exactly one parent Trail

This module is authoritative for Trail Segment discovery.

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
- Standardize vocabulary
- Deduplicate URLs and maps
- Choose canonical values
- Validate and clean

## 2.2 When in Doubt: Collect It

If you're unsure whether to include something:
- Include it
- Record it in notes_raw if uncertain
- Let Resolution/Normalization decide

## 2.3 Multiple Sources = Multiple Records

If you find the same Trail Segment at multiple URLs:
- Emit SEPARATE discovery records
- Do NOT attempt to merge
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

Each tier must surface Trail Segment candidates when applicable.

------------------------------------------------------------
# 4. REQUIRED SOURCES

Each tier must check the following for Trail Segment references:

- Official agency trail maps
- GIS systems with segment-level geometry
- Trail brochures showing named or numbered segments
- Park district trail pages with segment breakdowns
- Statewide trail inventories with segment IDs
- Federal trail inventories with segment IDs
- Corridor plans showing segment delineation
- Digitally documented trail signage
- Multi-trail system documents (for segment extraction)
- GPX/KML files with segment structure
- Interactive trail maps showing segment boundaries

All sources must be logged in **Discovery Metadata v5.0** and **source_map**.

------------------------------------------------------------
# 5. IDENTITY RULES FOR TRAIL SEGMENT CANDIDATES

A Trail Segment candidate is valid only if:

1. It is explicitly documented as a **portion of a Trail**.
2. It has a **stable identity** within the parent Trail.
3. It is **not itself a Trail**.
4. It is **not a Trail Network**.
5. It is **not an Access Point**.
6. It is **not a temporary or unnamed connector**.
7. It is **not a Site or child Site**.

If any condition fails, the candidate must not be created.

------------------------------------------------------------
# 6. WHEN TO CREATE TRAIL SEGMENTS

## 6.1 DO Create Trail Segments When:

**Named or numbered sections:**
- ✅ "Buckeye Trail - Wood County Section"
- ✅ "Slippery Elm Trail - Segment 5"
- ✅ "North Loop Section"
- ✅ "Mile 0-12", "Mile 12-24"

**Different surface types:**
- ✅ "Paved section" (Segment 1) vs "Gravel section" (Segment 2)
- ✅ Documented surface changes with operational significance

**Different managers:**
- ✅ Trail crosses jurisdictions with different managing agencies
- ✅ "Wood County section" (WCPD) vs "Lucas County section" (Metroparks)

**Different statuses:**
- ✅ Active section vs Gap vs Planned section
- ✅ Open section vs Closed section

**GIS-defined operational segments:**
- ✅ GIS data includes segment IDs or boundaries
- ✅ Management system uses segment-level tracking

**Explicit documentation:**
- ✅ Trail map shows numbered or named segments
- ✅ Trail description references specific segments
- ✅ Signage indicates segment boundaries

## 6.2 DON'T Create Trail Segments When:

**Trail has no documented segments:**
- ❌ Trail is treated as single continuous unit by manager
- ❌ No segment references in any source

**Minor surface changes without distinct identity:**
- ❌ Brief boardwalk section on otherwise natural trail
- ❌ Short paved connector between natural sections
- ❌ Surface variations without operational significance

**Synthetic divisions for convenience:**
- ❌ Dividing trail into segments just for analysis
- ❌ Creating segments every 5 miles for database purposes
- ❌ Arbitrary divisions not documented by trail manager

**Access point locations:**
- ❌ Don't create segment for each trailhead location
- ❌ Access points are separate entity type

## 6.3 Principle

**Only create segments that are:**
- Explicitly documented with names/numbers, OR
- Have distinct operational characteristics (surface, manager, status)

**When in doubt:**
- If trail has no documented segments → Don't create any
- If you're inventing segmentation → Don't create segments
- If source mentions segments → Create them

------------------------------------------------------------
# 7. DISCOVERY WORKFLOW

## 7.1 Step 1 — Identify Segment-Level Documentation

Search all required sources for:

- Named segments
- Numbered segments
- GIS-defined segments
- Operational segments (e.g., "North Section," "Riverside Segment")
- Segments with distinct surface types
- Segments with distinct management
- Segments with distinct statuses
- Documented segment boundaries

Record each appearance as a raw Trail Segment candidate.

## 7.2 Step 2 — Verify Segment Identity

A Trail Segment must:

- Be part of a specific parent Trail
- Have a documented boundary or identity
- Not be a full Trail
- Not be a Trail Network
- Not be an Access Point

If ambiguous, flag for review in notes_raw.

## 7.3 Step 3 — Confirm Parent Trail (Single-Parent Rule)

**Each Trail Segment must have exactly one parent Trail.**

**Rules:**

- Document relationship to that Trail
- No inferred parentage
- If multiple Trails share the same corridor, Discovery must create
  **parallel segments**, one per parent Trail
- Shared-treadway situations do **not** create multi-parent segments
- If the parent Trail has not yet been discovered, create a
  **placeholder Trail Raw Discovery Record** with:
  - correct entity_type = "Trail"
  - name_raw = parent trail name
  - minimal other values
  - no invented fields
  - metadata flag `placeholder_parent = true`

------------------------------------------------------------
# 8. FIELD-BY-FIELD EXTRACTION GUIDE

## 8.1 Core Identity Fields

### `segment_name_raw` (OPTIONAL)
**What to collect:**
- Named segments: "Wood County Section", "North Loop", "Riverside Segment"
- Numbered: "Segment 5", "Section A", "Mile 12-24"
- Operational names: "Paved Section", "Northern Portion"

**Leave blank if unnamed:**
- Many segments have no specific name
- Unnamed is common and acceptable
- Normalization will generate derived label if needed

**Record exactly as found:**
- "Section 5" ✅
- "Wood County Section" ✅
- "Mile 0-12.5" ✅

**What NOT to do:**
- ❌ Don't invent names: "Carter Farm Section" if not documented
- ❌ Don't add descriptions as names

### `parent_trail_raw` (REQUIRED)
**What to collect:**
- Exact name of parent Trail
- Must match how Trail is named in Trail Discovery

**Examples:**
- "Buckeye Trail" ✅
- "Slippery Elm Trail" ✅
- "North Country National Scenic Trail" ✅

**CRITICAL - Single Parent Only:**
- Each segment has exactly ONE parent Trail
- If multiple trails share corridor, create parallel segments (see Special Cases)

## 8.2 Physical Characteristics

### `segment_length_miles_raw` (OPTIONAL)
**What to collect:**
- Length of THIS segment only, not the full trail
- Number only: "12.5", "3.7", "0.8"

**Examples:**
- Source says "Section 5 is 12.5 miles" → record "12.5"
- Source says "Mile 0-12" → record "12" (or leave blank if not explicit)

**What NOT to do:**
- ❌ Don't measure from maps
- ❌ Don't calculate from geometry
- ❌ Only record if explicitly stated

### `surface_type_raw` (OPTIONAL)
**What to collect:**
- Paved, Crushed Stone, Gravel, Natural Surface, Boardwalk, Water, Mixed

**Record exactly as source describes:**
- "asphalt" → record "asphalt"
- "gravel and dirt" → record "gravel and dirt"
- Don't normalize vocabulary

**Important for segments:**
- Segments often exist BECAUSE surface changes
- "Paved section" vs "Natural surface section"

### `segment_type_raw` (OPTIONAL) ✨ NEW IN v5.0
**What to collect:**
- Linear, Loop, Connector, Spur, Crossing, Access Segment

**Only if explicitly documented or clearly distinct from Linear:**
- Most segments are Linear - only populate when different
- Loop: Segment forms a loop back to parent trail
- Connector: Connects two trails
- Spur: Dead-end segment off main trail
- Crossing: Segment crosses another feature (road, river)
- Access Segment: Short segment connecting to access point

**Examples:**
- "Loop trail off main trail" → record "Loop"
- "Spur trail to overlook" → record "Spur"
- Standard segment → leave blank (defaults to Linear)

**What NOT to do:**
- ❌ Don't guess type from geometry
- ❌ Don't invent types
- Leave blank if uncertain

### `status_raw` (OPTIONAL)
**What to collect:**
- Active, Planned, Gap, Closed

**"Gap" is important for segments:**
- "Gap" = missing or incomplete portion of trail
- Common in long-distance trails
- Example: "Mile 24-32 is currently a gap, road walk required"

**Only if explicitly stated:**
- Source says "Section 3 under construction" → record "under construction"
- Source says "Gap between Segment 5 and 6" → record "Gap"

## 8.3 NEW v5.0 Fields

### `difficulty_raw` (OPTIONAL) ✨ NEW IN v5.0
**What to collect:**
- Difficulty rating ONLY if segment has different rating than parent trail
- Easy, Moderate, Difficult, Strenuous, Expert

**CRITICAL - Do NOT assess difficulty yourself:**
- ✅ Source says "Section A is easy, Section B is difficult" → record each
- ✅ Source says "First 5 miles are moderate" → record "moderate"
- ❌ Section looks difficult to you → leave blank
- ❌ You think it should be rated Strenuous → leave blank

**Only record what authoritative sources state:**
- Segment difficulty can differ from overall trail difficulty
- Important when trail crosses varied terrain

### `accessibility_raw` (OPTIONAL) ✨ NEW IN v5.0
**What to collect:**
- Accessibility information ONLY if segment differs from parent trail
- Record what sources explicitly state

**Record exactly as stated:**
- "First mile wheelchair accessible, remainder not accessible"
- "ADA compliant paved section"
- "Accessible for first 2.5 miles"

**What NOT to do:**
- ❌ Don't infer from surface type
- ❌ Don't assess yourself
- Only record explicit statements

**Important for segments:**
- Accessibility often varies by segment
- "Paved segment is accessible, natural segment is not"

## 8.4 Governance

### `governance_raw` (OPTIONAL)
**What to collect:**
- Agency responsible for THIS segment
- May differ from parent Trail's governance

**Examples:**
- Long trail crosses jurisdictions:
  - Segment 1: "Wood County Park District"
  - Segment 2: "Lucas County Metroparks"
- Trail crosses land ownership:
  - Segment A: "State of Ohio"
  - Segment B: "Private landowner (public access easement)"

**Record exactly as stated:**
- Don't infer from parent trail governance
- Only record if segment-specific governance is documented

## 8.5 Location Fields

### `counties_raw` (REQUIRED)
**What to collect:**
- All counties THIS segment traverses
- Multiple counties: semicolon-delimited

**Examples:**
- "Wood" ✅
- "Wood;Lucas" ✅ (segment crosses county line)

**Note:**
- Segments can cross multiple counties
- May differ from parent trail's full county list
- Record only counties THIS segment touches

### `county_primary` (REQUIRED)
**What to record:**
- The county YOU are currently discovering in
- Discovery tier context

## 8.6 URLs and Maps

### `url_primary` (OPTIONAL)
**What to collect:**
- Most authoritative URL for this segment
- Often the parent trail page with segment section

### `url_all` (OPTIONAL)
**What to collect:**
- ALL URLs where this segment is mentioned
- Don't deduplicate

### `maps_raw` (OPTIONAL) ✨ NEW IN v5.0 - RICH ARRAY
**What to collect:**
- ALL map URLs showing this segment
- Segment-specific maps
- GPX files for this segment
- Section maps
- Trail maps highlighting this segment

**Don't deduplicate, just collect:**
- Segment detail map: collect it
- Trail system map showing segment: collect it
- GPX file for segment: collect it
- Elevation profile for segment: collect it

**Examples:**
- https://buckeyetrail.org/maps/wood-county-section.pdf
- https://buckeyetrail.org/gpx/section-5.gpx
- https://gis.county.gov/trails/viewer?segment=5

**Semicolon-delimited:**
- "https://trail.org/section-map.pdf;https://trail.org/gpx/section.gpx"

## 8.7 Descriptive Fields

### `description_raw` (OPTIONAL)
**What to collect:**
- Brief description of segment characteristics
- Surface changes, jurisdictional notes, contextual details
- 1-3 sentences

**Focus on THIS segment:**
- What makes this segment distinct
- Don't duplicate Trail-level description

**Examples:**
- "Paved section along former railroad corridor"
- "Natural surface loop trail through wetland area"
- "Gap segment requiring road walk on State Route 6"

### `notes_raw` (OPTIONAL)
**What to collect:**
- Clarifications, temporary conditions
- Construction updates
- Uncertainties

------------------------------------------------------------
# 9. PROVENANCE TRACKING (v5.0)

## 9.1 Source Mapping (REQUIRED) ✨ NEW IN v5.0

**For each discovery record, maintain source_map:**

Track which fields came from which URLs.

**Format:**
```json
{
  "source_map": {
    "https://buckeyetrail.org/sections/": [
      "segment_name", "parent_trail", "governance"
    ],
    "https://buckeyetrail.org/maps/wood-county.pdf": [
      "length", "surface_type", "counties", "maps"
    ],
    "https://buckeyetrail.org/gpx/section-5.gpx": [
      "geometry", "maps"
    ]
  }
}
```

**Guidelines:**
- Group fields by the URL they came from
- URL-level granularity is sufficient

## 9.2 Multiple Sources = Multiple Records

**If you encounter the same segment at multiple URLs:**

- Emit SEPARATE discovery records
- Each with its own source_map
- Do NOT attempt to merge
- Do NOT detect conflicts
- Resolution engine will handle merging

------------------------------------------------------------
# 10. WHAT NOT TO DO (CRITICAL)

## 10.1 Don't Create Segments Unnecessarily
- ❌ Don't segment every trail
- ❌ Don't create synthetic divisions
- ❌ Don't invent segmentation schemes
- ✅ Only create when explicitly documented OR operationally distinct

## 10.2 Don't Normalize or Standardize
- ❌ Don't change capitalization
- ❌ Don't fix typos
- ❌ Don't standardize terminology
- ✅ Record exactly as found

## 10.3 Don't Assess or Judge
- ❌ Don't rate difficulty yourself
- ❌ Don't judge accessibility yourself
- ❌ Don't evaluate terrain yourself
- ✅ Only record explicit statements

## 10.4 Don't Infer Parentage
- ❌ Don't guess parent Trail from proximity
- ❌ Don't create multi-parent segments (single parent only)
- ❌ Don't infer parent from location
- ✅ Create placeholder Trail if parent not yet discovered

## 10.5 Don't Merge or Detect Conflicts
- ❌ Don't merge records from multiple sources
- ❌ Don't try to detect if values conflict
- ❌ Don't choose between conflicting values
- ✅ Emit separate records, Resolution handles merging

------------------------------------------------------------
# 11. SPECIAL CASES

## 11.1 Shared Corridors (Multi-Trail Treadway)

**Scenario:** Two trails share the same physical path

**Example:**
- Buckeye Trail and North Country Trail share 5 miles of treadway

**Solution:** Create SEPARATE segments for each Trail:

```
Segment 1:
  segment_name_raw: "Shared Treadway Section"
  parent_trail_raw: "Buckeye Trail"
  
Segment 2:
  segment_name_raw: "Shared Treadway Section"
  parent_trail_raw: "North Country Trail"
```

**Why:**
- Each Trail Segment has exactly ONE parent
- Trails maintain their own segment inventories
- Resolution/Normalization handles co-location

**Don't:**
- ❌ Create single segment with multiple parents
- ❌ Try to create complex parent relationships

## 11.2 Unnamed Segments

**Common scenario:** Trail has operational segments but no names

**Example:**
- Trail map shows "Section 1", "Section 2" visually but no labels
- GIS has segments but no segment names
- Manager refers to "northern section" but no formal name

**Solution:**
- Leave segment_name_raw blank
- Document in description: "Northern paved section, miles 0-5"
- Normalization will generate derived label: "Slippery Elm Trail - Segment 1"

**This is completely acceptable:**
- Many segments don't have formal names
- Derived labels work fine

## 11.3 Gap Segments

**Scenario:** Missing or incomplete trail portions

**Example:**
- "Buckeye Trail Mile 24-32 is currently a gap, road walk required"

**How to document:**
```
segment_name_raw: "Gap - Mile 24-32" (if named) or blank
parent_trail_raw: "Buckeye Trail"
status_raw: "Gap"
description_raw: "Road walk required, trail continuation under development"
segment_length_miles_raw: "8"
geometry_raw: may be blank or road alignment
```

**Gap segments are important:**
- Document incomplete portions of trails
- Help users understand trail continuity
- Track planned development

## 11.4 Very Long Trails with Many Segments

**Scenario:** Buckeye Trail has 50+ segments across Ohio

**Discovery approach:**
- Discover segments encountered in your county
- Don't try to discover all 50 segments at once
- Each county tier discovers its segments
- Resolution merges them into complete trail structure

**Example - Wood County discovery:**
- Discover: Wood County Section (Segment 11)
- Don't discover: All other county sections
- Other counties discover their sections

## 11.5 Segments vs. Entire Trail

**Question:** When is something a Trail vs. a Segment?

**Trail:**
- Has identity-bearing name as standalone entity
- "Slippery Elm Trail" is a Trail (not a segment of something else)

**Segment:**
- Explicitly described as "section of [Trail]"
- "Wood County Section of Buckeye Trail" is a Segment

**Ambiguous case - Named section with strong identity:**
- "Towpath Trail" could be standalone Trail OR segment of "Ohio & Erie Canal Towpath"
- Check sources: How do they describe it?
- When in doubt, flag for review in notes_raw

------------------------------------------------------------
# 12. TIER-SPECIFIC EXPECTATIONS

## 12.1 Federal Tier (Tier 1)
May surface:
- Segment-level geometry for National Scenic Trails
- Segment IDs for National Historic Trails
- Federal trail inventory segments

## 12.2 State Tier (Tier 2)
Must surface:
- Segment-level breakdowns for state-managed trails
- Statewide trail inventory segments
- State park trail segments if documented

## 12.3 District Tier (Tier 3)
Must surface:
- All named or numbered segments
- Operational segments (e.g., "North Loop Section")
- GIS-defined segments

## 12.4 County Tier (Tier 4)
May surface:
- County-managed trail segments
- Bikeway segments
- Section-level breakdowns

## 12.5 Township & Municipal Tiers (Tiers 5-6)
May surface:
- Local trail segments
- Local bikeway segments
- Operational sections

## 12.6 Conservancy Tier (Tier 7)
May surface:
- Segment-level breakdowns within preserves
- Named trail sections

## 12.7 Private Tier (Tier 8)
May surface:
- Privately managed segment-level trails
- Campus-scale segment delineations

------------------------------------------------------------
# 13. OUTPUT REQUIREMENTS

Each Trail Segment candidate must output:

**Raw Discovery Record conforming to:**
- **Discovery Output Specification v5.0**
- **Trail Segment Schema Module v5.0**
- **Discovery Metadata Specification v5.0**

**Must include:**
- All extracted fields (raw, unnormalized)
- Complete source_map
- Parent Trail reference (required)
- Geometry (if available)
- Raw Access Point references (in notes)

**Must NOT include:**
- Normalized values
- Merged data from multiple sources
- Multi-parent references
- Inferred or guessed values
- Synthetic segmentation

------------------------------------------------------------
# 14. QUALITY CHECKLIST

Before emitting a discovery record, verify:

- ✅ parent_trail_raw identified (required)
- ✅ Single parent only (no multi-parent segments)
- ✅ segment_name_raw blank if unnamed (acceptable)
- ✅ Segment actually documented or operationally distinct
- ✅ segment_type only if explicitly documented or clearly non-Linear
- ✅ difficulty/accessibility only if explicitly stated by source
- ✅ surface_type recorded if documented
- ✅ status recorded if documented
- ✅ source_map populated with URL → fields mapping
- ✅ No normalization or standardization applied
- ✅ No synthetic segmentation
- ✅ No inferred values
- ✅ Geometry included if available

------------------------------------------------------------
# 15. INTEGRATION POINTS

This module integrates with:

- **Discovery Protocol Module v5.0**
- **Tier Sub-Procedure Template v5.0**
- **Trail Segment Schema Module v5.0**
- **Trail Segment Vocabulary Module v5.0**
- **Trail Discovery Sub-Procedure v5.0**
- **Trail Network Discovery Sub-Procedure v5.0**
- **Access Point Discovery Sub-Procedure v5.0**
- **Discovery Output Specification v5.0**
- **Discovery Metadata Specification v5.0**
- **Resolution Engine v5.0**
- **Normalization Engine v5.0**
- **TSV Output Specifications v5.0**
- **Audit & Logging Module v5.0**

------------------------------------------------------------
# END OF TRAIL SEGMENT DISCOVERY SUB-PROCEDURE v5.0
