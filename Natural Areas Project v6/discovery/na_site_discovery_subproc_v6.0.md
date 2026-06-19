# NATURAL AREAS PROJECT
# SITE DISCOVERY SUB-PROCEDURE v6.0
(Authoritative Sub-Procedure for Discovering Sites and Child Sites)

This module defines the authoritative, deterministic workflow for discovering
Sites (including child Sites) across all discovery tiers within the v6.x
Raw → Resolution → Normalization → Entity Graph pipeline.

This document supersedes `na_site_discovery_subproc_v5.10.md` for all v6.x
county runs.

------------------------------------------------------------
# CHANGES FROM v5.10 → v6.0

- **Four new raw fields added** (IMP-011, IMP-012, IMP-013):
  - `habitat_type_raw` — ecological/natural character; verbatim from source;
    full capture guidance at §7.4
  - `access_notes_raw` — seasonal access, permit requirements, access caveats;
    full capture guidance at §7.5
  - `last_verified_date` — date field; populate with current date at discovery
  - `field_verified` — boolean; default false at discovery; set true only on
    physical visit

- **Description guidance substantially expanded** (IMP-015, §7.3): Ecological
  and physical character is the priority. All v5.10 quality gates (IMP-032,
  IMP-052) carried forward and extended with v6.0 positive guidance on what
  good description looks like and how to use habitat_type_raw alongside it.

- **Habitat type capture guidance added** (§7.4): New section covering what
  belongs in habitat_type_raw vs. description_raw vs. features_raw, with
  examples.

- **Access notes capture guidance added** (§7.5): New section; notes that
  operational access content that was previously staged in identity_notes_raw
  or notes_raw now has a dedicated field.

- **Entity type references updated throughout**: Trail, Trail Segment, and Trail
  Network are no longer separate entity types. All are now Trailthings. Identity
  rules and non-qualifying cases updated accordingly.

- **Notes_raw scope tightened** (IMP-014, §7.8): notes_raw is a customer-facing
  field at the normalized stage. Pipeline provenance artifacts must not be written
  here even during discovery. Correct scope defined.

- **All v5.10 rules carried forward unchanged**: Edge venue scope (IMP-002),
  GIS sub-parcel rule (IMP-016), description quality gates (IMP-032, IMP-052),
  features prohibitions (IMP-027, IMP-049, IMP-050, IMP-051), cultural
  institution rule (IMP-068), private venue inclusion (IMP-073), first-pass
  capture rule, governance contamination rule.

------------------------------------------------------------
# 1. PURPOSE

The Site Discovery Sub-Procedure v6.0 provides the authoritative workflow for:

- Identifying Site and child Site candidates across all discovery tiers
- Extracting raw, unnormalized metadata including ecological character,
  access conditions, and verification status
- Supporting enumerative and recursive discovery
- Preventing misclassification across the v6.x four-entity ontology
  (Sites, Trailthings, Site Networks, Access Points)
- Emitting Raw Discovery Records conforming to Site Schema v6.0

A **Site** is:
- A named, identity-bearing land unit
- Documented in authoritative sources
- May be a top-level Site or a child Site
- Distinct from Trailthings (linear corridors), Site Networks (organizational
  collections), and Access Points (entry nodes)
- Not an amenity, feature, or temporary management zone

A **child Site** is an internal identity-bearing unit within a larger Site,
meeting the criteria in the Child Site Rules Module v5.x (v6 equivalent pending),
represented as a Site with a populated parent_site_id.

This module is authoritative for Site discovery under v6.x.

------------------------------------------------------------
# 2. DISCOVERY PHILOSOPHY

## 2.1 Core Principle: Discovery = Collection, Normalization = Decisions

**Discovery phase:**
- Collect everything you find
- Record exactly as found in source
- Do not normalize, standardize, or choose between values
- Do not make vocabulary decisions
- Do not deduplicate

**Normalization phase:**
- Standardizes vocabulary
- Deduplicates URLs
- Chooses canonical values
- Validates, cleans, and makes decisions without revisiting websites

## 2.2 When in Doubt: Collect It

If unsure whether to include a candidate:
- Include it
- Record uncertainty in identity_notes_raw
- Let Resolution and Normalization decide

## 2.3 Multiple Sources = Multiple Records

If the same Site appears at multiple URLs:
- Emit separate discovery records
- Do not merge
- Do not detect conflicts
- Resolution handles merging

------------------------------------------------------------
# 3. SCOPE

This sub-procedure applies to all discovery tiers:

1. Federal & Tribal
2. State
3. District (Metroparks, conservancy)
4. County
5. Township
6. Municipal
7. Conservancy & Land Trust
8. Private
9. Tier-0 Baseline

Each tier must surface Site candidates when applicable.

## 3.1 Edge Venue Scope (IMP-002)

The following venue types are **in scope** for Site discovery even when they
sit at the edge of what intuitively seems like a "natural area." Do not skip
these because the site type appears marginal or recreational rather than
conservation-oriented:

- **Golf courses** (all — public, semi-private, and private member clubs)
  — Category: Recreation Facility / Subtype: Golf Course
- **Sports complexes** — multi-field athletic parks, soccer complexes,
  tournament facilities
- **Cemeteries** (all — public, private, family, church, veterans, historic,
  active) — Category: Cemetery; subtype per inference rules. Do NOT assign
  Historic Site or Cultural Facility
- **Fairgrounds** — county and municipal fairgrounds with public outdoor land use
- **Shooting ranges / gun clubs** — publicly accessible outdoor ranges
- **Driving ranges** — standalone outdoor recreation venues
- **Entertainment venues with outdoor land use** — outdoor amphitheaters,
  event parks, etc.

The inclusion criterion is **publicly accessible, named, identity-bearing land
use** — not whether the site fits a conservation or parks-department mold.
When uncertain, collect it. Normalization assigns category; discovery does not
pre-filter edge cases out.

------------------------------------------------------------
# 4. REQUIRED SOURCES

Each tier must check authoritative sources appropriate to that tier:

- Official agency websites and listing/index pages
- GIS systems and parcel-level data
- State and federal agency inventories
- County auditor parcel data
- Planning and stewardship documents
- Land trust preserve lists
- Brochures and downloadable maps
- Historic district documentation
- Partnership announcements and co-management documentation

All sources must be logged in discovery_metadata and source_map.

------------------------------------------------------------
# 5. IDENTITY RULES — WHEN TO CREATE A SITE RECORD

A Site candidate is valid only if:

1. It is explicitly documented as an identity-bearing land unit.
2. It has a stable, documented name — not a temporary project label,
   informal description, or marketing slogan.
3. It is not a Trailthing — trail systems, greenways, water trails, and
   trail corridors where the primary identity is the linear route are
   Trailthings, not Sites.
4. It is not a Site Network — organizational collections of sites are
   captured as Site Network records.
5. It is not an Access Point — entry nodes are captured as Access Point
   records.
6. It is not an amenity, feature, or internal component of another site.
7. It is not a temporary or unnamed management zone.
8. It is not a GIS administrative sub-parcel without independent identity.
   (IMP-016 — see §5.1 below for the full test)

**A candidate may be a child Site if:**
- It is an internal identity-bearing unit within a larger Site, AND
- It meets the criteria in the Child Site Rules Module v5.x.

## 5.1 GIS Sub-Parcel Test (IMP-016)

Municipal and county GIS layers sometimes include administrative sub-parcels
alongside genuine Sites — for example, "Ballantrae Open Space A" through
"Ballantrae Open Space H" representing maintenance management zones within a
single named open space.

**The exclusion criterion is absence of independent identity, not the naming
pattern alone.** Apply this test:

- Does the managing entity's **official website** (parks page, facilities page,
  or equivalent authoritative non-GIS source) document this unit as a separately
  named, independently accessible location with its own identity?
  - **Yes** → may be a legitimate child Site or distinct Site; evaluate using
    Child Site Rules Module v5.x
  - **No** → the unit is an administrative maintenance zone; do not create a
    Site record
  - **Ambiguous** → flag in identity_notes_raw; do not create a Site record
    based on a GIS label alone

**Non-contiguous parcels**: A named park may consist of non-contiguous parcels
sharing a single identity in official sources. These are one Site:
- Record `acres_raw` as the **sum of all constituent parcel acreages** from GIS
- Record the parcel breakdown in identity_notes_raw:
  "Site consists of 3 non-contiguous GIS parcels: 4.2 ac (main parcel), 3.8 ac
  (north annex), 6.1 ac (woodland section) — summed to 14.1 ac for acres_raw"
- If some sub-parcels have no acreage in GIS, record the known acreage and note
  the gap

------------------------------------------------------------
# 5b. CULTURAL INSTITUTION CATEGORY ASSIGNMENT (IMP-068)

Discovery sources frequently list cultural institutions alongside parks, leading
to erroneous category assignments. Before assigning or leaving blank `category_raw`,
check the site name against the pattern table below. A matching name **must** receive
the listed category. Defaulting to "Recreation Facility" or leaving `category_raw`
blank for a matching name is a discovery error.

| Name Contains | Assign category_raw | Assign subtype_raw | Notes |
|---|---|---|---|
| "Botanical Garden" / "Botanical Gardens" | Curated Biological Site | Botanical Garden | Includes "X Conservatory and Botanical Gardens" |
| "Conservatory" (standalone) | Curated Biological Site | Botanical Garden | Not performing arts conservatories → Cultural Facility |
| "Arboretum" | Curated Biological Site | Arboretum | |
| "Zoo" / "Zoological" | Curated Biological Site | Zoo | |
| "Aquarium" | Curated Biological Site | Aquarium | |
| "Aviary" | Curated Biological Site | Aviary | |
| "Museum" (as primary identity) | Museum | assign from type context | Not "Museum Building" as a feature name |
| "Science Center" / "Science Museum" | Museum | Science Museum | |
| "Hall of Fame" | Museum | from context | |

**Ambiguous cases**: Assign per the table and record in identity_notes_raw:
"Category assigned per IMP-068 cultural institution rule; verify against
authoritative source."

This rule takes precedence over source context. A museum in a parks department
inventory is still a Museum.

------------------------------------------------------------
# 5c. PRIVATE VENUE INCLUSION — TIER 8 (IMP-073)

At Tier 8 (Private), private recreational and entertainment venues with publicly
accessible outdoor land use are **in scope** — collect as standard raw discovery
records without any review flag.

**In scope — collect without flag:**
- Public and semi-public golf courses
- Sports complexes and tournament facilities with public outdoor fields
- Driving ranges (standalone)
- Outdoor amphitheaters and event parks
- Commercial outdoor recreation venues
- Privately operated campgrounds open to the public

**Field mapping for Tier 8 private venues:**
- `ownership_raw`: owning company/organization name
- `governance_raw`: operating organization name
- `discovery_tier`: 8

**Exclusions — do not collect:**
- Indoor-only venues with no outdoor land component
- Retail commercial properties
- Venues that are exclusively ticketed events with no persistent outdoor
  land identity

------------------------------------------------------------
# 6. DISCOVERY WORKFLOW

## 6.1 Step 1 — Identify Named Identity-Bearing Land Units

Search all required sources for:
- Parks, preserves, natural areas, wildlife areas, forests
- Conservation areas, historic sites, cemeteries
- Campuses, recreation areas, cultural and heritage sites
- Multi-parcel conservation lands
- Golf courses, sports complexes, fairgrounds, shooting ranges (§3.1 — in scope)

## 6.2 Step 2 — Verify Identity-Bearing Name

A Site must have:
- A documented, stable name
- Not a temporary project name, marketing slogan, or GIS administrative label

## 6.3 Step 3 — Determine Whether Candidate Is a Child Site

If this is an internal unit within a larger site:
- Evaluate using Child Site Rules Module v5.x
- If valid → record parent_site_raw
- If not → treat as feature or ignore

## 6.4 Step 4 — Confirm Site-Level Identity

The candidate represents a full identity-bearing land unit that is not a
Trailthing, Site Network, or Access Point.

------------------------------------------------------------
# 7. FIELD-BY-FIELD EXTRACTION GUIDE

## 7.1 Core Identity Fields

### name_raw (REQUIRED)
Record exactly as written in the authoritative source.

### category_raw (OPTIONAL)
Record exactly as stated; do not normalize. Check §5b before assigning or
leaving blank — cultural institution patterns require specific assignment.

### subtype_raw (OPTIONAL)
Record only if explicitly stated by the source. Do not infer subtype during
discovery (normalization handles inference).

### designation_raw (OPTIONAL)
Record formal protective or recognition designations only — state, federal, or
local. Record exactly as found; do not normalize.

### status_raw (OPTIONAL)
Record only if explicitly stated. Do not infer.

------------------------------------------------------------
## 7.2 Organizational Fields

### ownership_raw (OPTIONAL)
Legal title holder — exactly as stated by source. Do not infer from governance.

### governance_raw (OPTIONAL)
Managing or operating organization — exact name only.

**GOVERNANCE CONTAMINATION RULE**: governance_raw must contain only the
managing organization's name. Never write GIS administrative classification
labels here:
- ❌ "City of Dublin; GIS park type: Community Park"
- ✅ "City of Dublin"

GIS park type labels ("Community Park," "Neighborhood Park," "Mini Park")
are category hints. Record them in category_raw or identity_notes_raw and
discard from governance_raw entirely. This rule applies to all GIS import
sources (MORPC, county auditor GIS, municipal GIS layers, etc.).

### partner_agencies_raw (OPTIONAL)
Formal, documented co-operator organizations only.

**Capture:** ODNR partnering with USACE; county park district formally
partnering with a state agency; documented co-management agreements.

**Do NOT capture:** Volunteer groups; informal partners; community groups
(those go in coordination_raw).

### coordination_raw (OPTIONAL)
Community-based, volunteer, or informal partners.

**Capture:** Friends groups; volunteer trail or stewardship associations;
advisory boards with documented involvement.

**Do NOT capture:** Formal co-operators (those go in partner_agencies_raw).

------------------------------------------------------------
## 7.3 Description Field

### description_raw (OPTIONAL)

Narrative description of the Site exactly as found in authoritative sources.
1–4 sentences; capture more when the source offers rich character or ecological
content that would otherwise be lost.

**Priority: ecological and physical character.** Description should convey what
kind of land this is, what its ecological character is, and what makes it
notable. This is the field's primary purpose in v6.0.

**Where to find description text:**
- Park homepage: introductory or "About" paragraph
- Brochure or PDF: opening description section
- Agency website: "About this park," "Overview," or "Park Description" section

**Capture rules:**
- Record verbatim — do not paraphrase, summarize, or combine sources
- If no narrative paragraph is found, leave blank — do not invent or synthesize
- Do not record amenity lists here — those belong in features_raw
- Do not record the site name, address, or acreage as the primary content

**v6.0 guidance on ecological character:** When the source describes habitat,
land cover, geology, or ecological significance, that content belongs in
description_raw AND habitat_type_raw. Capture it in both:
- description_raw: the full narrative sentence from source
- habitat_type_raw: the concise ecological character term (see §7.4)

Example source text: "A 47-acre remnant oak-hickory woodland on a glacial
moraine, one of the few intact upland forest tracts remaining in the county."

- description_raw: "A remnant oak-hickory woodland on a glacial moraine, one
  of the few intact upland forest tracts remaining in the county."
  (strip acreage opener per IMP-052; retain the ecological content)
- habitat_type_raw: "Oak-hickory woodland; glacial moraine setting"

**DESCRIPTION QUALITY GATE (IMP-032)**: Before staging a description, apply
this stripping test: mentally remove the site name, location, governance,
category, and acreage from the text. If nothing substantive remains, the source
description has zero information value — **leave description_raw blank**.

Content that earns its place:
- Ecological or habitat character: *"bottomland hardwood forest with spring
  ephemeral wildflowers along Brush Creek"*
- Physical or geological character: *"dramatic sandstone cliffs rising 80 feet
  above the Hocking River gorge"*
- Historical or cultural significance: *"site of CCC Camp No. 5; original stone
  lodge and picnic shelters still standing"*
- Unique access or context: *"only public Scioto River frontage accessible on
  foot in urban Portsmouth"*
- Programmatic distinctiveness: *"countywide ropes course and outdoor leadership
  venue; no general recreation use"*

**Zero-value patterns — leave description_raw blank for these:**

| Source text | Why it fails |
|---|---|
| "X Park is a neighborhood park in [City], Ohio." | Category + location — both in other fields |
| "X Park serves the residents of [City]." | Governance context — nothing distinctive |
| "X is a [N]-acre community park." | Acreage + category — both in other fields |
| "X Park is owned and operated by the City of [City]." | Restates governance_raw |
| "A great park for the whole family!" | Marketing copy — zero informational content |
| "X Park offers a variety of recreational amenities." | Vague filler — amenities belong in features_raw |
| "X Nature Preserve is a nature preserve managed by the county." | Name + category + governance |

**DESCRIPTION REDUNDANCY GATE (IMP-052)**: Even when a description passes the
strip test, certain opener patterns are prohibited:

- **Acreage + category opener**: "A [N]-acre [category] ..." — strip to the
  identity remainder; if only the opener remains, blank the description
- **Location opener**: "Located in [municipality/township/county] ..." — strip;
  retain only identity content that follows
- **Name restatement opener**: "[Site name] is a [category] ..." followed only
  by location or governance — strip or blank
- **Combined opener**: "A [N]-acre [category] located in [place] ..." — strip
  the entire opener; keep only what follows if substantive

When stripping leaves meaningful identity content, record the remainder.
When stripping leaves only additional boilerplate, leave description_raw blank.
A blank description is the correct result when the source offers nothing
distinctive.

------------------------------------------------------------
## 7.4 Habitat Type Field (NEW IN v6.0)

### habitat_type_raw (OPTIONAL)

**New in v6.0** (IMP-011). Captures the ecological or natural character of the
site — what kind of habitat or land cover type defines it.

**What to capture:**
Ecological or land cover terms drawn from the source description, site name,
managing agency classification, or scientific documentation. Verbatim or concise
paraphrase.

**Examples of useful values:**
- "Wet prairie remnant"
- "Oak-hickory woodland"
- "Riparian corridor"
- "Emergent wetland"
- "Glacial lake"
- "Shrub-scrub wetland"
- "Limestone glade"
- "Old-growth beech-maple forest"
- "Calcareous fen"
- "Sand barrens"
- "Floodplain forest"
- "Vernal pool complex"

**Where to find habitat type information:**
- Site description paragraph (may overlap with description_raw — that's fine)
- Site name itself (e.g., "Cedar Bog State Nature Preserve" → "Bog; calcareous
  fen complex")
- Managing agency classification (e.g., ODNR Wetland Reserve designation)
- State nature preserve management plan excerpts

**Relationship to description_raw:**
If the source has a sentence describing ecological character, capture the
full sentence in description_raw AND distill the concise habitat term into
habitat_type_raw. Both fields may draw from the same source text.

**Relationship to features_raw:**
Features like "Wetland," "Prairie," "Bog" may appear in both habitat_type_raw
and features_raw when:
- The source explicitly lists them as site features, AND
- They also describe the site's dominant ecological character

No conflict — populate both. At normalization, Habitat Type and Features serve
different purposes (characterization vs. amenity query).

**What NOT to capture here:**
- ❌ Amenities ("pavilion," "fishing dock") — those go in features_raw
- ❌ Activities ("hiking," "birdwatching") — those go in features_raw or are dropped
- ❌ Governance labels ("ODNR Wildlife Area") — those go in governance_raw
- ❌ Category labels ("nature preserve," "park") — those go in category_raw
- ❌ Geographic names ("near the Maumee River") — those go in location_raw

**When to leave blank:**
- Sites with no meaningful ecological character (purely developed sites,
  cemeteries, sports complexes, fairgrounds)
- Sites where ecological type is undocumented in available sources

Blank is acceptable and does not need documentation. Habitat Type will be
populated during verification passes for substantive natural areas where
sources were thin at discovery time.

------------------------------------------------------------
## 7.5 Access Notes Field (NEW IN v6.0)

### access_notes_raw (OPTIONAL)

**New in v6.0** (IMP-012). Captures seasonal access restrictions, public access
status detail, and access caveats.

**What to capture:**
- Seasonal restrictions: "Closed to public during deer gun season (Nov–Dec)"
- Permit requirements: "Access by permit only — contact ODNR Division of Natural
  Areas at [number]"
- Hours: "Day use only, dawn to dusk; gate locked at sunset"
- Public access status: "No public trail access; conservation easement protects
  land but no recreation access provided"
- Physical access caveats: "Accessible from CR-4 only; no on-site parking"
- Entry conditions: "Dogs permitted on leash; hunting permitted in season"

**Relationship to notes_raw:**
Prior to v6.0, access caveats were often staged in identity_notes_raw or
notes_raw. In v6.0, they have their own field. If you find access information
during discovery, put it in access_notes_raw — not notes_raw.

**Relationship to status_raw:**
status_raw captures the overall operational state ("Access Permit Required,"
"No Public Entry"). access_notes_raw explains the details: why, how, when,
contact information. Populate both when status implies access conditions.

**When to leave blank:**
Sites with no documented access caveats. The most common case — a site simply
open to the public — needs no access_notes_raw entry.

------------------------------------------------------------
## 7.6 Features Field

### features_raw (OPTIONAL)

Record all amenities, facilities, and physical features exactly as listed by
the authoritative source. Features are list items — bullet points, icon grids,
checkbox tags, or "Amenities" / "Facilities" sections. Not narrative sentences.

**Where to find features:**
- Park homepage: amenity icon grid, "Facilities" or "Amenities" section
- Parks search page: feature tags or checkboxes
- Brochure or PDF: amenity list or map legend items

**Capture rules:**
- Record verbatim as a list matching source formatting
- Do NOT record narrative sentences — those belong in description_raw
- Do NOT record named trail entities, named access points, or named child sites
  (IMP-051); generic infrastructure terms ("Hiking Trail," "Canoe Launch") are
  permitted if they don't name a specific entity
- Do NOT infer features from category
- Do NOT attempt to normalize during discovery

**ACTIVITY PROHIBITION (IMP-049)**: Activity terms must NOT be written to
features_raw. Drop these from source lists; record only the physical
infrastructure equivalent if documented:

| Drop | Physical infrastructure equivalent |
|---|---|
| Hiking / Walking | Hiking Trail (only if source documents the trail infrastructure) |
| Fishing | Fishing Area (only if a designated area is documented) |
| Hunting | Hunting Area (only if a designated zone is documented) |
| Paddling / Canoeing / Kayaking | Watercraft Access |
| Mountain Biking | Mountain Bike Trail |
| Swimming / Wading | Swimming Area or Splash Pad |
| Boating | Boat Launch or Watercraft Access |
| Wildlife Viewing / Birdwatching | Wildlife Observation Platform (only if a structure) |
| Horseback Riding | Bridle Trail (only if a designated equestrian trail) |
| Cross-Country Skiing / Snowshoeing | (no physical equivalent; drop entirely) |
| Geocaching / Photography / Nature Study | (no physical equivalent; drop entirely) |

**OPERATIONAL CONTENT PROHIBITION (IMP-050)**: Do NOT write to features_raw:
hours of operation, parking descriptions, access policies, permit requirements,
seasonal closures, or event listings. These go in access_notes_raw or
identity_notes_raw. If operational content is bundled with a physical feature
term, record the feature and drop the annotation.

**STAGING FIELD PROHIBITION (IMP-027)**: Write ONLY to features_raw during
discovery — never to `features`. If no explicit amenity list is present, leave
features_raw blank. Placeholder text is prohibited.

------------------------------------------------------------
## 7.7 Location and Geography Fields

### location_raw (OPTIONAL)
Address or geographic description exactly as found. For navigation to the site.

### acres_raw (OPTIONAL)
Numeric value only. Do not include units. Do not estimate.

### counties_raw (REQUIRED)
All counties mentioned or applicable.

### county_primary (REQUIRED)
The county being discovered in this session.

### gps_lat_raw (OPTIONAL)
Only if explicitly stated by an authoritative source. Never infer or geocode.

### gps_lon_raw (OPTIONAL)
Only if explicitly stated by an authoritative source. Same rules as gps_lat_raw.

### township_raw — ALWAYS BLANK
GIS-derived only. Never populate during discovery.

### municipality_raw — ALWAYS BLANK
GIS-derived only. Never populate during discovery.

------------------------------------------------------------
## 7.8 Notes Field

### notes_raw (OPTIONAL)

Operational context, discovery gaps, and historical notes not captured
in other fields.

**Correct scope:**
- Operational context relevant to understanding the site
- Discovery gaps: "Member trail count not confirmed; ODNR trail register
  listed 3 trails but source was unavailable"
- Historical context not covered by description_raw
- Boundary or jurisdiction notes that don't fit identity_notes_raw

**PROVENANCE PROHIBITION (IMP-014)**: notes_raw flows to the normalized `notes`
field, which is customer-facing. Do not write pipeline provenance artifacts here:
- ❌ Source attribution: "Source: MORPC GIS layer"
- ❌ Batch processing notes: "MORPC batch load; amenities require verification"
- ❌ IMP references: "See IMP-031 for GPS fill-forward"
- ❌ GPS acquisition notes: "GPS from county auditor GIS"

Source provenance belongs in the discovery_metadata source_map and provenance
tables — not in the Notes field.

**Access information belongs in access_notes_raw**, not notes_raw. If you find
seasonal restrictions, permit requirements, or access caveats, put them in
access_notes_raw.

------------------------------------------------------------
## 7.9 URL Fields

### url_primary_raw (OPTIONAL)
Most authoritative URL for the site. Site-specific page preferred over agency
homepage.

### urls_raw (OPTIONAL)
All URLs discovered, including map URLs (PDFs, interactive viewers, GIS layers).
Do not deduplicate.

------------------------------------------------------------
## 7.10 Parent Site Field

### parent_site_raw (OPTIONAL)
Parent Site name if this is a child Site and the parent is explicitly documented
in the source.

------------------------------------------------------------
## 7.11 Verification Fields (NEW IN v6.0)

### last_verified_date
DATE field (YYYY-MM-DD). Populate with the current date at discovery time.
This records when the record was created from active source review — not when
the pipeline ran.

### field_verified
Boolean, default false. Do not set to true during web-based discovery.
Set to true only when the user has physically visited the site. At discovery
time, always false.

------------------------------------------------------------
## 7.12 eBird Hotspot ID (NEW IN v6.0)

### ebird_hotspot_id (OPTIONAL)
The eBird hotspot identifier for this site, if one exists. Format: `L` followed
by digits (e.g., `L123456`).

**How to check:** On [ebird.org/explore](https://ebird.org/explore), search by
site name or navigate to the site's GPS location on the map. If an eBird hotspot
exists, its L-code appears in the URL (e.g., `ebird.org/hotspot/L123456`).

Capture at discovery time while the site source is open — it takes seconds and
enables linking this record to eBird sighting data in external systems.

Leave blank if no hotspot is found. Do not invent or infer one. Do not capture
personal eBird location IDs — only official eBird hotspots (shared public locations).

------------------------------------------------------------
# 8. FIRST-PASS CAPTURE RULE

When fetching a site's authoritative page, capture ALL fields in the same
page fetch. A single well-executed fetch should yield:

- name_raw, category_raw, designation_raw
- ownership_raw, governance_raw, partner_agencies_raw, coordination_raw
- description_raw (narrative paragraph, if present and passing quality gate)
- habitat_type_raw (ecological/land cover terms, if present)
- features_raw (amenity/facility list, if present)
- access_notes_raw (access restrictions or conditions, if present)
- location_raw, acres_raw
- urls_raw (all URLs including PDFs and maps)

**Returning to a source already fetched to collect fields available on first
visit is a process failure. Capture everything in one pass.**

If a page must be fetched twice (e.g., initially fetched for entity identification
and detail was missed), document this in identity_notes_raw.

------------------------------------------------------------
# 9. IDENTITY NOTES FIELD

### identity_notes_raw (OPTIONAL)

Use for flags, conflicts, and contextual notes that have no better home. This
is not a catch-all — use structured fields first.

**What belongs here:**
- Identity conflicts: "Name on ODNR website: Shade River State Forest; name on
  GIS: Shade River Forest"
- Boundary or county ambiguity: "GPS in Morgan County but mailing address in
  Athens County — GIS verify"
- Dual-name situations: "Also known as the Bob Evans Farm; both names active"
- Governance uncertainty: "VERIFY_GOVERNANCE — listed by county recreation dept
  but may be township-owned"
- Category assignment notes from §5b: "Category assigned per IMP-068 cultural
  institution rule; verify against authoritative source"
- Pipeline flags: VERIFY_IDENTITY, MINIMAL_DATA, PLANNED, CROSS_COUNTY_CANDIDATE
- GIS import context not mapping cleanly to schema fields
- Non-contiguous parcel documentation (see §5.1)
- Child Site evaluation notes

**What does NOT belong here:**
- Ecological descriptions or habitat character → habitat_type_raw
- Access restrictions or conditions → access_notes_raw
- Amenities → features_raw
- Site address or GPS coordinates → location_raw, gps fields
- Governance name → governance_raw
- Acreage → acres_raw
- Operational context notes → notes_raw

------------------------------------------------------------
# 10. WHAT NOT TO DO (CRITICAL)

- Do not populate township_raw or municipality_raw — GIS-derived only
- Do not normalize or standardize any field during discovery
- Do not deduplicate URLs or maps
- Do not merge candidates or detect conflicts
- Do not infer ownership, governance, or parent sites
- Do not make category decisions beyond the §5b cultural institution rule
- Do not write pipeline provenance into notes_raw — that belongs in provenance tables
- Do not write activity terms to features_raw (IMP-049)
- Do not write operational content to features_raw (IMP-050)
- Do not write access information to notes_raw — use access_notes_raw
- Do not create Site records for GIS administrative sub-parcels without
  independent identity (apply the §5.1 official website test)
- Do not set field_verified = true during web-based discovery

------------------------------------------------------------
# 11. COMPLETE RAW DISCOVERY RECORD TEMPLATE

```yaml
entity_type: Site
name_raw:
category_raw:
subtype_raw:
designation_raw:
status_raw:
ownership_raw:
governance_raw:
partner_agencies_raw:
coordination_raw:
description_raw:
habitat_type_raw:
features_raw:
access_notes_raw:
location_raw:
acres_raw:
counties_raw: []
county_primary:
gps_lat_raw:
gps_lon_raw:
boundary_document_raw:
urls_raw: []
ebird_hotspot_id:      # eBird L-code if site has a known hotspot (e.g. L123456); blank if none
identity_notes_raw:
parent_site_raw:
township_raw:          # BLANK — GIS-derived only
municipality_raw:      # BLANK — GIS-derived only
last_verified_date:
field_verified: false
discovery_tier:
seeded_from_baseline:
baseline_id:
```

**Fields always blank at discovery:** township_raw, municipality_raw
**Fields never blank at discovery:** entity_type, name_raw, county_primary,
  discovery_tier, last_verified_date (current date), field_verified (false)

------------------------------------------------------------
# 12. ENTITY TYPE SEQUENCE WITHIN TIERS

Within each discovery tier, process entity types in this order:

**Sites → Trailthings → Site Networks → Access Points**

Trail Networks, Trails, and Trail Segments are no longer separate entity types.
All are captured as Trailthings.

------------------------------------------------------------
# 13. QUALITY CHECKLIST

Before closing any Site discovery pass:

- [ ] name_raw recorded exactly as found
- [ ] category_raw assigned or noted per §5b cultural institution rule
- [ ] governance_raw contains only organization name — no GIS labels
- [ ] description_raw passes quality gate (IMP-032, IMP-052) or is blank
- [ ] habitat_type_raw populated for substantive natural areas where source
      provides ecological language
- [ ] features_raw contains no activity terms (IMP-049) and no operational
      content (IMP-050)
- [ ] access_notes_raw populated where access conditions are documented
- [ ] notes_raw contains no provenance artifacts
- [ ] township_raw and municipality_raw are blank
- [ ] GPS only if explicitly provided by authoritative source
- [ ] urls_raw includes all URLs including maps; not deduplicated
- [ ] ebird_hotspot_id checked on ebird.org/explore and populated if a hotspot exists
- [ ] last_verified_date populated with current date
- [ ] field_verified = false
- [ ] All discovered Site records physically staged in the YAML file (not
      just noted above — the file is the record)

------------------------------------------------------------
# 14. MODULE DEPENDENCIES

This module depends on:

- Site Schema Module v6.0 (field definitions)
- Site Vocabulary Module v6.0 (vocabulary reference)
- Child Site Rules Module v5.x *(v6 equivalent pending)*
- Discovery Orchestration Module v6.x *(pending — use v5.3)*
- Resolution Engine v6.x *(or v5.x)*
- Normalization Engine v6.x *(or v5.x)*
- Trailthing Discovery Sub-Procedure v6.x *(pending)*
- Site Network Discovery Sub-Procedure v6.x *(pending)*
- Access Point Discovery Sub-Procedure v6.x *(pending)*

------------------------------------------------------------
# END OF SITE DISCOVERY SUB-PROCEDURE v6.0
