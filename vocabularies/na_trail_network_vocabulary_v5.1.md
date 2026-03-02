# NATURAL AREAS PROJECT
# TRAIL NETWORK VOCABULARY MODULE v5.1
(Authoritative Controlled Vocabularies for Trail Network Fields)

This module contains all controlled vocabularies for Trail Network
entities in the Natural Areas Project v5.x.

All Trail Network-related modules must reference this module for
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

- Status vocabulary added (was missing from v4.0)
- Ownership field added (free-text, no controlled vocabulary)
- Enhanced definitions and normalization mappings

------------------------------------------------------------
# 1. PURPOSE

This module defines the authoritative controlled vocabularies for:
- Network Type
- Status

And provides field guidance for free-text fields:
- Ownership (no controlled vocabulary)
- Identity Notes (no controlled vocabulary)
- Notes (no controlled vocabulary)

These vocabularies are used across:
- Trail Network Discovery Sub-Procedure v5.x (raw capture)
- Resolution Engine v5.x (conflict detection)
- Normalization Engine v5.x (vocabulary mapping)
- Trail Network TSV Output Specification v5.x (output format)

**Key Principle:** Vocabularies are DESCRIPTIVE, not PRESCRIPTIVE.
- Values describe what authoritative sources document
- Values are not inferred from member count, geography, or governance
- If no documented value matches, leave field blank

------------------------------------------------------------
# 2. NETWORK TYPE VOCABULARY (Controlled)

## 2.1 Allowed Values

- Regional Greenway System
- National Scenic Trail System
- Water Trail Network
- Statewide Trail System
- County Trail Network
- Municipal Trail Network
- Multi-Jurisdictional Trail Network
- Other

------------------------------------------------------------
## 2.2 Definitions & Usage Rules

### Regional Greenway System

**Definition:**
A planned or documented greenway system spanning multiple
jurisdictions within a region.

**When to use:**
- ✅ Source explicitly documents as a regional greenway system
- ✅ Multi-jurisdiction greenway with formal identity

**When NOT to use:**
- ❌ Single-jurisdiction trail systems (use County or Municipal
  Trail Network)
- ❌ Inferred from geographic extent alone

**Normalization:**
- "regional greenway", "greenway system",
  "greenway network" → "Regional Greenway System"

---

### National Scenic Trail System

**Definition:**
A federally designated National Scenic Trail and its formal
system of member trails.

**When to use:**
- ✅ Federally designated National Scenic Trail
- ✅ The formal network/system associated with an NST designation

**When NOT to use:**
- ❌ State scenic trails without federal designation
- ❌ Trails that connect to an NST without formal membership

**Normalization:**
- "national scenic trail", "NST system" →
  "National Scenic Trail System"

---

### Water Trail Network

**Definition:**
A documented network of water-based trail routes.

**When to use:**
- ✅ Source explicitly documents as a water trail network or
  paddling trail system
- ✅ Formal network of two or more water trails

**When NOT to use:**
- ❌ A single water trail (that's a Trail entity, not a network)
- ❌ Inferred from presence of water trails

**Normalization:**
- "paddling trail network", "blueway network",
  "water trail system" → "Water Trail Network"

---

### Statewide Trail System

**Definition:**
A formally recognized trail system with statewide scope and
identity.

**When to use:**
- ✅ Explicitly documented as a statewide system by the managing
  or designating authority

**When NOT to use:**
- ❌ Inferred from geographic extent spanning the state
- ❌ State-managed trail that doesn't constitute a formal system

---

### County Trail Network

**Definition:**
A formally documented trail network at the county level.

**When to use:**
- ✅ Explicitly documented as a county trail network or system
- ✅ County agency formally identifies the collection as a network

**When NOT to use:**
- ❌ Inferred from a county owning multiple trails
- ❌ Collection of trails without formal network identity

---

### Municipal Trail Network

**Definition:**
A formally documented trail network at the municipal level
(city or village).

**When to use:**
- ✅ Explicitly documented as a municipal trail network or system
- ✅ City or village formally identifies the collection as a
  network

**When NOT to use:**
- ❌ Inferred from a municipality owning multiple trails
- ❌ Collection without formal network identity

---

### Multi-Jurisdictional Trail Network

**Definition:**
A formally recognized trail network spanning multiple agencies
or jurisdictions, not fitting a more specific category.

**When to use:**
- ✅ Source explicitly documents as multi-jurisdictional
- ✅ Doesn't qualify as Regional Greenway System, National Scenic
  Trail System, or Statewide Trail System

**When NOT to use:**
- ❌ Inferred from number of participating agencies
- ❌ When a more specific type applies

---

### Other

**Definition:**
Named network type from authoritative source that doesn't fit
any other category.

**Discovery guidance:**
Record raw term in identity_notes_raw. Flag for vocabulary
expansion review.

------------------------------------------------------------
# 3. STATUS VOCABULARY (Controlled)

## 3.1 Allowed Values

- Active
- Planned
- Under Development
- Partially Open
- Closed

------------------------------------------------------------
## 3.2 Definitions & Usage Rules

### Active

**Definition:**
Trail network is fully operational and open to the public.

**When to use:**
- ✅ Explicitly documented as active or open
- ✅ Default when no restrictions or development status documented

**Discovery guidance:**
Can be left blank if obviously active.

---

### Planned

**Definition:**
Trail network is documented as planned but not yet developed.

**When to use:**
- ✅ Source explicitly documents as planned or proposed
- ✅ Network appears in planning documents but no member trails
  exist yet

**When NOT to use:**
- ❌ Inferred from incomplete member trail set

---

### Under Development

**Definition:**
Trail network is actively being built or expanded; some member
trails may be open.

**When to use:**
- ✅ Source explicitly states under development or under
  construction
- ✅ Network is growing with documented active expansion

**When NOT to use:**
- ❌ Assumed from incomplete member set
- ❌ Any network that might grow in the future

---

### Partially Open

**Definition:**
Trail network has some member trails open but significant
portions are not yet complete or accessible.

**When to use:**
- ✅ Source explicitly documents partial opening
- ✅ Managing agency describes network as partially open or
  incomplete

**When NOT to use:**
- ❌ Inferred from knowing some trails are open and some aren't
- ❌ Networks with minor gaps (use Active + Notes)

---

### Closed

**Definition:**
Trail network is permanently or indefinitely closed.

**When to use:**
- ✅ Explicitly documented as permanently closed or decommissioned

**When NOT to use:**
- ❌ Temporary closures (use Notes)
- ❌ Seasonal closures (use Notes)

------------------------------------------------------------
# 4. OWNERSHIP (Free-Text — No Controlled Vocabulary)

## 4.1 Overview

**Ownership is a free-text field — there is no controlled
vocabulary.**

## 4.2 What to Collect

- Name of the owning entity when a single agency or organization
  owns the network
- Only when explicitly documented

**Examples:**
- "Ohio Department of Natural Resources"
- "Wood County Park District"
- "North Country Trail Association"

## 4.3 What NOT to Collect

- ❌ Governing or managing agencies (those go in Governance /
  Partner Agencies)
- ❌ Inferred ownership from governance
- ❌ Generic descriptions like "Multiple Agencies"

## 4.4 When to Leave Blank

Leave blank when:
- Ownership is distributed across multiple agencies
- Network is a coordinating body without land ownership
- Ownership is unclear or undocumented

**Blank is correct and common** — many trail networks are
coordinating or designating bodies rather than land owners.

------------------------------------------------------------
# 5. IDENTITY NOTES (Free-Text — No Controlled Vocabulary)

## 5.1 Overview

**Identity Notes is a free-text field — there is no controlled
vocabulary.**

## 5.2 What to Capture

- Network vs. trail boundary questions (is this a Trail or a
  Trail Network?)
- Name conflicts or ambiguities
- Membership uncertainty
- Vocabulary type flags (e.g., "source calls this a 'trail
  corridor' — unclear if Trail or Trail Network")

## 5.3 Discovery vs. Normalization

- **Discovery stage**: capture in `identity_notes_raw`
- **Normalized stage**: surfaced as `identity_notes` field

------------------------------------------------------------
# 6. VOCABULARY NORMALIZATION RULES

## 6.1 Common Mappings

**Network Type:**
```
Raw Value                          → Normalized Value
----------                           ----------------
"regional greenway"                → Regional Greenway System
"greenway network"                 → Regional Greenway System
"national scenic trail"            → National Scenic Trail System
"NST system"                       → National Scenic Trail System
"paddling trail network"           → Water Trail Network
"blueway network"                  → Water Trail Network
"statewide trail system"           → Statewide Trail System
"county trail system"              → County Trail Network
"city trail network"               → Municipal Trail Network
"multi-agency trail network"       → Multi-Jurisdictional Trail Network
```

**Status:**
```
Raw Value                          → Normalized Value
----------                           ----------------
"open"                             → Active
"operational"                      → Active
"proposed"                         → Planned
"in development"                   → Under Development
"under construction"               → Under Development
"partially complete"               → Partially Open
"some sections open"               → Partially Open
"permanently closed"               → Closed
"decommissioned"                   → Closed
```

## 6.2 Ambiguous Cases

**Require context or manual review:**
- "greenway" alone — could be Regional Greenway System or just
  a description
- "trail system" — could be Statewide, County, Municipal, or
  Multi-Jurisdictional
- "incomplete" — could be Under Development or Partially Open
- "closed" — permanent or temporary?

**Resolution:**
- Check source context
- Prefer more specific term when context supports it
- Leave blank rather than guess
- Flag in identity_notes if confidence is low

------------------------------------------------------------
# 7. VOCABULARY USAGE RULES

## 7.1 Universal Rules

1. **Use exactly as written** — No synonyms, abbreviations, or
   invented terms
2. **Don't infer** — Values must be documented
3. **Leave blank if unclear** — Better no value than wrong value
4. **One value per field** — No multi-value types
5. **Flag new values** — Don't add values; flag for vocabulary
   expansion

------------------------------------------------------------
# 8. VOCABULARY VERSIONING

## 8.1 Version History

**v5.1:**
- Cross-module references updated to v5.x
- identity_notes field guidance added
- Maps field guidance updated (URL list, no type/description
  metadata)
- "Other" guidance updated to reference identity_notes_raw

**v5.0:**
- Status vocabulary added (5 values)
- Ownership field guidance added (free-text)
- Enhanced Network Type definitions and normalization mappings

**v4.0:**
- Initial controlled vocabulary
- Network Type defined

------------------------------------------------------------
# 9. INTEGRATION POINTS

This vocabulary module integrates with:

- **Trail Network Schema Module v5.x** (field definitions)
- **Trail Network Discovery Sub-Procedure v5.x** (raw capture)
- **Resolution Engine v5.x** (conflict detection)
- **Normalization Engine v5.x** (vocabulary mapping)
- **Trail Network Normalization Contract v5.x** (normalization)
- **Trail Network TSV Output Specification v5.x** (output format)

------------------------------------------------------------
# END OF TRAIL NETWORK VOCABULARY MODULE v5.1
