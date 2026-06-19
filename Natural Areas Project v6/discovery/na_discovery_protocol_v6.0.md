# NATURAL AREAS PROJECT
# DISCOVERY PROTOCOL MODULE v6.0
(Authoritative Multi-Entity Discovery Framework)

This module defines the authoritative, deterministic protocol for discovering
all four entity types in the statewide Natural Areas system.

This module defines:

- The unified discovery workflow
- The four discovery tracks
- Tier-based source rules
- Entity-specific discovery rules
- Cross-entity relationship rules
- Designation-based entity rules
- Cross-tier Trailthing tier assignment rules
- No-classification mandate for Trailthings
- Document collection requirements
- Metadata requirements
- Raw output requirements
- YAML staging format requirements
- Large municipality batching requirements
- Integration points with Resolution, Normalization, and Entity Upsert
- Provenance and audit requirements

This module supersedes Discovery Protocol Module v5.9.

------------------------------------------------------------
# CHANGES FROM v5.9 → v6.0

- **Entity type consolidation throughout**: Trail, Trail Segment, and Trail
  Network are unified into the single Trailthing entity type. §1 Purpose, §4
  Entity Types, §7 Entity-Specific Discovery Rules, §8 Cross-Entity
  Relationships, and §11 What Discovery Must Never Do updated accordingly.
  §4.2–4.4 (Trail, Trail Segment, Trail Network) replaced by §4.2 Trailthing.
  §4.5 Site Network renumbered to §4.3. §4.6 Access Point renumbered to §4.4.

- **§18 Cross-Tier Trail Tier Assignment → Cross-Tier Trailthing Tier
  Assignment**: §18.3 discovery flag text updated to reference Trailthing.
  Scope extended from Trail-only to all Trailthings.

- **§19a Trailthing No-Classification Mandate added**: Discoverers must never
  classify a Trailthing as trail vs. trail network vs. trail segment during
  discovery. source_term_raw and source_hierarchy_context_raw capture verbatim
  source framing; hierarchy classification is deferred per IMP-009.

- **§24 Map and Asset File Preservation replaced by Document Collection
  System reference**: §24 is superseded by the Document Collection System
  defined in Discovery Orchestration Module v6.0 §4, which is more
  comprehensive (covers all document types, defines the county document log
  format, filename conventions, and download procedures).

- **All v5.9 rules carried forward**: IMP-013 (JS-paginated pages), IMP-014
  (baseline enumeration independence), IMP-015 (map verification sequencing),
  IMP-016 (GIS sub-parcel exclusion), IMP-022 (category_raw canonicalization),
  IMP-024 (YAML colon quoting), IMP-025 (YAML separators), IMP-001 (large
  municipality batching), IMP-006 (NNL designation), IMP-008 (scenic rivers),
  IMP-011/018 (cross-tier trail assignment).

------------------------------------------------------------
# 1. PURPOSE

Discovery Protocol v6.0 provides the authoritative, deterministic workflow for
discovering:

1. Site (including child Sites)
2. Trailthing
3. Site Network
4. Access Point

This protocol:

- Defines the unified discovery architecture
- Ensures consistency across all counties and data sources
- Prevents misclassification between entity types
- Prevents hierarchy classification of Trailthings during discovery
- Produces Raw Discovery Records v6.x for all four entities
- Produces Discovery Metadata v6.x for all four entities
- Integrates with Resolution, Normalization, and TSV output
- Enforces no normalization, no invention, no inference, and no silent
  correction during discovery

This module is authoritative for discovery logic.

------------------------------------------------------------
# 2. THE CORE PRINCIPLE

**Discovery = Collection. Normalization = Decisions.**

Discovery never:

- Decides if a name is correct
- Decides if an entity qualifies as a child Site
- Normalizes a vocabulary value
- Infers a township or municipality
- Assesses difficulty or accessibility
- Chooses between conflicting values
- Corrects spelling, formatting, or structure
- Classifies a Trailthing as a trail, trail network, or trail segment

All of these are Normalization decisions, made downstream.

Discovery that invents, infers, or decides corrupts the pipeline.

------------------------------------------------------------
# 3. SCOPE

Discovery Protocol v6.0 governs:

- All eight discovery tiers (Federal → Private)
- Tier-0 Baseline Loader
- All four entity types
- All authoritative sources
- All cross-entity relationships
- All discovery metadata
- All raw output rules
- Document collection (per Discovery Orchestration Module v6.0 §4)

This protocol applies to:

- Federal agencies
- State agencies
- Park districts
- Counties
- Townships
- Municipalities
- Land trusts & conservancies
- Private organizations
- Operator-provided baseline spreadsheets

------------------------------------------------------------
# 4. ENTITY TYPES (AUTHORITATIVE)

Discovery must surface candidates for all four identity-bearing entities:

## 4.1 Site
Identity-bearing land units (parks, preserves, forests, wildlife areas, etc.),
including internal identity-bearing units that qualify as child Sites under the
Child Site Rules per Site Discovery Sub-Procedure v6.0.

Child Sites are discovered exclusively through the Site Discovery Sub-Procedure
v6.0.

## 4.2 Trailthing
Any named, identity-bearing trail-related entity — including what would previously
have been classified as a Trail, Trail Segment, or Trail Network.

**The discoverer does not classify.** A Trailthing is a Trailthing. Whether it is
a trail, a trail system, a segment, a connector, or a network is determined
systematically after sufficient county runs have been collected (IMP-009). See
§19a for the no-classification mandate.

## 4.3 Site Network
Umbrella entities composed of multiple Sites.

## 4.4 Access Point
Visitor-facing navigational entry locations. Access Points may have multiple
parent entities (Sites, Trailthings).

------------------------------------------------------------
# 5. DISCOVERY TIERS

Discovery proceeds through the eight authoritative tiers in order:

1. Federal & Tribal
2. State
3. District-Level
4. County
5. Township
6. Municipal
7. Land Trust & Conservancy
8. Private
9. Tier-0 Baseline (runs last)

Each tier must surface candidates for all four entity types when applicable.

Tiers may be skipped if previously completed and sources are unchanged.
No parallelization is permitted across tiers within the same county.

------------------------------------------------------------
# 6. REQUIRED SOURCES

Each tier must check all applicable source types:

- Official websites
- GIS systems and portals
- Planning documents
- Stewardship documents
- Brochures & maps
- County auditor data
- Federal/state datasets
- Partnership announcements
- County-hosted pages
- Municipal/township-hosted pages
- Conservancy and land trust pages
- Private organization pages

All sources must be logged in discovery metadata. Qualifying documents
(maps, PDFs, GPX/KML, GIS exports) must be downloaded and logged per the
Document Collection System — see §24.

------------------------------------------------------------
# 7. ENTITY-SPECIFIC DISCOVERY RULES

Discovery must use the authoritative sub-procedure for each entity type:

- Site Discovery Sub-Procedure v6.0
- Trailthing Discovery Sub-Procedure v6.0
- Site Network Discovery Sub-Procedure v6.0
- Access Point Discovery Sub-Procedure v6.0

Discovery must also use the authoritative tier sub-procedure for each tier:

- Federal & Tribal Lands Discovery Sub-Procedure v6.0
- State Lands Discovery Sub-Procedure v6.0
- District-Level Public Landholders Discovery Sub-Procedure v6.0
- County Lands Discovery Sub-Procedure v6.0
- Township Lands Discovery Sub-Procedure v6.0
- Municipal Lands Discovery Sub-Procedure v6.0
- Conservancy & Land Trust Discovery Sub-Procedure v6.0
- Private & Organization-Based Discovery Sub-Procedure v6.0

Child Sites are surfaced via the Site Discovery Sub-Procedure v6.0 and
represented as Sites with Parent Site relationships.

Within each tier, entity types are processed in this order:
**Sites → Trailthings → Site Networks → Access Points**

Every entity type requires a documented result before closing a tier — either
entities or a confirmed null with evidence and sources checked. Silence is not
a null.

------------------------------------------------------------
# 8. CROSS-ENTITY RELATIONSHIP RULES

Discovery must identify and record all discoverable relationships:

- Site → child Site
- Trailthing → parent Trailthing (self-referential; only when source explicitly
  documents the hierarchy)
- Trailthing → parent Site (only when source explicitly documents containment
  and access dependency)
- Trailthing → external parent (Site Network or other; only when source
  explicitly documents membership)
- Site Network → member Sites
- Access Point → parent Entities (Sites, Trailthings)

All relationships must be recorded in raw form — names and references as
discovered, not normalized IDs. Resolution resolves names to IDs downstream.

**Do not infer Trailthing hierarchy from geography, governance, or name
similarity.** Only record parent relationships when the authoritative source
explicitly documents them.

All relationships must be logged in discovery metadata.

------------------------------------------------------------
# 9. MULTI-COUNTY RULE

Discovery must follow the authoritative multi-county rule:

- No segmentation of multi-county entities
- Record all counties exactly as discovered
- Preserve raw county lists in metadata
- Normalization alphabetizes and semicolon-delimits

Applies to all four entity types.

------------------------------------------------------------
# 10. DISCOVERY MODES

## 10.1 Enumerative Discovery
Performed by Tier Sub-Procedures v6.0.

Enumerative discovery must:

- Identify authoritative listing/index pages
- Extract all first-level entity URLs
- Queue each for entity detection and extraction

**JS-rendered and paginated listing pages (IMP-013)**: Some listing pages use
JavaScript rendering or lazy pagination (FacetWP, infinite scroll, numbered page
controls). Standard web fetch retrieves only the first page. When such pages are
encountered, all pages must be iterated before the listing is treated as complete.
Document the pagination type and iteration method in discovery metadata. See
Municipal Discovery Sub-Procedure v6.0 §4.3b for the full protocol.

## 10.2 Recursive Discovery
Performed by URL propagation within tier allowlists.

Recursive discovery must:

- Extract internal links
- Follow allowed patterns
- Enforce depth and count limits
- Queue child URLs
- Record parent_url for provenance

------------------------------------------------------------
# 11. WHAT DISCOVERY MUST NEVER DO

Discovery must never:

- Normalize names, types, or values
- Infer township or municipality
- Assess or infer difficulty or accessibility
- Invent GPS coordinates, locations, or parent relationships
- Deduplicate entities
- Choose between conflicting values
- Silently correct malformed values
- Apply vocabulary rules to raw values
- **Classify a Trailthing as a trail, trail network, or trail segment**
  (see §19a No-Classification Mandate)
- Create Site records for GIS administrative sub-parcels that lack independent
  identity on the managing entity's official website; the exclusion criterion is
  absence of independent identity, not the naming pattern alone — apply the
  official website test in Site Discovery Sub-Procedure v6.0 §5 rule 8 before
  excluding or collapsing; when GIS sub-parcels are collapsed into one Site,
  sum all constituent parcel acreages for acres_raw (IMP-016)

------------------------------------------------------------
# 12. CONSOLIDATION RULES

Discovery does not consolidate entities.

Consolidation is performed exclusively by the Resolution Engine v6.0, which:

- Merges identical entities across tiers
- Applies tier precedence
- Preserves conflicts
- Aligns parent/child relationships
- Aligns network membership
- Aligns Access Point parent sets

Discovery produces raw, unmerged, unnormalized records only.

------------------------------------------------------------
# 13. METADATA REQUIREMENTS

Discovery must produce a complete Discovery Metadata Object for every raw record.

Metadata must include:

- Identity metadata (raw)
- Tier metadata
- Source metadata
- Parent URL (if recursive)
- Conflict indicators
- Uncertainty indicators
- Parent entity hints (Access Points)
- Boundary metadata
- County list (raw)
- Notes

Metadata must conform to discovery metadata requirements and the Audit &
Logging Module v6.0.

------------------------------------------------------------
# 14. OUTPUT FORMAT

Discovery must output Raw Discovery Records v6.x for all four entities.

All outputs must conform to:

- Discovery Orchestration Module v6.0
- All Schema Modules v6.0
- All Vocabulary Modules v6.0

Discovery must not normalize, correct, dedupe, infer, invent, or silently modify.

Discovery may generate TSV previews when explicitly requested.

------------------------------------------------------------
# 15. INTEGRATION POINTS

This module integrates with:

- All four Schema Modules v6.0
- All four Vocabulary Modules v6.0
- Four Entity Discovery Sub-Procedures v6.0
- Eight Tier Discovery Sub-Procedures v6.0
- Discovery Orchestration Module v6.0
- Resolution Engine v6.0
- Normalization Engine v6.0
- Entity Upsert Engine v6.x *(or v5.x)*
- Audit & Logging Module v6.0
- County Baseline Module v6.x *(or v5.x)*

------------------------------------------------------------
# 16. MODULE DEPENDENCIES

This module depends on:

- Discovery Orchestration Module v6.0
- Four Entity Discovery Sub-Procedures v6.0
- Eight Tier Discovery Sub-Procedures v6.0
- Resolution Engine v6.0
- Audit & Logging Module v6.0
- County Baseline Module v6.x *(or v5.x)*

------------------------------------------------------------
# 17. DESIGNATION-BASED ENTITY RULES

Certain federal and state designations require explicit handling at discovery
time because their classification interacts with tier assignment and entity type
in non-obvious ways.

## 17.1 National Natural Landmark (NNL)

NNL is a federal designation attribute, not a management tier.

- An NNL-designated land unit is assigned to its **management tier**, regardless
  of the federal designation. An NNL on an ODNR State Nature Preserve stays
  Tier 2. An NNL on a metro park district property stays Tier 3.
- The `designation` field captures "National Natural Landmark".
- Do not elevate an entity to Tier 1 solely because it carries an NNL designation.
- Do not create a separate Tier 1 entity for the NNL designation itself.
- NNL status is documented in discovery metadata and `identity_notes_raw`.

## 17.2 Scenic River Designations (State Scenic River / National Wild and Scenic River)

Scenic river designations are legal status attributes, not site categories.

- A scenic river designation is a **Site** with:
  - `category` = Water Site
  - `subtype` = River
  - `designation` = State Scenic River, National Wild and Scenic River, or both
    (semicolon-delimited)
- **Do not create a Site Network** for the scenic designation.
- Scenic river Sites are discovered at **Tier 2** (ODNR Scenic Rivers Program).
  See State Lands Discovery Sub-Procedure v6.0.
- Access Points along a scenic river (boat launches, fishing access) are Access
  Point entities parented to the scenic river Site.
- **Water trail intersection**: A water trail Trailthing overlapping a scenic
  river corridor is a separate Trailthing entity, not the same entity as the
  scenic river Site. Flag overlapping records with:
  `identity_notes_raw: "Scenic river corridor — water trail Trailthing may exist"`

------------------------------------------------------------
# 18. CROSS-TIER TRAILTHING TIER ASSIGNMENT

Named Trailthings — particularly greenways and multi-park corridors — are
frequently documented at more than one discovery tier. This section governs how
such entities are handled at discovery time.

## 18.1 Management Tier Governs

The **primary managing entity's tier** is the canonical tier for a Trailthing.
Management tier is determined by the entity that holds primary operational
responsibility for the Trailthing, regardless of which other tiers have information.

- **Primary managing entity** = the agency that maintains the trail surface,
  manages trail access, and carries maintenance responsibility.
- Management tier is not necessarily the lowest-numbered tier.

## 18.2 Both Tiers Stage Records

When a Trailthing is discoverable at multiple tiers, **every tier that has
authoritative source material must stage a discovery record**. Discovery must
never suppress a Trailthing record merely because another tier is expected to
stage it.

- Stage at the tier whose source provides the richest authoritative data.
- Cross-tier duplication is correct behavior at discovery time.

## 18.3 Discovery Metadata Requirements for Cross-Tier Trailthings

When staging a Trailthing record at a tier that is NOT the primary managing
entity's tier:

- Record `governance_raw` exactly as stated in the local source.
- Add to `identity_notes_raw`: `"Cross-tier trail — primary manager may be [tier
  name / entity name]; Tier N documents this trail"`
- This flag informs Resolution that a cross-tier canonicalization decision is needed.

When staging a Trailthing record at the primary managing tier:
- Record comprehensive governance and management evidence.
- No special flag is required — this is the canonical record.

## 18.4 Resolution Handles Canonicalization

Discovery does not determine which record is canonical. Resolution Engine v6.0
merges cross-tier records and assigns canonical status to the management tier's
record (see Resolution Engine v6.0 §11.8).

------------------------------------------------------------
# 19. BASELINE ENUMERATION INDEPENDENCE (IMP-014)

The operator-provided baseline spreadsheet establishes the seed set of known
entities at the start of county discovery. It does not define the universe of
entities.

Website enumeration must always be performed independently of the baseline:

- **Always enumerate official websites fully and independently.** Do not stop
  because the number of entities found matches or approaches the baseline seed
  count.
- **The website count is the authoritative count** for a completed source.
- **Do not assume the baseline seed count equals the total entity count.** Parks,
  trails, and open spaces are added to official sources after the baseline is
  created. Post-baseline additions must be discovered.

When the website count exceeds the baseline seed count, the excess entities are
new discoveries — not errors. Stage them as normal raw discovery records.

When the baseline seed count exceeds the website count, investigate before
recording zero for the gap. Flag the discrepancy in discovery metadata.

The baseline is a starting point and a reference. It is not a ceiling.

------------------------------------------------------------
# 19a. TRAILTHING NO-CLASSIFICATION MANDATE (IMP-009)

**The discoverer does not classify Trailthings.**

When an authoritative source documents a named trail-related entity — whether it
calls it a "trail system," a "greenway," a "connector," a "section," a "route,"
or a "water trail" — the discoverer creates a Trailthing record. The discoverer
does not decide whether that entity is a Trail, a Trail Segment, or a Trail
Network.

This classification is deferred until after sufficient county runs have been
completed to establish hierarchy patterns empirically (target: 30 v6 county runs
per IMP-009). The `source_term_raw` and `source_hierarchy_context_raw` fields
capture verbatim source framing and are the primary input for that future analysis.

**In practice, this means:**

- Do not create separate Trailthing records for different "levels" of a trail
  system when those levels are not separately named and documented by the source.
- Do not infer that a "trail system" name implies there must be separate
  constituent trail records — only create constituent records when the source
  explicitly names and documents them.
- Do not use the presence of multiple trailheads, loops, or physical sections to
  justify creating hierarchy where the source does not document it.
- Do not add a "parent" Trailthing relationship unless the source explicitly frames
  one entity as a sub-component of another.

**What to capture instead of classifying:**

- `source_term_raw`: the exact term the source uses to describe this entity
  (e.g., "trail system", "greenway", "connector trail", "loop", "water trail",
  "section", "segment", "hub", "route") — **this field is REQUIRED**
- `source_hierarchy_context_raw`: how the source frames this entity in relation
  to others (e.g., "part of the X System", "one of seven trails", "northern
  reach of the Y Blueway") — optional
- `parent_id_raw`: only when the source explicitly states this entity is a
  component of another documented Trailthing
- `site_parent_raw`: only when the source explicitly states this entity is
  contained within and access-dependent on a specific named Site

**Surface/status/governance variation**: A trail that changes surface, status,
or governance along its corridor does NOT require multiple Trailthing records.
Document the variation in `notes_raw`. Only create separate Trailthings when
the source itself names and documents those sections as distinct identity-bearing
entities.

------------------------------------------------------------
# 20. MAP VERIFICATION SEQUENCING IN MULTI-MUNICIPALITY COUNTIES (IMP-015)

Map verification (viewing Google Maps or equivalent directly for each
municipality) is mandatory for all Tier 6 municipalities. In counties with
multiple adjacent municipalities, the sequencing matters.

**Rule**: Complete all municipal web discovery for **all** municipalities before
running map verification for **any** of them. Map verification runs as a single
consolidated pass across all jurisdictions.

**Why**: Running map verification per municipality as web discovery proceeds
risks false positives from parks in adjacent un-cataloged jurisdictions being
incorrectly attributed to the wrong jurisdiction.

**This rule does not apply** to isolated municipalities or to single-municipality
counties, where per-municipality verification is fine.

See also: Municipal Discovery Sub-Procedure v6.0 §4.4.

------------------------------------------------------------
# 21. CATEGORY FIELD STANDARDIZATION (IMP-022)

`category_raw` is the single authorized field name for recording entity category
in all staging records, across all entity types and all discovery tiers.

**Deprecated field names — must not appear in new staging records:**
- `park_type_raw` — retired; maps to `category_raw`
- `site_type_raw` — retired; maps to `category_raw`

**Correct usage:**
```yaml
category_raw: "Nature Preserve"   ✓
park_type_raw: "Nature Preserve"  ✗  deprecated
site_type_raw: "Nature Preserve"  ✗  deprecated
```

------------------------------------------------------------
# 22. YAML STAGING FORMAT REQUIREMENTS

All discovery staging files are YAML. The following formatting rules are mandatory
for all records in all staging files.

## 22.1 Colon Quoting (IMP-024)

Any field value that contains a literal colon character must be enclosed in
double quotes. In YAML, an unquoted colon followed by a space is interpreted as
a key-value separator, which breaks the parse.

**Rule**: Quote any value containing `:`.

```yaml
# CORRECT
governance_raw: "City of Dublin"
identity_notes_raw: "Source: MORPC Parks layer; note: verified 2026-03-21"
name_raw: "Olentangy: North Connector Trail"

# WRONG — unquoted colon causes YAML parse error
governance_raw: City of Dublin; GIS park type: Community Park
identity_notes_raw: Source: MORPC Parks layer
```

When in doubt, quote the value. Quoted values that don't need quoting are valid
YAML; unquoted values with colons are not.

## 22.2 Record Separators (IMP-025)

Every discovery record in a staging file must be preceded by a `---` YAML
document separator. Omitting separators causes block-end parse errors when
multiple records are concatenated.

**Rule**: Every entity record begins with `---` on its own line.

```yaml
---
entity_type: Site
name_raw: "Griggs Reservoir Park"
governance_raw: "City of Columbus"
discovery_tier: 6

---
entity_type: Site
name_raw: "Antrim Park"
governance_raw: "City of Columbus"
discovery_tier: 6
```

**When appending to an existing staging file**: Always add `---` before the new
record, even when the file already ends with another record.

**Tier transitions**: When appending Tier 6 records after Tier 5 records in the
same staging file, the `---` separator is still required between every individual
entity record, not just between tier blocks.

------------------------------------------------------------
# 23. LARGE MUNICIPALITY BATCHING (IMP-001)

Municipalities with more than 100 parks require alphabetical batching. See
Municipal Discovery Sub-Procedure v6.0 §5.13 for the full protocol.

**Trigger**: >100 parks total (all entity types) in the municipality.

**Method**: Alphabetical, 100 parks per batch, preceded by mandatory full
enumeration.

**All batches write to the same staging YAML file.**

**Map verification runs once, after all batches are complete.**

**Completion**: All batches marked complete in session log + map verification
done + all baseline seeds confirmed or flagged.

------------------------------------------------------------
# 24. DOCUMENT COLLECTION

During discovery, qualifying source documents — trail maps, park brochures,
paddling guides, master plans, GPX/KML files, GIS exports, and similar spatial
or descriptive documents — must be downloaded and logged.

**This section is governed by Discovery Orchestration Module v6.0 §4**
(Document Collection System), which is the authoritative definition of:

- What qualifies for download
- What is logged URL-only (interactive GIS viewers, REST endpoints)
- What is skipped (general HTML pages, contact pages)
- The county document log format ({county}_document_log.yaml)
- The filename convention ({date}_{tier}_{short-descriptor}.{ext})
- The source_documents/ folder structure
- Document type vocabulary (11 values)
- Failed download logging

The tier sub-procedures (§3.x sections) contain tier-specific priorities for
document collection — particularly high-value document types for that tier.

**Relationship to v5.9 §24**: The v5.9 Map and Asset File Preservation section
(§24) is superseded by this reference. The Document Collection System is more
comprehensive: it covers all document types (not just maps/brochures), defines
a formal county document log, and provides a standardized filename convention.
The underlying obligation (download at discovery time; do not defer) is unchanged.

------------------------------------------------------------
# END OF DISCOVERY PROTOCOL MODULE v6.0
