# DISCOVERY METADATA SPECIFICATION v3.1
(Structured Metadata for All Discovery Tiers and Access Point Consolidation)

Discovery Metadata is the **audit backbone** of the entire Natural Areas system.
It records *how* each entity was discovered, *why* it was included, *what sources
were used*, and *what uncertainties remain*. This specification defines the
**required metadata fields**, their structure, and their semantics.

This module is referenced **only** by the Discovery Protocol Module v3.1 and the
tier‑specific discovery sub‑procedures. No other module may reference it directly.

------------------------------------------------------------
# 1. PURPOSE

This specification defines:

- The metadata fields required for every discovered entity
- The structure of metadata for all seven entity types
- How conflicts, uncertainties, and multi‑tier discoveries must be recorded
- How metadata integrates with the Audit & Logging Module v1.1
- How metadata is passed to normalization and resolution modules

Metadata ensures that discovery is **transparent, auditable, reproducible, and
non‑destructive**.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All entities discovered in Tiers 1–8:
  - Site
  - Sub‑Site
  - Trail
  - Trail Segment
  - Trail Network
  - Site Network
  - Access Point
- All Access Points discovered in the Access Point Discovery Sub‑Procedure v3.1
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
identity: name_raw: (string, required) entity_type: (one of 7 ontology types, required) county: (string, required) township: (string, optional) municipality: (string, optional)

Rules:

- `name_raw` must be the name as discovered, not normalized.
- `entity_type` must be one of:
  - Site
  - Sub‑Site
  - Trail
  - Trail Segment
  - Trail Network
  - Site Network
  - Access Point
- County is always required.
- Township and municipality are included if known.

------------------------------------------------------------
# 5. TIER METADATA
tiers: discovered_in: [list of tier numbers or "AP", required] primary_tier: (tier number or "AP", required)

Rules:

- `discovered_in` lists all tiers where the entity appeared.
- `primary_tier` is the tier with the highest authority (lowest number).
- Access Points use `AP` as their tier.

Examples:

- A trailhead found in Tier 3 and Tier 4 → `discovered_in: [3,4]`, `primary_tier: 3`
- A Site found only in Tier 6 → `discovered_in: [6]`, `primary_tier: 6`

------------------------------------------------------------
# 6. SOURCE METADATA
sources: urls: [list of URLs, required if available] datasets: [list of dataset names, optional] maps: [list of map names or identifiers, optional] gis_layers: [list of GIS layers, optional]

Rules:

- All sources must be preserved.
- No source may be discarded.
- URLs must be stored exactly as discovered.
- GIS layers must be recorded if used.

------------------------------------------------------------
# 7. CONFLICT METADATA
conflicts: name_conflicts: [] type_conflicts: [] location_conflicts: [] parent_conflicts: []

Rules:

- Conflicts must be recorded, not resolved.
- Normalization resolves conflicts later.
- Discovery must preserve all conflicting values.

------------------------------------------------------------
# 8. UNCERTAINTY METADATA
uncertainty: requires_review: (boolean) reason: (string, optional) notes: (string, optional)

Examples:

- “Access Point appears on map but not in text.”
- “Site name inconsistent across sources.”
- “Trail corridor unclear; segmentation required.”

------------------------------------------------------------
# 9. PARENT METADATA (ACCESS POINTS ONLY)
parents: sites: [list of Site names or IDs] trail_systems: [list of Trail or Trail Network names]

Rules:

- Multiple parents allowed.
- Parent relationships must be preserved exactly as discovered.
- If no parent can be identified:
  - `sites: []`
  - `trail_systems: []`
  - `uncertainty.requires_review = true`

------------------------------------------------------------
# 10. BOUNDARY METADATA
boundary: multi_county: (boolean) counties: [list of counties] boundary_notes: (string, optional)

Rules:

- Multi‑county entities must be flagged.
- Each county receives its own Raw Candidate Record.
- Boundary notes must describe segmentation logic if known.

------------------------------------------------------------
# 11. BASELINE METADATA
baseline: seeded_from_baseline: (boolean) baseline_id: (string, optional)

Rules:

- If the entity originated from the County Baseline → `seeded_from_baseline = true`.
- If discovered independently → `seeded_from_baseline = false`.
- Baseline ID is included if available.

------------------------------------------------------------
# 12. NOTES
notes: general: (string, optional)

Notes may include:

- Access limitations
- Seasonal closures
- Co‑management details
- Stewardship notes
- Trail system integration notes

------------------------------------------------------------
# 13. COMPLETE METADATA OBJECT (TEMPLATE)
discovery_metadata:
identity: name_raw: entity_type: county: township: municipality:
tiers: discovered_in: [] primary_tier:
sources: urls: [] datasets: [] maps: [] gis_layers: []
conflicts: name_conflicts: [] type_conflicts: [] location_conflicts: [] parent_conflicts: []
uncertainty: requires_review: reason: notes:
parents: sites: [] trail_systems: []
boundary: multi_county: counties: [] boundary_notes:
baseline: seeded_from_baseline: baseline_id:
notes: general:

------------------------------------------------------------
# 14. INTEGRATION POINTS

This specification integrates with:

- Discovery Protocol Module v3.1
- All eight tier‑specific discovery sub‑procedures
- Access Point Discovery Sub‑Procedure v3.1
- Audit & Logging Module v1.1
- Discovery Output Specification v3.1
- County Baseline Module v1.1
- Resolution Module v1

No other module may reference this specification directly.

------------------------------------------------------------
# 15. VERSIONING

- This module is **Discovery Metadata Specification v3.1**.
- Any change to metadata structure requires v3.2, v4.0, etc.
- Any change to tier order or workflow must be made in the Discovery Protocol Module v3.1.

------------------------------------------------------------
# END OF DISCOVERY METADATA SPECIFICATION v3.1
