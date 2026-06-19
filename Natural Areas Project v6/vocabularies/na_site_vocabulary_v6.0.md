# NATURAL AREAS PROJECT
# SITE VOCABULARY MODULE v6.0
(Authoritative Controlled Vocabularies for Site Entities)

This module contains all controlled vocabularies for Site entities in the
Natural Areas Project v6.x architecture.

All Site-related modules must reference this module for vocabulary authority.

------------------------------------------------------------
# CHANGES FROM v5.6 → v6.0

- **Habitat Type guidance added** (§8, IMP-011): New free-text field for
  ecological/natural character of the site. Open vocabulary — no controlled
  values in v6.0. Guidance on what to capture, what not to capture, and
  expected value patterns.

- **Access Notes guidance added** (§9, IMP-012): New free-text field for
  seasonal access restrictions, public access status detail, and access
  caveats. Relationship to Status field clarified.

- **Last Verified Date and Field Verified guidance added** (§10, IMP-013):
  Brief usage guidance for the two new verification tracking fields.

- **All v5.6 controlled vocabularies carried forward unchanged**: Category,
  Subtype, Designation, Status, and Features values are identical to v5.6.
  No values added or removed in this release.

- **Notes field guidance added** (§11, IMP-014): Explicit guidance that Notes
  is a customer-facing field; provenance artifacts must not appear here.

- **Description field guidance added** (§12, IMP-015): Explicit mandate that
  description prioritizes ecological and physical character.

------------------------------------------------------------
# 1. PURPOSE

This module defines the authoritative controlled vocabularies for:
- Category (§2)
- Subtype — category-dependent (§3)
- Designation (§4)
- Status (§5)
- Features (§6)

And provides field guidance for free-text fields:
- Ownership (§7)
- Habitat Type (§8) — new in v6.0
- Access Notes (§9) — new in v6.0
- Last Verified Date / Field Verified (§10) — new in v6.0
- Notes (§11)
- Description (§12)

These vocabularies are used across:
- Site Discovery Sub-Procedure v6.x (raw capture)
- Resolution Engine v6.x (conflict detection)
- Normalization Engine v6.x (vocabulary mapping)
- Site TSV Output Specification v6.x (output format)

**Key Principle:** Vocabularies are DESCRIPTIVE, not PRESCRIPTIVE.
- Values describe what authoritative sources document
- Values are not inferred from geography, governance, or context
- If no documented value matches, leave the field blank

------------------------------------------------------------
# 2. CATEGORY (Controlled)

## 2.1 Allowed Values

- Campground
- Cemetery
- Community Garden
- Conservation Area
- Cultural Facility
- Curated Biological Site
- Fishing Area
- Historic Site
- Hunting Area
- Memorial
- Museum
- Natural Area
- Nature Preserve
- Open Space
- Park
- Recreation Facility
- Water Site
- Wildlife Area

------------------------------------------------------------
## 2.2 Definitions & Usage Rules

- Describes the primary identity-bearing classification of the Site.
- Must not encode governance, ownership, designation, or temporary conditions.
- One value only; leave blank if undocumented.
- Must reflect what the site actually is — not a GIS layer classification label.

**Key distinctions:**

**Park vs. Natural Area**: A Park is a place managed for public recreation and
enjoyment; a Natural Area is a place managed primarily for its natural character
(ecological, geological, or landscape value). A park with trails is still a Park
if its primary purpose is public recreation. A forest tract managed primarily for
ecological value is a Natural Area even if it has a trail.

**Nature Preserve vs. Natural Area**: Nature Preserve implies a formal level of
legal or organizational protection — state designation, land trust ownership, or
conservation easement. Natural Area is the broader category for documented natural
character without implied formal protection status.

**Conservation Area vs. Natural Area**: Conservation Area is used for land
actively managed for a conservation purpose (habitat restoration, watershed
protection, resource management) where the management program is the defining
identity. Natural Area is used when the land's natural character is the defining
identity, independent of management program.

**Wildlife Area vs. Natural Area**: Wildlife Area implies primary purpose is
wildlife management — hunting, trapping, or documented wildlife management
program. Not just "has wildlife."

**Recreation Facility vs. Park**: Recreation Facility is for places whose primary
purpose is a built recreational infrastructure (sports complex, pool, ice rink,
disc golf course). Park is for places with a mix of natural and built recreation
character.

**Open Space vs. Park**: Open Space is primarily visual or buffering — greenbelts,
civic lawns, boulevard medians. Not a park because it lacks programmatic
recreational use. A park with poor programming is still a Park.

**Historic Site vs. Memorial**: Historic Site is a place where something historically
significant occurred or is preserved. Memorial is a structure or place established
specifically to commemorate — a monument, war memorial, veterans memorial.

**Museum vs. Cultural Facility**: Museum is for places whose primary purpose is
collection, interpretation, and display. Cultural Facility is for places whose
primary purpose is performance, gathering, or cultural programming without a
primary collection function.

**Normalization guidance:**

| Raw Value | Maps To | Notes |
|---|---|---|
| "recreation area" | Park or Recreation Facility | Natural/passive → Park; built/active → Recreation Facility |
| "natural feature" | Natural Area or Water Site | Geological → Natural Area; water body → Water Site |
| "arboretum" (as category) | Curated Biological Site | Set subtype = Arboretum |
| "nature area" / "natural space" | Natural Area | Case/phrasing normalization |
| "preserve" (standalone) | Nature Preserve or Conservation Area | ODNR/formally designated → Nature Preserve; land trust/easement → Conservation Area |
| "greenway" (as category) | Park or Open Space | Trail corridor → Park (subtype: Linear Park); aesthetic/buffer → Open Space |
| "historic landmark" (as category) | Historic Site | Subtype per §3.2 |
| "wildlife management area" | Wildlife Area | Standard normalization |

**FATAL REJECT** — values with no valid mapping and no resolution path: discard,
log, flag for manual assignment.

------------------------------------------------------------
# 3. SUBTYPE (Controlled, Category-Dependent)

## 3.1 Rules

- Zero or one subtype per Site.
- Must belong to the list for the Site's Category.
- Must not be inferred from features or amenities.
- **Exception — Name-keyword inference (IMP-065, IMP-099):** For Nature Preserve,
  Water Site, Recreation Facility, Campground, and Cemetery, subtype MAY be
  deterministically inferred from name keywords, governance, or ownership when
  subtype is blank after vocabulary validation. See §8.4 Subtype Inference Rules.
  This exception applies only to the five named categories; all other categories
  must be explicitly documented.
- Leave blank if unclear or if inference rules do not match.

------------------------------------------------------------
## 3.2 Subtype Lists by Category

### Park
- Greenspace
- Neighborhood Park
- Linear Park
- Dog Park
- Playground Park
- Sports Park
- Waterfront Park
- Civic Park
- Historic Park

### Natural Area
- Forest
- Upland Forest
- Floodplain Forest
- Prairie
- Grassland
- Meadow
- Shrubland
- Savanna
- Old Field
- Successional Area
- Wetland
- Marsh
- Fen
- Bog
- Swamp
- Riparian Area
- Ravine
- Cliff or Bluff
- Barrens
- Dune

### Nature Preserve
- State Nature Preserve
- Private Nature Preserve
- County Nature Preserve
- Municipal Nature Preserve
- Land Trust Preserve
- Conservation Easement Preserve

### Wildlife Area
- State Wildlife Area
- Federal Wildlife Area
- Waterfowl Area
- Migratory Bird Area
- Wetland Management Area

### Conservation Area
- Restoration Area
- Habitat Management Area
- Resource Protection Area
- Watershed Protection Area
- Forest Management Area

### Open Space
- Urban Open Space
- Suburban Open Space
- Greenbelt
- Commons
- Civic Lawn
- Boulevard Median

### Recreation Facility
- Sports Complex
- Athletic Field
- Skate Park
- Swimming Pool
- Recreation Center
- Tennis Complex
- Pickleball Complex
- Golf Course
- Disc Golf Course
- Ice Rink
- BMX Track
- Pump Track

### Cultural Facility
- Cultural Center
- Performing Arts Center
- Interpretive Center
- Heritage Center
- Art Center
- Visitor Center

### Historic Site
- Historic Landmark
- Archaeological Site
- Historic Landscape
- Battlefield
- Historic Structure

### Cemetery
- Public Cemetery
- Private Cemetery
- Family Cemetery
- Veterans Cemetery
- Church Cemetery
- Green Burial Cemetery

### Memorial
- War Memorial
- Veterans Memorial
- Civic Memorial
- Monument
- Memorial Garden
- Memorial Plaza

### Community Garden
*(no subtypes)*

### Campground
- Tent Campground
- RV Campground
- Primitive Campground
- Group Campground
- Cabin Campground

### Water Site
- Lake
- Pond
- Reservoir
- River
- Harbor
- Marina
- Boat Launch Area
- Fishing Lake
- Retention Pond

### Curated Biological Site
- Arboretum
- Botanical Garden
- Zoo
- Aquarium
- Aviary
- Insectarium
- Butterfly House
- Reptile House
- Biopark
- Living Museum

### Museum
- History Museum
- Art Museum
- Science Museum
- Children's Museum
- Natural History Museum
- Cultural Museum

### Hunting Area
*(no subtypes)*

### Fishing Area
*(no subtypes)*

------------------------------------------------------------
# 4. DESIGNATION (Controlled)

## 4.1 Rules

- Describes formal legal or administrative protective or recognition status.
- Must be explicitly documented — never inferred from governance, ownership,
  or category.
- Multiple values allowed (semicolon-delimited).
- Leave blank if undocumented.
- "None" is used only when explicitly documented. Do not write "None" when
  designation status is simply unknown.

------------------------------------------------------------
## 4.2 Federal Designations

- National Park
- National Monument
- National Historic Site
- National Memorial
- National Historic Landmark
- National Natural Landmark
- National Recreation Area
- National Wildlife Refuge
- National Scenic Trail
- National Wild and Scenic River
- National Heritage Area
- National Battlefield
- National Cemetery
- National Register of Historic Places (NRHP)
- National Forest
- National Grassland
- National Historic Trail
- Wilderness Area

------------------------------------------------------------
## 4.3 State Designations

- State Park
- State Nature Preserve
- State Wildlife Area
- State Fishing Area
- State Hunting Area
- State Memorial
- State Forest
- State Scenic River
- State Natural Landmark
- State Archaeological Preserve
- State Historic Site
- State Recreation Area
- State Nature Area

------------------------------------------------------------
## 4.4 Local / Special Designations

- County Historic Landmark
- Municipal Historic Landmark
- Local Historic Landmark
- Local Nature Preserve
- Registered Cemetery
- Protected Wetland
- Mitigation Bank
- Conservation Easement
- Land Trust Preserve

------------------------------------------------------------
# 5. STATUS (Controlled)

## 5.1 Allowed Values

- Active
- Seasonal
- Access Permit Required
- No Public Entry
- Under Development
- Proposed
- Abandoned
- Closed
- Defunct
- Historical
- Unknown

------------------------------------------------------------
## 5.2 Definitions & Usage Rules

### Active
Site is currently operational and open to the public under normal conditions.
Default when no other status is documented and the site is clearly operational.

**Normalization:** "open," "open to public," "operational" → "Active"

---

### Seasonal
Site is open to the public on a seasonal schedule.

**When to use:**
- ✅ Source explicitly documents seasonal operation
- ✅ Site is documented as closed in winter or open only in summer

**When NOT to use:**
- ❌ Site has some seasonal programs but is otherwise open year-round
- ❌ Inferred from site type alone

---

### Access Permit Required
Site is accessible to the public only with a permit, reservation, or documented
authorization process.

**When to use:**
- ✅ Source explicitly states permit or reservation required
- ✅ State nature preserves with access permit programs
- ✅ Research stations or managed areas with controlled entry

**Note:** When this status is used, document the permit type and process in
`access_notes`. Status alone does not tell a user how to get access.

---

### No Public Entry
Site is documented as having no public access — it is protected or managed but
not open to the public.

**When to use:**
- ✅ Source explicitly states no public access
- ✅ Conservation easement land documented as private
- ✅ Working farm or utility property documented in the project for conservation value

**Note:** Document the reason and any access exceptions in `access_notes`.

---

### Under Development
Site is being actively developed or built out — documented as coming soon or
under construction for public use.

**Normalization:** "under construction," "coming soon," "in development" → "Under Development"

---

### Proposed
Site is documented as proposed but not yet formally established or in development.

**When NOT to use:**
- ❌ Inferred from planning maps or speculative coverage
- ❌ Sites in early fundraising without a formal proposal

**Normalization:** "proposed," "future" → "Proposed"

---

### Abandoned
Site is documented as untended, unmanaged, or no longer receiving active
stewardship — but has not been formally closed or transferred.

**Primarily used for:** cemeteries that are no longer actively maintained.

**When NOT to use:**
- ❌ Sites with reduced programming
- ❌ Sites temporarily closed for renovation

---

### Closed
Site is permanently closed to public access.

**Must be explicitly documented** — do not infer from lack of web presence.

**Normalization:** "permanently closed," "no longer open" → "Closed"

---

### Defunct
Applies **only** to Tier 5 township entities that have been fully dissolved or
absorbed into a municipality. Defunct townships produce zero entity records; a
discovery note documents the historical context and evidence.

---

### Historical
The site represents a named natural area or ecological feature that is documented
in authoritative sources (GNIS, USGS, historical surveys, etc.) but no longer
exists as a managed or physically distinct natural area. The name and location are
recorded for historical completeness and geographic reference.

**When to use:**
- ✅ GNIS-enumerated place name for a feature (marsh, wetland, woodland) that was
  drained, converted, or otherwise eliminated before the v6 project baseline
- ✅ Ecological complex documented in historical literature but lacking any current
  managing entity, public access, or physical remnant
- ✅ Entities confirmed "historical only" after exhaustive T1–T8 discovery with no
  managing organization found

**When NOT to use:**
- ❌ Sites that are currently closed but retain physical character and management
  potential → use "Closed"
- ❌ Sites that have no public entry but are actively managed → use "No Public Entry"
- ❌ Inferred from mere absence of web presence

**GPS:** These entities typically have GPS from GNIS or historical survey records;
set `gps_unresolvable = true` if no precise GPS is available. GPS at centroid
precision is acceptable when no point-level source exists.

**Notes:** Record the GNIS feature ID, historical source, and the approximate
date of elimination or conversion if known.

**Normalization:** "historical," "former," "historical place name," "no longer
present," "drained [feature name]" → "Historical"

---

### Unknown
Use sparingly and only when the site's operational status genuinely cannot be
determined from available sources. Prefer leaving Status blank over using Unknown
when the site appears active.

------------------------------------------------------------
# 6. FEATURES (Controlled)

## 6.1 Rules

- Features represent notable internal physical components, infrastructure,
  or ecological features of a Site.
- Must be documented in authoritative sources — not inferred from site type,
  governance, or assumed from site character.
- Must not include Trailthings, Access Points, or child Sites — those are
  separate entity records.
- Semicolon-delimited list; alphabetized.
- **Activities are prohibited** — hiking, fishing, birdwatching, and similar
  activities describe what people do at a site, not what the site contains.
  Map activities to physical infrastructure where possible (fishing → Fishing
  Area or Boat Ramp; hiking → trails, which are Trailthing records).
- **Ecological character primarily belongs in Habitat Type**, not Features —
  "wetland" and "riparian" may appear in Features when explicitly listed as
  an amenity or feature by the authoritative source, but Habitat Type is the
  primary field for ecological character queries.

## 6.2 Allowed Values

ADA Accessible
AED
Alvar
Amphibian Area
Amphitheater
Apiary
Arboretum
Archery Range
Art Gallery
Art Installation
Athletic Field
Ball Diamond
Ballroom
Bandstand
Basketball Court
Beach
Bike Rack
Bike Repair Station
Bird Viewing Area
Boardwalk
Boat Dock
Boat Ramp
Bocce Court
Bog
Bluff
Boathouse
Bridge
Bridle Trail
Building Ruins
Butterfly or Pollinator Garden
Camping
Cabin Rentals
Canal Structure
Cave or Cavern
Cemetery Section
Chapel
Cliff
Climbing Structure
Community Center
Community Garden
Composting Station
Conservatory
Covered Shelter
Cricket Pitch
Culvert
Dam
Dance Floor
Dance Performance Space
Demonstration Farm Plot
Demonstration Garden
Disc Golf Course
Dog Park
Drainage Ditch
Dune
Educational Pavilion
Electric Vehicle Charging
Equestrian Arena
Farm Store
Fence
Fen
Fieldhouse
Fire Ring
Fire Tower
Fishing Area
Fitness Station
Football Field
Football Stadium
Fountain
Garage
Garden
Gate
Gatehouse
Gazebo
Glacial Erratic
Golf Course
Gorge
Greenhouse
Grill
Guided Tours
Habitat Restoration Area
Handball Court
Hiking Trail
Hilltop
Historic Bridge
Historic Canal Segment
Historic Cemetery Section
Historic Fence Line
Historic Foundation
Historic Lock
Historic Marker
Historic Marker Cluster
Historic Millrace
Historic Road Trace
Historic Ruins
Historic Structure
Historic Well
Horseshoe Pitch
Hunting Area
Ice Rink
Information Board
Insectarium
Interpretive Exhibit
Interpretive Garden
Interpretive Sign
Island
Kiosk
Kite Flying
Lacrosse Field
Lake
Landmark Tree
Levee
Lodge
Lookout Cabin
Maintenance Building
Marina
Marsh
Meadow
Model Airplane Field
Model Rocketry Field
Mini Golf
Monitoring Station
Monument
Mountain Bike Trail
Multi-use Trail
Museum Building
Musical Instruments
Musical Performance Space
Native American Artifacts
Native American Cultural Site
Native American Earthwork
Natural Arch
Nature Center
Nature Play Area
Observation Deck
Observation Tower
Observatory
Old-Growth Stand
Orchard
Outdoor Art Installation
Outdoor Classroom
Overflow Parking
Overlook (built)
Overlook (natural)
Parking Lot
Pavilion
Peninsula
Pickleball Court
Picnic Area
Picnic Shelter
Picnic Table Cluster
Pipeline Corridor
Pioneer Historic Site
Pioneer Re-creation
Planetarium
Playground
Pollinator Garden
Pond
Powerline Corridor
Prairie
Prairie Restoration
Public Art Installation
Pump Station
Pump Track
Rain Garden
Ravine
Reforestation Area
Reptile House
Research Plot
Restrooms
Ropes Course
Retaining Wall
Retention Basin
Ridge
Rock Outcrop
Scenic View
S&M Dungeon
Sculpture
Sedge Meadow
Shooting Range
Shotgun Range
Shuffleboard Court
Silo
Sinkhole
Ski Slopes
Skate Park
Sledding Hill
Slide
Soccer Pitch
Spillway
Spray Park
Spring
Stable
Stage
Stormwater Basin
Stream Segment
Swimming Beach
Swimming Pool
Swing Set
Tennis Court
Theatre
Topiary
Trapping Area
Transit Stop
Trolley
Tropical Garden
Utility Corridor
Valley
Vegetable Garden
Vernal Pool
Via Ferrata
Viewing Platform
Vineyard
Visitor Center
Volleyball Court
Wall
Water Park
Water Tower
Watercraft Access
Waterfall (built)
Waterfall (natural)
Waterslide
Weather Station
Weir
Wetland
Wetland Restoration
Wilderness Area
Wild Animal Rehabilitation
Wildlife Observation Area
Working Railway
Zoo

------------------------------------------------------------
# 7. OWNERSHIP (Free-Text — No Controlled Vocabulary)

## 7.1 Overview

Ownership is a free-text field capturing legal title only.

## 7.2 What to Collect

- Legal name of the entity that holds title to the land
- Only when explicitly documented

## 7.3 What NOT to Collect

- ❌ Managing organizations (those go in Governance)
- ❌ Program names or GIS classification labels
- ❌ Inferred ownership from governance

## 7.4 When to Leave Blank

Blank when ownership is distributed across multiple entities, when the site is
a legal right-of-way without a single fee owner, or when unclear.

------------------------------------------------------------
# 8. HABITAT TYPE (Free-Text — Open Vocabulary)

## 8.1 Overview

Habitat Type is a **new free-text field in v6.0** (IMP-011). There is no
controlled vocabulary at this time. The vocabulary will be tightened after
sufficient county runs establish what values are realistic in Ohio.

## 8.2 Purpose

Habitat Type captures the ecological or natural character of the site — what
kind of habitat or land cover type defines it. It enables queries that the
Features field cannot cleanly support: "find all sites with wetland habitat,"
"find all riparian corridor sites," "find all old-growth woodland sites."

Habitat Type answers: *what kind of land is this?*

## 8.3 What to Capture

Ecological or natural character terms drawn from authoritative source descriptions
or documented ecological classification. Verbatim or close paraphrase from source.

**Examples of useful values:**
- "Wet prairie remnant"
- "Oak-hickory woodland"
- "Riparian corridor"
- "Emergent wetland"
- "Glacial lake"
- "Shrub-scrub wetland"
- "Limestone glade"
- "Old-growth beech-maple forest"
- "Mixed upland forest"
- "Calcareous fen"
- "Sand barrens"
- "Floodplain forest"
- "Vernal pool complex"

## 8.4 What NOT to Capture

- ❌ Amenities or infrastructure ("pavilion," "playground") — those go in Features
- ❌ Activities ("hiking," "birdwatching") — those go in Features or are dropped
- ❌ Governance or management labels ("ODNR Wildlife Area") — those go in Governance
- ❌ Category or subtype labels ("nature preserve," "park") — those go in Category/Subtype
- ❌ Geographic names ("near the Maumee River") — those go in Location or Description

## 8.5 When to Leave Blank

Blank is acceptable for:
- Sites with no meaningful ecological character (cemeteries, purely developed
  recreation facilities, urban plazas)
- Sites where ecological type is genuinely undocumented in available sources
- Batch-loaded records pending a verification or description pass

Blank does not require documentation — it simply reflects that the ecological
character has not yet been captured or is not applicable.

## 8.6 Discovery vs. Normalization

- **Discovery stage**: capture in `habitat_type_raw` — verbatim from source,
  no normalization
- **Normalized stage**: `habitat_type` field — carry forward verbatim; do not
  map to controlled vocabulary until v6.x establishes controlled values

------------------------------------------------------------
# 9. ACCESS NOTES (Free-Text — No Controlled Vocabulary)

## 9.1 Overview

Access Notes is a **new free-text field in v6.0** (IMP-012). There is no
controlled vocabulary.

## 9.2 Purpose

Access Notes captures access information that does not fit the Status field or
other structured fields. It supplements Status with explanatory detail about
*how* access works, *when* the site is accessible, and *what* conditions apply.

## 9.3 What to Capture

- **Seasonal access restrictions**: "Closed to public during deer gun season
  (typically Nov–Dec)"; "Trail system closed during spring thaw, typically
  March–April"
- **Public access status detail**: "Open to public by permit only — call ODNR
  Division of Natural Areas at [number] to schedule access"; "No public trail
  access; conservation easement land protected but not open for recreation"
- **Hours and scheduling**: "Day use only, dawn to dusk"; "Reservations required
  for shelter use"
- **Physical access caveats**: "Accessible from CR-4 only; no on-site parking
  lot — roadside parking on CR-4 shoulder"; "Boat-in access only; no land-based
  trail access"
- **Entry conditions**: "Dogs permitted on leash"; "Hunting permitted in season —
  wear blaze orange during deer season"

## 9.4 What NOT to Capture

- ❌ Overall operational status — that goes in Status
- ❌ Amenity inventory — that goes in Features
- ❌ Site character or ecological description — that goes in Description or Habitat Type

## 9.5 Relationship to Status

Status captures the overall operational state of the site. Access Notes captures
specific conditions within that state. These fields are complementary, not redundant:

| Status | Access Notes use |
|---|---|
| Active | Seasonal restrictions, hours, hunting season warnings, permit requirements |
| Access Permit Required | Permit type, how to obtain, contact info |
| No Public Entry | Reason for no entry; any exceptions |
| Seasonal | Which seasons open; how to verify current conditions |

When Status = "Access Permit Required" or "No Public Entry," Access Notes should
always be populated with explanatory detail.

## 9.6 Discovery vs. Normalization

- **Discovery stage**: capture in `access_notes_raw`
- **Normalized stage**: `access_notes` field — carry forward; free text

------------------------------------------------------------
# 10. LAST VERIFIED DATE AND FIELD VERIFIED

## 10.1 Last Verified Date

`last_verified_date` — DATE field (YYYY-MM-DD). No controlled vocabulary.

Records the date the site record was last confirmed accurate against an
authoritative source. Populate or update whenever a session actively reviews
and confirms the record. Does not update automatically on pipeline re-runs.

**Discovery guidance**: populate at discovery time with the current date.
Update during any subsequent verification pass.

## 10.2 Field Verified

`field_verified` — boolean, default false. No controlled vocabulary.

Set to true when the user has physically visited the site and confirmed its
existence, access, and general character. Never set to true based on web
review alone.

**Visit planning queries**: `WHERE field_verified = false` surfaces all sites
not yet personally confirmed. Combined with other filters (blank description,
blank habitat_type, no map URL), this enables a targeted pre-visit checklist.
See IMP-018 for the planned visit planning query template.

------------------------------------------------------------
# 11. NOTES (Free-Text — No Controlled Vocabulary)

## 11.1 Overview

Notes is a customer-facing free-text field. There is no controlled vocabulary.

## 11.2 What to Capture

- Operational context relevant to understanding the site
- Discovery gaps (e.g., "member trail count not confirmed; ODNR trail register
  listed 3 trails but source page was unavailable at time of discovery")
- Historical context not covered by Description
- Boundary notes or access caveats that don't fit Access Notes
- Caveats about record completeness

## 11.3 What NOT to Capture

- ❌ **Pipeline provenance artifacts** — source citations (MORPC layer, ODNR
  batch, IMP numbers, GPS acquisition source, batch load dates), pipeline
  mechanic notes, and similar process or provenance content must not appear
  here. Notes is readable by someone who knows nothing about the pipeline.
  Provenance belongs in the provenance tables.
- ❌ Access information — that belongs in Access Notes
- ❌ Amenity inventory — that belongs in Features
- ❌ Ecological character — that belongs in Description or Habitat Type
- ❌ Identity flags or disambiguation — those belong in Identity Notes

------------------------------------------------------------
# 12. DESCRIPTION (Free-Text — No Controlled Vocabulary)

## 12.1 Overview

Description is a customer-facing free-text field. There is no controlled
vocabulary.

## 12.2 What to Capture

**Priority: ecological and physical character.** Description should answer:
what kind of land is this, what is its ecological character, what makes it
notable or significant?

- Land cover type: woodland, wetland, prairie, riparian corridor, glacial lake
- Topography: rolling moraine, flat glacial plain, deeply dissected ravines
- Notable ecological features: calcareous fen community, old-growth canopy,
  significant vernal pool complex, rare plant communities
- Conservation significance: state-dedicated nature preserve, nationally
  significant habitat, regionally important wetland complex
- Brief establishment history or protection context where meaningful

## 12.3 What NOT to Capture

- ❌ **Amenity inventory** — "features a pavilion, restrooms, and a playground"
  belongs in Features, not Description. Description is not a facility list.
- ❌ Restatement of governance, ownership, or designation fields
- ❌ Temporary conditions
- ❌ Content that duplicates Notes

------------------------------------------------------------
# 13. VOCABULARY NORMALIZATION RULES — ENFORCEMENT

The Normalization Engine must apply the mapping tables in this section to
every controlled Site field. Out-of-vocabulary values must be mapped or
handled per the rules below.

------------------------------------------------------------
## 13.1 Category Normalization Mapping (IMP-063)

Normalization engine must validate every `category` value against the 18-value
list in §2.1. Invalid values must be mapped using the table in §2.2; ambiguous
cases are flagged for manual review, not auto-corrected. Values with no mapping
→ **FATAL REJECT**.

------------------------------------------------------------
## 13.2 Cultural Institution Name-Pattern Recognition (IMP-068)

When a site name contains any of the following patterns, the indicated category
**must** be assigned. This is a hard-assignment rule applied before vocabulary
enforcement.

| Name Contains (case-insensitive) | Required Category | Notes |
|---|---|---|
| "Botanical Garden" / "Botanical Gardens" / "Conservatory and Botanical Gardens" | Curated Biological Site | Subtype = Botanical Garden |
| "Conservatory" (standalone) | Curated Biological Site | Primarily horticultural → Botanical Garden; performing arts → Cultural Facility |
| "Arboretum" | Curated Biological Site | Subtype = Arboretum |
| "Zoo" / "Zoological" | Curated Biological Site | Subtype = Zoo |
| "Aquarium" | Curated Biological Site | Subtype = Aquarium |
| "Aviary" | Curated Biological Site | Subtype = Aviary |
| "Museum" | Museum | Subtype per §3.2 |
| "Science Center" / "Science Industry" / "Science Museum" | Museum | Subtype = Science Museum |
| "Hall of Fame" | Museum | Subtype from context |

Normalization-side application: if recorded `category` = "Recreation Facility"
but name matches a pattern above, flag as **CATEGORY MISMATCH** review item.
Do not auto-correct; surface for human review.

------------------------------------------------------------
## 13.3 Subtype Normalization Mapping (IMP-064)

Invalid subtype values (not in the category-specific list in §3.2) must be
mapped using the table below. Values with no valid mapping → **null the subtype
field** (do not reject the entity).

**Park subtypes:**

| Raw Subtype | Maps To | Notes |
|---|---|---|
| "Community Park" | Neighborhood Park | Direct synonym |
| "Pocket Park" | Neighborhood Park | Small neighborhood-scale parks |
| "Greenway" / "Trail Corridor" | Linear Park | Linear connectivity corridors |
| "Natural Park" / "Woodland Park" / "Riparian Park" | Greenspace | Primarily natural character parks |
| "Regional Park" | null | No vocabulary equivalent; flag for review |
| "Metro Park" | null | Governance label, not a subtype |

**Nature Preserve subtypes — ecological descriptor routing:**

The following raw values are ecological descriptors that belong in `description`
and `habitat_type`, not `subtype`:
Bog, Fen, Forest, Old-Growth Forest, Wetland, Woodland, Riparian, Savanna,
Prairie, Meadow, Shrubland, Grassland, Successional Area, Upland, Floodplain,
Ravine, Cliff.

When these appear in `subtype` for a Nature Preserve: null the `subtype` field.
If `description` does not already contain the ecological character, route to
`habitat_type` as well.

**Recreation Facility subtypes — Features terms misplaced in subtype:**

These are Features vocabulary terms and must not appear in `subtype`:
Gazebo, Pavilion, Splash Pad, Spray Park, Skate Bowl, Mountain Bike Park,
Pump Track, BMX.

When found in `subtype` for a Recreation Facility: null `subtype` and ensure
the corresponding Features vocabulary term appears in `features`.
Exception: "Skate Park" (without "Bowl") is a valid Recreation Facility subtype.

**Other categories — common out-of-vocabulary values:**

| Raw Subtype | Category | Maps To | Notes |
|---|---|---|---|
| "Lake/Wetland" | Water Site | null | Ambiguous; flag for manual resolution |
| "Swimming Hole" | Water Site | null | Flag for vocabulary expansion |
| "Green Burial Cemetery" | Cemetery | Green Burial Cemetery | Valid; already in vocabulary |
| "Living Museum" | Curated Biological Site | Living Museum | Valid; already in vocabulary |

------------------------------------------------------------
## 13.4 Subtype Inference Rules (IMP-065, IMP-099)

Applied **after** vocabulary validation, **only when `subtype` is blank**.
Inference is deterministic — no ambiguity, no judgment. If inference rules do
not unambiguously match, leave `subtype` blank. Record inference basis in
normalization provenance as `subtype_source = "name_inference"` or
`subtype_source = "description_inference"`.

### Nature Preserve
Evaluate in order; use the first match:
1. If `designation` = "State Nature Preserve" → subtype = "State Nature Preserve"
2. If `name` contains "State Nature Preserve" (case-insensitive) → subtype = "State Nature Preserve"
3. Else → subtype = "Private Nature Preserve"

### Water Site
Match against `name` (case-insensitive, whole-word or phrase):
- "River" / "Creek" / "Stream" / "Run" → "River"
- "Reservoir" → "Reservoir" (takes priority over "Lake" when both appear)
- "Lake" (without "Reservoir") → "Lake"
- "Pond" → "Pond"
- "Harbor" → "Harbor"
- "Marina" → "Marina"

No match → leave blank.

### Recreation Facility
Match against `name` (case-insensitive):
- "Golf Course" → "Golf Course"
- "Pool" / "Aquatic Center" / "Swim Center" → "Swimming Pool"
- "Tennis" → "Tennis Complex"
- "Pickleball" → "Pickleball Complex"
- "Skate Park" → "Skate Park"
- "Disc Golf" → "Disc Golf Course"
- "Ice Rink" / "Ice Arena" → "Ice Rink"
- "BMX" → "BMX Track"
- "Pump Track" → "Pump Track"
- "Sports Complex" / "Athletic Complex" / "Recreation Complex" → "Sports Complex"
- "Athletic Field" / "Soccer Field" / "Baseball Field" / "Softball Field" → "Athletic Field"
- "Recreation Center" / "Rec Center" / "Community Center" → "Recreation Center"

No match → leave blank.

### Campground
Match against `description` (apply first match):
- "cabin" / "lodge" → "Cabin Campground"
- "RV" / "hookup" / "electric" → "RV Campground"
- "primitive" → "Primitive Campground"
- "group" → "Group Campground"

No match → leave blank.

### Cemetery (IMP-099)
Apply in order; use the first matching rule. Evidence sources: `name`,
`governance_raw`, `ownership_raw`, `designation`.

1. `designation` includes "National Cemetery" OR `name` contains "National Cemetery" → **Veterans Cemetery**
2. `name` contains "Veterans" OR "Soldiers" OR "G.A.R." → **Veterans Cemetery**
3. `governance_raw` or `ownership_raw` references a church denomination, diocese, parish,
   or religious organization → **Church Cemetery**
4. `name` matches "[Surname] Family Cemetery" OR contains "Family Cemetery" OR "Family Burial" → **Family Cemetery**
5. `name` contains "Green Burial" OR "Natural Burial" → **Green Burial Cemetery**
6. `governance_raw` or `ownership_raw` is a government entity (township, municipality,
   county, state, federal) → **Public Cemetery**
7. None of the above → **Private Cemetery**

Note: Use the ownership entity for rule 6; maintenance entity alone does not
override ownership classification.

**Status guidance for cemeteries:** "Active" = currently accepting burials or
actively maintained; "Abandoned" = untended, no active management. "Historic"
is not a vocabulary status value — use "Active" for maintained historic cemeteries
or "Abandoned" for untended ones; note historical character in `description`.

------------------------------------------------------------
## 13.5 Status Normalization Mapping

| Raw Value | Maps To | Notes |
|---|---|---|
| "open" / "open to public" / "operational" | Active | Standard synonyms |
| "open seasonally" / "seasonal" | Seasonal | Standard synonyms |
| "by permit only" / "permit required" / "reservation required" | Access Permit Required | Standard synonyms |
| "no trespassing" / "private" / "no public access" | No Public Entry | Standard synonyms |
| "under construction" / "coming soon" / "in development" | Under Development | Standard synonyms |
| "proposed" / "future" | Proposed | Standard synonyms |
| "permanently closed" / "no longer open" | Closed | Standard synonyms |
| "dormant" / "untended" / "overgrown" | Abandoned | Verify context |
| Empty string ("") | null | Empty string is not a valid blank |
| Ambiguous or compound values | **REVIEW** | Surface for human resolution |

------------------------------------------------------------
## 13.6 Multi-Value and Empty String Enforcement

Category, Subtype, and Status are single-value fields.

When a compound value appears and cannot be resolved to a single canonical value:
1. Set the field to blank
2. Append to identity_notes: "[field] compound value: '[raw]' — could not resolve;
   flagged for review"
3. Write raw value to normalization_provenance as "compound_value_stripped"

An empty string ("") is not a valid blank in any vocabulary-controlled field.
After mapping table application: if the result is an empty string → convert to
null. Log: "field [name]: empty string converted to null."

------------------------------------------------------------
# 14. VOCABULARY USAGE RULES

## 14.1 Universal Rules

1. **Use exactly as written** — No synonyms, abbreviations, or invented terms
2. **Don't infer** — Values must be documented, not inferred from context
   (exception: deterministic subtype inference per §13.4)
3. **Leave blank if unclear** — Better no value than wrong value
4. **One value per controlled field** — No multi-value controlled fields
   except Designation (semicolon-delimited multiple allowed)
5. **Flag new values** — Do not add values; flag for vocabulary expansion

## 14.2 Discovery Phase

- Capture raw values exactly as found in `_raw` fields
- Do not attempt normalization during discovery
- `governance_raw` must contain only the managing organization's name —
  never GIS park type labels
- `features_raw` is a list, not narrative prose
- `description_raw` is narrative prose, not a facility list
- `habitat_type_raw` is verbatim ecological language from the source
- `access_notes_raw` captures access restrictions and caveats
- Capture identity clarifications in `identity_notes_raw`

## 14.3 Normalization Phase

- Apply §13.x mapping tables to all vocabulary-controlled fields
- Route ecological descriptors from subtype to description/habitat_type per §13.3
- Handle compound values per §13.6
- Convert empty strings to null per §13.6
- Null-and-log all unmappable values
- Surface REVIEW items for human resolution before TSV output

------------------------------------------------------------
# 15. MODULE DEPENDENCIES

This vocabulary module integrates with:

- Site Schema Module v6.0 (field definitions)
- Site Discovery Sub-Procedure v6.x (raw capture)
- Resolution Engine v6.x (conflict detection)
- Normalization Engine v6.x (vocabulary mapping)
- Site Normalization Contract v6.x (normalization rules)
- Site TSV Output Specification v6.x (output format)

------------------------------------------------------------
# END OF SITE VOCABULARY MODULE v6.0
