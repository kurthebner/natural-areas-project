# NATURAL AREAS PROJECT
# ACCESS POINT DISCOVERY SUB-PROCEDURE v6.0
(Authoritative Sub-Procedure for Discovering Access Point Entities)

This module defines the authoritative, deterministic workflow for discovering
**Access Point** entities across all discovery tiers within the v6.x pipeline.

This document supersedes Access Point Discovery Sub-Procedure v5.2.

------------------------------------------------------------
# CHANGES FROM v5.2 → v6.0

- **Identity Parent Entity Type updated**: Allowed parent types are now
  **Site** and **Trailthing**. "Trail" and "Trail Segment" no longer exist
  as entity types in v6.x — both are now Trailthing entities. The field
  `parent_trails_raw` and `parent_trail_segments_raw` are replaced by
  `parent_trailthings_raw`.

- **Two new verification fields added** (IMP-013):
  - `last_verified_date` — populate with the current date at discovery time
  - `field_verified` — always `false` at discovery; set to `true` only on
    physical visit

- **Notes field scope formalized** (IMP-014): Notes was already correctly
  scoped to operational access detail (gate hours, seasonal conditions,
  fees, restrictions, portage narratives). This is now formally stated
  with a provenance prohibition — pipeline source references and process
  content must not appear in `notes_raw`.

- **`access_notes` not added to Access Points**: The Notes field for
  Access Points was already correctly scoped to operational access detail.
  No separate access_notes field is needed. The Notes guidance formalizes
  and tightens this existing scope.

- **AP-to-Site reclassification candidate flagging** (IMP-114): Any Access
  Point with `acres_raw` populated, `description_raw` present, and governance
  distinct from the parent Trailthing should be flagged for reclassification
  review. See §5.5.

- **Water trail AP sourcing carried forward** (IMP-045, IMP-047): The
  MORPC Central Ohio Blueways dual-layer methodology is carried forward
  unchanged. References updated: "Trail" → "Trailthing" throughout.

- **Field-by-field rules expanded**: Consistent with v6.0 schema style.

------------------------------------------------------------
# 1. PURPOSE

This sub-procedure provides the authoritative workflow for:

- Identifying Access Point candidates
- Extracting raw, unnormalized metadata
- Recording tier and URL provenance
- Preventing misclassification across the four v6.x entity types
- Emitting Raw Discovery Records conforming to the Access Point Schema
  Module v6.0
- Integrating with Site, Trailthing, and Site Network discovery
- Feeding the Resolution Engine v6.x

An **Access Point** is:

- A visitor-facing, navigational entry location
- Documented in authoritative sources
- Attached to one or more identity-bearing parent entities (Site or Trailthing)
- Classifiable using the Access Point Vocabulary Module v6.x
- Not a feature, amenity, or non-navigational point

Examples:
- A named trailhead with a parking lot and kiosk
- A boat ramp providing river access for paddlers
- A hazard portage point at a dam on a water trail
- A pedestrian park entrance gate
- A roadside pull-off serving as the only access to a nature preserve
- A horse trailer parking area with bridle trail access

Access Points are processed **last** within each tier:

**Sites → Trailthings → Site Networks → Access Points**

This sub-procedure is authoritative for **Access Point discovery**.

------------------------------------------------------------
# 2. DISCOVERY PHILOSOPHY

## 2.1 Core Principle: Discovery = Collection, Normalization = Decisions

**Discovery Phase (YOU ARE HERE):**
- Collect everything you find
- Record exactly as found
- Do not normalize, standardize, or choose between values
- Do not deduplicate URLs
- Do not make vocabulary decisions
- Fast, mechanical extraction

**Normalization Phase (LATER):**
- Standardize vocabulary ("parking area" → "Parking Area")
- Parse gps_lat_raw + gps_lon_raw → numeric gps_lat / gps_lon
- Compute plus_code from GPS
- GIS-derive municipality and township
- Choose canonical values

## 2.2 When in Doubt: Collect It

If uncertain whether to include an Access Point candidate:
- Include it
- Record uncertainty in `identity_notes_raw`
- Let Resolution/Normalization decide

## 2.3 Multiple Sources = Multiple Records

If you find the same Access Point at multiple URLs:
- Emit SEPARATE discovery records
- Do NOT attempt to merge
- Resolution Engine handles merging

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
- Digitally documented trailhead kiosk pages
- Planning documents (master plans, corridor plans)
- Stewardship or management plans
- Land trust preserve maps
- Municipal park maps
- County recreation maps
- Interactive trail finders and map viewers
- Water trail guides and paddling brochures (see §14)

All sources must be logged in source_map.

------------------------------------------------------------
# 5. IDENTITY RULES FOR ACCESS POINT CANDIDATES

## 5.1 The Standard

A valid Access Point candidate must satisfy all of the following:

1. It is a **real, physical entry location** that can be mapped to a GPS
   coordinate.
2. It is documented in at least one authoritative or defensible source.
3. It is **visitor-facing**: a visitor would reasonably use it to begin
   access to a parent entity.
4. It has at least one parent entity — a Site or Trailthing.
5. It does not duplicate another Access Point at the same location with
   the same parent set and type.

If any condition fails, the candidate must not be created.

## 5.2 The Site-as-Destination Rule

Sites that are themselves the navigational destination do not require Access
Points unless they have distinct, visitor-facing entry locations separate from
the site itself. A cemetery, small preserve, or roadside natural area that a
visitor simply parks near and walks into does not need a separate Access Point
record — the Site record's GPS coordinate is sufficient.

Access Points are warranted when:
- There are multiple distinct entry locations to a site
- A named trailhead with documented facilities exists
- The entry involves specific navigation (boat ramp, parking area, trail
  access)
- The site has access conditions that warrant a separate entry record

## 5.3 Access Point vs. Site Feature

An Access Point is a discrete navigational entry location — often with its
own GPS coordinate and name. A Site Feature describes an internal component
of a site. When in doubt:
- Is a visitor using this as an **entry point**? → Access Point
- Is it an **amenity within** the site? → Feature on the Site record

## 5.4 Parent Entity Rules

Each Access Point may have one or more parent entities:
- **Allowed parent types: Site, Trailthing**
- "Trail" and "Trail Segment" no longer exist as entity types in v6.x.
  Trail-related parent entities are Trailthings.
- Site Networks must not be treated as parents for Access Points.
- Parentage must reflect what the source explicitly documents — do not
  infer from proximity alone.

The **identity parent** (single primary parent) is determined during
normalization. During discovery, collect all documented parent relationships.

## 5.5 AP-to-Site Reclassification Candidates (IMP-114)

Any Access Point record with:
- `acres_raw` populated
- `description_raw` present
- Governance distinct from the parent Trailthing

…is a candidate for reclassification as a Site entity. Flag these in
`identity_notes_raw`:
```
RECLASSIFICATION_CANDIDATE — AP has acreage, description, and distinct
governance; evaluate for Site entity at Stage 5.5 Human Review.
```

See Access Point Normalization Contract v6.x for full reclassification
criteria.

------------------------------------------------------------
# 6. DISCOVERY WORKFLOW

## 6.1 Step 1 — Identify Access Point Candidates

Search all required sources for:

- Named trailheads
- Parking areas that serve as entry points
- Boat ramps and watercraft launch sites
- Fishing access points
- Equestrian access points and horse trailer parking areas
- Bicycle access points
- Pedestrian entrances and gateways
- Scenic overlook pull-offs (if documented as a visitor entry point)
- Named or mapped access nodes on water trails
- Hazard portage points at dams or obstructions

## 6.2 Step 2 — Verify Access Point Identity

An Access Point must be:
- A visitor-facing entry location, not an amenity or feature
- Not a Site, Trailthing, or Site Network

If ambiguous, flag in `identity_notes_raw`.

## 6.3 Step 3 — Capture Type and Parent

Record `ap_type_raw` exactly as the source states. Do not choose a vocabulary
term during discovery.

Identify the parent entity or entities — which Site(s) or Trailthing(s) this
AP provides access to. Record them in `parent_sites_raw` and/or
`parent_trailthings_raw`.

## 6.4 Step 4 — Set Verification Fields

- `last_verified_date`: populate with today's date (the date of this discovery
  session). This is the date the record was last confirmed accurate based on
  the source information reviewed.
- `field_verified`: always `false` at discovery. Set to `true` only on physical
  visit to the access point.

------------------------------------------------------------
# 7. FIELD-BY-FIELD EXTRACTION GUIDE

## 7.1 Core Identity Fields

### `ap_name_raw` (OPTIONAL)
Official published name exactly as written. Do not normalize.

If unnamed, leave blank. Normalization may construct a name from
Type + parent name per the AP name construction rule.

**Examples:**
- "Griggs Reservoir Trailhead" ✅
- "Carter Historic Farm Main Entrance" ✅
- "Slippery Elm Trail — Bowling Green Trailhead" ✅
- "South Parking Area" ✅

---

### `ap_type_raw` (OPTIONAL)
Record exactly as the source describes the entry point. Do not normalize to
vocabulary terms during discovery.

**Examples of source terms to capture:**
- "trailhead", "parking area", "boat ramp", "boat launch", "watercraft
  launch", "river access", "fishing access", "equestrian access",
  "horse trailer parking", "roadside pull-off", "pedestrian entrance",
  "main entrance", "park gateway", "portage", "carry-around"

Leave blank if not clearly documentable. Note type uncertainty in
`identity_notes_raw`.

---

### `status_raw` (OPTIONAL)
Only if explicitly stated.

**Examples:**
- "seasonal — open April through October"
- "closed for construction"
- "restricted — permit required"

Do not infer from imagery or lack of recent updates.

## 7.2 Parent Relationship Fields

### `parent_sites_raw` (OPTIONAL)
Name(s) of parent Site(s), semicolon-delimited if multiple. Only if
explicitly documented — do not guess.

**Example:** "Carter Historic Farm"

---

### `parent_trailthings_raw` (OPTIONAL)
Name(s) of parent Trailthing(s), semicolon-delimited if multiple. Replaces
the v5 fields `parent_trails_raw` and `parent_trail_segments_raw` — both
trail and trail segment parents are now Trailthings.

**Examples:**
- "Slippery Elm Trail"
- "Buckeye Trail"
- "Buckeye Trail — Wood County Section"

Only if explicitly documented in source. Do not infer from proximity.

---

**Note:** If a parent entity has not yet been discovered at the time an
Access Point is staged, create a **placeholder Raw Discovery Record** for
the parent:
- Correct `entity_type` (Site or Trailthing)
- `name_raw` = parent entity name as documented
- Minimal raw values only; no invented fields
- Metadata flag `placeholder_parent: true`

## 7.3 Location Fields

### `county` (REQUIRED)
The single county in which the Access Point physically resides. Access Points
are point locations — one county only, never semicolon-delimited.

Must not include the word "County."

**Examples:**
- "Wood" ✅
- "Ottawa" ✅

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
An authoritative or defensible address or road description for navigation.

**In order of preference:**
1. Full street address if documented: "18331 Carter Road, Bowling Green, OH"
2. Nearest cross-street: "State Route 6 at Metzger Marsh Road"
3. General landmark reference: "0.5 miles north of Bowling Green on SR 25"
4. Authorized fallback: "County Road 47", "Township Road 103", "Forest Road 2"

Never invent street numbers. Never USPS-normalize. Blank if no authoritative
or defensible designation exists.

## 7.4 GPS Fields

### `gps_lat_raw` (OPTIONAL)
Latitude exactly as found in the source — record as a string.

**Examples:**
- "41.3734" ✅
- "41° 22' 24\" N" ✅ (record exactly; normalization converts)
- "N 41.3734" ✅

Leave blank if source does not provide it. Never estimate, infer, or geocode.

---

### `gps_lon_raw` (OPTIONAL)
Longitude exactly as found in the source — record as a string.

**Examples:**
- "-83.6501" ✅
- "83° 39' 0\" W" ✅ (record exactly)
- "W 83.6501" ✅

Leave blank if source does not provide it.

**GPS is critical for Access Points** — they are point locations and GPS is
required before an Access Point can be included in the statewide database.
Collect GPS whenever explicitly provided in authoritative sources.

**Rules:**
- Both `gps_lat_raw` and `gps_lon_raw` must be blank, or both must have
  values. Never record only one.
- If source provides combined "lat,lon" format, split into two fields at
  discovery time.
- Do not extract coordinates from embedded maps — unreliable.
- Do not geocode addresses yourself — GPS Acquisition Module handles this.
- Do not estimate or guess coordinates.

**If GPS is missing after normalization:** The entity is routed to the
GPS Acquisition Module for resolution.

## 7.5 Features Field

### `features_raw` (OPTIONAL)
Semicolon-delimited list of documented facilities and amenities at this
specific access point. Record exactly as source describes.

**What to look for:**
- Amenities sections on park/trail pages
- "What's here" and "facilities" sections
- Trailhead kiosk documentation
- Parking and facility description pages

**Examples:**
- "restrooms;paved parking (50 spaces, 4 ADA);bike racks" ✅
- "vault toilet;gravel parking (20 spaces);picnic table" ✅

Metadata in parentheses is encouraged:
- "Parking Area (50 spaces, paved)" ✅
- "Restrooms (ADA, seasonal April–Oct)" ✅

Record exactly as found — normalization standardizes vocabulary terms.

**Must not include:**
- ❌ Features of the parent entity — only features physically at this AP
- ❌ Inferred amenities

## 7.6 Identity Notes Field

### `identity_notes_raw` (OPTIONAL)
Free-text field for identity clarifications, uncertainty flags, and
disambiguation notes.

**Use for:**
- Access point type uncertainty:
  "Source unclear whether this is Trailhead or Parking Area — kiosk present
  but no dedicated lot documented"
- Parent entity assignment uncertainty:
  "Source lists both Slippery Elm Trail and North Country Trail as parents
  — cannot determine identity parent from source alone"
- Co-location notes (when a recreational AP and Hazard Portage share
  the same physical location):
  "Co-located with Hazard Portage at Griggs Dam — see OH-FRA-AP-XXX"
- Disambiguation notes:
  "This is the north entrance; a separate south entrance exists — verify
  both are captured as distinct Access Points"
- Reclassification candidates (IMP-114):
  "RECLASSIFICATION_CANDIDATE — AP has acreage, description, and distinct
  governance; evaluate for Site entity at Stage 5.5 Human Review."
- Vocabulary type flags:
  "Source calls this 'boardwalk access' — no vocabulary match, flagged
  for review"

**What NOT to put here:**
- ❌ Operational details (gate hours, fees, seasonal conditions) → `notes_raw`
- ❌ Features and amenities → `features_raw`

## 7.7 Notes Field

### `notes_raw` (OPTIONAL)
Short, factual, operational details relevant to reaching or using this
Access Point. This is the correct home for entrance-specific operational
content.

**Correct scope:**
- Gate hours and seasonal access
- Parking constraints (surface, grade, trailer restrictions)
- Fee information
- Signage visibility
- Permit requirements
- Safety warnings

**Hazard Portage records**: Always populate `notes_raw` with:
- Hazard type and name ("Griggs Dam — low-head dam, mandatory portage on
  river left")
- Carry distance and difficulty if documented
- Re-entry point location if documented
- Safety warnings

**Customer-facing field — no provenance artifacts.** Pipeline source
references, IMP numbers, batch load notes, GPS acquisition sources, and
similar process or provenance content must not appear here. Notes must be
readable by someone who knows nothing about the pipeline.

**Must not include:**
- ❌ Features or amenities → `features_raw`
- ❌ Identity clarifications or type uncertainty → `identity_notes_raw`
- ❌ Narrative description of the parent entity

## 7.8 Verification Fields

### `last_verified_date` (RECOMMENDED)
The date this record was last confirmed accurate.

**At discovery time**: Populate with today's date (the date of this
discovery session) — recording that the information was reviewed and
captured as of this date.

Format: YYYY-MM-DD

This field is especially valuable for Access Points, which change
frequently — GPS coordinates, parking availability, seasonal conditions,
and fees are among the most commonly updated entity attributes.

---

### `field_verified` (ALWAYS FALSE AT DISCOVERY)
Boolean, default `false`.

**At discovery**: Always record `false`. Web-based discovery does not
constitute field verification — this field requires physical presence
at the access point.

Set to `true` only when the user has physically visited this access point
and confirmed its existence, location, and general character.

`field_verified` on an Access Point is distinct from `field_verified` on
its parent entity — a Site may be field-verified while individual trailheads
within it have not been.

## 7.9 URL Fields

### `urls_raw` (OPTIONAL)
ALL URLs where this Access Point is mentioned or documented.
Semicolon-delimited. Includes:
- Parent entity pages referencing the access point
- Dedicated access point pages (rare but capture when present)
- Map URLs (PDF maps, interactive viewers, GIS layers showing the AP)

Do not deduplicate. Resolution handles deduplication.

There is no separate `map_url_raw` field — all map URLs go in `urls_raw`.

------------------------------------------------------------
# 8. WHAT NOT TO DO (CRITICAL)

- ❌ Do not populate `township_raw` or `municipality_raw` — GIS-derived; leave blank
- ❌ Do not geocode addresses yourself — GPS Acquisition Module handles missing GPS
- ❌ Do not extract coordinates from embedded maps — unreliable
- ❌ Do not record `gps_lat_raw` without `gps_lon_raw` or vice versa
- ❌ Do not normalize or standardize field values
- ❌ Do not deduplicate URLs
- ❌ Do not merge records from multiple sources
- ❌ Do not infer parent entities from proximity alone
- ❌ Do not infer access point type from amenities alone
- ❌ Do not create Access Points for features (shelters, overlooks, playgrounds)
  that are not visitor-facing entry points
- ❌ Do not create Access Points for Site Networks — Site Networks are not
  valid parent entities
- ❌ Do not use a separate `map_url_raw` field — map URLs go in `urls_raw`
- ❌ Do not put pipeline source references, IMP numbers, or process notes
  in `notes_raw` — it is a customer-facing field
- ❌ Do not set `field_verified: true` based on web or map review alone

------------------------------------------------------------
# 9. DISCOVERY STRATEGY OPTIONS

Access Points are inherently dependent on Sites and Trailthings. Their
discovery naturally follows parent entity discovery. Three strategies
exist — choose based on project phase and goals.

## 9.1 Option A: Concurrent Discovery (Intensive)

Discover Access Points while discovering parent entities in each tier.

**When to use:** When official sources prominently document access points
alongside sites/trails and GPS coordinates are readily available.

**Pro:** Complete, single-pass data collection.
**Con:** Significantly slower parent entity discovery.

## 9.2 Option B: Dedicated Post-Discovery Phase (Thorough)

After all parent entity discovery is complete, run a dedicated Access Point
research pass using official maps and GIS systems.

**When to use:** When comprehensive AP coverage is desired and GIS data
is available.

**Pro:** Systematic and complete.
**Con:** Requires a second pass over sources.

## 9.3 Option C: Opportunistic (Pragmatic) ⭐ RECOMMENDED

Capture Access Points that are **prominently documented** during parent
entity discovery. Defer the rest to an optional dedicated phase.

**When to use:** Default strategy for county-level discovery.

**Triggers for immediate capture:**
- Named trailheads with GPS coordinates on the source page
- Prominent parking or boat ramp information with documented facilities
- Access points with detailed facility or operational information

**Defer to later:**
- Secondary or informal access points
- Any AP requiring additional research beyond what is already open

**Pro:** Balances efficiency and completeness.
**Con:** May miss some Access Points on first pass.

------------------------------------------------------------
# 10. COMPOUND TYPE HANDLING

`ap_type_raw` is recorded as a single raw value. When a source describes an
access point as serving two functions, capture the compound description
verbatim in `ap_type_raw` and note it in `identity_notes_raw`. Normalization
resolves compound types:

- **Trailhead + Parking Area** → normalized `ap_type = "Trailhead"`;
  parking represented in Features.
- **Parking Area + incidental trail access** → normalized `ap_type =
  "Parking Area"`; trailhead in Features only if source designates it.
- **Other compound cases** → normalized to primary function; secondary
  function in Features if applicable.

Do not attempt compound type resolution during discovery — record as found.

------------------------------------------------------------
# 11. HAZARD PORTAGE IDENTITY

Hazard Portage is the one `ap_type` where inference from physical context
is permitted during normalization. A documented dam or low-head weir on an
active water trail with a mandatory carry qualifies as a Hazard Portage
even if the source does not use the word "portage."

At discovery, record what the source says in `ap_type_raw`. If the source
describes a dam, weir, or obstruction on a water trail, note in
`identity_notes_raw`:
```
Potential Hazard Portage — low-head dam documented on active water trail;
mandatory carry implied. Flag for normalization review.
```

When a recreational access point and a Hazard Portage share the same
physical location (e.g., a park boat ramp just above a dam), create two
separate Access Point records and note the co-location in `identity_notes_raw`
on both.

Always populate `notes_raw` on Hazard Portage candidates with whatever
portage narrative the source provides — carry instructions, hazard description,
and re-entry point if documented.

------------------------------------------------------------
# 12. TIER-SPECIFIC EXPECTATIONS

## Federal Tier (Tier 1)
Must surface:
- Trailheads for National Scenic Trails
- Access points for National Parks, Forests, Refuges, and Wildlife Areas
- Boat ramps and water access points at federal properties

## State Tier (Tier 2)
Must surface:
- Trailheads for state parks, forests, and wildlife areas
- Boat ramps and fishing access points at state properties
- Statewide trail system access points

## District Tier (Tier 3)
Must surface:
- All district-managed named trailheads
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
- Access points within conservation areas

## Private Tier (Tier 8)
May surface:
- Privately managed access points open to the public

------------------------------------------------------------
# 13. RAW DISCOVERY RECORD TEMPLATE

```yaml
entity_type: Access Point
ap_name_raw:                          # Optional; verbatim from source; blank if unnamed
ap_type_raw:                          # Optional; verbatim source descriptor
status_raw:                           # Optional; verbatim; only if explicitly stated
parent_sites_raw:                     # Optional; semicolon-delimited Site names
parent_trailthings_raw:               # Optional; semicolon-delimited Trailthing names
county:                               # Required; single county; no "County" suffix
address_raw:                          # Optional; authoritative address or road description
gps_lat_raw:                          # Optional; verbatim as found; never estimated
gps_lon_raw:                          # Optional; verbatim as found; never estimated
features_raw:                         # Optional; semicolon-delimited; with parenthetical metadata
identity_notes_raw:                   # Optional; type/parent uncertainty, co-location, flags
notes_raw:                            # Optional; operational details; no provenance artifacts
urls_raw: []                          # All URLs; semicolon-delimited; includes map URLs
last_verified_date:                   # Populate with today's date (YYYY-MM-DD)
field_verified: false                 # Always false at discovery
discovery_tier:                       # 1–8
seeded_from_baseline:                 # true | false
baseline_id:
```

**Fields that must remain blank at discovery:**
```yaml
township_raw:                         # GIS-derived — DO NOT POPULATE
municipality_raw:                     # GIS-derived — DO NOT POPULATE
plus_code:                            # Computed from GPS — DO NOT POPULATE
access_point_id:                      # Assigned by Upsert Engine — DO NOT POPULATE
```

------------------------------------------------------------
# 14. WATER TRAIL ACCESS POINT DISCOVERY (IMP-045, IMP-047)

Water trail Access Points (launch sites, take-outs, portages, hazard portages)
require a two-layer sourcing methodology because no single source provides
complete coverage of both amenity attributes and named/numbered site identity.

## 14.1 MORPC Central Ohio Blueways ArcGIS Layer (Primary Amenity-Attribute Source)

**Coverage:** 15-county MORPC region (Franklin, Delaware, Fairfield, Pickaway,
Licking, Knox, Morrow, Marion, Union, Madison, Perry, Hocking, Ross, Fayette,
Champaign).

**Access:** ArcGIS FeatureServer REST API.
Query endpoint:
`https://[morpc-server]/FeatureServer/[layer]/query?where=1%3D1&outFields=*&f=json`

**What this layer provides:**
- Point locations for documented water trail APs and hazard portages
- Amenity attributes: parking (boolean), bathroom (boolean), picnic (boolean)
- Facility type flag distinguishing recreational launch from hazard portage
- Waterway name and segment identifiers

**GPS coordinate handling:** MORPC layer coordinates are in Web Mercator
(EPSG:3857). Convert to WGS84 before staging `gps_lat_raw` / `gps_lon_raw`:
```
lon_wgs84 = x_mercator / 20037508.34 * 180
lat_wgs84 = atan(exp(y_mercator / 20037508.34 * pi)) * 360 / pi - 90
```
Stage converted WGS84 values only. Record `acquisition_method = "morpc_gis"`
in provenance.

**How to use:** Query the layer filtered to the county under discovery.
For each point:
- Stage as a candidate Access Point record
- Record amenity flags in `features_raw`: "Parking", "Restrooms", "Picnic
  Area" as applicable
- Record facility type in `ap_type_raw`
- Record MORPC point ID or segment identifier in `identity_notes_raw`

## 14.2 Official Trail Brochure / Guide (Primary Named Site Source)

Official trail brochures, guides, and paddling-specific PDF maps published
by the managing agency are the primary source for:
- Numbered or named access point designations (e.g., "Access Point A1",
  "Big Walnut Creek BW1")
- Portage narrative: description of mandatory carry-around procedure, hazard
  nature
- Directional and seasonal access notes

**How to use:** For each access point documented in the brochure:
- Stage as a candidate Access Point record with brochure-sourced name/number
- Record portage narrative in `notes_raw`
- Record directional or access notes in `identity_notes_raw`

## 14.3 Dual-Layer Reconciliation Protocol (IMP-047)

When both sources document the same physical location:

**Step 1 — Identify co-location:** Match MORPC points to brochure access
points by proximity (within ~50 meters) and waterway. A MORPC point within
50 meters of a named brochure point on the same waterway is presumptively
the same physical location.

**Step 2 — Create one record:**
- Use the brochure name/number as `ap_name_raw`
- Use MORPC amenity attributes for `features_raw`
- Use MORPC GPS coordinates for `gps_lat_raw` / `gps_lon_raw` (more precise
  than brochure)
- Use brochure portage narrative for `notes_raw`
- Record both sources in source_map

**Step 3 — MORPC-only points:** If a MORPC point has no brochure counterpart,
create a record from MORPC data alone. Assign a descriptive name from the
waterway + segment identifier. Note in `identity_notes_raw`:
```
MORPC layer point; no brochure counterpart identified.
```

**Step 4 — Brochure-only points:** If a brochure access point has no MORPC
counterpart, create a record from brochure data alone. GPS may need to be
acquired via GPS Acquisition Module. Note in `identity_notes_raw`:
```
Brochure-only; not in MORPC Blueways layer.
```

## 14.4 Hazard Portage on Water Trails

The MORPC layer flags hazard portages distinctly from recreational launches.
See §11 for general Hazard Portage identity rules and the Hazard Portage
ap_type definition in the Access Point Vocabulary Module v6.x.

When a recreational launch and a hazard portage co-exist at the same physical
location (e.g., a park boat ramp just above a dam):
- Create two separate Access Point records (one per ap_type)
- Both may share the same GPS coordinates and parent Trailthing
- Document the co-location in `identity_notes_raw` on each

------------------------------------------------------------
# 15. QUALITY CHECKLIST

Before emitting a discovery record, verify:

- ✅ `ap_type_raw` recorded if documentable
- ✅ At least one parent relationship documented in `parent_sites_raw`
  or `parent_trailthings_raw`
- ✅ `county` populated (single county; no "County" suffix; not semicolon-
  delimited)
- ✅ `township_raw` and `municipality_raw` left blank
- ✅ `gps_lat_raw` and `gps_lon_raw` both blank or both populated — never
  just one
- ✅ GPS not estimated, inferred, or geocoded
- ✅ `plus_code` left blank
- ✅ `features_raw` recorded if amenity/facility information available
- ✅ Hazard Portage candidates: `notes_raw` populated with portage narrative
  from source; co-located recreational APs flagged in `identity_notes_raw`
- ✅ `identity_notes_raw` used for type/parent uncertainty, co-location
  notes, and reclassification candidates
- ✅ `notes_raw` contains no pipeline source references, IMP numbers, or
  provenance content (IMP-014)
- ✅ `last_verified_date` populated with today's date
- ✅ `field_verified` recorded as `false`
- ✅ Reclassification candidates flagged: AP with acres_raw + description_raw
  + distinct governance → RECLASSIFICATION_CANDIDATE in `identity_notes_raw`
- ✅ All map URLs included in `urls_raw` (no separate `map_url_raw` field)
- ✅ `access_point_id` left blank
- ✅ No normalization or standardization applied
- ✅ No inferred or guessed values
- ✅ AP is a visitor-facing entry node — not a feature, amenity, or internal
  site component

------------------------------------------------------------
# 16. MODULE DEPENDENCIES

This module depends on:

- Access Point Schema Module v6.0
- Access Point Vocabulary Module v6.0
- Access Point Normalization Contract v6.x *(pending)*
- Site Discovery Sub-Procedure v6.0
- Trailthing Discovery Sub-Procedure v6.0
- Site Network Discovery Sub-Procedure v6.0
- Discovery Orchestration Module v6.x *(or v5.x)*
- Resolution Engine v6.x *(or v5.x)*
- GPS Acquisition Module v6.x *(or v5.x)*

------------------------------------------------------------
# END OF ACCESS POINT DISCOVERY SUB-PROCEDURE v6.0
