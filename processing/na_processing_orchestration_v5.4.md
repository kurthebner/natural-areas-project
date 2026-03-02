# NATURAL AREAS PROJECT
# PROCESSING ORCHESTRATION MODULE v5.4
Authoritative End‑to‑End Execution Pipeline for the v5.x Architecture

------------------------------------------------------------
# 1. PURPOSE

The Processing Orchestration Module v5.4 defines the authoritative, deterministic,
multi‑stage pipeline that transforms raw discovery outputs into fully resolved,
normalized, GIS‑enhanced, audit‑ready datasets for all six entity types:

- Site
- Trail
- Trail Segment
- Trail Network
- Site Network
- Access Point

This module governs:

- The order of execution for all v5.x modules
- How raw discovery values flow through resolution, GPS acquisition, normalization, and upsert
- How conflicts, lineage, and metadata are preserved
- How deterministic, reproducible processing is enforced
- How final TSV outputs are validated and packaged

This module contains **no vocabularies** and **no schema**. It orchestrates modules that do.

------------------------------------------------------------
# 2. CORE PRINCIPLES

### 2.1 Discovery = Collection  
Discovery collects raw values only. No normalization, inference, GPS validation, or GIS derivation occurs.

### 2.2 Resolution = Identity  
Resolution applies identity anchors and signatures, forms merge clusters, preserves conflicts, and resolves parent names to IDs. It does not normalize or infer.

### 2.3 GPS Acquisition = Coordinate Collection  
GPS Acquisition obtains missing GPS coordinates for Sites and Access Points and records provenance. It does not validate or normalize GPS.

### 2.4 Normalization = Decisions  
Normalization validates GPS, computes Plus Codes, performs GIS lookup, applies vocabularies, validates parent/child relationships, and produces normalized entities.

### 2.5 Upsert = Persistence  
Upsert writes normalized entities into the entity graph.

------------------------------------------------------------
# 3. MODULE HIERARCHY AND AUTHORITY

The following hierarchy governs all v5.x processing:

1. Schema Modules v5.x  
2. Vocabulary Modules v5.x  
3. Discovery Protocol Module v5.x  
4. Discovery Orchestration Module v5.x  
5. Discovery Output Specification v5.x  
6. Metadata Specification v5.x  
7. Resolution Rules Module v5.x  
8. Resolution Engine v5.x  
9. GPS Acquisition Module v5.x  
10. Normalization Engine v5.x  
11. Child Site Rules Module v5.x  
12. Entity Upsert Engine v5.x  
13. TSV Output Specifications v5.x  
14. TSV Integrity Check Module v5.x  
15. Audit & Logging Module v5.x  

Authority rules:

- Schema defines ontology and normalized field definitions  
- Discovery collects raw values  
- Resolution determines identity and merges raw values  
- GPS Acquisition collects missing coordinates  
- Normalization applies vocabularies, GIS, formatting, and validation  
- Upsert writes entities into the graph  
- TSV Output serializes normalized entities  
- TSV Integrity Check overrides TSV Output on format issues  
- Audit & Logging records all actions  

------------------------------------------------------------
# 4. END‑TO‑END PIPELINE (v5.x)

The v5.x pipeline consists of **eleven deterministic stages**.

------------------------------------------------------------
# STAGE 0 — MODULE AVAILABILITY CHECK

Verify all required v5.x modules are available.  
If any module is missing, halt processing.

**Output:** Verified v5.x module environment.

------------------------------------------------------------
# STAGE 1 — RUN DISCOVERY (TIERS 1–8)

Discovery collects raw values only.

Rules:

- No normalization  
- No inference  
- No GPS validation  
- No GIS lookup  
- No parent assignment  
- All values stored as `_raw`  
- Township and municipality must remain blank  

**Output:** Raw Discovery Layer v5.x.

------------------------------------------------------------
# STAGE 2 — LOAD COUNTY BASELINE (TIER‑0)

Baseline loads after discovery.

Rules:

- Load baseline rows exactly as written  
- Mark `seeded_from_baseline = true`  
- Preserve all raw values  
- Do not populate township/municipality  

**Output:** Baseline seed layer.

------------------------------------------------------------
# STAGE 3 — RESOLUTION ENGINE v5.x (PASS 1)

Resolution Pass 1 performs:

- Grouping  
- Identity anchor evaluation  
- Similarity scoring  
- Merge cluster formation  
- Conflict preservation  
- Parent name → ID resolution  
- Lineage preservation  

**GPS is not required in Pass 1.**

**Output:** Partially resolved entities (APs may still lack GPS).

------------------------------------------------------------
# STAGE 4 — GPS ACQUISITION MODULE v5.x

GPS Acquisition obtains missing coordinates for:

- Access Points (required)  
- Sites (recommended)  

Rules:

- Acquire GPS from authoritative sources  
- Verify plausibility (county, parent context)  
- Record GPS provenance  
- Do not normalize or validate GPS  
- Do not compute Plus Codes  
- Do not perform GIS lookup  

**Output:** Entities with updated `gps_lat_raw` / `gps_lon_raw`.

------------------------------------------------------------
# STAGE 5 — RESOLUTION ENGINE v5.x (PASS 2 — ACCESS POINTS ONLY)

Resolution Pass 2 re‑evaluates Access Points using:

- GPS anchors  
- GPS proximity buckets  
- Parent context  

This produces fully resolved Access Points.

**Output:** Fully resolved entity layer v5.x.

------------------------------------------------------------
# STAGE 6 — NORMALIZATION ENGINE v5.x

Normalization performs:

- Schema validation  
- Vocabulary normalization  
- Formatting normalization  
- GPS validation → numeric `gps_lat`, `gps_lon`  
- Plus Code computation  
- GIS spatial lookup → township, municipality  
- Derived label computation  
- Integrity anchor validation and dedup check  
- Parent/child validation (Child Site Rules v5.x)  

Normalization does **not** merge conflicts or infer identity.

**Output:** Six normalized datasets.

------------------------------------------------------------
# STAGE 7 — ENTITY UPSERT ENGINE v5.x

Upsert:

- Inserts or updates entities in the entity graph  
- Maintains stable IDs  
- Writes relationship tables  
- Writes provenance tables  

**Output:** Updated entity graph.

------------------------------------------------------------
# STAGE 8 — GENERATE TSV OUTPUT (v5.x)

Generate six TSV files:

- Sites.tsv  
- Trails.tsv  
- Trail_Segments.tsv  
- Access_Points.tsv  
- Trail_Networks.tsv  
- Site_Networks.tsv  

Rules:

- Tab‑delimited  
- UTF‑8  
- No embedded tabs or newlines  
- Arrays → semicolon‑delimited  

**Output:** TSV dataset bundle.

------------------------------------------------------------
# STAGE 9 — TSV INTEGRITY CHECK (v5.x)

Validate:

- Delimiter count  
- Field alignment  
- Blank‑field representation  
- Derived label placement  
- County formatting  

If integrity fails, halt finalization.

**Output:** Integrity‑validated TSVs.

------------------------------------------------------------
# STAGE 10 — RELATIONSHIP VALIDATION (CROSS‑ENTITY)

Validate:

- Site → Parent Site  
- Trail → Segment  
- Trail → Network  
- Site → Site Network  
- Access Point → Site/Trail/Segment  

**Output:** Relationship‑validated dataset.

------------------------------------------------------------
# STAGE 11 — FINAL OUTPUT BUNDLE

Package:

- Six TSVs  
- Audit logs  
- Metadata (module versions, timestamps)  
- Discovery summary  

**Output:** County Output Bundle v5.4.

------------------------------------------------------------
# 5. PIPELINE SUMMARY

1. Module check  
2. Discovery  
3. Baseline  
4. Resolution Pass 1  
5. GPS Acquisition  
6. Resolution Pass 2 (APs)  
7. Normalization  
8. Upsert  
9. TSV Output  
10. TSV Integrity Check  
11. Relationship Validation  
12. Final Bundle  

------------------------------------------------------------
# 6. MODULE DEPENDENCIES

This module depends on:

- Schema Modules v5.x  
- Vocabulary Modules v5.x  
- Discovery Protocol Module v5.x  
- Discovery Orchestration Module v5.x  
- Discovery Output Specification v5.x  
- Metadata Specification v5.x  
- Resolution Rules Module v5.x  
- Resolution Engine v5.x  
- GPS Acquisition Module v5.x  
- Normalization Engine v5.x  
- Child Site Rules Module v5.x  
- Entity Upsert Engine v5.x  
- TSV Output Specifications v5.x  
- TSV Integrity Check Module v5.x  
- Audit & Logging Module v5.x  

------------------------------------------------------------
# END OF PROCESSING ORCHESTRATION MODULE v5.4