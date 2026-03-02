# NATURAL AREAS PROJECT
# TRAIL SEGMENT DISCOVERY SUB-PROCEDURE v5.1
(Authoritative Sub-Procedure for Discovering Trail Segments)

This module defines the authoritative, deterministic workflow for discovering
**Trail Segments** across all discovery tiers within the v5.x
Raw → Resolution → GPS Acquisition → Normalization → Entity Graph pipeline.

This document supersedes all v5.0 and v4.x Trail Segment discovery logic.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **Field renames**:
  - notes_raw → identity_notes_raw (identity clarifications and flags)
  - url_all → urls_raw (all URLs)
  - url_primary → url_primary_raw
  - maps_raw remains but is now explicitly a plain URL list (was
    described as a rich array in v5.0 — type and description metadata
    no longer collected)
- **identity_notes_raw section added**: explicit extraction guidance
  for the renamed field and its normalized counterpart
- **maps_raw guidance updated**: simplified to URL-only collection;
  no type/description metadata; all map-type URLs collected together
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- Philosophy clarified: Discovery = Collection, Normalization = Decisions
- Source mapping added: Track which fields came from which URLs
- Field changes: Added segment_type, difficulty, accessibility, maps array
- Governance terminology: managing_agency_raw → governance_raw
- Complete rewrite: Enhanced practical guidance for discoverers

------------------------------------------------------------
# 1. PURPOSE

The Trail Segment Discovery Sub-Procedure v5.1 provides the authoritative
workflow for:

- Identifying Trail Segment candidates
- Extracting raw, unnormalized metadata
- Supporting enumerative and recursive discovery
- Preventing misclassification across the six-entity ontology
- Recording tier and URL provenance with field-level source mapping
- Emitting Raw Discovery Records v5.x
- Emitting Discovery Metadata v5.x
- Integrating cleanly with Trail, Trail Network, and Access Point
  discovery
- Feeding the Resolution Engine v5.x

A **Trail Segment** is:

- An identity-bearing operational portion of a Trail
- Documented in authoritative sources
- Distinct from the Trail itself
- Distinct from Access Points
- Distinct from Trail Networks
- Not a Site or child Site
- Has exactly one parent Trail

This module is authoritative for Trail Segment discovery.

------------------------------------------------------------
# 2. DISCOVERY PHILOSOPHY (v5.x)

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

If uncertain whether to include something:
- Include it
- Record uncertainty in identity_notes_raw
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
- Multi-trail system documents
- GPX/KML files with segment structure
- Interactive trail maps showing segment boundaries

All sources must be logged in **Discovery Metadata v5.x** and
**source_map**.

------------------------------------------------------------
# 5. IDENTITY RULES FOR TRAIL SEGMENT CANDIDATES

A Trail Segment candidate is valid only if:

1. It is explicitly documented as a **portion of a Trail**.
2. It has a **stable identity** within the parent Trail.
3. It is **not itself a Trail**.
4. It is **not a Trail Network**.
5. It is **not an Access Point**.
6. It is **not a Site or child Site**.

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
- ✅ Documented surface changes with operational significance
- ✅ "Paved section" vs "Gravel section"

**Different managers:**
- ✅ Trail crosses jurisdictions with different managing agencies

**Different statuses:**
- ✅ Active section vs Gap vs Planned section

**GIS-defined operational segments:**
- ✅ GIS data includes segment IDs or boundaries

**Explicit documentation:**
- ✅ Trail map shows numbered or named segments
- ✅ Trail description references specific segments

## 6.2 DON'T Create Trail Segments When:

**Trail has no documented segments:**
- ❌ Trail is treated as single continuous unit by manager
- ❌ No segment references in any source

**Minor surface changes without distinct identity:**
- ❌ Brief boardwalk section on otherwise natural trail
- ❌ Surface variations without operational significance

**Synthetic divisions:**
- ❌ Dividing trail into segments for analytical convenience
- ❌ Arbitrary divisions not documented by trail manager

**Access point locations:**
- ❌ Don't create a segment for each trailhead location
- ❌ Access points are a separate entity type

## 6.3 Principle

Only create segments that are:
- Explicitly documented with names/numbers, OR
- Have distinct operational characteristics (surface, manager, status)

When in doubt:
- If trail has no documented segments → don't create any
- If you're inventing segmentation → don't
- If source mentions segments → create them

------------------------------------------------------------
# 7. DISCOVERY WORKFLOW

## 7.1 Step 1 — Identify Segment-Level Documentation

Search all required sources for:

- Named segments
- Numbered segments
- GIS-defined segments
- Operational segments
- Segments with distinct surface types
- Segments with distinct management
- Segments with distinct statuses
- Documented segment boundaries

## 7.2 Step 2 — Verify Segment Identity

A Trail Segment must:
- Be part of a specific parent Trail
- Have a documented boundary or identity
- Not be a full Trail, Trail Network, or Access Point

If ambiguous, flag in identity_notes_raw.

## 7.3 Step 3 — Confirm Parent Trail (Single-Parent Rule)

**Each Trail Segment must have exactly one parent Trail.**

Rules:
- Document relationship to that Trail explicitly
- No inferred parentage
- If multiple Trails share the same corridor → create parallel
  segments, one per parent Trail
- Shared-treadway situations do NOT create multi-parent segments
- If the parent Trail has not yet been discovered → create a
  **placeholder Trail Raw Discovery Record** with:
  - entity_type = "Trail"
  - name_raw = parent trail name
  - minimal other values
  - metadata flag `placeholder_parent = true`

------------------------------------------------------------
# 8. FIELD-BY-FIELD EXTRACTION GUIDE

## 8.1 Core Identity Fields

### `segment_name_raw` (OPTIONAL)
Named or numbered segment name exactly as documented.

**Leave blank if unnamed** — this is completely acceptable. Many
segments have no formal name. Normalization will construct a
derived identifier if needed.

**Examples:**
- "Wood County Section" ✅
- "Segment 5" ✅
- "Mile 0-12.5" ✅

**What NOT to do:**
- ❌ Don't invent names
- ❌ Don't add descriptive labels not in source

---

### `parent_trail_raw` (REQUIRED)
Exact name of the parent Trail. Must match how the Trail is named
in Trail Discovery.

**Single parent only:**
- If multiple trails share corridor → create parallel segments

---

### `surface_type_raw` (OPTIONAL)
Record exactly as source describes. Don't normalize vocabulary.

**Examples:**
- "asphalt" → record "asphalt"
- "gravel and dirt" → record "gravel and dirt"

**Important:** Surface type is often the primary reason a segment
exists. Document carefully.

---

### `segment_type_raw` (OPTIONAL)
Only if explicitly documented or clearly distinct from Linear.
Most segments are Linear — leave blank when that's the case.

**Examples of terms to capture:**
- "loop", "connector", "spur", "crossing", "access segment"

---

### `status_raw` (OPTIONAL)
Only if explicitly stated.

**"Gap" is especially important** for long-distance trail
documentation:
- "Gap" = missing or incomplete trail portion requiring road walk
- "Mile 24-32 is currently a gap, road walk required" → record "Gap"

---

### `segment_length_miles_raw` (OPTIONAL)
Length of this segment only — not the full trail. Record the number.

**Never:**
- ❌ Measure from maps
- ❌ Calculate from geometry

---

### `counties_raw` (REQUIRED)
All counties this segment traverses. Semicolon-delimited if multiple.

**Examples:**
- "Wood" ✅
- "Wood;Lucas" ✅ (segment crosses county line)

## 8.2 Difficulty and Accessibility

### `difficulty_raw` (OPTIONAL)
**CRITICAL — Only record if explicitly stated for this specific
segment by an authoritative source.**

- ✅ Source says "Section A is easy, Section B is difficult" →
  record each accordingly
- ❌ Segment looks difficult to you → leave blank
- ❌ Surface is unpaved → leave blank

**Never assess difficulty yourself. Never inherit from parent Trail.**

---

### `accessibility_raw` (OPTIONAL)
Only if explicitly stated for this specific segment.

**Examples:**
- "First mile wheelchair accessible, remainder not accessible"
- "ADA compliant paved section"

**Never:**
- ❌ Infer from surface type
- ❌ Inherit from parent Trail

## 8.3 Governance

### `governance_raw` (OPTIONAL)
Agency responsible for THIS segment. May differ from parent Trail.

**Examples:**
- Long trail crosses jurisdictions:
  - Segment 1: "Wood County Park District"
  - Segment 2: "Lucas County Metroparks"

**Only record if segment-specific governance is documented.**

## 8.4 Identity Notes Field

### `identity_notes_raw` (OPTIONAL)
Free-text field for identity clarifications and uncertainty flags.

**Use for:**
- Segment vs. trail boundary questions:
  "Source describes this as a 'section' of the trail but also
  gives it a standalone page — may be Trail or Trail Segment"
- Shared-corridor documentation:
  "This segment shares treadway with North Country Trail —
  parallel segment created for NCT"
- Parent Trail assignment uncertainty:
  "Source references both Slippery Elm Trail and Wood County
  Trail as parent — cannot determine from source alone"
- Vocabulary type flags:
  "Source calls this a 'pathway' with no further description —
  unclear if named segment or informal reference"

**What NOT to put here:**
- ❌ Operational details → notes_raw
- ❌ Map URLs → maps_raw
- ❌ Difficulty/accessibility → their own fields

## 8.5 Notes Field

### `notes_raw` (OPTIONAL)
Operational details, surface conditions, construction updates,
gap details, temporary closures.

**Must not include:**
- ❌ Identity clarifications → identity_notes_raw
- ❌ Difficulty or accessibility → their own fields

## 8.6 URL and Map Fields

### `url_primary_raw` (OPTIONAL)
Most authoritative URL for this segment. Often the parent Trail
page with a segment section, since dedicated segment pages are
uncommon.

---

### `urls_raw` (OPTIONAL)
ALL URLs where this segment is mentioned. Semicolon-delimited.
Don't deduplicate.

---

### `maps_raw` (OPTIONAL)
ALL map URLs showing this segment — PDF maps, interactive maps,
GIS viewers, GPX downloads, KML files, elevation profiles,
route guides. Semicolon-delimited plain URL list. No type labels
or descriptions.

**Examples:**
```
https://buckeyetrail.org/maps/wood-county-section.pdf;https://buckeyetrail.org/gpx/section-5.gpx;https://gis.county.gov/trails/viewer?segment=5
```

**Don't deduplicate.** Resolution handles deduplication.

## 8.7 Descriptive Fields

### `description_raw` (OPTIONAL)
1-3 sentences describing what makes this segment distinct.

**Focus on this segment specifically:**
- "Paved section along former railroad corridor"
- "Natural surface loop through wetland area"
- "Gap segment requiring road walk on State Route 6"

---

### `geometry_raw` (OPTIONAL)
LineString geometry if available from GIS sources or GPX files.
Record exactly as found. Leave blank if not available — the GIS
phase handles geometry acquisition.

------------------------------------------------------------
# 9. PROVENANCE TRACKING (v5.x)

## 9.1 Source Mapping (REQUIRED)

For each discovery record, maintain source_map tracking which fields
came from which URLs.

**Format:**
```json
{
  "source_map": {
    "https://buckeyetrail.org/sections/": [
      "segment_name", "parent_trail", "governance"
    ],
    "https://buckeyetrail.org/maps/wood-county.pdf": [
      "length", "surface_type", "counties", "maps_raw"
    ],
    "https://buckeyetrail.org/gpx/section-5.gpx": [
      "geometry", "maps_raw"
    ]
  }
}
```

## 9.2 Multiple Sources = Multiple Records

If you encounter the same segment at multiple URLs:
- Emit SEPARATE discovery records
- Each with its own source_map
- Do NOT attempt to merge
- Resolution engine handles merging

------------------------------------------------------------
# 10. WHAT NOT TO DO (CRITICAL)

- ❌ Don't create segments unnecessarily — only when explicitly
  documented or operationally distinct
- ❌ Don't normalize or standardize field values
- ❌ Don't deduplicate URLs or map links
- ❌ Don't assess or infer difficulty
- ❌ Don't infer accessibility from surface type
- ❌ Don't infer parent Trail from proximity alone
- ❌ Don't create multi-parent segments (single parent only)
- ❌ Don't merge records from multiple sources
- ❌ Don't add type/description metadata to maps_raw entries —
  URLs only
- ❌ Don't create Access Points here — note them in
  identity_notes_raw

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

Document the shared corridor in identity_notes_raw for each record.

---

## 11.2 Unnamed Segments

Unnamed is common and acceptable. Leave segment_name_raw blank.
Document distinguishing characteristics in description_raw.
Normalization constructs a derived identifier if needed.

---

## 11.3 Gap Segments

**Example:** "Buckeye Trail Mile 24-32 is currently a gap,
road walk required"

```
segment_name_raw: "Gap - Mile 24-32" (or blank)
parent_trail_raw: "Buckeye Trail"
status_raw: "Gap"
description_raw: "Road walk required; trail continuation under
  development"
segment_length_miles_raw: "8"
```

Gap segments are important for long-distance trail documentation.

---

## 11.4 County-Scale Discovery for Long Trails

For long trails spanning many counties (e.g., Buckeye Trail with
50+ segments across Ohio):
- Discover segments encountered in your current county
- Don't attempt to discover all segments statewide at once
- Each county tier discovers its segments
- Resolution merges them into the complete trail structure

---

## 11.5 Segment vs. Trail Ambiguity

**Question:** Is this a Trail or a Trail Segment?

**Trail:**
- Identity-bearing standalone named entity
- "Slippery Elm Trail" is a Trail

**Segment:**
- Explicitly described as "section of [Trail]"
- "Wood County Section of Buckeye Trail" is a Segment

**Ambiguous case:**
- Named entity with strong standalone identity that's also part of
  a larger system
- Check how sources describe it
- When in doubt, flag in identity_notes_raw and let Resolution decide

------------------------------------------------------------
# 12. TIER-SPECIFIC EXPECTATIONS

## Federal Tier (Tier 1)
May surface:
- Segment-level geometry for National Scenic Trails
- Segment IDs for federal trail inventories

## State Tier (Tier 2)
Must surface:
- Segment-level breakdowns for state-managed trails
- Statewide trail inventory segments

## District Tier (Tier 3)
Must surface:
- All named or numbered segments
- GIS-defined segments

## County Tier (Tier 4)
May surface:
- County-managed trail segments
- County-scale sections of longer trails

## Township & Municipal Tiers (Tiers 5–6)
May surface:
- Local trail segments
- Operational sections of local trails

## Conservancy Tier (Tier 7)
May surface:
- Named trail sections within preserves

## Private Tier (Tier 8)
May surface:
- Privately managed segment-level trails

------------------------------------------------------------
# 13. OUTPUT REQUIREMENTS

Each Trail Segment candidate must output:

**Raw Discovery Record conforming to:**
- **Discovery Output Specification v5.x**
- **Trail Segment Schema Module v5.x**
- **Discovery Metadata Specification v5.x**

**Must include:**
- All extracted fields (raw, unnormalized)
- Complete source_map
- Parent Trail reference (required)
- maps_raw as plain URL list
- identity_notes_raw with any boundary questions, shared-corridor
  notes, parent Trail uncertainty
- Geometry (if available)

**Must NOT include:**
- Normalized values
- Merged data from multiple sources
- Multi-parent references
- Inferred or guessed values
- Synthetic segmentation
- Type/description metadata in maps_raw

------------------------------------------------------------
# 14. QUALITY CHECKLIST

Before emitting a discovery record, verify:

- ✅ parent_trail_raw identified (required)
- ✅ Single parent only
- ✅ segment_name_raw blank if unnamed (acceptable)
- ✅ Segment actually documented or operationally distinct
- ✅ segment_type only if explicitly documented or clearly non-Linear
- ✅ difficulty/accessibility only if explicitly stated for this
  specific segment
- ✅ surface_type recorded if documented
- ✅ status recorded if documented ("Gap" for missing trail portions)
- ✅ identity_notes_raw used for boundary questions, shared-corridor
  notes, parent Trail uncertainty
- ✅ source_map populated with URL → fields mapping
- ✅ No normalization or standardization applied
- ✅ maps_raw entries are plain URLs only — no metadata
- ✅ No synthetic segmentation
- ✅ No inferred values

------------------------------------------------------------
# 15. INTEGRATION POINTS

This module integrates with:

- **Discovery Protocol Module v5.x**
- **Trail Segment Schema Module v5.x**
- **Trail Segment Vocabulary Module v5.x**
- **Trail Discovery Sub-Procedure v5.x**
- **Trail Network Discovery Sub-Procedure v5.x**
- **Access Point Discovery Sub-Procedure v5.x**
- **Discovery Output Specification v5.x**
- **Discovery Metadata Specification v5.x**
- **Resolution Engine v5.x**
- **Normalization Engine v5.x**
- **Trail Segment TSV Output Specification v5.x**
- **Audit & Logging Module v5.x**

------------------------------------------------------------
# END OF TRAIL SEGMENT DISCOVERY SUB-PROCEDURE v5.1
