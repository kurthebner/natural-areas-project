# NATURAL AREAS PROJECT
# SITE NETWORK DISCOVERY SUB-PROCEDURE v6.0
(Authoritative Sub-Procedure for Discovering Site Network Entities)

This module defines the authoritative, deterministic workflow for discovering
**Site Network** entities across all discovery tiers within the v6.x pipeline.

This document supersedes Site Network Discovery Sub-Procedure v5.1.

------------------------------------------------------------
# CHANGES FROM v5.1 → v6.0

- **Broadened Site Network definition** (IMP-135): A Site Network is now any
  named organization or designation that manages, coordinates, or encompasses
  two or more Sites in the project. The prior requirement for "explicit
  system-level identity" and "branding distinct from the managing organization"
  is removed. See §3.

- **Four threshold rules replace the old identity gate** (IMP-135): Rules are
  keyed on `network_type_raw` and `org_type_raw`. They replace the
  "system-level identity" test and the gray-area guidance as the primary
  identity gate. See §3.

- **SITE_NETWORK_PROVISIONAL flag added** (IMP-135): When the first member
  site is cataloged for an organization expected to meet threshold, create a
  provisional Site Network record immediately rather than waiting for the
  threshold to be reached. See §3.4.

- **SITE_NETWORK_UNCERTAIN narrowed** (IMP-135): Now reserved for genuinely
  ambiguous cases — unclear which org_type or network_type applies, or where
  the organization's scope cannot be determined. See §3.5.

- **`coordination_raw` field added**: Community-based, volunteer, advisory,
  and informal partners — consistent with the organizational model across all
  v6.x entity types.

- **Notes provenance prohibition added** (IMP-014): Notes is a customer-facing
  field; pipeline source references and process content must not appear here.

- **Description mandate updated** (IMP-015): Ecological/physical character and
  organizational mission are the priority; amenity inventory excluded.

- **Entity type references updated**: Trail Network → Trailthing throughout.
  Site Networks and Trailthings are distinct; trail-system identity goes to
  Trailthing discovery, not Site Network discovery.

------------------------------------------------------------
# 1. PURPOSE

This sub-procedure provides the authoritative workflow for:

- Identifying Site Network candidates
- Applying the four threshold rules to determine whether to create a record
- Creating provisional Site Network records at first member site encounter
- Extracting raw, unnormalized metadata
- Flagging genuinely ambiguous candidates with SITE_NETWORK_UNCERTAIN
- Recording tier and URL provenance
- Emitting Raw Discovery Records conforming to the Site Network Schema Module v6.0
- Integrating with Site, Trailthing, and Access Point discovery
- Feeding the Resolution Engine v6.x

A **Site Network** is a named organization or designation that manages,
coordinates, or encompasses two or more Sites in the project, documented
in authoritative sources.

Site Networks serve two complementary purposes:

**Collection identity**: The network has a name and a defined set of member
Sites — an NHA, a scenic river corridor, a land trust's preserve portfolio,
a park district's parks system.

**Organizational intelligence**: The Site Network record is the canonical
anchor for organization-level information — total member count, primary
website URL, org type, service territory — that cannot be reconstructed by
querying individual Site records alone.

These purposes are not in tension. A metropark district managing 21 parks
both *is* an organization and *has* a collection of parks. Both aspects are
captured in a single Site Network record.

**Examples of qualifying Site Networks under the v6.0 definition:**
- Ohio & Erie Canalway National Heritage Area
- Little Miami Scenic River Corridor
- Muskingum Watershed Conservancy District Lakes
- Metro Parks Serving Franklin County
- Arc of Appalachia Preserve System
- Black Swamp Conservancy
- Wood County Park District
- Columbus Recreation and Parks Department (3+ in-scope sites)

**Not Site Networks:**
- A governance body managing fewer than the applicable threshold of in-scope
  Sites in the project
- A single Site with internal child Sites (use parent_site_id)
- An informal grouping or marketing label with no managing organization
- A Trail/Trailthing network — Trailthings are collections of linear
  trail-related entities; Site Networks are collections of Sites

This sub-procedure is authoritative for **Site Network discovery**.

------------------------------------------------------------
# 2. DISCOVERY PHILOSOPHY

## 2.1 Core Principle: Discovery = Collection, Normalization = Decisions

**Discovery Phase (YOU ARE HERE):**
- Collect everything you find
- Record exactly as found
- Do not normalize, standardize, or choose between values
- Do not deduplicate URLs
- Apply the threshold rules (§3) — create the record or flag as provisional

**Normalization Phase (LATER):**
- Standardize vocabulary
- Choose canonical values
- Validate member site relationships
- Populate member_site_ids

## 2.2 Create Early — Capture Organizational Context

The v6.0 approach favors creating Site Network records early — at first
member site encounter — rather than waiting to confirm threshold. Rationale:
organizational context gathered during discovery (website URL, governance
name, org type, service territory, description) should be captured at
discovery time, not reconstructed later.

When in doubt whether an organization will meet threshold: create the
provisional record. If the threshold is not met by end of full discovery,
evaluate retention at tier close.

## 2.3 Multiple Sources = Multiple Records

If you find the same Site Network at multiple URLs:
- Emit SEPARATE discovery records
- Do NOT attempt to merge
- Resolution Engine handles merging

------------------------------------------------------------
# 3. IDENTITY THRESHOLD — WHEN TO CREATE A SITE NETWORK RECORD

## 3.1 Overview

A Site Network record is created when **any one of the following four
rules** is satisfied. Rules are checked in order; the first matching rule
governs.

These rules replace the prior "system-level identity" test. The governing
variables are `network_type_raw` and `org_type_raw` — capture these fields
accurately to enable threshold evaluation.

---

## 3.2 Rule 1 — Formal Designation (always qualify)

If `network_type_raw` maps to any of these formal designation types:
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

→ Create the Site Network record regardless of member site count. A
formally designated entity exists as a network by definition. Member
sites may be zero at discovery time for newly designated networks.

---

## 3.3 Rule 2 — Conservation and Land-Holding Organizations (2+ member sites)

If `org_type_raw` maps to any of these organization types:
- Land Trust
- Nonprofit Conservancy
- Regional Authority
- County Authority
- State Agency
- Federal Agency

→ Create the Site Network record when **2 or more** member Sites have been
or are expected to be cataloged in this county run.

These organization types are defined by their conservation or land-management
mission. Any such organization managing 2+ in-scope Sites warrants a record.

*Examples: Arc of Appalachia, Black Swamp Conservancy, Metro Parks Serving
Franklin County, Wayne County Park District, Ohio Department of Natural
Resources (for multi-site portfolios within a county).*

---

## 3.4 Rule 3 — Municipal Departments (3+ in-scope member sites)

If `org_type_raw` maps to Municipal Department:

→ Create the Site Network record when **3 or more** in-scope member Sites
have been or are expected to be cataloged.

**"In-scope"** means Sites that are natural areas, open space, conservation
lands, trail-connected parks, or other sites of a similar character. Purely
developed athletic facilities (ballfields, basketball courts, splash pads)
with no natural area component are not in-scope for this count. A site with
both a ballfield and a nature trail or green space is in-scope.

The higher threshold reflects that municipal parks departments often manage
a mix of developed recreation facilities outside project scope.

---

## 3.5 Rule 4 — Other Organizations (3+ member sites, documented rationale)

If `org_type_raw` maps to Other:

→ Create the Site Network record when **3 or more** member Sites are
cataloged, and document in `identity_notes_raw` why a Site Network record
is warranted for this organization.

---

## 3.6 SITE_NETWORK_PROVISIONAL — Create Early

When the **first member Site** is cataloged for an organization expected to
meet threshold (under Rule 2, 3, or 4), **create a provisional Site Network
record immediately**:

```
identity_notes_raw: "SITE_NETWORK_PROVISIONAL — [org name] first member site
cataloged [date]; [N] additional member sites expected. Threshold: Rule [N] —
[applicable rule summary]."
```

Remove the SITE_NETWORK_PROVISIONAL flag when the threshold is met.

If the threshold is not met by end of full discovery, evaluate at tier close:
- Formal designation → retain regardless
- Strong documented expectation of future members from other county runs → retain
- No evidence of additional members → remove the record and document in session log

---

## 3.7 SITE_NETWORK_UNCERTAIN — For Genuine Ambiguity

The SITE_NETWORK_UNCERTAIN flag is now reserved for cases where the applicable
rule **cannot be determined** from available sources:
- It is unclear which org_type applies
- The organization's service territory and scope cannot be determined
- It is ambiguous whether the entity is a Site Network, governance body only,
  or some other entity type

```
identity_notes_raw: "SITE_NETWORK_UNCERTAIN — [specific description of
what is unclear and what sources were checked]"
```

SITE_NETWORK_UNCERTAIN is not a substitute for the provisional record pattern.
Do not use it simply because the threshold has not yet been confirmed.

---

## 3.8 Records That Must Not Be Created

- A single Site with internal child Sites → use `parent_site_id`, not a network
- An informal grouping or marketing label with no managing organization
- A governance body managing fewer than the applicable threshold of in-scope
  Sites in this county run, with no expectation of meeting threshold
- A Trailthing network — trail-system collections belong in Trailthing discovery
- Nested Site Networks — no Site Network may have another Site Network as parent

------------------------------------------------------------
# 4. SCOPE

This sub-procedure applies to all discovery tiers:

1. Federal
2. State
3. District
4. County
5. Township
6. Municipal
7. Conservancy
8. Private
9. Tier-0 Baseline (non-authoritative; runs last)

Each tier must surface Site Network candidates when applicable.

------------------------------------------------------------
# 5. REQUIRED SOURCES

Each tier must check the following for Site Network references:

- Official agency and organization websites
- Authoritative listing/index pages (/parks/, /preserves/, /heritage/, /corridors/)
- GIS systems and interactive maps showing multi-site systems
- Planning documents (master plans, corridor plans, heritage plans)
- Stewardship and management plans
- Federal designation documents (NHA, National Scenic River)
- State designation documents (Ohio Scenic River, ODNR corridor designations)
- Historic District documentation
- Watershed and ecological corridor plans
- Partnership announcements and stewardship agreements
- Multi-site program pages
- Park district or land trust system overview pages
- Regional conservation or heritage initiative pages

All sources must be logged in source_map.

------------------------------------------------------------
# 6. SITE NETWORK VS. RELATED ENTITIES: CRITICAL DISTINCTIONS

## 6.1 Site Network vs. Parent Site with Child Sites

**Site Network (umbrella over multiple separate Sites):**
- ✅ "Wood County Park District" — manages multiple geographically separate parks
- ✅ "Ohio & Erie Canalway" — encompasses multiple distinct sites along corridor
- ✅ "Maumee River Scenic River Corridor" — includes multiple sites along river

**Parent Site with Child Sites (hierarchical containment):**
- ❌ "Heritage Village Historic Park" with "Blacksmith District" inside it
  → One Site with internal child Sites; use parent_site_id

**Key difference:**
- Site Network = collection of **geographically separate** Sites sharing
  identity or management
- Parent Site = one Site **containing** internal identity-bearing areas

## 6.2 Site Network vs. Governance Body (the threshold question)

**Site Network (meets threshold):**
- ✅ Manages 2+ in-scope Sites and org_type = Land Trust / County Authority / etc.
- ✅ Manages 3+ in-scope Sites and org_type = Municipal Department
- ✅ Formal designation regardless of member count

**Governance body only (below threshold or threshold not met):**
- A village parks department that manages 1–2 parks only
- An agency listed as governance on individual Site records but below threshold
- → Record as `governance_raw` on member Sites; do not create Site Network

**When at threshold and org is being actively discovered:** Create the
provisional record (SITE_NETWORK_PROVISIONAL) immediately.

## 6.3 Site Network vs. Trailthing

**Site Network:** Collection of Sites (place-based land units)

**Trailthing:** Named trail-related entity (linear corridor, trail system,
trail network, trail section)

A greenway may produce both a Site Network (the sites along the greenway)
and a Trailthing (the trail system itself). Discover both when both
identities are documented. Do not collapse one into the other.

------------------------------------------------------------
# 7. DISCOVERY WORKFLOW

## 7.1 Step 1 — Identify Named Organizations and Designations

Search all required sources for:

- Named corridors, heritage areas, historic districts (formal designations)
- Scenic river systems and ecological corridor designations
- Cultural landscape networks
- Park district systems and conservation authority portfolios
- Municipal parks departments managing 3+ in-scope Sites
- Land trust preserve portfolios managing 2+ Sites
- State and federal agency multi-site portfolios within the county
- Multi-site conservation programs or networks

## 7.2 Step 2 — Apply the Threshold Rules

For each candidate:

1. Determine `network_type_raw` — does it map to a formal designation type?
   If yes → Rule 1 applies; create the record.
2. If not a formal designation, determine `org_type_raw` — Land Trust, County
   Authority, Municipal Department, etc.
3. Apply the corresponding Rule (2, 3, or 4) based on member site count and
   whether the threshold is expected to be met.
4. If threshold is met or first member site has been cataloged for an
   organization expected to meet threshold → create record (provisional if
   below threshold, active if at or above).
5. If org_type cannot be determined → flag SITE_NETWORK_UNCERTAIN.
6. If clearly below threshold with no expectation of meeting it → do not create;
   record organization name as governance on member Site records.

## 7.3 Step 3 — Capture Organization-Level Fields

For any Site Network record created (including provisional), capture at
discovery time:
- Governance name and URL (the primary website)
- Org type and network type
- Description of organization's mission and service territory
- Counties encompassed
- Any documented member sites

This organizational context cannot be easily reconstructed during normalization.
Capture it when you are actively viewing the organization's website.

------------------------------------------------------------
# 8. FIELD-BY-FIELD EXTRACTION GUIDE

## 8.1 Core Identity Fields

### `network_name_raw` (REQUIRED)
Official published name of the organization or designation, exactly as written.

**Examples:**
- "Wood County Park District" ✅
- "Ohio & Erie Canalway National Heritage Area" ✅
- "Black Swamp Conservancy" ✅
- "Columbus Recreation and Parks Department" ✅

Do not add or remove words. Do not normalize capitalization.

---

### `network_type_raw` (OPTIONAL — capture when inferable)
Record exactly as the source describes the entity type. Normalization maps
to controlled vocabulary. The raw value is what you find in the source.

**Examples of source terms to capture:**
- "national heritage area", "county park district", "land trust",
  "scenic river corridor", "preserve network", "conservation authority"

Even if the source does not explicitly state a type, capture what can be
inferred from the entity's nature and how it presents itself. This field
is essential for threshold rule application.

---

### `org_type_raw` (OPTIONAL — capture when determinable)
The organizational category of the primary governance entity. Essential for
applying Rules 2–4.

**Examples:**
- "county park district" → maps to County Authority
- "city parks department" → maps to Municipal Department
- "land trust" → maps to Land Trust
- "state agency" → maps to State Agency
- "federal agency" → maps to Federal Agency

---

### `status_raw` (OPTIONAL)
Only if explicitly stated. "Proposed" and "Dissolved" are especially important.

## 8.2 Member Fields

### `member_count_raw` (OPTIONAL)
The officially published count of member sites. Do not count yourself.

**Examples:**
- "21 parks in the system" → record "21"
- "16 lakes" → record "16"
- "8 preserves" → record "8"

For provisional records, this reflects confirmed members to date, not the
projected total.

---

### `member_site_names_raw` (OPTIONAL)
Names of member sites, semicolon-delimited, exactly as listed in source.

**Example:**
- "Carter Historic Farm;Oak Openings Preserve;Blue Creek Conservation Area"

Record what you find. Incompleteness is expected and acceptable.

If the source references a count but does not list all members:
```
identity_notes_raw: "Source lists 4 sites; district website states
'21 parks in system' — member list partial."
```

## 8.3 Governance and Organizational Fields

### `governance_raw` (OPTIONAL)
Primary managing agency or organization, exactly as stated.

For organizational portfolio records, governance and network name are
often the same. Record both fields explicitly.

**Examples:**
- "Wood County Park District"
- "National Park Service"
- "Ohio Department of Natural Resources"

---

### `partner_agencies_raw` (OPTIONAL)
Secondary managing agencies or formal organizational partners.
Semicolon-delimited. Only if explicitly documented.

**Look for:** "in partnership with...", "co-managed by...",
"in collaboration with...", "administered by..."

---

### `coordination_raw` (OPTIONAL)
Community-based, volunteer, advisory, or informal partners — friends groups,
stewardship volunteers, watershed councils, trail associations, advisory
boards. Only if documented.

Must not duplicate `governance_raw` or `partner_agencies_raw`.

---

### `ownership_raw` (OPTIONAL)
Legal owner of the network if applicable. Often blank for NHAs, scenic
corridors, and other designating bodies where ownership is distributed.

**Examples:**
- "Wood County" (for county authority)
- "State of Ohio" (for state program portfolio)
- Leave blank for NHAs, scenic corridors, land trust portfolios with
  distributed ownership

## 8.4 Geography Fields

### `counties_raw` (OPTIONAL)
All counties the network encompasses. Semicolon-delimited.

**Examples:**
- "Wood" ✅
- "Cuyahoga;Summit;Portage" ✅

---

### `states_raw` (OPTIONAL)
For multi-state networks only. Blank for Ohio-only networks.

## 8.5 Descriptive Fields

### `description_raw` (OPTIONAL)
1-3 sentences describing the network's identity, character, and mission.

**Priority: character and mission.** Describe what this organization or
designation actually is and does — its conservation mission, geographic
territory, significance, and nature of holdings. A description that says
only "a county park district" tells a reader nothing useful.

**What belongs here:**
- Organization's mission and service territory
- Nature of the designation or portfolio
- Geographic scope and character
- Significance (historic, ecological, recreational)
- Brief establishment history or founding context

**What does NOT belong here:**
- Individual site descriptions or facility inventory → those belong on
  individual Site records
- Amenity lists or operational details → Notes

---

### `identity_notes_raw` (OPTIONAL)
Free-text field for identity clarifications, flags, and disambiguation notes.

**SITE_NETWORK_PROVISIONAL format:**
```
SITE_NETWORK_PROVISIONAL — [org name] first member site cataloged [date];
[N] additional member sites expected. Threshold: Rule [N] — [applicable
rule summary].
```

**SITE_NETWORK_UNCERTAIN format (genuine ambiguity only):**
```
SITE_NETWORK_UNCERTAIN — [specific description of what is unclear and what
sources were checked]
```

**Also use for:**
- Alternate or historical names
- Disambiguation from similar-named entities
- Governance verification notes
- Trailthing/Site Network dual identity notes (when a greenway is both)

---

### `notes_raw` (OPTIONAL)
Operational and contextual notes: funding notes, boundary clarifications,
designation history, partnership context, service territory notes, discovery
gaps.

**Customer-facing field — no provenance artifacts.** Pipeline source
references, IMP numbers, batch load notes, and similar process or provenance
content must not appear here. Notes must be readable by someone who knows
nothing about the pipeline.

Must not include identity-defining characteristics (those belong in
`description_raw` or `identity_notes_raw`).

## 8.6 URL Fields

### `urls_raw` (OPTIONAL)
ALL URLs where this Site Network is mentioned or documented.
Semicolon-delimited. Includes:
- Primary organization or network website
- About/history pages
- Parks/preserves listing pages
- System overview map URLs
- PDF system maps
- GIS viewers showing member sites

Do not deduplicate. Resolution handles deduplication.

**Note:** The Site Network record is the canonical anchor for the managing
organization's primary website URL. This URL is captured once here and is
not duplicated across individual Site records. Member Sites reference the
organization by name in their `governance` field; the URL is retrieved by
joining to the Site Network record.

------------------------------------------------------------
# 9. MEMBER SITE TRACKING

## 9.1 During Discovery

Record member site names in `member_site_names_raw` — exactly as listed in
source, semicolon-delimited. Do not attempt to match to Site entity IDs.

When source references a count but does not list all members, record what you
find and note incompleteness in `identity_notes_raw`.

## 9.2 Provisional Records and Incremental Membership

For provisional records, `member_site_names_raw` initially reflects only the
member sites documented at time of record creation. As additional member sites
are discovered within the same tier or across tiers, the Site Network record
is updated and the SITE_NETWORK_PROVISIONAL flag is removed when threshold
is reached.

## 9.3 During Normalization

Normalization Engine:
- Resolves member site names to site_ids
- Populates `member_site_ids`
- Creates entries in `site_network_members` relationship table
- Handles name variants and spelling differences

------------------------------------------------------------
# 10. WHAT NOT TO DO (CRITICAL)

- ❌ Do not create Site Network records for parent Sites with internal child
  Sites — use `parent_site_id` on the child Sites
- ❌ Do not create Site Network records for governance bodies below the
  applicable threshold with no expectation of meeting it
- ❌ Do not create Site Network records for informal groupings or marketing
  labels with no managing organization
- ❌ Do not conflate Site Networks with Trailthings — trail-system collections
  belong in Trailthing discovery
- ❌ Do not use SITE_NETWORK_UNCERTAIN as a substitute for the PROVISIONAL
  pattern — create provisional records early; reserve UNCERTAIN for genuine
  ambiguity about org_type or network_type
- ❌ Do not count member sites yourself from a list — only record published
  counts in `member_count_raw`
- ❌ Do not infer member site relationships from proximity or shared governance
- ❌ Do not merge records from multiple sources
- ❌ Do not normalize or standardize field values
- ❌ Do not put pipeline source references, IMP numbers, or process notes
  in `notes_raw` — it is a customer-facing field

------------------------------------------------------------
# 11. TIER-SPECIFIC EXPECTATIONS

## Federal Tier (Tier 1)
Must surface:
- National Heritage Areas
- National Scenic River designations
- Multi-state heritage or conservation designations

## State Tier (Tier 2)
Must surface:
- Ohio State Scenic River Corridors
- Statewide heritage or conservation designations
- MWCD and other multi-county conservation authority systems
- Multi-county ecological corridors with formal designations

## District Tier (Tier 3)
Must surface:
- Park district systems (Rule 2 — County Authority; create provisionally at
  first member site)
- Regional conservation authority portfolios

## County Tier (Tier 4)
Must surface:
- County park authority systems (Rule 2)
- County historic districts (Rule 1 if formally designated)
- County conservation programs managing 2+ Sites
- Countywide watershed networks with formal designation

## Township & Municipal Tiers (Tiers 5–6)
Must surface:
- Municipal parks departments managing 3+ in-scope Sites (Rule 3)
- Local historic districts (Rule 1 if formally designated)
- Township-level conservation or nature programs managing 2+ Sites
  under Land Trust or Authority org_type

## Conservancy Tier (Tier 7)
Must surface:
- Land trust preserve portfolios (Rule 2 — Land Trust; create provisionally
  at first member preserve)
- Nonprofit conservancy portfolios (Rule 2)
- Multi-site conservation networks and ecological corridors

## Private Tier (Tier 8)
May surface:
- Privately managed heritage or conservation networks (Rule 4 if 3+ Sites)
- Campus-scale multi-site systems (Rule 4 if 3+ Sites)

------------------------------------------------------------
# 12. COMMON CASES AND EXAMPLES

## 12.1 County Park District

Rule 2 applies (County Authority). Create provisional record at first member
park; remove PROVISIONAL when second member park is cataloged.

```yaml
network_name_raw: "Wood County Park District"
network_type_raw: "county park district system"
org_type_raw: "county park district"
governance_raw: "Wood County Park District"
counties_raw: "Wood"
member_count_raw: "21"
member_site_names_raw: "Carter Historic Farm;Oak Openings Preserve Metropark;..."
identity_notes_raw: "SITE_NETWORK_PROVISIONAL — Wood County Park District first
  member site cataloged [date]; 20 additional member sites expected.
  Threshold: Rule 2 — County Authority, 2+ member sites."
```
*(Remove PROVISIONAL when second member site is cataloged.)*

## 12.2 National Heritage Area

Rule 1 applies (formal designation). Create immediately regardless of member
site count.

```yaml
network_name_raw: "Ohio & Erie Canalway National Heritage Area"
network_type_raw: "national heritage area"
org_type_raw: "federal program"
governance_raw: "National Park Service"
partner_agencies_raw: "Ohio & Erie Canalway Coalition;Ohio History Connection"
counties_raw: "Cuyahoga;Mahoning;Stark;Summit;Tuscarawas"
member_site_names_raw: "Cuyahoga Valley National Park;Canal Visitor Center;..."
```

## 12.3 Scenic River Corridor

Rule 1 applies (formal designation).

```yaml
network_name_raw: "Little Miami Scenic River Corridor"
network_type_raw: "scenic river corridor"
org_type_raw: "state agency"
governance_raw: "Ohio Department of Natural Resources"
counties_raw: "Clermont;Greene;Hamilton;Warren"
description_raw: "State-designated scenic river corridor encompassing the
  Little Miami River and its watershed; one of Ohio's first designated scenic
  rivers under the Ohio Scenic Rivers Program."
```

## 12.4 Land Trust Portfolio

Rule 2 applies (Land Trust). Create provisional at first preserve.

```yaml
network_name_raw: "Black Swamp Conservancy"
network_type_raw: "land trust portfolio"
org_type_raw: "land trust"
governance_raw: "Black Swamp Conservancy"
counties_raw: "Henry;Lucas;Wood"
identity_notes_raw: "SITE_NETWORK_PROVISIONAL — Black Swamp Conservancy first
  member preserve cataloged [date]; additional preserves expected.
  Threshold: Rule 2 — Land Trust, 2+ member sites."
```

## 12.5 Municipal Department — Below Threshold

A village with 2 in-scope parks does not meet Rule 3 (3+ sites for Municipal
Department). Do not create a Site Network record.

Record the village parks department as `governance_raw` on each Site. Note
in `identity_notes_raw` on the Site records that no Site Network was created
and the reason.

## 12.6 Greenway with Dual Identity

A greenway documented both as a collection of sites (park hubs along the
corridor) and as a trail system (the trail itself) produces both entities.

```
Site Network: "[Greenway Name]" — for the collection of park sites along
  the corridor. identity_notes_raw: "Greenway has dual identity — also
  discovered as Trailthing; see [Trailthing name]."

Trailthing: "[Greenway Trail Name]" — for the trail system.
  identity_notes_raw: "Trail system has dual identity — Site Network
  also created; see [Site Network name]."
```

------------------------------------------------------------
# 13. RAW DISCOVERY RECORD TEMPLATE

```yaml
entity_type: Site Network
network_name_raw:               # Required; official name verbatim
network_type_raw:               # Optional; verbatim from source; used in threshold evaluation
org_type_raw:                   # Optional; organization category; essential for Rules 2-4
status_raw:                     # Optional; verbatim; only if explicitly stated
ownership_raw:                  # Optional; often blank for designating bodies
governance_raw:                 # Optional; primary managing organization
partner_agencies_raw:           # Optional; semicolon-delimited; only if explicitly documented
coordination_raw:               # Optional; friends groups, volunteers, advisory boards
counties_raw:                   # Optional; semicolon-delimited; all counties encompassed
states_raw:                     # Optional; multi-state networks only; blank for Ohio-only
member_count_raw:               # Optional; published count only; do not self-count
member_site_names_raw:          # Optional; semicolon-delimited; exactly as listed in source
description_raw:                # Optional; character and mission priority; 1-3 sentences
identity_notes_raw:             # Optional; SITE_NETWORK_PROVISIONAL or SITE_NETWORK_UNCERTAIN
notes_raw:                      # Optional; operational context; no provenance artifacts
urls_raw: []                    # All URLs; semicolon-delimited; includes primary org website
discovery_tier:                 # 1–8
seeded_from_baseline:           # true | false
baseline_id:
```

------------------------------------------------------------
# 14. ENTITY TYPE SEQUENCE WITHIN TIERS

Within each discovery tier, process entity types in this order:

**Sites → Trailthings → Site Networks → Access Points**

------------------------------------------------------------
# 15. QUALITY CHECKLIST

Before emitting a discovery record, verify:

- ✅ `network_name_raw` recorded exactly as found
- ✅ `network_type_raw` captured — essential for threshold evaluation
- ✅ `org_type_raw` captured — essential for Rules 2–4
- ✅ Threshold rule evaluated and documented:
  - Rule 1: formal designation → create immediately
  - Rule 2: Conservation/Land org → 2+ member sites or provisional
  - Rule 3: Municipal Department → 3+ in-scope sites or provisional
  - Rule 4: Other → 3+ sites with documented rationale
- ✅ If below threshold but first member site cataloged → SITE_NETWORK_PROVISIONAL
  flag set in `identity_notes_raw` with rule reference and expected member count
- ✅ SITE_NETWORK_UNCERTAIN used only for genuine ambiguity about org_type or
  network_type — not as a substitute for PROVISIONAL
- ✅ `member_site_names_raw` recorded if member sites are listed
- ✅ `member_count_raw` recorded if published (never self-counted)
- ✅ `description_raw` prioritizes character and mission when populated (IMP-015)
- ✅ `notes_raw` contains no pipeline source references, IMP numbers, or
  provenance content (IMP-014)
- ✅ `urls_raw` includes primary organization website and all other relevant URLs
- ✅ Record is not for a parent Site with child Sites (use parent_site_id)
- ✅ Record is not for a Trailthing collection (use Trailthing discovery)
- ✅ No normalization or standardization applied
- ✅ No inferred member sites

------------------------------------------------------------
# 16. MODULE DEPENDENCIES

This module depends on:

- Site Network Schema Module v6.0
- Site Network Vocabulary Module v6.0 *(for network_type and org_type
  controlled values and threshold evaluation)*
- Site Discovery Sub-Procedure v6.0 *(for entity type boundary)*
- Trailthing Discovery Sub-Procedure v6.0 *(for Trailthing/Site Network
  dual-identity cases)*
- Access Point Discovery Sub-Procedure v6.x *(pending)*
- Discovery Orchestration Module v6.x *(or v5.x)*
- Resolution Engine v6.x *(or v5.x)*

------------------------------------------------------------
# END OF SITE NETWORK DISCOVERY SUB-PROCEDURE v6.0
