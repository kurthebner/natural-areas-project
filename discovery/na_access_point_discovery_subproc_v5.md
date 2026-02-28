# NATURAL AREAS PROJECT
# ACCESS POINT DISCOVERY SUB-PROCEDURE v5.0
(Authoritative Sub-Procedure for Discovering Access Points)

This module defines the authoritative, deterministic workflow for discovering
**Access Points** across all discovery tiers within the v5.0
Raw → Resolution → Normalization → Entity Graph pipeline.

This document supersedes all v4.x Access Point discovery logic.

------------------------------------------------------------
# CHANGES FROM v4.0

- **Philosophy clarified**: Discovery = Collection, Normalization = Decisions
- **Source mapping added**: Track which fields came from which URLs
- **Field changes**: Removed access_level, removed role; added features_raw
- **GPS split**: gps_raw recorded as "lat,lon" string; converted to numeric gps_lat/gps_lon during normalization
- **Township/municipality**: Clarified as GIS-derived — leave blank during discovery
- **Complete rewrite**: Enhanced practical guidance for discoverers
- All version references updated to v5.0

------------------------------------------------------------
# 1. PURPOSE

The Access Point Discovery Sub-Procedure v5.0 provides the authoritative workflow for:

- Identifying Access Point candidates
- Extracting raw, unnormalized metadata
- Supporting enumerative and recursive discovery
- Preventing misclassification across the six-entity ontology
- Recording tier and URL provenance with field-level source mapping
- Emitting Raw Discovery Records v5.0
- Emitting Discovery Metadata v5.0
- Integrating cleanly with Site, Trail, and Trail Segment discovery
- Feeding the Resolution Engine v5.0

An **Access Point** is:

- A visitor-facing, navigational entry location
- Documented in authoritative sources
- Attached to one or more identity-bearing parent entities
  (**Site, Trail, or Trail Segment**)
- Classified using the Access Point Vocabulary Module v5.0
- Not a feature, amenity, or non-navigational point

This module is authoritative for Access Point discovery.

------------------------------------------------------------
# 2. DISCOVERY PHILOSOPHY (v5.0)

## 2.1 Core Principle: Discovery = Collection, Normalization = Decisions

**Discovery Phase (YOU ARE HERE):**
- Collect everything you find
- Record exactly as found
- Don't normalize, standardize, or choose between values
- Don't deduplicate URLs
- Don't make vocabulary decisions
- Fast, mechanical extraction

**Why?**
- Discovery is expensive (web research time)
- Normalization is cheap (data processing)
- Better to over-collect than under-collect
- Can't go back to the source during normalization

**Normalization Phase (LATER):**
- Standardize vocabulary ("parking area" → "Parking Area")
- Convert gps_raw string → numeric gps_lat / gps_lon
- Populate plus_code from GPS
- GIS-derive municipality and township
- Choose canonical values
- Validate and clean

## 2.2 When in Doubt: Collect It

If you're unsure whether to include something:
- Include it
- Record it in notes_raw if uncertain
- Let Resolution/Normalization decide

## 2.3 Multiple Sources = Multiple Records

If you find the same Access Point at multiple URLs:
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

Each tier must surface Access Point candidates when applicable.

------------------------------------------------------------
# 4. REQUIRED SOURCES

Each tier must check the following for Access Point references:

- Official agency maps
- GIS layers showing trailheads, parking areas, boat ramps, etc.
- Park district trail maps
- State and federal recreation maps
- Brochures and downloadable PDFs
- Digitally documented trailhead kiosks
- Planning documents (master plans, corridor plans)
- Stewardship or restoration plans
- Land trust preserve maps
- Municipal park maps
- County recreation maps
- Digitally documented signage programs
- Interactive trail finders and map viewers

All sources must be logged in **Discovery Metadata v5.0** and **source_map**.

------------------------------------------------------------
# 5. IDENTITY RULES FOR ACCESS POINT CANDIDATES

A valid Access Point candidate must satisfy all of the following:

1. It is explicitly documented as a **visitor-facing entry location**.
2. It has a **documented geographic point** (coordinate, map marker, GIS point).
   - Discovery must **not infer** coordinates.
3. It is not a Site, child Site, Trail, or Trail Segment.
4. It is not a feature or amenity (e.g., shelter, overlook, playground).
5. It is not a parking lot unless it functions as an entry point to a site or trail.
6. It is not a road intersection unless documented as an entry point.
7. It is not a temporary or unnamed connector.
8. It attaches to **one or more identity-bearing parent entities**
   (Site, Trail, or Trail Segment).
9. It must never attach to Site Networks or Trail Networks.

If any condition fails, the candidate must not be created.

------------------------------------------------------------
# 6. DISCOVERY WORKFLOW

## 6.1 Step 1 — Identify Access Point Candidates

Search all required sources for:

- Trailheads
- Parking areas that serve as entry points
- Boat ramps
- Watercraft access points
- Fishing access points
- Equestrian access points
- Bicycle access points
- Pedestrian access points
- Scenic overlook pull-offs (if documented as entry)
- Gateways or named entrances
- Named or mapped access nodes

Record each appearance as a raw Access Point candidate.

## 6.2 Step 2 — Verify Access Point Identity

An Access Point must:

- Be a visitor-facing entry location
- Have a documented geographic point or reference
- Not be an amenity or feature
- Not be a Site, child Site, Trail, or Trail Segment

If ambiguous, flag for review in notes_raw.

## 6.3 Step 3 — Assign Access Point Type

Assign a type from the **Access Point Vocabulary Module v5.0**.

Record exactly as stated in the source. Don't choose a vocabulary term
during discovery — that's normalization's job.

If no type is clearly documentable, leave blank and flag in notes_raw.

## 6.4 Step 4 — Confirm Parent Entities (Multi-Parent Rule)

Each Access Point may attach to **one or more** of the following:

- Site
- Trail
- Trail Segment

Rules:

- Parentage must reflect what the source explicitly shows.
- Do not infer parentage unless the map or source clearly indicates it.
- If multiple parents are documented, **preserve all of them**.
- If a parent entity has not yet been discovered, create a
  **placeholder Raw Discovery Record** with:
  - correct entity_type
  - name_raw = parent entity name
  - minimal raw values only
  - no invented fields
  - metadata flag `placeholder_parent = true`
- Site Networks and Trail Networks must **not** be treated as parents.
- Access Points may temporarily have no parents until placeholders resolve.

------------------------------------------------------------
# 7. FIELD-BY-FIELD EXTRACTION GUIDE

## 7.1 Core Identity Fields

### `access_point_name_raw` (OPTIONAL)
**What to collect:**
- Official published name exactly as written
- Don't normalize capitalization
- Don't add or remove words

**Examples:**
- "Carter Historic Farm Main Entrance" ✅
- "Slippery Elm Trail - Bowling Green Trailhead" ✅
- "Parking Lot A" ✅ (if that's what the source says)

**If unnamed:**
- Leave blank
- Normalization will construct a derived label from Access Point Type + parent name

**What NOT to do:**
- ❌ Don't invent names beyond what source provides
- ❌ Don't add "Trailhead" or other type descriptors unless in the source

---

### `access_point_type_raw` (OPTIONAL)
**What to collect:**
- Type of entry point as described by the source
- Record exactly as found, don't normalize

**Source terms to capture:**
- "Trailhead", "Parking Area", "Boat Ramp", "Boat Launch",
  "Watercraft Access", "River Access", "Fishing Access",
  "Bicycle Access", "Equestrian Access", "Roadside Pull-Off",
  "Pedestrian Entrance", "Vehicle Entrance", "Administrative Access"

**Record exactly as stated:**
- Source says "boat launch" → record "boat launch"
- Source says "trailhead parking" → record "trailhead parking"
- Don't normalize to vocabulary during discovery

**Leave blank if:**
- Type not clearly documentable from source
- Ambiguous between two types

---

### `status_raw` (OPTIONAL)
**What to collect:**
- Active, Closed, Seasonal, Restricted

**Only if explicitly stated:**
- Source says "seasonal — open April through October" → record "seasonal — open April through October"
- Source says "closed for construction" → record "closed for construction"
- Don't infer from imagery

## 7.2 Parent Relationship Fields

### `parent_sites_raw` (OPTIONAL)
**What to collect:**
- Name(s) of parent Site(s) as documented
- Semicolon-delimited if multiple

**Examples:**
- "Carter Historic Farm" ✅
- "City Park;Ridge Park" ✅ (access point serves two sites)

**Only if explicitly documented:**
- ❌ Don't guess which site this access point belongs to

---

### `parent_trails_raw` (OPTIONAL)
**What to collect:**
- Name(s) of parent Trail(s) as documented
- Semicolon-delimited if multiple

**Examples:**
- "Slippery Elm Trail" ✅
- "Buckeye Trail;North Country Trail" ✅ (shared trailhead)

---

### `parent_trail_segments_raw` (OPTIONAL)
**What to collect:**
- Name(s) or identifiers of parent Trail Segment(s) as documented
- Less common — only when source explicitly references a specific segment

---

### **Identity Parent (Normalization determines this)**
The identity parent (single primary parent for grouping) is determined
during normalization, not during discovery.

During discovery, simply collect ALL documented parent relationships
in the appropriate parent_*_raw fields above.

## 7.3 Location Fields

### `county_raw` (REQUIRED)
**What to collect:**
- The single county in which the Access Point physically resides
- Access Points are point locations — one county only, never semicolon-delimited

**Examples:**
- "Wood" ✅
- "Wood County" → record "Wood County" (normalization removes "County")

**What NOT to do:**
- ❌ Don't list multiple counties for an Access Point
- ❌ Don't use parent entity's county list

---

### `township_raw` (LEAVE BLANK) ⚠️ CRITICAL
**DO NOT attempt to discover township during web research.**

- NOT discoverable from web sources
- Populated via GIS spatial lookup during normalization
- Leave this field blank

---

### `municipality_raw` (LEAVE BLANK) ⚠️ CRITICAL
**DO NOT attempt to discover municipality during web research.**

- NOT discoverable from web sources
- Populated via GIS spatial lookup during normalization
- Leave this field blank

---

### `address_raw` (OPTIONAL)
**What to collect (in order of preference):**

**1. Full street address if available:**
- "18331 Carter Road, Bowling Green, OH 43402" ✅
- "350 West Poe Road, Bowling Green, OH" ✅

**2. Nearest cross-street or road description:**
- "State Route 6 at Metzger Marsh Road"
- "Corner of Main Street and Wooster Street"

**3. General landmark reference:**
- "0.5 miles north of Bowling Green on SR 25"
- "At the north end of Carter Road"

**What NOT to do:**
- ❌ Don't invent street numbers
- ❌ Don't USPS-normalize addresses
- ❌ Don't standardize formatting

---

### `gps_raw` (OPTIONAL)
**What to collect:**
- GPS coordinates if explicitly provided by the source
- Format: "lat,lon" (comma-separated, no space)
- Example: "41.3734,-83.6501"

**GPS is CRITICAL for Access Points** — they are point locations, and
GPS is required before an Access Point can be included in the statewide database.

**Collect GPS if:**
- Source explicitly provides coordinates
- GIS layer has coordinate data
- Map page shows coordinates
- Trailhead kiosk page lists coordinates

**What NOT to do:**
- ❌ Don't extract from embedded maps (unreliable)
- ❌ Don't geocode addresses yourself (batch geocoding happens post-discovery)
- ❌ Don't guess

**Note on format:**
- During discovery, record as "lat,lon" string
- During normalization, this is split into numeric gps_lat + gps_lon fields
- plus_code is auto-generated from GPS during normalization

## 7.4 Features Field

### `features_raw` (OPTIONAL) ✨ NEW IN v5.0
**What to collect:**
- Semicolon-delimited list of documented facilities and amenities at the access point
- Record exactly as the source describes them

**Look for features on:**
- Amenities sections
- "What's here" sections
- Trailhead kiosk pages
- Parking/facility description pages

**Examples:**
- "restrooms;water fountain;paved parking (50 spaces, 4 ADA);bike racks" ✅
- "pit toilet;gravel parking (20 spaces);picnic table" ✅
- "seasonal restrooms;parking;boat ramp;fishing pier" ✅

**Metadata in parentheses is encouraged:**
- "parking (50 spaces, paved)" ✅
- "restrooms (ADA, seasonal April-Oct)" ✅
- "picnic tables (6)" ✅

**IMPORTANT — Just collect, don't normalize:**
- Source says "bathroom" → record "bathroom" (not "restrooms")
- Source says "parking lot" → record "parking lot" (not "Parking Area")
- Source says "pit toilet" → record "pit toilet"
- Normalization will standardize these

**Must not include:**
- ❌ Features of the parent entity (trails, sites, etc.)
- ❌ Features that belong to the site, not the access point
- ❌ Inferred amenities ("it probably has restrooms")

## 7.5 Notes Field

### `notes_raw` (OPTIONAL)
**What to collect:**
- Short, factual, operational details relevant to reaching or using the Access Point
- Seasonal conditions, gate hours, parking constraints, surface/grade issues,
  fees, signage visibility, access restrictions

**Examples:**
- "Gate locked from dusk to dawn"
- "Gravel lot, limited parking for trailers"
- "Fee station at entrance: $5/vehicle"
- "No signage visible from road — look for gravel pull-off"

**What NOT to include:**
- ❌ Features or ecological descriptions (those go in features_raw)
- ❌ Parent entity information that's already captured elsewhere
- ❌ Narrative descriptions

## 7.6 URL and Map Fields

### `url_primary` (OPTIONAL)
**What to collect:**
- The most authoritative URL referencing this access point
- Often the parent entity's page if no dedicated AP page exists

---

### `url_all` (OPTIONAL)
**What to collect:**
- ALL URLs where this access point is mentioned
- Don't deduplicate, don't choose
- Semicolon-delimited

---

### `map_url_raw` (OPTIONAL)
**What to collect:**
- URL to a map showing this access point
- Can be PDF, interactive viewer, GIS layer, or Google Maps link
- Semicolon-delimited if multiple

**Note:** Access Points use a simple map_url field (not a rich array like Trails).
The primary use is a map showing where the access point is located.

------------------------------------------------------------
# 8. PROVENANCE TRACKING (v5.0)

## 8.1 Source Mapping (REQUIRED) ✨ NEW IN v5.0

**For each discovery record, maintain source_map:**

Track which fields came from which URLs.

**Format:**
```json
{
  "source_map": {
    "https://wcparks.org/parks/carter-historic-farm/": [
      "access_point_name", "access_point_type", "parent_sites", "url_primary"
    ],
    "https://wcparks.org/maps/carter-farm-map.pdf": [
      "gps", "address", "features", "map_url"
    ]
  }
}
```

**Guidelines:**
- Group fields by the URL they came from
- URL-level granularity is sufficient
- Don't need to track which paragraph or sentence

## 8.2 Discovery Tier Context

**Record in discovery_metadata:**

```json
{
  "discovery_tier": 3,
  "tier_context_township": null,
  "tier_context_municipality": "Bowling Green",
  "county_primary": "Wood"
}
```

**This is different from the access point's actual township/municipality:**
- tier_context = where you FOUND it (discovery context)
- township/municipality fields = where it actually IS (GIS-derived later)

## 8.3 Multiple Sources = Multiple Records

**If you encounter the same access point at multiple URLs:**

- Emit SEPARATE discovery records
- Each with its own source_map
- Do NOT attempt to merge
- Do NOT detect conflicts
- Resolution engine will handle merging

**Example:**
```
Record 1: From Carter Farm main page
  - name, type, parent_site, url
  - source_map: {"https://wcparks.org/carter/": [...]}

Record 2: From trails GIS viewer
  - gps, features
  - source_map: {"https://gis.woodcountyohio.gov/": [...]}

Resolution will merge these 2 records.
```

------------------------------------------------------------
# 9. WHAT NOT TO DO (CRITICAL)

## 9.1 Don't Discover These Fields
- ❌ `township_raw` — Leave blank, GIS-derived
- ❌ `municipality_raw` — Leave blank, GIS-derived
- ❌ `plus_code` — Auto-generated from GPS during normalization

## 9.2 Don't Geocode or Compute GPS
- ❌ Don't look up addresses to get coordinates
- ❌ Don't extract coordinates from embedded maps
- ❌ Only record GPS if source explicitly provides it
- ✅ Batch geocoding happens post-discovery

## 9.3 Don't Normalize or Standardize
- ❌ Don't change capitalization
- ❌ Don't standardize terminology ("bathroom" → "restrooms")
- ❌ Don't choose vocabulary terms
- ✅ Record exactly as found

## 9.4 Don't Deduplicate
- ❌ Don't deduplicate URLs
- ❌ Don't choose "best" URL
- ✅ Collect everything, normalization decides

## 9.5 Don't Merge or Detect Conflicts
- ❌ Don't merge records from multiple sources
- ❌ Don't try to detect if values conflict
- ❌ Don't choose between conflicting values
- ✅ Emit separate records, Resolution handles merging

## 9.6 Don't Infer or Guess
- ❌ Don't infer parent entities from proximity alone
- ❌ Don't guess GPS coordinates
- ❌ Don't infer access point type from amenities alone
- ❌ Don't infer features
- ✅ Only record explicitly documented information

## 9.7 Don't Create Access Points for Features
- ❌ Playgrounds, overlooks, shelters are NOT access points
- ❌ Parking lots that serve only a small internal area are NOT access points
- ✅ Parking areas that serve as entry to trails or sites ARE access points

------------------------------------------------------------
# 10. DISCOVERY STRATEGY OPTIONS

Access Points are unique in the six-entity ontology because they are
**inherently dependent** on Sites, Trails, and Trail Segments. Their
discovery naturally follows parent entity discovery.

Three strategies exist; choose based on project phase and goals:

## 10.1 Option A: Concurrent Discovery (Intensive)

Discover access points WHILE discovering parent entities in each tier.

**When to use:**
- When official sources prominently document access points alongside sites/trails
- When GPS coordinates are readily available from the source

**Pro:** Complete, single-pass data collection
**Con:** Significantly slower parent entity discovery

## 10.2 Option B: Dedicated Post-Discovery Phase (Thorough)

After parent entity discovery is complete, run a dedicated access point
research pass using official maps and GIS systems.

**When to use:**
- When comprehensive access point coverage is desired
- When GIS data is available

**Pro:** Systematic, complete
**Con:** Requires second pass; more total time

## 10.3 Option C: Opportunistic (Pragmatic) ⭐ RECOMMENDED

Capture access points that are **prominently documented** during parent
entity discovery. Defer the rest to an optional dedicated phase.

**When to use:**
- Default strategy for county-level discovery
- When primary goal is parent entity completeness

**Triggers for immediate capture:**
- Major trailheads with GPS coordinates on the page
- Prominent parking or boat ramp information
- Access points with detailed facility information (restrooms, ADA, etc.)

**Defer to later:**
- Secondary or informal access points
- Any access point requiring additional research to document

**Pro:** Balances efficiency and completeness
**Con:** May miss some access points

------------------------------------------------------------
# 11. TIER-SPECIFIC EXPECTATIONS

## 11.1 Federal Tier (Tier 1)
Must surface:
- Trailheads for National Scenic Trails
- Access points for National Parks, Forests, and Refuges
- Boat ramps and water access points

## 11.2 State Tier (Tier 2)
Must surface:
- Trailheads for state parks, forests, and wildlife areas
- Boat ramps and fishing access points
- Statewide trail system access points

## 11.3 District Tier (Tier 3)
Must surface:
- All district-managed trailheads
- All district-managed parking-based access points
- All district-managed water access points

## 11.4 County Tier (Tier 4)
May surface:
- County-managed trailheads
- County-managed access points

## 11.5 Township & Municipal Tiers (Tiers 5-6)
May surface:
- Local trailheads
- Local park access points

## 11.6 Conservancy Tier (Tier 7)
Must surface:
- Preserve access points and trailheads
- Trailheads within conservation areas

## 11.7 Private Tier (Tier 8)
May surface:
- Privately managed access points open to the public
- Campus-scale access nodes

------------------------------------------------------------
# 12. OUTPUT REQUIREMENTS

Each Access Point candidate must output:

**Raw Discovery Record conforming to:**
- **Discovery Output Specification v5.0**
- **Access Point Schema Module v5.0**
- **Discovery Metadata Specification v5.0**

**Must include:**
- All extracted fields (raw, unnormalized)
- Complete source_map
- All documented parent relationships (parent_sites_raw, parent_trails_raw, parent_trail_segments_raw)
- GPS if explicitly provided by source
- Features if documented

**Must NOT include:**
- Normalized values
- Merged data from multiple sources
- Inferred GPS coordinates
- Municipality or township values (leave blank)
- Computed plus_code (blank — generated from GPS during normalization)

------------------------------------------------------------
# 13. QUALITY CHECKLIST

Before emitting a discovery record, verify:

- ✅ access_point_type_raw recorded if documentable
- ✅ At least one parent relationship documented (parent_sites_raw, parent_trails_raw, or parent_trail_segments_raw)
- ✅ county_raw populated (single county, not semicolon-delimited)
- ✅ township_raw and municipality_raw left blank
- ✅ gps_raw recorded as "lat,lon" string if explicitly provided; otherwise blank
- ✅ plus_code left blank (auto-generated during normalization)
- ✅ features_raw recorded if amenity/facility information available
- ✅ notes_raw has operational details only (not features, not narrative)
- ✅ source_map populated with URL → fields mapping
- ✅ No normalization or standardization applied
- ✅ No inferred or guessed values
- ✅ No geocoded GPS (only record if source provides it)
- ✅ Access point is visitor-facing entry node (not a feature or amenity)

------------------------------------------------------------
# 14. INTEGRATION POINTS

This module integrates with:

- **Discovery Protocol Module v5.0**
- **Tier Sub-Procedure Template v5.0**
- **Access Point Schema Module v5.0**
- **Access Point Vocabulary Module v5.0**
- **Site Discovery Sub-Procedure v5.0**
- **Trail Discovery Sub-Procedure v5.0**
- **Trail Segment Discovery Sub-Procedure v5.0**
- **Discovery Output Specification v5.0**
- **Discovery Metadata Specification v5.0**
- **Resolution Engine v5.0**
- **Normalization Engine v5.0**
- **TSV Output Specifications v5.0**
- **Audit & Logging Module v5.0**

------------------------------------------------------------
# END OF ACCESS POINT DISCOVERY SUB-PROCEDURE v5.0
