# NATURAL AREAS PROJECT
# DISCOVERY PROTOCOL MODULE v3.1
(Full Multi‑Entity Discovery Framework, Updated to Site Network Ontology)

Authoritative, versioned protocol for discovering all seven entity types in the
statewide Natural Areas & Trails system.

This module defines:
- The unified discovery workflow
- The seven discovery tracks
- Tier‑based source rules
- Entity‑specific discovery rules
- Cross‑entity consolidation
- Metadata requirements
- Output requirements
- Integration points

This module supersedes v3.0 and updates the ontology to use **Site Network** instead
of Area Network.

------------------------------------------------------------
# 1. PURPOSE

Discovery Protocol v3.1 provides the authoritative, deterministic workflow for
discovering:

1. Site
2. Sub‑Site
3. Trail
4. Trail Segment
5. Trail Network
6. Site Network
7. Access Point

This protocol:
- Defines the unified discovery architecture
- Ensures consistency across all counties and data sources
- Prevents misclassification between entity types
- Produces Raw Candidate Records for all seven entities
- Produces Discovery Metadata for all seven entities
- Integrates with normalization, resolution, and TSV output
- Enforces no normalization, no invention, and no silent correction during discovery

This module is authoritative for discovery logic.

------------------------------------------------------------
# 2. SCOPE

Discovery Protocol v3.1 governs:
- All eight discovery tiers (Federal → Private)
- All seven entity types
- All authoritative sources
- All cross‑entity relationships
- All discovery metadata
- All consolidation workflows

This protocol applies to:
- Federal agencies
- State agencies
- Park districts
- Counties
- Townships
- Municipalities
- Land trusts & conservancies
- Private organizations

------------------------------------------------------------
# 3. ENTITY TYPES (AUTHORITATIVE)

Discovery must surface candidates for all seven identity‑bearing entities:

## 3.1 Site
Identity‑bearing land units (parks, preserves, forests, wildlife areas, etc.)

## 3.2 Sub‑Site
Identity‑bearing internal units within a Site.

## 3.3 Trail
Identity‑bearing linear corridors.

## 3.4 Trail Segment
Operational portions of Trails.

## 3.5 Trail Network
Umbrella entities composed of multiple Trails.

## 3.6 Site Network
Umbrella entities composed of multiple Sites.

## 3.7 Access Point
Visitor‑facing navigational entry locations.

------------------------------------------------------------
# 4. DISCOVERY TIERS (UNCHANGED)

Discovery proceeds through the eight authoritative tiers:

1. Federal  
2. State  
3. Park District  
4. County  
5. Township  
6. Municipal  
7. Land Trust & Conservancy  
8. Private & Organization‑Based  

Each tier must surface candidates for all seven entity types when applicable.

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

All sources must be logged in Discovery Metadata.

------------------------------------------------------------
# 6. ENTITY‑SPECIFIC DISCOVERY RULES

Discovery must use the authoritative sub‑procedure for each entity type:

## 6.1 Site Discovery  
Use **Site Discovery Sub‑Procedure v3.1**.

## 6.2 Sub‑Site Discovery  
Use **Sub‑Site Discovery Sub‑Procedure v3.1**.

## 6.3 Trail Discovery  
Use **Trail Discovery Sub‑Procedure v3.1**.

## 6.4 Trail Segment Discovery  
Use **Trail Segment Discovery Sub‑Procedure v3.1**.

## 6.5 Trail Network Discovery  
Use **Trail Network Discovery Sub‑Procedure v3.1**.

## 6.6 Site Network Discovery  
Use **Site Network Discovery Sub‑Procedure v3.1**.  
A Site Network must be an umbrella entity composed of multiple Sites.

## 6.7 Access Point Discovery  
Use **Access Point Discovery Sub‑Procedure v3.1**.

------------------------------------------------------------
# 7. CROSS‑ENTITY RELATIONSHIP RULES

Discovery must identify and record:
- Site → Sub‑Site relationships
- Trail → Trail Segment relationships
- Trail Network → Trail relationships
- Site Network → Site relationships
- Access Point → Parent Entity relationships (multiple allowed)

All relationships must be logged in Discovery Metadata v3.1.

------------------------------------------------------------
# 8. CONSOLIDATION WORKFLOW

After all tiers produce raw candidates:

## 8.1 Consolidate Sites  
Merge identical Sites across tiers.

## 8.2 Consolidate Sub‑Sites  
Merge identical Sub‑Sites within parent Sites.

## 8.3 Consolidate Trails  
Merge identical Trails across tiers.

## 8.4 Consolidate Trail Segments  
Merge identical segments and align with parent Trails.

## 8.5 Consolidate Trail Networks  
Merge identical networks and align with member Trails.

## 8.6 Consolidate Site Networks  
Merge identical networks and align with member Sites.

## 8.7 Consolidate Access Points  
Merge identical APs and assign identity parents.

Rules:
- No normalization during consolidation
- No invention of missing values
- All conflicts must be preserved in metadata

------------------------------------------------------------
# 9. METADATA REQUIREMENTS

Discovery must produce a complete **Discovery Metadata Object v3.1** for every entity.

Metadata must include:
- Identity metadata
- Tier metadata
- Source metadata
- Conflict metadata
- Uncertainty metadata
- Parent metadata (AP only)
- Boundary metadata
- Baseline metadata
- Notes

Metadata must conform to:
- **Discovery Metadata Specification v3.1**
- **Audit & Logging Module v1.1**

------------------------------------------------------------
# 10. OUTPUT FORMAT

Discovery must output **Raw Candidate Records v3.1** for all seven entities:

- Site  
- Sub‑Site  
- Trail  
- Trail Segment  
- Trail Network  
- Site Network  
- Access Point  

All outputs must conform to:
- **Discovery Output Specification v3.1**
- The seven Schema Modules v3.1
- The seven Vocabulary Modules v3.1

No normalization, no invention, and no silent correction is permitted.

------------------------------------------------------------
# 11. INTEGRATION POINTS

This module integrates with:
- All seven Schema Modules v3.1
- All seven Vocabulary Modules v3.1
- All eight Discovery Sub‑Procedures v3.1
- Access Point Discovery Sub‑Procedure v3.1
- Discovery Metadata Specification v3.1
- Discovery Output Specification v3.1
- Access Point Association Module v3.1
- Normalization Contracts v3.1
- TSV Output Specifications v3.1
- Resolution Module v1
- County Baseline Module v1.1
- Orchestration Module v3.1

------------------------------------------------------------
# 12. VERSIONING

This module is **Discovery Protocol Module v3.1**.  
Future updates may produce v3.2, v3.3, etc.

------------------------------------------------------------
# END OF DISCOVERY PROTOCOL MODULE v3.1