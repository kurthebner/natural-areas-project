# NATURAL AREAS PROJECT
# TRAIL DISCOVERY SUB-PROCEDURE v5.1
(Authoritative Sub-Procedure for Discovering Trails)

This module defines the authoritative, deterministic workflow for discovering
**Trails** across all discovery tiers within the v5.x
Raw → Resolution → GPS Acquisition → Normalization → Entity Graph pipeline.

This document supersedes all v5.0 and v4.x Trail discovery logic.

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
- Field changes: Removed network_affiliation; added difficulty,
  accessibility, maps array
- Governance terminology: managing_agency_raw → governance_raw;
  added partner_agencies_raw
- Complete rewrite: Enhanced practical guidance for discoverers

------------------------------------------------------------
# 1. PURPOSE

The Trail Discovery Sub-Procedure v5.1 provides the authoritative workflow
for:

- Identifying Trail candidates
- Extracting raw, unnormalized metadata
- Supporting enumerative and recursive discovery
- Preventing misclassification across the six-entity ontology
- Recording tier and URL provenance with field-level source mapping
- Emitting Raw Discovery Records v5.x
- Emitting Discovery Metadata v5.x
- Integrating cleanly with Trail Segment, Trail Network, and Access
  Point discovery
- Feeding the Resolution Engine v5.x

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
- Standardize vocabulary ("bike trail" → proper trail_use_type)
- Deduplicate URLs and maps
- Choose canonical values
- Validate and clean

## 2.2 When in Doubt: Collect It

If uncertain whether to include something:
- Include it
- Record uncertainty in identity_notes_raw
- Let Resolution/Normalization decide

## 2.3 Multiple Sources = Multiple Records

If you find the same Trail at multiple URLs:
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

Each tier must surface Trail candidates when applicable.

------------------------------------------------------------
# 4. REQUIRED SOURCES

Each tier must check the following for Trail references:

- Official agency websites
- Authoritative listing/index pages (e.g., /trails/, /bikeways/)
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

All sources must be logged in **Discovery Metadata v5.x** and
**source_map**.

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

If ambiguous, flag in identity_notes_raw.

## 6.3 Step 3 — Confirm Trail-Level Identity

The candidate must:
- Represent a full linear corridor
- Not be a single segment
- Not be a cluster of segments
- Not be a Trail Network

If unclear, flag in identity_notes_raw.

------------------------------------------------------------
# 7. FIELD-BY-FIELD EXTRACTION GUIDE

## 7.1 Core Identity Fields

### `name_raw` (REQUIRED)
Record the official published trail name exactly as written.
- Don't normalize capitalization
- Don't add or remove words

**Examples:**
- "Slippery Elm Trail" ✅
- "slippery elm trail" ✅ (record as shown)
- "Slippery Elm Bike Trail" ✅ (if that's what source says)

---

### `alternate_names_raw` (OPTIONAL)
Documented historical or variant names, abbreviations, or formally used
alternate designations. Semicolon-delimited.

**Examples:**
- "NCT;North Country Trail;North Country NST"

**Only documented names:**
- ❌ Don't invent abbreviations
- ❌ Don't include nicknames unless officially used

---

### `trail_use_type_raw` (OPTIONAL)
Record the use type exactly as the source describes it — don't normalize
to vocabulary terms.

**Examples of source terms to capture:**
- "multi-use", "bike trail", "hiking trail", "equestrian trail",
  "water trail", "mountain bike trail", "nature trail"

---

### `trail_surface_type_raw` (OPTIONAL)
Record exactly as found.

**Examples:**
- "asphalt" → record "asphalt"
- "gravel and dirt" → record "gravel and dirt"

---

### `trail_origin_type_raw` (OPTIONAL)
Only if explicitly stated. Don't guess from context.

**Examples:**
- "former railroad corridor" → record "former railroad corridor"
- "canal towpath" → record "canal towpath"

---

### `status_raw` (OPTIONAL)
Only if explicitly stated. Don't infer from maps or imagery.

## 7.2 Physical Characteristics

### `total_length_miles_raw` (OPTIONAL)
Record the number only. If source says "12.5 miles" → record "12.5".

**Never:**
- ❌ Estimate from maps
- ❌ Calculate from segments

---

### `counties_raw` (REQUIRED)
All counties the trail traverses. Semicolon-delimited if multiple.

**Examples:**
- "Wood" ✅
- "Wood;Lucas;Ottawa" ✅
- "Wood County" → record as "Wood County" (normalization removes
  "County")

## 7.3 Difficulty and Accessibility

### `difficulty_raw` (OPTIONAL)
**CRITICAL — Only record if explicitly stated by an authoritative source.**

- ✅ Source says "Easy" → record "Easy"
- ✅ Source says "Moderate to Difficult" → record "Moderate to Difficult"
- ❌ Trail looks easy to you → leave blank
- ❌ Surface is paved → leave blank (never infer difficulty)

**Never assess difficulty yourself.** Only record what authoritative
sources explicitly state.

---

### `accessibility_raw` (OPTIONAL)
Only if explicitly stated. Record exactly as found.

- "ADA compliant" → record "ADA compliant"
- "Wheelchair accessible for first mile" → record as found
- ❌ Don't infer from surface type

## 7.4 Governance Fields

### `governance_raw` (OPTIONAL)
Primary managing agency or organization, exactly as stated.

**Examples:**
- "Wood County Park District"
- "Ohio Department of Natural Resources"
- "Buckeye Trail Association"

---

### `partner_agencies_raw` (OPTIONAL)
Secondary managing agencies or land managers, semicolon-delimited.
Only if explicitly documented.

**Look for:** "in partnership with...", "co-managed by..."

**Examples:**
- "Cleveland Metroparks;Summit Metro Parks"

## 7.5 Descriptive Fields

### `description_raw` (OPTIONAL)
1-3 sentence description of the trail. Focus on what the trail IS.

---

### `trail_history_raw` (OPTIONAL)
Historical context — railroad history, canal history, designation dates,
former names. Only if explicitly documented; don't research yourself.

**Examples:**
- "Former Penn Central Railroad corridor, converted to trail in 1985"
- "Follows historic Miami & Erie Canal towpath from 1845"

## 7.6 Identity Notes Field

### `identity_notes_raw` (OPTIONAL)
Free-text field for identity clarifications, uncertainty flags, and
disambiguation notes.

**Use for:**
- Trail vs. trail segment boundary questions:
  "Source treats this as a standalone trail, but it appears to be a
  named segment of the Slippery Elm Trail — verify"
- Trail vs. Trail Network ambiguity:
  "Source alternately calls this a 'trail' and a 'trail system' —
  may be Trail or Trail Network; flag for review"
- Alternate name conflicts:
  "Source uses 'Slippery Elm Trail' and 'Slippery Elm Bike Trail'
  interchangeably — cannot determine which is official"
- Vocabulary type flags:
  "Source calls this a 'pathway' — unclear if Hiking or Multi-Use"

**What NOT to put here:**
- ❌ Operational details (seasonal hours, parking) → notes_raw
- ❌ Map URLs → maps_raw
- ❌ Historical context → trail_history_raw

## 7.7 Notes Field

### `notes_raw` (OPTIONAL)
Operational details, temporary conditions, access restrictions,
construction updates, gap locations.

**Must not include:**
- ❌ Identity clarifications → identity_notes_raw
- ❌ Historical context → trail_history_raw
- ❌ Difficulty or accessibility → their own fields

## 7.8 URL and Map Fields

### `url_primary_raw` (OPTIONAL)
The single most authoritative URL for this trail — usually the trail's
dedicated page.

**Example:** https://wcparks.org/trails/slippery-elm-trail/ ✅

---

### `urls_raw` (OPTIONAL)
ALL URLs where this trail is mentioned, semicolon-delimited. Don't
deduplicate, don't choose — collect everything.

**Examples:**
- "https://wcparks.org/trails/slippery-elm-trail/;https://traillink.com/trail/slippery-elm-trail/;https://alltrails.com/trail/slippery-elm-trail"

---

### `maps_raw` (OPTIONAL)
ALL map URLs you find — PDF maps, interactive maps, GIS viewers,
GPX downloads, KML files, elevation profiles, route guides.
Semicolon-delimited plain URL list. No type labels or descriptions.

**Collect everything:**
- Trail map PDF → collect it
- Interactive GIS viewer → collect it
- GPX file download → collect it
- Elevation profile → collect it
- Turn-by-turn route guide → collect it

**Format — URLs only, semicolon-delimited:**
```
https://wcparks.org/maps/slippery-elm-trail.pdf;https://wcparks.org/trails/interactive-map;https://wcparks.org/gpx/slippery-elm.gpx
```

**Don't deduplicate** — Resolution handles deduplication.

------------------------------------------------------------
# 8. PROVENANCE TRACKING (v5.x)

## 8.1 Source Mapping (REQUIRED)

For each discovery record, maintain source_map tracking which fields
came from which URLs.

**Format:**
```json
{
  "source_map": {
    "https://wcparks.org/trails/": [
      "name", "governance", "url_primary_raw"
    ],
    "https://wcparks.org/trails/slippery-elm/": [
      "total_length_miles", "surface_type", "description",
      "trail_history", "difficulty", "accessibility", "maps_raw"
    ],
    "https://traillink.com/trail/slippery-elm/": [
      "alternate_names", "trail_use_type"
    ]
  }
}
```

## 8.2 Multiple Sources = Multiple Records

If you encounter the same trail at multiple URLs:
- Emit SEPARATE discovery records
- Each with its own source_map
- Do NOT attempt to merge
- Resolution engine handles merging

------------------------------------------------------------
# 9. WHAT NOT TO DO (CRITICAL)

- ❌ Don't normalize or standardize field values
- ❌ Don't deduplicate URLs or map links
- ❌ Don't merge records from multiple sources
- ❌ Don't assess or infer difficulty
- ❌ Don't infer accessibility from surface type
- ❌ Don't infer origin type from name or alignment
- ❌ Don't calculate length from maps
- ❌ Don't create Trail Segments here — just note them in
  identity_notes_raw
- ❌ Don't create Access Points here — just note them in
  identity_notes_raw
- ❌ Don't record network membership as a field — just note it in
  identity_notes_raw
- ❌ Don't add type/description metadata to maps_raw entries —
  URLs only

------------------------------------------------------------
# 10. TRAIL SEGMENTS, ACCESS POINTS, AND NETWORK MEMBERSHIP

## 10.1 Trail Segments
If source mentions trail segments:
- Note segment names in identity_notes_raw as raw references
- Do NOT create Trail Segment entities here
- Trail Segment Discovery Sub-Procedure v5.x handles these

## 10.2 Trail Network Membership
If source mentions the trail is part of a network:
- Note network name in identity_notes_raw
- Do NOT create network relationships here
- Resolution/Normalization handles network membership via
  trail_network_members relationship table

## 10.3 Access Points
If source shows trailheads or access points:
- Note access point names in identity_notes_raw as raw references
- Do NOT create Access Point entities here
- Access Point Discovery Sub-Procedure v5.x handles these

------------------------------------------------------------
# 11. TIER-SPECIFIC EXPECTATIONS

## Federal Tier (Tier 1)
Must surface:
- National Scenic Trails
- National Historic Trails
- National Recreation Trails
- Federally documented water trails

## State Tier (Tier 2)
Must surface:
- State-designated trails
- Statewide trail corridors
- State water trails
- State greenway or bikeway systems (individual trails)

## District Tier (Tier 3)
Must surface:
- All named trails within district boundaries
- All named loops
- All named multi-use trails

## County Tier (Tier 4)
May surface:
- Countywide bikeways and greenways
- County-managed trail corridors

## Township & Municipal Tiers (Tiers 5–6)
May surface:
- Local named trails
- Local greenways and bikeways
- Municipal trail systems

## Conservancy Tier (Tier 7)
May surface:
- Named trails within preserves
- Named loops and access corridors

## Private Tier (Tier 8)
May surface:
- Privately managed named trails open to public
- Campus-scale trail systems (individual trails)

------------------------------------------------------------
# 12. OUTPUT REQUIREMENTS

Each Trail candidate must output:

**Raw Discovery Record conforming to:**
- **Discovery Output Specification v5.x**
- **Trail Schema Module v5.x**
- **Discovery Metadata Specification v5.x**

**Must include:**
- All extracted fields (raw, unnormalized)
- Complete source_map
- maps_raw as plain URL list
- identity_notes_raw with any trail/segment boundary questions,
  network membership notes, alternate name conflicts
- Raw segment references (in identity_notes_raw)
- Raw network membership references (in identity_notes_raw)
- Raw Access Point references (in identity_notes_raw)

**Must NOT include:**
- Normalized values
- Merged data from multiple sources
- Inferred or guessed values
- Assessed difficulty or accessibility
- Created Trail Segments or Access Points
- Type/description metadata in maps_raw

------------------------------------------------------------
# 13. QUALITY CHECKLIST

Before emitting a discovery record, verify:

- ✅ name_raw recorded exactly as found
- ✅ All available fields extracted
- ✅ source_map populated with URL → fields mapping
- ✅ No normalization or standardization applied
- ✅ Multiple URLs collected in urls_raw, not deduplicated
- ✅ Multiple map URLs collected in maps_raw as plain URLs, not
  deduplicated, no metadata
- ✅ difficulty_raw only included if explicitly stated by authoritative
  source
- ✅ accessibility_raw only included if explicitly stated
- ✅ No inferred or guessed values
- ✅ Trail segments noted in identity_notes_raw (not created)
- ✅ Network membership noted in identity_notes_raw (not linked)
- ✅ Access points noted in identity_notes_raw (not created)
- ✅ alternate_names_raw recorded if documented
- ✅ trail_history_raw recorded if available

------------------------------------------------------------
# 14. INTEGRATION POINTS

This module integrates with:

- **Discovery Protocol Module v5.x**
- **Trail Schema Module v5.x**
- **Trail Vocabulary Module v5.x**
- **Trail Segment Discovery Sub-Procedure v5.x**
- **Trail Network Discovery Sub-Procedure v5.x**
- **Access Point Discovery Sub-Procedure v5.x**
- **Discovery Output Specification v5.x**
- **Discovery Metadata Specification v5.x**
- **Resolution Engine v5.x**
- **Normalization Engine v5.x**
- **Trail TSV Output Specification v5.x**
- **Audit & Logging Module v5.x**

------------------------------------------------------------
# END OF TRAIL DISCOVERY SUB-PROCEDURE v5.1
