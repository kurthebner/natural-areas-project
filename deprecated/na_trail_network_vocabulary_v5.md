# NATURAL AREAS PROJECT
# TRAIL NETWORK VOCABULARY MODULE v5.0
(Authoritative Controlled Vocabularies for Trail Network Fields)

This module contains all controlled vocabularies for Trail Network entities
in the Natural Areas Project v5.0.

All Trail Network-related modules must reference this module for vocabulary authority.

------------------------------------------------------------
# CHANGES FROM v4.0

- **Status vocabulary added** ✨ NEW — was missing from v4.0, clearly needed
- **Ownership field added** ✨ NEW — free-text, no controlled vocabulary
- Updated to v5.0 references
- Enhanced definitions, usage rules, and normalization mappings
- Added discovery vs. normalization guidance per v5.0 philosophy

------------------------------------------------------------
# 1. PURPOSE

This module defines the authoritative controlled vocabularies for:
- Network Type
- Status ✨ NEW IN v5.0
- Ownership ✨ NEW IN v5.0 (free-text, no controlled vocabulary)

These vocabularies are used across:
- Trail Network Discovery Sub-Procedure v5.0 (raw capture)
- Resolution Engine v5.0 (conflict detection)
- Normalization Engine v5.0 (vocabulary mapping)
- TSV Output Specification v5.0 (output format)

**Key Principle:** Vocabularies are DESCRIPTIVE, not PRESCRIPTIVE.
- Values describe what authoritative sources document
- Values are not inferred from geometry, member count, or governance structure
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
A planned or documented greenway system spanning multiple jurisdictions within a region.

**When to use:**
- ✅ Source explicitly documents as a regional greenway system
- ✅ Multi-jurisdiction greenway with formal identity

**When NOT to use:**
- ❌ Single-jurisdiction trail systems (use County or Municipal Trail Network)
- ❌ Inferred from geographic extent alone
- ❌ Any trail that passes through a greenway

**Normalization:**
- "regional greenway", "greenway system", "greenway network" → "Regional Greenway System"

---

### National Scenic Trail System

**Definition:**
A federally designated National Scenic Trail and its formal system of member trails.

**When to use:**
- ✅ Federally designated National Scenic Trail (e.g., North Country Trail, Appalachian Trail)
- ✅ The formal network/system associated with an NST designation

**When NOT to use:**
- ❌ State scenic trails without federal designation
- ❌ Trails that connect to an NST but aren't part of its formal system
- ❌ Inferred from trail name containing "scenic"

---

### Water Trail Network

**Definition:**
A documented network of water-based trail routes.

**When to use:**
- ✅ Source explicitly documents as a water trail network or paddling trail system
- ✅ Formal network of water trails

**When NOT to use:**
- ❌ A single water trail (that's a Trail entity, not a network)
- ❌ Inferred from presence of water trails

**Normalization:**
- "paddling trail network", "blueway network", "water trail system" → "Water Trail Network"

---

### Statewide Trail System

**Definition:**
A formally recognized trail system with statewide scope and identity.

**When to use:**
- ✅ Explicitly documented as a statewide system by the managing or designating authority
- ✅ Formal statewide recognition (e.g., Ohio's statewide trail systems)

**When NOT to use:**
- ❌ Inferred from geographic extent spanning the state
- ❌ State-managed trail that doesn't constitute a formal system

---

### County Trail Network

**Definition:**
A formally documented trail network at the county level.

**When to use:**
- ✅ Explicitly documented as a county trail network or system
- ✅ County park district or county agency formally identifies the collection as a network

**When NOT to use:**
- ❌ Inferred from a county owning multiple trails
- ❌ Collection of trails within a county without formal network identity

---

### Municipal Trail Network

**Definition:**
A formally documented trail network at the municipal level (city or village).

**When to use:**
- ✅ Explicitly documented as a municipal trail network or system
- ✅ City or village formally identifies the collection as a network

**When NOT to use:**
- ❌ Inferred from a municipality owning multiple trails
- ❌ Collection of trails within a municipality without formal network identity

---

### Multi-Jurisdictional Trail Network

**Definition:**
A formally recognized trail network spanning multiple agencies or jurisdictions, not fitting a more specific category.

**When to use:**
- ✅ Source explicitly documents as multi-jurisdictional
- ✅ Spans multiple agencies or jurisdictions with formal network identity
- ✅ Doesn't qualify as Regional Greenway System, National Scenic Trail System, or Statewide Trail System

**When NOT to use:**
- ❌ Inferred from number of participating agencies
- ❌ When a more specific type applies

---

### Other

**Definition:**
Named network type from authoritative source that doesn't fit any other category.

**When to use:**
- ✅ Source provides a specific network type that doesn't match vocabulary
- ✅ Is a legitimate, documented network type

**When NOT to use:**
- ❌ Invented categories
- ❌ Inferred types

**Discovery guidance:**
Record raw term exactly in notes. Flag for vocabulary expansion review.

------------------------------------------------------------
# 3. STATUS VOCABULARY (Controlled) ✨ NEW IN v5.0

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
- ✅ Explicitly documented as active/open
- ✅ Default when no restrictions or development status documented

**Discovery guidance:**
Can be left blank if obviously active. Use explicitly when differentiating from networks with other statuses.

---

### Planned

**Definition:**
Trail network is documented as planned but not yet developed.

**When to use:**
- ✅ Source explicitly documents as planned or proposed
- ✅ Network appears in planning documents but no member trails exist yet

**When NOT to use:**
- ❌ Inferred from incomplete member trail set
- ❌ Assumed from maps showing proposed routes

**Discovery guidance:**
Must be explicitly documented.

---

### Under Development

**Definition:**
Trail network is actively being built or expanded; some member trails may be open.

**When to use:**
- ✅ Source explicitly states under development or under construction
- ✅ Network is growing with documented active expansion

**When NOT to use:**
- ❌ Assumed from incomplete member set
- ❌ Any network that might grow in the future

---

### Partially Open

**Definition:**
Trail network has some member trails open but significant portions are not yet complete or accessible.

**When to use:**
- ✅ Source explicitly documents partial opening
- ✅ Managing agency describes network as partially open or incomplete

**When NOT to use:**
- ❌ Inferred from knowing some trails are open and some aren't
- ❌ Networks with minor gaps (use Active + notes)

---

### Closed

**Definition:**
Trail network is permanently or indefinitely closed.

**When to use:**
- ✅ Explicitly documented as permanently closed
- ✅ Network has been decommissioned

**When NOT to use:**
- ❌ Temporary closures (use notes)
- ❌ Seasonal closures (use notes)

**Discovery guidance:**
Must be explicitly documented as closed.

------------------------------------------------------------
# 4. OWNERSHIP (Free-Text — No Controlled Vocabulary) ✨ NEW IN v5.0

## 4.1 Overview

**Ownership is a free-text field — there is no controlled vocabulary.**

Record the ownership description exactly as documented by the authoritative source.

## 4.2 What to Collect

- Name of the owning entity when a single agency or organization owns the network
- Ownership arrangement when explicitly documented

**Examples of valid ownership descriptions:**
- "Ohio Department of Natural Resources"
- "Wood County Park District"
- "Metroparks Toledo"
- "North Country Trail Association"

## 4.3 What NOT to Collect

- ❌ Governing or managing agencies (those go in Governance / Partner Agencies)
- ❌ Inferred ownership from governance
- ❌ Invented ownership descriptions

## 4.4 When to Leave Blank

Leave blank when:
- Ownership is distributed across multiple agencies (no single owner)
- Network is a coordinating body without land ownership
- Ownership is unclear or undocumented

**Note:** Many trail networks are coordinating bodies rather than land owners — blank is correct and common for this field.

## 4.5 Discovery Guidance

- Record ownership exactly as documented by authoritative source
- Don't rephrase or standardize agency names during discovery
- Leave blank if not explicitly documented

## 4.6 Normalization Guidance

- Standardize agency name to official form
- Verify against known agency names in the Entity Graph
- Leave blank if distributed or undocumented

------------------------------------------------------------
# 5. VOCABULARY NORMALIZATION RULES

## 5.1 Common Mappings

**Network Type:**
```
Raw Value                          → Normalized Value
----------                           ----------------
"regional greenway"                → "Regional Greenway System"
"greenway network"                 → "Regional Greenway System"
"national scenic trail"            → "National Scenic Trail System"
"NST system"                       → "National Scenic Trail System"
"paddling trail network"           → "Water Trail Network"
"blueway network"                  → "Water Trail Network"
"statewide trail system"           → "Statewide Trail System"
"county trail system"              → "County Trail Network"
"city trail network"               → "Municipal Trail Network"
"multi-agency trail network"       → "Multi-Jurisdictional Trail Network"
```

**Status:**
```
Raw Value                          → Normalized Value
----------                           ----------------
"open"                             → "Active"
"operational"                      → "Active"
"proposed"                         → "Planned"
"in development"                   → "Under Development"
"under construction"               → "Under Development"
"partially complete"               → "Partially Open"
"permanently closed"               → "Closed"
"decommissioned"                   → "Closed"
```

## 5.2 Ambiguous Cases

**Require context or manual review:**
- "greenway" alone — could be Regional Greenway System or just a description
- "trail system" — could be Statewide, County, Municipal, or Multi-Jurisdictional
- "incomplete" — could be Under Development or Partially Open
- "closed" — could be permanent or temporary

**Resolution:**
- Check source context for additional descriptors
- Prefer more specific term when context supports it
- Leave blank rather than guess
- Flag for manual review if confidence low

------------------------------------------------------------
# 6. VOCABULARY USAGE RULES

## 6.1 Universal Rules

1. **Use exactly as written** — No synonyms, abbreviations, or invented terms
2. **Don't infer** — Values must be documented, not inferred from member count or geography
3. **Leave blank if unclear** — Better to have no value than wrong value
4. **One value per field** — No multi-value types
5. **Flag new values** — Don't add values; flag for vocabulary expansion

## 6.2 Discovery Phase

- Capture raw values exactly as found
- Don't attempt normalization during discovery
- Record raw variations in *_raw fields

## 6.3 Normalization Phase

- Map raw values to controlled vocabulary
- Handle common variations (see Section 5)
- Flag unrecognized values for review
- Validate against vocabulary list

------------------------------------------------------------
# 7. VOCABULARY VERSIONING

## 7.1 Version History

**v5.0:**
- Added Status vocabulary (5 values)
- Added Ownership field guidance (free-text, no vocabulary)
- Enhanced Network Type definitions and normalization mappings
- Updated to v5.0 references

**v4.0:**
- Initial controlled vocabulary
- Network Type defined

------------------------------------------------------------
# 8. INTEGRATION POINTS

This vocabulary module integrates with:

- **Trail Network Schema Module v5.0** (field definitions)
- **Trail Network Discovery Sub-Procedure v5.0** (raw capture)
- **Resolution Engine v5.0** (conflict detection)
- **Normalization Engine v5.0** (vocabulary mapping)
- **TSV Output Specification v5.0** (output format)

------------------------------------------------------------
# END OF TRAIL NETWORK VOCABULARY MODULE v5.0
