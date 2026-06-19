# NATURAL AREAS PROJECT
# PROCESSING ORCHESTRATION MODULE v5.5
Authoritative End‑to‑End Execution Pipeline for the v5.x Architecture

# CHANGES FROM v5.4 (IMP-093, 2026-05-04)
# - GPS Gate moved from Stage 4 to Stage 5.5 (after Resolution Pass 2, not before)
# - GPS Acquisition split into Stage 4a (fill-forward) and Stage 4b (acquisition)
# - Human Review Gate added as Stage 8.5 (between TSV Integrity Check and Upsert)
# - Pipeline Summary updated to match
# - Stage label cross-reference to na-pipeline skill added

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

**Entry condition:** All 8 discovery tiers are complete. The staging YAML
(`{county}_{state}_raw_discovery.yaml`) is finalized and the handoff document
is set to `DISCOVERY COMPLETE — PIPELINE READY`. If discovery is not yet
complete, return to the `na-discovery` skill.

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
# STAGE 4a — GPS FILL-FORWARD (IMP-031)
# na-pipeline skill label: Stage 2a

Before running GPS acquisition, check the DB for each entity being processed.
If the DB record already has non-blank `gps_lat` and `gps_lon` from a prior
pipeline run, carry those values forward without re-acquisition.

Precedence: YAML GPS > DB GPS (fill-forward when YAML is blank) > blank → Stage 4b.

Preserved fields: `gps_lat`, `gps_lon`, `plus_code`, `township`, `municipality`.

**Output:** Entities with GPS carried forward from prior runs where applicable.

------------------------------------------------------------
# STAGE 4b — GPS ACQUISITION MODULE v5.x
# na-pipeline skill label: Stage 2b

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
# na-pipeline skill label: Stage 1b
# Runs AFTER Stage 4b (GPS Acquisition), BEFORE Stage 5.5 (GPS Gate)

Resolution Pass 2 re‑evaluates Access Points using GPS data acquired in Stage 4b:

- GPS anchors  
- GPS proximity buckets  
- Parent context  

This produces fully resolved Access Points with GPS-informed identity decisions.

**Output:** Fully resolved entity layer v5.x.

------------------------------------------------------------
# STAGE 5.5 — GPS GATE (IMP-069)
# na-pipeline skill label: Stage 2c
# Runs AFTER Stage 5 (Resolution Pass 2), BEFORE Stage 6 (Normalization)

After Resolution Pass 2, any Site or Access Point that still lacks GPS coordinates
and does not carry `gps_unresolvable=true` is routed to `held_entities` with
`hold_reason = gps_missing`. It does not proceed to Stage 6 or beyond.

**Rationale for position:** Resolution Pass 2 (Stage 5) uses GPS to resolve AP
identity. The GPS Gate runs after Pass 2 so that APs can benefit from GPS-informed
resolution before being evaluated for the gate. Placing the gate before Pass 2
(the v5.4 error) would have incorrectly gated APs whose GPS was valid but whose
identity had not yet been finalized.

**Output:** GPS-null entities without `gps_unresolvable` flag written to
`held_entities`; all remaining entities proceed to normalization.

------------------------------------------------------------
# STAGE 6 — NORMALIZATION ENGINE v5.x

Normalization performs:

- Schema validation  
- Vocabulary normalization  
- Formatting normalization  
- GPS validation → numeric `gps_lat`, `gps_lon`  
- Plus Code computation  
- GIS spatial lookup → township, municipality  
- Integrity anchor validation and dedup check  
- Parent/child validation (Child Site Rules v5.x)  

Normalization does **not** merge conflicts or infer identity.

**Output:** Six normalized datasets.

------------------------------------------------------------
# STAGE 7 — GENERATE TSV OUTPUT (v5.x)

Generate six TSV files from normalized entities **before** database upsert:

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
# STAGE 7.5 — VOCABULARY VALIDATION GATE (v5.x)

Validate all vocabulary-governed fields in each TSV against the authoritative
Vocabulary Modules v5.x. **Halts the pipeline on any violation** — no upsert
may proceed until all TSVs pass.

Validates:
- Every `category` value against §2.1 (18 values)
- Every `subtype` value against the category-dependent list in §3
- Every `designation` value against §4
- Every `status` value against §5
- Every `features` value against §6
- Trail `use_type`, `surface_type`, `origin_type`, `difficulty`
- Access Point `type`

**Output:** Vocabulary-validated TSVs, or pipeline halt with violation report.

------------------------------------------------------------
# STAGE 8 — TSV INTEGRITY CHECK (v5.x)

Validate:

- Delimiter count  
- Field alignment  
- Blank‑field representation  
- County formatting  

If integrity fails, halt finalization.

**Output:** Integrity‑validated TSVs.

------------------------------------------------------------
# STAGE 8.5 — HUMAN REVIEW GATE
# na-pipeline skill label: Stage 5.5

**The pipeline halts here. Do not proceed to Stage 9 until a human has reviewed
the TSV files and confirmed.**

The reviewer opens the six TSV files and verifies:

- Entity counts look reasonable for this county (no unexpected zeros or inflated counts)
- Category and subtype assignments are substantively correct — not just vocabulary-valid
- Any GPS coordinates that were newly acquired look plausible (spot-check against a map)
- Held entities are expected — no surprises in what was held or why

To confirm review and proceed, the user must explicitly confirm (e.g., "TSV looks
good, proceed with upsert"). Silence, a skill re-run, or any automated signal is
not confirmation.

Record the reviewer and confirmation statement in the session log before Stage 9.

**Output:** Human-confirmed TSV bundle, ready for upsert.

------------------------------------------------------------
# STAGE 9 — ENTITY UPSERT ENGINE v5.x

Upsert after TSV validation is confirmed:

- Inserts or updates entities in the entity graph  
- Maintains stable IDs  
- Writes relationship tables  
- Writes provenance tables  
- Processes held entity release workflow  

**Output:** Updated entity graph.

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

| This Module (v5.5) | na-pipeline Skill Label | Description |
|---|---|---|
| Stage 0 | (prereq check) | Module availability check |
| Stage 1 | (prereq) | Discovery — tiers 1–8 |
| Stage 2 | (prereq) | Load county baseline |
| Stage 3 | Stage 1a | Resolution Pass 1 |
| Stage 4a | Stage 2a | GPS fill-forward from DB |
| Stage 4b | Stage 2b | GPS acquisition |
| Stage 5.5a | Stage 2c | **GPS Gate — Sites only** (before Pass 2) |
| Stage 5 | Stage 1b | Resolution Pass 2 — APs only |
| Stage 5.5b | Stage 2d | **GPS Gate — APs only** (after Pass 2) |
| Stage 6 | Stage 3 | Normalization Engine |
| Stage 7 | Stage 4 | TSV Output |
| Stage 7.5 | Stage 4.5 | Vocabulary Validation Gate |
| Stage 8 | Stage 5 | TSV Integrity Check |
| Stage 8.5 | Stage 5.5 | Human Review Gate ← pipeline halts |
| Stage 9 | Stage 6 | Database Upsert |
| Stage 10 | — | Relationship Validation |
| Stage 11 | — | Final Output Bundle |

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
# END OF PROCESSING ORCHESTRATION MODULE v5.5