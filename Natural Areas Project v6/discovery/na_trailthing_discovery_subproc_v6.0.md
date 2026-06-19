# NATURAL AREAS PROJECT
# TRAILTHING DISCOVERY SUB-PROCEDURE v6.0
(Authoritative Sub-Procedure for Discovering Trailthing Entities)

This module defines the authoritative, deterministic workflow for discovering
**Trailthing** entities across all discovery tiers within the v6.x pipeline.

A Trailthing is the unified entity type that replaces Trail, Trail Segment,
and Trail Network in the v6.x architecture. This sub-procedure supersedes:

- Trail Discovery Sub-Procedure v5.x
- Trail Segment Discovery Sub-Procedure v5.x
- Trail Network Discovery Sub-Procedure v5.x

Those sub-procedures remain in the v5 repository as reference material.
For active discovery under v6.x, this sub-procedure is authoritative.

------------------------------------------------------------
# CHANGES FROM v5.x → v6.0

- **Trail, Trail Segment, and Trail Network consolidated into Trailthing**:
  All three entity types are now discovered as a single entity type. The
  discoverer does not classify which kind of Trailthing an entity is.

- **`source_term` and `source_hierarchy_context` added**: These two fields
  capture how the authoritative source describes the entity. They are the
  primary input for future Trailthing hierarchy classification analysis
  (IMP-007). Consistent, verbatim capture is essential.

- **`parent_id`, `site_parent_id`, `parent_site_network_id` added**: Hierarchy
  and cross-entity parent fields capture documented relationships without
  requiring the discoverer to classify them.

- **No-classification mandate**: During discovery, the discoverer must not
  decide whether a Trailthing is a trail, trail network, trail segment, or
  any other sub-type. That determination is deferred to post-county analysis.

- **Surface, status, and governance variation rules**: Unnamed variation along
  a Trailthing's corridor (surface changes, governance handoffs, partial
  closures) is documented in Notes — not by creating additional Trailthing
  records. Only named, source-documented sections rise to entity-level.

- **Description mandate updated** (IMP-015): Ecological/physical character
  is the priority for descriptions. Amenity inventory belongs in Notes.

- **Notes provenance prohibition** (IMP-014): Notes is a customer-facing field.
  Pipeline source references, IMP numbers, and process content must not appear
  here.

- **Generic name qualification carried forward** (IMP-010): The qualification
  rule for generic trail names in multi-park systems applies to Trailthings.

- **Explicit use/surface field guidance carried forward** (IMP-021): Separate
  fields for use type and surface type; do not embed in accessibility_raw.

- **Multi-county protocol carried forward** (IMP-046): Create the Trailthing
  record during the first county session that encounters it; document partial
  membership; update when subsequent counties are processed.

------------------------------------------------------------
# 1. PURPOSE

This sub-procedure provides the authoritative workflow for:

- Identifying Trailthing candidates
- Extracting raw, unnormalized metadata
- Capturing source-native terminology and hierarchy framing
- Supporting enumerative and recursive discovery
- Preventing misclassification across the four v6.x entity types
- Recording tier and URL provenance
- Emitting Raw Discovery Records conforming to the Trailthing Schema Module v6.0
- Integrating with Site, Site Network, and Access Point discovery
- Feeding the Resolution Engine v6.x

A **Trailthing** is any named, identity-bearing trail-related entity documented
in authoritative sources — including what would previously have been classified
as a Trail, Trail Segment, or Trail Network.

Examples:
- A named regional trail system or greenway network
- A named water trail, blueway, or paddling route
- A named hiking, biking, equestrian, or multi-use trail
- A named section, reach, or segment of a larger trail
- A named connector, spur, or loop trail
- A named trail corridor, route, or hub
- A statewide or national trail system with documented identity
- A heritage trail within a National Heritage Area or scenic corridor

A Trailthing is **not**:
- A Site or Site Network (place-based entities)
- An Access Point (entry point entities)
- A synthetic or inferred entity
- An unnamed path with no documented identity

This sub-procedure is authoritative for **Trailthing discovery**.

------------------------------------------------------------
# 2. DISCOVERY PHILOSOPHY

## 2.1 Core Principle: Discovery = Collection, Normalization = Decisions

**Discovery Phase (YOU ARE HERE):**
- Collect everything you find
- Record exactly as found
- Do not normalize, standardize, or choose between values
- Do not deduplicate URLs or map links
- Do not make vocabulary decisions
- Do not classify the Trailthing as trail, trail network, or trail segment
- Fast, mechanical extraction

**Normalization Phase (LATER):**
- Standardize vocabulary terms
- Deduplicate URLs and maps
- Validate parent relationships
- Classify Trailthing hierarchy position (deferred to post-30-county analysis)

## 2.2 The No-Classification Mandate

**Do not decide during discovery:**
- Whether this Trailthing is a "trail network" vs. a "trail" vs. a "trail segment"
- Whether a child Trailthing "should" be a trail or a segment
- Whether a parent Trailthing "should" be a trail network or a trail
- What level in a hierarchy this Trailthing occupies

Record `source_term` verbatim (what the source calls it) and
`source_hierarchy_context` verbatim (how the source frames it in relation
to other entities). These fields are the empirical foundation for future
classification decisions.

If you find yourself wanting to write "this is probably a trail network" —
instead record what the source says in `source_term_raw` and
`source_hierarchy_context_raw` and move on.

## 2.3 When in Doubt: Collect It

If uncertain whether to include a Trailthing candidate:
- Include it
- Record uncertainty in `identity_notes_raw`
- Let Resolution and Normalization decide

## 2.4 Multiple Sources = Multiple Records

If you find the same Trailthing at multiple URLs:
- Emit SEPARATE discovery records
- Do NOT attempt to merge
- Resolution Engine handles merging

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
9. Tier-0 Baseline (non-authoritative; runs last)

Each tier must surface Trailthing candidates when applicable.

------------------------------------------------------------
# 4. REQUIRED SOURCES

Each tier must check the following for Trailthing references:

- Official agency websites and trail pages
- Authoritative listing/index pages (e.g., /trails/, /bikeways/, /greenways/)
- GIS systems and interactive trail maps
- Trail brochures and downloadable maps
- Park district trail pages with trail and segment detail
- Statewide trail inventories
- Federal trail inventories and national trail system documentation
- Regional greenway, bikeway, and water trail plans
- Trail signage programs
- Digitally documented trailhead kiosks
- Planning documents (master plans, corridor plans)
- Multi-trail system documents (for individual trail extraction)
- GPX/KML download pages
- Network-level system overview maps
- PDF strip maps by county

All sources must be logged in source_map.

------------------------------------------------------------
# 5. IDENTITY RULES FOR TRAILTHING CANDIDATES

A Trailthing candidate is valid only if:

1. An authoritative source documents a named entity that is a trail, trail
   system, trail network, greenway, water trail, trail section, connector,
   spur, loop, or similar linear recreational corridor or system.
2. The entity has a **stable, documented name** — not a temporary project
   label, informal description, or marketing slogan.
3. The entity is not a Site, Site Network, or Access Point.
4. The entity is not a synthetic or inferred entity assembled from geographic
   proximity rather than documented source identity.

If any condition fails, the candidate must not be created.

------------------------------------------------------------
# 5a. WATER TRAIL QUALIFICATION RULES (IMP-103)

Water trails (blueways, paddling routes, canoe/kayak trails) follow the general
Trailthing identity rules in §5, with the following additional guidance.

## 5a.1 Qualification Threshold

A paddling route earns a Trailthing record when **both** of the following are true:

1. A managing entity (ODNR, NPS, a paddle trail organization, a county park
   district, etc.) has published a **formal name** for the route in an
   authoritative source — not a generic geographic description.
2. At least **two Access Points are documented** in authoritative sources.

When condition 1 is met but condition 2 is not, flag with `WATER_TRAIL_REVIEW`
(§5a.2) and stage a null-evidence block. Return to evaluate when additional
Access Points are documented in the same or a later tier.

When neither condition is met, do not create a Trailthing record.

## 5a.2 WATER_TRAIL_REVIEW Flag

Use this flag in `identity_notes_raw` when a formal published name exists but
fewer than 2 documented Access Points were found, or when qualification is
uncertain pending additional source research:

```
identity_notes_raw: "WATER_TRAIL_REVIEW — Formal name documented by [source]
but only 1 AP confirmed. Defer Trailthing record pending second AP documentation."
```

Also use for paddling routes documented only in planning documents (proposed,
not yet formally designated by a managing entity).

## 5a.3 Water Trail Child Trailthing Triggers

Create a **separate named child Trailthing** — not notes-only variation — when
an authoritative source explicitly names and documents a distinct section for
any of the following reasons:

- **Management boundary**: a named reach managed by a different agency than
  the adjoining section
- **Hazard Portage interruption**: a formally named section separated by a
  documented required portage at a dam, waterfall, or rapid
- **Difficulty change**: a named section explicitly rated at a materially
  different difficulty level in authoritative sources (e.g., Class I vs. Class III)
- **Seasonal navigability change**: a named section documented as navigable
  in different seasons than the adjoining section

Unnamed variation along any of these dimensions belongs in `notes_raw`, not a
new entity. Only create child Trailthings when the source itself names and
documents the distinct sections as separate entities.

------------------------------------------------------------
# 6. DISCOVERY WORKFLOW

## 6.1 Step 1 — Identify Named Trail-Related Entities

Search all required sources for:

- Named trails (any use type)
- Named loops, connectors, spurs
- Named bikeways or greenways
- Named water trails, blueways, paddling routes
- Named equestrian trails
- Named multi-use trails and rail trails
- Named trail sections, segments, or reaches
- Named trail systems, networks, or hubs
- Named corridor plans with documented identity
- Named heritage trails
- Named statewide or national trail systems

Record each appearance as a Trailthing candidate.

## 6.2 Step 2 — Verify Identity-Bearing Name

A Trailthing must have:
- A documented, stable name
- Not a temporary project name
- Not a marketing slogan
- Not a generic label unless officially used

If ambiguous, flag in `identity_notes_raw`.

**Generic name check (§7.1a):** If the entity's name is a generic term
(Overlook Trail, Lake Trail, Nature Trail, Loop Trail, etc.) and you are
discovering within a multi-park system, apply the generic name qualification
rule in §7.1a before recording `name_raw`.

## 6.3 Step 3 — Capture Source Framing

For every Trailthing candidate, capture:

- `source_term_raw`: the exact word or phrase the source uses for this entity
  ("trail," "trail network," "greenway," "section," "route," "corridor," etc.)
- `source_hierarchy_context_raw`: how the source frames this entity in relation
  to other entities ("part of the X System," "one of five member trails,"
  "a section of the Y Trail," "connecting A Park and B Park")

Do not skip these fields. They are essential for future classification analysis.

## 6.4 Step 4 — Document Parent Relationships

Record parent relationships only when explicitly stated by the authoritative source:

- `parent_id_raw`: the name of the parent Trailthing when the source explicitly
  frames this entity as a component, member, section, or part of it
- `site_parent_raw`: the name of the containing site when the source explicitly
  frames this Trailthing as contained within and access-dependent on a site
- `parent_site_network_raw`: when the source explicitly frames this entity as a
  member of a Site Network (e.g., a heritage trail within a National Heritage Area)

Do not infer parent relationships from geography, governance, or name similarity.

------------------------------------------------------------
# 7. FIELD-BY-FIELD EXTRACTION GUIDE

## 7.1 Identity Fields

### `name_raw` (REQUIRED)
Record the official published name exactly as written. Do not normalize
capitalization. Do not add or remove words.

**Examples:**
- "Slippery Elm Trail" ✅
- "Ohio to Erie Trail" ✅
- "Buckeye Trail — Wood County Section" ✅
- "slippery elm trail" ✅ (record as found)

---

### §7.1a Generic Trail Name Qualification (IMP-010)

Many parks use generic names — Overlook Trail, Lake Trail, Nature Trail,
Loop Trail, River Trail, Meadow Trail, and similar. When the same generic
name appears at multiple parks in a multi-park system, each Trailthing is
a distinct entity but Resolution's identity matching would risk false merges.

**Qualification is required when ALL of the following are true:**

1. The name is a generic term that commonly appears at multiple parks.
2. You are discovering within a **multi-park system** — a park district,
   county park system, conservancy network, or any agency managing more
   than one distinct park property.
3. The Trailthing is explicitly associated with a specific named park or
   preserve in the source material.

**Qualification format:**
```
name_raw: "[Park Name] — [Trail Name as published]"
alternate_names_raw: "[Trail Name as published]"
identity_notes_raw: "Name qualified per §7.1a — generic name in multi-park
  system; original: [Trail Name as published]"
```

**Examples of generic names requiring qualification:**
- Overlook Trail → "Glacier Hills Metropark — Overlook Trail"
- Lake Trail → "Chestnut Ridge Metro Park — Lake Trail"
- Nature Trail → "Prairie Oaks Metro Park — Nature Trail"
- Loop Trail → "Battelle Darby Creek Metro Park — Loop Trail"

**Names that are NOT generic and do NOT require qualification** — names
containing distinctive proper nouns, geographic references, or unique
identifiers that would not commonly repeat across parks:
- "Slippery Elm Trail" ✅
- "Buckeye Trail" ✅
- "Blacklick Valley Greenway" ✅
- "Overlook Trail" ❌ (generic — qualify if in multi-park system)

**When NOT to qualify:**
- Single-park agencies (a trail at the only park managed by an entity)
- Cross-tier greenway trails with established regional identities spanning
  multiple parks as a single named corridor

---

### `alternate_names_raw` (OPTIONAL)
Documented historical or variant names, abbreviations, or formally used
alternate designations. Semicolon-delimited.

When §7.1a qualification is applied, the original published name must be
recorded here.

Do not invent abbreviations. Do not include nicknames unless officially used.

---

### `source_term_raw` (REQUIRED)
The exact word or phrase the authoritative source uses to describe what kind
of entity this is.

**Examples of source terms to capture verbatim:**
- "trail system"
- "greenway"
- "water trail network"
- "connector trail"
- "spur"
- "loop trail"
- "blueway"
- "trail hub"
- "route"
- "corridor"
- "rail-trail"
- "heritage trail"
- "section"
- "reach"
- "segment"
- "pathway"

Do not normalize to a controlled vocabulary. Do not synthesize — use
the source's own words. This field is the primary input for future hierarchy
pattern analysis. Leave blank only if the source provides no descriptive term.

---

### `source_hierarchy_context_raw` (OPTIONAL)
How the authoritative source frames this entity in relation to other entities.

**Examples:**
- "part of the Ohio to Erie Trail system"
- "one of seven member trails in the [network name]"
- "the Wood County section of the Buckeye Trail"
- "connecting Slippery Elm Trail and the Towpath Trail"
- "the northern reach of the Great Miami River Recreational Trail"
- "a branch trail within [park name]"

Free text. Verbatim or close paraphrase from source. Do not interpret or
classify — record what the source says. Leave blank if no hierarchical
context is provided.

## 7.2 Hierarchy and Parent Fields

### `parent_id_raw` (OPTIONAL)
The name of the parent Trailthing entity as documented in the source.
Populate only when the source **explicitly** frames this entity as a
component, member, section, or part of another Trailthing-type entity.

**Examples:**
- Source says "the Wood County Section of the Buckeye Trail" →
  `parent_id_raw: "Buckeye Trail"`
- Source says "one of seven member trails of the Ohio to Erie Trail system" →
  `parent_id_raw: "Ohio to Erie Trail"`
- Source describes a loop within a larger named trail →
  `parent_id_raw: "[parent trail name]"`

Must not be inferred from geography, governance, or name similarity alone.
A Trailthing may have at most one parent Trailthing.

---

### `site_parent_raw` (OPTIONAL)
The name of the containing site, populated only when the source explicitly
frames this Trailthing as contained within and access-dependent on a specific
named site.

**Correct use:**
- A trail that exists entirely within one park and the source treats it as
  a component of that park's trail system → record the park name here.

**Do not populate if:**
- The Trailthing crosses or spans multiple sites
- The Trailthing merely passes near or adjacent to a site
- Containment is inferred from proximity or governance alone

---

### `parent_site_network_raw` (OPTIONAL)
Populate when the source explicitly frames this Trailthing as a member
of a Site Network.

**Example:**
- A heritage trail documented as a component of a National Heritage Area
  (which is a Site Network) → record the heritage area name in
  `parent_site_network_raw`.

## 7.3 Character Fields

### `trail_use_type_raw` (PREFERRED — IMP-021)
Record the use type exactly as the source describes it. Do not normalize
to vocabulary terms during discovery.

Capture this field explicitly whenever the source states or implies a use
type. Do not embed use type information inside `accessibility_raw`.
`accessibility_raw` is for ADA/accessibility statements only; use type
belongs here.

**Examples of source terms to capture:**
- "multi-use", "bike trail", "hiking trail", "equestrian trail",
  "water trail", "mountain bike trail", "nature trail", "paved multi-use
  path", "rail-trail"

**Anti-pattern (IMP-021):**
- ❌ `accessibility_raw: "Paved multi-use (hiking, biking)"` — extract instead:
  - `trail_use_type_raw: "hiking, biking"`
  - `trail_surface_type_raw: "paved"`
  - `accessibility_raw: [leave blank unless source states ADA compliance]`

Leave blank if no use type information is provided. Never infer.

---

### `trail_surface_type_raw` (PREFERRED — IMP-021)
Record exactly as found. Capture explicitly whenever the source states a
surface type. Do not embed in `accessibility_raw`.

**Examples:**
- "asphalt", "gravel and dirt", "crushed limestone", "natural surface",
  "compacted gravel", "boardwalk sections"

**Surface variation rule:** Unnamed surface variation along a Trailthing's
corridor does not require multiple Trailthing records. Document the variation
in `notes_raw` instead. Only create separate child Trailthing records for
surface variation when the source itself names and documents those sections
as distinct identity-bearing entities.

Leave blank if not documented. Never infer from trail photos or category.

---

### `trail_origin_type_raw` (OPTIONAL)
Only if explicitly stated. Do not guess from context.

**Examples:**
- "former railroad corridor" → record "former railroad corridor"
- "canal towpath" → record "canal towpath"
- "purpose-built" → record "purpose-built"

---

### `org_type_raw` (OPTIONAL)
The organizational category of the primary governance entity, as described
by an authoritative source. Only if explicitly documented.

**Examples:**
- "state agency", "park district", "conservancy", "trail association",
  "federal agency"

Leave blank if not stated. Never infer from governance name alone.

## 7.4 Status Fields

### `status_raw` (OPTIONAL)
Only if explicitly stated. Do not infer from maps or imagery.

**Status variation rule:** A trail that is open along most of its length
but has a closed section or gap does not require multiple Trailthing records.
Document the variation in `notes_raw`. Only create separate child Trailthing
records for status variation when the source itself names and documents those
sections as distinct identity-bearing entities.

**"Gap" and "Planned" are especially important** for long-distance trail
documentation:
- "Gap" = missing or incomplete trail portion requiring road walk
- "Planned" = not yet built

---

### `difficulty_raw` (OPTIONAL)
**Only record if explicitly stated by an authoritative source.**
Never assess difficulty yourself.

- ✅ Source says "Easy" → record "Easy"
- ✅ Source says "Moderate to Difficult" → record "Moderate to Difficult"
- ❌ Trail looks easy based on topography → leave blank
- ❌ Surface is paved → leave blank (never infer difficulty from surface)

---

### `accessibility_raw` (OPTIONAL)
Only if explicitly stated. Record exactly as found.

**Examples:**
- "ADA compliant" → record "ADA compliant"
- "Wheelchair accessible for first mile" → record as found

Do not infer from surface type or trail width.

## 7.5 Governance Fields

### `governance_raw` (OPTIONAL)
Primary managing agency or organization, exactly as stated.

**Examples:**
- "Wood County Park District"
- "Ohio Department of Natural Resources"
- "Buckeye Trail Association"

**Governance variation rule:** A trail that passes through sections managed
by different agencies does not require multiple Trailthing records. Document
the variation in `notes_raw`. Only create separate child Trailthing records
for governance variation when the source itself names and documents those
sections as distinct identity-bearing entities.

---

### `partner_agencies_raw` (OPTIONAL)
Secondary managing agencies or land managers. Semicolon-delimited. Only if
explicitly documented ("in partnership with...", "co-managed by...").

---

### `coordination_raw` (OPTIONAL)
Community-based, volunteer, advisory, or informal partners — trail stewardship
volunteers, friends groups, trail associations, advisory boards. Only if
documented. Must not duplicate governance_raw or partner_agencies_raw.

---

### `ownership_raw` (OPTIONAL)
Legal owner of the corridor or right-of-way. Often blank for coordinating
bodies and trail systems where ownership is distributed.

## 7.6 Geography and Physical Fields

### `counties_raw` (REQUIRED)
All counties the Trailthing traverses. Semicolon-delimited if multiple.

**Examples:**
- "Wood" ✅
- "Wood;Lucas;Ottawa" ✅

Do not include the word "County." Do not infer counties from maps.

---

### `states_raw` (OPTIONAL)
Only for multi-state Trailthings. Leave blank for Ohio-only entities.

---

### `total_length_miles_raw` (OPTIONAL)
Record the number only from what the source publishes.
- "12.5 miles" → record "12.5"

Never estimate from maps. Never sum child Trailthing lengths. Leave blank
if unknown or undocumented.

---

### `member_trailthing_names_raw` (OPTIONAL)
For system-level Trailthings where the source lists member entities:
record member names exactly as listed, semicolon-delimited.

This field replaces `member_trail_names_raw` from v5. Normalization resolves
names to trailthing_ids and populates the trailthing_hierarchy relationship
table.

**Example:**
- "Towpath Trail;Slippery Elm Trail;University Parks Trail"

When source mentions some members but not all, record what you find and note
incompleteness in `identity_notes_raw`:
```
PARTIAL MEMBERSHIP: Source lists 4 member trails; system documented as
having "over 15 trails" — partial member list only.
```

## 7.7 Descriptive Fields

### `description_raw` (OPTIONAL)
1-3 sentences describing the Trailthing's identity, scope, and character.

**Priority: physical and ecological character.** Describe what the corridor
or system is like — its terrain, setting, natural context, and defining
character. A description that says only "a multi-use trail" tells a reader
nothing about the experience or environment.

**What belongs here:**
- Physical and ecological setting (river valley, upland forest, wetland edge,
  prairie corridor)
- Terrain and character (flat, rolling, steep sections, open exposure)
- Geographic scope and routing
- Origin context (former railroad corridor, canal towpath, purpose-built)
- Brief establishment history if documented

**What does NOT belong here:**
- Amenity inventory ("features a pavilion, restrooms, and parking") → Notes
- Temporary conditions → Notes

May include brief establishment history or origin context when documented.

---

### `trail_history_raw` (OPTIONAL)
Historical context — railroad history, canal conversion, federal designation
history, established date, former names, or major route changes.

Only if explicitly documented. Do not research yourself.

**Examples:**
- "Former Penn Central Railroad corridor, converted to trail in 1985"
- "Follows historic Miami & Erie Canal towpath from 1845"

## 7.8 Identity Notes Field

### `identity_notes_raw` (OPTIONAL)
Free-text field for identity clarifications, uncertainty flags, and
disambiguation notes.

**Use for:**
- Hierarchy uncertainty:
  ```
  TRAIL_HIERARCHY_UNCERTAIN — source alternately calls this a "trail" and
  a "trail system"; unclear whether this is a system-level or navigable
  entity. source_term_raw captures both usages.
  ```
- Generic name qualification notices (§7.1a):
  ```
  Name qualified per §7.1a — generic name in multi-park system;
  original: Overlook Trail
  ```
- Multi-county partial membership (IMP-046):
  ```
  PARTIAL MEMBERSHIP: Only [County] County child Trailthings documented
  as of [date]. Additional members expected from [County2] session.
  ```
- Cross-tier Trailthing flags
- Parent entity assignment uncertainty
- Co-location notes with Access Points

**What NOT to put here:**
- ❌ Operational details → `notes_raw`
- ❌ Map URLs → `maps_raw`
- ❌ Historical context → `trail_history_raw`

## 7.9 Notes Field

### `notes_raw` (OPTIONAL)
Short, factual, operational details: gap documentation, partial completion
notes, access restrictions, seasonal conditions, surface variation along
corridor, governance handoffs, planning status.

**Correct use for unnamed variation:**
- "Paved from trailhead to mile 4; crushed limestone mile 4 to terminus"
- "Section between State Route 12 and Cedar Road currently a gap —
  road walk required"
- "Mile 8 to mile 11 managed by Lucas County Metroparks; remainder
  by Wood County Park District"

**Customer-facing field — no provenance artifacts.** Pipeline source
references, IMP numbers, batch load notes, GPS source citations, and
similar process or provenance content must not appear here. Notes must
be readable by someone who knows nothing about the pipeline.

Must not include identity-defining characteristics (those belong in
`description_raw` or `identity_notes_raw`).

## 7.10 URL and Map Fields

### `urls_raw` (OPTIONAL)
ALL URLs where this Trailthing is mentioned. Semicolon-delimited. Do not
deduplicate. Do not choose — collect everything.

Include the primary/most authoritative URL within this list. No separate
`url_primary_raw` field is needed — the full list goes here.

---

### `maps_raw` (OPTIONAL)
ALL map URLs you find — PDF maps, interactive maps, GIS viewers, GPX
downloads, KML files, elevation profiles, route guides, strip maps.
Semicolon-delimited plain URL list. No type labels or descriptions.

Do not deduplicate. Resolution handles deduplication.

## 7.11 GPS Capture Opportunity — All Trailthings

When you are on an authoritative source page for a Trailthing, **capture GPS and
address information for all documented Access Points visible on that same page in
the same session.** Do not defer AP GPS to Stage 4b GPS Acquisition if it is
available now.

This applies to every Trailthing type — rail trails, greenways, water trails,
metro park trails, national scenic trails. Any source page that names and locates
trailheads, parking areas, or boat launches for a Trailthing is an opportunity
to collect AP GPS before the session moves on.

**What to capture during Trailthing discovery:**
- Trailhead, parking area, and boat launch names as listed in the source
- Street addresses when provided — note in `identity_notes_raw` on the
  Trailthing record so the AP Discovery stage can pick them up:
  ```
  AP GPS captured during T[N] discovery: [AP Name] — [lat, lon or address]
  ```
- GPS coordinates when explicitly stated by the source or visible in a map URL

**Why this matters:** The Access Point Discovery stage follows Trailthing
discovery within a tier. Noting what is visible now while already on the
source page eliminates returning to that same page during Stage 4b GPS
Acquisition. Discovery and GPS acquisition are separate pipeline stages, but
nothing prevents recording what is visible during discovery.

**This is an efficiency rule, not a discovery obligation.** Do not delay
Trailthing record staging to research AP GPS you cannot see on the current
page. If it requires additional lookups, leave it for Stage 4b.

------------------------------------------------------------
# 8. THE NO-ENTITY-CREATION RULE

During Trailthing discovery, you are capturing Trailthings only. Do not
create or attempt to capture:

- Access Points — note trailhead/access point names in `identity_notes_raw`;
  Access Point Discovery handles these
- Sites — if a trail-adjacent entity looks like it may be a Site, flag in
  `identity_notes_raw`; do not create a Site here
- Site Networks — if a trail system appears to encompass multiple sites,
  note in `identity_notes_raw`; Site Network discovery handles these

Within a Trailthing record, note the existence of related entities but do
not create them. Relationship creation happens during normalization.

------------------------------------------------------------
# 9. WHAT NOT TO DO (CRITICAL)

- ❌ Do not classify Trailthings as "trail," "trail network," or "trail
  segment" in entity type or in fields — that is what source_term_raw captures
- ❌ Do not create separate Trailthing records for unnamed surface variation
  along a corridor — document in notes_raw
- ❌ Do not create separate Trailthing records for unnamed status variation
  (a closed section, a gap) — document in notes_raw
- ❌ Do not create separate Trailthing records for unnamed governance
  variation along a corridor — document in notes_raw
- ❌ Do not infer parent relationships from geography, governance, or name
  similarity
- ❌ Do not normalize or standardize field values
- ❌ Do not deduplicate URLs or map links
- ❌ Do not assess or infer difficulty
- ❌ Do not infer accessibility from surface type
- ❌ Do not infer origin type from name or alignment
- ❌ Do not calculate length from maps or by summing child entities
- ❌ Do not add type/description metadata to maps_raw entries — URLs only
- ❌ Do not leave a generic trail name unqualified when in a multi-park
  system — apply §7.1a
- ❌ Do not put pipeline source references, IMP numbers, or process notes
  in notes_raw — it is a customer-facing field

------------------------------------------------------------
# 10. MULTI-COUNTY TRAILTHING PROTOCOL (IMP-046)

Trailthings whose corridors or member trails span multiple counties require
special handling because membership is discovered county-by-county.

## 10.1 When to Create the Record

Create the Trailthing entity record during the **first county session** that
encounters it. Do not defer creation until all counties have been processed —
the Trailthing entity must exist before child Trailthing records can reference
it via `parent_id`.

## 10.2 Partial Membership Documentation

When creating a multi-county Trailthing during the first county session:

- Populate `member_trailthing_names_raw` with only the child Trailthings
  documented in the current county session.
- Record in `identity_notes_raw`:
  ```
  PARTIAL MEMBERSHIP: Only [County] County child Trailthings documented
  as of [date]. Additional members expected from [County2], [County3]
  county sessions.
  ```
- Set `total_length_miles_raw` to the length documentable from available
  sources, noting in `notes_raw` if this is partial.

## 10.3 Record File Location

The Trailthing record lives in the **first county's** staging YAML.
It is not duplicated in subsequent county staging files.

## 10.4 Subsequent County Sessions

When a subsequent county session discovers additional child Trailthings that
belong to an already-created Trailthing:

- Do NOT create a new Trailthing entity record.
- Locate the existing Trailthing in the Entity Graph by name.
- For each new child Trailthing: populate `parent_id_raw` on the child
  record referencing the parent Trailthing name.
- Update the parent Trailthing record's `member_trailthing_names_raw` if
  accessible; otherwise document the addition in the session log.
- Remove the PARTIAL MEMBERSHIP flag from `identity_notes_raw` when all
  expected county sessions have been processed.

------------------------------------------------------------
# 11. TIER-SPECIFIC EXPECTATIONS

## Federal Tier (Tier 1)
Must surface:
- National Scenic Trails (each is a Trailthing with source_term "National
  Scenic Trail" or as source describes)
- National Historic Trails
- National Recreation Trails
- Federally documented water trails
- Heritage trails within National Heritage Areas

## State Tier (Tier 2)
Must surface:
- State-designated trails and trail systems
- Statewide trail corridors
- State water trails and blueways
- State greenway or bikeway systems and their named member trails

## District Tier (Tier 3)
Must surface:
- All named Trailthings within district boundaries
- All named loops, connectors, and spurs documented by the district
- Named trail systems managed by the district

**Generic name note:** District-managed multi-park systems frequently produce
duplicate generic trail names. Apply §7.1a qualification for all generic names
found within a district's park portfolio.

## County Tier (Tier 4)
May surface:
- Countywide bikeways and greenways
- County-managed trail corridors and trail systems
- Named county trail sections of longer trails

## Township & Municipal Tiers (Tiers 5–6)
May surface:
- Local named Trailthings
- Local greenways and bikeways
- Municipal trail systems and named member trails

**Generic name note:** Municipal park systems with multiple parks are
multi-park systems for purposes of §7.1a. Apply qualification for generic
trail names within any municipal park portfolio of two or more distinct parks.

## Conservancy Tier (Tier 7)
May surface:
- Named trails within preserves
- Named loops, connectors, and access corridors
- Multi-preserve trail corridors

## Private Tier (Tier 8)
May surface:
- Privately managed named trails open to public
- Campus-scale trail systems and named member trails

------------------------------------------------------------
# 12. RAW DISCOVERY RECORD TEMPLATE

```yaml
entity_type: Trailthing
name_raw:                           # Required; verbatim from source; qualify per §7.1a if generic
alternate_names_raw:                # Optional; semicolon-delimited; include original if §7.1a applied
source_term_raw:                    # Required; verbatim source descriptor ("trail system," "greenway," etc.)
source_hierarchy_context_raw:       # Optional; how source frames relationship to other entities
parent_id_raw:                      # Optional; name of parent Trailthing; only if explicitly stated
site_parent_raw:                    # Optional; name of containing site; only if explicitly stated
parent_site_network_raw:            # Optional; name of parent Site Network (e.g., heritage area); only if explicit
trail_use_type_raw:                 # Preferred; verbatim from source; do not embed in accessibility_raw
trail_surface_type_raw:             # Preferred; verbatim from source; do not embed in accessibility_raw
trail_origin_type_raw:              # Optional; verbatim; only if explicitly stated
org_type_raw:                       # Optional; verbatim; only if explicitly stated
status_raw:                         # Optional; verbatim; only if explicitly stated
difficulty_raw:                     # Optional; verbatim; only if explicitly stated by authoritative source
accessibility_raw:                  # Optional; ADA/accessibility statements only; verbatim
ownership_raw:                      # Optional; often blank for coordinating bodies
governance_raw:                     # Optional; primary managing organization
partner_agencies_raw:               # Optional; secondary managers; semicolon-delimited
coordination_raw:                   # Optional; friends groups, trail associations, volunteers
counties_raw:                       # Required; semicolon-delimited; all counties traversed
states_raw:                         # Optional; multi-state only; blank for Ohio-only
total_length_miles_raw:             # Optional; numeric; published length only; never calculated
member_trailthing_names_raw:        # Optional; for system-level Trailthings; semicolon-delimited
description_raw:                    # Optional; physical/ecological character priority; 1-3 sentences
trail_history_raw:                  # Optional; documented historical context
identity_notes_raw:                 # Optional; TRAIL_HIERARCHY_UNCERTAIN, PARTIAL MEMBERSHIP, other flags
notes_raw:                          # Optional; operational details; no provenance artifacts
urls_raw: []                        # All URLs where encountered; semicolon-delimited
maps_raw: []                        # All map URLs; plain URLs only; no metadata
discovery_tier:                     # 1–8
seeded_from_baseline:               # true | false
baseline_id:
```

------------------------------------------------------------
# 13. ENTITY TYPE SEQUENCE WITHIN TIERS

Within each discovery tier, process entity types in this order:

**Sites → Trailthings → Site Networks → Access Points**

Trail Networks, Trails, and Trail Segments are no longer processed as
separate entity types in v6.x. All are discovered as Trailthings.

------------------------------------------------------------
# 14. QUALITY CHECKLIST

Before emitting a discovery record, verify:

- ✅ `name_raw` recorded exactly as found; qualified per §7.1a if generic
  name in multi-park system
- ✅ If §7.1a applied: `alternate_names_raw` contains original published name;
  `identity_notes_raw` contains qualification notice
- ✅ `source_term_raw` populated verbatim from source — this field must not
  be blank unless the source truly provides no descriptive term
- ✅ `source_hierarchy_context_raw` populated when source frames hierarchical
  relationship
- ✅ `parent_id_raw` populated only when source explicitly documents parent
  relationship
- ✅ `trail_use_type_raw` and `trail_surface_type_raw` captured explicitly
  and separately (IMP-021); not embedded in `accessibility_raw`
- ✅ `difficulty_raw` only included if explicitly stated by authoritative source
- ✅ `accessibility_raw` only included if explicitly stated; not inferred from
  surface type
- ✅ Surface, status, or governance variation along corridor documented in
  `notes_raw` — not by creating additional Trailthing records
- ✅ `notes_raw` contains no pipeline source references, IMP numbers, or
  provenance content (IMP-014)
- ✅ `description_raw` prioritizes physical/ecological character when populated
  (IMP-015); amenity inventory not included
- ✅ Multi-county Trailthings: PARTIAL MEMBERSHIP note in `identity_notes_raw`
  if not all county members documented (IMP-046)
- ✅ `total_length_miles_raw` is a published number, not calculated
- ✅ `counties_raw` populated; all counties traversed included
- ✅ All available URLs in `urls_raw`; not deduplicated
- ✅ All map URLs in `maps_raw`; plain URLs only; no metadata
- ✅ No normalization or standardization applied
- ✅ No inferred or guessed values in any field
- ✅ No classification decision made (trail vs. trail network vs. trail segment)

------------------------------------------------------------
# 15. MODULE DEPENDENCIES

This module depends on:

- Trailthing Schema Module v6.0
- Trailthing Vocabulary Module v6.x *(pending — use Trail Vocabulary Module
  v5.x for Use Type, Surface Type, Origin Type, Status, Difficulty; Trail
  Network Vocabulary Module v5.x for Org Type until v6 vocabulary is written)*
- Site Discovery Sub-Procedure v6.0 *(for entity type boundary)*
- Site Network Discovery Sub-Procedure v6.x *(pending)*
- Access Point Discovery Sub-Procedure v6.x *(pending)*
- Discovery Orchestration Module v6.x *(or v5.x)*
- Resolution Engine v6.x *(or v5.x)*
- Normalization Engine v6.x *(or v5.x)*

------------------------------------------------------------
# END OF TRAILTHING DISCOVERY SUB-PROCEDURE v6.0
