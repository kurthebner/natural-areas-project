# NATURAL AREAS PROJECT
# DISTRICT-LEVEL PUBLIC LANDHOLDERS DISCOVERY SUB-PROCEDURE v5.7
(Tier 3 — Park Districts, Metro Parks, Joint Recreation Districts, Conservancy Districts, Watershed Districts, Soil & Water Conservation Districts, Special Districts)

This module defines the authoritative, deterministic Tier-3 discovery rules for
district-level public landholders within the v5.x Raw → Resolution → Normalization →
Entity Graph pipeline.

This module supersedes District-Level Public Landholders Discovery Sub-Procedure v5.6.

This module contains no controlled vocabularies.
All vocabularies are defined in the appropriate v5.x Vocabulary Modules.

------------------------------------------------------------
# CHANGES FROM v5.6 → v5.7

- **IMP-072 — Ohio Auditor pre-enumeration mandatory**: Added §3.0 as the first and
  mandatory step of §3 AUTHORITATIVE SOURCES. Before consulting official district
  websites or any other source, the discoverer must query the Ohio Auditor of State
  entity search (https://www.auditor.state.oh.us/AuditSearch/Entities) to obtain the
  authoritative list of districts in scope for the current county. This catches districts
  that have no web presence and would otherwise be missed. §3.0 specifies the search
  procedure, what to record, and how to reconcile the Auditor list against the sources
  in §3.1–§3.5.

------------------------------------------------------------
# CHANGES FROM v5.5 → v5.6

- **IMP-029**: Added Pre-Discovery Checklist cross-reference to §5.1 — after enumerating
  district properties from listing pages and before fetching individual entity pages, the
  entity list must be written to the handoff's Pre-Discovery Checklist. Prevents redundant
  re-enumeration after context breaks.
- **IMP-030**: Added Captured Source Data cross-reference to §5.1 — when a structured
  source table (park directory, property listing with addresses) is fetched, it must be
  written verbatim to the handoff's Captured Source Data section immediately, not deferred
  to staging time.

------------------------------------------------------------
# CHANGES FROM v5.4 → v5.5

- **IMP-004 — SWCD tier assignment**: Soil & Water Conservation Districts are Tier 3.
  Added to §2.3 Special Districts scope. Added §4.7 SWCD-Specific Rules: statutory
  basis (ORC Chapter 1515), what to search for, authoritative sources, rarity note,
  and field mapping.

------------------------------------------------------------
# CHANGES FROM v5.3 → v5.4

- Added §4.6 Cross-Tier Greenway Trails (IMP-011): When a trail is primarily managed
  by Tier 3 but is also documented at Tier 6 (or another tier), both tiers stage records.
  The Tier 3 record is canonical when Tier 3 holds primary management responsibility.
  Discovery metadata requirements for cross-tier flagging documented.
- Expanded §6.3 Trail Creation with cross-tier trail note.

------------------------------------------------------------
# CHANGES FROM v5.2 → v5.3

- Added `description_raw` to Metadata Requirements — must be captured when a narrative description exists on the source page; distinct from `features_raw`
- Added first-pass capture rule to §5.1: when fetching a district property page, extract description_raw and features_raw in the same fetch — no deferred return visits
- Bumped version to v5.3

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- Updated all cross-module references to v5.x
- Updated header version to v5.2

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **OBS-016**: Government conservancy district vs. nonprofit conservancy disambiguation
  added to §2.2 and new §4.5 — statutory conservancy districts (MWCD, Miami
  Conservancy District) are Tier-3 public entities; nonprofit conservancies belong
  in Tier 7 regardless of the word "conservancy" in their name

------------------------------------------------------------
# 1. PURPOSE

The District-Level Public Landholders Discovery Sub-Procedure v5.x defines how Tier 3 must:

- Identify all district-managed Sites
- Identify child Sites within district Sites
- Identify Trails, Trail Segments, and Trail Networks managed by districts
- Identify Site Networks managed by districts
- Identify Access Points associated with district Sites and Trails
- Distinguish district management from municipal, township, county, state, or federal co-management
- Identify conservancy district lands, watershed district lands, and flood-control lands
- Avoid false positives from similarly named places
- Log uncertainty and boundary cases
- Produce Raw Discovery Records v5.x
- Produce Discovery Metadata v5.x

This module is referenced only by:

- Discovery Protocol Module v5.x
- Discovery Orchestration Module v5.x

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
- **Soil & Water Conservation Districts (SWCDs)** — one per county, created under ORC
  Chapter 1515; see §4.7 for discovery guidance

Tier 3 sits **below State** and **above County**.

------------------------------------------------------------
# 3. AUTHORITATIVE SOURCES (MANDATORY)

Tier 3 must enumerate and recursively explore the following authoritative sources.
**§3.0 must be completed before any other source in this section.**

## 3.0 Ohio Auditor Pre-Enumeration (MANDATORY FIRST STEP) ✨ IMP-072

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

All sources must be logged in **Discovery Metadata v5.x**.

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

## 4.6 Cross-Tier Greenway Trails

Named trails — especially greenways, multi-park corridors, and regional bikeways — are
frequently documented at both Tier 3 and Tier 6 (and sometimes Tier 2 or Tier 4).
Management tier governs canonical tier assignment (see Discovery Protocol v5.5 §18).

**When Tier 3 is the primary manager:**

- Stage a Tier 3 discovery record for the trail. This is the canonical record.
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

## 4.7 Soil & Water Conservation Districts (SWCDs) ✨ NEW IN v5.5 (IMP-004)

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
used for GIS sub-parcels (Discovery Protocol §11 / Site Discovery Subproc §5 rule 8):
independent identity on the official website is required.

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

**First-Pass Capture**: When fetching a district property or recreation area page, extract ALL available fields in a single pass — including `description_raw` (the narrative paragraph describing the site's character, ecology, or significance) and `features_raw` (the amenity or facilities list). Both fields are typically present on the same page. A return visit to collect fields that were available on first fetch is a process failure. See `na_site_discovery_subproc.md` §7.3 for field definitions, source guidance, and the Description Quality Gate (IMP-032).

**Pre-Discovery Checklist (IMP-029)**: After enumerating district properties from listing pages and before fetching individual entity pages, write the full entity list to the handoff's **Pre-Discovery Checklist**. A context break between enumeration and individual fetches should not require re-enumerating from source. See na-discovery skill.

**Captured Source Data (IMP-030)**: When fetching a structured source table (park directory, property listing with addresses), write it verbatim to the handoff's **Captured Source Data** section immediately — do not defer to staging time. See na-discovery skill.

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
- It meets the **Child Site Rules Module v5.x**

## 6.3 Trail Creation
Create a **Trail** when:
- A named trail appears in district datasets or maps

Record `difficulty_raw` and `accessibility_raw` only if explicitly stated by the source.
Record `urls_raw` for all discovered map URLs (PDF, interactive, GPX, KML).

**Cross-tier trails**: When a named trail is primarily managed by Tier 3 but also appears
in municipal or other tier sources, stage a Tier 3 record regardless. Do not wait for
or defer to another tier's record. See §4.6 and Discovery Protocol v5.5 §18.

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
- All district-owned or district-managed Sites
- All identity-bearing child Sites within district properties
- All district-managed Trails
- All district-managed Trail Segments
- All district-managed Access Points

Tier 3 **may** surface:
- District-managed Trail Networks
- District-managed Site Networks
- Planned parks and trail corridors (if identity-bearing)
- Easements and co-managed parcels (if identity-bearing)

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

Each district entity must output a **Raw Discovery Record** conforming to:

- **Discovery Output Specification v5.x**
- **Discovery Metadata Specification v5.x**
- The appropriate Schema Module v5.x
- The appropriate Vocabulary Module v5.x

No normalized fields may appear in Tier 3 output.

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
# END OF DISTRICT-LEVEL PUBLIC LANDHOLDERS DISCOVERY SUB-PROCEDURE v5.7
