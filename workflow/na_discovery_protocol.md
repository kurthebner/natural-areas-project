# NATURAL AREAS PROJECT
# DISCOVERY PROTOCOL MODULE v3.2.2
(Full Multi‑Entity Discovery Framework, Updated to Child Site Ontology, Multi‑County Rule, and Multi‑Parent Access Points)

Authoritative, versioned protocol for discovering all six entity types in the
statewide Natural Areas & Trails system.

This module defines:

- The unified discovery workflow  
- The six discovery tracks  
- Tier‑based source rules  
- Entity‑specific discovery rules  
- Cross‑entity relationship rules  
- Metadata requirements  
- Output requirements  
- Integration points  

This module supersedes v3.1 and updates the ontology to represent internal units
as **child Sites** (Sites with Parent Site) governed by the **Child Site Rules Module v3.2.2**.

------------------------------------------------------------
# 1. PURPOSE

Discovery Protocol v3.2.2 provides the authoritative, deterministic workflow for
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
- Produces Raw Candidate Records for all six entities  
- Produces Discovery Metadata for all six entities  
- Integrates with normalization, resolution, and TSV output  
- Enforces no normalization, no invention, and no silent correction during discovery  

This module is authoritative for discovery logic.

------------------------------------------------------------
# 2. SCOPE

Discovery Protocol v3.2.2 governs:

- All eight discovery tiers (Federal → Private)  
- All six entity types  
- All authoritative sources  
- All cross‑entity relationships  
- All discovery metadata  
- All logical consolidation rules  

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

Discovery must surface candidates for all six identity‑bearing entities:

## 3.1 Site

Identity‑bearing land units (parks, preserves, forests, wildlife areas, etc.),
including internal identity‑bearing units that qualify as **child Sites** under the
**Child Site Rules Module v3.2.2**.

Child Sites are discovered **exclusively through the Site Discovery Sub‑Procedure v3.2.2**.
No standalone child‑site discovery track exists in v3.2.2.

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

------------------------------------------------------------
# 4. DISCOVERY TIERS

Discovery proceeds through the eight authoritative tiers:

1. Federal   
2. State   
3. District-Level 
4. County  
5. Township  
6. Municipal 
7. Conservancy 
8. Private

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

All sources must be logged in Discovery Metadata.

------------------------------------------------------------
# 6. ENTITY‑SPECIFIC DISCOVERY RULES

Discovery must use the authoritative sub‑procedure for each entity type:

## 6.1 Site Discovery

Use **Site Discovery Sub‑Procedure v3.2.2**.  
Must surface:

- Top‑level Sites  
- Child Sites (internal identity‑bearing units)  
- Parent Site relationships for child Sites, following the **Child Site Rules Module v3.2.2**  

**Note:**  
Child Sites are discovered *only* through the Site Discovery Sub‑Procedure.  
The former Child Site Discovery Sub‑Procedure has been retired.

## 6.2 Trail Discovery
Use **Trail Discovery Sub‑Procedure v3.2.2**.

## 6.3 Trail Segment Discovery
Use **Trail Segment Discovery Sub‑Procedure v3.2.2**.

## 6.4 Trail Network Discovery
Use **Trail Network Discovery Sub‑Procedure v3.2.2**.

## 6.5 Site Network Discovery
Use **Site Network Discovery Sub‑Procedure v3.2.2**.  
A Site Network must be an umbrella entity composed of multiple Sites.

## 6.6 Access Point Discovery
Use **Access Point Discovery Sub‑Procedure v3.2.2**.

------------------------------------------------------------
# 7. CROSS‑ENTITY RELATIONSHIP RULES

Discovery must identify and record:

- Site → child Site relationships (Sites with Parent Site)  
- Trail → Trail Segment relationships  
- Trail Network → Trail relationships  
- Site Network → Site relationships  
- **Access Point → Parent Entity relationships (Sites, Trails, Trail Segments; multiple allowed)**  

All relationships must be logged in **Discovery Metadata v3.2.2**.

------------------------------------------------------------
# 8. MULTI‑COUNTY RULE (UPDATED)

Discovery must follow the authoritative multi‑county rule:

### ✔ 8.1 No segmentation  
Discovery must **never** segment multi‑county entities into multiple records.

### ✔ 8.2 Record all counties  
Discovery must record **all counties** in which the entity appears.

### ✔ 8.3 Raw county list  
Discovery Metadata must store the raw county list exactly as discovered.

### ✔ 8.4 Normalization rule  
Normalization writes the county list as a **semicolon‑delimited, alphabetized list**.

### Applies to:
- Sites  
- Child Sites  
- Trails  
- Trail Segments  
- Trail Networks  
- Site Networks  
- Access Points  

------------------------------------------------------------
# 9. CONSOLIDATION RULES (LOGICAL)

After all tiers produce raw candidates, Discovery must support consolidation
according to these logical rules (execution is defined in the Orchestration Module v3.2.2):

## 9.1 Sites
Merge identical Sites across tiers, including child Sites.  
Preserve Parent Site relationships for child Sites.

## 9.2 Trails
Merge identical Trails across tiers.

## 9.3 Trail Segments
Merge identical segments and align with parent Trails.

## 9.4 Trail Networks
Merge identical networks and align with member Trails.

## 9.5 Site Networks
Merge identical networks and align with member Sites.

## 9.6 Access Points
Merge identical Access Points and assign identity parents  
(Sites, Trails, and/or Trail Segments).

Rules:

- No normalization during consolidation  
- No invention of missing values  
- All conflicts must be preserved in metadata  

------------------------------------------------------------
# 10. METADATA REQUIREMENTS

Discovery must produce a complete **Discovery Metadata Object v3.2.2** for every entity.

Metadata must include:

- Identity metadata  
- Tier metadata  
- Source metadata  
- Conflict metadata  
- Uncertainty metadata  
- **Parent metadata (Access Points only; Sites, Trails, Trail Segments)**  
- Boundary metadata  
- **County list (raw)**  
- **Access level (raw)** when applicable  
- Notes  

Metadata must conform to:

- **Discovery Metadata Specification v3.2.2**  
- **Audit & Logging Module v3.2.2**  

------------------------------------------------------------
# 11. OUTPUT FORMAT

Discovery must output **Raw Candidate Records v3.2.2** for all six entities:

- Site  
- Trail  
- Trail Segment  
- Trail Network  
- Site Network  
- Access Point  

All outputs must conform to:

- **Discovery Output Specification v3.2.2**  
- The six Schema Modules v3.2.2  
- The six Vocabulary Modules v3.2.2  

No normalization, no invention, and no silent correction is permitted.

Discovery may generate TSV previews of intermediate states when explicitly requested by the operator.  
These previews do not replace Raw Candidate Records and are not used by downstream modules.

------------------------------------------------------------
# 12. INTEGRATION POINTS

This module integrates with:

- All six Schema Modules v3.2.2  
- All six Vocabulary Modules v3.2.2  
- All Discovery Sub‑Procedures v3.2.2  
- Discovery Metadata Specification v3.2.2  
- Discovery Output Specification v3.2.2  
- **Normalization Contracts v3.2.2**  
- **TSV Output Specifications v3.2.2**  
- Resolution Module v3.2.2  
- County Baseline Module v3.2.2  
- Processing / Orchestration Module v3.2.2  

**Note:**  
The Access Point Association Module has been retired and must not be referenced.  
The Child Site Discovery Sub‑Procedure has been retired; child Sites are discovered exclusively through the Site Discovery Sub‑Procedure.

------------------------------------------------------------
# 13. VERSIONING

This module is **Discovery Protocol Module v3.2.2**.  
Sub‑procedures may advance to v3.2.2+ without requiring a bump to the Protocol version.  
Future updates may produce v3.3, v3.4, etc.

------------------------------------------------------------
# END OF DISCOVERY PROTOCOL MODULE v3.2.2