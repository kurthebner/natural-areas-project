# NATURAL AREAS PROJECT
# TRAIL SEGMENT VOCABULARY MODULE v5.1
(Authoritative Controlled Vocabularies for Trail Segment Fields)

This module contains all controlled vocabularies for Trail Segment
entities in the Natural Areas Project v5.x.

All Trail Segment-related modules must reference this module for
vocabulary authority.

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

- `segment_role` vocabulary removed (field removed from schema)
- `segment_type` vocabulary retained
- `surface_type` vocabulary retained
- `status` vocabulary retained
- `difficulty` vocabulary added (new field)
- Enhanced definitions and usage guidance

------------------------------------------------------------
# 1. PURPOSE

This module defines the authoritative controlled vocabularies for:
- Segment Type
- Surface Type
- Status
- Difficulty

And provides field guidance for free-text fields:
- Accessibility (no controlled vocabulary)
- Identity Notes (no controlled vocabulary)
- Notes (no controlled vocabulary)

These vocabularies are used across:
- Trail Segment Discovery Sub-Procedure v5.x (raw capture)
- Resolution Engine v5.x (conflict detection)
- Normalization Engine v5.x (vocabulary mapping)
- Trail Segment TSV Output Specification v5.x (output format)

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
Segment that follows a straight or continuous path without forming
a loop.

**When to use:**
- ✅ Default for most segments
- ✅ Segment continues in one direction without looping back

**When NOT to use:**
- ❌ Segment forms a loop (use Loop)
- ❌ Segment branches off main trail (use Spur)

**Discovery guidance:**
Linear is the default. Only populate segment_type when explicitly
different from Linear.

**Normalization:**
- Leave blank if not specified — defaults to Linear
- "straight section", "continuous trail" → Linear

---

### Loop

**Definition:**
Segment that forms a closed loop returning to the starting point.

**When to use:**
- ✅ Segment itself forms a complete loop
- ✅ Loop trail section documented as a loop

**When NOT to use:**
- ❌ Entire trail is a loop (trail characteristic, not segment)
- ❌ Segment connects to another segment to form a loop (use Linear)

**Example:**
"Nature Loop Trail" with stem access:
- Stem (access to loop): Linear
- Loop portion: Loop

---

### Connector

**Definition:**
Segment that explicitly links two trails or two trail segments.

**When to use:**
- ✅ Links two different trails
- ✅ Explicitly documented as "connector"

**When NOT to use:**
- ❌ Access from parking to trail (use Access Segment)
- ❌ Short spur (use Spur)

---

### Spur

**Definition:**
Short segment that branches off the main trail and does not
reconnect.

**When to use:**
- ✅ Dead-end side trail
- ✅ Trail to overlook or viewpoint
- ✅ Offshoot that terminates

**When NOT to use:**
- ❌ Reconnects to main trail (use Loop or Connector)
- ❌ Access from parking (use Access Segment)

**Example:**
"Overlook Spur" — branches off main trail to viewpoint, ends there.

---

### Crossing

**Definition:**
Segment that crosses infrastructure (road, river, etc.) via bridge,
underpass, or at-grade crossing.

**When to use:**
- ✅ Bridge segment
- ✅ Underpass segment
- ✅ Road crossing explicitly documented as distinct segment

**When NOT to use:**
- ❌ Trail happens to cross a road (not a separate segment unless
  documented)

---

### Access Segment

**Definition:**
Short segment providing access from an access point to the main
trail corridor.

**When to use:**
- ✅ Parking lot to trailhead connector
- ✅ Access path from road to main trail
- ✅ Explicitly documented access connector

**When NOT to use:**
- ❌ Part of main trail (use Linear)
- ❌ Spur trail (use Spur)

---

### Other

**Definition:**
Named segment type from authoritative source that doesn't fit any
category.

**Discovery guidance:**
Record raw term in identity_notes_raw. Flag for vocabulary expansion
review.

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
Hard-surfaced trail with asphalt, concrete, or similar paved
material.

**Note:** Asphalt and concrete are NOT separate values — both map
to "Paved."

**Normalization:**
- "asphalt", "concrete", "pavement", "blacktop" → "Paved"

---

### Crushed Stone

**Definition:**
Compacted crushed stone or limestone surface.

**Normalization:**
- "limestone", "stone dust", "crushed limestone",
  "limestone screenings" → "Crushed Stone"

---

### Gravel

**Definition:**
Loose or compacted gravel surface.

**Normalization:**
- "loose gravel", "gravel path", "stone" → "Gravel"

---

### Natural Surface

**Definition:**
Unpaved trail with dirt, soil, grass, or unimproved tread.

**Normalization:**
- "dirt", "soil", "grass", "earth", "turf",
  "native surface", "unimproved" → "Natural Surface"

---

### Boardwalk

**Definition:**
Elevated wooden walkway or boardwalk.

**Normalization:**
- "wooden walkway", "deck", "elevated walkway" → "Boardwalk"

---

### Water

**Definition:**
Water-based segment (paddling trail).

**When to use:**
- ✅ Paddling trail segment
- ✅ Water trail portion

**When NOT to use:**
- ❌ Land trail that crosses water

---

### Mixed

**Definition:**
Segment with multiple documented surface types that cannot be
categorized as primarily one type.

**When to use:**
- ✅ Source explicitly states "mixed surface" or documents multiple
  surfaces for one segment

**When NOT to use:**
- ❌ Different segments have different surfaces — create separate
  segments instead
- ❌ Inferred from maps

**Note:** When in doubt, create separate segments per surface rather
than using Mixed.

---

### Other

**Discovery guidance:**
Record raw term in identity_notes_raw. Flag for vocabulary expansion
review.

**Examples of legitimate Other values:**
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

**Discovery guidance:**
Can be left blank if obviously active. Use explicitly when
differentiating from other segments with different status.

---

### Planned

**Definition:**
Segment is planned for future construction but not yet built.

**When to use:**
- ✅ Explicitly documented as planned or future segment

**When NOT to use:**
- ❌ Inferred from maps or incomplete alignments

---

### Gap

**Definition:**
Missing or incomplete portion of a trail where the segment does
not yet exist.

**When to use:**
- ✅ Trail discontinuity requiring road walk or detour
- ✅ Explicitly documented as a gap

**When NOT to use:**
- ❌ Closed segment (use Closed)
- ❌ Planned segment (use Planned)

**"Gap" is segment-specific** — represents missing trail continuity,
not a status of a physical segment.

**Example:**
"Buckeye Trail Mile 24-32 is a gap requiring road walk"

---

### Closed

**Definition:**
Segment is permanently or indefinitely closed to public use.

**When to use:**
- ✅ Explicitly documented as closed or decommissioned

**When NOT to use:**
- ❌ Temporary closures (use Notes)
- ❌ Seasonal closures (use Notes)

------------------------------------------------------------
# 5. DIFFICULTY VOCABULARY (Controlled)

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
Suitable for beginners; minimal elevation change, good surface.

**When to use:**
- ✅ Source explicitly rates this segment as "Easy"

**When NOT to use:**
- ❌ Looks easy to you — never self-assess
- ❌ Paved surface — never infer from surface type

---

### Moderate

**Definition:**
Some elevation change or moderate challenge; average fitness
required.

**When to use:**
- ✅ Source explicitly rates this segment as "Moderate"

---

### Difficult

**Definition:**
Significant elevation change, rough terrain, or challenging
features.

**When to use:**
- ✅ Source explicitly rates this segment as "Difficult" or "Hard"

**Normalization:**
- "hard", "challenging", "advanced" → "Difficult" (verify context)

---

### Strenuous

**Definition:**
Very demanding; significant elevation gain or length.

**When to use:**
- ✅ Source explicitly rates this segment as "Strenuous"

---

### Expert

**Definition:**
Highly technical or hazardous; suitable only for expert users.

**When to use:**
- ✅ Source explicitly rates this segment as "Expert" or
  "Black Diamond"

**Normalization:**
- "black diamond", "expert only", "technical" → "Expert"
  (verify context)

------------------------------------------------------------
## 5.3 CRITICAL USAGE RULES FOR DIFFICULTY

**DO:**
- ✅ Record ONLY what authoritative sources explicitly state
- ✅ Leave blank if not documented for this specific segment
- ✅ Capture raw value during discovery; normalize during normalization

**DON'T:**
- ❌ Assess difficulty yourself — ever
- ❌ Infer from terrain, length, or surface type
- ❌ Inherit from parent Trail without explicit segment-level
  documentation

**Segment-specific note:**
Difficulty can vary by segment even when the parent Trail has an
overall rating. A segment may be rated Moderate while the parent
Trail is rated Easy overall. Only populate if this specific segment
has explicit documentation.

**Common normalization mappings:**
```
Raw Value          → Normalized Value
----------           ----------------
"beginner"         → Easy
"intermediate"     → Moderate
"hard"             → Difficult
"advanced"         → Difficult
"challenging"      → Difficult (verify context)
"strenuous"        → Strenuous
"expert only"      → Expert
"black diamond"    → Expert
"technical"        → Expert (verify context)
```

------------------------------------------------------------
# 6. ACCESSIBILITY (Free-Text — No Controlled Vocabulary)

## 6.1 Overview

**Accessibility is a free-text field — there is no controlled
vocabulary.**

## 6.2 What to Collect

- ADA compliance statements specific to this segment
- Wheelchair accessibility descriptions for this segment
- Surface grade and width information for this segment
- Accessible facility descriptions at segment endpoints

**Examples:**
- "ADA accessible; paved surface, grades under 5%"
- "Wheelchair accessible for entire length"
- "Not ADA compliant; natural surface with variable grades"
- "Accessible viewing platform at mile 1.2"

## 6.3 What NOT to Collect

- ❌ Inferred accessibility from surface type alone
- ❌ Personal assessments of accessibility
- ❌ Parent Trail's accessibility description unless explicitly
  confirmed to apply to this segment

## 6.4 Segment-Specific Rule

**Do not inherit accessibility from the parent Trail without explicit
documentation.**

A segment may be ADA accessible while the parent Trail overall is
not — and vice versa. Only populate if segment-specific accessibility
documentation exists.

------------------------------------------------------------
# 7. IDENTITY NOTES (Free-Text — No Controlled Vocabulary)

## 7.1 Overview

**Identity Notes is a free-text field — there is no controlled
vocabulary.**

## 7.2 What to Capture

- Segment vs. trail boundary questions
- Segment name conflicts or ambiguities
- Shared-corridor documentation
- Parent Trail assignment uncertainty
- Vocabulary type flags (e.g., "source calls this a 'section' —
  unclear if named segment or informal reference")

## 7.3 Discovery vs. Normalization

- **Discovery stage**: capture in `identity_notes_raw`
- **Normalized stage**: surfaced as `identity_notes` field

------------------------------------------------------------
# 8. VOCABULARY NORMALIZATION RULES

## 8.1 Common Mappings

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
"technical"             → Expert (verify context)
```

------------------------------------------------------------
# 9. VOCABULARY USAGE RULES

## 9.1 Universal Rules

1. **Use exactly as written** — No synonyms or invented terms
2. **Don't infer** — Values must be documented
3. **Leave blank if unclear** — Better no value than wrong value
4. **One value per field** — No multi-value entries
5. **Flag new values** — Don't add values; flag for vocabulary
   expansion

## 9.2 Segment-Specific Notes

**Difficulty and Accessibility:**
- Can differ from parent Trail
- Only populate if segment-specific documentation exists
- Never inherit from parent Trail without explicit confirmation

**Surface Type:**
- Often the PRIMARY reason a segment exists as a distinct entity
- Different surface = different segment (preferred over Mixed)
- Be precise with surface documentation

**Status:**
- "Gap" is segment-specific vocabulary — represents missing trail
  continuity
- Important for long-distance trail documentation

------------------------------------------------------------
# 10. VOCABULARY VERSIONING

## 10.1 Version History

**v5.1:**
- Cross-module references updated to v5.x
- identity_notes field guidance added
- Maps field guidance updated (URL list, no type/description metadata)
- "Other" guidance updated to reference identity_notes_raw

**v5.0:**
- Difficulty vocabulary added (5 values)
- Accessibility field guidance added (free-text)
- segment_role vocabulary removed
- Enhanced definitions and normalization mappings

**v4.0:**
- Initial controlled vocabulary

------------------------------------------------------------
# 11. INTEGRATION POINTS

This vocabulary module integrates with:

- **Trail Segment Schema Module v5.x** (field definitions)
- **Trail Segment Discovery Sub-Procedure v5.x** (raw capture)
- **Resolution Engine v5.x** (identity matching)
- **Normalization Engine v5.x** (vocabulary mapping)
- **Trail Segment Normalization Contract v5.x** (normalization rules)
- **Trail Segment TSV Output Specification v5.x** (output format)

------------------------------------------------------------
# END OF TRAIL SEGMENT VOCABULARY MODULE v5.1
