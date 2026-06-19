# NATURAL AREAS PROJECT
# SITE VOCABULARY MODULE v5.0
(Authoritative Controlled Vocabularies for Site Entities)

This module contains all controlled vocabularies for Site entities
in the Natural Areas Project v5.0.

All Site-related modules must reference this module for vocabulary authority.

------------------------------------------------------------
# CHANGES FROM v4.0

- No vocabulary value changes — all existing values preserved
- Updated to v5.0 references
- Enhanced definitions and usage rules for Category and Subtype
- Added normalization mappings
- Added discovery vs. normalization guidance per v5.0 philosophy
- Removed test artifact from Features list

------------------------------------------------------------
# 1. PURPOSE

This module defines the authoritative controlled vocabularies for:
- Category
- Subtype (Category-dependent)
- Designation
- Status
- Features

**Not controlled vocabularies** (rule-governed free-text fields):
- Ownership
- Governance
- Partner Agencies

These vocabularies are used across:
- Site Discovery Sub-Procedure v5.0 (raw capture)
- Resolution Engine v5.0 (conflict detection)
- Normalization Engine v5.0 (vocabulary mapping)
- TSV Output Specification v5.0 (output format)

**Key Principle:** Vocabularies are DESCRIPTIVE, not PRESCRIPTIVE.
- Values describe what authoritative sources document
- Values are not inferred from features, amenities, or context
- If no documented value matches, leave field blank

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
## 2.2 Rules & Clarifications

- Describes the **primary identity-bearing classification** of the Site.
- Must not encode governance, ownership, designation, or temporary conditions.
- Must be supported by authoritative source documentation.
- One value only — choose the most specific category that applies.
- Leave blank if no category is clearly documentable.

**Key distinctions:**

- **Park** vs. **Natural Area**: Park implies managed recreational infrastructure; Natural Area implies ecological character is primary.
- **Nature Preserve** vs. **Natural Area**: Nature Preserve has a formal preservation designation or legal protection. Natural Area may not.
- **Conservation Area** vs. **Natural Area**: Conservation Area implies active management for conservation outcomes. Natural Area describes ecological character.
- **Wildlife Area** vs. **Natural Area**: Wildlife Area is managed specifically for wildlife — hunting, wildlife observation, habitat. Natural Area is ecologically characterized but not necessarily wildlife-managed.
- **Recreation Facility** vs. **Park**: Recreation Facility is primarily a built recreational infrastructure (sports complex, pool, ice rink). Park has broader character.
- **Open Space** vs. **Park**: Open Space has minimal infrastructure and is not formally developed as a park.
- **Historic Site** vs. **Memorial**: Historic Site has a place-based historic identity. Memorial is primarily commemorative.
- **Museum** vs. **Cultural Facility**: Museum has collections-based identity. Cultural Facility provides programming or performance.

**Normalization guidance:**
```
Raw Value                    → Normalized Value
----------                     ----------------
"nature preserve"            → "Nature Preserve"
"wildlife management area"   → "Wildlife Area"
"open space preserve"        → "Open Space" or "Conservation Area" (check source)
"recreation area"            → "Park" or "Recreation Facility" (check context)
"greenway"                   → "Park" or "Open Space" (check context)
"historic landmark"          → "Historic Site"
"memorial park"              → "Memorial" or "Park" (check primary identity)
```

------------------------------------------------------------
# 3. SUBTYPE (Controlled, Category-Dependent)

## 3.1 Rules

- A Site may have **zero or one** Subtype.
- Subtypes must belong to the list for the Site's Category.
- Must not be inferred from features, amenities, or geography.
- Leave blank if no subtype is clearly documentable.
- Do not apply a subtype from a different Category.

------------------------------------------------------------
## 3.2 Subtype Lists by Category

### A. Park
- Greenspace
- Neighborhood Park
- Linear Park
- Dog Park
- Playground Park
- Sports Park
- Waterfront Park
- Civic Park
- Historic Park

**Guidance:**
- "Linear Park" applies to parks with a corridor identity (along a river, rail trail, etc.)
- "Historic Park" applies when historic character is the primary identity of the park
- "Civic Park" applies to formally designated civic/public squares and plazas

---

### B. Natural Area
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

**Guidance:**
- Use the most specific subtype supported by authoritative documentation
- "Wetland" is the general fallback when type is undocumented
- "Old Field" and "Successional Area" describe sites in ecological transition

---

### C. Nature Preserve
- State Nature Preserve
- Private Nature Preserve

**Guidance:**
- "State Nature Preserve" requires formal ODNR (or equivalent) designation
- "Private Nature Preserve" applies to land trust or privately held preserves with formal preservation status

---

### D. Wildlife Area
- State Wildlife Area
- Federal Wildlife Area
- Waterfowl Area
- Migratory Bird Area
- Wetland Management Area

---

### E. Conservation Area
- Restoration Area
- Habitat Management Area
- Resource Protection Area
- Watershed Protection Area
- Forest Management Area

---

### F. Open Space
- Urban Open Space
- Suburban Open Space
- Greenbelt
- Commons
- Civic Lawn
- Boulevard Median
- Campus Open Space

---

### G. Recreation Facility
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

---

### H. Cultural Facility
- Cultural Center
- Performing Arts Center
- Interpretive Center
- Heritage Center
- Art Center
- Visitor Center

---

### I. Historic Site
- Historic Landmark
- Archaeological Site
- Historic Landscape
- Battlefield
- Historic Structure

---

### J. Cemetery
- Public Cemetery
- Private Cemetery
- Family Cemetery
- Veterans Cemetery
- Church Cemetery
- Green Burial Cemetery
- Mausoleum Grounds

---

### K. Memorial
- War Memorial
- Veterans Memorial
- Civic Memorial
- Monument
- Memorial Garden
- Memorial Plaza

---

### L. Community Garden
*(No subtypes)*

---

### M. Campground
- Tent Campground
- RV Campground
- Primitive Campground
- Group Campground
- Cabin Campground

---

### N. Water Site
- Lake
- Pond
- Reservoir
- Harbor
- Marina
- Boat Launch Area
- Fishing Lake
- Retention Pond

---

### O. Curated Biological Site
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

---

### P. Museum
- History Museum
- Art Museum
- Science Museum
- Children's Museum
- Natural History Museum
- Cultural Museum

---

### Q. Hunting Area
*(No subtypes)*

---

### R. Fishing Area
*(No subtypes)*

------------------------------------------------------------
# 4. DESIGNATION (Controlled)

## 4.1 Rules

- Describes **formal legal or administrative status** conferred by a designating authority.
- Must not encode ownership, governance, or temporary conditions.
- Must be explicitly documented — not inferred from site character.
- A site may have multiple designations (semicolon-delimited).
- Leave blank if no formal designation is documented.

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
- National Heritage Area
- National Battlefield
- National Cemetery
- National Register of Historic Places (NRHP)

---

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

---

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

---

## 4.5 None

- None

**Use "None" only when:** Source explicitly confirms no formal designation exists.
**Leave blank when:** Designation status is unknown or undocumented.

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

------------------------------------------------------------
## 5.2 Definitions & Usage Rules

### Active

**Definition:**
Site is currently open and operational for its primary use.

**When to use:**
- ✅ Explicitly documented as open/active
- ✅ Default when no restrictions documented

**Discovery guidance:**
Can be left blank if obviously active.

---

### Seasonal

**Definition:**
Site is open only during documented seasons or date ranges.

**When to use:**
- ✅ Source explicitly documents seasonal operation
- ✅ "Open May through October" or similar

**Discovery guidance:**
Include season details in notes field.

---

### Access Permit Required

**Definition:**
Public access is available but requires a permit, reservation, or fee.

**When to use:**
- ✅ Permit or reservation system documented
- ✅ Fee-based access explicitly documented

**When NOT to use:**
- ❌ General park entrance fees (those are notes, not status)
- ❌ Assumed from site type

---

### No Public Entry

**Definition:**
Site exists but is not open to general public access.

**When to use:**
- ✅ Explicitly documented as no public access
- ✅ Staff or research access only
- ✅ Private land without public access

**When NOT to use:**
- ❌ Inferred from remoteness or lack of web presence

---

### Under Development

**Definition:**
Site is actively being developed or constructed; not yet open.

**When to use:**
- ✅ Source explicitly documents under development or under construction
- ✅ Opening anticipated but not yet occurred

---

### Proposed

**Definition:**
Site is documented as proposed but acquisition or development has not begun.

**When to use:**
- ✅ Explicitly documented as proposed or planned
- ✅ Appears in planning documents without confirmed acquisition

---

### Abandoned

**Definition:**
Site has been vacated or fallen into disuse but not formally closed.

**When to use:**
- ✅ Source explicitly documents as abandoned
- ✅ Site shows documented evidence of abandonment

**When NOT to use:**
- ❌ Inferred from appearance or lack of maintenance
- ❌ Temporary closure

---

### Closed

**Definition:**
Site is permanently or indefinitely closed to public use.

**When to use:**
- ✅ Explicitly documented as permanently closed
- ✅ Decommissioned site

**When NOT to use:**
- ❌ Temporary closures (use notes)
- ❌ Seasonal closures (use Seasonal)

------------------------------------------------------------
# 6. FEATURES (Controlled)

## 6.1 Rules

- Features represent **internal components** of a Site.
- Must not include Trails, Trail Segments, Access Points, or child Sites.
- Semicolon-delimited list.
- Must be documented by authoritative sources — not inferred from site type.
- Do not duplicate child entities as features.

------------------------------------------------------------
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
Ballroom
Bandstand
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
Canal Structure
Cave or Cavern
Cemetery Section
Chapel
Cliff
Climbing Structure
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
Gorge
Greenhouse
Grill
Habitat Restoration Area
Handball Court
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
Ravine
Reforestation Area
Reptile House
Research Plot
Restrooms
Retaining Wall
Retention Basin
Ridge
Rock Outcrop
S&M Dungeon
Scenic View
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
Wild Animal Rehabilitation
Wildlife Observation Area
Working Railway
Zoo

------------------------------------------------------------
# 7. VOCABULARY NORMALIZATION RULES

## 7.1 Category Common Mappings

```
Raw Value                    → Normalized Value
----------                     ----------------
"nature preserve"            → "Nature Preserve"
"wildlife management area"   → "Wildlife Area"
"wildlife area"              → "Wildlife Area"
"open space"                 → "Open Space"
"recreation area"            → "Park" or "Recreation Facility"
"historic landmark"          → "Historic Site"
"arboretum"                  → "Curated Biological Site"
"botanical garden"           → "Curated Biological Site"
"fish hatchery"              → "Fishing Area" or "Conservation Area"
"hunting ground"             → "Hunting Area"
```

## 7.2 Status Common Mappings

```
Raw Value                    → Normalized Value
----------                     ----------------
"open"                       → "Active"
"operational"                → "Active"
"open seasonally"            → "Seasonal"
"by permit only"             → "Access Permit Required"
"reservation required"       → "Access Permit Required"
"no trespassing"             → "No Public Entry"
"private"                    → "No Public Entry"
"under construction"         → "Under Development"
"coming soon"                → "Under Development"
"proposed"                   → "Proposed"
"permanently closed"         → "Closed"
"decommissioned"             → "Closed"
```

## 7.3 Ambiguous Cases

**Require context or manual review:**
- "recreation area" — could be Park or Recreation Facility depending on infrastructure
- "greenway" — could be Park, Open Space, or even a Trail entity
- "memorial park" — could be Memorial or Park depending on primary identity
- "preserve" — could be Nature Preserve, Conservation Area, or Land Trust Preserve (Designation)
- "closed" — could be permanent or temporary

------------------------------------------------------------
# 8. VOCABULARY USAGE RULES

## 8.1 Universal Rules

1. **Use exactly as written** — No synonyms, abbreviations, or invented terms
2. **Don't infer** — Values must be documented, not inferred from site character
3. **Leave blank if unclear** — Better to have no value than wrong value
4. **Category = one value; Features = semicolon-delimited list**
5. **Flag new values** — Don't add values; flag for vocabulary expansion

## 8.2 Discovery Phase

- Capture raw values exactly as found
- Don't attempt normalization during discovery
- Record raw category/subtype/status in *_raw fields

## 8.3 Normalization Phase

- Map raw values to controlled vocabulary
- Handle common variations (see Section 7)
- Flag unrecognized values for review
- Validate against vocabulary list

------------------------------------------------------------
# 9. VOCABULARY VERSIONING

## 9.1 Version History

**v5.0:**
- No vocabulary value changes
- Enhanced definitions and usage rules for Category and Subtype
- Added normalization mappings and ambiguous case guidance
- Removed test artifact from Features list
- Updated to v5.0 references

**v4.0:**
- Initial controlled vocabulary
- Category, Subtype, Designation, Status, Features defined

------------------------------------------------------------
# 10. INTEGRATION POINTS

This vocabulary module integrates with:

- **Site Schema Module v5.0** (field definitions)
- **Site Discovery Sub-Procedure v5.0** (raw capture)
- **Resolution Engine v5.0** (conflict detection)
- **Normalization Engine v5.0** (vocabulary mapping)
- **TSV Output Specification v5.0** (output format)

------------------------------------------------------------
# END OF SITE VOCABULARY MODULE v5.0
