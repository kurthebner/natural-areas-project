# NATURAL AREAS PROJECT
# TRAIL VOCABULARY MODULE v5.1
(Authoritative Controlled Vocabularies for Trail Fields)

This module contains all controlled vocabularies for Trail entities
in the Natural Areas Project v5.x.

All Trail-related modules must reference this module for vocabulary
authority.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **All cross-module references updated to v5.x**
- **identity_notes field guidance added**: identity_notes_raw at
  discovery feeds the normalized identity_notes field; no controlled
  vocabulary
- **Maps field guidance updated**: maps is now a plain URL list; type
  and description metadata removed from vocabulary guidance
- No vocabulary values added or removed

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- Difficulty vocabulary added (5 values)
- Accessibility field added (free-text, no controlled vocabulary)
- Enhanced definitions, usage rules, and normalization mappings

------------------------------------------------------------
# 1. PURPOSE

This module defines the authoritative controlled vocabularies for:
- Trail Use Type
- Trail Surface Type
- Trail Origin Type
- Trail Status
- Difficulty

And provides field guidance for free-text fields:
- Accessibility (no controlled vocabulary)
- Identity Notes (no controlled vocabulary)
- Notes (no controlled vocabulary)

These vocabularies are used across:
- Trail Discovery Sub-Procedure v5.x (raw capture)
- Resolution Engine v5.x (conflict detection)
- Normalization Engine v5.x (vocabulary mapping)
- Trail TSV Output Specification v5.x (output format)

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
- ❌ You observe multiple uses seem possible
- ❌ Trail allows bikes AND hikers but isn't labeled multi-use

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

**Normalization:**
- "walking trail", "pedestrian trail", "footpath" → "Hiking"
- "nature trail" → "Hiking"

---

### Bridle

**Definition:**
Trail primarily intended for equestrian use.

**When to use:**
- ✅ Source explicitly documents as bridle trail or equestrian trail

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
Trail primarily intended for general bicycle use on paved or
hard-surface trails.

**When to use:**
- ✅ Source explicitly documents as bicycle trail or bike path
- ✅ Paved or hard-surface trail with bicycle as primary use

**When NOT to use:**
- ❌ Mountain bike specific trails (use Mountain Bike)
- ❌ Multi-use trail that allows bikes (use Multi-Use)

**Normalization:**
- "bike path", "bicycle path", "bike trail", "cycle path" → "Bicycling"

---

### Mountain Bike

**Definition:**
Trail specifically designed or designated for mountain biking —
typically singletrack or natural-surface.

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

---

### Cross Country Ski

**Definition:**
Trail designated for cross-country skiing.

**When to use:**
- ✅ Source explicitly documents XC ski designation

**Normalization:**
- "XC ski trail", "nordic trail", "cross-country ski trail" →
  "Cross Country Ski"

---

### Other

**Definition:**
Named use type from authoritative source that doesn't fit any other
category.

**Discovery guidance:**
Record raw term in identity_notes_raw. Flag for vocabulary expansion
review.

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

**Note:** Asphalt and concrete are NOT separate values — both map to
"Paved."

**Normalization:**
- "asphalt", "concrete", "hard surface", "paved path" → "Paved"

---

### Crushed Stone

**Definition:**
Trail with compacted crushed stone, limestone screenings, or similar
fine aggregate surface.

**Normalization:**
- "crushed limestone", "stone dust", "limestone screenings",
  "compacted gravel" → "Crushed Stone"

---

### Gravel

**Definition:**
Trail with loose gravel surface.

**Normalization:**
- "loose gravel", "gravel path" → "Gravel"

---

### Natural Surface

**Definition:**
Unpaved trail with dirt, soil, grass, or unimproved tread.

**Normalization:**
- "dirt trail", "earthen", "grass trail", "unimproved",
  "native surface" → "Natural Surface"

---

### Boardwalk

**Definition:**
Trail surface constructed of wood or composite decking.

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
- ✅ Source explicitly states "mixed surface" or documents multiple
  surface types

**When NOT to use:**
- ❌ You observe a mix without documentation

**Normalization:**
- "mixed surface", "varies" → "Mixed"

---

### Other

**Discovery guidance:**
Record raw term in identity_notes_raw. Flag for vocabulary expansion
review.

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
- "rails-to-trails", "former rail corridor", "railroad trail" →
  "Rail Trail"

---

### Canal Towpath

**Definition:**
Trail on or adjacent to a historic canal towpath.

**Normalization:**
- "towpath", "canal trail" → "Canal Towpath"

---

### Historic Route

**Definition:**
Trail following a documented historic route (pioneer, military,
native, etc.).

**When to use:**
- ✅ Source explicitly documents historic route designation

**When NOT to use:**
- ❌ Old trails without documented historic designation
- ❌ Inferred from age

---

### Greenway Corridor

**Definition:**
Trail that is part of a planned or documented greenway system.

**When to use:**
- ✅ Source explicitly documents greenway corridor designation

**When NOT to use:**
- ❌ Any trail through green space
- ❌ Inferred from landscape character

---

### Purpose-Built

**Definition:**
Trail constructed specifically as a trail with no prior corridor origin.

**Note:** Only use if source supports it or no other origin type applies
and the trail is documented as purpose-built. Otherwise leave blank.

---

### Utility Corridor

**Definition:**
Trail built within a utility right-of-way (power line, pipeline, etc.).

**Normalization:**
- "power line trail", "pipeline trail" → "Utility Corridor"

---

### Roadside Corridor

**Definition:**
Trail built along a road right-of-way.

**Normalization:**
- "road corridor", "highway trail", "roadside path" →
  "Roadside Corridor"

---

### Other

**Discovery guidance:**
Record raw term in identity_notes_raw. Flag for vocabulary expansion
review.

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

**Discovery guidance:**
Can be left blank if obviously active.

---

### Planned

**Definition:**
Trail is documented as planned but not yet built.

**When to use:**
- ✅ Source explicitly documents as planned or proposed

**When NOT to use:**
- ❌ Inferred from incomplete segments
- ❌ Dotted lines on maps without documentation

---

### Under Construction

**Definition:**
Trail is actively being built.

**When to use:**
- ✅ Source explicitly states under construction

---

### Gap

**Definition:**
A missing or incomplete portion of an otherwise continuous trail
corridor.

**When to use:**
- ✅ Source explicitly identifies a gap in the trail
- ✅ Trail corridor exists but has a documented missing section

**Note:** Status describes the trail as a whole. Only use Gap if the
missing section is the defining characteristic of the trail's current
state. For minor gaps, use Notes instead.

---

### Closed

**Definition:**
Trail is permanently or indefinitely closed.

**When to use:**
- ✅ Explicitly documented as permanently closed
- ✅ Decommissioned trail

**When NOT to use:**
- ❌ Temporary closures (use Notes)
- ❌ Seasonal closures (use Notes)

------------------------------------------------------------
# 6. DIFFICULTY VOCABULARY (Controlled)

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

**When NOT to use:**
- ❌ Looks easy to you — never self-assess
- ❌ Paved trail — never infer from surface type

---

### Moderate

**Definition:**
Trail suitable for average users; some elevation change or challenge.

**When to use:**
- ✅ Source explicitly rates as "Moderate"

---

### Difficult

**Definition:**
Trail with significant elevation change, challenging terrain, or
technical features.

**When to use:**
- ✅ Source explicitly rates as "Difficult" or "Hard"

**Normalization:**
- "hard", "challenging", "advanced" → "Difficult" (verify context)

---

### Strenuous

**Definition:**
Trail requiring high physical exertion; significant elevation gain or
length.

**When to use:**
- ✅ Source explicitly rates as "Strenuous"

---

### Expert

**Definition:**
Trail suitable only for expert users; highly technical or hazardous.

**When to use:**
- ✅ Source explicitly rates as "Expert" or "Black Diamond"

**Normalization:**
- "black diamond", "expert only" → "Expert"

------------------------------------------------------------
## 6.3 CRITICAL USAGE RULES FOR DIFFICULTY

**DO:**
- ✅ Record ONLY what authoritative sources explicitly state
- ✅ Leave blank if not documented
- ✅ Capture raw value during discovery; normalize during normalization

**DON'T:**
- ❌ Assess difficulty yourself — ever
- ❌ Infer from terrain, length, or surface type
- ❌ Use personal judgment

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
# 7. ACCESSIBILITY (Free-Text — No Controlled Vocabulary)

## 7.1 Overview

**Accessibility is a free-text field — there is no controlled
vocabulary.**

## 7.2 What to Collect

- ADA compliance statements
- Wheelchair accessibility descriptions
- Surface grade and width information
- Accessible facility descriptions

**Examples:**
- "ADA accessible from Main Street trailhead; paved surface, grades
  under 5%"
- "Wheelchair accessible for first 0.5 miles from north trailhead"
- "Not ADA compliant; natural surface with variable grades"

## 7.3 What NOT to Collect

- ❌ Inferred accessibility from surface type alone
- ❌ Personal assessments of accessibility

------------------------------------------------------------
# 8. IDENTITY NOTES (Free-Text — No Controlled Vocabulary)

## 8.1 Overview

**Identity Notes is a free-text field — there is no controlled
vocabulary.**

Used for identity clarifications that don't belong in Notes.

## 8.2 What to Capture

- Trail vs. trail segment boundary questions
- Alternate name conflicts
- Network membership uncertainty
- Disambiguation notes
- Vocabulary type flags (e.g., "source calls this 'pathway' — may be
  Hiking or Multi-Use; flagged for review")

## 8.3 Discovery vs. Normalization

- **Discovery stage**: capture in `identity_notes_raw`
- **Normalized stage**: surfaced as `identity_notes` field

------------------------------------------------------------
# 9. VOCABULARY NORMALIZATION RULES

## 9.1 Common Mappings

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

## 9.2 Ambiguous Cases

**Require context or manual review:**
- "multi-use" vs. specific use — check if source documents multiple
  explicit uses
- "bike trail" — could be Bicycling or Mountain Bike depending on
  surface/context
- "mixed" surface — check if documented or inferred
- "challenging" difficulty — check context before mapping to Difficult
- "closed" status — permanent or temporary?

**Resolution:**
- Check source context
- Prefer more specific term when context supports it
- Leave blank rather than guess
- Flag in identity_notes if confidence is low

------------------------------------------------------------
# 10. VOCABULARY USAGE RULES

## 10.1 Universal Rules

1. **Use exactly as written** — No synonyms, abbreviations, or
   invented terms
2. **Don't infer** — Values must be documented, not inferred from
   context or geometry
3. **Leave blank if unclear** — Better no value than wrong value
4. **One value per field** — No multi-value controlled fields
5. **Flag new values** — Don't add values; flag for vocabulary
   expansion

## 10.2 Discovery Phase

- Capture raw values exactly as found in `_raw` fields
- Don't attempt normalization during discovery
- Capture identity clarifications in `identity_notes_raw`

## 10.3 Normalization Phase

- Map raw values to controlled vocabulary
- Handle common variations (see Section 9)
- Flag unrecognized values for review
- Validate against vocabulary list

------------------------------------------------------------
# 11. VOCABULARY VERSIONING

## 11.1 Version History

**v5.1:**
- Cross-module references updated to v5.x
- identity_notes field guidance added
- Maps field guidance updated (URL list, no type/description metadata)
- "Other" vocabulary guidance updated to reference identity_notes_raw

**v5.0:**
- Difficulty vocabulary added (5 values)
- Accessibility field guidance added (free-text)
- Enhanced definitions and normalization mappings

**v4.0:**
- Initial controlled vocabulary
- Trail Use Type, Surface Type, Origin Type, Status defined

------------------------------------------------------------
# 12. INTEGRATION POINTS

This vocabulary module integrates with:

- **Trail Schema Module v5.x** (field definitions)
- **Trail Discovery Sub-Procedure v5.x** (raw capture)
- **Resolution Engine v5.x** (conflict detection)
- **Normalization Engine v5.x** (vocabulary mapping)
- **Trail Normalization Contract v5.x** (normalization rules)
- **Trail TSV Output Specification v5.x** (output format)

------------------------------------------------------------
# END OF TRAIL VOCABULARY MODULE v5.1
