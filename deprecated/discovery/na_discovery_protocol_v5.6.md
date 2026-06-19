# NATURAL AREAS PROJECT
# DISCOVERY PROTOCOL MODULE v5.6
(Authoritative Multi-Entity Discovery Framework)

This module defines the authoritative, deterministic protocol for discovering
all six entity types in the statewide Natural Areas & Trails system.

This module defines:

- The unified discovery workflow
- The six discovery tracks
- Tier-based source rules
- Entity-specific discovery rules
- Cross-entity relationship rules
- Designation-based entity rules
- Cross-tier trail tier assignment rules
- Metadata requirements
- Raw output requirements
- Integration points with Resolution, Normalization, and Entity Upsert
- Provenance and audit requirements

This module supersedes Discovery Protocol Module v4.0, v5.2, v5.3, v5.4, and v5.5.

------------------------------------------------------------
# CHANGES FROM v5.5 → v5.6

- Updated §10.1 Enumerative Discovery with JS pagination note (IMP-013): Listing
  pages using JavaScript rendering or lazy pagination must have all pages iterated
  before the listing is treated as complete. See Municipal Discovery Subproc v5.7
  §4.3b for the full protocol.
- Added §19 Baseline Enumeration Independence (IMP-014): Website enumeration is
  always independent of the baseline seed count. The official website count is the
  authoritative count for a completed source; the baseline is a starting point, not
  a ceiling.
- Added §20 Map Verification Sequencing in Multi-Municipality Counties (IMP-015):
  In counties with multiple adjacent municipalities, complete all municipal web
  discovery first, then run a single consolidated map verification pass. Per-
  municipality map verification risks false positives from adjacent un-cataloged
  jurisdictions.
- Updated §11 What Discovery Must Never Do with GIS sub-parcel exclusion (IMP-016):
  Discovery must never create Site records for GIS administrative sub-parcels that
  lack independent identity on the managing entity's official website. Exclusion
  criterion is absence of independent identity (not naming pattern alone); summing
  of constituent parcel acreages required when collapsing. See Site Discovery
  Subproc v5.5 §5 rule 8 for the full test.

------------------------------------------------------------
# CHANGES FROM v5.4 → v5.5

- Added §18 Cross-Tier Trail Tier Assignment (IMP-011, IMP-018):
  Management tier governs when a named trail is managed by one tier but documented
  at multiple tiers. Both tiers stage records; Resolution assigns canonical status
  to the management tier. Discovery metadata must identify the primary managing entity.
  See also: District Discovery Subproc v5.4 §4.6; Municipal Discovery Subproc v5.5 §8.3;
  Resolution Engine v5.5 §11.8.

------------------------------------------------------------
# CHANGES FROM v5.3 → v5.4

- Added §17 Designation-Based Entity Rules, covering:
  - IMP-006: NNL (National Natural Landmark) — designation attribute, not management tier;
    entity stays at its management tier; `designation` field captures "National Natural Landmark"
  - IMP-008: Scenic rivers — Sites with category=Water Site, subtype=River, and designation=
    State Scenic River or National Wild and Scenic River; NOT Site Networks; the scenic
    designation is a legal status handled by the Designation field

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.3

- Updated module version to v5.3
- Updated all cross-module references to v5.x
- Updated organizational field cluster to four-field model:
  ownership_raw, governance_raw, partner_agencies_raw, coordination_raw
- Replaced address_raw with location_raw for Sites and Access Points
- Updated integration points and module dependencies to v5.x
- Updated output field model to v5.3:
  gps_raw replaced by gps_lat_raw and gps_lon_raw
  maps_raw removed; map URLs included in urls_raw
  url_primary renamed to url_primary_raw
  url_all renamed to urls_raw
  notes_raw renamed to identity_notes_raw
  geometry_raw removed
- Discovery Output Specification v5.x retired; all references now v5.x
- No changes to discovery philosophy or mechanics

------------------------------------------------------------
# 1. PURPOSE

Discovery Protocol v5.5 provides the authoritative, deterministic workflow for
discovering:

1. Site (including child Sites)
2. Trail
3. Trail Segment
4. Trail Network
5. Site Network
6. Access Point

This protocol:

- Defines the unified discovery architecture
- Ensures consistency across all counties and data sources
- Prevents misclassification between entity types
- Produces Raw Discovery Records v5.x for all six entities
- Produces Discovery Metadata v5.x for all six entities
- Integrates with Resolution, Normalization, and TSV output
- Enforces no normalization, no invention, no inference, and no silent correction during discovery

This module is authoritative for discovery logic.

------------------------------------------------------------
# 2. THE CORE PRINCIPLE

Discovery = Collection. Normalization = Decisions.

Discovery never:

- Decides if a name is correct
- Decides if an entity qualifies as a child Site
- Normalizes a vocabulary value
- Infers a township or municipality
- Assesses difficulty or accessibility
- Chooses between conflicting values
- Corrects spelling, formatting, or structure

All of these are Normalization decisions, made downstream.

Discovery that invents, infers, or decides corrupts the pipeline.

------------------------------------------------------------
# 3. SCOPE

Discovery Protocol v5.5 governs:

- All eight discovery tiers (Federal → Private)
- Tier‑0 Baseline Loader
- All six entity types
- All authoritative sources
- All cross-entity relationships
- All discovery metadata
- All raw output rules

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

Discovery must surface candidates for all six identity-bearing entities:

## 4.1 Site
Identity-bearing land units (parks, preserves, forests, wildlife areas, etc.),
including internal identity-bearing units that qualify as child Sites under the
Child Site Rules Module v5.x.

Child Sites are discovered exclusively through the Site Discovery Sub-Procedure v5.x.

## 4.2 Trail
Identity-bearing linear corridors.

## 4.3 Trail Segment
Operational portions of Trails that meet the Trail Segment Identity Rule.

## 4.4 Trail Network
Umbrella entities composed of multiple Trails.

## 4.5 Site Network
Umbrella entities composed of multiple Sites.

## 4.6 Access Point
Visitor-facing navigational entry locations.
Access Points may have multiple parent entities (Sites, Trails, Trail Segments).

------------------------------------------------------------
# 5. DISCOVERY TIERS

Discovery proceeds through the eight authoritative tiers in order:

1. Federal
2. State
3. District-Level
4. County
5. Township
6. Municipal
7. Land Trust & Conservancy
8. Private
9. Tier‑0 Baseline (runs last)

Each tier must surface candidates for all six entity types when applicable.

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

All sources must be logged in Discovery Metadata v5.x.

------------------------------------------------------------
# 7. ENTITY-SPECIFIC DISCOVERY RULES

Discovery must use the authoritative sub-procedure for each entity type:

- Site Discovery Sub-Procedure v5.x
- Trail Discovery Sub-Procedure v5.x
- Trail Segment Discovery Sub-Procedure v5.x
- Trail Network Discovery Sub-Procedure v5.x
- Site Network Discovery Sub-Procedure v5.x
- Access Point Discovery Sub-Procedure v5.x

Child Sites are surfaced via the Site Discovery Sub-Procedure v5.x and represented
as Sites with Parent Site relationships, governed by the Child Site Rules Module v5.x.

------------------------------------------------------------
# 8. CROSS-ENTITY RELATIONSHIP RULES

Discovery must identify and record all discoverable relationships:

- Site → child Site
- Trail → Trail Segment
- Trail Network → Trail
- Site Network → Site
- Access Point → Parent Entities (Sites, Trails, Trail Segments)

All relationships must be recorded in raw form — names and references as discovered,
not normalized IDs. Resolution resolves names to IDs downstream.

All relationships must be logged in Discovery Metadata v5.x.

------------------------------------------------------------
# 9. MULTI-COUNTY RULE

Discovery must follow the authoritative multi-county rule:

- No segmentation of multi-county entities
- Record all counties exactly as discovered
- Preserve raw county lists in metadata
- Normalization alphabetizes and semicolon-delimits

Applies to all six entity types.

------------------------------------------------------------
# 10. DISCOVERY MODES

## 10.1 Enumerative Discovery
Performed by Tier Sub-Procedures v5.x.

Enumerative discovery must:

- Identify authoritative listing/index pages
- Extract all first-level entity URLs
- Queue each for entity detection and extraction

**JS-rendered and paginated listing pages (IMP-013)**: Some listing pages use
JavaScript rendering or lazy pagination (FacetWP, infinite scroll, numbered page
controls). Standard web fetch retrieves only the first page. When such pages are
encountered, all pages must be iterated before the listing is treated as complete.
Document the pagination type and iteration method in discovery metadata. See
Municipal Discovery Sub-Procedure v5.7 §4.3b for the full protocol.

## 10.2 Recursive Discovery
Performed by the Discovery Engine via URL propagation.

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
- Create Site records for GIS administrative sub-parcels that lack independent
  identity on the managing entity's official website; the exclusion criterion is
  absence of independent identity, not the naming pattern alone — apply the official
  website test in Site Discovery Sub-Procedure v5.5 §5 rule 8 before excluding or
  collapsing; when GIS sub-parcels are collapsed into one Site, sum all constituent
  parcel acreages for acres_raw (IMP-016)

------------------------------------------------------------
# 12. CONSOLIDATION RULES

Discovery does not consolidate entities.

Consolidation is performed exclusively by the Resolution Engine v5.x, which:

- Merges identical entities across tiers
- Applies tier precedence
- Preserves conflicts
- Aligns parent/child relationships
- Aligns network membership
- Aligns Access Point parent sets

Discovery produces raw, unmerged, unnormalized records only.

------------------------------------------------------------
# 13. METADATA REQUIREMENTS

Discovery must produce a complete Discovery Metadata Object v5.x for every raw record.

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

Metadata must conform to:

- Discovery Metadata Specification v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# 14. OUTPUT FORMAT

Discovery must output Raw Discovery Records v5.x for all six entities.

All outputs must conform to:

- Discovery Output Specification v5.x
- All Schema Modules v5.x
- All Vocabulary Modules v5.x

Discovery must not normalize, correct, dedupe, infer, invent, or silently modify.

Discovery may generate TSV previews when explicitly requested.

------------------------------------------------------------
# 15. INTEGRATION POINTS

This module integrates with:

- All six Schema Modules v5.x
- All six Vocabulary Modules v5.x
- All Discovery Sub-Procedures v5.x
- All Tier Sub-Procedures v5.x
- Discovery Metadata Specification v5.x
- Discovery Output Specification v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- Entity Upsert Engine v5.x
- Processing / Orchestration Module v5.x
- Audit & Logging Module v5.x
- County Baseline Module v5.x

------------------------------------------------------------
# 16. MODULE DEPENDENCIES

This module depends on:

- Discovery Output Specification v5.x
- Discovery Metadata Specification v5.x
- Discovery Orchestration Module v5.x
- All six entity Discovery Sub-Procedures v5.x
- All eight Tier Sub-Procedures v5.x
- Child Site Rules Module v5.x
- Resolution Engine v5.x
- Audit & Logging Module v5.x
- County Baseline Module v5.x

------------------------------------------------------------
# 17. DESIGNATION-BASED ENTITY RULES

Certain federal and state designations require explicit handling at discovery time because
their classification interacts with tier assignment and entity type in non-obvious ways.

## 17.1 National Natural Landmark (NNL)

NNL is a federal designation attribute, not a management tier.

- An NNL-designated land unit is assigned to its **management tier**, regardless of the
  federal designation. An NNL on an ODNR State Nature Preserve stays Tier 2. An NNL on a
  metro park district property stays Tier 3. An NNL on a private conservancy property stays
  Tier 7.
- The `designation` field captures "National Natural Landmark".
- Do not elevate an entity to Tier 1 solely because it carries an NNL designation.
- Do not create a separate Tier 1 entity for the NNL designation itself.
- NNL status is documented in discovery metadata and `identity_notes_raw` where found.

## 17.2 Scenic River Designations (State Scenic River / National Wild and Scenic River)

Scenic river designations are legal status attributes, not site categories.

- A scenic river designation is a **Site** with:
  - `category` = Water Site
  - `subtype` = River
  - `designation` = State Scenic River, National Wild and Scenic River, or both (semicolon-delimited)
- **Do not create a Site Network** for the scenic designation. The designation is handled by
  the Designation field, parallel to State Nature Preserve and NNL.
- Scenic river Sites are discovered at **Tier 2** (ODNR Scenic Rivers Program).
  See State Lands Discovery Sub-Procedure v5.x §3.5 and §4.5.
- Access Points along a scenic river (boat launches, fishing access) are Access Point entities
  parented to the scenic river Site.
- **Water trail intersection**: A water trail overlapping a scenic river corridor produces
  separate Trail or Trail Segment entities in addition to the Water Site. The scenic river
  Site and the water trail Trail are related entities, not the same entity. Flag overlapping
  records with `identity_notes_raw: "Scenic river corridor — water trail entity may exist"`.
  This intersection is flagged for revisit when water trail discovery begins.

------------------------------------------------------------
# 18. CROSS-TIER TRAIL TIER ASSIGNMENT

Named trails — particularly greenways and multi-park corridors — are frequently documented
at more than one discovery tier. A metro park district trail may also appear on a municipal
recreation page; a state-managed bikeway may appear at Tier 6. This section governs how
such trails are handled at discovery time.

## 18.1 Management Tier Governs

The **primary managing entity's tier** is the canonical tier for a trail. Management tier
is determined by the entity that holds primary operational responsibility for the trail,
regardless of which other tiers have information about it.

- **Primary managing entity** = the agency or organization that maintains the trail surface,
  manages trail access, and carries maintenance responsibility (not merely an agency that
  references the trail, cross-promotes it, or holds a corridor easement).
- Management tier is not necessarily the lowest-numbered tier. A city (Tier 6) may be the
  primary manager of a trail that also passes through or is documented by a county (Tier 4).

## 18.2 Both Tiers Stage Records

When a trail is discoverable at multiple tiers, **every tier that has authoritative source
material for the trail must stage a discovery record**. Discovery must never suppress a
trail record merely because another tier is expected to stage it.

- Stage at the tier whose source provides the richest authoritative data.
- Stage at every additional tier where the trail appears in an authoritative source.
- Cross-tier duplication is correct behavior at discovery time.

## 18.3 Discovery Metadata Requirements for Cross-Tier Trails

When staging a trail record at a tier that is NOT the primary managing entity's tier:

- Record `governance_raw` exactly as stated in the local source. If the local source
  correctly attributes the trail to another tier's entity, record that value.
- Add to `identity_notes_raw`: `"Cross-tier trail — primary manager may be [tier name/entity name]"`
- This flag informs Resolution that a cross-tier canonicalization decision is needed.

When staging a trail record at the primary managing tier:

- Record comprehensive governance and management evidence.
- No special flag is required — this is the canonical record.

## 18.4 Resolution Handles Canonicalization

Discovery does not determine which record is canonical. Resolution Engine v5.x merges
cross-tier records for the same trail and assigns canonical status to the management tier's
record (see Resolution Engine v5.5 §11.8). The non-canonical record's data is preserved
in resolution provenance.

------------------------------------------------------------
# 19. BASELINE ENUMERATION INDEPENDENCE (IMP-014)

The operator-provided baseline spreadsheet establishes the seed set of known entities
at the start of county discovery. It does not define the universe of entities.

Website enumeration must always be performed independently of the baseline:

- **Always enumerate official websites fully and independently.** Do not stop
  enumerating because the number of entities found matches or approaches the baseline
  seed count.
- **The website count is the authoritative count** for a completed source. If the
  official parks page lists 47 parks, the discovery output must include 47 parks —
  regardless of what the baseline contains.
- **Do not assume the baseline seed count equals the total entity count** for any
  source. Parks, trails, and open spaces are added to official sources after the
  baseline is created. Post-baseline additions must be discovered.

When the website count exceeds the baseline seed count, the excess entities are not
errors — they are new discoveries. Stage them as normal raw discovery records.

When the baseline seed count exceeds the website count, investigate before recording
zero for the gap. Entities may have been renamed, moved, or removed from the website
without being decommissioned. Flag the discrepancy in discovery metadata.

The baseline is a starting point and a reference. It is not a ceiling.

------------------------------------------------------------
# 20. MAP VERIFICATION SEQUENCING IN MULTI-MUNICIPALITY COUNTIES (IMP-015)

Map verification (viewing Google Maps or equivalent directly for each municipality)
is mandatory for all Tier 6 municipalities. In counties with multiple adjacent
municipalities, the sequencing of map verification matters.

**Rule**: In counties with two or more adjacent municipalities, complete all
municipal web discovery (Steps 2, 3, 4.3a, 4.3b of the Municipal Discovery
Sub-Procedure v5.7) for **all** municipalities before running map verification
for **any** of them. Map verification then runs as a single consolidated pass
across all jurisdictions.

**Why**: Running map verification per municipality as web discovery proceeds risks
false positives. Parks in adjacent un-cataloged jurisdictions appear on the map
during verification of a specific municipality and may be incorrectly attributed
to the wrong jurisdiction. The consolidated pass is performed after all web
discovery is complete, providing the full picture of what is already cataloged
and making jurisdictional attributions accurate.

**This rule does not apply** to isolated municipalities (no adjacent municipality in
the same county) or to single-municipality counties, where per-municipality
verification is fine.

See also: Municipal Discovery Sub-Procedure v5.7 §4.4.

------------------------------------------------------------
# END OF DISCOVERY PROTOCOL MODULE v5.6
