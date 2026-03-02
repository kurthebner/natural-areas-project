# NATURAL AREAS PROJECT
# DISTRICT-LEVEL PUBLIC LANDHOLDERS DISCOVERY SUB-PROCEDURE v5.1
(Tier 3 — Park Districts, Metro Parks, Joint Recreation Districts, Conservancy Districts, Watershed Districts, Special Districts)

This module defines the authoritative, deterministic Tier-3 discovery rules for
district-level public landholders within the v5.0 Raw → Resolution → Normalization →
Entity Graph pipeline.

This module supersedes District-Level Public Landholders Discovery Sub-Procedure v5.0.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v5.0 Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v5.0

- **OBS-016**: Government conservancy district vs. nonprofit conservancy disambiguation
  added to §2.2 and new §4.5 — statutory conservancy districts (MWCD, Miami
  Conservancy District) are Tier-3 public entities; nonprofit conservancies belong
  in Tier 7 regardless of the word "conservancy" in their name

------------------------------------------------------------
# 1. PURPOSE

The District-Level Public Landholders Discovery Sub-Procedure v5.0 defines how Tier 3 must:

- Identify all district-managed Sites
- Identify child Sites within district Sites
- Identify Trails, Trail Segments, and Trail Networks managed by districts
- Identify Site Networks managed by districts
- Identify Access Points associated with district Sites and Trails
- Distinguish district management from municipal, township, county, state, or federal co-management
- Identify conservancy district lands, watershed district lands, and flood-control lands
- Avoid false positives from similarly named places
- Log uncertainty and boundary cases
- Produce Raw Discovery Records v5.0
- Produce Discovery Metadata v5.0

This module is referenced only by:

- Discovery Protocol Module v5.0
- Discovery Orchestration Module v5.0

------------------------------------------------------------
# 2. SCOPE

This sub-procedure applies to all district-level public landholders in Ohio.

## 2.1 Park & Recreation Districts
- County park districts
- Metro parks systems
- Joint recreation districts

## 2.2 Conservancy & Watershed Districts
- Muskingum Watershed Conservancy District (MWCD)
- Miami Conservancy District
- Joint conservancy districts
- Watershed districts
- Flood-control districts

**CRITICAL — Government Conservancy District vs. Nonprofit Conservancy**:
The word "conservancy" appears in both government district names and nonprofit
organization names. These belong in different tiers:

- **Government conservancy districts** (Tier 3): Created by Ohio statute, have taxing
  authority or statutory land management powers. Examples: MWCD, Miami Conservancy
  District, watershed conservancy districts. These are public entities and belong here.
- **Nonprofit conservancies** (Tier 7): Private 501(c)(3) organizations that use
  "conservancy" or "conservancy district" in their name informally. Examples: local
  land trusts with "conservancy" in their name. These belong in Tier 7.

To determine which tier applies, check:
1. Does the organization have a statutory formation under Ohio Revised Code? → Tier 3
2. Is the organization a 501(c)(3) nonprofit? → Tier 7
3. Does it have taxing authority or eminent domain powers? → Tier 3
4. Is it governed by a publicly appointed board under ORC? → Tier 3

When ambiguous, flag with: `DISTRICT_VS_NONPROFIT — verify statutory authority`

## 2.3 Special Districts
- Districts with statutory authority to own/manage natural areas
- Districts managing lakes, reservoirs, or floodplain corridors
- Districts with recreation or conservation mandates

Tier 3 sits **below State** and **above County**.

------------------------------------------------------------
# 3. AUTHORITATIVE SOURCES (MANDATORY)

Tier 3 must enumerate and recursively explore the following authoritative sources.

## 3.1 Official District Websites
Required sources:
- Park or property listing pages → Sites
- Facility listing pages → child Sites
- Trail pages → Trails
- Trail maps → Trails, Trail Segments
- Access point listings → Access Points
- District-managed programs or networks → Site Networks, Trail Networks

Always **fetch** district listing pages directly — do not rely on search snippets alone.
Extract ALL parks, trails, and facilities listed, not just those prominently featured.

## 3.2 District GIS
Required sources:
- District boundaries → Sites
- Internal units → child Sites
- Trail geometry → Trails, Trail Segments
- Access point layers → Access Points

## 3.3 District Brochures & Maps
Required sources:
- Named parks → Sites
- Named internal areas → child Sites
- Named trails → Trails
- Trailheads, parking, boat access → Access Points

## 3.4 County Auditor / County GIS
Required sources:
- Parcels owned by the district → Sites
- Parcels leased or co-managed → Sites or child Sites

## 3.5 Partner Agencies
Required sources:
- Co-managed parks
- Joint recreation districts
- Shared trail systems
- USACE partnerships (e.g., MWCD lakes)

All sources must be logged in **Discovery Metadata v5.0**.

------------------------------------------------------------
# 4. DOMAIN RULES FOR DISTRICT-LEVEL DISCOVERY

## 4.1 Multi-County Districts
Districts may span multiple counties.

Rules:
- **Do NOT segment multi-county Sites**
- Record all counties in `counties_raw` exactly as discovered

## 4.2 Conservancy Districts
Examples: MWCD, Miami Conservancy District

Check for:
- Lakes and reservoirs → Sites
- Recreation areas → Sites or child Sites
- Shoreline access → Access Points
- Flood-control lands → Sites
- Multi-site lake systems → Site Networks
- Multi-trail lake corridors → Trail Networks

## 4.3 Watershed & Flood-Control Districts
Check for:
- Floodplain corridors → Sites
- River access → Access Points
- Multi-county river systems → Site Networks
- District-managed trails → Trails

## 4.4 Co-Management
Districts may co-manage Sites with:
- Municipalities
- Townships
- Counties
- ODNR
- USACE

Record all co-management details in metadata; do not attempt to resolve.

## 4.5 Government Conservancy District vs. Nonprofit Conservancy
Before creating a Tier-3 entity for any organization with "conservancy" in its name,
verify its legal status:

**Tier 3 (this module) — statutory districts:**
- Formed under Ohio Revised Code Chapter 6101 (Conservancy Districts)
- Or under ORC Chapter 1515 (Soil and Water Conservation)
- Have a board of directors appointed by the court of common pleas
- May have taxing authority
- Examples: MWCD, Miami Conservancy District, any county watershed conservancy district

**Tier 7 (Conservancy sub-procedure) — nonprofits:**
- Formed as 501(c)(3) organizations
- Governed by a self-appointed nonprofit board
- No taxing authority
- Examples: [County] Land Conservancy, [Name] Conservancy (nonprofit land trusts)

If an organization cannot be confirmed as a statutory district, default to Tier 7
and flag: `DISTRICT_VS_NONPROFIT — verify statutory authority before final tier assignment`

------------------------------------------------------------
# 5. ENUMERATIVE + RECURSIVE DISCOVERY RULES

Tier 3 must use both enumerative and recursive discovery.

## 5.1 Enumerative Discovery (Listing Pages)
Tier 3 must enumerate:
- All district property listings
- All district trail listings
- All district facility listings
- All district-managed program listings
- All district GIS datasets

Always **fetch** listing pages directly — do not rely on search snippets alone.
Extract ALL entities listed, not just those prominently featured.

## 5.2 Recursive Discovery (URL Propagation)
Tier 3 must recursively follow:
- Internal links within district domains
- Internal links within partner agency domains (if relevant)

Recursion must stop when:
- The domain is not on the allowlist
- The page is not relevant to Sites, Trails, or Access Points
- The page is administrative or non-recreational

## 5.3 Recursion Allowlist
- *.metroparks.*
- *.parkdistrict.*
- *.parks.*
- *.conservancy.*
- *.watershed.*
- *.mwcd.*
- *.usace.army.mil (for partnerships only)

------------------------------------------------------------
# 6. ENTITY CREATION RULES (TIER-SPECIFIC)

## 6.1 Site Creation
Create a **Site** when:
- District-owned or district-managed
- Identity-bearing (named, mapped, or designated)
- Public access or recreation infrastructure exists
- It influences Access Point logic

Exclude:
- Administrative offices
- Maintenance yards
- Non-public parcels with no identity

## 6.2 Child Site Creation
Create a **child Site** when:
- A named internal unit exists within a district Site
- It meets the **Child Site Rules Module v5.0**

## 6.3 Trail Creation
Create a **Trail** when:
- A named trail appears in district datasets or maps

Record `difficulty_raw` and `accessibility_raw` only if explicitly stated by the source.
Record `urls_raw` for all discovered map URLs (PDF, interactive, GPX, KML).

## 6.4 Trail Segment Creation
Create a **Trail Segment** when:
- Segment-level geometry or identifiers exist

## 6.5 Trail Network Creation
Create a **Trail Network** when:
- A district-managed multi-trail system exists
- A multi-lake or multi-river corridor trail system exists

## 6.6 Site Network Creation
Create a **Site Network** when:
- A district-managed multi-site system exists
- A multi-lake or multi-river system is documented

## 6.7 Access Point Creation
Create an **Access Point** when:
- A visitor-facing entry location is documented

Record `features_raw` for all documented amenities at the access point.
Leave `township_raw` and `municipality_raw` blank — GIS-derived only.

------------------------------------------------------------
# 7. TIER-SPECIFIC EXPECTATIONS

Tier 3 **must** surface:
- All district-managed Sites
- All identity-bearing child Sites
- All district-managed Trails
- All district-managed Trail Segments
- All district-managed Access Points
- All conservancy district Sites (e.g., MWCD lakes, recreation areas)
- All watershed/flood-control district Sites

Tier 3 **may** surface:
- District-managed Trail Networks
- District-managed Site Networks
- District-managed easements
- Flood-control corridors
- Multi-lake or multi-river systems

------------------------------------------------------------
# 8. METADATA REQUIREMENTS

Each discovered entity must include:

- Full **Discovery Metadata v5.0**
- All raw source references
- All counties (raw)
- All conflicts and uncertainties
- All parent relationships (for child Sites and Access Points)
- All geometry (if available)
- `features_raw` for Sites and Access Points (if documented)
- `difficulty_raw` and `accessibility_raw` for Trails and Trail Segments (if explicitly stated)
- `urls_raw` for Trails, Trail Segments, Trail Networks, and Site Networks (map URLs included)

`township_raw` and `municipality_raw` must be blank.
All values must be raw and unnormalized.

------------------------------------------------------------
# 9. OUTPUT REQUIREMENTS

Each district-level entity must output a **Raw Discovery Record** conforming to:

- **Discovery Output Specification v5.0**
- **Discovery Metadata Specification v5.0**
- The appropriate Schema Module v5.0
- The appropriate Vocabulary Module v5.0

No normalized fields may appear in Tier 3 output.

------------------------------------------------------------
# 10. INTEGRATION POINTS

This module integrates with:

- Discovery Protocol Module v5.0
- Discovery Orchestration Module v5.0
- All Entity Discovery Sub-Procedures v5.0
- Child Site Rules Module v5.0
- Discovery Metadata Specification v5.0
- Discovery Output Specification v5.0
- Resolution Engine v5.0
- Normalization Engine v5.0
- Audit & Logging Module v5.0
- County Baseline Module v5.0

------------------------------------------------------------
# 11. MODULE DEPENDENCIES

This module depends on:

- Discovery Protocol Module v5.0
- Discovery Output Specification v5.0
- Discovery Metadata Specification v5.0
- All six entity Discovery Sub-Procedures v5.0
- Child Site Rules Module v5.0
- Audit & Logging Module v5.0

------------------------------------------------------------
# END OF DISTRICT-LEVEL PUBLIC LANDHOLDERS DISCOVERY SUB-PROCEDURE v5.0
