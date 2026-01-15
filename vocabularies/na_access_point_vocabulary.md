# NATURAL AREAS PROJECT — ACCESS POINT VOCABULARY MODULE v1
Authoritative, versioned, single‑source‑of‑truth controlled vocabularies for all Access Point–level fields in the statewide Natural Areas & Trails system.

This module contains:
- All controlled vocabularies used in the 10‑field Access Point Schema
- Rules for each controlled vocabulary only
- No definitions
- No rules for fields without controlled vocabularies
- No schema logic
- No normalization logic

All Access Point–related modules must reference this module for vocabulary authority.

---

# 1. ACCESS POINT TYPE VOCABULARY (Controlled)

## Allowed Values
Trailhead  
Parking Area  
Boat Ramp  
Watercraft Access Point  
Fishing Access  
River Access  
Bicycle Access  
Snowmobile Access  
Cross Country Ski Access  
Equestrian Access  
Roadside Pull-Off  
Pedestrian Entrance  
Vehicle Entrance  
Administrative Access (restricted)  
Other (explicitly named only)

## Rules
- Access Point Type must match one of the approved values exactly.  
- “Other” may be used only when explicitly named in authoritative sources.  
- Do not infer type from amenities or internal features.  
- Access Point Type must describe a visitor‑facing navigational entry node.  
- Must not describe internal features or amenities.

---

# 2. ACCESS POINT STATUS VOCABULARY (Controlled)

## Allowed Values
Active  
Closed  
Seasonal  
Restricted  

## Rules
- Status must reflect authoritative information.  
- “Restricted” applies only when explicitly stated.  
- Leave blank if status is ambiguous or unverifiable.  
- Status must describe the access point itself, not the parent site.

---

# END OF ACCESS POINT VOCABULARY MODULE v1