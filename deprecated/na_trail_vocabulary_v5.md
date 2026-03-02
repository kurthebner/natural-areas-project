# NATURAL AREAS PROJECT
# TRAIL VOCABULARY MODULE v5.0
(Authoritative Controlled Vocabularies for Trail Fields)

This module contains all controlled vocabularies for Trail entities
in the Natural Areas Project v5.0.

All Trail-related modules must reference this module for vocabulary authority.

------------------------------------------------------------
# CHANGES FROM v4.0

- **Difficulty vocabulary added** ✨ NEW — record only from authoritative sources
- **Accessibility field added** ✨ NEW — free-text, no controlled vocabulary
- Updated to v5.0 references
- Enhanced definitions, usage rules, and normalization mappings
- Added discovery vs. normalization guidance per v5.0 philosophy

------------------------------------------------------------
# 1. PURPOSE

This module defines the authoritative controlled vocabularies for:
- Trail Use Type
- Trail Surface Type
- Trail Origin Type
- Trail Status
- Difficulty ✨ NEW IN v5.0
- Accessibility ✨ NEW IN v5.0 (free-text, no controlled vocabulary)

These vocabularies are used across:
- Trail Discovery Sub-Procedure v5.0 (raw capture)
- Resolution Engine v5.0 (conflict detection)
- Normalization Engine v5.0 (vocabulary mapping)
- TSV Output Specification v5.0 (output format)

**Key Principle:** Vocabularies are DESCRIPTIVE, not PRESCRIPTIVE.
- Values describe what authoritative sources document
- Values are not inferred from geometry, amenities, or context
- If no documented value matches, leave field blank

------------------------------------------------------------
# 2. TRAIL USE TYPE VOCABULARY (Controlled)

## 2.1 Allowed Values

- Multi-Use
- Hiking
- Bridle
- Water
- Bicycling
- Mountain Bike
- BMX
- Pump Track
- Snowmobile
- Cross Country Ski
- Other

------------------------------------------------------------
## 2.2 Definitions & Usage Rules

### Multi-Use

**Definition:**
Trail explicitly documented as serving multiple user types.

**When to use:**
- ✅ Source explicitly states "multi-use" or "multi-purpose"
- ✅ Managing agency documents multiple permitted uses

**When NOT to use:**
- ❌ You observe that multiple uses seem possible
- ❌ Trail allows bikes AND hikers but isn't labeled multi-use (pick primary use)

**Normalization:**
- "multi-purpose", "multipurpose" → "Multi-Use"
- "shared use" → "Multi-Use"

---

### Hiking

**Definition:**
Trail primarily intended for foot travel.

**When to use:**
- ✅ Source explicitly documents as hiking trail
- ✅ Foot traffic is the documented primary use

**When NOT to use:**
- ❌ Any trail you can hike on (must be documented primary use)

**Normalization:**
- "walking trail", "pedestrian trail", "footpath" → "Hiking"
- "nature trail" → "Hiking"

---

### Bridle

**Definition:**
Trail primarily intended for equestrian use.

**When to use:**
- ✅ Source explicitly documents as bridle trail or equestrian trail
- ✅ Horse/equestrian use is documented primary use

**Normalization:**
- "equestrian trail", "horse trail" → "Bridle"

---

### Water

**Definition:**
Water trail — a defined route on a waterway.

**When to use:**
- ✅ Trail is a documented water route (river, lake, reservoir)
- ✅ Source documents as "water trail" or "paddling trail"

**When NOT to use:**
- ❌ Trail that passes near water
- ❌ Trail with water crossings

**Normalization:**
- "paddling trail", "canoe trail", "kayak trail" → "Water"
- "blueway" → "Water"

---

### Bicycling

**Definition:**
Trail primarily intended for general bicycle use on paved or hard-surface trails.

**When to use:**
- ✅ Source explicitly documents as bicycle trail or bike path
- ✅ Paved or hard-surface trail with bicycle as primary use

**When NOT to use:**
- ❌ Mountain bike specific trails (use Mountain Bike)
- ❌ Multi-use trail that allows bikes (use Multi-Use or primary use)

**Normalization:**
- "bike path", "bicycle path", "bike trail", "cycle path" → "Bicycling"

---

### Mountain Bike

**Definition:**
Trail specifically designed or designated for mountain biking — typically singletrack or natural-surface.

**When to use:**
- ✅ Source explicitly designates as MTB or mountain bike trail
- ✅ Natural-surface singletrack documented as MTB

**When NOT to use:**
- ❌ Paved bike paths (use Bicycling)
- ❌ General multi-use trail that allows mountain bikes

**Normalization:**
- "MTB trail", "mountain biking trail" → "Mountain Bike"

---

### BMX

**Definition:**
Linear BMX trail (not a closed-loop BMX park).

**When to use:**
- ✅ Source explicitly documents as BMX trail
- ✅ Linear BMX route, not a park

**When NOT to use:**
- ❌ BMX parks (these are Sites, not Trails)
- ❌ Pump tracks (use Pump Track)

---

### Pump Track

**Definition:**
Documented pump track explicitly classified as a trail (linear route).

**When to use:**
- ✅ Source explicitly documents as pump track
- ✅ Classified as a trail by managing agency

**When NOT to use:**
- ❌ Pump track parks (these are Sites)
- ❌ Inferred from surface type or layout

---

### Snowmobile

**Definition:**
Trail designated for snowmobile use.

**When to use:**
- ✅ Source explicitly documents snowmobile designation
- ✅ Snowmobile trail system

**Discovery guidance:**
Must be documented; don't infer from trail characteristics.

---

### Cross Country Ski

**Definition:**
Trail designated for cross-country skiing.

**When to use:**
- ✅ Source explicitly documents XC ski designation
- ✅ Nordic trail system

**Discovery guidance:**
Must be documented; don't infer from terrain.

**Normalization:**
- "XC ski trail", "nordic trail", "cross-country ski trail" → "Cross Country Ski"

---

### Other

**Definition:**
Named use type from authoritative source that doesn't fit any other category.

**When to use:**
- ✅ Source provides specific use type that doesn't match vocabulary
- ✅ Is a legitimate, documented use type

**When NOT to use:**
- ❌ Invented categories
- ❌ Inferred uses

**Discovery guidance:**
Record raw term exactly in notes. Flag for vocabulary expansion review.

------------------------------------------------------------
# 3. TRAIL SURFACE TYPE VOCABULARY (Controlled)

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
Trail with asphalt or concrete surface.

**When to use:**
- ✅ Asphalt surface
- ✅ Concrete surface
- ✅ Source documents as "paved"

**Note:** Asphalt and concrete are NOT separate values — both map to "Paved."

**Normalization:**
- "asphalt", "concrete", "hard surface", "paved path" → "Paved"

---

### Crushed Stone

**Definition:**
Trail with compacted crushed stone, limestone screenings, or similar fine aggregate surface.

**When to use:**
- ✅ Source documents as "crushed stone", "crushed limestone", "stone dust"
- ✅ Compacted aggregate surface

**Normalization:**
- "crushed limestone", "stone dust", "limestone screenings", "compacted gravel" → "Crushed Stone"

---

### Gravel

**Definition:**
Trail with loose gravel surface.

**When to use:**
- ✅ Source documents as "gravel"
- ✅ Loose stone surface (not compacted fine aggregate)

**Normalization:**
- "loose gravel", "gravel path" → "Gravel"

---

### Natural Surface

**Definition:**
Unpaved trail with dirt, soil, grass, or unimproved tread.

**When to use:**
- ✅ Source documents as "natural surface", "dirt", "unpaved"
- ✅ Unimproved tread

**Normalization:**
- "dirt trail", "earthen", "grass trail", "unimproved", "native surface" → "Natural Surface"

---

### Boardwalk

**Definition:**
Trail surface constructed of wood or composite decking.

**When to use:**
- ✅ Source documents as "boardwalk"
- ✅ Elevated wood or composite decking surface

**Normalization:**
- "wood deck", "elevated boardwalk" → "Boardwalk"

---

### Water

**Definition:**
Water trail — the surface is the waterway itself.

**When to use:**
- ✅ Trail is a water route
- ✅ Use Type is also "Water"

---

### Mixed

**Definition:**
Trail with multiple documented surface types.

**When to use:**
- ✅ Source explicitly states "mixed surface" or documents multiple surface types

**When NOT to use:**
- ❌ You observe a mix (must be documented)
- ❌ Trail transitions between surfaces without documentation

**Normalization:**
- "mixed surface", "varies" → "Mixed"

---

### Other

**Definition:**
Named surface type from authoritative source that doesn't fit any other category.

**Discovery guidance:**
Record raw term exactly in notes. Flag for vocabulary expansion review.

------------------------------------------------------------
# 4. TRAIL ORIGIN TYPE VOCABULARY (Controlled)

## 4.1 Allowed Values

- Rail Trail
- Canal Towpath
- Historic Route
- Greenway Corridor
- Purpose-Built
- Utility Corridor
- Roadside Corridor
- Other

------------------------------------------------------------
## 4.2 Definitions & Usage Rules

### Rail Trail

**Definition:**
Trail developed on a former railroad corridor.

**When to use:**
- ✅ Source explicitly documents rail trail history
- ✅ Former railroad right-of-way

**When NOT to use:**
- ❌ Trail near railroad tracks
- ❌ Inferred from linear alignment

**Normalization:**
- "rails-to-trails", "former rail corridor", "railroad trail" → "Rail Trail"

---

### Canal Towpath

**Definition:**
Trail on or adjacent to a historic canal towpath.

**When to use:**
- ✅ Source explicitly documents canal towpath origin
- ✅ "Towpath" used alone in source is sufficient

**Normalization:**
- "towpath", "canal trail" → "Canal Towpath"

---

### Historic Route

**Definition:**
Trail following a documented historic route (pioneer, military, native, etc.).

**When to use:**
- ✅ Source explicitly documents historic route designation
- ✅ Named historic road or corridor

**When NOT to use:**
- ❌ Old trails without documented historic designation
- ❌ Inferred from age

---

### Greenway Corridor

**Definition:**
Trail that is part of a planned or documented greenway system.

**When to use:**
- ✅ Source explicitly documents greenway corridor designation
- ✅ Managing agency describes as greenway

**When NOT to use:**
- ❌ Any trail through green space
- ❌ Inferred from landscape character

---

### Purpose-Built

**Definition:**
Trail constructed specifically as a trail with no prior corridor origin.

**When to use:**
- ✅ Source documents as purpose-built
- ✅ No prior corridor use documented

**Note:** This is the default for trails without documented origin — but only use if source supports it. Otherwise leave blank.

---

### Utility Corridor

**Definition:**
Trail built within a utility right-of-way (power line, pipeline, etc.).

**When to use:**
- ✅ Source explicitly documents utility corridor
- ✅ Power line trail, pipeline corridor trail

**Normalization:**
- "power line trail", "pipeline trail" → "Utility Corridor"

---

### Roadside Corridor

**Definition:**
Trail built along a road right-of-way.

**When to use:**
- ✅ Source explicitly documents roadside or road ROW origin
- ✅ Trail runs along a named road in its ROW

**Normalization:**
- "road corridor", "highway trail", "roadside path" → "Roadside Corridor"

---

### Other

**Definition:**
Named origin type from authoritative source that doesn't fit any other category.

**Discovery guidance:**
Record raw term exactly in notes. Flag for vocabulary expansion review.

------------------------------------------------------------
# 5. TRAIL STATUS VOCABULARY (Controlled)

## 5.1 Allowed Values

- Active
- Planned
- Under Construction
- Gap
- Closed

------------------------------------------------------------
## 5.2 Definitions & Usage Rules

### Active

**Definition:**
Trail is currently open and operational.

**When to use:**
- ✅ Explicitly documented as open/active
- ✅ Default when no restrictions are documented

**Discovery guidance:**
Can be left blank if obviously active and no other status indicators present.

---

### Planned

**Definition:**
Trail is documented as planned but not yet built.

**When to use:**
- ✅ Source explicitly documents as planned or proposed
- ✅ Trail appears in planning documents but not yet built

**When NOT to use:**
- ❌ Inferred from incomplete segments
- ❌ Assumed from maps showing dotted lines without documentation

**Discovery guidance:**
Must be explicitly documented.

---

### Under Construction

**Definition:**
Trail is actively being built.

**When to use:**
- ✅ Source explicitly states under construction
- ✅ Construction documented as active/ongoing

**Discovery guidance:**
Must be explicitly documented.

---

### Gap

**Definition:**
A missing or incomplete portion of an otherwise continuous trail corridor.

**When to use:**
- ✅ Source explicitly identifies a gap in the trail
- ✅ Trail corridor exists but has a documented missing section

**Note:** Status describes the trail as a whole. If the gap is the trail's defining characteristic, use Gap. Don't use for every trail with a small missing piece — use notes instead.

---

### Closed

**Definition:**
Trail is permanently or indefinitely closed.

**When to use:**
- ✅ Explicitly documented as permanently closed
- ✅ Decommissioned trail

**When NOT to use:**
- ❌ Temporary closures (use notes)
- ❌ Seasonal closures (use notes + Seasonal in notes field)

**Discovery guidance:**
Must be explicitly documented as closed.

------------------------------------------------------------
# 6. DIFFICULTY VOCABULARY (Controlled) ✨ NEW IN v5.0

## 6.1 Allowed Values

- Easy
- Moderate
- Difficult
- Strenuous
- Expert

------------------------------------------------------------
## 6.2 Definitions & Usage Rules

### Easy

**Definition:**
Trail suitable for beginners; minimal elevation change, good surface.

**When to use:**
- ✅ Source explicitly rates as "Easy"
- ✅ Beginner-friendly designation from managing agency

**When NOT to use:**
- ❌ Looks easy to you — don't assess yourself
- ❌ Paved trail — don't infer from surface type

---

### Moderate

**Definition:**
Trail suitable for average users; some elevation change or surface challenge.

**When to use:**
- ✅ Source explicitly rates as "Moderate"
- ✅ Intermediate designation from managing agency

**When NOT to use:**
- ❌ Assumed from trail characteristics
- ❌ Between Easy and Difficult without documentation

---

### Difficult

**Definition:**
Trail with significant elevation change, challenging terrain, or technical features.

**When to use:**
- ✅ Source explicitly rates as "Difficult" or "Hard"
- ✅ Advanced designation from managing agency

**Normalization:**
- "hard", "challenging", "advanced" → "Difficult" (context dependent)

---

### Strenuous

**Definition:**
Trail requiring high physical exertion; significant elevation gain or length.

**When to use:**
- ✅ Source explicitly rates as "Strenuous"
- ✅ Source documents high exertion requirements

---

### Expert

**Definition:**
Trail suitable only for expert users; highly technical or hazardous features.

**When to use:**
- ✅ Source explicitly rates as "Expert" or "Black Diamond"
- ✅ Expert-only designation

**Normalization:**
- "black diamond", "expert only", "technical" → "Expert" (context dependent)

------------------------------------------------------------
## 6.3 CRITICAL USAGE RULES FOR DIFFICULTY

**DO:**
- ✅ Record ONLY what authoritative sources explicitly state
- ✅ Leave blank if not documented
- ✅ Collect raw value during discovery; normalize during normalization

**DON'T:**
- ❌ Assess difficulty yourself
- ❌ Infer from terrain, length, or surface type
- ❌ Guess based on trail characteristics
- ❌ Use personal judgment

**Note on Trail vs. Trail Segment difficulty:**
- Trail-level difficulty describes the trail as a whole
- Trail Segment difficulty describes individual segments
- When segments vary widely, trail-level difficulty should reflect the most challenging segment or the overall characterization from the source

**Common normalization mappings:**
```
Raw Value          → Normalized Value
----------           ----------------
"beginner"         → Easy
"intermediate"     → Moderate
"hard"             → Difficult
"advanced"         → Difficult
"challenging"      → Difficult (check context)
"strenuous"        → Strenuous
"expert only"      → Expert
"black diamond"    → Expert
"technical"        → Expert (check context)
```

------------------------------------------------------------
# 7. ACCESSIBILITY (Free-Text — No Controlled Vocabulary) ✨ NEW IN v5.0

## 7.1 Overview

**Accessibility is a free-text field — there is no controlled vocabulary.**

Record the accessibility description exactly as documented by the authoritative source.

## 7.2 What to Collect

- ADA compliance statements
- Wheelchair accessibility descriptions
- Surface grade and width information
- Accessible facility descriptions (restrooms, parking, picnic areas)
- Specific accommodation information

**Examples of valid accessibility descriptions:**
- "ADA accessible from Main Street trailhead; paved surface, grades under 5%"
- "Wheelchair accessible for first 0.5 miles from north trailhead"
- "Not ADA compliant; natural surface with variable grades"
- "Accessible restrooms and parking at Bowling Green trailhead"

## 7.3 What NOT to Collect

- ❌ Inferred accessibility from surface type alone
- ❌ Personal assessments of accessibility
- ❌ Features of the parent site that don't relate to trail access

## 7.4 Discovery Guidance

- Record raw accessibility description exactly as found
- Don't rephrase or standardize
- If source provides multiple accessibility statements, semicolon-delimit them
- Leave blank if no accessibility information documented

## 7.5 Normalization Guidance

- Preserve free-text as-is
- No vocabulary mapping needed
- Clean obvious formatting issues (extra spaces, broken encoding)
- Combine multiple sources' accessibility statements if consistent

------------------------------------------------------------
# 8. VOCABULARY NORMALIZATION RULES

## 8.1 Common Mappings

**Trail Use Type:**
```
Raw Value                   → Normalized Value
-----------                   ----------------
"multi-purpose"             → "Multi-Use"
"multipurpose"              → "Multi-Use"
"shared use"                → "Multi-Use"
"walking trail"             → "Hiking"
"pedestrian trail"          → "Hiking"
"nature trail"              → "Hiking"
"footpath"                  → "Hiking"
"equestrian trail"          → "Bridle"
"horse trail"               → "Bridle"
"bike path"                 → "Bicycling"
"bicycle path"              → "Bicycling"
"paddling trail"            → "Water"
"blueway"                   → "Water"
"MTB trail"                 → "Mountain Bike"
"XC ski trail"              → "Cross Country Ski"
"nordic trail"              → "Cross Country Ski"
```

**Trail Surface Type:**
```
Raw Value                   → Normalized Value
-----------                   ----------------
"asphalt"                   → "Paved"
"concrete"                  → "Paved"
"hard surface"              → "Paved"
"crushed limestone"         → "Crushed Stone"
"stone dust"                → "Crushed Stone"
"limestone screenings"      → "Crushed Stone"
"compacted gravel"          → "Crushed Stone"
"dirt trail"                → "Natural Surface"
"earthen"                   → "Natural Surface"
"native surface"            → "Natural Surface"
"unimproved"                → "Natural Surface"
"elevated boardwalk"        → "Boardwalk"
"mixed surface"             → "Mixed"
```

**Trail Origin Type:**
```
Raw Value                   → Normalized Value
-----------                   ----------------
"rails-to-trails"           → "Rail Trail"
"former rail corridor"      → "Rail Trail"
"towpath"                   → "Canal Towpath"
"canal trail"               → "Canal Towpath"
"power line trail"          → "Utility Corridor"
"pipeline trail"            → "Utility Corridor"
"road corridor"             → "Roadside Corridor"
```

**Trail Status:**
```
Raw Value                   → Normalized Value
-----------                   ----------------
"open"                      → "Active"
"operational"               → "Active"
"proposed"                  → "Planned"
"permanently closed"        → "Closed"
"decommissioned"            → "Closed"
```

## 8.2 Ambiguous Cases

**Require context or manual review:**
- "multi-use" vs. specific use — check if source documents multiple explicit uses
- "bike trail" — could be Bicycling or Mountain Bike depending on surface/context
- "mixed" surface — check if documented or inferred
- "challenging" difficulty — could be Difficult or context-dependent
- "closed" status — could be permanent or temporary

**Resolution:**
- Check source context for additional descriptors
- Prefer more specific term when context supports it
- Leave blank rather than guess
- Flag for manual review if confidence low

------------------------------------------------------------
# 9. VOCABULARY USAGE RULES

## 9.1 Universal Rules

1. **Use exactly as written** — No synonyms, abbreviations, or invented terms
2. **Don't infer** — Values must be documented, not inferred from context or geometry
3. **Leave blank if unclear** — Better to have no value than wrong value
4. **One value per field** — No multi-value types (use most specific single term)
5. **Flag new values** — Don't add values; flag for vocabulary expansion

## 9.2 Discovery Phase

- Capture raw values exactly as found
- Don't attempt normalization during discovery
- Record raw variations in *_raw fields

## 9.3 Normalization Phase

- Map raw values to controlled vocabulary
- Handle common variations (see Section 8)
- Flag unrecognized values for review
- Validate against vocabulary list

## 9.4 When Vocabulary Doesn't Fit

**If authoritative source uses term not in vocabulary:**

1. **Discovery:** Record raw term exactly
2. **Normalization:** Map to closest vocabulary match OR leave blank and flag
3. **Flag for review:** Add to vocabulary expansion queue
4. **Document:** Include original term in notes field

------------------------------------------------------------
# 10. VOCABULARY VERSIONING

## 10.1 Version History

**v5.0:**
- Added Difficulty vocabulary (5 values)
- Added Accessibility field guidance (free-text, no vocabulary)
- Enhanced definitions for all existing vocabularies
- Added normalization mappings
- Updated to v5.0 references

**v4.0:**
- Initial controlled vocabulary
- Trail Use Type, Surface Type, Origin Type, Status defined

------------------------------------------------------------
# 11. INTEGRATION POINTS

This vocabulary module integrates with:

- **Trail Schema Module v5.0** (field definitions)
- **Trail Discovery Sub-Procedure v5.0** (raw capture)
- **Resolution Engine v5.0** (conflict detection)
- **Normalization Engine v5.0** (vocabulary mapping)
- **TSV Output Specification v5.0** (output format)

------------------------------------------------------------
# END OF TRAIL VOCABULARY MODULE v5.0
