# NATURAL AREAS PROJECT
# TRAILTHING VOCABULARY MODULE v6.0
(Authoritative Controlled Vocabularies for Trailthing Fields)

This module contains all controlled vocabularies for Trailthing entities
in the Natural Areas Project v6.x.

All Trailthing-related modules must reference this module for vocabulary
authority.

------------------------------------------------------------
# CHANGES FROM v5.x TRAIL AND TRAIL NETWORK VOCABULARIES → v6.0

This module supersedes:
- Trail Vocabulary Module v5.x (for Trail-related vocabularies)
- Trail Network Vocabulary Module v5.x (for Trail Network-related vocabularies)

**Changes from v5 Trail Vocabulary:**
- **Org Type vocabulary added** (§5): New field for Trailthing entities;
  classifies the organizational category of the primary governance entity.
  Descriptive only — no threshold or identity-gate function.
- **Status vocabulary expanded** (§6): Merged Trail status (Active, Planned,
  Under Construction, Gap, Closed) with Trail Network status (Under Development,
  Partially Open). Seven values total; all are mutually exclusive.
- **Source Term guidance added** (§9): New free-text field; captures verbatim
  source vocabulary. No controlled vocabulary — explicit guidance on what
  constitutes good capture vs. normalization attempts.
- **Source Hierarchy Context guidance added** (§9): New free-text field;
  captures how sources frame relational context.
- Trail Use Type, Surface Type, Origin Type, and Difficulty carry forward
  from v5 Trail Vocabulary with no changes to allowed values. Normalization
  mapping tables carried forward and extended.
- Trail Network network_type vocabulary is retired — the source_term field
  captures this information as verbatim source vocabulary without forcing
  controlled classification.

**Note on Org Type and Site Network consistency**: Org Type values defined
here (§5) should be treated as the canonical org_type vocabulary for all
entity types in v6.x. When the Site Network Vocabulary Module v6.0 is
written (IMP-003), its org_type values must align with §5 of this module.

------------------------------------------------------------
# 1. PURPOSE

This module defines the authoritative controlled vocabularies for:
- Use Type (§2)
- Surface Type (§3)
- Origin Type (§4)
- Org Type (§5)
- Status (§6)
- Difficulty (§7)

And provides field guidance for free-text fields:
- Accessibility (§8)
- Source Term (§9)
- Source Hierarchy Context (§9)
- Ownership (§10)
- Identity Notes (§11)

These vocabularies are used across:
- Trailthing Discovery Sub-Procedure v6.x (raw capture)
- Resolution Engine v6.x (conflict detection)
- Normalization Engine v6.x (vocabulary mapping)
- Trailthing TSV Output Specification v6.x (output format)

**Key Principle:** Vocabularies are DESCRIPTIVE, not PRESCRIPTIVE.
- Values describe what authoritative sources document
- Values are not inferred from geometry, context, or judgment
- If no documented value matches, leave the field blank

------------------------------------------------------------
# 2. USE TYPE VOCABULARY (Controlled)

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
Trailthing explicitly documented as serving multiple user types.

**When to use:**
- ✅ Source explicitly states "multi-use" or "multi-purpose"
- ✅ Managing agency documents multiple permitted uses

**When NOT to use:**
- ❌ You observe multiple uses seem possible — never infer
- ❌ Trail allows bikes AND hikers but isn't labeled multi-use by the source

**Normalization:** "multi-purpose," "multipurpose," "shared use," "shared-use" → "Multi-Use"

---

### Hiking

**Definition:**
Trailthing primarily intended for foot travel.

**When to use:**
- ✅ Source explicitly documents as hiking trail, walking trail, or foot trail
- ✅ Foot traffic is the documented primary use

**Normalization:** "walking trail," "pedestrian trail," "footpath," "nature trail,"
"foot," "foot travel," "walking" → "Hiking"

---

### Bridle

**Definition:**
Trailthing primarily intended for equestrian use.

**When to use:**
- ✅ Source explicitly documents as bridle trail or equestrian trail

**Normalization:** "equestrian trail," "equestrian," "horse trail," "riding trail" → "Bridle"

---

### Water

**Definition:**
Water trail — a defined route on a waterway.

**When to use:**
- ✅ Trailthing is a documented water route (river, lake, reservoir)
- ✅ Source documents as "water trail," "paddling trail," or "blueway"

**When NOT to use:**
- ❌ A land trail that passes near water
- ❌ A land trail with water crossings

**Normalization:** "paddling trail," "canoe trail," "kayak trail," "blueway,"
"paddling route," "water route" → "Water"

---

### Bicycling

**Definition:**
Trailthing primarily intended for general bicycle use on paved or
hard-surface trails.

**When to use:**
- ✅ Source explicitly documents as bicycle trail or bike path
- ✅ Paved or hard-surface trail with bicycle as primary documented use

**When NOT to use:**
- ❌ Mountain bike specific trails (use Mountain Bike)
- ❌ Multi-use trail that allows bikes (use Multi-Use)

**Normalization:** "bike path," "bicycle path," "bike trail," "cycle path" → "Bicycling"

---

### Mountain Bike

**Definition:**
Trailthing specifically designed or designated for mountain biking —
typically singletrack or natural-surface.

**When to use:**
- ✅ Source explicitly designates as MTB or mountain bike trail
- ✅ Natural-surface singletrack documented as MTB by managing agency

**When NOT to use:**
- ❌ Paved bike paths (use Bicycling)
- ❌ General multi-use trail that permits mountain bikes

**Normalization:** "MTB trail," "mountain biking trail," "MTB" → "Mountain Bike"

---

### BMX

**Definition:**
Linear BMX trail (not a closed-loop BMX park).

**When to use:**
- ✅ Source explicitly documents as BMX trail
- ✅ Linear BMX route, not a park facility

**When NOT to use:**
- ❌ BMX parks (these are Sites, not Trailthings)
- ❌ Pump tracks (use Pump Track)

---

### Pump Track

**Definition:**
Documented pump track explicitly classified as a trail (linear route).

**When to use:**
- ✅ Source explicitly documents as pump track and classifies it as a trail
- ✅ Classified as a trail by the managing agency

**When NOT to use:**
- ❌ Pump track parks (these are Sites)
- ❌ Inferred from surface type or layout description

---

### Snowmobile

**Definition:**
Trailthing designated for snowmobile use.

**When to use:**
- ✅ Source explicitly documents snowmobile designation

---

### Cross Country Ski

**Definition:**
Trailthing designated for cross-country skiing.

**When to use:**
- ✅ Source explicitly documents XC ski designation

**Normalization:** "XC ski trail," "nordic trail," "cross-country ski trail,"
"nordic ski trail" → "Cross Country Ski"

---

### Other

**Definition:**
Named use type from authoritative source that doesn't fit any other category.

**Discovery guidance:**
Record raw term in identity_notes_raw. Flag for vocabulary expansion review.

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
Trailthing with asphalt, concrete, or chip-and-seal surface.

**Note:** Asphalt, concrete, and chip-and-seal are not separate values —
all map to "Paved."

**Normalization:** "asphalt," "concrete," "hard surface," "paved path,"
"chip-and-seal," "chip and seal," "paved asphalt" → "Paved"

---

### Crushed Stone

**Definition:**
Trailthing with compacted crushed stone, limestone screenings, or similar
fine aggregate surface.

**Normalization:** "crushed limestone," "stone dust," "limestone screenings,"
"compacted gravel," "fine gravel" → "Crushed Stone"

---

### Gravel

**Definition:**
Trailthing with loose gravel surface.

**Normalization:** "loose gravel," "gravel path" → "Gravel"

---

### Natural Surface

**Definition:**
Unpaved trail with dirt, soil, grass, or unimproved tread. Includes
primitive, rustic, and singletrack trails documented without a more
specific surface type.

**Note:** "Singletrack" is a width descriptor, not a surface type.
Map to Natural Surface unless a different surface is explicitly documented.

**Normalization:** "dirt trail," "earthen," "grass trail," "unimproved,"
"native surface," "primitive," "rustic," "primitive/rustic,"
"singletrack," "natural/singletrack," "natural/primitive" → "Natural Surface"

---

### Boardwalk

**Definition:**
Trailthing surface constructed of wood or composite decking.

**Normalization:** "wood deck," "elevated boardwalk," "wooden boardwalk" → "Boardwalk"

---

### Water

**Definition:**
Water trail — the surface is the waterway itself.

**When to use:**
- ✅ Use Type is also "Water"
- ✅ Route is on a waterway, not adjacent to one

---

### Mixed

**Definition:**
Trailthing with multiple documented surface types.

**When to use:**
- ✅ Source explicitly states "mixed surface" or documents multiple surface types

**When NOT to use:**
- ❌ You observe a mix without documentation

**Normalization:** "mixed surface," "varies" → "Mixed"

---

### Other

**Discovery guidance:**
Record raw term in identity_notes_raw. Flag for vocabulary expansion review.

------------------------------------------------------------
# 4. ORIGIN TYPE VOCABULARY (Controlled)

## 4.1 Allowed Values

- Rail Trail
- Canal Towpath
- Historic Route
- Greenway Corridor
- Purpose-Built
- Utility Corridor
- Roadside Corridor
- Waterway
- Other

------------------------------------------------------------
## 4.2 Definitions & Usage Rules

### Rail Trail

**Definition:**
Trailthing developed on a former railroad corridor.

**When to use:**
- ✅ Source explicitly documents rail trail history or former railroad right-of-way

**When NOT to use:**
- ❌ Trail near railroad tracks without a corridor conversion
- ❌ Inferred from linear alignment or grade

**Normalization:** "rails-to-trails," "former rail corridor," "railroad trail,"
"rail-trail" → "Rail Trail"

---

### Canal Towpath

**Definition:**
Trailthing on or adjacent to a historic canal towpath.

**Normalization:** "towpath," "canal trail," "canal path" → "Canal Towpath"

---

### Historic Route

**Definition:**
Trailthing following a documented historic route (pioneer, military,
native American, or similar).

**When to use:**
- ✅ Source explicitly documents a historic route designation

**When NOT to use:**
- ❌ Old trails without documented historic designation
- ❌ Inferred from age or character

---

### Greenway Corridor

**Definition:**
Trailthing that is part of a planned or documented greenway system.

**When to use:**
- ✅ Source explicitly documents greenway corridor designation

**When NOT to use:**
- ❌ Any trail through green space — not a sufficient basis
- ❌ Inferred from landscape character

---

### Purpose-Built

**Definition:**
Trailthing constructed specifically as a trail with no prior corridor
origin; or built by a governance entity on dedicated land with no
inherited corridor.

**Note:** Any "[governance entity]-built" pattern (e.g., "Village-built,"
"State-built," "City-built," "District-built") maps to "Purpose-Built."
The governance entity is already captured in the governance field.

**Normalization:** "purpose-built," "village-built," "state-built,"
"city-built," "district-built," "county-built," "township-built" → "Purpose-Built"

---

### Utility Corridor

**Definition:**
Trailthing built within a utility right-of-way (power line, pipeline, etc.).

**Normalization:** "power line trail," "powerline trail," "power line corridor,"
"pipeline trail," "pipeline corridor" → "Utility Corridor"

---

### Roadside Corridor

**Definition:**
Trailthing built along a road right-of-way.

**Normalization:** "road corridor," "highway trail," "roadside path" → "Roadside Corridor"

---

### Waterway

**Definition:**
Water trail — the corridor is the waterway itself.

**When to use:**
- ✅ Use Type is "Water"
- ✅ The route follows a river, stream, or other waterway

---

### Other

**Discovery guidance:**
Record raw term in identity_notes_raw. Flag for vocabulary expansion review.

------------------------------------------------------------
# 5. ORG TYPE VOCABULARY (Controlled)

## 5.1 Allowed Values

- Federal Agency
- State Agency
- Regional Authority
- County Authority
- Municipal Department
- Land Trust
- Nonprofit Conservancy
- Trail Association
- Coordinating Body
- Other

**Cross-module note:** These values are the canonical org_type vocabulary
for v6.x. When the Site Network Vocabulary Module v6.0 is written (IMP-003),
its org_type values must align with this list. Any additions or changes to
org_type values must be made in both modules simultaneously.

------------------------------------------------------------
## 5.2 Definitions & Usage Rules

**IMPORTANT:** Org Type is **descriptive only** for Trailthings. It carries
no threshold or identity-gate function. Do not use Org Type to decide
whether a Trailthing record should exist.

### Federal Agency

**Definition:**
Primary governance entity is a federal agency (National Park Service,
U.S. Forest Service, Army Corps of Engineers, Bureau of Land Management,
U.S. Fish & Wildlife Service, etc.).

**When to use:**
- ✅ A federal agency is the documented primary manager or coordinator

---

### State Agency

**Definition:**
Primary governance entity is a state agency (ODNR divisions, Ohio
Department of Transportation, state university system, etc.).

**When to use:**
- ✅ A state agency is the documented primary manager or coordinator

---

### Regional Authority

**Definition:**
Primary governance entity is a regional multi-county authority, metropark
district, or conservancy district with jurisdiction spanning multiple
counties or a defined multi-county service territory.

**When to use:**
- ✅ Metropark districts, regional park authorities, conservancy districts
- ✅ Multi-county trail coordinating authorities

---

### County Authority

**Definition:**
Primary governance entity is a county-level body — county park district,
county commissioners, county engineer, or county-level government agency.

---

### Municipal Department

**Definition:**
Primary governance entity is a city or village government department —
parks and recreation department, public works, or similar.

---

### Land Trust

**Definition:**
Primary governance entity is an accredited or documented land trust whose
mission includes land conservation and permanent protection.

---

### Nonprofit Conservancy

**Definition:**
Primary governance entity is a nonprofit conservation organization that
holds land or manages conservation property, but is not a formally
accredited land trust.

---

### Trail Association

**Definition:**
Primary governance entity is a nonprofit, volunteer, or membership-based
organization whose primary purpose is managing, maintaining, advocating
for, or coordinating a specific trail or trail system.

**Examples:** North Country Trail Association, Ohio to Erie Trail Fund,
friends-of-trail groups with documented management roles.

**When NOT to use:**
- ❌ A conservancy or land trust that also manages trails (use Land Trust
  or Nonprofit Conservancy)
- ❌ An informal volunteer group with no organizational standing

---

### Coordinating Body

**Definition:**
Primary governance entity is a multi-agency partnership, coordinating
committee, or coalition that does not hold land or have primary management
authority, but coordinates planning, development, or maintenance across
participating agencies.

**When to use:**
- ✅ Governance is documented as a partnership or coordinating committee
- ✅ No single agency has primary management authority

---

### Other

**Discovery guidance:**
Record the actual governance entity name in the governance field and
describe the organization type in identity_notes_raw. Flag for vocabulary
expansion review.

------------------------------------------------------------
# 6. STATUS VOCABULARY (Controlled)

## 6.1 Allowed Values

- Active
- Planned
- Under Development
- Under Construction
- Partially Open
- Gap
- Closed

**Note on Under Development vs. Under Construction:**
These are distinct concepts. "Under Development" applies to systems or
corridors still being assembled, planned, or funded — the concept exists
but the physical work is not yet underway or is early-stage. "Under
Construction" applies to physical trail construction actively in progress.

------------------------------------------------------------
## 6.2 Definitions & Usage Rules

### Active

**Definition:**
Trailthing is fully operational and open to the public.

**Discovery guidance:**
Can be left blank if obviously active — Active is the default for
documented open Trailthings.

**Normalization:** "open," "open to public," "operational" → "Active"

---

### Planned

**Definition:**
Trailthing is documented as planned or proposed but not yet under
development or construction.

**When to use:**
- ✅ Source explicitly documents as planned or proposed
- ✅ Appears in planning documents with no development yet underway

**When NOT to use:**
- ❌ Inferred from an incomplete member set or gap in a corridor
- ❌ Dotted lines on maps without authoritative documentation

**Normalization:** "proposed," "future," "future trail" → "Planned"

---

### Under Development

**Definition:**
Trailthing is being actively developed, funded, or assembled as a
system — the concept and some components may exist but the full
entity is not yet operational.

**When to use:**
- ✅ Source explicitly states under development
- ✅ System is actively growing with documented plans and partial components
- ✅ Applies more to system-level Trailthings than to individual trail corridors

**When NOT to use:**
- ❌ Assumed from an incomplete member set without documentation
- ❌ Any system that might grow in the future

**Normalization:** "in development," "being developed," "under development" → "Under Development"

---

### Under Construction

**Definition:**
Physical trail construction is actively in progress.

**When to use:**
- ✅ Source explicitly states under construction or being built

**When NOT to use:**
- ❌ Planning phase only — use Planned or Under Development

**Normalization:** "under construction," "in construction," "being built,"
"construction underway" → "Under Construction"

---

### Partially Open

**Definition:**
Trailthing has some portions open and operational but significant
portions are not yet complete or accessible.

**When to use:**
- ✅ Source explicitly documents partial opening
- ✅ Managing agency describes the trail or system as partially open

**When NOT to use:**
- ❌ Inferred from knowing some sections exist and others don't
- ❌ Minor restrictions or temporary closures (use Active + Notes)

**Normalization:** "partially open," "partially complete,"
"some sections open" → "Partially Open"

---

### Gap

**Definition:**
A missing or incomplete section of an otherwise continuous trail
corridor that is the defining characteristic of the Trailthing's
current state.

**When to use:**
- ✅ Source explicitly identifies a gap in a trail corridor
- ✅ A specific Trailthing exists primarily to document a missing link

**When NOT to use:**
- ❌ A system with some members not yet built — use Partially Open
- ❌ Minor gaps — document in Notes and use Active or Partially Open

---

### Closed

**Definition:**
Trailthing is permanently or indefinitely closed.

**When to use:**
- ✅ Explicitly documented as permanently closed or decommissioned

**When NOT to use:**
- ❌ Temporary closures (use Notes)
- ❌ Seasonal closures (use Notes)

**Normalization:** "permanently closed," "decommissioned,"
"permanent closure" → "Closed"

------------------------------------------------------------
# 7. DIFFICULTY VOCABULARY (Controlled)

## 7.1 Allowed Values

- Easy
- Moderate
- Difficult
- Strenuous
- Expert

------------------------------------------------------------
## 7.2 Definitions & Usage Rules

### Easy

**Definition:**
Trailthing suitable for beginners; minimal elevation change, good surface.

**When to use:**
- ✅ Source explicitly rates as Easy

**When NOT to use:**
- ❌ Looks easy — never self-assess
- ❌ Paved surface — never infer from surface type

**Normalization:** "beginner," "beginning" → "Easy"

---

### Moderate

**Definition:**
Trailthing suitable for average users; some elevation change or challenge.

**When to use:**
- ✅ Source explicitly rates as Moderate

**Normalization:** "intermediate" → "Moderate"

---

### Difficult

**Definition:**
Trailthing with significant elevation change, challenging terrain, or
technical features requiring experienced users.

**When to use:**
- ✅ Source explicitly rates as Difficult or Hard

**Normalization:** "hard," "challenging," "advanced" → "Difficult"
(verify context — only map when used as a difficulty rating in a
managed trail system, not as casual description)

---

### Strenuous

**Definition:**
Trailthing requiring high physical exertion; significant elevation
gain or length.

**When to use:**
- ✅ Source explicitly rates as Strenuous

---

### Expert

**Definition:**
Trailthing suitable only for expert users; highly technical or hazardous.

**When to use:**
- ✅ Source explicitly rates as Expert or uses Black Diamond designation

**Normalization:** "black diamond," "expert only," "expert-only" → "Expert"
"technical" → "Expert" (verify context; in MTB trail-rating context only)

------------------------------------------------------------
## 7.3 Critical Usage Rules for Difficulty

**DO:**
- ✅ Record only what authoritative sources explicitly state
- ✅ Leave blank if not documented by the managing agency or authoritative source
- ✅ Capture raw value during discovery; normalize during normalization

**DON'T:**
- ❌ Assess difficulty yourself — ever
- ❌ Infer from terrain, length, or surface type
- ❌ Apply a difficulty rating from a third-party review site unless it
  is the only documented rating and it comes from the managing agency

------------------------------------------------------------
# 8. ACCESSIBILITY (Free-Text — No Controlled Vocabulary)

## 8.1 Overview

Accessibility is a free-text field. There is no controlled vocabulary.

## 8.2 What to Collect

- ADA compliance statements
- Wheelchair accessibility descriptions
- Surface grade and width information
- Accessible facility descriptions
- Only when explicitly documented by an authoritative source

**Examples:**
- "ADA accessible from Main Street trailhead; paved surface, grades under 5%"
- "Wheelchair accessible for first 0.5 miles from north trailhead"
- "Not ADA compliant; natural surface with variable grades"

## 8.3 What NOT to Collect

- ❌ Inferred accessibility from surface type alone
- ❌ Personal assessments
- ❌ Accessibility information from non-authoritative user reviews

------------------------------------------------------------
# 9. SOURCE TERM AND SOURCE HIERARCHY CONTEXT
(Free-Text — No Controlled Vocabulary)

## 9.1 Overview

Both fields are **free text with no controlled vocabulary**. Do not
normalize, map, or translate source vocabulary into project terminology.
The value of these fields depends entirely on verbatim capture.

## 9.2 Source Term — What to Capture

Source Term captures the exact word or phrase the authoritative source
uses to describe what kind of entity this Trailthing is.

**Good capture (verbatim):**
- "regional trail system"
- "greenway"
- "water trail network"
- "connector trail"
- "spur trail"
- "loop trail"
- "blueway"
- "trail hub"
- "route"
- "heritage corridor trail"
- "section"
- "reach"
- "multi-use path"

**Bad capture (normalized/interpreted):**
- "Trail Network" ← this is project terminology, not source vocabulary
- "Trail" ← too generic; capture what the source actually calls it
- "trail system" ← acceptable only if the source actually says "trail system"
- "multi-use trail" ← acceptable only if the source says exactly this

**When to leave blank:**
Only when the source provides no descriptive term for the entity type at all
(e.g., a trail listed only by name on a park map with no type label).

## 9.3 Source Hierarchy Context — What to Capture

Source Hierarchy Context captures how the authoritative source frames this
entity in relation to other entities — its described position in a system,
network, or hierarchy.

**Good capture (verbatim or close paraphrase):**
- "Part of the Great Ohio Lake-to-River Greenway"
- "One of seven member trails in the X Water Trail Network"
- "The eastern section of the Y Trail"
- "Connecting A State Park to B State Nature Preserve"
- "A segment of the North Country National Scenic Trail"
- "The northern reach of the Z Blueway"

**Bad capture (interpreted/classified):**
- "This is a member trail" ← that's your classification, not the source's words
- "Parent is X Trail Network" ← that's a schema relationship, not source text

**When to leave blank:**
When the source provides no language about how this entity relates to
other trail entities.

## 9.4 Why These Fields Matter

The source_term and source_hierarchy_context fields, populated consistently
across many Trailthings and county runs, will provide the empirical basis
for the eventual Trailthing hierarchy classification decisions (IMP-007,
target: after 30 v6 county runs). Poor capture — normalized or interpreted
values instead of verbatim source vocabulary — will degrade the quality of
that analysis.

------------------------------------------------------------
# 10. OWNERSHIP (Free-Text — No Controlled Vocabulary)

## 10.1 Overview

Ownership is a free-text field. There is no controlled vocabulary.

## 10.2 What to Collect

- Legal name of the owning entity when a single agency or organization
  owns the trail corridor or right-of-way
- Only when explicitly documented by an authoritative source

**Examples:**
- "Ohio Department of Natural Resources"
- "Wood County Park District"
- "North Country Trail Association"
- "Norfolk Southern Corporation" (for rail corridor easements)

## 10.3 What NOT to Collect

- ❌ Managing or governing agencies (those go in Governance / Partner Agencies)
- ❌ Inferred ownership from governance
- ❌ Generic descriptions like "Multiple Agencies"

## 10.4 When to Leave Blank

Blank when:
- Ownership is distributed across multiple agencies or landowners
- The Trailthing is a coordinating or designating body without land ownership
- The corridor crosses multiple ownership parcels
- Ownership is unclear or undocumented

**Blank is correct and common** — many trail corridors cross multiple
ownership parcels, and many trail systems are coordinating bodies rather
than land owners.

------------------------------------------------------------
# 11. IDENTITY NOTES (Free-Text — No Controlled Vocabulary)

## 11.1 Overview

Identity Notes is a free-text field. There is no controlled vocabulary.

## 11.2 Flags Used in Identity Notes

**TRAIL_HIERARCHY_UNCERTAIN** — use when source framing is ambiguous about
whether this Trailthing is a system-level entity, a navigable trail, or a
component:
```
TRAIL_HIERARCHY_UNCERTAIN — [description of specific ambiguity and source evidence]
```

**PARTIAL MEMBERSHIP** — for multi-county Trailthings where not all child
Trailthings have been documented:
```
PARTIAL MEMBERSHIP: Only [County] County child Trailthings documented
as of [date]. Additional members expected from [County2], [County3] sessions.
```

**CROSS_COUNTY_CANDIDATE** — for Trailthings whose counties_raw lists
more than one county, per IMP-104.

## 11.3 Discovery vs. Normalization

- **Discovery stage**: capture in `identity_notes_raw`
- **Normalized stage**: surfaced as `identity_notes` field

------------------------------------------------------------
# 12. VOCABULARY NORMALIZATION RULES — ENFORCEMENT

The Normalization Engine must apply the mapping tables in this section to
every controlled Trailthing field. Out-of-vocabulary raw values must be
mapped or nulled per the rules below; they must never silently pass through
to normalized output or TSV.

**Enforcement model:**
- All vocabulary-controlled Trailthing fields are optional (blanks are valid).
  Out-of-vocabulary values that cannot be mapped → **null-and-log**.
- "Null-and-log": set the field to blank, preserve the raw value in
  identity_notes (append a vocabulary flag), write the decision to
  normalization_provenance.
- **REVIEW** items require the normalization engine to surface the entity for
  human resolution before proceeding.
- Empty strings ("") are data defects — see §12.7.

------------------------------------------------------------
## 12.1 Use Type Normalization Mapping

| Raw / Out-of-Vocabulary Value | Maps To | Resolution Method |
|-------------------------------|---------|-------------------|
| "foot" / "foot travel" / "walking" | Multi-Use or Hiking | If source documents single use → Hiking. If multiple uses → Multi-Use. |
| "pedestrian" / "pedestrian trail" / "footpath" | "Hiking" | Standard synonyms. |
| "nature trail" / "walking trail" | "Hiking" | Standard synonyms. |
| "equestrian" / "equestrian trail" / "horse trail" | "Bridle" | Standard synonyms. |
| "paddling" / "paddling trail" / "canoe trail" / "kayak trail" | "Water" | Standard synonyms. |
| "blueway" / "water route" / "paddling route" | "Water" | Standard synonyms. |
| "bike path" / "bicycle path" / "bike trail" / "cycle path" | "Bicycling" | Standard synonyms. |
| "MTB" / "MTB trail" / "mountain biking trail" | "Mountain Bike" | Standard synonyms. |
| "snowmobile trail" / "snowmobile route" | "Snowmobile" | Standard synonyms. |
| "XC ski" / "XC ski trail" / "nordic trail" / "cross-country ski trail" | "Cross Country Ski" | Standard synonyms. |
| "multi-purpose" / "multipurpose" / "shared use" / "shared-use" | "Multi-Use" | Standard synonyms. |
| Compound values (e.g., "Foot;Bike", "Hiking/Biking") | **REVIEW** | Single-value field. If source documents "multi-use" → map to Multi-Use. If ambiguous → null-and-log; record raw in identity_notes. |
| Any value not in §2.1 and not in this table | **null-and-log** | Flag "use_type OOV: [value]" in normalization_provenance. |

---

## 12.2 Surface Type Normalization Mapping

| Raw / Out-of-Vocabulary Value | Maps To | Resolution Method |
|-------------------------------|---------|-------------------|
| "asphalt" / "concrete" / "hard surface" / "paved path" / "paved asphalt" | "Paved" | Standard synonyms. |
| "chip-and-seal" / "chip and seal" | "Paved" | Surface treatment; maps to Paved. |
| "crushed limestone" / "limestone screenings" / "stone dust" / "compacted gravel" / "fine gravel" | "Crushed Stone" | Standard synonyms. |
| "loose gravel" / "gravel path" | "Gravel" | Standard synonyms. |
| "dirt" / "dirt trail" / "earthen" / "soil" / "grass trail" / "unimproved" / "native surface" | "Natural Surface" | Standard synonyms. |
| "primitive" / "rustic" / "primitive/rustic" | "Natural Surface" | Unpaved minimal-improvement surfaces. |
| "singletrack" | "Natural Surface" | Width descriptor, not surface type. |
| "natural/singletrack" / "natural/primitive" | "Natural Surface" | Both components indicate natural surface. |
| "wood deck" / "elevated boardwalk" / "wooden boardwalk" | "Boardwalk" | Standard synonyms. |
| "mixed surface" / "varies" | "Mixed" | Only when documented, not inferred. |
| Compound with "/" where components differ (e.g., "Gravel/Chip-and-seal") | **REVIEW** | If source supports multiple surfaces → map to "Mixed". If ambiguous → null-and-log; record both raw terms in identity_notes. |
| Any value not in §3.1 and not in this table | **null-and-log** | Flag "surface_type OOV: [value]" in normalization_provenance. |

---

## 12.3 Origin Type Normalization Mapping

| Raw / Out-of-Vocabulary Value | Maps To | Resolution Method |
|-------------------------------|---------|-------------------|
| "rails-to-trails" / "railroad trail" / "former rail corridor" / "rail-trail" | "Rail Trail" | Standard synonyms. |
| "towpath" / "canal trail" / "canal path" | "Canal Towpath" | Standard synonyms. |
| "power line trail" / "powerline trail" / "pipeline trail" / "pipeline corridor" | "Utility Corridor" | Standard synonyms. |
| "road corridor" / "roadside path" / "highway trail" | "Roadside Corridor" | Standard synonyms. |
| "village-built" / "state-built" / "city-built" / "district-built" / "county-built" / "township-built" | "Purpose-Built" | Governance-built pattern; governance is in governance field. |
| "purpose-built" | "Purpose-Built" | Case normalization. |
| "natural" | **null-and-log** | Describes surface/ecology, not origin. Strip; log. |
| "wildlife area trail" | **null-and-log** | Describes governance context, not origin. Strip; log. |
| "water route" / "waterway" | "Waterway" | Standard synonyms. |
| Any value not in §4.1 and not in this table | **null-and-log** | Flag "origin_type OOV: [value]" for vocabulary expansion review. |

---

## 12.4 Org Type Normalization Mapping

Org Type is captured from governance documentation during discovery. The
raw governance name goes in governance_raw; org_type_raw captures the
organizational category when documented or clearly determinable.

| Raw / Out-of-Vocabulary Value | Maps To | Resolution Method |
|-------------------------------|---------|-------------------|
| "national park service" / "NPS" / "US forest service" / "USFS" / "army corps" / "BLM" / "USFWS" | "Federal Agency" | Standard synonyms. |
| "ODNR" / "Ohio Department of Natural Resources" / "state park" / "state forest" / "Ohio Division of Wildlife" | "State Agency" | Standard synonyms. |
| "metropark" / "metro park" / "conservancy district" / "regional park authority" | "Regional Authority" | Standard synonyms. |
| "county park district" / "county parks" / "county park" / "county commissioner" | "County Authority" | Standard synonyms. |
| "city parks" / "parks and recreation" / "municipal parks" / "parks department" | "Municipal Department" | Standard synonyms. |
| "land trust" / "land conservancy" (when accredited/land-holding) | "Land Trust" | Verify land-holding mission. |
| "conservancy" / "nonprofit" / "foundation" (when primary manager, not land trust) | "Nonprofit Conservancy" | Standard synonyms. |
| "trail association" / "trail club" / "friends of [trail]" (when managing role) | "Trail Association" | Standard synonyms. |
| "coordinating committee" / "partnership" / "coalition" / "consortium" | "Coordinating Body" | Standard synonyms. |
| Any value not in §5.1 and not in this table | **null-and-log** | Flag "org_type OOV: [value]"; leave blank rather than guess. |

---

## 12.5 Status Normalization Mapping

| Raw / Out-of-Vocabulary Value | Maps To | Resolution Method |
|-------------------------------|---------|-------------------|
| "open" / "open to public" / "operational" / "active" | "Active" | Standard synonyms. |
| "proposed" / "future" / "future trail" | "Planned" | Standard synonyms. |
| "in development" / "under development" / "being developed" | "Under Development" | Standard synonyms. |
| "under construction" / "in construction" / "being built" / "construction underway" | "Under Construction" | Standard synonyms. |
| "partially open" / "partially complete" / "some sections open" | "Partially Open" | Standard synonyms. |
| "permanently closed" / "decommissioned" / "permanent closure" | "Closed" | Standard synonyms. |
| "open/partial" | **REVIEW** | Context-dependent: if a missing section is the defining characteristic → "Gap"; if mostly open with minor restriction → "Active" + Note; if significant portions incomplete → "Partially Open". Surface for human resolution. |
| "incomplete" | **REVIEW** | Could be Under Development, Partially Open, or Gap. Check source for context. |
| Empty string ("") | null | See §12.7. |
| Any value not in §6.1 and not in this table | **null-and-log** | Leave blank; log "status OOV: [value]". |

---

## 12.6 Difficulty Normalization Mapping

Difficulty must never be inferred. Apply this table only to values
captured from explicit authoritative source ratings.

| Raw / Out-of-Vocabulary Value | Maps To | Resolution Method |
|-------------------------------|---------|-------------------|
| "beginner" / "beginning" | "Easy" | Standard synonyms. |
| "intermediate" | "Moderate" | Standard synonym. |
| "hard" / "advanced" / "challenging" | "Difficult" | Verify context before mapping — only when used as a managed difficulty rating. |
| "expert only" / "expert-only" / "black diamond" | "Expert" | Standard synonyms. |
| "technical" | "Expert" | MTB/trail-rating context only; verify. |
| "varies" / "variable" | **null-and-log** | Not a valid difficulty value. Document source range in Notes. |
| Compound values (e.g., "Easy-Moderate", "Easy to Difficult") | **null-and-log** | Single-value field. Document source range in Notes: "Source rates difficulty as [raw value]." |
| Empty string ("") | null | See §12.7. |
| Any value not in §7.1 and not in this table | **null-and-log** | Leave blank; log "difficulty OOV: [value]". |

---

## 12.7 Multi-Value and Empty String Enforcement

### Single-Value Requirement

All six vocabulary-controlled Trailthing fields are single-value:

| Field | Single-Value | Multi-value prohibited |
|-------|--------------|------------------------|
| `use_type` | ✅ | "Foot;Bike", "Hiking/Biking" are never valid |
| `surface_type` | ✅ | "Paved/Gravel" is never valid (use "Mixed" if documented) |
| `origin_type` | ✅ | No compound origin types |
| `org_type` | ✅ | One organizational category per Trailthing |
| `status` | ✅ | "Open/Partial" is never valid (see §12.5 REVIEW) |
| `difficulty` | ✅ | "Easy-Moderate", "Easy to Difficult" are never valid |

When a compound value appears in any controlled field and cannot be
resolved to a single canonical value:
1. Set the field to blank
2. Append to identity_notes: "field_name compound value: '[raw]' — could not resolve to single term; flagged for review"
3. Write raw value to normalization_provenance as "compound_value_stripped"

### Empty String Enforcement

An empty string ("") is not a valid blank in any vocabulary-controlled
field. An empty string is a data defect, not a documented absence.

After mapping table application: if the result is an empty string →
convert to null. Log: "field [name]: empty string converted to null."

------------------------------------------------------------
# 13. VOCABULARY USAGE RULES

## 13.1 Universal Rules

1. **Use exactly as written** — No synonyms, abbreviations, or invented terms
2. **Don't infer** — Values must be documented, not inferred from context or geometry
3. **Leave blank if unclear** — Better no value than wrong value
4. **One value per field** — No multi-value controlled fields
5. **Flag new values** — Do not add values; flag for vocabulary expansion

## 13.2 Discovery Phase

- Capture raw values exactly as found in `_raw` fields
- Do not attempt normalization during discovery
- Capture source_term and source_hierarchy_context verbatim (§9)
- Capture identity clarifications in identity_notes_raw

## 13.3 Normalization Phase

- Apply §12.x mapping tables to all vocabulary-controlled fields
- Handle compound values per §12.7
- Convert empty strings to null per §12.7
- Null-and-log all unmappable values
- Surface REVIEW items for human resolution before TSV output

------------------------------------------------------------
# 14. MODULE DEPENDENCIES

This vocabulary module integrates with:

- Trailthing Schema Module v6.0 (field definitions)
- Trailthing Discovery Sub-Procedure v6.x (raw capture)
- Resolution Engine v6.x (conflict detection)
- Normalization Engine v6.x (vocabulary mapping)
- Trailthing Normalization Contract v6.x (normalization rules)
- Trailthing TSV Output Specification v6.x (output format)

------------------------------------------------------------
# END OF TRAILTHING VOCABULARY MODULE v6.0
