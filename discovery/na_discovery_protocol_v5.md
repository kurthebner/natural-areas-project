# NATURAL AREAS PROJECT
# DISCOVERY PROTOCOL MODULE v5.0
(Authoritative Multi-Entity Discovery Framework)

This module defines the authoritative, deterministic protocol for discovering
all six entity types in the statewide Natural Areas & Trails system.

This module defines:

- The unified discovery workflow
- The six discovery tracks
- Tier-based source rules
- Entity-specific discovery rules
- Cross-entity relationship rules
- Metadata requirements
- Raw output requirements
- Integration points with Resolution, Normalization, and Entity Upsert
- Provenance and audit requirements

This module supersedes Discovery Protocol Module v4.0.

------------------------------------------------------------
# CHANGES FROM v4.0

- `role_raw` removed from discovery outputs — role field deleted from Access Point schema
- `access_level_raw` removed from discovery outputs — access_level field deleted from Access Point schema
- `features_raw` added — for Access Point and Site features
- `difficulty_raw` added — for Trail and Trail Segment discovery
- `accessibility_raw` added — for Trail and Trail Segment discovery
- `maps_raw` added — for multiple map URLs (Trails, Trail Segments, Networks)
- `township_raw` and `municipality_raw` explicitly prohibited during discovery — GIS-derived only
- **Core principle reinforced**: Discovery = Collection. Normalization = Decisions.
- Discovery must never assess, infer, or evaluate — only collect and record
- All version references updated to v5.0

------------------------------------------------------------
# 1. PURPOSE

Discovery Protocol v5.0 provides the authoritative, deterministic workflow for
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
- Produces **Raw Discovery Records v5.0** for all six entities
- Produces **Discovery Metadata v5.0** for all six entities
- Integrates with Resolution, Normalization, and TSV output
- Enforces **no normalization, no invention, no inference, and no silent correction** during discovery

This module is authoritative for discovery logic.

------------------------------------------------------------
# 2. THE CORE PRINCIPLE

**Discovery = Collection. Normalization = Decisions.**

Discovery's only job is to find and faithfully record what exists in authoritative
sources. Discovery never:

- Decides if a name is correct
- Decides if an entity qualifies as a child Site
- Normalizes a vocabulary value
- Infers a township or municipality
- Assesses difficulty or accessibility
- Chooses between conflicting values
- Corrects spelling, formatting, or structure

All of these are Normalization decisions, made downstream.

Discovery that invents, infers, or decides is discovery that corrupts the pipeline.

------------------------------------------------------------
# 3. SCOPE

Discovery Protocol v5.0 governs:

- All eight discovery tiers (Federal → Private)
- Tier-0 Baseline Loader
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
including internal identity-bearing units that qualify as **child Sites** under
the **Child Site Rules Module v5.0**.

Child Sites are discovered **exclusively through the Site Discovery Sub-Procedure v5.0**.

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
Access Points may have **multiple parent entities** (Sites, Trails, Trail Segments).

------------------------------------------------------------
# 5. DISCOVERY TIERS

Discovery proceeds through the eight authoritative tiers in order:

1. Federal
2. State
3. District-Level
4. County
5. Township
6. Municipal
7. Conservancy
8. Private
9. **Tier-0 Baseline** (operator-provided; runs last)

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

All sources must be logged in **Discovery Metadata v5.0**.

------------------------------------------------------------
# 7. ENTITY-SPECIFIC DISCOVERY RULES

Discovery must use the authoritative sub-procedure for each entity type:

## 7.1 Site Discovery
Use **Site Discovery Sub-Procedure v5.0**.
Must surface:

- Top-level Sites
- Child Sites
- Parent Site relationships

## 7.2 Trail Discovery
Use **Trail Discovery Sub-Procedure v5.0**.

## 7.3 Trail Segment Discovery
Use **Trail Segment Discovery Sub-Procedure v5.0**.

## 7.4 Trail Network Discovery
Use **Trail Network Discovery Sub-Procedure v5.0**.

## 7.5 Site Network Discovery
Use **Site Network Discovery Sub-Procedure v5.0**.

## 7.6 Access Point Discovery
Use **Access Point Discovery Sub-Procedure v5.0**.

------------------------------------------------------------
# 8. CROSS-ENTITY RELATIONSHIP RULES

Discovery must identify and record all discoverable relationships:

- Site → child Site
- Trail → Trail Segment
- Trail Network → Trail
- Site Network → Site
- **Access Point → Parent Entities (multiple allowed: Sites, Trails, Trail Segments)**

All relationships must be recorded in raw form — names and references as discovered,
not normalized IDs. Resolution resolves names to IDs downstream.

All relationships must be logged in **Discovery Metadata v5.0**.

------------------------------------------------------------
# 9. MULTI-COUNTY RULE

Discovery must follow the authoritative multi-county rule for all six entity types:

**9.1 No segmentation**
Discovery must **never** segment multi-county entities.

**9.2 Record all counties**
Discovery must record **all counties** in which the entity appears, exactly as discovered.

**9.3 Raw county list**
Discovery Metadata must store the raw county list exactly as discovered, with no
normalization, alphabetization, or formatting.

**9.4 Normalization rule**
Normalization writes the county list as a **semicolon-delimited, alphabetized list**.
This is a Normalization decision, not a Discovery decision.

Applies to all six entity types.

------------------------------------------------------------
# 10. DISCOVERY MODES

Discovery v5.0 operates in two complementary modes:

## 10.1 Enumerative Discovery (siblings)
Performed by **Tier Sub-Procedures v5.0**.

Enumerative discovery must:

- Identify authoritative listing/index pages (e.g., `/parks/`, `/trails/`, `/locations/`)
- Extract **all first-level entity URLs**
- Queue each for entity detection and extraction

This ensures discovery of siblings such as:

- `/parks/englewood`
- `/parks/foreman`
- `/parks/argyll`

## 10.2 Recursive Discovery (children)
Performed by the **Discovery Engine** via URL propagation.

Recursive discovery must:

- Extract internal links from entity pages
- Follow allowed patterns (e.g., `trails`, `maps`, `facilities`, `access`)
- Queue child URLs
- Enforce depth and count limits
- Record `parent_url` for provenance

This ensures discovery of deeper pages such as:

- `/parks/englewood/trails`
- `/parks/englewood/maps`

------------------------------------------------------------
# 11. WHAT DISCOVERY MUST NEVER DO

Discovery must never:

- Normalize names, types, or values
- Infer township or municipality (leave blank — GIS-derived in normalization)
- Assess or infer difficulty or accessibility (only record if explicitly stated)
- Invent GPS coordinates, addresses, or parent relationships
- Deduplicate entities (Resolution's job)
- Choose between conflicting values (Normalization's job)
- Silently correct malformed values
- Apply vocabulary rules to raw values

Violations corrupt the raw layer and undermine the integrity of the entire pipeline.

------------------------------------------------------------
# 12. CONSOLIDATION RULES

In v5.0, **Discovery does not consolidate entities**.

Consolidation is performed exclusively by the **Resolution Engine v5.0**, which:

- Merges identical entities across tiers
- Applies tier precedence
- Applies authority weighting
- Preserves conflicts for Normalization
- Preserves provenance
- Aligns parent/child relationships
- Aligns network membership
- Aligns Access Point parent sets

Discovery produces **raw, unmerged, unnormalized** records only.

------------------------------------------------------------
# 13. METADATA REQUIREMENTS

Discovery must produce a complete **Discovery Metadata Object v5.0** for every
raw record.

Metadata must include:

- Identity metadata (raw)
- Tier metadata
- Source metadata
- Parent URL (if propagated via recursive discovery)
- Conflict indicators (raw)
- Uncertainty indicators (raw)
- Parent entity hints (Access Points)
- Boundary metadata (raw)
- County list (raw)
- Notes

Metadata must conform to:

- **Discovery Metadata Specification v5.0**
- **Audit & Logging Module v5.0**

------------------------------------------------------------
# 14. OUTPUT FORMAT

Discovery must output **Raw Discovery Records v5.0** for all six entities.

All outputs must conform to:

- **Discovery Output Specification v5.0**
- The six Schema Modules v5.0
- The six Vocabulary Modules v5.0

Discovery must not:

- Normalize
- Correct
- Dedupe
- Infer
- Invent
- Silently modify

Discovery may generate TSV previews when explicitly requested. Previews are
for inspection only and are not part of the official pipeline.

------------------------------------------------------------
# 15. INTEGRATION POINTS

This module integrates with:

- All six Schema Modules v5.0
- All six Vocabulary Modules v5.0
- All Discovery Sub-Procedures v5.0 (entity-specific)
- All Tier Sub-Procedures v5.0
- Discovery Metadata Specification v5.0
- Discovery Output Specification v5.0
- **Resolution Engine v5.0**
- **Normalization Engine v5.0**
- **Entity Upsert Engine v5.0**
- **Processing / Orchestration Module v5.0**
- **Audit & Logging Module v5.0**
- **County Baseline Module v5.0**

Retired in v5.0:

- Access Point Association Module (v4.0)
- Child Site Discovery Sub-Procedure (v4.0, merged into Site Discovery Sub-Procedure)

------------------------------------------------------------
# 16. MODULE DEPENDENCIES

This module depends on:

- Discovery Output Specification v5.0
- Discovery Metadata Specification v5.0
- Discovery Orchestration Module v5.0
- All six entity Discovery Sub-Procedures v5.0
- All eight Tier Sub-Procedures v5.0
- Child Site Rules Module v5.0
- Resolution Engine v5.0
- Audit & Logging Module v5.0

------------------------------------------------------------
# END OF DISCOVERY PROTOCOL MODULE v5.0
