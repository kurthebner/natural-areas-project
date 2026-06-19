# NATURAL AREAS PROJECT
# FEDERAL & TRIBAL LANDS DISCOVERY SUB-PROCEDURE v6.0
(Tier 1 — U.S. Federal Agencies & Tribal Lands)

This module defines the authoritative, deterministic Tier 1 discovery rules for
federal and tribal lands within the v6.x pipeline.

This module supersedes Federal & Tribal Lands Discovery Sub-Procedure v5.5.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v6.x Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v5.5 → v6.0

- **Entity type references updated throughout**: Trail, Trail Segment, and Trail
  Network are unified into the single Trailthing entity type. §2 Scope, §6 Entity
  Creation Rules, §7 Tier-Specific Expectations, and §8 Metadata Requirements
  updated accordingly. §6.3–6.5 (Trail, Trail Segment, Trail Network creation)
  consolidated into §6.3 (Trailthing Creation).

- **Document Collection added** (§5.4): During Tier 1 discovery, all qualifying
  maps, PDFs, GPX/KML files, GIS exports, and other source documents must be
  downloaded and logged per Discovery Orchestration Module v6.0 §4.

- **Section numbering corrected**: v5.5 §4 had 4.1–4.3 followed by 4.6 then 4.5
  (NHA was added as §4.6 before §4.5 was written). v6.0 renumbers to 4.1–4.5
  in logical order: Tribal Trust Lands, Tribal Reservations, Tribal Fee-Simple,
  Tribal Cultural Sites, NHA, USACE–ODNR Split Entities.

- **All v5.5 rules carried forward**: IMP-111 (VA NCA), IMP-029 (Pre-Discovery
  Checklist), IMP-030 (Captured Source Data), IMP-007 (NHA rules),
  OBS-004 (USACE–ODNR co-management), OBS-005 (NRHP on federal land).

------------------------------------------------------------
# 1. PURPOSE

The Federal & Tribal Lands Discovery Sub-Procedure v6.0 defines how Tier 1 must:

- Identify all federal Sites
- Identify tribal lands, tribal ownership, and tribal cultural Sites
- Identify Trailthings on federal lands
- Identify child Sites within federal Sites
- Identify Access Points associated with federal or tribal Sites and Trailthings
- Distinguish federal management from state/local co-management
- Avoid false positives from similarly named places
- Log uncertainty and boundary cases
- Produce Raw Discovery Records v6.x
- Download and log source documents per the Document Collection System

This module is referenced only by:
- Discovery Protocol Module v6.x
- Discovery Orchestration Module v6.0

------------------------------------------------------------
# 2. SCOPE

This sub-procedure applies to all federal agencies and tribal land categories:

- U.S. Forest Service (USFS)
- National Park Service (NPS)
- U.S. Fish & Wildlife Service (USFWS)
- U.S. Army Corps of Engineers (USACE)
- Bureau of Land Management (BLM)
- Department of Defense (DoD)
- VA National Cemetery Administration (VNCA) (IMP-111)
- Tribal trust land registries
- Tribal fee-simple ownership
- Tribal cultural Sites

It governs discovery of:

- Sites
- Child Sites
- Trailthings
- Site Networks
- Access Points

Tier 1 is the highest-authority tier in the discovery hierarchy.

------------------------------------------------------------
# 3. AUTHORITATIVE SOURCES (MANDATORY)

Tier 1 must enumerate and recursively explore the following authoritative sources.

## 3.1 U.S. Forest Service (USFS)
Ohio's only National Forest: **Wayne National Forest**

Required sources:
- Forest boundary datasets
- Recreation area pages
- USFS trail datasets
- USFS recreation maps (download qualifying maps per §5.4)
- Special management area datasets
- Campground datasets
- Trailhead datasets

## 3.2 National Park Service (NPS)
Required sources:
- NPS unit pages
- NPS boundary datasets
- NPS recreation maps (download qualifying maps per §5.4)
- NPS trail datasets
- National Heritage Area documentation

## 3.3 U.S. Fish & Wildlife Service (USFWS)
Required sources:
- Refuge pages
- Refuge boundary datasets
- USFWS recreation maps (download qualifying maps per §5.4)
- USFWS trail datasets
- Waterfowl Production Area datasets

## 3.4 U.S. Army Corps of Engineers (USACE)
Required sources:
- USACE project pages
- USACE recreation maps (download qualifying maps per §5.4)
- USACE facility datasets
- Boat ramp datasets
- Campground datasets

**USACE–ODNR Co-Management Pattern**: See §4.6.

## 3.5 Bureau of Land Management (BLM)
Ohio has minimal BLM surface holdings.

Required sources:
- BLM parcel datasets
- BLM easement datasets
- BLM mineral rights datasets

## 3.6 Department of Defense (DoD)
Required sources:
- DoD installation datasets
- FUDS datasets
- DoD environmental restoration maps

## 3.7 VA National Cemetery Administration (VNCA) — IMP-111

The Department of Veterans Affairs National Cemetery Administration manages
federally designated national cemeteries and VA-maintained Soldiers' Lots
within civilian cemeteries. These are Tier 1 Sites.

**National cemeteries** (standalone federal cemetery properties):
Required source:
- `https://www.cem.va.gov/find-cemetery/all-national.asp` — complete NCA
  national cemetery directory; filter by state, then identify any within
  the county being worked

**Soldiers' Lots** (federally maintained sections inside civilian/public
cemeteries):
Required source:
- `https://www.cem.va.gov/find-cemetery/soldiers-lots.asp` — complete VA
  Soldiers' Lot directory; filter by state, then identify any within the
  county being worked

Soldiers' Lots are smaller than full national cemeteries and are commonly
missed because they sit inside municipally or privately managed cemeteries.
The host cemetery stays at its governance tier (T4/T6/T8); the Soldiers'
Lot is a child Site at T1.

**Entity classification:**
- `category: Cemetery`
- `subtype: Veterans Cemetery`
- `governance_raw: U.S. Department of Veterans Affairs / National Cemetery Administration`
- `ownership_raw: Federal`
- `discovery_tier: 1`

For Soldiers' Lots: note in `identity_notes_raw`:
```
VA Soldiers' Lot — child of [host cemetery name]; host cemetery is at Tier [N].
```
Add `parent_site_id` reference once IDs are assigned in normalization.

**Null result documentation (most Ohio counties):**
Most Ohio counties have no NCA-managed cemetery. Document the null:
```yaml
tier_result:
  tier: 1
  governance_level: VA National Cemetery Administration
  entity_type: Site (Cemetery / Veterans Cemetery)
  result: null
  sources_checked:
    - https://www.cem.va.gov/find-cemetery/all-national.asp
    - https://www.cem.va.gov/find-cemetery/soldiers-lots.asp
  reasoning: No VA national cemeteries or Soldiers' Lots found for [County] County, Ohio
```

------------------------------------------------------------
# 4. DOMAIN RULES FOR FEDERAL & TRIBAL DISCOVERY

## 4.1 Tribal Trust Lands
- Check federal tribal land registries.
- If none exist in Ohio → record "None in Ohio" in metadata.

## 4.2 Tribal Reservations
- Check BIA datasets.
- If none exist in Ohio → record "None in Ohio" in metadata.

## 4.3 Tribal Fee-Simple Ownership
Check county auditor / GIS for parcels owned by:
- Federally recognized tribes
- Tribal corporations
- Tribal cultural organizations

If found → record as a **Site**, with tribal classification in metadata.

## 4.4 Tribal Cultural Sites
These are **not tribal lands**, but must be discovered:
- Mound sites
- Archaeological sites
- Cultural landscapes
- Burial grounds

Record as **Sites**, with metadata noting "Cultural Site — not tribal land."

## 4.5 National Heritage Areas (NHA) — IMP-007

National Heritage Areas are congressionally designated regions recognized for
their nationally significant natural, cultural, historical, and recreational
resources. They receive federal funding and technical assistance but no federal
land acquisition.

**Key rule:** NHA designation conveys no federal land ownership.

- Do **not** create Tier 1 land records for individual Sites, parks, or
  preserves solely because they fall within an NHA boundary. Those entities
  remain at their management tier.
- NHA designation may be noted in site `notes_raw` where relevant:
  `"Located within [NHA Name] National Heritage Area."`
- NHA affiliation does **not** change an entity's ownership, governance, or
  tier assignment.

**Site Network at Tier 1 (conditional):** If the NHA has a formally designated
coordinating entity (e.g., an NPS-affiliated NHA management organization) and a
defined geographic identity, create a **Site Network** at Tier 1 representing the
NHA as a whole. See §6.4.

**NPS NHA pages** (§3.2): NPS unit pages and National Heritage Area documentation
are authoritative sources for identifying NHA boundaries and their coordinating
entities.

## 4.6 USACE–ODNR Split Entities

When USACE owns the project boundary and ODNR manages recreation lands within it:

1. Create a Tier 1 Site for the USACE project (lake/reservoir/dam)
2. Flag it: `USACE_ODNR_COMANAGED — ODNR recreation entities will appear in Tier 2`
3. In Tier 2, create separate Sites for each ODNR-managed entity within the project
4. Flag each Tier 2 Site: `USACE_ODNR_COMANAGED — USACE project entity created in Tier 1`
5. Record the USACE project name in `identity_notes_raw` of each Tier 2 entity
6. Do not assign `parent_site_id` during discovery — the relationship is documented
   in notes and resolved in normalization

This pattern is common in Ohio wherever USACE built flood-control reservoirs
(Caesar Creek, East Fork, Mosquito Creek, etc.). The USACE project and the ODNR
park/wildlife area are separate legal entities with separate governance, separate
management plans, and sometimes different acreages.

------------------------------------------------------------
# 5. ENUMERATIVE + RECURSIVE DISCOVERY RULES

Tier 1 must use both enumerative and recursive discovery.

## 5.1 Enumerative Discovery (Listing Pages)
Tier 1 must enumerate:
- All federal unit listing pages
- All recreation area listings
- All trail listings
- All facility listings
- All boundary datasets

Always **fetch** official pages directly — do not rely on search snippets alone.
Extract ALL entities listed, not just those prominently featured.

**First-Pass Capture:** When fetching a federal unit or recreation area page,
extract ALL available fields in a single pass — including `description_raw`
(the narrative paragraph describing the site's character, ecology, or
significance) and `features_raw` (the amenity or facilities list). Both fields
are typically present on the same page. A return visit to collect fields that
were available on first fetch is a process failure. See Site Discovery Sub-
Procedure v6.0 §7.3 for field definitions and the Description Quality Gate.

**Pre-Discovery Checklist (IMP-029):** After enumerating federal units from
listing pages and before fetching individual entity pages, write the full entity
list to the handoff's Pre-Discovery Checklist. A context break between
enumeration and individual fetches should not require re-enumerating from source.

**Captured Source Data (IMP-030):** When fetching a structured source table
(unit directory, recreation area listing), write it verbatim to the handoff's
Captured Source Data section immediately — do not defer to staging time.

## 5.2 Recursive Discovery (URL Propagation)
Tier 1 must recursively follow:
- Internal links within federal domains
- Internal links within tribal registries
- Internal links within USACE project pages

Recursion must stop when:
- The domain is not on the allowlist
- The page is not relevant to Sites, Trailthings, or Access Points
- The page is a non-recreational administrative page

## 5.3 Recursion Allowlist
- *.nps.gov
- *.fs.usda.gov
- *.fws.gov
- *.usace.army.mil
- *.blm.gov
- *.defense.gov
- *.bia.gov

## 5.4 Document Collection

During Tier 1 discovery, download all qualifying source documents encountered —
trail maps, unit maps, brochures, recreation guides, GPX/KML files, GIS exports
— and log each in the county document log per **Discovery Orchestration Module
v6.0 §4**.

Federal land units are among the best-documented entities in the project.
USFS, NPS, and USFWS typically publish high-quality trail maps, unit brochures,
and recreation guides. These are valuable research assets that may be revised or
removed over time — download them at discovery time.

Particularly valuable documents to capture at Tier 1:
- Wayne National Forest trail maps and district maps
- NPS unit maps and visitor guides
- USFWS refuge maps and hunting/fishing guides
- USACE project recreation maps
- Water trail paddling guides (if a federal water trail is present)
- GPX/KML files for federal trails

------------------------------------------------------------
# 6. ENTITY CREATION RULES (TIER-SPECIFIC)

## 6.1 Site Creation
Create a **Site** when:
- Federally owned or federally managed
- Identity-bearing (named, mapped, or designated)
- Public access or recreation infrastructure exists
- It influences Access Point logic

Exclude:
- Federal office buildings
- Courthouses
- Post offices
- Non-recreational DoD facilities
- BLM mineral rights with no surface access

**NRHP Listings on Federal Land:** When a National Register of Historic Places
listing (mound, archaeological site, historic structure, historic district) exists
within a federal land unit:

- If the NRHP feature has its own identity and visitor access → create a child Site
  with `parent_site_id` pointing to the federal unit (assigned in normalization)
- If the NRHP feature is part of the federal unit's identity → add to the parent
  Site record's `identity_notes_raw`:
  `"NRHP-listed: [name], [ref]"`
- During discovery, create an independent raw record for any identity-bearing
  NRHP feature and note the suspected parent in `identity_notes_raw`

Cross-reference: See Resolution Engine v6.x (or v5.x) for the full NRHP
entity-type decision matrix.

## 6.2 Child Site Creation
Create a **child Site** when:
- A named internal unit exists within a federal Site
- A recreation area, campground, or management area is identity-bearing
- A special management zone is documented

## 6.3 Trailthing Creation
Create a **Trailthing** when:
- A named trail, trail section, trail system, or trail network appears in
  federal datasets or maps

Capture `source_term_raw` verbatim (how the source describes the entity —
"National Scenic Trail," "recreation trail," "trail system," "connector")
and `source_hierarchy_context_raw` when the source frames the entity in
relation to others. Do not classify the Trailthing as trail vs. trail
network vs. trail segment during discovery — record what the source says.

Record `difficulty_raw` and `accessibility_raw` only if explicitly stated
by the source. Record `urls_raw` for all discovered map URLs. Download
trail maps and GPX/KML files per §5.4.

## 6.4 Site Network Creation
Create a **Site Network** when:
- A National Heritage Area with a coordinating entity and defined geographic
  identity exists — see §4.5. Individual Sites within the NHA stay at their
  management tier; only the NHA umbrella entity itself is a Tier 1 Site Network.
- A similar multi-site federal designation exists (e.g., a federally designated
  scenic river corridor with a coordinating entity)

Apply the Site Network threshold rules per Site Network Discovery Sub-Procedure
v6.0 §3 — formal designations always qualify under Rule 1.

**If no Site Networks qualify at Tier 1:** Document an explicit null-evidence block
before advancing to Access Point creation. Silence is not a null.

```yaml
entity_type_result:
  tier: 1
  governance_level: Federal & Tribal
  entity_type: Site Network
  result: null
  sources_checked:
    - [URL or source description]
  reasoning: [why no Site Networks qualify — no NHA or formal corridor designation
              found, or coordinating entity not documented, etc.]
```

At minimum, two sources must be checked before concluding null.

## 6.5 Access Point Creation
Create an **Access Point** when:
- A visitor-facing entry location is documented

Record `features_raw` for all documented amenities at the access point.
Leave `township_raw` and `municipality_raw` blank — GIS-derived only.
Populate `last_verified_date` with today's date; set `field_verified: false`.

------------------------------------------------------------
# 7. TIER-SPECIFIC EXPECTATIONS

Tier 1 **must** surface:
- All federal Sites
- All tribal Sites (if any)
- All child Sites within federal Sites
- All federal Trailthings (trails, trail sections, trail systems)
- All federal Site Networks (NHAs, designated corridors)
- All federal or tribal Access Points
- All tribal cultural Sites

Tier 1 **may** surface:
- BLM mineral rights Sites (if identity-bearing)
- DoD recreation areas (if public access exists)
- Federal easements (if identity-bearing)

Tier 1 **must not** surface:
- Administrative buildings
- Non-public federal facilities
- Non-identity-bearing parcels
- Tribal cultural Sites as tribal land

------------------------------------------------------------
# 8. METADATA REQUIREMENTS

Each discovered entity must include:
- All raw source references
- All counties (raw)
- All conflicts and uncertainties
- All parent relationships (for child Sites and Access Points)
- `description_raw` for Sites and Access Points (if narrative description
  exists on the source page)
- `features_raw` for Sites and Access Points (if an amenity/facilities list
  is documented)
- `source_term_raw` and `source_hierarchy_context_raw` for Trailthings
- `difficulty_raw` and `accessibility_raw` for Trailthings (only if explicitly
  stated by authoritative source)
- `urls_raw` for all entity types (map URLs included)

`township_raw` and `municipality_raw` must be blank.
All values must be raw and unnormalized.

------------------------------------------------------------
# 9. OUTPUT REQUIREMENTS

Each federal or tribal entity must output a Raw Discovery Record conforming to:
- The appropriate v6.0 Schema Module
- The appropriate v6.0 Vocabulary Module

No normalized fields may appear in Tier 1 output.

------------------------------------------------------------
# 10. INTEGRATION POINTS

This module integrates with:
- Discovery Orchestration Module v6.0
- Site Discovery Sub-Procedure v6.0
- Trailthing Discovery Sub-Procedure v6.0
- Site Network Discovery Sub-Procedure v6.0
- Access Point Discovery Sub-Procedure v6.0
- Resolution Engine v6.x *(or v5.x)*
- Audit & Logging Module v6.x *(or v5.x)*

------------------------------------------------------------
# 11. MODULE DEPENDENCIES

This module depends on:
- Discovery Orchestration Module v6.0 *(for document collection rules, §4)*
- Site Discovery Sub-Procedure v6.0
- Trailthing Discovery Sub-Procedure v6.0
- Site Network Discovery Sub-Procedure v6.0
- Access Point Discovery Sub-Procedure v6.0
- Resolution Engine v6.x *(or v5.x)*
- Audit & Logging Module v6.x *(or v5.x)*

------------------------------------------------------------
# END OF FEDERAL & TRIBAL LANDS DISCOVERY SUB-PROCEDURE v6.0
