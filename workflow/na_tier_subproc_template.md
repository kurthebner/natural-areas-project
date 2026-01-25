# NATURAL AREAS PROJECT
# TIER SUB‑PROCEDURE TEMPLATE v4.0
(Authoritative Template for Enumerative + Recursive Tier Discovery)

This template defines the **required structure, responsibilities, and outputs**
for all Tier Discovery Sub‑Procedures in the Natural Areas Project v4.0
architecture.

Every tier module (Federal, State, District, County, Township, Municipal,
Conservancy, Private) must implement this template exactly, with no additions,
removals, or deviations unless explicitly authorized by the Discovery Protocol
Module v4.0.

This document is **new in v4.0** and supersedes all implicit v3.x tier patterns.

------------------------------------------------------------
# 1. PURPOSE

A Tier Sub‑Procedure is responsible for:

- Identifying authoritative listing/index pages for the tier  
- Performing **enumerative discovery** (sibling enumeration)  
- Extracting all first‑level entity URLs  
- Passing enumerated URLs to the Orchestration Engine  
- Supporting **recursive discovery** via URL propagation  
- Invoking the correct Entity Discovery Sub‑Procedures  
- Producing Raw Discovery Records v4.0  
- Producing Discovery Metadata v4.0  
- Recording tier provenance  
- Recording parent_url provenance for propagated pages  

A Tier Sub‑Procedure does **not**:

- Normalize  
- Consolidate  
- Resolve identity  
- Invent values  
- Infer missing metadata  
- Modify raw values  

------------------------------------------------------------
# 2. REQUIRED INPUTS

Each Tier Sub‑Procedure receives:

- `county_context`  
- `tier_id` (1–8)  
- `tier_name`  
- `tier_entry_points` (one or more authoritative URLs)  
- `orchestration_context` (execution state, recursion limits, domain rules)  

The sub‑procedure must not fetch or infer additional entry points.

------------------------------------------------------------
# 3. REQUIRED OUTPUTS

Each Tier Sub‑Procedure must return:

### 3.1 Enumerated Entity URLs
A complete list of all first‑level entity URLs discovered from authoritative
listing/index pages.

### 3.2 Raw Discovery Records v4.0
One raw record per entity occurrence, containing:

- `source_tier`  
- `source_system`  
- `source_url`  
- `parent_url` (if propagated)  
- `raw_payload` (JSON)  
- `entity_type_guess`  
- `harvested_at`  
- `discovery_run_id`  
- `errors` (optional)  

### 3.3 Discovery Metadata v4.0
Metadata must include:

- tier metadata  
- source metadata  
- conflict indicators  
- uncertainty indicators  
- parent_url provenance  
- boundary flags  
- raw county list  
- notes  

------------------------------------------------------------
# 4. ENUMERATIVE DISCOVERY REQUIREMENTS (MANDATORY)

Each Tier Sub‑Procedure must:

1. Identify authoritative listing/index pages  
   Examples:  
   - `/parks/`  
   - `/trails/`  
   - `/properties/`  
   - `/locations/`  

2. Fetch each listing page  

3. Extract **all first‑level entity URLs**  
   These are the “siblings” at the same level as:  
   - `/parks/englewood`  
   - `/parks/foreman`  
   - `/parks/argyll`  

4. Normalize URLs only structurally (never semantically)  
   - resolve relative paths  
   - remove fragments  
   - preserve query parameters  

5. Return the full enumerated URL list to the Orchestration Engine  

Enumerative discovery is **required** for complete tier coverage.

------------------------------------------------------------
# 5. RECURSIVE DISCOVERY SUPPORT (MANDATORY)

Tier Sub‑Procedures must support recursive discovery by:

- Extracting internal links from entity pages  
- Filtering links using the Orchestration Engine’s allowlist  
- Respecting recursion depth limits  
- Respecting per‑domain and per‑entity page limits  
- Returning child URLs with `parent_url` provenance  

Allowed patterns typically include:

- `trails`  
- `maps`  
- `facilities`  
- `access`  
- `gis`  

Recursive discovery is **depth‑oriented**, not breadth‑oriented.

------------------------------------------------------------
# 6. ENTITY DETECTION & SUB‑PROCEDURE INVOCATION

For each enumerated or propagated URL:

1. Fetch the page  
2. Run Entity Detector v4.0  
3. Invoke the correct Entity Discovery Sub‑Procedure v4.0  
4. Receive raw payload + metadata  
5. Attach tier metadata  
6. Attach parent_url (if propagated)  
7. Return raw record + metadata to Orchestration  

Entity types:

- Site  
- Trail  
- Trail Segment  
- Trail Network  
- Site Network  
- Access Point  

Child Sites are surfaced exclusively through the Site Discovery Sub‑Procedure v4.0.

------------------------------------------------------------
# 7. ERROR HANDLING

Tier Sub‑Procedures must:

- Log all errors  
- Preserve partial results  
- Never invent missing values  
- Never silently correct malformed values  
- Mark uncertainties in metadata  
- Continue unless the entire tier is inaccessible  

------------------------------------------------------------
# 8. PROVENANCE REQUIREMENTS

Each raw record must include:

- `source_tier`  
- `source_system`  
- `source_url`  
- `parent_url` (if propagated)  
- `harvested_at`  
- `discovery_run_id`  

Tier Sub‑Procedures must not modify provenance fields.

------------------------------------------------------------
# 9. INTEGRATION WITH ORCHESTRATION

Tier Sub‑Procedures must:

- Return enumerated URLs immediately  
- Accept recursive URLs from Orchestration  
- Return raw records incrementally  
- Respect Orchestration’s recursion limits  
- Respect Orchestration’s domain rules  
- Respect Orchestration’s skip logic  

Tier Sub‑Procedures do **not**:

- Decide which tiers run  
- Decide recursion depth  
- Decide domain allowlists  
- Perform consolidation  
- Perform normalization  

------------------------------------------------------------
# 10. VERSIONING

This document is **Tier Sub‑Procedure Template v4.0**.  
All tier modules must declare:
tier_subprocedure_version: 4.0

Future updates may produce v4.1, v4.2, etc.

------------------------------------------------------------
# END OF TIER SUB‑PROCEDURE TEMPLATE v4.0