# NATURAL AREAS PROJECT — DISCOVERY METADATA SPECIFICATION v3.2.2
(Structured Metadata for All Discovery Tiers and Access Point Consolidation)

Discovery Metadata is the **audit backbone** of the entire Natural Areas system.
It records *how* each entity was discovered, *why* it was included, *what sources
were used*, and *what uncertainties remain*. This specification defines the
**required metadata fields**, their structure, and their semantics.

This module is referenced **only** by the Discovery Protocol Module v3.2.2 and the
tier‑specific discovery sub‑procedures v3.2.2. No other module may reference it directly.

------------------------------------------------------------
# 1. PURPOSE

This specification defines:

- The metadata fields required for every discovered entity  
- The structure of metadata for all six entity types  
- How conflicts, uncertainties, and multi‑tier discoveries must be recorded  
- How metadata integrates with the Audit & Logging Module v3.2.2  
- How metadata is passed to normalization and resolution modules  

Metadata ensures that discovery is **transparent, auditable, reproducible, and
non‑destructive**.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All entities discovered in Tiers 1–8:  
  - Site (including child Sites)  
  - Trail  
  - Trail Segment  
  - Trail Network  
  - Site Network  
  - Access Point  
- All Access Points discovered in the Access Point Discovery Sub‑Procedure v3.2.1  
- All multi‑tier discoveries  
- All conflict cases  
- All uncertainty cases  
- All baseline interactions  

It governs:

- Metadata structure  
- Metadata semantics  
- Metadata completeness requirements  
- Metadata integration with logs  

------------------------------------------------------------
# 3. METADATA STRUCTURE OVERVIEW

Each discovered entity must have a **Discovery Metadata Object** containing:

1. **Identity Metadata**  
2. **Tier Metadata**  
3. **Source Metadata**  
4. **Conflict Metadata**  
5. **Uncertainty Metadata**  
6. **Parent Metadata** (Access Points only)  
7. **Boundary Metadata**  
8. **Baseline Metadata**  
9. **Notes**  

All fields are required unless explicitly marked optional.

------------------------------------------------------------
# 4. IDENTITY METADATA

identity:
  name_raw: (string, required)  
  entity_type: (one of 6 ontology types, required)  
  county: (string, required)  
  counties_raw: [list of counties, required]  
  township: (string, optional)  
  municipality: (string, optional)  
  parent_site: (string, optional)  
  access_level_raw: (string, optional)  

Rules:

- `name_raw` must be the name as discovered, not normalized.  
- `entity_type` must be one of:  
  - Site  
  - Trail  
  - Trail Segment  
  - Trail Network  
  - Site Network  
  - Access Point  
- `county` is the primary county (first discovered or highest‑authority source).  
- `counties_raw` must list **all counties exactly as discovered**.  
- `parent_site` is required for child Sites.  
- `access_level_raw` is required for Private tier entities and optional elsewhere.

------------------------------------------------------------
# 5. TIER METADATA

tiers:
  discovered_in: [list of tier numbers or "AP", required]  
  primary_tier: (tier number or "AP", required)  

Rules:

- `discovered_in` lists all tiers where the entity appeared.  
- `primary_tier` is the tier with the highest authority (lowest number).  
- Access Points may use `"AP"` if discovered via AP‑specific workflows.

------------------------------------------------------------
# 6. SOURCE METADATA

sources:
  urls: [list of URLs, required if available]  
  datasets: [list of dataset names, optional]  
  maps: [list of map names or identifiers, optional]  
  gis_layers: [list of GIS layers, optional]  

Rules:

- All sources must be preserved.  
- No source may be discarded.  
- URLs must be stored exactly as discovered.  
- GIS layers must be recorded if used.

------------------------------------------------------------
# 7. CONFLICT METADATA

conflicts:
  name_conflicts: []  
  type_conflicts: []  
  location_conflicts: []  
  parent_conflicts: []  

Rules:

- Conflicts must be recorded, not resolved.  
- Normalization and Resolution resolve conflicts later.  
- Discovery must preserve all conflicting values.

------------------------------------------------------------
# 8. UNCERTAINTY METADATA

uncertainty:
  requires_review: (boolean)  
  reason: (string, optional)  
  notes: (string, optional)  

Examples:

- “Access Point appears on map but not in text.”  
- “Site name inconsistent across sources.”  
- “Trail corridor unclear; segmentation required.”  

------------------------------------------------------------
# 9. PARENT METADATA (ACCESS POINTS ONLY)

parents:
  sites: [list of Site names or IDs]  
  trails: [list of Trail names or IDs]  
  trail_segments: [list of Trail Segment names or IDs]  

Rules:

- Multiple parents allowed.  
- Parent lists must preserve **exactly what was discovered**, without normalization.  
- Parent lists must reflect **identity‑defining** relationships only.  
- Site Networks and Trail Networks must **not** appear in parent metadata.  
- If no parent can be identified:  
  - `sites: []`  
  - `trails: []`  
  - `trail_segments: []`  
  - `uncertainty.requires_review = true`  

------------------------------------------------------------
# 10. BOUNDARY METADATA (UPDATED)

boundary:
  multi_county: (boolean)  
  counties_raw: [list of counties]  
  boundary_notes: (string, optional)  

Rules:

- Multi‑county entities must be flagged.  
- Discovery must **never segment** multi‑county entities.  
- All counties must be recorded **exactly as discovered**.  
- Normalization writes the county list as a **semicolon‑delimited, alphabetized list**.  
- `counties_raw` must preserve the raw discovery order and spelling.

------------------------------------------------------------
# 11. BASELINE METADATA

baseline:
  seeded_from_baseline: (boolean)  
  baseline_id: (string, optional)  

Rules:

- If the entity originated from the County Baseline → `seeded_from_baseline = true`.  
- If discovered independently → `seeded_from_baseline = false`.  
- Baseline ID is included if available.

------------------------------------------------------------
# 12. NOTES

notes:
  general: (string, optional)  
  discovery_raw: (string, optional)  

Notes may include:

- Access limitations  
- Seasonal closures  
- Co‑management details  
- Stewardship notes  
- Trail system integration notes  
- Raw discovery notes from tier modules  

------------------------------------------------------------
# 13. COMPLETE METADATA OBJECT (TEMPLATE)

discovery_metadata:
  identity:
    name_raw:
    entity_type:
    county:
    counties_raw: []
    township:
    municipality:
    parent_site:
    access_level_raw:
  tiers:
    discovered_in: []
    primary_tier:
  sources:
    urls: []
    datasets: []
    maps: []
    gis_layers: []
  conflicts:
    name_conflicts: []
    type_conflicts: []
    location_conflicts: []
    parent_conflicts: []
  uncertainty:
    requires_review:
    reason:
    notes:
  parents:
    sites: []
    trails: []
    trail_segments: []
  boundary:
    multi_county:
    counties_raw: []
    boundary_notes:
  baseline:
    seeded_from_baseline:
    baseline_id:
  notes:
    general:
    discovery_raw:

------------------------------------------------------------
# 14. INTEGRATION POINTS

This specification integrates with:

- Discovery Protocol Module v3.2.2  
- All tier‑specific discovery sub‑procedures v3.2.2  
- Access Point Discovery Sub‑Procedure v3.2.2  
- Audit & Logging Module v3.2.2  
- Discovery Output Specification v3.2.2  
- County Baseline Module v3.2.2  
- Resolution Module v3.2.2  

No other module may reference this specification directly.

------------------------------------------------------------
# 15. VERSIONING

- This module is **Discovery Metadata Specification v3.2.2**.  
- Any change to metadata structure requires v3.3, v4.0, etc.  
- Any change to tier order or workflow must be made in the Discovery Protocol Module v3.2.2.

------------------------------------------------------------
# END OF DISCOVERY METADATA SPECIFICATION v3.2.2