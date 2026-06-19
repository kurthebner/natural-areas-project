# NATURAL AREAS PROJECT
# DISCOVERY ORCHESTRATION MODULE v6.0
Execution Engine for Tiered, Multi-Entity, Enumerative and Recursive Discovery

This module defines the runtime execution workflow for the Natural Areas Project
v6.x discovery phase. It coordinates all eight discovery tiers, Tier-0 baseline
seeds, all four entity types, all sub-procedures, and all session artifact
requirements.

This module does not define discovery rules.
It executes them within the v6.x Raw → Resolution → Normalization → Entity
Graph pipeline.

------------------------------------------------------------
# CHANGES FROM v5.3 → v6.0

- **Entity type references updated throughout**: Trail, Trail Segment, and Trail
  Network are unified into the single Trailthing entity type. The four v6.x
  entity types are: Sites, Trailthings, Site Networks, Access Points. All
  sub-procedure invocations and entity track execution order updated accordingly.

- **Document Collection System added** (§4, §5): Discovery now includes a
  mandatory document collection discipline alongside entity record staging.
  Maps, brochures, trail guides, PDFs, GPX/KML files, and other spatial or
  descriptive documents encountered during discovery must be downloaded and
  logged. A `source_documents/` folder and `{county}_document_log.yaml` are
  required session artifacts. This formalizes and preserves source material
  that entity `urls_raw` fields reference by URL alone.

- **Session artifact list updated** (§3): `source_documents/` folder and
  document log added as required artifacts. Filename convention defined.

- **Sub-procedure list updated** (§9): Four v6.0 entity sub-procedures replace
  six v5.x sub-procedures.

------------------------------------------------------------
# 1. PURPOSE

Discovery Orchestration Module v6.0 provides the authoritative execution engine
for:

- Running all eight discovery tiers (plus Tier-0) in the correct order
- Executing all four entity-specific discovery tracks
- Performing enumerative discovery (sibling enumeration)
- Performing recursive discovery (child URL propagation)
- Collecting and filing source documents encountered during discovery
- Managing state across tiers and counties
- Enforcing the Discovery Protocol v6.x
- Producing Raw Discovery Records v6.x
- Producing the county Document Log
- Passing raw outputs to the Resolution Engine v6.x
- Supporting deterministic, reproducible discovery runs

This module ensures that discovery is deterministic, auditable, reproducible,
and complete — including the research asset record produced by document collection.

------------------------------------------------------------
# 2. SCOPE

This module governs:

- Execution order of all discovery tiers
- Execution of all entity-specific sub-procedures
- Enumerative discovery
- Recursive discovery
- Document collection and logging
- State management across tiers
- Metadata enforcement
- Raw output assembly
- Tier-0 baseline integration
- Error handling and fallback logic

This module applies to:

- All counties
- All four entity types (Sites, Trailthings, Site Networks, Access Points)
- All eight discovery tiers
- Tier-0 baseline seeds
- All authoritative sources
- All discovery sub-procedures v6.0

------------------------------------------------------------
# 3. SESSION ARTIFACTS
Mandatory Files Created at Bootstrap

Every discovery session must create and maintain the following artifacts before
Tier 1 begins. These files are the persistent record of the session — they must
not rely on chat history.

## 3.1 Raw Discovery Staging File

**Filename:** `{county}_ohio_raw_discovery.yaml`
**Location:** `County_Spreadsheets/{County}/`

- Create at bootstrap, before Tier 1 begins
- Append each entity record immediately upon discovery — do not batch-write at
  tier end
- Records entity-level data: raw discovery records and null-tier documentation
- The authoritative data record for the county run

## 3.2 Handoff Document

**Filename:** `{county}_ohio_handoff.md`
**Location:** `County_Spreadsheets/{County}/`

- Tracks inter-session progress: current tier, completed tiers, flags, open items
- Progress tracker only — no protocol authority

## 3.3 Session Log

**Filename:** `{county}_ohio_session_log.md`
**Location:** `County_Spreadsheets/{County}/`

- Chronological log of decisions, sources checked, and notable findings

## 3.4 Source Documents Folder

**Path:** `County_Spreadsheets/{County}/source_documents/`

- Created at bootstrap
- Stores downloaded maps, brochures, trail guides, PDFs, GPX/KML files, and
  other spatial or descriptive documents encountered during discovery
- See §4 (Document Collection System) for full rules

## 3.5 Document Log

**Filename:** `{county}_document_log.yaml`
**Location:** `County_Spreadsheets/{County}/source_documents/`

- Lives inside the `source_documents/` folder alongside the downloaded files
- One entry per downloaded document
- Append each entry at the time of download
- See §4 (Document Collection System) for format and rules

## 3.6 Chat Window Role

The chat window is a progress monitor, not a data store:

- Raw discovery records → staging file only
- Brief entity summary (name, tier, type, flags) → chat window
- Uncertainties and conflicts → both chat (flag) and staging file
  (`identity_notes_raw`)
- Tier completion status → chat window
- Null-tier documentation → staging file

------------------------------------------------------------
# 4. DOCUMENT COLLECTION SYSTEM

## 4.1 Purpose

Entity records capture URLs in `urls_raw` to document their sources. This is
necessary but not sufficient — URLs rot, websites reorganize, and PDFs are
removed without notice. The Document Collection System ensures that the actual
source material is preserved alongside the entity records that reference it.

Maps, brochures, trail guides, and similar documents are research assets. They
often contain information — GPS coordinates, surface type diagrams, access
narratives, facility layouts — that informed discovery decisions. Preserving them
creates a durable, auditable record of what was known at discovery time.

## 4.2 What to Download

**Download (save to `source_documents/`):**
- Trail maps and system maps (PDF, image)
- Park and preserve brochures (PDF)
- Paddling guides and water trail guides (PDF)
- Master plans and corridor plans (PDF) when they contain spatial or natural
  area content relevant to discovery
- GIS exports in downloadable format (Shapefile ZIP, GeoJSON)
- GPX and KML files for trails
- System overview maps (PDF, image)
- Trailhead kiosk documentation if downloadable

**Log URL only (do not download — record in document log with `local_file` blank):**
- Interactive GIS viewers and ArcGIS REST endpoints — these cannot be meaningfully
  saved as a file; log the URL for reference
- Web pages that are HTML only with no downloadable content
- ArcGIS FeatureServer query endpoints — log the URL and query parameters

**Skip:**
- General web pages, about pages, contact pages — cite in `urls_raw` on the entity
  record but do not log in the document log
- Duplicate documents: if you have already downloaded the same file in this
  session, do not download again; reference the existing entry in the document log

## 4.3 Filename Convention

All downloaded files must be named:

```
{date}_{tier}_{short-descriptor}.{ext}
```

**Components:**
- `{date}`: YYYY-MM-DD — the date the file was retrieved
- `{tier}`: T1 through T8 — the discovery tier in which it was found
- `{short-descriptor}`: lowercase, hyphen-separated; enough to identify the
  document at a glance without opening it (3–6 words)
- `{ext}`: original file extension (pdf, gpx, kml, geojson, zip, jpg, png, etc.)

**Examples:**
```
2026-05-30_T3_oak-openings-trail-map.pdf
2026-05-30_T2_maumee-state-forest-brochure.pdf
2026-05-30_T7_bsc-preserve-network-map.pdf
2026-05-30_T1_buckeye-trail-wood-county.gpx
2026-05-30_T4_county-park-district-system-map.pdf
2026-05-30_T6_bowling-green-parks-trail-guide.pdf
```

Do not use spaces in filenames. Do not include the county name (it is implicit
from the folder location).

## 4.4 Document Log Format

Each downloaded document — or URL-only reference — gets an entry in
`{county}_document_log.yaml`. Append the entry at the time of download.

```yaml
documents:
  - local_file: "2026-05-30_T3_oak-openings-trail-map.pdf"
    url: "https://metroparks.net/maps/oak-openings-trail-map.pdf"
    document_type: Trail Map PDF
    date_accessed: "2026-05-30"
    title: "Oak Openings Preserve Metropark — Trail Map"
    description: "Full trail system map; trailhead locations, loop names, distances,
      surface types, facility icons"
    tier: 3
    entities: "Oak Openings Preserve Metropark; Oak Openings trailheads"

  - local_file: ""
    url: "https://gis.metroparks.net/viewer/?layer=trails"
    document_type: Interactive GIS Viewer
    date_accessed: "2026-05-30"
    title: "MCMP Interactive Trail Map Viewer"
    description: "Interactive GIS viewer showing all district trails and trailheads;
      no downloadable file"
    tier: 3
    entities: "Metro Parks Serving Franklin County (multiple entities)"
```

**Field definitions:**

| Field | Required | Description |
|---|---|---|
| `local_file` | Yes | Filename in `source_documents/`; blank if URL-only |
| `url` | Yes | Full URL where the document was found or accessed |
| `document_type` | Yes | See §4.5 for allowed values |
| `date_accessed` | Yes | YYYY-MM-DD — date retrieved or accessed |
| `title` | Yes | Document title as stated, or a clear descriptive title |
| `description` | Yes | 1-2 sentences: what the document covers and what it contains |
| `tier` | Yes | Discovery tier (integer 1–8) in which the document was encountered |
| `entities` | Optional | Informal list of entity names this document supports; semicolon-delimited; free text, not enforced references |

The `entities` field is a convenience annotation. It captures what is obvious at
discovery time but is not required to be comprehensive, and does not need to be
updated when entity names change during resolution. The entity record's `urls_raw`
field is the authoritative forward link from entity to document.

## 4.5 Document Type Values

Use one of the following values for `document_type`:

- **Trail Map PDF** — static PDF trail map
- **Park Brochure PDF** — park or preserve brochure (may include maps)
- **Paddling Guide PDF** — water trail guide or paddling brochure
- **Master Plan PDF** — master plan or corridor plan with natural area content
- **System Overview Map** — multi-site or county-wide system map (PDF or image)
- **GPX File** — GPS track file for a trail or route
- **KML/KMZ File** — Google Earth format trail or route file
- **GIS Export** — downloaded shapefile, GeoJSON, or similar GIS data file
- **Interactive GIS Viewer** — web-based map viewer (URL-only; no local file)
- **ArcGIS REST Endpoint** — ArcGIS FeatureServer or MapServer URL (URL-only)
- **Kiosk Documentation** — downloaded trailhead kiosk content or image
- **Other** — any downloadable document not covered above; describe in `description`

## 4.6 Download Timing

Download and log documents as you encounter them during discovery — not at tier
end. If you find a trail map PDF while discovering a specific trail, download it
and log it immediately. This prevents documents from being missed if a session
ends before tier close.

## 4.7 Relationship to Entity Records

The document log and the entity records serve complementary roles:

- **Entity record `urls_raw`**: lists all URLs associated with that entity,
  including links to maps and PDFs. This is the forward link: entity → document.
- **Document log**: provides the provenance record for every significant document
  — URL, local filename, date, what it covers. This is the document inventory.

Any document cited in `urls_raw` that meets the download criteria (§4.2) must
have an entry in the document log. The two records are complementary — one is not
a substitute for the other.

------------------------------------------------------------
# 5. EXECUTION PRINCIPLES

The orchestration engine must enforce:

**No normalization:**
- Do not normalize names, types, features, difficulty, accessibility, GPS,
  county lists, URLs, governance, or any other field
- Raw values are preserved exactly as found

**No invention:**
- Do not invent names, parents, URLs, GPS coordinates, features, difficulty,
  accessibility, ownership, governance, partner agencies, or coordination

**No inference:**
- Do not infer township (GIS-derived in normalization)
- Do not infer municipality (GIS-derived in normalization)
- Do not infer difficulty (must be explicitly stated by authoritative source)
- Do not infer accessibility (must be explicitly stated)
- Do not infer parent relationships (must be documented in source)

**No silent correction:**
- Malformed values must be preserved exactly as discovered
- Corrections are handled downstream by Normalization

**Deterministic execution:**
- Given the same inputs, discovery must always produce the same raw outputs

**Tier authority:**
- Lower-numbered tiers take precedence in primary tier assignment
- Conflict precedence is applied downstream in Resolution

**Enumerative + recursive discovery:**
- Enumerate all first-level entity URLs from authoritative listing pages
- Recursively follow allowed internal links for deeper metadata

------------------------------------------------------------
# 6. HIGH-LEVEL WORKFLOW

For each county:

1. Create session artifacts at bootstrap (§3): staging YAML, handoff, session
   log, `source_documents/` folder, document log
2. Run Tiers 1–8 in order (skipping tiers already fully discovered)
3. Run Tier-0 Baseline (if provided)
4. For each tier:
   a. Perform enumerative discovery
   b. For each enumerated entity URL, run entity detection and extraction
   c. Perform recursive discovery on allowed internal links
   d. Download and log source documents encountered (§4)
   e. Run all four entity tracks in order (§8)
   f. Document null-tier result if no entities found
5. Collect Raw Discovery Records v6.x
6. Pass all raw outputs to the Resolution Engine v6.x

This workflow must be executed once per county, independently.
State must never be shared across counties.

------------------------------------------------------------
# 7. TIER EXECUTION ORDER

Discovery must execute tiers in the following strict order:

1. Federal
2. State
3. Park District
4. County
5. Township
6. Municipal
7. Land Trust and Conservancy
8. Private
9. Tier-0 Baseline (runs last)

Each tier must fully complete before the next tier begins.
Parallelization across tiers within the same county is not permitted.

**Null-tier documentation is mandatory.** If a tier produces zero entities,
the staging file must record:

- The tier number
- The tier category
- A null result indicator
- The number of entities discovered (zero)
- All sources checked
- Notes explaining what was searched
- The date of completion

A missing null-tier record is a discovery defect.

------------------------------------------------------------
# 8. ENTITY TRACK EXECUTION ORDER

Within each tier, entity tracks must execute in the following order:

1. Sites
2. Trailthings
3. Site Networks
4. Access Points

This ordering ensures that parent entities (Sites and Trailthings) are
surfaced before the entities that depend on them (Access Points). Site Networks
are processed after Trailthings because Site Network membership may reference
Sites discovered during the current tier.

Trail Networks, Trails, and Trail Segments are no longer processed as separate
entity tracks in v6.x. All are captured as Trailthings.

------------------------------------------------------------
# 9. SUB-PROCEDURE INVOCATION

Each entity track must invoke its authoritative v6.0 discovery sub-procedure:

- **Site Discovery Sub-Procedure v6.0**
- **Trailthing Discovery Sub-Procedure v6.0**
- **Site Network Discovery Sub-Procedure v6.0**
- **Access Point Discovery Sub-Procedure v6.0**

Each sub-procedure must return:
- Raw Discovery Records conforming to the v6.0 schema for that entity type
- All parent relationships captured in raw form

Each tier's execution must also invoke the authoritative tier sub-procedure
for governance-tier-specific rules (v5.x tier sub-procedures remain
authoritative until v6.x equivalents are written).

------------------------------------------------------------
# 10. STATE MANAGEMENT

The orchestration engine must maintain three scopes of state.

**County-scoped state:**
- All discovered entities
- All source documents (document log)
- All source references
- All conflicts
- All uncertainties

**Tier-scoped state:**
- Entities discovered within the current tier
- Documents downloaded within the current tier
- Sources used
- Errors and fallbacks

**Entity-scoped state:**
- Raw Discovery Records
- Parent relationships (raw)
- Boundary flags
- parent_url provenance

State must never be shared across counties.

------------------------------------------------------------
# 11. MULTI-COUNTY RULE ENFORCEMENT

The orchestration engine must enforce the multi-county rule:

- Multi-county entities must not be segmented
- All counties must be recorded exactly as discovered
- Raw county lists must be preserved
- Normalization alphabetizes and formats county lists downstream

This rule applies to all four entity types.

------------------------------------------------------------
# 12. ENUMERATIVE DISCOVERY

For each tier, enumerative discovery must:

- Identify authoritative listing or index pages
- Extract all first-level entity URLs
- Queue each URL for entity detection and extraction

Partial enumeration is a discovery defect.

------------------------------------------------------------
# 13. RECURSIVE DISCOVERY

For each discovered entity page, recursive discovery must:

- Extract internal links
- Filter links using allowed patterns
- Enforce recursion depth limits
- Enforce per-domain and per-entity page limits
- Queue child URLs
- Record parent_url for provenance

Recursive discovery must never infer structure or invent relationships.

During recursive traversal, apply document collection rules (§4) at each
page — download qualifying documents encountered on child pages, not only
on top-level entity pages.

------------------------------------------------------------
# 14. RAW OUTPUT ASSEMBLY

The orchestration engine must produce one Raw Discovery Record v6.x per
entity occurrence. All outputs must conform to the relevant v6.0 schema
modules and vocabulary modules.

The following fields must remain blank at discovery time for all entity types:
- `township_raw` / `township`
- `municipality_raw` / `municipality`
- `plus_code`
- All entity ID fields (assigned by Upsert Engine)

The following fields must remain blank at discovery time for Access Points
specifically:
- `access_point_id`

Discovery must not normalize, correct, dedupe, infer, invent, or silently
modify any values. All malformed or partial values must be preserved exactly
as found.

------------------------------------------------------------
# 15. BASELINE INTEGRATION (TIER-0)

If a county baseline exists, the orchestration engine must:

- Load baseline rows as Tier-0 raw records
- Mark `seeded_from_baseline: true`
- Preserve baseline IDs exactly
- Allow authoritative discovery to override baseline values
- Preserve all conflicts in metadata
- Record all discrepancies without correction

Tier-0 runs after all authoritative tiers.
Tier-0 must never override authoritative discovery.

------------------------------------------------------------
# 16. ERROR HANDLING AND FALLBACKS

The orchestration engine must:

- Log all errors
- Never discard partial results
- Never invent missing values
- Never silently correct malformed values
- Mark uncertainties in metadata
- Continue execution unless a tier is completely inaccessible
- Explicitly flag inaccessible tiers

If a tier cannot be accessed due to outage, missing pages, or structural failure,
the staging file must record:

- The nature of the failure
- All attempted sources
- The date
- Whether retry is recommended

If a document download fails (file not accessible, timeout, format
unrecognized), log the URL in the document log with `local_file` blank and
a note in `description` indicating the failure. Do not retry indefinitely —
log and continue.

------------------------------------------------------------
# 17. COUNTY FOLDER STRUCTURE AT DISCOVERY COMPLETION

At the end of a completed county discovery run, the county folder should contain:

```
County_Spreadsheets/{County}/
├── {county}_ohio_raw_discovery.yaml      ← entity staging file
├── {county}_ohio_handoff.md              ← inter-session progress tracker
├── {county}_ohio_session_log.md          ← session log
├── {county}_config.json                  ← pipeline run config (created at pipeline stage)
│
└── source_documents/
    ├── {county}_document_log.yaml        ← document provenance log
    ├── 2026-05-30_T1_buckeye-trail-gpx.gpx
    ├── 2026-05-30_T2_maumee-state-forest-brochure.pdf
    ├── 2026-05-30_T3_metroparks-trail-system-map.pdf
    ├── 2026-05-30_T4_county-park-trail-guide.pdf
    ├── 2026-05-30_T7_bsc-preserve-network-map.pdf
    └── ...
```

The `source_documents/` folder is a research asset. It is not consumed by
the pipeline — the pipeline works from the staging YAML. It is preserved for
reference, re-verification, and audit.

------------------------------------------------------------
# 18. INTEGRATION POINTS

This module integrates with:

- All Discovery Sub-Procedures v6.0
- All Tier Sub-Procedures v5.x *(until v6.x equivalents are written)*
- Site Network Schema Module v6.0
- Trailthing Schema Module v6.0
- Site Schema Module v6.0
- Access Point Schema Module v6.0
- Resolution Engine v6.x *(or v5.x)*
- Normalization Engine v6.x *(or v5.x)*
- Entity Upsert Engine v6.x *(or v5.x)*
- Audit and Logging Module v6.x *(or v5.x)*
- County Baseline Module v6.x *(or v5.x)*

Integration must be deterministic and must not rely on chat history.

------------------------------------------------------------
# 19. MODULE DEPENDENCIES

This module depends on:

- Site Discovery Sub-Procedure v6.0
- Trailthing Discovery Sub-Procedure v6.0
- Site Network Discovery Sub-Procedure v6.0
- Access Point Discovery Sub-Procedure v6.0
- All eight Tier Sub-Procedures v5.x *(until v6.x equivalents are written)*
- Resolution Engine v6.x *(or v5.x)*
- Audit and Logging Module v6.x *(or v5.x)*
- County Baseline Module v6.x *(or v5.x)*

------------------------------------------------------------
# END OF DISCOVERY ORCHESTRATION MODULE v6.0
