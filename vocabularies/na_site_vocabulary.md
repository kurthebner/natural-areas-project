# NATURAL AREAS PROJECT — SITE VOCABULARY MODULE v1
Authoritative, versioned, single‑source‑of‑truth controlled vocabularies for all Site‑level fields in the statewide Natural Areas & Trails system.

This module contains:
- All controlled vocabularies used in the 25‑field Site Schema
- Rules for each vocabulary
- No definitions
- No schema logic
- No normalization logic

All other modules must reference this module for vocabulary authority.

---

# 1. CATEGORY VOCABULARY (Controlled)

## Allowed Values
Arboretum  
Botanical Garden  
Buffer Zone  
Camp  
Cemetery  
Community Garden  
Conservation Area  
Cultural Facility  
Dam  
Fishing Area  
Floodplain Area  
Greenspace  
Greenway Corridor  
Historic Site  
Hunting Area  
Internal Feature  
Memorial  
Museum  
Natural Area  
Nature Preserve  
Open Space  
Park  
Recreation Facility  
Reservoir  
Scenic Overlook  
Trail Access Point  
Trail Corridor  
Trail  
Water Access Site  
Water Site  
Wildlife Area  

## Rules
- Category expresses the ontological identity of the site.  
- Use only approved values.  
- Do not infer Category.  
- Category must not describe temporary conditions.  
- Category must not encode governance or ownership.  
- Category determines whether Subtype is allowed.

---

# 2. SUBTYPE VOCABULARY (Controlled, Category‑Dependent)

Subtype is optional.  
Subtype must match the Category‑specific lists below.

---

## A. Subtypes for Category = Park
Sports Complex  
Athletic Field  
Playground  
Dog Park  
Skate Park  
Special Use Park  
Recreational Park  
Linear Park  

### Rules
- Use only when the subtype expresses a stable identity.  
- Do not use for amenities or features.

---

## B. Subtypes for Conservation Area / Natural Area / Nature Preserve
Prairie  
Fen  
Wetland  
Bog  
Marsh  
Swamp  
Riparian Corridor  
Gorge  
Ravine  
Bluff  
Karst Area  
Sand Barrens  
Old‑Growth Forest  
Prairie Remnant  
Wetland Complex  
Mitigation Bank  
Savanna  
Grassland  

### Rules
- Subtype must represent an identity‑bearing landform or ecological unit.  
- Do not use habitat conditions (e.g., “Upland Forest,” “Meadow”).  
- Do not use governance terms (e.g., “Wildlife Area”).  
- Do not use restoration terms (e.g., “Restoration Area”).

---

## C. Subtypes for Category = Trail / Trail Corridor
Multi‑Use Trail  
Nature Trail  
Hiking Trail  
Connector Trail  
Access Segment  
Rail Trail  
Greenway Trail  
Water Trail  
Equestrian Trail  
Mountain Bike Trail  
Fitness Trail  
Canal Corridor  

### Rules
- Subtype must describe the identity of the trail, not its condition.  
- Do not use for unnamed internal paths.

---

## D. Subtypes for Category = Trail Access Point
Neighborhood Access  
Roadside Access  
Parking‑Lot Access  
Park Access  
Connector Access  

### Rules
- Subtype must describe the access context.  
- Do not use for internal features.

---

## E. Subtypes for Category = Cemetery
Historic Cemetery  
Active Cemetery  
Inactive Cemetery  
Pioneer Cemetery  
Family Cemetery  

### Rules
- Use only when explicitly stated in authoritative sources.

---

## F. Subtypes for Category = Historic Site
Archaeological Site  
Covered Bridge  
Historic Structure  
Historic District Fragment  
Cultural Landscape  
Industrial Heritage Site  
Transportation Heritage Site  
Military Site  

### Rules
- Subtype must reflect a recognized historic identity.

---

## G. Subtypes for Category = Recreation Facility
Recreation Center  
Senior Center  
Athletic Complex  
Aquatic Center  
Community Center  
Indoor Sports Facility  

### Rules
- Subtype must reflect a stable facility identity.

---

## H. Subtypes for Category = Internal Feature
Dog Park (Internal)  
Skate Area (Internal)  
BMX Track (Internal)  
Playground (Internal)  
Trail Segment (Internal)  
Garden (Internal)  
Memorial (Internal)  

### Rules
- Internal Feature subtypes apply only when Category = Internal Feature.

---

# 3. DESIGNATION VOCABULARY (Controlled)

## A. Federal Designations
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

## B. State Designations
State Park  
State Nature Preserve  
State Fishing Area  
State Hunting Area  
State Memorial  
State Wildlife Area  
State Forest  
State Scenic River  
State Natural Landmark  
State Archaeological Preserve  
State Historic Site  
State Recreation Area  

## C. Local / Special Designations
County Nature Preserve  
County Historic Landmark  
Municipal Historic Landmark  
Local Landmark  
Local Historic District  
Certified Arboretum (Level I–IV)  
Registered Cemetery  
Protected Wetland  
Mitigation Bank  
Conservation Easement  
Land Trust Preserve  

## D. Blank
Most sites have no designation.

### Rules
- Use only when explicitly stated in authoritative sources.  
- Do not infer designation.  
- Do not combine multiple designations unless explicitly documented.

---

# 4. STATUS VOCABULARY (Controlled)

Active  
Seasonal  
Access Permit Required  
No Public Entry  
Under Development  
Proposed  
Abandoned  
Closed  

### Rules
- “Closed” = permanently closed as the entity described.  
- “Proposed” must be officially referenced.  
- Do not infer status from imagery alone.

---

# 5. TRAIL ROLE VOCABULARY (Controlled)

Trail System  
Trail Segment  
Trail  
Connector Trail / Spur  
Trailhead  
Trail Access Point  
Bikeway Access Point  
Bikeway Spur  
Greenway Corridor  
Other  
None  

### Rules
- Trail Role must reflect the site’s relationship to a trail network.  
- Use “None” when the site has no trail identity.

---

# 6. TRAIL SEGMENT TYPE VOCABULARY (Controlled)

Connector  
Crossing  
Loop  
Linear  
Access Segment  
None  

### Rules
- Use only for sites with Trail Role = Trail Segment.  
- Use “None” when not applicable.

---

# 7. TRAIL ACCESS TYPE VOCABULARY (Controlled)

Trailhead  
Access Point  
Connector  
Crossing  
None  

### Rules
- Use only when the site functions as a trail access location.  
- Use “None” when not applicable.

---

# 8. FEATURES VOCABULARY (Controlled)

Arboretum  
Accessibility Features  
ADA Accessible  
AED  
Amphibian Area  
Amphitheater  
Archery Range  
Art Gallery  
Athletic Fields  
Ballroom  
Bandstand  
Baseball Field  
Basketball Court  
Beach  
Bike Rack  
Bike Repair Station  
Bird Viewing Area  
Boardwalk  
Bridle Trail  
Butterfly or Pollinator Garden  
Camping  
Cave or Cavern  
Climbing Wall  
Community Garden  
Conservatory  
Covered Bridge  
Covered Shelter  
Cricket Pitch  
Dance Floor  
Dance Performance Space  
Disc Golf Course  
Dog Park  
Electric Vehicle Charging  
Equestrian Arena  
Fieldhouse  
Fishing Area  
Football Field  
Football Stadium  
Gaming Area  
Garden  
Gazebo  
Handball Court  
Historic Marker  
Historic Structure  
Horseshoe Pitch  
Hunting Area  
Ice Rink  
Interpretive Signage  
Kite Flying  
Lacrosse Field  
Marina  
Model Airplane Field  
Model Rocketry Field  
Mountain Bike Trail  
Multi-use Trail  
Musical Instruments  
Musical Performance Space  
Native American Artifacts  
Native American Cultural Site  
Native American Earthworks  
Natural Arch  
Observation Deck  
Observatory  
Outdoor Art Installation  
Parking Area  
Paved Path  
Pavilion  
Pickleball Court  
Picnic Area  
Pioneer Historic Site  
Pioneer Re-creation  
Pistol Range  
Planetarium  
Playground  
Prairie Restoration  
Pump Track  
Restrooms  
S&M Dungeon  
Scenic View / Overlook  
Shooting Range  
Shotgun Range  
Skate Park  
Ski Slopes  
Sledding Hill  
Soccer Pitch  
Swimming Pool  
Tennis Court  
Theatre  
Trapping Area  
Trolley  
Tropical Garden  
Unpaved Trail  
Volleyball Court  
Water Park  
Watercraft Access  
Waterfall  
Waterslide  
Wetland Restoration  
Wildlife Observation Area  
Working Railway  
Zoo  

### Rules
- Features describe internal components, not identity‑bearing land units.  
- Use only approved values.  
- No site-defining ecology. Soome ecological terms (listed above) are acceptable when they are simply features of the site, such as a park with a Natural Arch.  
- No governance.  
- No temporary conditions.  
- Named trails are never Features.  
- Unnamed trails use the trail‑related Feature terms.  
- Minor connectors belong in Notes, not Features.

---

# END OF SITE VOCABULARY MODULE v1