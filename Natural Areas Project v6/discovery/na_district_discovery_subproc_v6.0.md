# NATURAL AREAS PROJECT
# DISTRICT-LEVEL PUBLIC LANDHOLDERS DISCOVERY SUB-PROCEDURE v6.0
(Tier 3 — Park Districts, Metro Parks, Joint Recreation Districts, Conservancy Districts, Watershed Districts, Soil & Water Conservation Districts, Special Districts)

This module defines the authoritative, deterministic Tier 3 discovery rules for
district-level public landholders within the v6.x pipeline.

This module supersedes District-Level Public Landholders Discovery Sub-Procedure v5.7.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v6.x Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v5.7 → v6.0

- **Entity type references updated throughout**: Trail, Trail Segment, and Trail
  Network are unified into the single Trailthing entity type. §1 Purpose, §6 Entity
  Creation Rules, §7 Tier-Specific Expectations, and §8 Metadata Requirements
  updated accordingly. §6.3–6.5 (Trail, Trail Segment, Trail Network creation)
  consolidated into §6.3 (Trailthing Creation). §6.6 Site Network renumbered to §6.4;
  §6.7 Access Point renumbered to §6.5.

- **Document Collection added** (§5.4): During Tier 3 discovery, all qualifying
  maps, PDFs, GPX/KML files, GIS exports, and other source documents must be
  downloaded and logged per Discovery Orchestration Module v6.0 §4.

- **All v5.7 rules carried forward**: IMP-072 (Ohio Auditor pre-enumeration),
  IMP-029 (Pre-Discovery Checklist), IMP-030 (Captured Source Data),
  OBS-016 (Government conservancy vs. nonprofit conservancy), IMP-011 (Cross-tier
  greenway trails), IMP-004 (SWCD tier assignment).

------------------------------------------------------------
# 1. PURPOSE

The District-Level Public Landholders Discovery Sub-Procedure v6.0 defines how Tier 3 must:

- Identify all district-managed Sites
- Identify child Sites within district Sites
- Identify Trailthings managed by districts
- Identify Site Networks managed by districts
- Identify Access Points associated with district Sites and Trailthings
- Distinguish district management from municipal, township, county, state, or federal co-management
- Identify conservancy district lands, watershed district lands, and flood-control lands
- Avoid false positives from similarly named places
- Log uncertainty and boundary cases
- Produce Raw Discovery Records v6.x
- Download and log source documents per the Document Collection System

This module is referenced only by:
- Discovery Protocol Module v6.x
- Discovery Orchestration Module v6.0

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

**CRITICAL — Government Conservancy District vs. Nonprofit Conservancy** (OBS-016):
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
- **Soil & Water Conservation Districts (SWCDs)** — one per county, created under ORC
  Chapter 1515; see §4.7 for discovery guidance

Tier 3 sits **below State** and **above County**.

------------------------------------------------------------
# 3. AUTHORITATIVE SOURCES (MANDATORY)

Tier 3 must enumerate and recursively explore the following authoritative sources.
**§3.0 must be completed before any other source in this section.**

## 3.0 Ohio Auditor Pre-Enumeration (MANDATORY FIRST STEP) — IMP-072

Before consulting official district websites, county GIS, or any other source, search
the Ohio Auditor of State's entity database to obtain the authoritative enumeration of
districts in scope for the county being processed.

**Search URL**: https://www.auditor.state.oh.us/AuditSearch/Entities

**Procedure**:
1. Navigate to the Auditor entity search.
2. Filter by county and by entity type. Relevant entity types include:
   - Park Districts
   - Joint Recreation Districts
   - Conservancy Districts
   - Watershed Districts
   - Soil & Water Conservation Districts
   - Special Districts (review for any recreation or land-management mandate)
3. Record each returned entity name in the session handoff's Pre-Discovery Checklist
   before proceeding.
4. For each entity on the Auditor list, proceed to §3.1–§3.5 sources to discover
   properties and entities managed by that district.

**Why this is mandatory**: Many districts have no public web presence and no GIS footprint.
The Auditor list is the only authoritative enumeration of legally constituted districts.
A discoverer who skips §3.0 and works only from §3.1–§3.5 will miss web-dark districts
entirely — the source gap will never be visible in the session log.

**Reconciliation**: If a district appears on the Auditor list but no properties are found
via §3.1–§3.5, record a null tier result for that district with the Auditor entry as the
documented source and a note that no properties were located. Do not silently skip it.

**Ohio Auditor Canvass Block (copy into session log for each county)**:
```
Ohio Auditor pre-enumeration complete — [date]
  URL: https://www.auditor.state.oh.us/AuditSearch/Entities
  County filter: [county name]
  Entity types searched: Park Districts, Joint Recreation Districts, Conservancy Districts,
    Watershed Districts, SWCDs, Special Districts
  Entities found: [count]
  Entity names: [list]
  Web-dark (no §3.1 web presence found): [list or "none"]
```

## 3.1 Official District Websites
Required sources:
- Park or property listing pages → Sites
- Facility listing pages → child Sites
- Trail pages → Trailthings
- Trail maps → Trailthings (download per §5.4)
- Access point listings → Access Points
- District-managed programs or networks → Site Networks

Always **fetch** district listing pages directly — do not rely on search snippets alone.
Extract ALL parks, trails, and facilities listed, not just those prominently featured.

## 3.2 District GIS
Required sources:
- District boundaries → Sites
- Internal units → child Sites
- Trail geometry → Trailthings
- Access point layers → Access Points

## 3.3 District Brochures & Maps
Required sources:
- Named parks → Sites
- Named internal areas → child Sites
- Named trails → Trailthings
- Trailheads, parking, boat access → Access Points

Download all qualifying brochures, trail maps, and visitor guides per §5.4.

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

All sources must be logged in discovery metadata.

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
- Multi-lake or multi-river corridor trail systems → Trailthings

## 4.3 Watershed & Flood-Control Districts
Check for:
- Floodplain corridors → Sites
- River access → Access Points
- Multi-county river systems → Site Networks
- District-managed trails → Trailthings

## 4.4 Co-Management
Districts may co-manage Sites with:
- Municipalities
- Townships
- Counties
- ODNR
- USACE

Record all co-management details in metadata; do not attempt to resolve.

## 4.5 Government Conservancy District vs. Nonprofit Conservancy
Before creating a Tier 3 entity for any organization with "conservancy" in its name,
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

## 4.6 Cross-Tier Greenway Trailthings

Named trails — especially greenways, multi-park corridors, and regional bikeways — are
frequently documented at both Tier 3 and Tier 6 (and sometimes Tier 2 or Tier 4).
Management tier governs canonical tier assignment.

**When Tier 3 is the primary manager:**

- Stage a Tier 3 discovery record for the Trailthing. This is the canonical record.
- The primary manager is Tier 3 when the district holds primary maintenance and operational
  responsibility (trail is mapped on district website, maintained by district staff, accessed
  via district trailheads, and identified as a district trail in district publications).
- Record comprehensive `governance_raw` evidence: the district name, management basis (e.g.,
  "Metro Parks manages and maintains"), and source URL.
- No special `identity_notes_raw` flag is needed for the canonical record.

**When another tier also documents the trail:**

- Do not suppress or modify the Tier 3 record based on the existence of records at other
  tiers. Cross-tier duplication is correct behavior; Resolution merges them.
- If the Tier 3 source itself references another managing entity (e.g., "trail managed
  jointly with City of X"), add to `identity_notes_raw`:
  `"Cross-tier trail — co-managed with [entity name]; verify primary manager"`

**When management responsibility is unclear:**

- Stage the Tier 3 record with whatever governance evidence exists.
- Add to `identity_notes_raw`: `"Cross-tier trail — management tier uncertain"`
- Do not suppress the record pending clarification.

## 4.7 Soil & Water Conservation Districts (SWCDs) — IMP-004

### Statutory Basis

SWCDs are political subdivisions of Ohio state government created under ORC Chapter
1515, one per county (88 total). They are governed by a five-member board of
supervisors (three elected, two appointed by the ODNR Director). They have statutory
authority to acquire land and conservation easements for soil and water conservation
purposes. This statutory formation under ORC places them firmly in Tier 3.

### Land Ownership Rarity

Most SWCDs do not own land. Their primary function is technical assistance — erosion
control planning, water quality consulting, agricultural conservation programs. Check
for land holdings as part of Tier 3 discovery, but expect null results in most counties.
Do not assume a SWCD owns land without evidence; document the null result with sources.

### What to Search For

When checking a county's SWCD, look for:
- Named restoration sites, demonstration areas, or conservation parcels
- Riparian buffer strips with distinct identity and public access
- Wetland restoration projects with a formal site name
- Conservation easements held by the SWCD on significant natural lands

**Do not stage**: Agricultural fields under easement with no natural area character,
temporary erosion control demonstration plots, or parcels with no public access and
no distinct identity.

### Authoritative Sources

Check in this order:
1. The county SWCD's official website (typically `[county]swcd.com` or `[county]cd.com`)
2. Ohio Department of Agriculture / ODNR SWCD directory for the county's SWCD contact
3. NRCS (Natural Resources Conservation Service) for jointly managed restoration sites
4. County auditor GIS parcels — search for owner name containing "soil" or "conservation"

### Field Mapping

| Field | Value |
|---|---|
| `governance_raw` | SWCD name exactly as stated (e.g., "Franklin Soil & Water Conservation District") |
| `ownership_raw` | "State of Ohio" — SWCD land is a political subdivision of the state |
| `category_raw` | As stated by the SWCD — typically "Restoration Site," "Demonstration Area," "Nature Area," or "Conservation Area" |
| `discovery_tier` | 3 |

### Verification Flag

If a county auditor GIS parcel is owned by a SWCD but has no web presence on the
SWCD's official site, do not stage it as a Site. Apply the same official-website test
used for GIS sub-parcels (Site Discovery Sub-Procedure v6.0 §5): independent identity
on the official website is required.

------------------------------------------------------------
# 5. ENUMERATIVE + RECURSIVE DISCOVERY RULES

Tier 3 must use both enumerative and recursive discovery.

## 5.1 Enumerative Discovery (Listing Pages)
Tier 3 must enumerate:
- All district property listings
- All district Trailthing listings
- All district facility listings
- All district-managed program listings
- All district GIS datasets

Always **fetch** listing pages directly — do not rely on search snippets alone.
Extract ALL entities listed, not just those prominently featured.

**First-Pass Capture**: When fetching a district property or recreation area page,
extract ALL available fields in a single pass — including `description_raw` (the
narrative paragraph describing the site's character, ecology, or significance) and
`features_raw` (the amenity or facilities list). Both fields are typically present
on the same page. A return visit to collect fields that were available on first fetch
is a process failure. See Site Discovery Sub-Procedure v6.0 §7.3 for field definitions
and the Description Quality Gate.

**Pre-Discovery Checklist (IMP-029)**: After enumerating district properties from
listing pages and before fetching individual entity pages, write the full entity list
to the handoff's Pre-Discovery Checklist. A context break between enumeration and
individual fetches should not require re-enumerating from source.

**Captured Source Data (IMP-030)**: When fetching a structured source table (park
directory, property listing with addresses), write it verbatim to the handoff's
Captured Source Data section immediately — do not defer to staging time.

## 5.2 Recursive Discovery (URL Propagation)
Tier 3 must recursively follow:
- Internal links within district domains
- Internal links within partner agency domains (if relevant)

Recursion must stop when:
- The domain is not on the allowlist
- The page is not relevant to Sites, Trailthings, or Access Points
- The page is administrative or non-recreational

## 5.3 Recursion Allowlist
- *.metroparks.*
- *.parkdistrict.*
- *.parks.*
- *.conservancy.*
- *.watershed.*
- *.mwcd.*
- *.usace.army.mil (for partnerships only)

## 5.4 Document Collection

During Tier 3 discovery, download all qualifying source documents encountered —
trail maps, park brochures, recreation guides, master plans, GPX/KML files, GIS
exports — and log each in the county document log per **Discovery Orchestration
Module v6.0 §4**.

District land units are well-documented. Metro parks systems, conservancy districts,
and regional park authorities typically publish high-quality trail maps, park
brochures, and recreation guides. Download them at discovery time.

Particularly valuable documents to capture at Tier 3:
- Metro parks trail maps and park maps
- Conservancy district recreation maps (MWCD, Miami Conservancy)
- Park district brochures and visitor guides
- Master plans for parks or trail corridors
- GPX/KML files for district-managed trails
- GIS boundary exports for district properties

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
- It meets the Child Site Rules per Site Discovery Sub-Procedure v6.0

## 6.3 Trailthing Creation
Create a **Trailthing** when:
- A named trail, trail section, trail system, or trail network appears in
  district datasets or maps

Capture `source_term_raw` verbatim (how the source describes the entity —
"greenway," "trail system," "connector," "mountain bike trail") and
`source_hierarchy_context_raw` when the source frames the entity in relation
to others. Do not classify the Trailthing as trail vs. trail network vs. trail
segment during discovery — record what the source says.

Record `difficulty_raw` and `accessibility_raw` only if explicitly stated by
the source. Record `urls_raw` for all discovered map URLs. Download trail maps
and GPX/KML files per §5.4.

**Cross-tier Trailthings**: When a named trail is primarily managed by Tier 3
but also appears in municipal or other tier sources, stage a Tier 3 record
regardless. Do not wait for or defer to another tier's record. See §4.6.

## 6.4 Site Network Creation
Create a **Site Network** when:
- A district-managed multi-site system exists
- A multi-lake or multi-river system is documented

Apply the Site Network threshold rules per Site Network Discovery Sub-Procedure
v6.0 §3.

**If no Site Networks qualify at Tier 3:** Document an explicit null-evidence block
before advancing to Access Point creation. Silence is not a null.

```yaml
entity_type_result:
  tier: 3
  governance_level: District
  entity_type: Site Network
  result: null
  sources_checked:
    - [URL or source description]
  reasoning: [why no Site Networks qualify — threshold not met, single-site
              district, no qualifying multi-site system found, etc.]
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

Tier 3 **must** surface:
- All district-owned or district-managed Sites
- All identity-bearing child Sites within district properties
- All district-managed Trailthings (trails, trail sections, trail systems)
- All district-managed Access Points

Tier 3 **may** surface:
- District-managed Site Networks
- Planned parks and trail corridors (if identity-bearing)
- Easements and co-managed parcels (if identity-bearing)

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

Each district entity must output a Raw Discovery Record conforming to:
- The appropriate v6.0 Schema Module
- The appropriate v6.0 Vocabulary Module

No normalized fields may appear in Tier 3 output.

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
# END OF DISTRICT-LEVEL PUBLIC LANDHOLDERS DISCOVERY SUB-PROCEDURE v6.0
