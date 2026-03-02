# NATURAL AREAS PROJECT
# TRAIL SEGMENT VOCABULARY MODULE v5.0
(Authoritative Controlled Vocabularies for Trail Segment Fields)

This module contains all controlled vocabularies for Trail Segment entities
in the Natural Areas Project v5.0.

All Trail Segment-related modules must reference this module for vocabulary authority.

------------------------------------------------------------
# CHANGES FROM v4.0

- `segment_role` vocabulary removed (field removed from schema)
- `segment_type` vocabulary retained
- `surface_type` vocabulary retained
- `status` vocabulary retained
- `difficulty` vocabulary added (NEW field in v5.0)
- Enhanced definitions and usage guidance
- Removed categories from value lists
- Updated to v5.0 references

------------------------------------------------------------
# 1. PURPOSE

This module defines the authoritative controlled vocabularies for:
- Segment Type
- Surface Type
- Status
- Difficulty

These vocabularies are used across:
- Discovery Sub-Procedure v5.0 (raw capture)
- Resolution Engine v5.0 (conflict detection)
- Normalization Engine v5.0 (vocabulary mapping)
- TSV Output Specification v5.0 (output format)

**Key Principle:** Vocabularies are DESCRIPTIVE, not PRESCRIPTIVE.
- Values describe what authoritative sources document
- Values are not inferred from geometry or characteristics
- If no documented value matches, leave field blank

------------------------------------------------------------
# 2. SEGMENT TYPE VOCABULARY (Controlled)

## 2.1 Allowed Values

- Linear
- Loop
- Connector
- Spur
- Crossing
- Access Segment
- Other

------------------------------------------------------------
## 2.2 Definitions & Usage Rules

### Linear

**Definition:**
Segment that follows a straight or continuous path without forming a loop.

**When to use:**
- ✅ Default for most segments
- ✅ Segment continues in one direction
- ✅ Does not loop back to starting point

**When NOT to use:**
- ❌ Segment forms a loop (use Loop)
- ❌ Segment branches off main trail (use Spur)

**Discovery guidance:**
Linear is the default. Only populate segment_type when explicitly different from Linear.

**Normalization:**
- Leave blank if not specified → defaults to Linear
- "straight section" → Linear
- "continuous trail" → Linear

---

### Loop

**Definition:**
Segment that forms a closed loop returning to the starting point.

**When to use:**
- ✅ Segment forms complete loop by itself
- ✅ Loop trail section
- ✅ Circuit that returns to origin

**When NOT to use:**
- ❌ Entire trail is a loop (that's Trail characteristic, not segment)
- ❌ Segment connects to another segment to form loop (that's Linear)
- ❌ Lollipop trail (stem is Linear, loop portion is Loop)

**Discovery guidance:**
Only use when segment itself forms a loop.

**Example:**
"Nature Loop Trail" with stem access:
- Access segment (stem): Linear
- Loop portion: Loop

---

### Connector

**Definition:**
Segment that links two trails or two trail segments.

**When to use:**
- ✅ Links two different trails
- ✅ Connector between trail segments
- ✅ Explicitly documented as "connector"

**When NOT to use:**
- ❌ Access from parking to trail (use Access Segment)
- ❌ Short spur (use Spur)

**Discovery guidance:**
Must explicitly connect two trails or segments. Not for access connections.

---

### Spur

**Definition:**
Short segment that branches off main trail and does not reconnect.

**When to use:**
- ✅ Dead-end side trail
- ✅ Trail to overlook or viewpoint
- ✅ Offshoot that terminates

**When NOT to use:**
- ❌ Reconnects to main trail (that's Loop or Connector)
- ❌ Access from parking (use Access Segment)

**Discovery guidance:**
Spur trails dead-end without reconnecting.

**Example:**
"Overlook Spur" - branches off main trail to viewpoint, ends there.

---

### Crossing

**Definition:**
Segment that crosses infrastructure (road, river, etc.) via bridge, underpass, or at-grade crossing.

**When to use:**
- ✅ Bridge segment
- ✅ Underpass segment
- ✅ Road crossing explicitly mapped as segment
- ✅ River ford crossing

**When NOT to use:**
- ❌ Trail happens to cross a road (not a separate segment)
- ❌ Unless explicitly documented as distinct crossing segment

**Discovery guidance:**
Only use when crossing infrastructure is documented as a distinct segment.

**Example:**
"Maumee River Bridge Section" - documented bridge crossing as segment.

---

### Access Segment

**Definition:**
Short segment providing access from an access point to the main trail corridor.

**When to use:**
- ✅ Parking lot to trailhead connector
- ✅ Access path from road to main trail
- ✅ Short connector explicitly for access

**When NOT to use:**
- ❌ Part of main trail (use Linear)
- ❌ Spur trail (use Spur)

**Discovery guidance:**
Used for documented access connectors, not the main trail itself.

**Example:**
"Parking Access Trail" - 200 feet from parking lot to main trail.

---

### Other

**Definition:**
Named segment type from authoritative source that doesn't fit any category.

**When to use:**
- ✅ Source provides specific type name
- ✅ Doesn't match any controlled vocabulary term
- ✅ Is legitimate, documented segment type

**When NOT to use:**
- ❌ Invented types
- ❌ Inferred types

**Discovery guidance:**
Include authoritative name in notes. Flag for vocabulary expansion review.

------------------------------------------------------------
# 3. SURFACE TYPE VOCABULARY (Controlled)

## 3.1 Allowed Values

- Paved
- Crushed Stone
- Gravel
- Natural Surface
- Boardwalk
- Water
- Mixed
- Other

------------------------------------------------------------
## 3.2 Definitions & Usage Rules

### Paved

**Definition:**
Hard-surfaced trail with asphalt, concrete, or similar paved material.

**When to use:**
- ✅ Asphalt surface
- ✅ Concrete surface
- ✅ Any hard-paved surface

**Discovery guidance:**
Combine asphalt and concrete under "Paved" - don't differentiate.

**Normalization:**
- "asphalt" → Paved
- "concrete" → Paved
- "pavement" → Paved
- "blacktop" → Paved

---

### Crushed Stone

**Definition:**
Compacted crushed stone or limestone surface.

**When to use:**
- ✅ Crushed limestone
- ✅ Compacted stone dust
- ✅ Crushed gravel (fine)

**Discovery guidance:**
Use when source specifies "crushed stone" or "limestone."

**Normalization:**
- "limestone" → Crushed Stone
- "stone dust" → Crushed Stone
- "crushed gravel" → Crushed Stone or Gravel (context dependent)

---

### Gravel

**Definition:**
Loose or compacted gravel surface.

**When to use:**
- ✅ Gravel trail
- ✅ Loose stone surface
- ✅ Compacted gravel

**Normalization:**
- "stone" → Gravel (if not crushed stone)
- "rock" → Gravel

---

### Natural Surface

**Definition:**
Unimproved dirt, soil, grass, or natural tread surface.

**When to use:**
- ✅ Dirt trail
- ✅ Soil surface
- ✅ Grass trail
- ✅ Unimproved surface
- ✅ Packed earth

**Discovery guidance:**
Default for unimproved trails.

**Normalization:**
- "dirt" → Natural Surface
- "soil" → Natural Surface
- "grass" → Natural Surface
- "earth" → Natural Surface
- "turf" → Natural Surface
- "native surface" → Natural Surface

---

### Boardwalk

**Definition:**
Elevated wooden walkway or boardwalk.

**When to use:**
- ✅ Wooden boardwalk
- ✅ Elevated walkway
- ✅ Decking

**Discovery guidance:**
Clear when documented; usually for wetland crossings.

**Normalization:**
- "wooden walkway" → Boardwalk
- "deck" → Boardwalk
- "elevated walkway" → Boardwalk

---

### Water

**Definition:**
Water-based segment (paddling trail).

**When to use:**
- ✅ Paddling trail segment
- ✅ Water trail portion
- ✅ River or lake segment

**Discovery guidance:**
Only for water trails, not land trails that cross water.

---

### Mixed

**Definition:**
Segment with multiple surface types that cannot be categorized as primarily one type.

**When to use:**
- ✅ Explicitly documented as "mixed surface"
- ✅ Source states multiple surfaces for one segment
- ✅ "Paved and gravel" for same segment

**When NOT to use:**
- ❌ Different segments have different surfaces (create separate segments)
- ❌ Inferred from maps

**Discovery guidance:**
Only use when source explicitly states mixed surfaces for one segment.

**Example:**
"First mile paved, remainder gravel" - if treated as one segment, use Mixed.
Better: Create two segments (Paved segment + Gravel segment).

---

### Other

**Definition:**
Named surface type from authoritative source that doesn't fit any category.

**When to use:**
- ✅ Source provides specific surface name
- ✅ Doesn't match controlled vocabulary
- ✅ Is legitimate surface type

**Discovery guidance:**
Include authoritative term in notes. Flag for vocabulary review.

**Examples:**
- "Rubber surface"
- "Synthetic turf"
- "Recycled tire surface"

------------------------------------------------------------
# 4. STATUS VOCABULARY (Controlled)

## 4.1 Allowed Values

- Active
- Planned
- Gap
- Closed

------------------------------------------------------------
## 4.2 Definitions & Usage Rules

### Active

**Definition:**
Segment is currently open and operational.

**When to use:**
- ✅ Open to public
- ✅ Operational
- ✅ Available for use

**Discovery guidance:**
Can be left blank if obviously active. Use explicitly when differentiating from other segments with different status.

---

### Planned

**Definition:**
Segment is planned for future construction but not yet built.

**When to use:**
- ✅ Explicitly documented as planned
- ✅ Future trail extension
- ✅ Under design

**Discovery guidance:**
Must be explicitly documented as planned future segment.

---

### Gap

**Definition:**
Missing or incomplete portion of trail where segment doesn't exist.

**When to use:**
- ✅ Trail discontinuity
- ✅ Missing segment requiring road walk or detour
- ✅ Explicitly documented gap

**When NOT to use:**
- ❌ Closed segment (use Closed)
- ❌ Planned segment (use Planned)

**Discovery guidance:**
"Gap" is specific to trail segments - represents missing trail continuity.

**Example:**
"Buckeye Trail Mile 24-32 is a gap requiring road walk"
- segment_name: "Gap - Mile 24-32"
- status: Gap

---

### Closed

**Definition:**
Segment is closed to public use.

**When to use:**
- ✅ Explicitly closed
- ✅ Decommissioned segment
- ✅ Permanently closed

**When NOT to use:**
- ❌ Temporary closures (use notes field)
- ❌ Seasonal closures (use notes field)

**Discovery guidance:**
Must be explicitly documented as closed.

------------------------------------------------------------
# 5. DIFFICULTY VOCABULARY (Controlled) ✨ NEW IN v5.0

## 5.1 Allowed Values

- Easy
- Moderate
- Difficult
- Strenuous
- Expert

------------------------------------------------------------
## 5.2 Definitions & Usage Rules

### Easy

**Definition:**
Suitable for beginners, minimal elevation change, good surface.

**When to use:**
- ✅ Source explicitly rates as "Easy"
- ✅ Beginner-friendly designation

**When NOT to use:**
- ❌ Looks easy to you (don't assess yourself)
- ❌ Paved trail (don't infer from surface)

**CRITICAL:** Only use when authoritative source explicitly states difficulty.

---

### Moderate

**Definition:**
Some elevation change, moderate obstacles, average fitness required.

**When to use:**
- ✅ Source explicitly rates as "Moderate"

**CRITICAL:** Only use when authoritative source explicitly states difficulty.

---

### Difficult

**Definition:**
Significant elevation, rough terrain, good fitness required.

**When to use:**
- ✅ Source explicitly rates as "Difficult"

**CRITICAL:** Only use when authoritative source explicitly states difficulty.

---

### Strenuous

**Definition:**
Very challenging, steep climbs, excellent fitness required.

**When to use:**
- ✅ Source explicitly rates as "Strenuous"

**CRITICAL:** Only use when authoritative source explicitly states difficulty.

---

### Expert

**Definition:**
Extremely challenging, technical skills required.

**When to use:**
- ✅ Source explicitly rates as "Expert"

**CRITICAL:** Only use when authoritative source explicitly states difficulty.

---

## 5.3 CRITICAL USAGE RULES FOR DIFFICULTY

**DO:**
- ✅ Record ONLY what authoritative sources explicitly state
- ✅ Leave blank if not documented
- ✅ Use exact terminology from source

**DON'T:**
- ❌ Assess difficulty yourself
- ❌ Infer from terrain or surface
- ❌ Guess based on segment characteristics
- ❌ Use personal judgment

**Normalization:**
- "beginner" → Easy
- "advanced" → Difficult
- "challenging" → Difficult (context dependent)
- "technical" → Expert (context dependent)

**Segment-specific note:**
Difficulty can vary by segment even if parent trail has overall rating.

**Example:**
"Slippery Elm Trail" overall: Easy
"Segment 3 (Hill Section)": Moderate (if explicitly documented)

------------------------------------------------------------
# 6. VOCABULARY NORMALIZATION RULES

## 6.1 Common Mappings

**Segment Type:**
```
Raw Value               → Normalized Value
-----------------         ------------------
"loop trail"            → Loop
"connector trail"       → Connector
"spur trail"            → Spur
"access trail"          → Access Segment
```

**Surface Type:**
```
Raw Value               → Normalized Value
-----------------         ------------------
"asphalt"               → Paved
"concrete"              → Paved
"pavement"              → Paved
"dirt"                  → Natural Surface
"soil"                  → Natural Surface
"grass"                 → Natural Surface
"limestone"             → Crushed Stone
"stone dust"            → Crushed Stone
"wooden walkway"        → Boardwalk
```

**Status:**
```
Raw Value               → Normalized Value
-----------------         ------------------
"open"                  → Active
"operational"           → Active
"future trail"          → Planned
"trail gap"             → Gap
"permanently closed"    → Closed
```

**Difficulty:**
```
Raw Value               → Normalized Value
-----------------         ------------------
"beginner"              → Easy
"easy/moderate"         → Moderate
"advanced"              → Difficult
"very difficult"        → Strenuous
"technical"             → Expert
```

------------------------------------------------------------
# 7. VOCABULARY USAGE RULES

## 7.1 Universal Rules

1. **Use exactly as written** - No synonyms or invented terms
2. **Don't infer** - Values must be documented
3. **Leave blank if unclear** - Better no value than wrong value
4. **One value per field** - No multi-value entries
5. **Flag new values** - Don't add values; flag for review

## 7.2 Discovery Phase

- Capture raw values exactly as found
- Don't normalize during discovery
- Record variations in *_raw fields

## 7.3 Normalization Phase

- Map raw values to controlled vocabulary
- Handle common variations
- Flag unrecognized values
- Validate against vocabulary list

## 7.4 Segment-Specific Notes

**Difficulty and Accessibility:**
- Can differ from parent Trail
- Only populate if segment-specific documentation exists
- Don't inherit from parent Trail unless explicitly stated

**Surface Type:**
- Often the PRIMARY reason segments exist
- Different surface = different segment
- Be precise with surface documentation

**Status:**
- "Gap" is segment-specific vocabulary term
- Represents missing trail continuity
- Important for long-distance trail documentation

------------------------------------------------------------
# 6b. ACCESSIBILITY (Free-Text — No Controlled Vocabulary) ✨ NEW IN v5.0

## 6b.1 Overview

**Accessibility is a free-text field — there is no controlled vocabulary.**

Record the accessibility description exactly as documented by the authoritative source.

## 6b.2 What to Collect

- ADA compliance statements specific to this segment
- Wheelchair accessibility descriptions
- Surface grade and width information for this segment
- Accessible facility descriptions at segment endpoints or along the segment

**Examples of valid accessibility descriptions:**
- "ADA accessible; paved surface, grades under 5%"
- "Wheelchair accessible for entire length"
- "Not ADA compliant; natural surface with variable grades"
- "Accessible viewing platform at mile 1.2"

## 6b.3 What NOT to Collect

- ❌ Inferred accessibility from surface type alone
- ❌ Personal assessments of accessibility
- ❌ Parent trail's accessibility description (unless segment-specific documentation confirms it applies)

## 6b.4 Segment-Specific Rule

**Do not inherit accessibility from the parent Trail unless explicitly stated.**

- Parent trail may be documented as accessible while this segment is not
- Only populate if segment-specific accessibility documentation exists
- Leave blank if no segment-specific information found

## 6b.5 Discovery Guidance

- Record raw accessibility description exactly as found
- Don't rephrase or standardize
- Leave blank if no accessibility information documented for this specific segment

## 6b.6 Normalization Guidance

- Preserve free-text as-is
- No vocabulary mapping needed
- Clean obvious formatting issues only

------------------------------------------------------------
# 8. INTEGRATION POINTS

This vocabulary module integrates with:

- **Trail Segment Schema Module v5.0** (field definitions)
- **Trail Segment Discovery Sub-Procedure v5.0** (raw capture)
- **Resolution Engine v5.0** (identity matching)
- **Normalization Engine v5.0** (vocabulary mapping)
- **TSV Output Specification v5.0** (output format)

------------------------------------------------------------
# END OF TRAIL SEGMENT VOCABULARY MODULE v5.0
