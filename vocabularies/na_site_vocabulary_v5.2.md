# NATURAL AREAS PROJECT
# SITE VOCABULARY MODULE v5.2
(Authoritative Controlled Vocabularies for Site Entities)

This module contains all controlled vocabularies for Site entities in the
Natural Areas Project v5.2 architecture.

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
- Leave blank if unclear.

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
- Campus Open Space

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
- Mausoleum Grounds

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
National Heritage Area  
National Battlefield  
National Cemetery  
National Register of Historic Places (NRHP)

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

Definitions and usage rules remain unchanged.

------------------------------------------------------------
# 6. FEATURES (Controlled)

## 6.1 Rules

- Features represent internal components of a Site.
- Must not include Trails, Trail Segments, Access Points, or child Sites.
- Semicolon-delimited list.
- Must be documented in authoritative sources.

## 6.2 Allowed Values

(Full list preserved exactly as in v5.0 — unchanged in v5.2.)

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

Category mappings:
"nature preserve" → "Nature Preserve"  
"wildlife management area" → "Wildlife Area"  
"open space" → "Open Space"  
"recreation area" → "Park" or "Recreation Facility"  
"historic landmark" → "Historic Site"  

Status mappings:
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
- Do not infer values.
- Leave blank if unclear.
- Discovery captures raw values; normalization maps them.
- Flag new values for vocabulary expansion.

------------------------------------------------------------
# 9. VERSIONING

v5.2:
- Updated integration points to v5.x.
- Updated organizational model (ownership, governance, partner_agencies, coordination).
- Clarified that partner_agencies is not a controlled vocabulary.
- No changes to vocabulary values.

v5.0:
- Enhanced definitions and usage rules.
- Added normalization mappings.
- Removed test artifact from Features list.

------------------------------------------------------------
# 10. INTEGRATION POINTS

This vocabulary module integrates with:

- Site Schema Module v5.x
- Site Discovery Sub-Procedure v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- TSV Output Specification v5.x

------------------------------------------------------------
# END OF SITE VOCABULARY MODULE v5.2