# NATURAL AREAS PROJECT
# SITE NETWORK VOCABULARY MODULE v6.0
(Authoritative Controlled Vocabularies for Site Network Fields)

This module contains all controlled vocabularies for Site Network entities
in the Natural Areas Project v6.x.

All Site Network-related modules must reference this module for vocabulary
authority.

------------------------------------------------------------
# CHANGES FROM v5.3 → v6.0 (IMP-003)

- **Network Type vocabulary expanded** (§2): The two generic organizational
  portfolio types ("Multi-Site Recreation Network" and "Multi-Site Conservation
  Network") are retired. Replaced with seven specific organizational portfolio
  types that distinguish park districts, municipal systems, state programs,
  federal programs, land trusts, conservation authorities, and nonprofit
  conservancies. Total network_type values: 17 + Other.

- **Org Type vocabulary updated** (§3): Aligned with the canonical v6.x
  org_type vocabulary defined in Trailthing Vocabulary Module v6.0. Two values
  added: Trail Association and Coordinating Body. Definitions and examples
  updated. This module and the Trailthing Vocabulary Module are the co-authoritative
  sources for org_type; they must remain aligned.

- **Coordination field guidance added** (§7): New free-text field added to
  the Site Network schema in v6.0; guidance parallels the Trailthing vocabulary.

- **Identity Notes guidance updated** (§8): SITE_NETWORK_PROVISIONAL flag
  format documented. SITE_NETWORK_UNCERTAIN narrowed per Site Network Schema
  v6.0 §3.14.

- **Normalization mapping tables updated** (§9): Network Type mapping table
  updated to remove retired Multi-Site types and add new organizational
  portfolio type mappings. Org Type mapping table updated for new values.

------------------------------------------------------------
# 1. PURPOSE

This module defines the authoritative controlled vocabularies for:
- Network Type (§2)
- Org Type (§3)
- Status (§4)

And provides field guidance for free-text fields:
- Ownership (§5)
- Governance (§6)
- Coordination (§7)
- Identity Notes (§8)
- Notes (§9)

These vocabularies are used across:
- Site Network Discovery Sub-Procedure v6.x (raw capture)
- Resolution Engine v6.x (conflict detection)
- Normalization Engine v6.x (vocabulary mapping)
- Site Network TSV Output Specification v6.x (output format)

**Key Principle:** Vocabularies are DESCRIPTIVE, not PRESCRIPTIVE.
- Values describe what authoritative sources document
- Values are not inferred from member sites, geography, or governance structure
- If no documented value matches, leave the field blank

------------------------------------------------------------
# 2. NETWORK TYPE VOCABULARY (Controlled)

## 2.1 Allowed Values

**Formal Designations**
- National Heritage Area
- Scenic River Corridor
- Heritage Corridor
- Historic Corridor
- Conservation Corridor
- Ecological Corridor
- Cultural Landscape Network
- Watershed Network
- Greenway Network
- Local Historic District

**Organizational Portfolio Types**
- Park District System
- Municipal Recreation System
- State Program Portfolio
- Federal Program Portfolio
- Land Trust Portfolio
- Conservation Authority Portfolio
- Nonprofit Conservation Portfolio

**Catch-all**
- Other

**Retired values (v5.x only — do not use in v6.x):**
- Multi-Site Recreation Network ← retired; use Park District System,
  Municipal Recreation System, or appropriate portfolio type
- Multi-Site Conservation Network ← retired; use Land Trust Portfolio,
  Conservation Authority Portfolio, or Nonprofit Conservation Portfolio

------------------------------------------------------------
## 2.2 Definitions & Usage Rules

### Formal Designations

Formal designation network types qualify under Rule 1 of the Site Network
identity rules — a formal designation always warrants a record regardless
of member site count. See Site Network Schema Module v6.0 §4.

---

#### National Heritage Area

**Definition:**
A federally designated National Heritage Area — a region recognized by
Congress for its natural, cultural, historic, and recreational resources.

**When to use:**
- ✅ Federally designated NHA by Congressional act
- ✅ Source explicitly references NHA designation

**When NOT to use:**
- ❌ State heritage areas without federal designation
- ❌ Inferred from heritage-related content

---

#### Scenic River Corridor

**Definition:**
A corridor of sites along a formally designated scenic river — state or
federal scenic river designation.

**When to use:**
- ✅ Ohio Scenic River designation or federal Wild and Scenic River
- ✅ Source explicitly documents as scenic river corridor

**When NOT to use:**
- ❌ Any collection of sites near a river
- ❌ Inferred from proximity to a scenic waterway

**Normalization:** "scenic river system," "wild and scenic river corridor,"
"state scenic river," "wild and scenic river" → "Scenic River Corridor"

---

#### Heritage Corridor

**Definition:**
A formally designated heritage corridor encompassing natural, cultural,
and historic resources — broader in scope than Historic Corridor.

**When to use:**
- ✅ Formal heritage corridor designation (state or federal)
- ✅ Source explicitly documents as heritage corridor
- ✅ Scope includes natural and cultural resources together

**When NOT to use:**
- ❌ If Historic Corridor is more precise (historic focus only)

**Normalization:** "national heritage corridor," "state heritage corridor" → "Heritage Corridor"

---

#### Historic Corridor

**Definition:**
A formally documented corridor focused primarily on historically significant
sites.

**When to use:**
- ✅ Formal historic corridor designation
- ✅ Source explicitly documents as historic corridor
- ✅ Primary focus is historically significant sites

**When NOT to use:**
- ❌ If Heritage Corridor is more appropriate (broader natural+cultural scope)

---

#### Conservation Corridor

**Definition:**
A formally documented conservation corridor connecting member sites for
ecological or conservation purposes.

**When to use:**
- ✅ Source explicitly documents as conservation corridor
- ✅ Formal corridor designation by a conservation agency

**When NOT to use:**
- ❌ Inferred from sites being near each other
- ❌ Any collection of conservation sites

---

#### Ecological Corridor

**Definition:**
A formally documented ecological corridor connecting natural area sites
for wildlife movement or ecological function.

**When to use:**
- ✅ Source explicitly documents as ecological corridor
- ✅ Formal ecological corridor designation

**When NOT to use:**
- ❌ Inferred from ecological connectivity or proximity
- ❌ Any collection of natural areas

---

#### Cultural Landscape Network

**Definition:**
A formally recognized network of sites sharing cultural landscape identity
or designation.

**When to use:**
- ✅ Source explicitly documents as cultural landscape network
- ✅ Formal cultural landscape designation

**When NOT to use:**
- ❌ Inferred from cultural character of sites

---

#### Watershed Network

**Definition:**
A formally documented network of sites organized around a shared watershed
identity — the watershed itself is the organizing principle, not the managing
organization.

**When to use:**
- ✅ Source explicitly documents as watershed network or watershed system
- ✅ Formal watershed-based network designation with documented site membership

**When NOT to use:**
- ❌ Inferred from sites being in the same watershed
- ❌ A watershed conservancy district managing land (use Conservation Authority
  Portfolio for the organization's holdings)

---

#### Greenway Network

**Definition:**
A formally documented network of sites along a greenway corridor, where
the sites are the primary identity — not the trail connecting them.

**When to use:**
- ✅ Source explicitly documents as greenway network with named member sites
- ✅ Formal greenway system where site membership is the documented identity

**When NOT to use:**
- ❌ Trail greenways where the primary identity is the trail system
  (those are Trailthings, not Site Networks)
- ❌ Inferred from linear arrangement of sites

---

#### Local Historic District

**Definition:**
A formally designated local historic district with legal standing, recognized
by municipal, county, or state authority.

**When to use:**
- ✅ Formal historic district designation with documented member sites
- ✅ Source explicitly references historic district designation

**When NOT to use:**
- ❌ Informal historic neighborhoods without formal designation
- ❌ Inferred from age or character of sites

---

### Organizational Portfolio Types

Organizational portfolio types apply to Site Networks created under Rules 2,
3, and 4 of the Site Network identity rules — networks where the organization's
holdings are the collection. See Site Network Schema Module v6.0 §4.

**Guidance on selecting the right portfolio type:**
Use the type that most precisely describes the nature of the organization and
its collection. Org Type describes what kind of organization manages it; Network
Type describes what kind of collection it is. Both fields carry information and
should be consistent with each other, but they are not redundant.

---

#### Park District System

**Definition:**
The portfolio of parks and natural areas managed by a county, metropolitan,
or regional park district — a government authority specifically created by
charter or statute to manage parks.

**When to use:**
- ✅ County park district (Wood County Park District, Wayne County Park District)
- ✅ Metropolitan park district (Metro Parks Serving Franklin County)
- ✅ Regional park authority created for park management

**When NOT to use:**
- ❌ Municipal parks departments — those are Municipal Recreation System
- ❌ State agencies — those are State Program Portfolio
- ❌ A park district referenced only as governance on individual Site records
  without sufficient member sites to meet the applicable threshold

**Examples:**
- Metro Parks Serving Franklin County
- Wood County Park District
- Metroparks Toledo

---

#### Municipal Recreation System

**Definition:**
The portfolio of in-scope parks, natural areas, and open spaces managed by
a city or village parks and recreation department.

**When to use:**
- ✅ City or village parks and recreation department with 3+ in-scope member sites
  (per Rule 3 of the Site Network identity rules)
- ✅ Municipal forestry, greenspace, or open space office

**When NOT to use:**
- ❌ Park districts (use Park District System)
- ❌ Municipal departments with fewer than the applicable threshold of in-scope sites

**Examples:**
- Columbus Recreation and Parks Department
- Dublin Parks and Recreation

---

#### State Program Portfolio

**Definition:**
A statewide program, program division, or named collection of sites managed
by a state agency under a common program identity. The program identity —
not the agency itself — is the anchor: ODNR manages multiple distinct programs,
each of which is a separate Site Network record.

**When to use:**
- ✅ ODNR program portfolios: Ohio State Nature Preserves, Ohio State Parks,
  Ohio State Forests, Ohio Division of Wildlife Areas — each is a separate
  Site Network record
- ✅ Ohio History Connection site portfolio
- ✅ Any state agency program that groups its sites under a named program identity
  with 2+ member sites (per Rule 2 of the Site Network identity rules)

**When NOT to use:**
- ❌ ODNR as a single statewide network — ODNR manages multiple distinct programs;
  each program is its own Site Network record
- ❌ A state agency referenced only as governance on individual Site records

**Examples:**
- Ohio State Nature Preserves (governance: ODNR Division of Natural Areas and Preserves)
- Ohio State Parks (governance: ODNR Division of Parks and Watercraft)
- Ohio State Forests (governance: ODNR Division of Forestry)
- Ohio Division of Wildlife Areas (governance: ODNR Division of Wildlife)
- Ohio History Connection Sites

---

#### Federal Program Portfolio

**Definition:**
A regional or state-level collection of sites managed by a federal agency
under a common program or administrative unit.

**When to use:**
- ✅ National Park Service units in a region or administrative grouping
- ✅ U.S. Fish and Wildlife Service refuge complex or regional portfolio
- ✅ U.S. Army Corps of Engineers lakes and recreation areas portfolio
- ✅ U.S. Forest Service district or ranger district holdings
- ✅ Any federal agency program grouping 2+ member sites

**When NOT to use:**
- ❌ A single federal site (that's a Site entity)
- ❌ A federal agency referenced only as governance

---

#### Land Trust Portfolio

**Definition:**
The portfolio of preserves, conservation properties, and protected lands
held in fee or under conservation easement by a land trust.

**When to use:**
- ✅ Accredited or recognized land trust with 2+ in-scope member sites
  (per Rule 2 of the Site Network identity rules)
- ✅ Primary activity is land acquisition or conservation easements

**When NOT to use:**
- ❌ Nonprofit conservancies whose primary activity is stewardship without
  land ownership (use Nonprofit Conservation Portfolio)
- ❌ Government land-holding agencies (use appropriate government portfolio type)

**Examples:**
- Arc of Appalachia Preserve System
- Black Swamp Conservancy
- Central Ohio Land Trust

---

#### Conservation Authority Portfolio

**Definition:**
The portfolio of conservation lands managed by a conservancy district,
watershed conservancy district, soil and water conservation authority, or
similar government or quasi-government authority created for conservation
or resource management purposes.

**When to use:**
- ✅ Muskingum Watershed Conservancy District lakes and recreation areas
- ✅ Soil and water conservation district managed lands (when meeting threshold)
- ✅ Watershed conservancy or conservancy district with 2+ in-scope member sites

**When NOT to use:**
- ❌ Non-governmental land trusts (use Land Trust Portfolio)
- ❌ Park districts created for park management (use Park District System)

**Examples:**
- Muskingum Watershed Conservancy District (MWCD) — 16 lakes and associated
  recreation areas

---

#### Nonprofit Conservation Portfolio

**Definition:**
The portfolio of managed natural areas, preserves, or conservation properties
held or stewarded by a nonprofit conservancy, friends organization, or
environmental nonprofit that does not qualify as a land trust.

**When to use:**
- ✅ Nonprofit conservancy or watershed alliance managing multiple sites
- ✅ Friends group with documented stewardship of multiple distinct sites
- ✅ University-affiliated natural area programs managing multiple sites
- ✅ Environmental nonprofit with 2+ in-scope member sites

**When NOT to use:**
- ❌ Organizations whose primary activity is land acquisition (use Land Trust Portfolio)
- ❌ Government agencies (use appropriate government portfolio type)

**Examples:**
- Conservancy for Cuyahoga Valley National Park (supporting NPS)
- Friends groups with multiple stewardship sites

---

#### Other

**Definition:**
Named network type from authoritative source that does not fit any other
category.

**Discovery guidance:**
Record raw term exactly in identity_notes_raw. Flag for vocabulary expansion
review.

------------------------------------------------------------
# 3. ORG TYPE VOCABULARY (Controlled)

## 3.1 Allowed Values

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

**Cross-module note:** These values are the canonical org_type vocabulary for
v6.x, shared with the Trailthing Vocabulary Module v6.0. Any additions or
changes to org_type values must be made in both modules simultaneously.

**Note on Trail Association for Site Networks:** Trail Association is included
for consistency with the canonical org_type list but will rarely apply to Site
Networks. A trail association that also manages conservation land might warrant
it. When in doubt, Nonprofit Conservancy is the more likely fit.

------------------------------------------------------------
## 3.2 Definitions & Usage Rules

**IMPORTANT:** Org Type is used in threshold enforcement for Site Networks.
See Site Network Schema Module v6.0 §4 (Identity Rules) for how org_type
determines which threshold rule applies.

### Federal Agency

**Definition:**
Primary governance entity is a U.S. federal government agency or bureau
managing natural areas, parks, forests, wildlife refuges, or waterways.

**When to use:**
- ✅ National Park Service
- ✅ U.S. Fish and Wildlife Service
- ✅ U.S. Army Corps of Engineers
- ✅ U.S. Forest Service
- ✅ Bureau of Land Management

**Examples:** National Park Service, U.S. Army Corps of Engineers

---

### State Agency

**Definition:**
Primary governance entity is a state government agency or division with
authority over natural areas, parks, forests, wildlife areas, or waterways.

**When to use:**
- ✅ ODNR and its divisions (Division of Parks and Watercraft, Division of
  Natural Areas and Preserves, Division of Wildlife, Division of Forestry)
- ✅ Ohio History Connection
- ✅ Other Ohio state executive agency divisions managing natural areas

**When NOT to use:**
- ❌ Federal agencies (use Federal Agency)
- ❌ State universities managing natural areas (use Nonprofit Conservancy
  or Other as appropriate)

**Examples:** Ohio Department of Natural Resources, Ohio History Connection

---

### Regional Authority

**Definition:**
Primary governance entity is a regional multi-county authority, metropark
district, or conservancy district with jurisdiction spanning multiple
counties or a defined multi-county service territory.

**When to use:**
- ✅ Multi-county park or greenway authority
- ✅ Regional park authorities spanning multiple jurisdictions

**When NOT to use:**
- ❌ Single-county park districts (use County Authority)
- ❌ State agencies (use State Agency)

---

### County Authority

**Definition:**
Primary governance entity is a county-level body — county park district,
metropolitan park district (single-county service territory), county
commissioners, county engineer, or county-level government agency.

**When to use:**
- ✅ County park district or metropolitan park district (single-county)
- ✅ County conservation board or natural resources commission

**When NOT to use:**
- ❌ Municipal departments (use Municipal Department)
- ❌ Multi-county regional authorities (use Regional Authority)

**Examples:** Metro Parks Serving Franklin County, Wood County Park District

---

### Municipal Department

**Definition:**
Primary governance entity is a city or village government department —
parks and recreation, public works, or similar.

**When to use:**
- ✅ City or village parks and recreation department
- ✅ Municipal forestry, greenspace, or open space office

**When NOT to use:**
- ❌ County or regional park districts (use County Authority or Regional Authority)

**Examples:** Columbus Recreation and Parks Department, Dublin Parks and Recreation

---

### Land Trust

**Definition:**
Primary governance entity is an accredited or recognized land trust whose
mission includes land conservation and permanent protection through fee
acquisition or conservation easements.

**When to use:**
- ✅ Accredited or recognized land trust
- ✅ Primary activity is land acquisition or conservation easements

**When NOT to use:**
- ❌ Nonprofits focused on stewardship without land ownership
  (use Nonprofit Conservancy)
- ❌ Government agencies with conservation land programs

**Examples:** Arc of Appalachia, Black Swamp Conservancy, Central Ohio Land Trust

---

### Nonprofit Conservancy

**Definition:**
Primary governance entity is a private nonprofit organization whose mission
is conservation, environmental stewardship, or natural area management, but
whose primary activity is not land acquisition.

**When to use:**
- ✅ Friends groups or conservancy associations supporting a park system
- ✅ Watershed councils, river alliances, or stream conservancies
- ✅ Environmental nonprofits managing or stewarding specific sites
- ✅ University-affiliated natural areas managed as nonprofit entities

**When NOT to use:**
- ❌ Organizations whose primary activity is land acquisition (use Land Trust)
- ❌ Government agencies (use appropriate government org type)

---

### Trail Association

**Definition:**
Primary governance entity is a nonprofit, volunteer, or membership-based
organization whose primary purpose is managing, maintaining, or coordinating
a trail or trail system — and which also manages conservation lands or sites.

**When to use:**
- ✅ Trail association with documented stewardship of conservation sites
  (uncommon for Site Networks; more common for Trailthings)

**Note:** When in doubt for a Site Network, Nonprofit Conservancy is the more
likely fit. Trail Association is included for canonical consistency across
entity types.

---

### Coordinating Body

**Definition:**
Primary governance entity is a multi-agency partnership, coordinating
committee, or coalition that does not hold land or have primary management
authority, but coordinates planning, development, or stewardship across
participating agencies.

**When to use:**
- ✅ Governance is documented as a partnership or coordinating committee
- ✅ No single agency has primary management authority
- ✅ Common for NHAs, scenic river corridors, and heritage designation programs

---

### Other

**Discovery guidance:**
Record the actual governance entity name in the governance field and describe
the organization type in identity_notes_raw. Flag for vocabulary expansion review.

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
Site Network is currently operational and recognized.

**When to use:**
- ✅ Explicitly documented as active or operational
- ✅ Default when no other status is documented

**Discovery guidance:**
Can be left blank if obviously active.

**Normalization:** "open," "operational" → "Active"

---

### Proposed

**Definition:**
Site Network is documented as proposed but not yet formally established.

**When to use:**
- ✅ Source explicitly documents as proposed
- ✅ Network appears in planning or legislative documents but has not
  been formally designated or established

**When NOT to use:**
- ❌ Inferred from incomplete member site set
- ❌ Networks in early organizational stages without explicit documentation

**Normalization:** "proposed" → "Proposed"

---

### Under Development

**Definition:**
Site Network has been formally established but is actively being built
out, organized, or assembled — the designation or organization exists but
member sites or infrastructure are incomplete.

**When to use:**
- ✅ Source explicitly states under development or in formation
- ✅ Designation exists but member site identification is ongoing

**When NOT to use:**
- ❌ Any network that might grow in the future
- ❌ Assumed from an incomplete member site set

**Normalization:** "in formation," "in development," "being formed,"
"under development" → "Under Development"

---

### Inactive

**Definition:**
Site Network is no longer actively managed or promoted but has not been
formally dissolved. The network identity persists but operations have ceased.

**When to use:**
- ✅ Source documents as inactive or dormant
- ✅ Network identity persists but active programming or management has ended

**When NOT to use:**
- ❌ Assumed from lack of recent web updates
- ❌ Networks with temporary gaps in programming

**Normalization:** "dormant," "inactive," "no longer active" → "Inactive"

---

### Dissolved

**Definition:**
Site Network has been formally dissolved, disbanded, or decommissioned.

**When to use:**
- ✅ Explicitly documented as dissolved, disbanded, or terminated
- ✅ Formal dissolution of the network identity

**When NOT to use:**
- ❌ Assumed from site closures
- ❌ Networks that appear inactive without formal dissolution documentation

**Discovery guidance:** Must be explicitly documented.

**Normalization:** "disbanded," "terminated," "decommissioned,"
"formally dissolved" → "Dissolved"

------------------------------------------------------------
# 5. OWNERSHIP (Free-Text — No Controlled Vocabulary)

## 5.1 Overview

Ownership is a free-text field. There is no controlled vocabulary.

## 5.2 What to Collect

- Legal name of the entity that owns or legally established the network
- Only when explicitly documented by an authoritative source

**Examples:**
- "National Park Service"
- "Ohio History Connection"
- "Maumee Valley Land Trust"
- "U.S. Congress (federal designation)"

## 5.3 What NOT to Collect

- ❌ Governing or managing agencies (those go in Governance / Partner Agencies)
- ❌ Inferred ownership from governance or member site ownership
- ❌ Generic descriptions like "Multiple Agencies"

## 5.4 When to Leave Blank

Leave blank when:
- Ownership is distributed among member sites or multiple agencies
- Network is a coordinating or designating body without land ownership
- Ownership is unclear or undocumented

**Blank is correct and common** — most formal designations (NHAs, heritage
corridors, scenic river corridors) are not land-owning entities.

------------------------------------------------------------
# 6. GOVERNANCE (Free-Text — No Controlled Vocabulary)

## 6.1 Overview

Governance is a free-text field. There is no controlled vocabulary.

## 6.2 What to Capture

- The primary agency or organization responsible for managing or
  coordinating the Site Network
- Authoritative name exactly as documented

**Examples:**
- "Ohio & Erie Canalway Coalition"
- "Ohio Department of Natural Resources, Division of Natural Areas and Preserves"
- "Metro Parks Serving Franklin County"
- "National Park Service"

## 6.3 What NOT to Capture

- ❌ Inferred governance from member site governance
- ❌ Generic descriptions
- ❌ Organizations that appear only as partner agencies

------------------------------------------------------------
# 7. COORDINATION (Free-Text — No Controlled Vocabulary)

## 7.1 Overview

Coordination is a free-text field. There is no controlled vocabulary.

Added in Site Network Schema v6.0 — captures community-based, volunteer,
advisory, or informal partners, consistent with the four-tier organizational
model across all entity types.

## 7.2 What to Capture

- Friends groups and stewardship volunteers associated with the network
- Advisory boards or planning committees for the network
- Watershed councils or watershed partnerships supporting the network
- Community organizations with documented involvement in network programming

**Examples:**
- "Friends of the Little Miami"
- "Ohio & Erie Canalway Coalition Volunteer Network"
- "Scenic River Advisory Council"

## 7.3 Distinction from Partner Agencies

Partner Agencies are formal co-managers with documented operational roles
and institutional standing. Coordination captures informal, advisory, or
community-level involvement that does not rise to co-management.

When in doubt: if the source describes the organization as a co-manager,
grant recipient, or operational partner → Partner Agencies. If the source
describes volunteer support, advisory input, or community engagement → Coordination.

## 7.4 What NOT to Capture

- ❌ Organizations already listed in Governance or Partner Agencies
- ❌ Inferred coordination relationships
- ❌ Organizations with no documented role in this network

------------------------------------------------------------
# 8. IDENTITY NOTES (Free-Text — No Controlled Vocabulary)

## 8.1 Overview

Identity Notes is a free-text field. There is no controlled vocabulary.

## 8.2 Flags Used in Identity Notes

**SITE_NETWORK_PROVISIONAL** — use when a record is created before the
applicable member site threshold is met, because the first member site has
been cataloged and additional members are expected:
```
SITE_NETWORK_PROVISIONAL — [org name] first member site cataloged
[date]; [N] additional member sites expected. Threshold: [applicable rule].
```
Remove this flag when the applicable threshold is met.

**SITE_NETWORK_UNCERTAIN** — use only when it is genuinely unclear which
org_type or network_type applies, or when the organization's scope cannot
be determined from available sources:
```
SITE_NETWORK_UNCERTAIN — [description of specific uncertainty]
```
Do not use SITE_NETWORK_UNCERTAIN as a general placeholder or for
provisional records — use SITE_NETWORK_PROVISIONAL for those.

## 8.3 Other Uses

- Disambiguation notes (why this is a Site Network rather than a parent Site)
- Alternate or historical names for the network
- Governance verification notes
- Rationale for inclusion of gray-area candidates (Rule 4 records)
- Vocabulary type uncertainty (e.g., "source calls this 'greenway system' —
  may be Trailthing or Site Network; flagged for review")

## 8.4 Discovery vs. Normalization

- **Discovery stage**: capture in `identity_notes_raw`
- **Normalized stage**: surfaced as `identity_notes` field

------------------------------------------------------------
# 9. NOTES (Free-Text — No Controlled Vocabulary)

## 9.1 Overview

Notes is a free-text field. There is no controlled vocabulary.

## 9.2 What to Capture

- Funding notes and grant history relevant to network context
- Designation history or boundary clarification
- Partnership context not captured in other fields
- Discovery gaps (e.g., "member site count from website; individual site
  names not yet enumerated")
- Service territory notes for organizational portfolios
- Operational context that is not identity-defining

## 9.3 What NOT to Capture

- ❌ Identity-defining characteristics (those go in Description or Identity Notes)
- ❌ Member site details (those go in the Site records)
- ❌ Temporary conditions that belong in member Site records
- ❌ Pipeline provenance artifacts — source citations, IMP numbers, batch load
  notes, GPS references, and similar process content. Notes is a customer-facing
  field; it must be readable by someone who knows nothing about the pipeline.
  Provenance belongs in the provenance tables.

------------------------------------------------------------
# 10. VOCABULARY NORMALIZATION RULES — ENFORCEMENT

The Normalization Engine must apply the mapping tables in this section to
every controlled Site Network field. Out-of-vocabulary raw values must be
mapped or nulled per the rules below; they must never silently pass through
to normalized output or TSV.

**Enforcement model:**
- All vocabulary-controlled Site Network fields are optional (blanks are valid).
  Out-of-vocabulary values that cannot be mapped → **null-and-log**.
- "Null-and-log": set field to blank, preserve raw value in identity_notes
  (append vocabulary flag), write decision to normalization_provenance.
- **REVIEW** items require the normalization engine to surface the entity for
  human resolution before proceeding.
- Empty strings ("") are data defects — see §10.4.

------------------------------------------------------------
## 10.1 Network Type Normalization Mapping

| Raw Value (case-insensitive) | Maps To | Resolution Method |
|------------------------------|---------|-------------------|
| "national heritage area" | National Heritage Area | map-and-log |
| "national heritage corridor" | Heritage Corridor | map-and-log |
| "state heritage corridor" | Heritage Corridor | map-and-log |
| "wild and scenic river corridor" | Scenic River Corridor | map-and-log |
| "wild and scenic river" | Scenic River Corridor | map-and-log |
| "scenic river system" | Scenic River Corridor | map-and-log |
| "state scenic river" | Scenic River Corridor | map-and-log |
| "ohio scenic river" | Scenic River Corridor | map-and-log |
| "historic sites system" | Historic Corridor | map-and-log |
| "historic district network" | Historic Corridor | map-and-log |
| "park district system" | Park District System | map-and-log |
| "county park system" | Park District System | map-and-log |
| "metro park system" / "metropark system" | Park District System | map-and-log |
| "metropolitan park district" | Park District System | map-and-log |
| "municipal park system" / "city park system" | Municipal Recreation System | map-and-log |
| "village park system" | Municipal Recreation System | map-and-log |
| "city parks" (used as network type) | Municipal Recreation System | map-and-log |
| "state nature preserves" / "ohio state nature preserves" | State Program Portfolio | map-and-log |
| "state parks" / "ohio state parks" | State Program Portfolio | map-and-log |
| "state forests" / "ohio state forests" | State Program Portfolio | map-and-log |
| "wildlife areas" / "division of wildlife areas" | State Program Portfolio | map-and-log |
| "national park complex" | Federal Program Portfolio | map-and-log |
| "national wildlife refuge complex" | Federal Program Portfolio | map-and-log |
| "national forest district" | Federal Program Portfolio | map-and-log |
| "preserve portfolio" / "land trust preserves" | Land Trust Portfolio | map-and-log |
| "conservation easement portfolio" | Land Trust Portfolio | map-and-log |
| "conservancy district" / "watershed conservancy" | Conservation Authority Portfolio | map-and-log |
| "conservation district" (when land-managing) | Conservation Authority Portfolio | map-and-log |
| "conservancy preserves" / "conservancy portfolio" | Nonprofit Conservation Portfolio | map-and-log |
| "preserve network" / "nature preserve network" | Nonprofit Conservation Portfolio | map-and-log |
| "multi-site recreation network" | **REVIEW** | Retired v5 value — reclassify to appropriate v6 type. Check org_type: County Authority or Regional Authority → Park District System; Municipal Department → Municipal Recreation System; State Agency → State Program Portfolio. If unclear → null-and-log. |
| "multi-site conservation network" | **REVIEW** | Retired v5 value — reclassify to appropriate v6 type. Check org_type and mission: land acquisition → Land Trust Portfolio; conservancy district → Conservation Authority Portfolio; nonprofit stewardship → Nonprofit Conservation Portfolio. If unclear → null-and-log. |
| "recreation system" / "park network" | **REVIEW** | Check org_type: park district → Park District System; municipal → Municipal Recreation System. |
| Empty string ("") | null | See §10.4. |
| Compound or slash-delimited value | **REVIEW** | Single-value field. |
| Any value not in §2.1 and not in this table | **null-and-log** | Flag "network_type OOV: [value]" for vocabulary expansion review. |

---

## 10.2 Org Type Normalization Mapping

| Raw Value (case-insensitive) | Maps To | Resolution Method |
|------------------------------|---------|-------------------|
| "national park service" / "NPS" | Federal Agency | map-and-log |
| "u.s. army corps" / "army corps of engineers" | Federal Agency | map-and-log |
| "us fish and wildlife" / "USFWS" | Federal Agency | map-and-log |
| "us forest service" / "USFS" | Federal Agency | map-and-log |
| "bureau of land management" / "BLM" | Federal Agency | map-and-log |
| "ODNR" / "ohio department of natural resources" | State Agency | map-and-log |
| "ohio history connection" | State Agency | map-and-log |
| "state park" / "state nature preserve" / "state forest" | State Agency | map-and-log |
| "metropolitan park district" / "metro park district" | County Authority | map-and-log |
| "county park district" / "metropolitan parks" / "park district" | County Authority | map-and-log |
| "regional park authority" / "multi-county authority" | Regional Authority | map-and-log |
| "city parks department" / "parks and recreation department" | Municipal Department | map-and-log |
| "village parks" / "village recreation department" | Municipal Department | map-and-log |
| "land conservancy" / "land trust" / "conservation trust" | Land Trust | map-and-log |
| "the nature conservancy" | Land Trust | map-and-log |
| "friends group" / "friends of" (prefix) | Nonprofit Conservancy | map-and-log |
| "watershed council" / "watershed alliance" | Nonprofit Conservancy | map-and-log |
| "conservancy association" | Nonprofit Conservancy | map-and-log (verify not land-holding) |
| "coordinating committee" / "partnership" / "coalition" | Coordinating Body | map-and-log |
| "trail association" / "trail conservancy" (site-managing) | Trail Association | map-and-log (rare for Site Networks) |
| Empty string ("") | null | See §10.4. |
| Compound or slash-delimited value | **REVIEW** | Single-value field. |
| Any value not in §3.1 and not in this table | **null-and-log** | Flag "org_type OOV: [value]" for vocabulary expansion review. |

**Ambiguous case — "conservancy":** Check primary activity. Land acquisition
as primary mission → Land Trust. Stewardship, advocacy, or education as
primary mission → Nonprofit Conservancy. If unclear → null-and-log.

---

## 10.3 Status Normalization Mapping

| Raw Value (case-insensitive) | Maps To | Resolution Method |
|------------------------------|---------|-------------------|
| "open" / "operational" / "active" | Active | map-and-log |
| "proposed" | Proposed | map-and-log |
| "in formation" / "in development" / "being formed" | Under Development | map-and-log |
| "dormant" / "inactive" / "no longer active" | Inactive | map-and-log |
| "disbanded" / "terminated" / "decommissioned" / "formally dissolved" | Dissolved | map-and-log |
| "closed" | **REVIEW** | Ambiguous for Site Networks: permanent dissolution → Dissolved; temporary inaccessibility → Active + Note. Check for formal dissolution documentation. |
| Empty string ("") | null | See §10.4. |
| Any value not in §4.1 and not in this table | **null-and-log** | Flag "status OOV: [value]". |

---

## 10.4 Multi-Value and Empty String Enforcement

### Single-Value Requirement

Network Type, Org Type, and Status are single-value fields:

| Field | Single-Value | Multi-value prohibited |
|-------|--------------|------------------------|
| `network_type` | ✅ | Compound or slash-delimited values are never valid |
| `org_type` | ✅ | Compound or slash-delimited values are never valid |
| `status` | ✅ | Compound or slash-delimited values are never valid |

When a compound value cannot be resolved to a single canonical value:
1. Set field to blank
2. Append to identity_notes: "[field] compound value: '[raw]' — could not resolve; flagged for review"
3. Write raw value to normalization_provenance as "compound_value_stripped"

### Empty String Enforcement

An empty string ("") is not a valid blank. After mapping table application:
if result is empty string → convert to null. Log: "field [name]: empty string
converted to null."

---

## 10.5 Ambiguous Cases Requiring Context-Dependent Resolution

| Raw Value / Situation | Ambiguity | Guidance |
|----------------------|-----------|----------|
| "heritage corridor" vs. "historic corridor" | Broader natural+cultural scope (Heritage) vs. historic-only (Historic) | Check designation scope; if unclear → null-and-log |
| "greenway network" | Site Network (linked sites along greenway) vs. Trailthing (trail system) | If primary identity is sites → Site Network: Greenway Network. If primary identity is the trail → Trailthing. |
| "conservancy" (org type) | Land Trust vs. Nonprofit Conservancy | Check primary activity: land acquisition → Land Trust; stewardship/advocacy → Nonprofit Conservancy |
| "inactive" vs. "dissolved" | Dormant but continuing vs. formally ended | Check for formal dissolution documentation; if none → Inactive |
| "proposed" vs. "under development" | Pre-establishment vs. actively forming | Check whether formal establishment has occurred; if yes → Under Development |
| SITE_NETWORK_UNCERTAIN flag | Network identity uncertain | Preserve flag in identity_notes; do not resolve silently; surface for manual review |
| Retired v5 network_type values appearing in raw data | Multi-Site Recreation Network, Multi-Site Conservation Network | Reclassify per §10.1 REVIEW guidance |

------------------------------------------------------------
# 11. VOCABULARY USAGE RULES

## 11.1 Universal Rules

1. **Use exactly as written** — No synonyms, abbreviations, or invented terms
2. **Don't infer** — Values must be documented, not inferred from member sites
   or governance structure
3. **Leave blank if unclear** — Better no value than wrong value
4. **One value per field** — No multi-value controlled fields
5. **Flag new values** — Do not add values; flag for vocabulary expansion

## 11.2 Discovery Phase

- Capture raw values exactly as found in `_raw` fields
- Do not attempt normalization during discovery
- Capture identity clarifications in `identity_notes_raw`

## 11.3 Normalization Phase

- Apply §10.x mapping tables to all vocabulary-controlled fields
- Handle compound values per §10.4
- Convert empty strings to null per §10.4
- Null-and-log all unmappable values
- Surface REVIEW items for human resolution before TSV output

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This vocabulary module integrates with:

- Site Network Schema Module v6.0 (field definitions)
- Trailthing Vocabulary Module v6.0 (canonical org_type — must remain aligned)
- Site Network Discovery Sub-Procedure v6.x (raw capture)
- Resolution Engine v6.x (conflict detection)
- Normalization Engine v6.x (vocabulary mapping)
- Site Network Normalization Contract v6.x (normalization rules)
- Site Network TSV Output Specification v6.x (output format)

------------------------------------------------------------
# END OF SITE NETWORK VOCABULARY MODULE v6.0
