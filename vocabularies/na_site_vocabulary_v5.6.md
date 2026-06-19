# NATURAL AREAS PROJECT
# SITE VOCABULARY MODULE v5.6
(Authoritative Controlled Vocabularies for Site Entities)

This module contains all controlled vocabularies for Site entities in the
Natural Areas Project v5.x architecture.

All Site-related modules must reference this module for vocabulary authority.
Cross‑module references use “v5.x” to indicate compatibility across the v5 family.

------------------------------------------------------------
# 1. PURPOSE

This module defines the authoritative controlled vocabularies for:
- Category
- Subtype (Category-dependent)
- Designation
- Status
- Features

Not controlled vocabularies (rule-governed free-text fields):
- Ownership
- Governance
- Partner Agencies
- Coordination

These vocabularies are used across:
- Site Discovery Sub-Procedure v5.x (raw capture)
- Resolution Engine v5.x (conflict detection)
- Normalization Engine v5.x (vocabulary mapping)
- TSV Output Specification v5.x (output format)

Key principle: Vocabularies are descriptive, not prescriptive.
Values must be documented in authoritative sources; never inferred.

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

## 2.2 Rules & Clarifications

- Describes the primary identity-bearing classification of the Site.
- Must not encode governance, ownership, designation, or temporary conditions.
- One value only; leave blank if undocumented.

Key distinctions:
- Park vs. Natural Area
- Nature Preserve vs. Natural Area
- Conservation Area vs. Natural Area
- Wildlife Area vs. Natural Area
- Recreation Facility vs. Park
- Open Space vs. Park
- Historic Site vs. Memorial
- Museum vs. Cultural Facility

Normalization guidance:
"nature preserve" → "Nature Preserve"  
"wildlife management area" → "Wildlife Area"  
"recreation area" → "Park" or "Recreation Facility"  
"greenway" → "Park" or "Open Space"  
"historic landmark" → "Historic Site"  

------------------------------------------------------------
# 3. SUBTYPE (Controlled, Category-Dependent)

## 3.1 Rules

- Zero or one subtype.
- Must belong to the list for the Site’s Category.
- Must not be inferred from features or amenities.
- **Exception — Name-keyword inference (IMP-065, IMP-099):** For Nature Preserve, Water Site, Recreation Facility, Campground, and Cemetery, subtype MAY be deterministically inferred from name keywords, governance, or ownership when subtype is blank after vocabulary validation. See §7.4 Subtype Inference Rules. This exception applies only to the five named categories; all other categories must be explicitly documented.
- Leave blank if unclear or if inference rules do not match.

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
(no subtypes)

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
(no subtypes)

### Fishing Area
(no subtypes)

------------------------------------------------------------
# 4. DESIGNATION (Controlled)

## 4.1 Rules

- Describes formal legal or administrative status.
- Must be explicitly documented.
- Multiple values allowed (semicolon-delimited).
- Leave blank if undocumented.

## 4.2 Federal Designations
National Park  
National Monument  
National Historic Site  
National Memorial  
National Historic Landmark  
National Natural Landmark  
National Recreation Area  
National Wildlife Refuge  
National Scenic Trail
National Wild and Scenic River
National Heritage Area
National Battlefield  
National Cemetery  
National Register of Historic Places (NRHP)
National Forest
National Grassland
National Historic Trail
Wilderness Area

## 4.3 State Designations
State Park  
State Nature Preserve  
State Wildlife Area  
State Fishing Area  
State Hunting Area  
State Memorial  
State Forest  
State Scenic River  
State Natural Landmark  
State Archaeological Preserve  
State Historic Site  
State Recreation Area
State Nature Area

## 4.4 Local / Special Designations
County Historic Landmark  
Municipal Historic Landmark  
Local Historic Landmark  
Local Nature Preserve  
Registered Cemetery  
Protected Wetland  
Mitigation Bank  
Conservation Easement  
Land Trust Preserve

## 4.5 None
Use “None” only when explicitly documented.  
Leave blank when designation status is unknown.

------------------------------------------------------------
# 5. STATUS (Controlled)

Allowed values:
- Active
- Seasonal
- Access Permit Required
- No Public Entry
- Under Development
- Proposed
- Abandoned
- Closed
- Defunct
- Unknown

Definitions and usage rules remain unchanged.

Note: **Defunct** applies only to Tier 5 township entities that have been fully dissolved or absorbed into a municipality. Defunct townships produce zero entity records; a discovery note documents the historical context and evidence.

------------------------------------------------------------
# 6. FEATURES (Controlled)

## 6.1 Rules

- Features represent internal components of a Site.
- Must not include Trails, Trail Segments, Access Points, or child Sites.
- Semicolon-delimited list.
- Must be documented in authoritative sources.

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
# 7. VOCABULARY NORMALIZATION RULES

------------------------------------------------------------
## 7.1 Category Normalization Mapping (IMP-063)

Normalization engine must validate every `category` value against the 18-value list in §2.1.
Invalid values must be mapped using the table below; ambiguous cases are flagged for manual review,
not auto-corrected. Values with no mapping → **FATAL REJECT**.

| Raw / Out-of-Vocabulary Value | Maps To | Resolution Method |
|-------------------------------|---------|-------------------|
| "recreation area" | "Park" or "Recreation Facility" | Resolve from name/context: primarily natural/passive use → "Park"; primarily built/active recreation → "Recreation Facility". Flag for review if ambiguous. |
| "natural feature" | "Natural Area" or "Water Site" | Resolve from name/context: geological formation → "Natural Area"; water body → "Water Site". Flag for review if ambiguous. |
| "arboretum" (as category value) | "Curated Biological Site" | Set subtype = "Arboretum". |
| "nature area" / "natural space" | "Natural Area" | Case/phrasing normalization. |
| "preserve" (standalone) | "Nature Preserve" or "Conservation Area" | Resolve from governance/designation: ODNR-designated/formally designated → "Nature Preserve"; land trust/easement protected → "Conservation Area". |
| "greenway" (as category) | "Park" or "Open Space" | Resolve from character: linear trail corridor → "Park" (subtype: Linear Park); primarily aesthetic/buffer → "Open Space". |
| "historic landmark" (as category) | "Historic Site" | Subtype resolution per §3.2. |
| "wildlife management area" | "Wildlife Area" | Standard normalization. |

**FATAL REJECT** — values with no valid mapping and no resolution path: discard, log, flag for manual assignment.

------------------------------------------------------------
## 7.2 Cultural Institution Name-Pattern Recognition (IMP-068)

When a site name contains any of the following patterns, the indicated category **must** be assigned.
Discovery-side sources (parks websites, municipal lists) frequently list cultural institutions
alongside parks; this rule prevents Recreation Facility from being defaulted for these sites.
This is a hard-assignment rule applied before vocabulary enforcement.

| Name Contains (case-insensitive) | Required Category | Notes |
|----------------------------------|-------------------|-------|
| "Botanical Garden" / "Botanical Gardens" / "Conservatory and Botanical Gardens" | "Curated Biological Site" | Subtype = "Botanical Garden" |
| "Conservatory" (standalone) | "Curated Biological Site" | Subtype = "Botanical Garden" if primarily horticultural; may also apply to performing arts conservatories → "Cultural Facility" (distinguish by context) |
| "Arboretum" | "Curated Biological Site" | Subtype = "Arboretum" |
| "Zoo" / "Zoological" | "Curated Biological Site" | Subtype = "Zoo" |
| "Aquarium" | "Curated Biological Site" | Subtype = "Aquarium" |
| "Aviary" | "Curated Biological Site" | Subtype = "Aviary" |
| "Museum" | "Museum" | Subtype assigned per §3.2. |
| "Science Center" / "Science Industry" / "Science Museum" | "Museum" | Subtype = "Science Museum" |
| "Hall of Fame" | "Museum" | Subtype determined from type (history, art, etc.) |

Normalization-side application: if recorded `category` = "Recreation Facility" but name matches a
pattern above, flag as a **CATEGORY MISMATCH** review item. Do not auto-correct; surface for human
review. Discovery-side application: discoverers must assign correct category at discovery time — see
Site Discovery Subproc v5.x §5b.

------------------------------------------------------------
## 7.3 Subtype Normalization Mapping (IMP-064)

Invalid subtype values (i.e., values not in the category-specific list in §3.2) must be mapped using
the table below. Values with no valid mapping → **null the subtype field** (do not reject the entity).

**Park subtypes:**

| Raw Subtype | Maps To | Notes |
|-------------|---------|-------|
| "Community Park" | "Neighborhood Park" | Direct synonym. |
| "Pocket Park" | "Neighborhood Park" | Small neighborhood-scale parks. |
| "Greenway" / "Trail Corridor" | "Linear Park" | Linear connectivity corridors. |
| "Natural Park" / "Woodland Park" / "Riparian Park" | "Greenspace" | Parks with primarily natural character. |
| "Regional Park" | null | No vocabulary equivalent; flag for subtype-level review. |
| "Metro Park" | null | Governance label, not a subtype. |

**Nature Preserve subtypes — ecological descriptor routing:**

The following raw values are ecological descriptors that belong in `description`, not `subtype`:
Bog, Fen, Forest, Old-Growth Forest, Wetland, Woodland, Riparian, Savanna, Prairie, Meadow,
Shrubland, Grassland, Successional Area, Upland, Floodplain, Ravine, Cliff.

When these appear in `subtype` for a Nature Preserve, null the `subtype` field, and if `description`
does not already contain the ecological character, append it to `description` as a brief note.

**Recreation Facility subtypes — Features terms misplaced in subtype:**

These are Features vocabulary terms and must not appear in `subtype`:
Gazebo, Pavilion, Splash Pad, Spray Park, Skate Bowl, Mountain Bike Park, Pump Track, BMX.

When found in `subtype` for a Recreation Facility, null `subtype` and ensure the corresponding
Features vocabulary term appears in `features` if the physical infrastructure is documented.
Exception: "Skate Park" (without "Bowl") is a valid Recreation Facility subtype — retain it.

**Other categories — common out-of-vocabulary values:**

| Raw Subtype | Category | Maps To | Notes |
|-------------|----------|---------|-------|
| "Lake/Wetland" | Water Site | null | Ambiguous; flag for manual resolution. |
| "Swimming Hole" | Water Site | null | No vocabulary term; flag for vocabulary expansion. |
| "Green Burial Cemetery" | Cemetery | "Green Burial Cemetery" | Valid; already in vocabulary. |
| "Living Museum" | Curated Biological Site | "Living Museum" | Valid; already in vocabulary. |

------------------------------------------------------------
## 7.4 Subtype Inference Rules (IMP-065)

Applied **after** vocabulary validation, **only when `subtype` is blank**. Inference is deterministic —
no ambiguity, no judgment. If inference rules do not unambiguously match, leave `subtype` blank.
Record inference basis in normalization provenance as `subtype_source = "name_inference"` or
`subtype_source = "description_inference"`.

### Nature Preserve
Evaluate in order; use the first match:
1. If `designation` = "State Nature Preserve" → subtype = "State Nature Preserve"
2. If `name` contains "State Nature Preserve" (case-insensitive) → subtype = "State Nature Preserve"
3. Else → subtype = "Private Nature Preserve"

### Water Site
Match against `name` (case-insensitive, whole-word or phrase):
- "River" / "Creek" / "Stream" / "Run" (e.g., "Big Walnut Creek") → "River"
- "Lake" (e.g., "Hoover Reservoir / O'Shaughnessy Reservoir") → note: see Reservoir rule
- "Reservoir" → "Reservoir"
- "Lake" (without "Reservoir") → "Lake"
- "Pond" → "Pond"
- "Harbor" → "Harbor"
- "Marina" → "Marina"
Precedence: "Reservoir" takes priority over "Lake" when both appear. No match → leave blank.

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
Match against `description` (case-insensitive; apply only first match):
- "cabin" / "lodge" → "Cabin Campground"
- "RV" / "hookup" / "electric" → "RV Campground"
- "primitive" → "Primitive Campground"
- "group" → "Group Campground"
No match → leave blank.

### Cemetery (IMP-099)
Apply in order; use the first matching rule. Evidence sources: `name`, `governance_raw`, `ownership_raw`, `designation`.

1. If `designation` includes "National Cemetery" OR `name` contains "National Cemetery" → **"Veterans Cemetery"**
2. If `name` contains "Veterans" OR "Soldiers" OR "G.A.R." (Grand Army of the Republic) → **"Veterans Cemetery"**
3. If `governance_raw` or `ownership_raw` references a church denomination, diocese, parish, or religious organization (e.g., "St. Mary's Parish", "First Baptist Church", "Catholic Diocese") → **"Church Cemetery"**
4. If `name` matches pattern "[Surname] Family Cemetery" OR contains "Family Cemetery" OR "Family Burial" → **"Family Cemetery"**
5. If `name` contains "Green Burial" OR "Natural Burial" → **"Green Burial Cemetery"**
6. If `governance_raw` or `ownership_raw` is a government entity (township, municipality, county, state, federal) → **"Public Cemetery"**
7. If none of the above match → **"Private Cemetery"**

Note: Many cemeteries are maintained by multiple entities (e.g., a township-owned cemetery maintained by a historical society). Use the ownership entity for rule 6; maintenance entity alone does not override ownership classification. Record all governance/ownership detail in `governance_raw` and `ownership_raw` — do not reduce to the subtype label.

Status guidance for cemeteries: "Active" = currently accepting burials or actively maintained; "Abandoned" = untended, no active management; "Historic" is not a vocabulary status value — use "Active" for maintained historic cemeteries or "Abandoned" for untended ones; note historical character in `description`.

------------------------------------------------------------
## 7.5 Status Normalization Mapping

"open" → "Active"
"open seasonally" → "Seasonal"
"by permit only" → "Access Permit Required"
"no trespassing" → "No Public Entry"
"under construction" → "Under Development"
"coming soon" → "Under Development"
"proposed" → "Proposed"
"permanently closed" → "Closed"

Ambiguous cases require manual review.

------------------------------------------------------------
# 8. VOCABULARY USAGE RULES

- Use values exactly as written.
- Do not infer values (except subtype per §3.1 exception and §7.4).
- Leave blank if unclear.
- Discovery captures raw values; normalization maps them.
- Flag new values for vocabulary expansion.

------------------------------------------------------------
# 9. CHANGES

## v5.5 → v5.6 (2026-05-05)

- **IMP-099 — Cemeteries and golf courses formally in scope, all instances**: Both types already existed in vocabulary (no new terms added). Added Cemetery to the §3.1 subtype inference exception list. Added §7.4 Cemetery inference rules: 7-step ordered rule set using name, governance, ownership, and designation to assign Public Cemetery / Private Cemetery / Family Cemetery / Veterans Cemetery / Church Cemetery / Green Burial Cemetery. Status guidance for cemeteries added (Active vs. Abandoned; "Historic" is not a vocabulary status).

## v5.4 → v5.5 (2026-04-07)

- **IMP-063 — Category vocabulary enforcement**: Added §7.1 full category normalization mapping table
  with FATAL REJECT rule for unmappable values. Prior §7 had only minimal case-normalization examples.
- **IMP-064 — Subtype vocabulary enforcement**: Added §7.3 subtype normalization mapping tables by
  category. Covers common out-of-vocabulary values, ecological descriptor routing for Nature Preserve,
  and Features-term detection for Recreation Facility.
- **IMP-065 — Deterministic subtype inference**: Added §7.4 with inference rules for Nature Preserve,
  Water Site, Recreation Facility, and Campground. Added §3.1 exception clause permitting name-keyword
  inference for the four named categories.
- **IMP-068 — Cultural institution name-pattern recognition**: Added §7.2 with name-pattern table
  covering Botanical Garden / Conservatory / Arboretum / Zoo / Aquarium / Aviary / Museum / Science
  Center / Hall of Fame. Specifies both discovery-side (hard assignment) and normalization-side
  (mismatch flag) application.

------------------------------------------------------------
# 9. VERSIONING

v5.4 (2026-03-31):
- Added Hiking Trail to Features (confirmed across multiple Ohio counties; gap identified during
  Scioto County quality review — vocabulary had Bridle Trail and Mountain Bike Trail but no
  general hiking trail infrastructure value).
- Added Hunting Area to Features (follows same dual-use pattern as Fishing Area, which appears
  in both Category and Features; needed for large multi-use sites where hunting is permitted
  in designated areas but the site's primary category is not Hunting Area).
- Added Mini Golf to Features (confirmed at Shawnee State Park; distinct from Golf Course).
- Added Wilderness Area to Features (confirmed at Shawnee State Forest; designated wilderness
  is a meaningful internal component of a larger forest site).

v5.3 (2026-03-23):
- Added Via Ferrata to Features (confirmed at Quarry Trails Metro Park, Columbus).

v5.3 (2026-03-22):
- Restored S&M Dungeon to Features (was incorrectly removed as "test artifact" in v5.0).
- Removed stale §6.2 header note.

v5.2 (updated 2026-03-21):
- Added 5 new Features values confirmed during Franklin County CRP data intake:
  Ball Diamond, Basketball Court, Community Center, Golf Course, Rain Garden.
- Added Spray Park to Features (IMP-039).
- Added 5 new Features values confirmed during Fulton County pipeline run (2026-04-13):
  Cabin Rentals, Farm Store, Guided Tours, Ropes Course, Vernal Pool.
- Added Defunct to Status; applies to dissolved/absorbed Tier 5 township entities (IMP-020).
- Added River subtype to Water Site; added National Wild and Scenic River to Federal Designations (IMP-019/IMP-008). "Scenic River Corridor" dropped as a Category — scenic rivers are Water Sites with subtype River and designation State Scenic River / National Wild and Scenic River.
- Water Frontage (CRP amenity term): retained in features_raw only; not mapped to features. Boundary condition, not an internal site component (IMP-038).

v5.2 (original):
- Updated integration points to v5.x.
- Updated organizational model (ownership, governance, partner_agencies, coordination).
- Clarified that partner_agencies is not a controlled vocabulary.
- No changes to vocabulary values (original release).

v5.0:
- Enhanced definitions and usage rules.
- Added normalization mappings.

------------------------------------------------------------
# 10. INTEGRATION POINTS

This vocabulary module integrates with:

- Site Schema Module v5.x
- Site Discovery Sub-Procedure v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- TSV Output Specification v5.x

------------------------------------------------------------
# END OF SITE VOCABULARY MODULE v5.6