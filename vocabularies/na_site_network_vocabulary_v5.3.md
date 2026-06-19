# NATURAL AREAS PROJECT
# SITE NETWORK VOCABULARY MODULE v5.3
(Authoritative Controlled Vocabularies for Site Network Fields)

This module contains all controlled vocabularies for Site Network entities
in the Natural Areas Project v5.x.

All Site Network-related modules must reference this module for vocabulary authority.

------------------------------------------------------------
# CHANGES FROM v5.2 → v5.3

- **IMP-102 — Enforcement-grade §7 mapping tables**: Replaced informal
  code-block mappings with structured §7.1–§7.5 enforcement tables.
  - §7.1 Network Type Mapping Table: structured table with Raw Value,
    Maps To, and Resolution Method columns; null-and-log on unmappable
    values; REVIEW on compound values.
  - §7.2 Org Type Mapping Table: structured table; null-and-log on
    unmappable values; REVIEW on compound values.
  - §7.3 Status Mapping Table: "open"/"operational" → "Active" made
    explicit; "inactive" → "Inactive" (not "Dissolved"); REVIEW on
    ambiguous dissolution cases.
  - §7.4 Multi-Value and Empty String Enforcement: new section;
    documents single-value enforcement and empty string → null rule
    for network_type, org_type, and status.
  - §7.5 Ambiguous Cases: structured table replacing prose list;
    per-case guidance with network_type and org_type ambiguities.
- No vocabulary values added or removed.

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- **Org Type vocabulary added**: New controlled vocabulary section (§3) for the
  `org_type` field introduced in Site Network Schema v5.2. Seven values covering
  the full range of managing organization categories encountered in natural areas
  cataloging.
- All cross-module references updated to v5.2.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **All cross-module references updated to v5.x**
- **identity_notes guidance added**: Discovery-stage field identity_notes_raw
  feeds the normalized identity_notes field; vocabulary guidance updated accordingly
- No vocabulary values added or removed

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- **Status vocabulary added** — was missing from v4.0
- **Ownership field added** — free-text, no controlled vocabulary
- Updated to v5.0 references
- Enhanced definitions, usage rules, and normalization mappings
- Added discovery vs. normalization guidance per v5.0 philosophy

------------------------------------------------------------
# 1. PURPOSE

This module defines the authoritative controlled vocabularies for:
- Network Type
- Org Type
- Status

And provides field guidance for free-text fields:
- Ownership (no controlled vocabulary)
- Identity Notes (no controlled vocabulary)
- Notes (no controlled vocabulary)

These vocabularies are used across:
- Site Network Discovery Sub-Procedure v5.x (raw capture)
- Resolution Engine v5.x (conflict detection)
- Normalization Engine v5.x (vocabulary mapping)
- TSV Output Specification v5.x (output format)

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
A federally designated National Heritage Area — a region recognized by Congress
for its natural, cultural, historic, and recreational resources.

**When to use:**
- ✅ Federally designated NHA only
- ✅ Source explicitly references NHA designation

**When NOT to use:**
- ❌ State heritage areas without federal designation
- ❌ Inferred from heritage-related content

---

### Local Historic District

**Definition:**
A formally designated local historic district recognized by a municipal,
county, or state authority.

**When to use:**
- ✅ Formally designated historic district with legal standing
- ✅ Source explicitly references historic district designation

**When NOT to use:**
- ❌ Informal historic neighborhoods without formal designation
- ❌ Inferred from age or character of sites

---

### Scenic River Corridor

**Definition:**
A documented scenic river system with formally recognized member sites
along its corridor.

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
A formally documented conservation corridor connecting member sites for
ecological or conservation purposes.

**When to use:**
- ✅ Source explicitly documents as conservation corridor
- ✅ Formal corridor designation by a conservation agency or land trust

**When NOT to use:**
- ❌ Inferred from sites being near each other
- ❌ Any collection of conservation sites

---

### Cultural Landscape Network

**Definition:**
A formally recognized network of sites sharing cultural landscape identity
or designation.

**When to use:**
- ✅ Source explicitly documents as cultural landscape network
- ✅ Formal cultural landscape designation

**When NOT to use:**
- ❌ Inferred from cultural character of sites
- ❌ Any collection of culturally significant sites

---

### Watershed Network

**Definition:**
A formally documented network of sites organized around a shared watershed
identity.

**When to use:**
- ✅ Source explicitly documents as watershed network or watershed system
- ✅ Formal watershed-based network designation

**When NOT to use:**
- ❌ Inferred from sites being in the same watershed
- ❌ Watershed management districts without site network identity

---

### Greenway Network

**Definition:**
A formally documented greenway system with member sites along a greenway
corridor.

**When to use:**
- ✅ Source explicitly documents as greenway network
- ✅ Formal greenway system with documented member sites

**When NOT to use:**
- ❌ Inferred from linear arrangement of sites
- ❌ Trail greenways without site network identity (those are Trail Networks)

**Note:** Greenway Networks in Site Network context refer to site collections
along a greenway, not the trail system itself. If the primary identity is the
trail system, use Trail Network.

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
A formally designated heritage corridor — broader than a historic corridor,
may include natural and cultural resources.

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
A formally documented historic corridor focused on historically significant
sites.

**When to use:**
- ✅ Source explicitly documents as historic corridor
- ✅ Formal historic corridor designation

**When NOT to use:**
- ❌ Inferred from age or historical significance
- ❌ If "Heritage Corridor" is more appropriate (broader scope)

---

### Multi-Site Recreation Network

**Definition:**
A formally documented network of recreation sites managed or promoted as
a unified system.

**When to use:**
- ✅ Source explicitly documents as a recreation network or system
- ✅ Multiple recreation sites formally unified under a single identity
- ✅ County or municipal park systems with explicit system-level branding
  (unified map, passport program, system name distinct from managing org)

**When NOT to use:**
- ❌ Inferred from sites being recreation-oriented
- ❌ A park district as governance body with no system-level identity

**Normalization:**
- "recreation system", "park network", "recreation area network",
  "county park system", "municipal park system" → "Multi-Site Recreation Network"

---

### Multi-Site Conservation Network

**Definition:**
A formally documented network of conservation sites managed or coordinated
as a unified system.

**When to use:**
- ✅ Source explicitly documents as a conservation network or system
- ✅ Multiple conservation sites formally unified under a single identity
- ✅ Land trust preserve networks with explicit system-level branding

**When NOT to use:**
- ❌ Inferred from sites being conservation-oriented
- ❌ A land trust as governance body with no system-level identity

**Normalization:**
- "preserve network", "conservation lands network" → "Multi-Site Conservation Network"

---

### Other

**Definition:**
Named network type from authoritative source that doesn't fit any other
category.

**When to use:**
- ✅ Source provides a specific network type that doesn't match vocabulary
- ✅ Is a legitimate, documented network type

**When NOT to use:**
- ❌ Invented categories
- ❌ Inferred types

**Discovery guidance:**
Record raw term exactly in identity_notes_raw. Flag for vocabulary expansion
review.

------------------------------------------------------------
# 3. ORG TYPE VOCABULARY (Controlled)

## 3.1 Allowed Values

- Municipal Department
- County Authority
- Regional Authority
- State Agency
- Federal Agency
- Land Trust
- Nonprofit Conservancy
- Other

------------------------------------------------------------
## 3.2 Definitions & Usage Rules

### Municipal Department

**Definition:**
A parks, recreation, or natural resources department that is a division of
a municipal (city or village) government.

**When to use:**
- ✅ City or village parks and recreation department
- ✅ Municipal forestry, greenspace, or open space office
- ✅ Source identifies the org as a city or village department

**When NOT to use:**
- ❌ Township trustees (use County Authority or Other as appropriate)
- ❌ Regional park districts that span multiple jurisdictions

**Examples:**
- Canal Winchester Parks & Recreation Department
- Columbus Recreation and Parks Department
- Dublin Parks & Recreation

---

### County Authority

**Definition:**
A parks or natural resources authority, commission, or district organized
at the county level, including metropolitan park districts whose primary
jurisdiction is a single county or a defined metropolitan area.

**When to use:**
- ✅ County park district or metropolitan park district
- ✅ County conservation board or natural resources commission
- ✅ Source identifies org as county-level or metro-district authority

**When NOT to use:**
- ❌ Municipal departments (use Municipal Department)
- ❌ Multi-county regional authorities (use Regional Authority)

**Examples:**
- Metro Parks Serving Franklin County (Columbus and Franklin County Metro Parks)
- Delaware County District Library (non-parks example, for reference)

---

### Regional Authority

**Definition:**
A parks, greenway, or conservation authority whose jurisdiction spans
multiple counties or a defined multi-jurisdictional region, often created
by intergovernmental agreement or state legislation.

**When to use:**
- ✅ Multi-county park or greenway authority
- ✅ Regional planning commission managing natural areas
- ✅ Source identifies org as regional or multi-county authority

**When NOT to use:**
- ❌ Single-county park districts (use County Authority)
- ❌ State agencies (use State Agency)

**Examples:**
- Mid-Ohio Regional Planning Commission (MORPC) — greenway coordination role
- Conservancy for Cuyahoga Valley National Park

---

### State Agency

**Definition:**
A state government agency or division with authority over natural areas,
parks, forests, wildlife areas, or waterways.

**When to use:**
- ✅ Ohio Department of Natural Resources (ODNR) and its divisions
  (Division of Parks & Watercraft, Division of Wildlife, Division of Forestry)
- ✅ Ohio History Connection
- ✅ Other state executive agency divisions managing natural areas

**When NOT to use:**
- ❌ Federal agencies (use Federal Agency)
- ❌ State universities managing natural areas (use Nonprofit Conservancy
  or Other depending on context)

**Examples:**
- Ohio Department of Natural Resources
- Ohio History Connection

---

### Federal Agency

**Definition:**
A U.S. federal government agency or bureau managing natural areas, parks,
forests, wildlife refuges, or waterways.

**When to use:**
- ✅ National Park Service
- ✅ U.S. Fish and Wildlife Service
- ✅ U.S. Army Corps of Engineers
- ✅ U.S. Forest Service
- ✅ Bureau of Land Management

**When NOT to use:**
- ❌ State agencies (use State Agency)
- ❌ Federally chartered but non-governmental conservancies

**Examples:**
- National Park Service
- U.S. Army Corps of Engineers

---

### Land Trust

**Definition:**
A private, nonprofit organization whose primary mission is acquiring and
protecting land through conservation easements, fee-simple acquisition,
or stewardship.

**When to use:**
- ✅ Accredited or recognized land trust
- ✅ Source identifies org as a land trust, land conservancy, or
  conservation land trust
- ✅ Primary activity is land acquisition or conservation easements

**When NOT to use:**
- ❌ Nonprofits primarily focused on advocacy, education, or programming
  without land ownership (use Nonprofit Conservancy)
- ❌ Government agencies with conservation land programs (use appropriate
  government org type)

**Examples:**
- The Nature Conservancy (Ohio chapter)
- Olentangy Land Trust
- Central Ohio Land Trust

---

### Nonprofit Conservancy

**Definition:**
A private, nonprofit organization whose primary mission is conservation,
environmental stewardship, or natural area management, but whose primary
activity is not land acquisition (distinguishing it from Land Trust).
Includes friends groups, conservancy associations, watershed councils,
and similar organizations.

**When to use:**
- ✅ Friends groups or conservancy associations supporting a park system
- ✅ Watershed councils, river alliances, or stream conservancies
- ✅ Environmental nonprofits managing or stewarding specific sites
- ✅ University-affiliated natural areas when managed as nonprofit entity

**When NOT to use:**
- ❌ Organizations whose primary activity is land acquisition (use Land Trust)
- ❌ Government agencies (use appropriate government org type)

**Examples:**
- Friends of Scioto Audubon
- Olentangy Watershed Alliance
- Rocky Fork Metro Park Conservancy

---

### Other

**Definition:**
Managing organization type from authoritative source that doesn't fit
any other vocabulary value.

**When to use:**
- ✅ Source provides a specific org type that doesn't match vocabulary
- ✅ Is a legitimate, documented organization type

**When NOT to use:**
- ❌ Invented or inferred categories

**Discovery guidance:**
Record raw term in identity_notes_raw. Flag for vocabulary expansion review.

------------------------------------------------------------
# 4. STATUS VOCABULARY (Controlled)

## 4.1 Allowed Values

- Active
- Proposed
- Under Development
- Inactive
- Dissolved

------------------------------------------------------------
## 4.2 Definitions & Usage Rules

### Active

**Definition:**
Site network is currently operational and recognized.

**When to use:**
- ✅ Explicitly documented as active or operational
- ✅ Default when no other status is documented

**Discovery guidance:**
Can be left blank if obviously active. Use explicitly when differentiating
from networks with other statuses.

---

### Proposed

**Definition:**
Site network is documented as proposed but not yet formally established.

**When to use:**
- ✅ Source explicitly documents as proposed
- ✅ Network appears in planning or legislative documents but has not
  been formally designated

**When NOT to use:**
- ❌ Inferred from incomplete member site set
- ❌ Networks in early organizational stages without explicit "proposed"
  documentation

**Discovery guidance:**
Must be explicitly documented — do not infer.

---

### Under Development

**Definition:**
Site network has been formally established but is actively being built
out or organized.

**When to use:**
- ✅ Source explicitly states under development or in formation
- ✅ Network designation exists but member sites or infrastructure
  are incomplete

**When NOT to use:**
- ❌ Any network that might grow in the future
- ❌ Assumed from incomplete member site set

---

### Inactive

**Definition:**
Site network is no longer actively managed or promoted but has not been
formally dissolved.

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
# 5. OWNERSHIP (Free-Text — No Controlled Vocabulary)

## 5.1 Overview

**Ownership is a free-text field — there is no controlled vocabulary.**

Record the ownership description exactly as documented by the authoritative
source.

## 5.2 What to Collect

- Legal name of the entity that owns or established the network
- Ownership arrangement when a single entity is clearly responsible

**Examples of valid ownership descriptions:**
- "National Park Service"
- "Ohio History Connection"
- "Maumee Valley Land Trust"
- "U.S. Congress (federal designation)"

## 5.3 What NOT to Collect

- ❌ Governing or managing agencies (those go in Governance / Partner Agencies)
- ❌ Inferred ownership from governance or member site ownership
- ❌ Invented ownership descriptions

## 5.4 When to Leave Blank

Leave blank when:
- Ownership is distributed among member sites or multiple agencies
- Network is a coordinating or designating body without land ownership
- Ownership is unclear or undocumented

**Note:** Many Site Networks are formal designations (NHAs, heritage corridors,
scenic river corridors) rather than land-owning entities — blank is correct
and common for this field.

------------------------------------------------------------
# 6. IDENTITY NOTES (Free-Text — No Controlled Vocabulary)

## 6.1 Overview

**Identity Notes is a free-text field — there is no controlled vocabulary.**

Used for identity clarifications that don't belong in Description or Notes.

## 6.2 What to Capture

- Disambiguation notes (e.g., why this is a network rather than a parent Site)
- Alternate or historical names
- System identity uncertainty flags (`SITE_NETWORK_UNCERTAIN`)
- Governance verification notes
- Rationale for inclusion of gray-area candidates
- Vocabulary type uncertainty (e.g., "source calls this 'greenway system' —
  may be Trail Network or Site Network")

## 6.3 Discovery vs. Normalization

- **Discovery stage**: capture in `identity_notes_raw`
- **Normalized stage**: surfaced as `identity_notes` field
- May include notes added during Resolution or Normalization passes

------------------------------------------------------------
# 7. VOCABULARY NORMALIZATION RULES

## 7.1 Network Type Mapping Table

MANDATORY: Read this table in full before normalizing any network_type value.

| Raw Value (case-insensitive) | Maps To | Resolution Method |
|------------------------------|---------|-------------------|
| "national heritage corridor" | Heritage Corridor | map-and-log |
| "national heritage area" | Heritage Corridor | map-and-log |
| "wild and scenic river corridor" | Scenic River Corridor | map-and-log |
| "scenic river system" | Scenic River Corridor | map-and-log |
| "wild and scenic river" | Scenic River Corridor | map-and-log |
| "state scenic river" | Scenic River Corridor | map-and-log |
| "recreation system" | Multi-Site Recreation Network | map-and-log |
| "park network" | Multi-Site Recreation Network | map-and-log |
| "county park system" | Multi-Site Recreation Network | map-and-log |
| "municipal park system" | Multi-Site Recreation Network | map-and-log |
| "metro park system" | Multi-Site Recreation Network | map-and-log |
| "preserve network" | Multi-Site Conservation Network | map-and-log |
| "conservation lands network" | Multi-Site Conservation Network | map-and-log |
| "nature preserve network" | Multi-Site Conservation Network | map-and-log |
| "conservation area network" | Multi-Site Conservation Network | map-and-log |
| "national wildlife refuge complex" | Multi-Site Conservation Network | map-and-log |
| "historic district network" | Historic Corridor | map-and-log |
| "historic sites system" | Historic Corridor | map-and-log |
| "recreation area system" | National Recreation Area | map-and-log |
| "national recreation area" | National Recreation Area | map-and-log |
| Any value not in this table | — | null-and-log |
| Empty string ("") | — | null (convert); log as defect |
| Compound or slash-delimited value | — | REVIEW |

**Enforcement rules:**
- Matching is case-insensitive; strip leading/trailing whitespace before matching.
- If raw value maps to a controlled value in this table → apply mapping and log.
- If raw value is not in this table and unambiguous → null-and-log; do not
  invent a mapping.
- If raw value is compound (slash, comma, semicolon) → flag as REVIEW.
- "Other" is a valid controlled value; use only when none of the above values
  apply and the entity is documented but atypical.
- NEVER use a value not in the §2.1 allowed values list.
- See §7.5 for ambiguous cases that require context-dependent resolution.

---

## 7.2 Org Type Mapping Table

MANDATORY: Read this table in full before normalizing any org_type value.

| Raw Value (case-insensitive) | Maps To | Resolution Method |
|------------------------------|---------|-------------------|
| "city parks department" | Municipal Department | map-and-log |
| "village parks" | Municipal Department | map-and-log |
| "parks and recreation department" | Municipal Department | map-and-log |
| "township parks" | Municipal Department | map-and-log |
| "village recreation department" | Municipal Department | map-and-log |
| "metro park district" | County Authority | map-and-log |
| "metropolitan park district" | County Authority | map-and-log |
| "county park district" | County Authority | map-and-log |
| "metropolitan parks" | County Authority | map-and-log |
| "park district" | County Authority | map-and-log |
| "regional park authority" | Regional Authority | map-and-log |
| "multi-county authority" | Regional Authority | map-and-log |
| "regional parks authority" | Regional Authority | map-and-log |
| "state park" | State Agency | map-and-log |
| "state nature preserve" | State Agency | map-and-log |
| "ohio dnr" | State Agency | map-and-log |
| "odnr" | State Agency | map-and-log |
| "ohio department of natural resources" | State Agency | map-and-log |
| "national park service" | Federal Agency | map-and-log |
| "u.s. army corps" | Federal Agency | map-and-log |
| "us fish and wildlife" | Federal Agency | map-and-log |
| "us forest service" | Federal Agency | map-and-log |
| "land conservancy" | Land Trust | map-and-log |
| "land trust" | Land Trust | map-and-log |
| "conservation trust" | Land Trust | map-and-log |
| "nature conservancy" | Land Trust | map-and-log |
| "friends group" | Nonprofit Conservancy | map-and-log |
| "watershed council" | Nonprofit Conservancy | map-and-log |
| "conservancy association" | Nonprofit Conservancy | map-and-log |
| "friends of" (prefix pattern) | Nonprofit Conservancy | map-and-log |
| Any value not in this table | — | null-and-log |
| Empty string ("") | — | null (convert); log as defect |
| Compound or slash-delimited value | — | REVIEW |

**Enforcement rules:**
- Matching is case-insensitive; strip leading/trailing whitespace before matching.
- If raw value maps to a controlled value in this table → apply mapping and log.
- If raw value is not in this table → null-and-log; do not invent a mapping.
- If raw value is compound → flag as REVIEW.
- "Other" may be used when none of the above apply and the org type is
  documented but atypical.
- NEVER use a value not in the §3.1 allowed values list.
- See §7.5 for ambiguous cases (especially "conservancy").

**Schema note:** The org_type column does not yet exist in the trail_networks
or site_networks DB tables as of v5.3. Normalization should compute and log
org_type values, but DB upsert for this field will succeed only after the schema migration is applied. Flag as a known gap in normalization_provenance.

---

## 7.3 Status Mapping Table

MANDATORY: Read this table in full before normalizing any status value.

| Raw Value (case-insensitive) | Maps To | Resolution Method |
|------------------------------|---------|-------------------|
| "open" | Active | map-and-log |
| "operational" | Active | map-and-log |
| "active" | Active | map-and-log |
| "proposed" | Proposed | map-and-log |
| "in formation" | Under Development | map-and-log |
| "in development" | Under Development | map-and-log |
| "being formed" | Under Development | map-and-log |
| "dormant" | Inactive | map-and-log |
| "inactive" | Inactive | map-and-log |
| "no longer active" | Inactive | map-and-log |
| "disbanded" | Dissolved | map-and-log |
| "terminated" | Dissolved | map-and-log |
| "decommissioned" | Dissolved | map-and-log |
| "formally dissolved" | Dissolved | map-and-log |
| Any value not in this table | — | null-and-log |
| Empty string ("") | — | null (convert); log as defect |
| "closed" | — | REVIEW (see §7.5) |

**Enforcement rules:**
- Matching is case-insensitive; strip leading/trailing whitespace before matching.
- "open" and "operational" map explicitly to "Active" — do not leave as raw.
- "dormant" and "inactive" → "Inactive" — do not use "Dissolved" unless
  formal dissolution is documented.
- "disbanded", "terminated", "decommissioned" → "Dissolved" only when
  explicitly documented.
- If raw value is not in this table → null-and-log; do not guess.
- "closed" is ambiguous for Site Networks (see §7.5) → REVIEW.
- Leave blank (null) if status is undocumented.

---

## 7.4 Multi-Value and Empty String Enforcement

**Multi-value fields:**
- network_type, org_type, and status are single-value fields.
- If a raw value contains a slash, comma, or semicolon → flag as REVIEW.
- Never split a compound value and silently pick one.

**Empty string enforcement:**
- An empty string ("") is a data defect, not a valid blank.
- Convert all empty string values for network_type, org_type, and status
  to null.
- Log each conversion as a normalization defect event.
- This step runs after field-level normalization (§7.1, §7.2, §7.3),
  before integrity anchor validation.

---

## 7.5 Ambiguous Cases

These raw values require REVIEW or context-dependent resolution:

| Raw Value | Ambiguity | Guidance |
|-----------|-----------|----------|
| "heritage corridor" vs. "historic corridor" | Cultural+natural scope (Heritage) vs. historic-only (Historic) | Check designation scope; if unclear → null-and-log |
| "greenway network" | Site Network (linked sites) or Trail Network (linear trail) | Check whether entity identity is site-based or trail-based; use entity type to guide vocabulary |
| "inactive" vs. "dissolved" | Dormant but continuing vs. formally ended | Check for formal dissolution documentation; if none → "Inactive" |
| "proposed" vs. "under development" | Pre-establishment vs. actively forming | Check whether formal establishment has occurred; if so → "Under Development" |
| County or municipal park system | Documented system identity vs. governance body only | Check for system-level branding or published identity; if governance only → not a Site Network |
| "conservancy" | Land Trust (land acquisition) vs. Nonprofit Conservancy (stewardship/advocacy) | Check primary activity; land acquisition → Land Trust; stewardship → Nonprofit Conservancy |
| "closed" | Permanent dissolution or temporary inaccessibility | Check for permanence; if temporary → Active with note; if permanent → Dissolved |
| SITE_NETWORK_UNCERTAIN flag | Network identity uncertain | Preserve flag in identity_notes; do not resolve silently; flag for manual review |

------------------------------------------------------------
# 8. VOCABULARY USAGE RULES

## 8.1 Universal Rules

1. **Use exactly as written** — No synonyms, abbreviations, or invented terms
2. **Don't infer** — Values must be documented, not inferred from member
   sites or geography
3. **Leave blank if unclear** — Better to have no value than wrong value
4. **One value per field** — No multi-value types (Network Type, Org Type, Status)
5. **Flag new values** — Don't add values; flag for vocabulary expansion

## 8.2 Discovery Phase

- Capture raw values exactly as found in `_raw` fields
- Don't attempt normalization during discovery
- Capture identity clarifications in `identity_notes_raw`

## 8.3 Normalization Phase

- Map raw values to controlled vocabulary
- Handle common variations (see Section 7)
- Flag unrecognized values for review
- Validate against vocabulary list
- Surface identity_notes_raw as normalized identity_notes field

------------------------------------------------------------
# 9. VOCABULARY VERSIONING

## 9.1 Version History

**v5.3:**
- IMP-102: §7 replaced with enforcement-grade §7.1–§7.5 mapping tables
  (Network Type, Org Type, Status, Multi-Value/Empty String Enforcement,
  Ambiguous Cases)
- No vocabulary values added or removed

**v5.2:**
- Org Type vocabulary added (7 values: Municipal Department, County Authority,
  Regional Authority, State Agency, Federal Agency, Land Trust,
  Nonprofit Conservancy, Other)
- Normalization mappings added for Org Type
- Cross-module references updated to v5.2

**v5.1:**
- Cross-module references updated to v5.x
- identity_notes field guidance added
- Multi-Site Recreation Network expanded to cover park district systems
  with system-level branding
- Normalization mappings updated for county/municipal park systems

**v5.0:**
- Added Status vocabulary (5 values)
- Added Ownership field guidance (free-text, no vocabulary)
- Enhanced Network Type definitions and normalization mappings

**v4.0:**
- Initial controlled vocabulary
- Network Type defined (12 values + Other)

------------------------------------------------------------
# 10. INTEGRATION POINTS

This vocabulary module integrates with:

- **Site Network Schema Module v5.2** (field definitions)
- **Site Network Discovery Sub-Procedure v5.x** (raw capture)
- **Resolution Engine v5.x** (conflict detection)
- **Normalization Engine v5.x** (vocabulary mapping)
- **Site Network Normalization Contract v5.2** (normalization rules)
- **TSV Output Specification v5.x** (output format)

------------------------------------------------------------
# END OF SITE NETWORK VOCABULARY MODULE v5.3
