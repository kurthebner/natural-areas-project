# NATURAL AREAS PROJECT
# FEDERAL & TRIBAL LANDS DISCOVERY SUB-PROCEDURE v5.2
(Tier 1 — U.S. Federal Agencies & Tribal Lands)

This module defines the authoritative, deterministic Tier-1 discovery rules for
federal and tribal lands within the v5.x Raw → Resolution → Normalization →
Entity Graph pipeline.

This module supersedes Federal & Tribal Lands Discovery Sub-Procedure v5.1.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v5.x Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- Added `description_raw` to Metadata Requirements — must be captured when a narrative description exists on the source page; distinct from `features_raw`
- Added first-pass capture rule to §5.1: when fetching a federal unit page, extract description_raw and features_raw in the same fetch — no deferred return visits
- Bumped version to v5.2

------------------------------------------------------------
# CHANGES FROM v5.0

- **OBS-004**: USACE co-managed land flag added to §3.4 and new §4.5 — when USACE owns
  the lake/reservoir and ODNR manages the surrounding land, both entities must be
  created and cross-flagged for downstream tier assignment review
- **OBS-005**: NRHP archaeological sites on federal land added to §6.1 — companion rule
  to the private land NRHP rule in Resolution Rules v5.x; federal NRHP sites are
  surfaced as Sites or child Sites depending on their relationship to parent federal units

------------------------------------------------------------
# 1. PURPOSE

The Federal & Tribal Lands Discovery Sub-Procedure v5.x defines how Tier 1 must:

- Identify all federal Sites
- Identify tribal lands, tribal ownership, and tribal cultural Sites
- Identify Trails, Trail Segments, and Trail Networks on federal lands
- Identify child Sites within federal Sites
- Identify Access Points associated with federal or tribal Sites
- Distinguish federal management from state/local co-management
- Avoid false positives from similarly named places
- Log uncertainty and boundary cases
- Produce Raw Discovery Records v5.x
- Produce Discovery Metadata v5.x

This module is referenced only by:

- Discovery Protocol Module v5.x
- Discovery Orchestration Module v5.x

------------------------------------------------------------
# 2. SCOPE

This sub-procedure applies to all federal agencies and tribal land categories:

- U.S. Forest Service (USFS)
- National Park Service (NPS)
- U.S. Fish & Wildlife Service (USFWS)
- U.S. Army Corps of Engineers (USACE)
- Bureau of Land Management (BLM)
- Department of Defense (DoD)
- Tribal trust land registries
- Tribal fee-simple ownership
- Tribal cultural Sites

It governs discovery of:

- Sites
- Child Sites
- Trails
- Trail Segments
- Trail Networks
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
- USFS recreation maps
- Special management area datasets
- Campground datasets
- Trailhead datasets

## 3.2 National Park Service (NPS)
Required sources:
- NPS unit pages
- NPS boundary datasets
- NPS recreation maps
- NPS trail datasets
- National Heritage Area documentation

## 3.3 U.S. Fish & Wildlife Service (USFWS)
Required sources:
- Refuge pages
- Refuge boundary datasets
- USFWS recreation maps
- USFWS trail datasets
- Waterfowl Production Area datasets

## 3.4 U.S. Army Corps of Engineers (USACE)
Required sources:
- USACE project pages
- USACE recreation maps
- USACE facility datasets
- Boat ramp datasets
- Campground datasets

**USACE–ODNR Co-Management Pattern**: USACE frequently owns the lake/reservoir
impoundment and surrounding project boundary, while ODNR manages the adjacent
recreation lands and wildlife areas under license or lease. These are two distinct
entities that must both be surfaced:

- The USACE project (lake, dam, project boundary) → Tier-1 Site
- The ODNR-managed recreation areas and wildlife areas within the project boundary → Tier-2 Sites

Flag each with: `USACE_ODNR_COMANAGED — verify tier assignment in normalization`

Both entities must be created. Do not collapse them into one record. The USACE
project boundary and the ODNR recreation lands often have different names, acreages,
and governance structures. Examples in Ohio: Caesar Creek Lake (USACE) / Caesar Creek
State Park and Caesar Creek Wildlife Area (ODNR).

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

All sources must be logged in **Discovery Metadata v5.x**.

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

## 4.5 USACE–ODNR Split Entities
When USACE owns the project boundary and ODNR manages recreation lands within it:

1. Create a Tier-1 Site for the USACE project (lake/reservoir/dam)
2. Flag it: `USACE_ODNR_COMANAGED — ODNR recreation entities will appear in Tier 2`
3. In Tier 2, create separate Sites for each ODNR-managed entity within the project
4. Flag each Tier-2 Site: `USACE_ODNR_COMANAGED — USACE project entity created in Tier 1`
5. Record the USACE project name in `identity_notes_raw` of each Tier-2 entity
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

**First-Pass Capture**: When fetching a federal unit or recreation area page, extract ALL available fields in a single pass — including `description_raw` (the narrative paragraph describing the site's character, ecology, or significance) and `features_raw` (the amenity or facilities list). Both fields are typically present on the same page. A return visit to collect fields that were available on first fetch is a process failure. See `na_site_discovery_subproc_v5.4.md` §7.3 for field definitions and source guidance.

## 5.2 Recursive Discovery (URL Propagation)
Tier 1 must recursively follow:
- Internal links within federal domains
- Internal links within tribal registries
- Internal links within USACE project pages

Recursion must stop when:
- The domain is not on the allowlist
- The page is not relevant to Sites, Trails, or Access Points
- The page is a non-recreational administrative page

## 5.3 Recursion Allowlist
- *.nps.gov
- *.fs.usda.gov
- *.fws.gov
- *.usace.army.mil
- *.blm.gov
- *.defense.gov
- *.bia.gov

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

**NRHP Listings on Federal Land**: When a National Register of Historic Places
listing (mound, archaeological site, historic structure, historic district) exists
within a federal land unit:

- If the NRHP feature has its own identity and visitor access → create a child Site
  with `parent_site_id` pointing to the federal unit (assigned in normalization)
- If the NRHP feature is part of the federal unit's identity (e.g., a CCC historic
  district within a state forest that is itself NRHP-listed) → add to the parent
  Site record's `identity_notes_raw`: "NRHP-listed: [name], [ref]"
- During discovery, create an independent raw record for any identity-bearing NRHP
  feature and note the suspected parent in `identity_notes_raw` — do not suppress

Cross-reference: See Resolution Rules Module v5.x §4.15 for the full NRHP
entity-type decision matrix covering federal, state, and private land contexts.

## 6.2 Child Site Creation
Create a **child Site** when:
- A named internal unit exists within a federal Site
- A recreation area, campground, or management area is identity-bearing
- A special management zone is documented

## 6.3 Trail Creation
Create a **Trail** when:
- A named trail appears in federal datasets or maps

Record `difficulty_raw` and `accessibility_raw` only if explicitly stated by the source.
Record `urls_raw` for all discovered map URLs (PDF, interactive, GPX, KML).

## 6.4 Trail Segment Creation
Create a **Trail Segment** when:
- Segment-level geometry or identifiers exist

## 6.5 Trail Network Creation
Create a **Trail Network** when:
- A federally designated multi-trail system exists (e.g., North Country Trail)

## 6.6 Site Network Creation
Create a **Site Network** when:
- A National Heritage Area or similar multi-site federal designation exists

## 6.7 Access Point Creation
Create an **Access Point** when:
- A visitor-facing entry location is documented

Record `features_raw` for all documented amenities at the access point.
Leave `township_raw` and `municipality_raw` blank — GIS-derived only.

------------------------------------------------------------
# 7. TIER-SPECIFIC EXPECTATIONS

Tier 1 **must** surface:
- All federal Sites
- All tribal Sites (if any)
- All child Sites within federal Sites
- All federal Trails
- All federal Trail Segments
- All federally designated Trail Networks
- All federal Site Networks
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

- Full **Discovery Metadata v5.x**
- All raw source references
- All counties (raw)
- All conflicts and uncertainties
- All parent relationships (for child Sites and Access Points)
- All geometry (if available)
- `description_raw` for Sites and Access Points (if a narrative description exists on the source page)
- `features_raw` for Sites and Access Points (if an amenity/facilities list is documented)
- `difficulty_raw` and `accessibility_raw` for Trails and Trail Segments (if explicitly stated)
- `urls_raw` for Trails, Trail Segments, Trail Networks, and Site Networks (map URLs included)

`township_raw` and `municipality_raw` must be blank.
All values must be raw and unnormalized.

------------------------------------------------------------
# 9. OUTPUT REQUIREMENTS

Each federal or tribal entity must output a **Raw Discovery Record** conforming to:

- **Discovery Output Specification v5.x**
- **Discovery Metadata Specification v5.x**
- The appropriate Schema Module v5.x
- The appropriate Vocabulary Module v5.x

No normalized fields may appear in Tier 1 output.

------------------------------------------------------------
# 10. INTEGRATION POINTS

This module integrates with:

- Discovery Protocol Module v5.x
- Discovery Orchestration Module v5.x
- All Entity Discovery Sub-Procedures v5.x
- Child Site Rules Module v5.x
- Discovery Metadata Specification v5.x
- Discovery Output Specification v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- Audit & Logging Module v5.x
- County Baseline Module v5.x

------------------------------------------------------------
# 11. MODULE DEPENDENCIES

This module depends on:

- Discovery Protocol Module v5.x
- Discovery Output Specification v5.x
- Discovery Metadata Specification v5.x
- All six entity Discovery Sub-Procedures v5.x
- Child Site Rules Module v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF FEDERAL & TRIBAL LANDS DISCOVERY SUB-PROCEDURE v5.1
