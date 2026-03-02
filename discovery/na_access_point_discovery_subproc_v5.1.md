# NATURAL AREAS PROJECT
# ACCESS POINT DISCOVERY SUB-PROCEDURE v5.1
(Authoritative Sub-Procedure for Discovering Access Points)

This module defines the authoritative, deterministic workflow for discovering
**Access Points** across all discovery tiers within the v5.x
Raw → Resolution → GPS Acquisition → Normalization → Entity Graph pipeline.

This document supersedes all v5.0 and v4.x Access Point discovery logic.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **GPS field split**: gps_raw replaced by gps_lat_raw + gps_lon_raw
  (two separate string fields, recorded exactly as found)
- **Field renames**:
  - notes_raw → identity_notes_raw (identity clarifications and flags)
  - url_all → urls_raw (all URLs including map URLs)
  - url_primary → url_primary_raw
  - map_url_raw removed — map URLs now included in urls_raw
- **identity_notes_raw section added**: explicit extraction guidance for
  the renamed field and its normalized counterpart
- **GPS Acquisition Module reference added**: Access Points without GPS
  after normalization are routed to Stage 3 (GPS Acquisition Module),
  not a separate batch geocoding process
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- Philosophy clarified: Discovery = Collection, Normalization = Decisions
- Source mapping added: Track which fields came from which URLs
- Field changes: Removed access_level, removed role; added features_raw
- GPS split: gps_raw recorded as "lat,lon" string (further split in v5.1)
- Township/municipality: Clarified as GIS-derived — leave blank during
  discovery
- Complete rewrite: Enhanced practical guidance for discoverers

------------------------------------------------------------
# 1. PURPOSE

The Access Point Discovery Sub-Procedure v5.1 provides the authoritative
workflow for:

- Identifying Access Point candidates
- Extracting raw, unnormalized metadata
- Supporting enumerative and recursive discovery
- Preventing misclassification across the six-entity ontology
- Recording tier and URL provenance with field-level source mapping
- Emitting Raw Discovery Records v5.x
- Emitting Discovery Metadata v5.x
- Integrating cleanly with Site, Trail, and Trail Segment discovery
- Feeding the Resolution Engine v5.x

An **Access Point** is:

- A visitor-facing, navigational entry location
- Documented in authoritative sources
- Attached to one or more identity-bearing parent entities
  (Site, Trail, or Trail Segment)
- Classified using the Access Point Vocabulary Module v5.x
- Not a feature, amenity, or non-navigational point

This module is authoritative for Access Point discovery.

------------------------------------------------------------
# 2. DISCOVERY PHILOSOPHY (v5.x)

## 2.1 Core Principle: Discovery = Collection, Normalization = Decisions

**Discovery Phase (YOU ARE HERE):**
- Collect everything you find
- Record exactly as found
- Don't normalize, standardize, or choose between values
- Don't deduplicate URLs
- Don't make vocabulary decisions
- Fast, mechanical extraction

**Normalization Phase (LATER):**
- Standardize vocabulary ("parking area" → "Parking Area")
- Parse gps_lat_raw + gps_lon_raw → numeric gps_lat / gps_lon
- Compute plus_code from GPS
- GIS-derive municipality and township
- Choose canonical values
- Validate and clean

## 2.2 When in Doubt: Collect It

If uncertain whether to include something:
- Include it
- Record uncertainty in identity_notes_raw
- Let Resolution/Normalization decide

## 2.3 Multiple Sources = Multiple Records

If you find the same Access Point at multiple URLs:
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
- Interactive trail finders and map viewers

All sources must be logged in **Discovery Metadata v5.x** and
**source_map**.

------------------------------------------------------------
# 5. IDENTITY RULES FOR ACCESS POINT CANDIDATES

A valid Access Point candidate must satisfy all of the following:

1. It is explicitly documented as a **visitor-facing entry location**.
2. It has a **documented geographic point** (coordinate, map marker,
   GIS point). Discovery must **not infer** coordinates.
3. It is not a Site, child Site, Trail, or Trail Segment.
4. It is not a feature or amenity (e.g., shelter, overlook, playground).
5. It is not a parking lot unless it functions as an entry point to a
   site or trail.
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
- Boat ramps and watercraft launches
- Fishing access points
- Equestrian access points
- Bicycle access points
- Pedestrian entrances
- Scenic overlook pull-offs (if documented as entry)
- Gateways or named entrances
- Named or mapped access nodes

Record each appearance as a raw Access Point candidate.

## 6.2 Step 2 — Verify Access Point Identity

An Access Point must be:
- A visitor-facing entry location
- Not an amenity or feature
- Not a Site, child Site, Trail, or Trail Segment

If ambiguous, flag in identity_notes_raw.

## 6.3 Step 3 — Assign Access Point Type

Record the type exactly as stated in the source.
Don't choose a vocabulary term during discovery — that's normalization's job.
If no type is clearly documentable, leave blank and note in
identity_notes_raw.

## 6.4 Step 4 — Confirm Parent Entities (Multi-Parent Rule)

Each Access Point may attach to one or more of:
- Site
- Trail
- Trail Segment

Rules:
- Parentage must reflect what the source explicitly shows.
- Do not infer parentage unless the map or source clearly indicates it.
- If multiple parents are documented, preserve all of them.
- If a parent entity has not yet been discovered, create a
  **placeholder Raw Discovery Record** with:
  - correct entity_type
  - name_raw = parent entity name
  - minimal raw values only
  - no invented fields
  - metadata flag `placeholder_parent = true`
- Site Networks and Trail Networks must not be treated as parents.

------------------------------------------------------------
# 7. FIELD-BY-FIELD EXTRACTION GUIDE

## 7.1 Core Identity Fields

### `access_point_name_raw` (OPTIONAL)
Record the official published name exactly as written.
- Don't normalize capitalization
- Don't add or remove words

**If unnamed:** Leave blank. Normalization may construct a name from
Type + parent name.

**Examples:**
- "Carter Historic Farm Main Entrance" ✅
- "Slippery Elm Trail - Bowling Green Trailhead" ✅
- "Parking Lot A" ✅

---

### `access_point_type_raw` (OPTIONAL)
Record exactly as the source describes the entry point.
- Don't normalize to vocabulary terms during discovery

**Examples of source terms to capture:**
- "trailhead", "parking area", "boat ramp", "boat launch",
  "watercraft access", "river access", "fishing access",
  "equestrian access", "roadside pull-off", "pedestrian entrance",
  "vehicle entrance", "administrative access"

Leave blank if not clearly documentable.

---

### `status_raw` (OPTIONAL)
Only if explicitly stated. Examples:
- "seasonal — open April through October"
- "closed for construction"

Don't infer from imagery or lack of recent updates.

## 7.2 Parent Relationship Fields

### `parent_sites_raw` (OPTIONAL)
Name(s) of parent Site(s) as documented. Semicolon-delimited if
multiple. Only if explicitly documented — do not guess.

**Example:** "Carter Historic Farm"

---

### `parent_trails_raw` (OPTIONAL)
Name(s) of parent Trail(s) as documented. Semicolon-delimited if
multiple.

**Example:** "Slippery Elm Trail"

---

### `parent_trail_segments_raw` (OPTIONAL)
Name(s) or identifiers of parent Trail Segment(s) as documented.
Less common — only when source explicitly references a specific
segment.

---

### **Identity Parent (Normalization determines this)**
The identity parent (single primary parent) is determined during
normalization, not discovery. During discovery, collect ALL documented
parent relationships in the appropriate parent_*_raw fields above.

## 7.3 Location Fields

### `county_raw` (REQUIRED)
The single county in which the Access Point physically resides.
Access Points are point locations — one county only, never
semicolon-delimited.

**Examples:**
- "Wood" ✅
- "Wood County" → record as "Wood County" (normalization removes
  "County")

---

### `township_raw` — LEAVE BLANK ⚠️ CRITICAL
**DO NOT attempt to discover township during web research.**
Populated via GIS spatial lookup during normalization.

---

### `municipality_raw` — LEAVE BLANK ⚠️ CRITICAL
**DO NOT attempt to discover municipality during web research.**
Populated via GIS spatial lookup during normalization.

---

### `address_raw` (OPTIONAL)
In order of preference:

1. Full street address: "18331 Carter Road, Bowling Green, OH 43402"
2. Nearest cross-street: "State Route 6 at Metzger Marsh Road"
3. General landmark reference: "0.5 miles north of Bowling Green on
   SR 25"

Never invent street numbers. Never USPS-normalize.

## 7.4 GPS Fields

### `gps_lat_raw` (OPTIONAL)
Latitude exactly as found in the source — record as a string, as
written. Examples:
- "41.3734" ✅
- "41° 22' 24\" N" ✅ (record exactly; normalization converts)
- "N 41.3734" ✅ (record exactly)

Leave blank if source does not provide it.

### `gps_lon_raw` (OPTIONAL)
Longitude exactly as found in the source — record as a string, as
written. Examples:
- "-83.6501" ✅
- "83° 39' 0\" W" ✅ (record exactly)
- "W 83.6501" ✅ (record exactly)

Leave blank if source does not provide it.

**GPS is CRITICAL for Access Points** — they are point locations and GPS
is required before an Access Point can be included in the statewide
database. Collect GPS whenever explicitly provided.

**What NOT to do:**
- ❌ Don't extract coordinates from embedded maps (unreliable)
- ❌ Don't geocode addresses yourself
- ❌ Don't guess

**Note:** Both fields should be blank or both should have values. Don't
record only one. If source provides combined "lat,lon" format, split
into the two fields at discovery time.

**If GPS is missing after normalization:** The entity is routed to the
GPS Acquisition Module (Stage 3 of the pipeline) for resolution. There
is no separate batch geocoding process.

## 7.5 Features Field

### `features_raw` (OPTIONAL)
Semicolon-delimited list of documented facilities and amenities at the
access point. Record exactly as the source describes them — don't
normalize terminology.

**Look for features in:**
- Amenities sections
- "What's here" sections
- Trailhead kiosk pages
- Parking/facility description pages

**Examples:**
- "restrooms;water fountain;paved parking (50 spaces, 4 ADA);bike
  racks" ✅
- "pit toilet;gravel parking (20 spaces);picnic table" ✅

**Metadata in parentheses is encouraged:**
- "parking (50 spaces, paved)" ✅
- "restrooms (ADA, seasonal April-Oct)" ✅

**Record exactly as found:**
- Source says "bathroom" → record "bathroom"
- Source says "parking lot" → record "parking lot"
- Normalization standardizes these

**Must not include:**
- ❌ Features of the parent entity
- ❌ Inferred amenities

## 7.6 Identity Notes Field

### `identity_notes_raw` (OPTIONAL)
Free-text field for identity clarifications, uncertainty flags, and
disambiguation notes. This is the renamed version of v5.0 `notes_raw`
for identity-specific content.

**Use for:**
- Access point type uncertainty:
  "Source unclear whether this is Trailhead or Parking Area — kiosk
  present but no lot documented"
- Parent entity assignment uncertainty:
  "Source lists both Slippery Elm Trail and North Country Trail as
  parents — cannot determine identity parent from source alone"
- Vocabulary type flags:
  "Source calls this 'boardwalk access' — no vocabulary match, flagged
  for review"
- Disambiguation notes:
  "This is the north entrance; a separate south entrance exists — verify
  both are captured as distinct Access Points"

**What NOT to put here:**
- ❌ Operational details (gate hours, fees, seasonal conditions) →
  those go in notes_raw
- ❌ Features and amenities → those go in features_raw

## 7.7 Notes Field

### `notes_raw` (OPTIONAL)
Short, factual, operational details relevant to reaching or using the
Access Point. This field captures entrance-specific operational content
that is NOT identity clarification.

**Examples:**
- "Gate locked from dusk to dawn"
- "Gravel lot, limited parking for trailers"
- "Fee station at entrance: $5/vehicle"
- "No signage visible from road — look for gravel pull-off"

**Must not include:**
- ❌ Features or amenities (those go in features_raw)
- ❌ Identity clarifications or type uncertainty (those go in
  identity_notes_raw)
- ❌ Parent entity information captured elsewhere
- ❌ Narrative descriptions

## 7.8 URL and Map Fields

### `url_primary_raw` (OPTIONAL)
The most authoritative URL referencing this access point — often the
parent entity's page if no dedicated AP page exists.

---

### `urls_raw` (OPTIONAL)
ALL URLs where this access point is mentioned, semicolon-delimited.
Includes:
- All content pages (trailhead kiosk, amenities, directions)
- Map URLs (PDF maps, interactive viewers, GIS layers showing the AP)

Do not deduplicate. Resolution handles deduplication.

**Note:** There is no separate map_url_raw field. All map URLs go into
urls_raw along with other URLs.

------------------------------------------------------------
# 8. PROVENANCE TRACKING (v5.x)

## 8.1 Source Mapping (REQUIRED)

For each discovery record, maintain source_map tracking which fields
came from which URLs.

**Format:**
```json
{
  "source_map": {
    "https://wcparks.org/parks/carter-historic-farm/": [
      "access_point_name", "access_point_type", "parent_sites",
      "url_primary_raw"
    ],
    "https://wcparks.org/maps/carter-farm-map.pdf": [
      "gps_lat_raw", "gps_lon_raw", "address", "features",
      "urls_raw"
    ]
  }
}
```

## 8.2 Discovery Tier Context

Record in discovery_metadata:

```json
{
  "discovery_tier": 3,
  "tier_context_township": null,
  "tier_context_municipality": "Bowling Green",
  "county_primary": "Wood"
}
```

This is the discovery context (where you found it), not the access
point's actual township/municipality (GIS-derived later).

## 8.3 Multiple Sources = Multiple Records

If you encounter the same access point at multiple URLs:
- Emit SEPARATE discovery records
- Each with its own source_map
- Do NOT attempt to merge
- Resolution engine handles merging

------------------------------------------------------------
# 9. WHAT NOT TO DO (CRITICAL)

- ❌ Don't discover township_raw or municipality_raw — leave blank,
  GIS-derived
- ❌ Don't geocode addresses yourself — GPS Acquisition Module handles
  missing GPS
- ❌ Don't extract coordinates from embedded maps — unreliable
- ❌ Don't normalize or standardize field values
- ❌ Don't deduplicate URLs
- ❌ Don't merge records from multiple sources
- ❌ Don't infer parent entities from proximity alone
- ❌ Don't infer access point type from amenities alone
- ❌ Don't create access points for features (shelters, overlooks,
  playgrounds)
- ❌ Don't use a separate map_url_raw field — map URLs go in urls_raw
- ❌ Don't record gps_lat_raw without gps_lon_raw or vice versa

------------------------------------------------------------
# 10. DISCOVERY STRATEGY OPTIONS

Access Points are inherently dependent on Sites, Trails, and Trail
Segments. Their discovery naturally follows parent entity discovery.
Three strategies exist — choose based on project phase and goals.

## 10.1 Option A: Concurrent Discovery (Intensive)

Discover access points while discovering parent entities in each tier.

**When to use:** When official sources prominently document access
points alongside sites/trails and GPS coordinates are readily available.

**Pro:** Complete, single-pass data collection
**Con:** Significantly slower parent entity discovery

## 10.2 Option B: Dedicated Post-Discovery Phase (Thorough)

After parent entity discovery is complete, run a dedicated access point
research pass using official maps and GIS systems.

**When to use:** When comprehensive access point coverage is desired and
GIS data is available.

**Pro:** Systematic, complete
**Con:** Requires second pass

## 10.3 Option C: Opportunistic (Pragmatic) ⭐ RECOMMENDED

Capture access points that are **prominently documented** during parent
entity discovery. Defer the rest to an optional dedicated phase.

**When to use:** Default strategy for county-level discovery.

**Triggers for immediate capture:**
- Major trailheads with GPS coordinates on the page
- Prominent parking or boat ramp information
- Access points with detailed facility information

**Defer to later:**
- Secondary or informal access points
- Any access point requiring additional research

**Pro:** Balances efficiency and completeness
**Con:** May miss some access points

------------------------------------------------------------
# 11. TIER-SPECIFIC EXPECTATIONS

## Federal Tier (Tier 1)
Must surface:
- Trailheads for National Scenic Trails
- Access points for National Parks, Forests, and Refuges
- Boat ramps and water access points

## State Tier (Tier 2)
Must surface:
- Trailheads for state parks, forests, and wildlife areas
- Boat ramps and fishing access points
- Statewide trail system access points

## District Tier (Tier 3)
Must surface:
- All district-managed trailheads
- All district-managed parking-based access points
- All district-managed water access points

## County Tier (Tier 4)
May surface:
- County-managed trailheads and access points

## Township & Municipal Tiers (Tiers 5–6)
May surface:
- Local trailheads and park access points

## Conservancy Tier (Tier 7)
Must surface:
- Preserve access points and trailheads
- Trailheads within conservation areas

## Private Tier (Tier 8)
May surface:
- Privately managed access points open to the public

------------------------------------------------------------
# 12. OUTPUT REQUIREMENTS

Each Access Point candidate must output:

**Raw Discovery Record conforming to:**
- **Discovery Output Specification v5.x**
- **Access Point Schema Module v5.x**
- **Discovery Metadata Specification v5.x**

**Must include:**
- All extracted fields (raw, unnormalized)
- Complete source_map
- All documented parent relationships
- gps_lat_raw + gps_lon_raw if explicitly provided by source
- features_raw if documented
- identity_notes_raw with any type/parent uncertainty flags
- All URLs including map URLs in urls_raw

**Must NOT include:**
- Normalized values
- Merged data from multiple sources
- Geocoded or inferred GPS coordinates
- township_raw or municipality_raw (leave blank)
- plus_code (blank — generated from GPS during normalization)
- map_url_raw (map URLs go in urls_raw)

------------------------------------------------------------
# 13. QUALITY CHECKLIST

Before emitting a discovery record, verify:

- ✅ access_point_type_raw recorded if documentable
- ✅ At least one parent relationship documented
- ✅ county_raw populated (single county, not semicolon-delimited)
- ✅ township_raw and municipality_raw left blank
- ✅ gps_lat_raw and gps_lon_raw recorded as strings if explicitly
  provided; both blank or both populated — never just one
- ✅ plus_code left blank
- ✅ features_raw recorded if amenity/facility information available
- ✅ identity_notes_raw used for type/parent uncertainty and
  disambiguation
- ✅ notes_raw has operational details only
- ✅ All map URLs included in urls_raw (not in a separate map_url_raw)
- ✅ source_map populated with URL → fields mapping
- ✅ No normalization or standardization applied
- ✅ No inferred or guessed values
- ✅ Access point is visitor-facing entry node (not a feature or amenity)

------------------------------------------------------------
# 14. INTEGRATION POINTS

This module integrates with:

- **Discovery Protocol Module v5.x**
- **Access Point Schema Module v5.x**
- **Access Point Vocabulary Module v5.x**
- **Site Discovery Sub-Procedure v5.x**
- **Trail Discovery Sub-Procedure v5.x**
- **Trail Segment Discovery Sub-Procedure v5.x**
- **Discovery Output Specification v5.x**
- **Discovery Metadata Specification v5.x**
- **Resolution Engine v5.x**
- **GPS Acquisition Module v5.x**
- **Normalization Engine v5.x**
- **Access Point TSV Output Specification v5.x**
- **Audit & Logging Module v5.x**

------------------------------------------------------------
# END OF ACCESS POINT DISCOVERY SUB-PROCEDURE v5.1
