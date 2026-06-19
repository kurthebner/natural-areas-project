# NATURAL AREAS PROJECT
# SITE DISCOVERY SUB-PROCEDURE v5.8
(Authoritative Sub-Procedure for Discovering Sites and Child Sites)

This module defines the authoritative, deterministic workflow for discovering
Sites (including child Sites) across all discovery tiers within the v5.x
Raw → Resolution → Normalization → Entity Graph pipeline.

This document supersedes all v4.x, v5.3, v5.4, v5.5, v5.6, and v5.7 Site discovery logic.

------------------------------------------------------------
# CHANGES FROM v5.7 → v5.8

- **IMP-049 — Activity terms in `features_raw`**: Added ACTIVITY PROHIBITION block to §7.3
  `features_raw`. Activity terms (Hiking, Fishing, Hunting, Horseback Riding, Mountain Biking,
  Swimming, Boating, Paddling, Wildlife Viewing, etc.) sourced verbatim from park websites must
  NOT be recorded in `features_raw`. Activities are implied by site category and trail entities;
  physical infrastructure that enables an activity (e.g., Watercraft Access, Fishing Area,
  Mountain Bike Trail) may be recorded if documented as physical infrastructure by the source.
  Activity terms that appear alongside legitimate physical features in a source list must be
  stripped individually; the remaining physical items are captured normally.

- **IMP-050 — Operational content in `features_raw`**: Added OPERATIONAL CONTENT PROHIBITION
  block to §7.3 `features_raw`. Hours of operation, parking descriptions, access policies,
  permit requirements, seasonal closures, and event listings must NOT be recorded in
  `features_raw`. These belong in `identity_notes_raw` during discovery and are routed to
  `notes` or `status` at normalization. Physical infrastructure terms that happen to appear
  alongside operational detail are captured normally; only the operational annotation is dropped.

- **IMP-051 — Named entity references in `features_raw`**: Strengthened the existing named-entity
  prohibition in §7.3 `features_raw`. "Do NOT record features that are actually Trails, child
  Sites, or Access Points" now explicitly covers named entity references: specific trail names
  (e.g., "Stone Quarry Trail"), named access points, and named child site references must not
  appear in `features_raw`. Generic infrastructure references that do not name a specific
  entity ("Hiking Trail", "Bridle Trail", "Canoe Launch") are permitted.

- **IMP-052 — Description redundancy gate**: Expanded the DESCRIPTION QUALITY GATE in §7.3
  `description_raw` with explicit prohibited opener patterns. Descriptions that open with
  "A [N]-acre [category] located in...", "Located in [municipality/township]...", or a
  direct restatement of the site name as the primary or only identifying content are prohibited.
  Added examples table of zero-value openers. The strip test was clarified: if stripping the
  opener leaves only location/governance boilerplate, the full description is zero-value.

------------------------------------------------------------
# CHANGES FROM v5.6 → v5.7

- **IMP-032 — Description quality gate**: Added DESCRIPTION QUALITY GATE to §7.3
  `description_raw` section. The prior verbatim-capture rule was necessary but not
  sufficient — source descriptions that merely restate the Site name, location,
  governance, category, or acreage have zero information value. IMP-032 adds an
  explicit stripping test and a bad/good examples table so the rule is unambiguous
  in practice. Leave `description_raw` blank when the source description would
  pass entirely through a name+location+governance+acreage filter unchanged.
- **Expanded `identity_notes_raw` guidance**: Added scope guidance and
  "what belongs here vs. elsewhere" list. The single-sentence prior guidance was
  too sparse to prevent the field from becoming a catch-all.

------------------------------------------------------------
# CHANGES FROM v5.5 → v5.6

- **IMP-027 — Features staging prohibition**: Added explicit prohibition in §7.3
  features_raw section: write only to `features_raw` during discovery, never to
  the normalized `features` field. Placeholder text is prohibited in `features_raw`.
  If the source provides no amenity list, leave `features_raw` blank.

------------------------------------------------------------
# CHANGES FROM v5.4 → v5.5

- Revised §5 Identity Rules rule 8 (IMP-016): GIS administrative sub-parcels without
  independent identity on the managing entity's official website are not Sites.
  Exclusion criterion is absence of independent identity — not the naming pattern alone.
  Official website test defined. Non-contiguous/disjunct parcel handling added: when
  GIS sub-parcels are collapsed into one Site, all constituent acreages must be summed
  for acres_raw and the parcel breakdown documented in identity_notes_raw. §9 What Not
  To Do updated accordingly.

------------------------------------------------------------
# CHANGES FROM v5.3 → v5.4

- Expanded `description_raw` guidance: where to look, what constitutes narrative description, verbatim capture rule
- Expanded `features_raw` guidance: where to look, list vs. narrative distinction, raw-only rule
- Added FIRST-PASS CAPTURE RULE: all descriptive fields must be captured in a single page fetch — no deferred return visits
- Added GOVERNANCE_RAW CONTAMINATION RULE: GIS administrative labels (park type, zone classification) must never be written to governance_raw; they belong in category_raw or identity_notes_raw
- Bumped version to v5.4

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.3

- Updated module version to v5.3
- Updated all cross-module references to v5.x
- Updated organizational field cluster to four-field model:
  ownership_raw, governance_raw, partner_agencies_raw, coordination_raw
- Added guidance for collecting partner_agencies_raw (formal partners only)
- Added guidance for collecting coordination_raw (community/volunteer partners only)
- No changes to discovery philosophy or mechanics
- Updated output field model to v5.3:
  gps_raw replaced by gps_lat_raw and gps_lon_raw (split at source)
  geometry_raw removed (GIS-derived geometry prohibited during discovery)
  maps_raw removed; all map URLs recorded in urls_raw
  url_primary renamed to url_primary_raw
  url_all renamed to urls_raw
  notes_raw renamed to identity_notes_raw
- Discovery Output Specification v5.x retired; all references now v5.x
- No changes to required fields or extraction behavior

------------------------------------------------------------
# 1. PURPOSE

The Site Discovery Sub-Procedure v5.3 provides the authoritative workflow for:

- Identifying Site and child Site candidates
- Extracting raw, unnormalized metadata
- Supporting enumerative and recursive discovery
- Preventing misclassification across the six-entity ontology
- Recording tier and URL provenance with field-level source mapping
- Emitting Raw Discovery Records v5.x
- Emitting Discovery Metadata v5.x
- Integrating cleanly with Resolution Engine v5.x

A Site is:
- A named, identity-bearing land unit
- Documented in authoritative sources
- May be a top-level Site or a child Site
- Distinct from Trails, Trail Segments, Trail Networks, Site Networks, and Access Points
- Not an amenity, feature, or temporary management zone

A child Site is an internal identity-bearing unit that meets the criteria in
the Child Site Rules Module v5.x and is represented as a Site with a Parent Site.

This module is authoritative for Site discovery.

------------------------------------------------------------
# 2. DISCOVERY PHILOSOPHY (v5.x)

## 2.1 Core Principle: Discovery = Collection, Normalization = Decisions

Discovery Phase:
- Collect everything you find
- Record exactly as found
- Do not normalize, standardize, or choose between values
- Do not deduplicate URLs or map links
- Do not make vocabulary decisions
- Do not make presentation decisions

Normalization Phase:
- Standardizes vocabulary
- Deduplicates URLs
- Chooses canonical values
- Validates and cleans
- Makes decisions without revisiting websites

## 2.2 When in Doubt: Collect It
If unsure whether to include something:
- Include it
- Record uncertainty in identity_notes_raw
- Let Resolution/Normalization decide

## 2.3 Multiple Sources = Multiple Records
If the same Site appears at multiple URLs:
- Emit separate discovery records
- Do not merge
- Do not detect conflicts
- Resolution handles merging

------------------------------------------------------------
# 3. SCOPE

This sub-procedure applies to all discovery tiers:

1. Federal
2. State
3. District
4. County
5. Township
6. Municipal
7. Conservancy
8. Private
9. Tier-0 Baseline

Each tier must surface Site candidates when applicable.

------------------------------------------------------------
# 4. REQUIRED SOURCES

Each tier must check:

- Official agency websites
- Listing/index pages
- GIS systems and parcel-level data
- Park district site lists
- State and federal inventories
- Planning/stewardship documents
- County auditor parcel data
- Brochures and downloadable maps
- Historic district documentation
- Land trust preserve lists
- Private organization site lists
- Partnership announcements

All sources must be logged in discovery_metadata and source_map.

------------------------------------------------------------
# 5. IDENTITY RULES FOR SITE CANDIDATES

A Site candidate is valid only if:

1. It is explicitly documented as an identity-bearing land unit.
2. It has a stable, identity-bearing name.
3. It is not a Trail, Trail Segment, Trail Network, or Site Network.
4. It is not an Access Point.
5. It is not an amenity or feature.
6. It is not a temporary or unnamed management zone.
7. It is not a parcel unless documented as a Site.
8. It is not a GIS administrative sub-parcel without independent identity. (IMP-016)
   Municipal ArcGIS layers sometimes include administrative sub-parcels alongside
   genuine Sites — for example, "Ballantrae Open Space A" through "Ballantrae Open
   Space H" representing maintenance management zones within a single named open space.
   These GIS-only labels are not independently discoverable Sites.

   **The exclusion criterion is absence of independent identity, not the naming
   pattern alone.** A lettered or numbered GIS label is a signal to investigate, not
   a conclusive basis for exclusion. Apply the following test:

   - Does the managing entity's **official website** (parks page, facilities page,
     or equivalent authoritative non-GIS source) document this unit as a separately
     named, independently accessible location with its own identity? If yes, it may
     be a legitimate child Site or distinct Site — evaluate using the Child Site Rules
     Module v5.x.
   - If the official website documents only the parent unit (e.g., "Ballantrae Open
     Space") and the lettered sub-parcels appear only in the GIS layer, the sub-parcels
     are administrative maintenance zones. Do not create Site records for them.
   - If the answer is ambiguous, flag in identity_notes_raw for review — do not
     create a Site record based on a GIS label alone.

   **Non-contiguous parcels**: A named park or open space may consist of non-contiguous
   land parcels that share a single identity in official sources (e.g., a main parcel
   and a detached woodland annex documented together as one park). These are one Site,
   not multiple Sites. When GIS sub-parcels or disjunct parcels are collapsed into a
   single Site record:

   - Record `acres_raw` as the **sum of all constituent parcel acreages** from the
     GIS layer. Do not record only the largest parcel's acreage or leave acres_raw
     blank because no single GIS record has the total.
   - Record the parcel breakdown in `identity_notes_raw`, e.g.: "Site consists of
     3 non-contiguous GIS parcels: 4.2 ac (main parcel), 3.8 ac (north annex),
     6.1 ac (woodland section) — summed to 14.1 ac for acres_raw"
   - If some sub-parcels have no acreage in the GIS layer, record the known acreage
     and note the gap: "Partial acreage only — 2 of 4 GIS parcels have area values"

A candidate may be a child Site if:
- It is an internal identity-bearing unit within a larger Site, and
- It meets the criteria in the Child Site Rules Module v5.x.

------------------------------------------------------------
# 6. DISCOVERY WORKFLOW

## 6.1 Step 1 — Identify Named Identity-Bearing Land Units
Search all required sources for:
- Parks, preserves, natural areas, wildlife areas, forests
- Conservation areas, historic sites, cemeteries
- Campuses, recreation areas, cultural/heritage sites
- Multi-parcel conservation lands

## 6.2 Step 2 — Verify Identity-Bearing Name
A Site must have:
- A documented, stable name
- Not a temporary project name
- Not a marketing slogan

## 6.3 Step 3 — Determine Whether Candidate Is a Child Site
If internal unit:
- Evaluate using Child Site Rules Module v5.x
- If valid → record parent_site_raw
- If not → treat as feature or ignore

## 6.4 Step 4 — Confirm Site-Level Identity
Candidate must represent a full identity-bearing land unit.

------------------------------------------------------------
# 7. FIELD-BY-FIELD EXTRACTION GUIDE

## 7.1 Core Identity Fields

### name_raw (REQUIRED)
Record exactly as written.

### category_raw (OPTIONAL)
Record exactly as stated; do not normalize.

### subtype_raw (OPTIONAL)
Record only if explicitly stated.

### designation_raw (OPTIONAL)
Record formal designations only.

### status_raw (OPTIONAL)
Record only if explicitly stated.

------------------------------------------------------------
## 7.2 Organizational Fields

### ownership_raw (OPTIONAL)
Record legal owner exactly as stated.

### governance_raw (OPTIONAL)
Record managing/operating organization(s).

### partner_agencies_raw (OPTIONAL) ✨ NEW IN v5.2
Record **formal, documented partner organizations**.
Examples:
- ODNR partnering with USACE
- County park district partnering with a state agency

Do NOT record:
- Volunteer groups
- Informal partners
- Community groups (those go in coordination_raw)

### coordination_raw (OPTIONAL)
Record **community-based, volunteer, or informal partners**.
Examples:
- Friends groups
- Volunteer trail associations

Do NOT record:
- Formal co-operators (those go in partner_agencies_raw)

------------------------------------------------------------
## 7.3 Descriptive Fields

### description_raw (OPTIONAL)
Record a narrative description of the Site exactly as found on the authoritative source. Aim for 1–3 sentences; capture more if the source provides a rich description that would be lost.

Description text is narrative prose — complete sentences that convey the Site’s character, ecology, history, community purpose, or significance. It is almost always in paragraph form on a park webpage, brochure, or PDF.

**Where to find description text:**
- Park homepage: introductory or "About" paragraph
- Brochure or downloadable PDF: opening description section
- Agency website: "About this park," "Overview," or "Park Description" section

**Capture rules:**
- Record verbatim — do not paraphrase, summarize, or combine multiple sources
- If no narrative paragraph is found, leave blank — do not invent or synthesize
- Do not record bullet-point amenity lists here — those belong in features_raw
- Do not record the Site name, address, or acreage here — those have their own fields

**DESCRIPTION QUALITY GATE (IMP-032)**: Before staging a description, apply this
stripping test: mentally remove the Site name, location, governance, category, and
acreage from the text. If nothing substantive remains, the source description has
zero information value — **leave `description_raw` blank**.

A description earns its place only if it conveys something that cannot be inferred
from the structured fields alone. Passing content includes:

- Ecological or habitat character: *"bottomland hardwood forest with spring ephemeral wildflowers along Brush Creek"*
- Physical or geological character: *"dramatic sandstone cliffs rising 80 feet above the Hocking River gorge"*
- Historical or cultural significance: *"site of CCC Camp No. 5; original stone lodge and picnic shelters still standing"*
- Unique access or context: *"only public Scioto River frontage accessible on foot in urban Portsmouth"*
- Programmatic distinctiveness: *"countywide ropes course and outdoor leadership venue; no general recreation use"*

**Zero-value source text — do not stage these patterns:**

| Source text | Why it fails |
|---|---|
| "X Park is a neighborhood park in [City], Ohio." | Restates category + location — both in other fields |
| "X Park serves the residents of [City]." | Restates governance context — nothing distinctive |
| "X is a [N]-acre community park." | Restates acreage + category — both in other fields |
| "X Park is owned and operated by the City of [City]." | Restates governance_raw |
| "A great park for the whole family!" | Marketing copy — zero informational content |
| "X Park offers a variety of recreational amenities." | Vague filler — the amenities belong in features_raw |
| "A 47-acre community park located in Washington Township." | Restates acres + category + township — all in other fields |
| "Located in the northwest part of Columbus near Dublin Road." | Location only — already in location_raw |
| "X Nature Preserve is a nature preserve managed by the county." | Name + category + governance restatement — zero identity content |

**DESCRIPTION REDUNDANCY GATE (IMP-052)**: Even when a description passes the strip test above, certain opener patterns produce descriptions that are redundant with structured fields even when an identity remainder exists. The following opener forms are prohibited:

- **Acreage + category opener**: "A [N]-acre [category] ..." — strip to the identity remainder. If only the opener remains, blank the description.
- **Location opener**: "Located in [municipality/township/county] ..." — strip to identity content that follows. If nothing follows, blank it.
- **Name restatement opener**: "[Site name] is a [category] ..." followed only by location or governance — strip or blank.
- **Combined opener**: "A [N]-acre [category] located in [place] ..." — strip the entire opener; keep only what follows if substantive.

When an opener is stripped and meaningful identity content remains, record the remainder as `description_raw`. When stripping the opener leaves only additional boilerplate (more location, governance, or acreage), leave `description_raw` blank.

If the entire source description matches these patterns (or combination thereof),
leave `description_raw` blank and do not note the absence in `identity_notes_raw`.
A blank description is the correct result when the source offers nothing distinctive.

### features_raw (OPTIONAL)
Record all amenities, facilities, and physical features exactly as listed by the authoritative source.

Features are items from a list — typically shown as bullet points, icon grids, searchable checkboxes, or a "Park Amenities," "Facilities," or "What’s Here" section. They are NOT narrative sentences.

**Where to find features:**
- Park homepage: amenity icon grid, "Facilities" or "Amenities" section
- Parks search or filter page: checkbox-style feature tags attached to the park record
- Brochure or PDF: amenity list or map legend items
- Interactive park finder: feature tags or icons assigned to the park

**Capture rules:**
- Record verbatim as a comma-separated or semicolon-separated list matching the source’s own formatting: e.g., "Picnic shelter, restrooms, fishing pond, playground"
- Do NOT record narrative sentences — those belong in description_raw
- Do NOT record features that are actually Trails, child Sites, or Access Points — including any specific named trail (e.g., "Stone Quarry Trail"), named access point, or named child site reference; generic infrastructure terms ("Hiking Trail", "Bridle Trail", "Canoe Launch") that do not name a specific entity are permitted (IMP-051)
- Do NOT infer or assume features based on category — only record what the source explicitly states
- The Normalization Engine maps features_raw tokens to controlled vocabulary; raw capture is correct and expected — do not attempt to normalize during discovery

**ACTIVITY PROHIBITION (IMP-049)**: Activity terms must NOT be written to `features_raw`, even if the source explicitly lists them. Activities are implied by site category and trail entities and must not appear in the normalized `features` field. If an activity term appears in the source alongside physical infrastructure items, record only the physical items and drop the activity term.

Terms that must be dropped from source lists when capturing `features_raw`:

| Drop | Physical infrastructure equivalent (record instead if documented) |
|---|---|
| Hiking / Walking | Hiking Trail (only if the source documents a named trail infrastructure) |
| Fishing | Fishing Area (only if a designated fishing area is documented) |
| Hunting | Hunting Area (only if a designated hunting zone is documented) |
| Paddling / Canoeing / Kayaking | Watercraft Access |
| Mountain Biking | Mountain Bike Trail |
| Swimming / Wading | Swimming Area or Splash Pad |
| Boating | Boat Launch or Watercraft Access |
| Wildlife Viewing / Birdwatching | Wildlife Observation Platform (only if a structure is documented) |
| Horseback Riding | Bridle Trail (only if a designated equestrian trail is documented) |
| Cross-Country Skiing / Snowshoeing | (no physical infrastructure equivalent; drop entirely) |
| Geocaching / Photography / Nature Study | (no physical infrastructure equivalent; drop entirely) |

When the activity term is the entire item (e.g., "Hiking" as a standalone checkbox), drop it entirely. When it is bundled with infrastructure text (e.g., "Hiking — 3 miles of trails"), record the infrastructure portion only.

**OPERATIONAL CONTENT PROHIBITION (IMP-050)**: Operational content must NOT be written to `features_raw`. Hours, parking descriptions, access policies, permit requirements, seasonal closures, and events are operational metadata — they belong in `identity_notes_raw` during discovery and are routed to `notes` or `status` at normalization.

Content that must NOT appear in `features_raw`:
- Hours of operation: "Open sunrise to sunset", "Open daily 7am–9pm"
- Parking descriptions: "Small gravel parking lot (8 spaces)", "Street parking only"
- Access policies: "Dogs permitted on leash", "No bikes allowed"
- Permit requirements: "Permit required for shelter rental", "Fee area"
- Seasonal closures: "Trails closed November–March", "Hunting season closures"
- Event listings: "Annual Fall Festival", "Wetland Discovery Days"
- Facility sub-detail annotations: "Shelter A: electrical outlets, near bathrooms"

If operational content is mixed with a physical feature term in the source list, record the physical feature term alone and drop the annotation. For example: "Picnic Shelter (electrical outlets, 50 capacity)" → record "Picnic Shelter".

If operationally significant (e.g., a permit requirement), record it in `identity_notes_raw`.

**STAGING FIELD PROHIBITION (IMP-027)**: During discovery, write ONLY to `features_raw` — never to `features`. The normalized `features` field is populated exclusively by the Normalization Engine from controlled vocabulary tokens. Writing to `features` directly in a staging record bypasses normalization and will produce schema violations.

Additionally, `features_raw` must contain actual amenity list items from the source. Placeholder text such as "GIS-documented; amenities require individual verification" is prohibited. If no explicit amenity list is present on the source page, leave `features_raw` blank and note the gap in `identity_notes_raw`.

### FIRST-PASS CAPTURE RULE ✨ NEW IN v5.4

When fetching a park’s page, capture description_raw AND features_raw in the same page fetch. A single well-executed page fetch from an authoritative source should yield all of the following without a return visit:
- name_raw, category_raw (if stated), designation_raw (if stated)
- ownership_raw, governance_raw (NEVER include GIS park type labels — see rule below)
- description_raw (the narrative paragraph, if present)
- features_raw (the amenity/facility list, if present)
- location_raw, acres_raw (if stated)
- urls_raw (all URLs including PDFs and maps)

**Returning to a source that was already fetched to collect fields that were available on first visit is a process failure. Capture everything in one pass.**

If a page must be fetched twice (e.g., it was initially fetched for entity identification and detail was missed), document this explicitly in identity_notes_raw.

### GOVERNANCE_RAW CONTAMINATION RULE ✨ NEW IN v5.4

governance_raw must contain only the name(s) of the managing or operating organization(s). It must never contain GIS administrative classification labels.

**Never write to governance_raw:**
- GIS park type labels (e.g., "Community Park," "Neighborhood Park," "Mini Park")
- GIS zone or layer classifications (e.g., "Open Space Layer A," "Park Tier 2")
- ArcGIS field values that describe administrative category, not the managing organization

**If a GIS source provides park type metadata alongside the managing organization:**
- governance_raw: `City of Dublin` ✓
- governance_raw: `City of Dublin; GIS park type: Community Park` ✗

GIS park type labels are category hints, not governance. Record them in category_raw or identity_notes_raw if useful, and discard them from governance_raw entirely.

This rule applies to all GIS import sources (MORPC, county auditor GIS, municipal GIS layers, etc.).

### identity_notes_raw (OPTIONAL)
Use `identity_notes_raw` for flags, conflicts, and contextual notes that do not fit
any structured field. This field is the last resort for content that truly has no
better home — it is not a catch-all for everything that seems important.

**What belongs here:**
- Identity conflicts: *"Name on ODNR website: Shade River State Forest; name on GIS: Shade River Forest"*
- Boundary or county ambiguity: *"GPS in Morgan County but mailing address in Athens County — GIS verify"*
- Dual-name situations: *"Also known as the Bob Evans Farm; both names in active use"*
- Tier or governance uncertainty: *"VERIFY_GOVERNANCE — listed by county recreation dept but may be township-owned"*
- Deferred capture notes: *"Second park entrance and trailhead on south side — not documented on first fetch"*
- Process flags: standard pipeline flags (VERIFY_IDENTITY, MINIMAL_DATA, PLANNED, etc.)
- GIS import context: field values from the import source that don’t map cleanly to schema fields
- NRHP listing references: *"NRHP-listed: Scioto Hopewell Mound Group, ref 87000456"*
- Cross-tier notes: *"Trail also documented at Tier 3 (metro parks); verify primary manager"*
- USACE/ODNR co-management flags

**What does NOT belong here:**
- Descriptions of ecology, character, or history → `description_raw`
- Amenities or facilities → `features_raw`
- The site address or GPS coordinates → `location_raw`, `gps_lat_raw` / `gps_lon_raw`
- The governing organization name → `governance_raw`
- Acreage → `acres_raw`
- Redundant restatement of any other field already populated

------------------------------------------------------------
## 7.4 Location Fields

### location_raw (OPTIONAL)
Record address or geographic description exactly as found.

### acres_raw (OPTIONAL)
Record numeric value only.

### counties_raw (REQUIRED)
Record all counties mentioned.

### county_primary (REQUIRED)
Record the county you are discovering in.

### township_raw (LEAVE BLANK)
GIS-derived later.

### municipality_raw (LEAVE BLANK)
GIS-derived later.

### gps_lat_raw (OPTIONAL)
Record latitude only if explicitly provided by authoritative source. Do not infer or derive.

### gps_lon_raw (OPTIONAL)
Record longitude only if explicitly provided by authoritative source. Do not infer or derive.

------------------------------------------------------------
## 7.5 URL and Map Fields

### url_primary_raw (OPTIONAL)
Record the most authoritative URL.

### urls_raw (OPTIONAL)
Record all URLs discovered, including map URLs (PDFs, JPGs, interactive viewers); do not deduplicate.

------------------------------------------------------------
## 7.6 Parent Site Field

### parent_site_raw (OPTIONAL)
Record parent Site name if explicitly documented.

------------------------------------------------------------
# 8. PROVENANCE TRACKING (v5.x)

## 8.1 Source Mapping (REQUIRED)
Track which fields came from which URLs.

## 8.2 Discovery Tier Context
Record tier_context_township, tier_context_municipality, county_primary.

## 8.3 Multiple Sources = Multiple Records
Emit separate records for each URL.

------------------------------------------------------------
# 9. WHAT NOT TO DO (CRITICAL)

- Do not discover township_raw or municipality_raw
- Do not normalize or standardize
- Do not deduplicate URLs or maps
- Do not merge or detect conflicts
- Do not infer ownership, governance, partner agencies, or parent sites
- Do not make category decisions
- Do not create Site records for GIS administrative sub-parcels that lack independent
  identity on the managing entity's official website; use the official website test
  in §5 rule 8 before excluding or collapsing — and when collapsing GIS sub-parcels
  into one Site, sum all constituent parcel acreages for acres_raw

------------------------------------------------------------
# 10. TIER-SPECIFIC EXPECTATIONS
(unchanged from v5.0; all tiers remain required or optional as defined)

------------------------------------------------------------
# 11. OUTPUT REQUIREMENTS

Each Site candidate must output a Raw Discovery Record conforming to:
- Discovery Output Specification v5.x
- Site Schema Module v5.x
- Discovery Metadata Specification v5.x

------------------------------------------------------------
# 12. QUALITY CHECKLIST

- name_raw recorded exactly
- All available fields extracted
- source_map populated
- township_raw and municipality_raw blank
- No normalization applied
- urls_raw includes all URLs (primary, secondary, and map URLs); not deduplicated
- Features recorded exactly
- GPS only if explicitly provided
- No inferred values
- Tier context documented

------------------------------------------------------------
# 13. INTEGRATION POINTS

This module integrates with:

- Discovery Protocol Module v5.x
- Tier Sub-Procedure Template v5.x
- Site Schema Module v5.x
- Site Vocabulary Module v5.x
- Child Site Rules Module v5.x
- Trail Discovery Sub-Procedure v5.x
- Trail Segment Discovery Sub-Procedure v5.x
- Access Point Discovery Sub-Procedure v5.x
- Site Network Discovery Sub-Procedure v5.x
- Discovery Output Specification v5.x
- Discovery Metadata Specification v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- TSV Output Specifications v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF SITE DISCOVERY SUB-PROCEDURE v5.7