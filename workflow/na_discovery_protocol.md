# NATURAL AREAS PROJECT
# DISCOVERY PROTOCOL MODULE v4.0
(Full Multi‑Entity Discovery Framework, Updated to Raw Layer Architecture, Enumerative + Recursive Discovery, Tier‑0 Baseline Integration, Multi‑Table Entity Graph, and Provenance‑Driven Resolution)

Authoritative, versioned protocol for discovering all six entity types in the
statewide Natural Areas & Trails system.

This module defines:

- The unified discovery workflow  
- The six discovery tracks  
- Tier‑based source rules  
- Entity‑specific discovery rules  
- Cross‑entity relationship rules  
- Metadata requirements  
- Raw output requirements  
- Integration points with Resolution, Normalization, and Entity Upsert  
- Provenance and audit requirements  

This module supersedes v3.2.2 and updates the ontology and architecture to the
**Raw → Resolution → Normalization → Entity Graph pipeline**, including:

- Enumerative (sibling) discovery  
- Recursive (child) discovery  
- Tier‑0 Baseline Loader  
- Multi‑table SQLite entity graph  
- Provenance‑rich raw records  
- Deterministic, reproducible discovery runs  
- Explicit separation of discovery vs. resolution vs. normalization  

------------------------------------------------------------
# 1. PURPOSE

Discovery Protocol v4.0 provides the authoritative, deterministic workflow for
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
- Produces **Raw Discovery Records** for all six entities  
- Produces **Discovery Metadata** for all six entities  
- Integrates with Resolution, Normalization, and TSV output  
- Enforces **no normalization, no invention, and no silent correction** during discovery  

This module is authoritative for discovery logic.

------------------------------------------------------------
# 2. SCOPE

Discovery Protocol v4.0 governs:

- All eight discovery tiers (Federal → Private)  
- Tier‑0 Baseline Loader  
- All six entity types  
- All authoritative sources  
- All cross‑entity relationships  
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
- Operator‑provided baseline spreadsheets  

------------------------------------------------------------
# 3. ENTITY TYPES (AUTHORITATIVE)

Discovery must surface candidates for all six identity‑bearing entities:

## 3.1 Site
Identity‑bearing land units (parks, preserves, forests, wildlife areas, etc.),
including internal identity‑bearing units that qualify as **child Sites** under the
**Child Site Rules Module v4.0**.

Child Sites are discovered **exclusively through the Site Discovery Sub‑Procedure v4.0**.

## 3.2 Trail
Identity‑bearing linear corridors.

## 3.3 Trail Segment
Operational portions of Trails that meet the Trail Segment Identity Rule.

## 3.4 Trail Network
Umbrella entities composed of multiple Trails.

## 3.5 Site Network
Umbrella entities composed of multiple Sites.

## 3.6 Access Point
Visitor‑facing navigational entry locations.  
Access Points may have **multiple parent entities** (Sites, Trails, Trail Segments).

------------------------------------------------------------
# 4. DISCOVERY TIERS

Discovery proceeds through the eight authoritative tiers:

1. Federal  
2. State  
3. District‑Level  
4. County  
5. Township  
6. Municipal  
7. Conservancy  
8. Private  
9. **Tier‑0 Baseline** (operator‑provided; runs last)

Each tier must surface candidates for all six entity types when applicable.

------------------------------------------------------------
# 5. REQUIRED SOURCES

Each tier must check:

- Official websites  
- GIS systems  
- Planning documents  
- Stewardship documents  
- Brochures & maps  
- County auditor data  
- Federal/state datasets  
- Partnership announcements  
- County‑hosted pages  
- Municipal/township‑hosted pages  
- Conservancy and land‑trust pages  
- Private organization pages  

All sources must be logged in **Discovery Metadata v4.0**.

------------------------------------------------------------
# 6. ENTITY‑SPECIFIC DISCOVERY RULES

Discovery must use the authoritative sub‑procedure for each entity type:

## 6.1 Site Discovery
Use **Site Discovery Sub‑Procedure v4.0**.  
Must surface:

- Top‑level Sites  
- Child Sites  
- Parent Site relationships  

## 6.2 Trail Discovery
Use **Trail Discovery Sub‑Procedure v4.0**.

## 6.3 Trail Segment Discovery
Use **Trail Segment Discovery Sub‑Procedure v4.0**.

## 6.4 Trail Network Discovery
Use **Trail Network Discovery Sub‑Procedure v4.0**.

## 6.5 Site Network Discovery
Use **Site Network Discovery Sub‑Procedure v4.0**.

## 6.6 Access Point Discovery
Use **Access Point Discovery Sub‑Procedure v4.0**.

------------------------------------------------------------
# 7. CROSS‑ENTITY RELATIONSHIP RULES

Discovery must identify and record:

- Site → child Site  
- Trail → Trail Segment  
- Trail Network → Trail  
- Site Network → Site  
- **Access Point → Parent Entities (multiple allowed)**  

All relationships must be logged in **Discovery Metadata v4.0**.

------------------------------------------------------------
# 8. MULTI‑COUNTY RULE (UNCHANGED)

Discovery must follow the authoritative multi‑county rule:

### ✔ 8.1 No segmentation  
Discovery must **never** segment multi‑county entities.

### ✔ 8.2 Record all counties  
Discovery must record **all counties** in which the entity appears.

### ✔ 8.3 Raw county list  
Discovery Metadata must store the raw county list exactly as discovered.

### ✔ 8.4 Normalization rule  
Normalization writes the county list as a **semicolon‑delimited, alphabetized list**.

Applies to all six entity types.

------------------------------------------------------------
# 9. DISCOVERY MODES (NEW IN v4.0)

Discovery v4.0 operates in two complementary modes:

## 9.1 Enumerative Discovery (siblings)
Performed by **Tier Sub‑Procedures**.

Enumerative discovery must:

- Identify authoritative listing/index pages (e.g., `/parks/`, `/trails/`, `/locations/`)  
- Extract **all first‑level entity URLs**  
- Queue each for entity detection and extraction  

This ensures discovery of siblings such as:

- `/parks/englewood`  
- `/parks/foreman`  
- `/parks/argyll`  

## 9.2 Recursive Discovery (children)
Performed by the **Discovery Engine + URL Propagation Module**.

Recursive discovery must:

- Extract internal links from entity pages  
- Follow allowed patterns (e.g., `trails`, `maps`, `facilities`)  
- Queue child URLs  
- Enforce depth and count limits  
- Record `parent_url` for provenance  

This ensures discovery of deeper pages such as:

- `/parks/englewood/trails`  
- `/parks/englewood/maps`  

------------------------------------------------------------
# 10. CONSOLIDATION RULES (REVISED)

In v4.0, **Discovery does not consolidate entities**.

Consolidation is performed exclusively by the **Resolution Engine v4.0**, which:

- Merges identical entities across tiers  
- Applies tier precedence  
- Applies authority weighting  
- Preserves conflicts  
- Preserves provenance  
- Aligns parent/child relationships  
- Aligns network membership  
- Aligns Access Point parent sets  

Discovery produces **raw, unmerged, unnormalized** records.

------------------------------------------------------------
# 11. METADATA REQUIREMENTS

Discovery must produce a complete **Discovery Metadata Object v4.0** for every raw record.

Metadata must include:

- Identity metadata (raw)  
- Tier metadata  
- Source metadata  
- Parent URL (if propagated)  
- Conflict indicators (raw)  
- Uncertainty indicators (raw)  
- Parent entity hints (Access Points)  
- Boundary metadata (raw)  
- County list (raw)  
- Access level (raw)  
- Notes  

Metadata must conform to:

- **Discovery Metadata Specification v4.0**  
- **Audit & Logging Module v4.0**  

------------------------------------------------------------
# 12. OUTPUT FORMAT

Discovery must output **Raw Discovery Records v4.0** for all six entities.

All outputs must conform to:

- **Discovery Output Specification v4.0**  
- The six Schema Modules v4.0  
- The six Vocabulary Modules v4.0  

Discovery must not:

- Normalize  
- Correct  
- Dedupe  
- Infer  
- Invent  
- Silently modify  

Discovery may generate TSV previews when explicitly requested.

------------------------------------------------------------
# 13. INTEGRATION POINTS

This module integrates with:

- All six Schema Modules v4.0  
- All six Vocabulary Modules v4.0  
- All Discovery Sub‑Procedures v4.0  
- Discovery Metadata Specification v4.0  
- Discovery Output Specification v4.0  
- **Resolution Engine v4.0**  
- **Normalization Engine v4.0**  
- **Entity Upsert Engine v4.0**  
- **Baseline Loader v4.0**  
- **Processing / Orchestration Module v4.0**  

Retired modules:

- Access Point Association Module  
- Child Site Discovery Sub‑Procedure  

------------------------------------------------------------
# 14. VERSIONING

This module is **Discovery Protocol Module v4.0**.  
Sub‑procedures may advance to v4.0+ without requiring a bump to the Protocol version.  
Future updates may produce v4.1, v4.2, etc.

------------------------------------------------------------
# END OF DISCOVERY PROTOCOL MODULE v4.0