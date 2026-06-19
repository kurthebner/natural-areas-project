# NATURAL AREAS PROJECT
# SITE NETWORK VOCABULARY MODULE v5.0
(Authoritative Controlled Vocabularies for Site Network Fields)

This module contains all controlled vocabularies for Site Network entities
in the Natural Areas Project v5.0.

All Site Network-related modules must reference this module for vocabulary authority.

------------------------------------------------------------
# CHANGES FROM v4.0

- **Status vocabulary added** ✨ NEW — was missing from v4.0
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
- Site Network Discovery Sub-Procedure v5.0 (raw capture)
- Resolution Engine v5.0 (conflict detection)
- Normalization Engine v5.0 (vocabulary mapping)
- TSV Output Specification v5.0 (output format)

**Key Principle:** Vocabularies are DESCRIPTIVE, not PRESCRIPTIVE.
- Values describe what authoritative sources document
- Values are not inferred from member sites, geography, or governance structure
- If no documented value matches, leave field blank

------------------------------------------------------------
# 2. NETWORK TYPE VOCABULARY (Controlled)

## 2.1 Allowed Values

- National Heritage Area
- Local Historic District
- Scenic River Corridor
- Conservation Corridor
- Cultural Landscape Network
- Watershed Network
- Greenway Network
- Ecological Corridor
- Heritage Corridor
- Historic Corridor
- Multi-Site Recreation Network
- Multi-Site Conservation Network
- Other

------------------------------------------------------------
## 2.2 Definitions & Usage Rules

### National Heritage Area

**Definition:**
A federally designated National Heritage Area — a region recognized by Congress for its natural, cultural, historic, and recreational resources.

**When to use:**
- ✅ Federally designated NHA only
- ✅ Source explicitly references NHA designation

**When NOT to use:**
- ❌ State heritage areas without federal designation
- ❌ Inferred from heritage-related content

---

### Local Historic District

**Definition:**
A formally designated local historic district recognized by a municipal, county, or state authority.

**When to use:**
- ✅ Formally designated historic district with legal standing
- ✅ Source explicitly references historic district designation

**When NOT to use:**
- ❌ Informal historic neighborhoods without formal designation
- ❌ Inferred from age or character of sites

---

### Scenic River Corridor

**Definition:**
A documented scenic river system with formally recognized member sites along its corridor.

**When to use:**
- ✅ Source explicitly documents as scenic river corridor
- ✅ Formal scenic river designation (state or federal)

**When NOT to use:**
- ❌ Any collection of sites near a river
- ❌ Inferred from proximity to a scenic waterway

**Normalization:**
- "scenic river system", "wild and scenic river corridor" → "Scenic River Corridor"

---

### Conservation Corridor

**Definition:**
A formally documented conservation corridor connecting member sites for ecological or conservation purposes.

**When to use:**
- ✅ Source explicitly documents as conservation corridor
- ✅ Formal corridor designation by a conservation agency or land trust

**When NOT to use:**
- ❌ Inferred from sites being near each other
- ❌ Any collection of conservation sites

---

### Cultural Landscape Network

**Definition:**
A formally recognized network of sites sharing cultural landscape identity or designation.

**When to use:**
- ✅ Source explicitly documents as cultural landscape network
- ✅ Formal cultural landscape designation

**When NOT to use:**
- ❌ Inferred from cultural character of sites
- ❌ Any collection of culturally significant sites

---

### Watershed Network

**Definition:**
A formally documented network of sites organized around a shared watershed identity.

**When to use:**
- ✅ Source explicitly documents as watershed network or watershed system
- ✅ Formal watershed-based network designation

**When NOT to use:**
- ❌ Inferred from sites being in the same watershed
- ❌ Watershed management districts without site network identity

---

### Greenway Network

**Definition:**
A formally documented greenway system with member sites along a greenway corridor.

**When to use:**
- ✅ Source explicitly documents as greenway network
- ✅ Formal greenway system with documented member sites

**When NOT to use:**
- ❌ Inferred from linear arrangement of sites
- ❌ Trail greenways without site network identity (those are Trail Networks)

**Note:** Greenway Networks in Site Network context refer to site collections along a greenway, not the trail system itself. If the primary identity is the trail system, use Trail Network.

---

### Ecological Corridor

**Definition:**
A formally documented ecological corridor connecting natural area sites.

**When to use:**
- ✅ Source explicitly documents as ecological corridor
- ✅ Formal ecological corridor designation

**When NOT to use:**
- ❌ Inferred from ecological connectivity
- ❌ Any collection of natural areas in proximity

---

### Heritage Corridor

**Definition:**
A formally designated heritage corridor — broader than a historic corridor, may include natural and cultural resources.

**When to use:**
- ✅ Source explicitly documents as heritage corridor
- ✅ Formal heritage corridor designation (state or federal)

**When NOT to use:**
- ❌ Inferred from heritage character of sites
- ❌ If "Historic Corridor" is more precise

**Normalization:**
- "national heritage corridor" → "Heritage Corridor"

---

### Historic Corridor

**Definition:**
A formally documented historic corridor focused on historically significant sites.

**When to use:**
- ✅ Source explicitly documents as historic corridor
- ✅ Formal historic corridor designation

**When NOT to use:**
- ❌ Inferred from age or historical significance
- ❌ If "Heritage Corridor" is more appropriate (broader scope)

---

### Multi-Site Recreation Network

**Definition:**
A formally documented network of recreation sites managed or promoted as a unified system.

**When to use:**
- ✅ Source explicitly documents as a recreation network or system
- ✅ Multiple recreation sites formally unified under a single identity

**When NOT to use:**
- ❌ Inferred from sites being recreation-oriented
- ❌ A park district's collection of parks without formal network identity

**Normalization:**
- "recreation system", "park network", "recreation area network" → "Multi-Site Recreation Network"

---

### Multi-Site Conservation Network

**Definition:**
A formally documented network of conservation sites managed or coordinated as a unified system.

**When to use:**
- ✅ Source explicitly documents as a conservation network or system
- ✅ Multiple conservation sites formally unified under a single identity

**When NOT to use:**
- ❌ Inferred from sites being conservation-oriented
- ❌ A land trust's collection of preserves without formal network identity

**Normalization:**
- "preserve network", "conservation lands network" → "Multi-Site Conservation Network"

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
- Proposed
- Under Development
- Inactive
- Dissolved

------------------------------------------------------------
## 3.2 Definitions & Usage Rules

### Active

**Definition:**
Site network is currently operational and recognized.

**When to use:**
- ✅ Explicitly documented as active or operational
- ✅ Default when no other status is documented

**Discovery guidance:**
Can be left blank if obviously active. Use explicitly when differentiating from networks with other statuses.

---

### Proposed

**Definition:**
Site network is documented as proposed but not yet formally established.

**When to use:**
- ✅ Source explicitly documents as proposed
- ✅ Network appears in planning or legislative documents but has not been formally designated

**When NOT to use:**
- ❌ Inferred from incomplete member site set
- ❌ Networks in early organizational stages without explicit "proposed" documentation

**Discovery guidance:**
Must be explicitly documented. The schema specifically calls this out — do not infer.

---

### Under Development

**Definition:**
Site network has been formally established but is actively being built out or organized.

**When to use:**
- ✅ Source explicitly states under development or in formation
- ✅ Network designation exists but member sites or infrastructure are incomplete

**When NOT to use:**
- ❌ Any network that might grow in the future
- ❌ Assumed from incomplete member site set

---

### Inactive

**Definition:**
Site network is no longer actively managed or promoted but has not been formally dissolved.

**When to use:**
- ✅ Source documents as inactive or dormant
- ✅ Network identity persists but operations have ceased

**When NOT to use:**
- ❌ Assumed from lack of recent web updates
- ❌ Networks with temporary gaps in programming

---

### Dissolved

**Definition:**
Site network has been formally dissolved or decommissioned.

**When to use:**
- ✅ Explicitly documented as dissolved, disbanded, or terminated
- ✅ Formal dissolution of the network identity

**When NOT to use:**
- ❌ Assumed from site closures
- ❌ Networks that appear inactive without formal dissolution documentation

**Discovery guidance:**
Must be explicitly documented.

------------------------------------------------------------
# 4. OWNERSHIP (Free-Text — No Controlled Vocabulary) ✨ NEW IN v5.0

## 4.1 Overview

**Ownership is a free-text field — there is no controlled vocabulary.**

Record the ownership description exactly as documented by the authoritative source.

## 4.2 What to Collect

- Legal name of the entity that owns or established the network
- Ownership arrangement when a single entity is clearly responsible

**Examples of valid ownership descriptions:**
- "National Park Service"
- "Ohio History Connection"
- "Maumee Valley Land Trust"
- "U.S. Congress (federal designation)"

## 4.3 What NOT to Collect

- ❌ Governing or managing agencies (those go in Governance / Partner Agencies)
- ❌ Inferred ownership from governance or member site ownership
- ❌ Invented ownership descriptions

## 4.4 When to Leave Blank

Leave blank when:
- Ownership is distributed among member sites or multiple agencies
- Network is a coordinating or designating body without land ownership
- Ownership is unclear or undocumented

**Note:** Many Site Networks are formal designations (NHAs, heritage corridors) rather than land-owning entities — blank is correct and common for this field.

## 4.5 Discovery Guidance

- Record ownership exactly as documented by authoritative source
- Don't rephrase or standardize agency names during discovery
- Leave blank if not explicitly documented

## 4.6 Normalization Guidance

- Standardize to official legal name of the entity
- Verify against known agency/organization names in the Entity Graph
- Leave blank if distributed or undocumented

------------------------------------------------------------
# 5. VOCABULARY NORMALIZATION RULES

## 5.1 Common Mappings

**Network Type:**
```
Raw Value                              → Normalized Value
----------                               ----------------
"national heritage corridor"           → "Heritage Corridor"
"wild and scenic river corridor"       → "Scenic River Corridor"
"scenic river system"                  → "Scenic River Corridor"
"recreation system"                    → "Multi-Site Recreation Network"
"park network"                         → "Multi-Site Recreation Network"
"preserve network"                     → "Multi-Site Conservation Network"
"conservation lands network"           → "Multi-Site Conservation Network"
```

**Status:**
```
Raw Value                              → Normalized Value
----------                               ----------------
"open"                                 → "Active"
"operational"                          → "Active"
"proposed"                             → "Proposed"
"in formation"                         → "Under Development"
"in development"                       → "Under Development"
"dormant"                              → "Inactive"
"disbanded"                            → "Dissolved"
"terminated"                           → "Dissolved"
"decommissioned"                       → "Dissolved"
```

## 5.2 Ambiguous Cases

**Require context or manual review:**
- "heritage corridor" vs. "historic corridor" — check whether scope is cultural+natural (Heritage) or historic-only (Historic)
- "greenway network" — check whether primarily sites (Site Network) or trails (Trail Network)
- "inactive" vs. "dissolved" — check for formal dissolution documentation
- "proposed" vs. "under development" — check whether formal establishment has occurred

**Resolution:**
- Check source context for additional descriptors
- Prefer more specific term when context supports it
- Leave blank rather than guess
- Flag for manual review if confidence low

------------------------------------------------------------
# 6. VOCABULARY USAGE RULES

## 6.1 Universal Rules

1. **Use exactly as written** — No synonyms, abbreviations, or invented terms
2. **Don't infer** — Values must be documented, not inferred from member sites or geography
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
- Network Type defined (12 values + Other)

------------------------------------------------------------
# 8. INTEGRATION POINTS

This vocabulary module integrates with:

- **Site Network Schema Module v5.0** (field definitions)
- **Site Network Discovery Sub-Procedure v5.0** (raw capture)
- **Resolution Engine v5.0** (conflict detection)
- **Normalization Engine v5.0** (vocabulary mapping)
- **TSV Output Specification v5.0** (output format)

------------------------------------------------------------
# END OF SITE NETWORK VOCABULARY MODULE v5.0
