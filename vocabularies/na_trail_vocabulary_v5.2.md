# NATURAL AREAS PROJECT
# TRAIL VOCABULARY MODULE v5.2
(Authoritative Controlled Vocabularies for Trail Fields)

This module contains all controlled vocabularies for Trail entities
in the Natural Areas Project v5.x.

All Trail-related modules must reference this module for vocabulary
authority.

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- **§9 Vocabulary Normalization Rules replaced with enforcement-grade tables (IMP-100)**:
  The previous §9 contained informal code-block mapping lists with no
  enforcement semantics. Replaced with six numbered subsections (§9.1–§9.6)
  modeled on the site vocabulary §7.x pattern. Each subsection provides:
  a formatted mapping table for out-of-vocabulary raw values; resolution
  method (null-and-log vs. REVIEW); and enforcement requirements for the
  Normalization Engine and Trail Normalization Contract.
- **§9.6 Multi-value and empty string enforcement added**: All five
  vocabulary-controlled Trail fields are single-value. Compound values
  (e.g., "Foot;Bike", "Easy/Moderate") and empty strings ("") are now
  explicitly prohibited and must be handled per §9.6 rules.
- **IMP-100 DB findings incorporated into mapping tables**: Live DB audit
  of 12 Ohio county runs identified the following out-of-vocabulary values
  in active use; all are mapped in §9.x tables: "Foot" (use_type),
  "Foot;Bike" (compound), "Paved asphalt", "Primitive/Rustic",
  "Natural/Singletrack", "Natural/Primitive", "Chip-and-seal",
  "Gravel/Chip-and-seal" (surface_type), "Natural", "Village-built",
  "State-built", "Rail-trail", "City-built", "Wildlife area trail",
  "District-built" (origin_type), "Open", "Open/Partial" (status),
  "Varies", "Easy-Moderate", "Easy to Moderate", "Easy to Difficult"
  (difficulty).
- **§11 Version history updated**

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
- "foot", "foot travel", "walking" → "Hiking"

---

### Bridle

**Definition:**
Trail primarily intended for equestrian use.

**When to use:**
- ✅ Source explicitly documents as bridle trail or equestrian trail

**Normalization:**
- "equestrian trail", "equestrian", "horse trail" → "Bridle"

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
- "MTB trail", "mountain biking trail", "MTB" → "Mountain Bike"

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
Trail with asphalt, concrete, or chip-and-seal surface.

**Note:** Asphalt, concrete, and chip-and-seal are NOT separate values —
all map to "Paved."

**Normalization:**
- "asphalt", "concrete", "hard surface", "paved path" → "Paved"
- "chip-and-seal", "chip and seal", "paved asphalt" → "Paved"

---

### Crushed Stone

**Definition:**
Trail with compacted crushed stone, limestone screenings, or similar
fine aggregate surface.

**Normalization:**
- "crushed limestone", "stone dust", "limestone screenings",
  "compacted gravel", "fine gravel" → "Crushed Stone"

---

### Gravel

**Definition:**
Trail with loose gravel surface.

**Normalization:**
- "loose gravel", "gravel path" → "Gravel"

---

### Natural Surface

**Definition:**
Unpaved trail with dirt, soil, grass, or unimproved tread. Includes
primitive, rustic, and singletrack trails documented without a more
specific surface type.

**Normalization:**
- "dirt trail", "earthen", "grass trail", "unimproved",
  "native surface" → "Natural Surface"
- "primitive", "rustic", "primitive/rustic" → "Natural Surface"
- "singletrack" → "Natural Surface" (singletrack is a width
  descriptor; surface is Natural Surface unless otherwise documented)
- "natural/singletrack", "natural/primitive" → "Natural Surface"

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
- "rails-to-trails", "former rail corridor", "railroad trail",
  "rail-trail" → "Rail Trail"

---

### Canal Towpath

**Definition:**
Trail on or adjacent to a historic canal towpath.

**Normalization:**
- "towpath", "canal trail", "canal path" → "Canal Towpath"

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
Trail constructed specifically as a trail with no prior corridor
origin. Also used when a government or agency built a trail on
dedicated land with no inherited corridor.

**Note:** Any "[governance entity]-built" pattern (e.g., "Village-built",
"State-built", "City-built", "District-built") maps to "Purpose-Built" —
the governance entity is already captured in the governance field.

**Normalization:**
- "purpose-built", "Purpose-built" → "Purpose-Built"
- "village-built", "state-built", "city-built", "district-built",
  "county-built", "township-built" → "Purpose-Built"

---

### Utility Corridor

**Definition:**
Trail built within a utility right-of-way (power line, pipeline, etc.).

**Normalization:**
- "power line trail", "powerline trail", "power line corridor",
  "pipeline trail" → "Utility Corridor"

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

**Normalization:**
- "open", "open to public", "operational" → "Active"

---

### Planned

**Definition:**
Trail is documented as planned but not yet built.

**When to use:**
- ✅ Source explicitly documents as planned or proposed

**When NOT to use:**
- ❌ Inferred from incomplete segments
- ❌ Dotted lines on maps without documentation

**Normalization:**
- "proposed", "future" → "Planned"

---

### Under Construction

**Definition:**
Trail is actively being built.

**When to use:**
- ✅ Source explicitly states under construction

**Normalization:**
- "under construction", "in construction" → "Under Construction"

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

**Normalization:**
- "permanently closed", "decommissioned", "permanent closure" → "Closed"

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

**Normalization:**
- "beginner", "beginning" → "Easy"

---

### Moderate

**Definition:**
Trail suitable for average users; some elevation change or challenge.

**When to use:**
- ✅ Source explicitly rates as "Moderate"

**Normalization:**
- "intermediate" → "Moderate"

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
- "black diamond", "expert only", "expert-only" → "Expert"
- "technical" → "Expert" (verify context; technical in MTB context = Expert)

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
# 9. VOCABULARY NORMALIZATION RULES — ENFORCEMENT (IMP-100)

The Normalization Engine and Trail Normalization Contract must apply
the mapping tables in this section to every controlled Trail field.
All out-of-vocabulary raw values must be mapped or nulled per the
rules below; they must never silently pass through to the normalized
entity or TSV output.

**Enforcement model:**
- All five vocabulary-controlled Trail fields are **optional** (blanks are valid).
  Out-of-vocabulary values that cannot be mapped → **null the field and log**
  (not FATAL REJECT — the entity is not rejected).
- "Null-and-log" means: set the field to blank, preserve the original raw value
  in `identity_notes` (append a vocabulary flag), and write the mapping decision
  to `normalization_provenance`.
- **REVIEW** items require the normalization engine to halt on that field and
  surface the entity for human resolution before proceeding.
- Empty strings ("") are not valid blanks — see §9.6.

------------------------------------------------------------
## 9.1 Trail Use Type Normalization Mapping (IMP-100)

The normalization engine must validate every `use_type` value against the
§2.1 allowed list. Apply the mapping table below for out-of-vocabulary values.
Unmappable values → **null-and-log**.

| Raw / Out-of-Vocabulary Value | Maps To | Resolution Method |
|-------------------------------|---------|-------------------|
| "foot" | "Hiking" | Standard synonym. |
| "foot travel" | "Hiking" | Standard synonym. |
| "walking" | "Hiking" | Standard synonym. |
| "pedestrian" | "Hiking" | Standard synonym. |
| "nature trail" | "Hiking" | Standard synonym. |
| "walking trail" | "Hiking" | Standard synonym. |
| "pedestrian trail" | "Hiking" | Standard synonym. |
| "footpath" | "Hiking" | Standard synonym. |
| "equestrian" | "Bridle" | Standard synonym. |
| "equestrian trail" | "Bridle" | Standard synonym. |
| "horse trail" | "Bridle" | Standard synonym. |
| "paddling" / "paddling trail" | "Water" | Standard synonyms. |
| "canoe trail" / "kayak trail" | "Water" | Standard synonyms. |
| "blueway" | "Water" | Standard synonym. |
| "bike path" / "bicycle path" | "Bicycling" | Standard synonyms. |
| "bike trail" / "cycle path" | "Bicycling" | Standard synonyms. |
| "MTB" / "MTB trail" | "Mountain Bike" | Standard synonyms. |
| "mountain biking trail" | "Mountain Bike" | Standard synonym. |
| "snowmobile trail" / "snowmobile route" | "Snowmobile" | Standard synonyms. |
| "XC ski" / "XC ski trail" | "Cross Country Ski" | Standard synonyms. |
| "cross-country ski trail" | "Cross Country Ski" | Standard synonym. |
| "nordic trail" / "nordic" | "Cross Country Ski" | Standard synonyms. |
| "multi-purpose" / "multipurpose" | "Multi-Use" | Standard synonyms. |
| "shared use" / "shared-use" | "Multi-Use" | Standard synonyms. |
| Compound values (e.g., "Foot;Bike", "Hiking/Biking", "Hiking/Mountain Biking") | **REVIEW** | Single-value field — multiple uses must be resolved. If source explicitly documents "multi-use" → map to "Multi-Use". If ambiguous → null-and-log. Record raw value in `identity_notes`. |
| Any value not in §2.1 and not in this table | **null-and-log** | Preserve raw in identity_notes; flag "use_type OOV: [value]" in normalization_provenance. |

------------------------------------------------------------
## 9.2 Trail Surface Type Normalization Mapping (IMP-100)

The normalization engine must validate every `surface_type` value against
the §3.1 allowed list. Apply the mapping table below for out-of-vocabulary
values. Unmappable values → **null-and-log**.

| Raw / Out-of-Vocabulary Value | Maps To | Resolution Method |
|-------------------------------|---------|-------------------|
| "asphalt" / "asphalt path" / "paved asphalt" | "Paved" | Standard synonyms; "paved asphalt" contains "asphalt". |
| "concrete" | "Paved" | Standard synonym. |
| "hard surface" | "Paved" | Standard synonym. |
| "chip-and-seal" / "chip and seal" | "Paved" | Surface treatment applied to a compacted base; maps to Paved. |
| "crushed limestone" / "limestone screenings" | "Crushed Stone" | Standard synonyms. |
| "stone dust" | "Crushed Stone" | Standard synonym. |
| "compacted gravel" / "fine gravel" | "Crushed Stone" | Fine aggregate; maps to Crushed Stone. |
| "loose gravel" / "gravel path" | "Gravel" | Standard synonyms. |
| "dirt" / "dirt trail" | "Natural Surface" | Standard synonyms. |
| "earthen" / "soil" | "Natural Surface" | Standard synonyms. |
| "grass" / "grass trail" | "Natural Surface" | Standard synonyms. |
| "unimproved" / "native surface" | "Natural Surface" | Standard synonyms. |
| "primitive" / "rustic" / "primitive/rustic" | "Natural Surface" | Unpaved, minimal-improvement surfaces. |
| "singletrack" | "Natural Surface" | Singletrack is a trail width descriptor, not a surface type. Map to Natural Surface unless otherwise documented. |
| "natural/singletrack" | "Natural Surface" | Compound — both components indicate natural surface. Strip context note. |
| "natural/primitive" | "Natural Surface" | Compound — both components indicate natural surface. |
| "natural surface (former railroad grade)" | "Natural Surface" | Parenthetical origin note — strip parenthetical, map surface. Record origin context in `identity_notes`. |
| "wood deck" / "elevated boardwalk" | "Boardwalk" | Standard synonyms. |
| "mixed surface" / "varies" | "Mixed" | Standard synonyms — only when documented, not inferred. |
| Compound with "/" where components differ (e.g., "Gravel/Chip-and-seal", "Paved/Crushed Stone") | **REVIEW** | Possible "Mixed" if source supports it. If source explicitly documents multiple surfaces → map to "Mixed". If ambiguous → null-and-log. Record both raw terms in `identity_notes`. |
| "Natural surface" (wrong case) | "Natural Surface" | Case normalization only. |
| "Paved" / "Gravel" / "Mixed" (correct value, wrong case) | Apply case correction | Identity mapping with case normalization. |
| Any value not in §3.1 and not in this table | **null-and-log** | Preserve raw in identity_notes; flag "surface_type OOV: [value]" in normalization_provenance. |

------------------------------------------------------------
## 9.3 Trail Origin Type Normalization Mapping (IMP-100)

Origin type is fully optional — blank is always valid. Apply the mapping
table below for out-of-vocabulary values. Unmappable values → **null-and-log**
(entity is not rejected; raw value preserved in identity_notes).

| Raw / Out-of-Vocabulary Value | Maps To | Resolution Method |
|-------------------------------|---------|-------------------|
| "rails-to-trails" / "railroad trail" / "former rail corridor" | "Rail Trail" | Standard synonyms. |
| "rail-trail" | "Rail Trail" | Hyphenated variant. |
| "towpath" / "canal trail" / "canal path" | "Canal Towpath" | Standard synonyms. |
| "power line trail" / "powerline trail" / "power line corridor" | "Utility Corridor" | Standard synonyms. |
| "pipeline trail" / "pipeline corridor" | "Utility Corridor" | Standard synonyms. |
| "road corridor" / "roadside path" / "highway trail" | "Roadside Corridor" | Standard synonyms. |
| "village-built" | "Purpose-Built" | Governance-built pattern. Governance entity is in `governance` field. |
| "state-built" | "Purpose-Built" | Governance-built pattern. |
| "city-built" | "Purpose-Built" | Governance-built pattern. |
| "district-built" | "Purpose-Built" | Governance-built pattern. |
| "county-built" | "Purpose-Built" | Governance-built pattern. |
| "township-built" | "Purpose-Built" | Governance-built pattern. |
| "purpose-built" | "Purpose-Built" | Case normalization. |
| "natural" | **null-and-log** | "Natural" describes surface character or ecological context, not corridor origin. Not a valid origin type. Strip; log "origin_type: 'natural' is not a valid origin type; stripped." |
| "wildlife area trail" | **null-and-log** | Describes governance context, not trail origin. Not a valid origin type. Strip; log. |
| Any value not in §4.1 and not in this table | **null-and-log** | Preserve raw in identity_notes; flag "origin_type OOV: [value]" for vocabulary expansion review. |

------------------------------------------------------------
## 9.4 Trail Status Normalization Mapping (IMP-100)

| Raw / Out-of-Vocabulary Value | Maps To | Resolution Method |
|-------------------------------|---------|-------------------|
| "open" / "open to public" / "operational" | "Active" | Standard synonyms. |
| "proposed" / "future" | "Planned" | Standard synonyms. |
| "under construction" / "in construction" | "Under Construction" | Standard synonyms. |
| "permanent closure" / "permanently closed" / "decommissioned" | "Closed" | Standard synonyms. |
| "open/partial" | **REVIEW** | Context-dependent: if a defined section is missing and is the defining characteristic of the trail's current state → "Gap"; if mostly open with a minor restriction → "Active" + Note. Surface for human resolution; do not auto-assign. |
| Empty string ("") | null | See §9.6. |
| Any value not in §5.1 and not in this table | **null-and-log** | Leave blank; log "status OOV: [value]". |

------------------------------------------------------------
## 9.5 Trail Difficulty Normalization Mapping (IMP-100)

Difficulty is optional and must never be inferred. Apply this table only
to values captured from explicit authoritative source ratings.

| Raw / Out-of-Vocabulary Value | Maps To | Resolution Method |
|-------------------------------|---------|-------------------|
| "beginner" / "beginning" | "Easy" | Standard synonyms. |
| "intermediate" | "Moderate" | Standard synonym. |
| "hard" | "Difficult" | Verify context before mapping. |
| "advanced" | "Difficult" | Verify context before mapping. |
| "challenging" | "Difficult" | Verify context; if used as a difficulty rating in a managed trail system → "Difficult". |
| "expert only" / "expert-only" | "Expert" | Standard synonyms. |
| "black diamond" | "Expert" | Trail rating system standard. |
| "technical" | "Expert" | Verify context; in MTB/trail-rating context → "Expert". |
| "varies" / "variable" | **null-and-log** | Not a valid difficulty value. Variability should be documented in Notes. |
| Compound values (e.g., "Easy-Moderate", "Easy to Moderate", "Easy to Difficult", "Moderate to Difficult") | **null-and-log** | Single-value field. A range cannot be assigned. Leave blank; document the source range in Notes (e.g., "Source rates difficulty as Easy to Moderate"). |
| Empty string ("") | null | See §9.6. |
| Any value not in §6.1 and not in this table | **null-and-log** | Leave blank; log "difficulty OOV: [value]". |

------------------------------------------------------------
## 9.6 Multi-Value and Empty String Enforcement (IMP-100)

### Single-Value Requirement

All five vocabulary-controlled Trail fields are **single-value** — one
canonical value only:

| Field | Single-Value | Multi-value prohibited |
|-------|--------------|------------------------|
| `use_type` | ✅ | "Foot;Bike", "Hiking/Biking" are never valid |
| `surface_type` | ✅ | "Paved/Gravel" is never valid (use "Mixed" if documented) |
| `origin_type` | ✅ | No compound origin types |
| `status` | ✅ | "Open/Partial" is never valid (see §9.4 REVIEW) |
| `difficulty` | ✅ | "Easy-Moderate", "Easy to Difficult" are never valid |

When a compound value appears in any of these fields, apply the mapping
table for that field. If the compound cannot be resolved to a single
canonical value:
1. Set the field to blank
2. Append a vocabulary flag to `identity_notes`: e.g., "use_type compound value: 'Foot;Bike' — could not resolve to single term; flagged for review"
3. Write the raw value to `normalization_provenance` as "compound_value_stripped"

### Empty String Enforcement

An empty string ("") is **not** a valid blank in any vocabulary-controlled
field. An empty string is a data defect, not a documented absence.

**Rule:** For every vocabulary-controlled field, after mapping table
application, if the result is an empty string → convert to null (blank).
Log: "field [name]: empty string converted to null."

This rule applies to all five controlled Trail fields and prevents empty
strings from reaching TSV output where they would fail the TSV integrity check.

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

- Apply §9.x mapping tables to all vocabulary-controlled fields
- Handle compound values per §9.6
- Convert empty strings to null per §9.6
- Null-and-log all unmappable values
- Surface REVIEW items for human resolution before TSV output

------------------------------------------------------------
# 11. VOCABULARY VERSIONING

## 11.1 Version History

**v5.2 (2026-05-06):**
- §9 replaced with enforcement-grade normalization tables (§9.1–§9.6)
  per site vocabulary §7.x pattern. Previous §9 code-block mapping lists
  had no enforcement semantics; replaced with formatted tables, resolution
  methods, REVIEW/null-and-log rules, and multi-value/empty-string
  enforcement. Live DB audit findings from 12 county runs incorporated
  into mapping tables. Resolves IMP-100.

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
# END OF TRAIL VOCABULARY MODULE v5.2
