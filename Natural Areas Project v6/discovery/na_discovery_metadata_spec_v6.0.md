# NATURAL AREAS PROJECT
# DISCOVERY METADATA SPECIFICATION v6.0
Authoritative Metadata Structure for Raw Discovery Layer

This module supersedes Discovery Metadata Specification v5.3.

Discovery Metadata is the audit backbone of the v6.0 Discovery System. It records
how each entity was discovered, where it came from, what URLs and documents led to
it, what uncertainties remain, and how the raw record fits into the enumerative
and recursive discovery model.

This specification defines the required metadata fields, their structure, and their
semantics for all four v6.x entity types.

This module is referenced only by:

- Discovery Protocol Module v6.x
- Discovery Orchestration Module v6.x
- All Tier Sub-Procedures v6.x
- All Entity Discovery Sub-Procedures v6.x

No other module may reference this specification directly.

------------------------------------------------------------
# CHANGES FROM v5.3 → v6.0

- **Entity types updated throughout**: Six types → four (Site, Trailthing, Site
  Network, Access Point). entity_type allowed values updated in §4.

- **Trailthing raw fields added** (§15.2): Complete raw field list replacing the
  three "pending" sections for Trail, Trail Segment, and Trail Network. Includes
  source_term_raw, source_hierarchy_context_raw, parent_id_raw, site_parent_raw,
  parent_site_network_raw, member_trailthing_names_raw and all v5 trail fields.

- **Site Network and Access Point raw fields added** (§15.3, §15.4): Previously
  marked "pending" in v5.3 — now complete.

- **`boundary_document_raw` added to Site raw fields** (§15.1): Replaces the
  boundary metadata block. Records the filename of a downloaded boundary document
  (shapefile, KMZ, GeoJSON) in `source_documents/`. Presence = boundary document
  captured; blank = none found. The Document Collection System handles the
  corresponding document log entry.

- **Boundary Metadata block dropped** (was §13): The boolean `boundary_present`
  triggered no downstream pipeline behavior. Boundary document capture is now
  handled by `boundary_document_raw` on the entity raw record (site-level) and
  the Document Collection System (county-level log). The block was vestigial.

- **Source Metadata updated** (§7): `documents` added as a named source type,
  referencing the Document Collection System (`{county}_document_log.yaml`).
  Source documents (maps, PDFs, GIS exports, GPX/KML files) encountered during
  discovery are logged there and referenced here by filename.

- **Extraction method values renamed** (§8): Values now describe the tool or
  method used, not a workflow category. Renamed for consistency and clarity:
  - `"agency_website"` — information read from an official agency or organization
    website (the primary discovery method for most entities)
  - `"browser"` — Claude in Chrome used to navigate a JS-rendered page, ArcGIS
    viewer, interactive GIS portal, or other browser-dependent source
  - `"gis_download"` — coordinates or entity data extracted from a downloaded
    GIS dataset (MORPC layer, ODNR Lake Map, SORP, county GIS export, etc.)
  - `"document"` — entity data extracted from a downloaded document (PDF map,
    brochure, management plan, GPX/KML file) logged in the document collection
  - `"baseline"` — entity seeded from Tier-0 county baseline spreadsheet
  - `"human_assist"` — user provided information directly (coordinate, name
    confirmation, source page) when automated methods could not resolve it

- **AP Parent Metadata expanded** (§12): v5 only covered `parent_site_raw`. v6
  APs may parent to both Sites and Trailthings. Both are now documented.

- **Lineage block retained as single-parent pointer** (§9): Trailthing multi-parent
  detail (parent Trailthing, site parent, Site Network parent) lives in the raw
  fields section where it is already captured verbatim. Lineage metadata records
  the discovery chain — which entity or URL spawned this discovery — not the full
  parent model.

- **All v5.3 conflict and uncertainty rules carried forward** (§10, §11).

------------------------------------------------------------
# 1. PURPOSE

This specification defines:

- The metadata fields required for every Raw Discovery Record v6.x
- The structure of metadata for all four entity types
- How provenance, lineage, and recursion must be recorded
- How conflicts and uncertainties must be preserved
- How metadata integrates with the Audit & Logging Module v6.x
- How metadata is passed to the Resolution Engine v6.x

Metadata ensures that discovery is transparent, auditable, reproducible,
and non-destructive.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All entities discovered in Tiers 1–8
- All entities discovered via recursive URL propagation
- All entities seeded from Tier-0 Baseline
- All multi-tier discoveries
- All conflict cases
- All uncertainty cases

It governs:

- Metadata structure
- Metadata semantics
- Metadata completeness requirements
- Metadata integration with logs

------------------------------------------------------------
# 3. METADATA STRUCTURE OVERVIEW

Each Raw Discovery Record v6.x must include a Discovery Metadata Object containing:

1.  Identity Metadata
2.  Organizational Metadata
3.  Tier Metadata
4.  Source Metadata
5.  Provenance Metadata
6.  Lineage Metadata
7.  Conflict Metadata
8.  Uncertainty Metadata
9.  Parent Metadata (Access Points only)
10. Baseline Metadata
11. Raw Field Preservation Rules
12. Notes

All fields are required unless explicitly marked optional.

------------------------------------------------------------
# 4. IDENTITY METADATA

```yaml
identity:
  name_raw:              # string, required
  entity_type:           # one of four v6.x types, required
  counties_raw:          # list of counties, required
  township_raw:          # must be blank — GIS-derived only
  municipality_raw:      # must be blank — GIS-derived only
  parent_site_raw:       # string, optional — required for child Sites
  category_raw:          # string, optional — Sites only
  subtype_raw:           # string, optional — Sites only
  designation_raw:       # string, optional — Sites only
  status_raw:            # string, optional
  description_raw:       # string, optional
  location_raw:          # string, optional — Sites and Access Points
  acres_raw:             # string or numeric, optional — Sites only
  habitat_type_raw:      # string, optional — Sites only
  access_notes_raw:      # string, optional — Sites only
  boundary_document_raw: # string, optional — Sites only; filename in source_documents/
  gps_lat_raw:           # numeric, optional — only when explicitly stated by source
  gps_lon_raw:           # numeric, optional — only when explicitly stated by source
  features_raw:          # string, optional — Sites and Access Points
  source_term_raw:       # string, required for Trailthings — verbatim from source
  source_hierarchy_context_raw: # string, optional — Trailthings only
  difficulty_raw:        # string, optional — Trailthings only
  accessibility_raw:     # string, optional — Trailthings only
  url_primary_raw:       # string, optional
  urls_raw:              # list of URLs, optional
  ebird_hotspot_id:      # string, optional — Sites only; eBird L-code (e.g. L123456)
  identity_notes_raw:    # string, optional
  last_verified_date:    # DATE, optional — populated with today's date at discovery
  field_verified:        # boolean, optional — always false at discovery
```

Rules:

- `name_raw` must be preserved exactly as discovered.
- `entity_type` must be one of:
  - `Site`
  - `Trailthing`
  - `Site Network`
  - `Access Point`
- `counties_raw` must list all counties exactly as discovered, with no normalization.
- `township_raw` and `municipality_raw` must always be blank during discovery.
  These fields are GIS-derived only.
- `parent_site_raw` is required for child Sites; optional elsewhere.
- `category_raw`, `subtype_raw`, `designation_raw`, and `status_raw` must be
  preserved exactly as discovered. No normalization or vocabulary matching occurs
  during discovery.
- `description_raw` must be preserved exactly as discovered. No summarization
  or rewriting is permitted.
- `habitat_type_raw` must be preserved exactly as discovered. No normalization —
  this is an open vocabulary field in v6.x.
- `access_notes_raw` must be preserved exactly as discovered.
- `boundary_document_raw` records the filename (relative to `source_documents/`)
  of a downloaded boundary file (shapefile, KMZ, GeoJSON, etc.) for this entity.
  Blank if no boundary document was downloaded. The corresponding document log
  entry in `{county}_document_log.yaml` is the authoritative provenance record.
- `location_raw` must be preserved exactly as discovered. No GIS substitution
  or inference is permitted.
- `acres_raw` must be preserved exactly as discovered, including malformed or
  ambiguous values.
- `gps_lat_raw` and `gps_lon_raw` may be populated only when explicitly provided
  by an authoritative source. No inference or derivation is permitted.
- `source_term_raw` is required for Trailthings. It records verbatim the word or
  phrase the authoritative source uses to describe what kind of entity this is.
  Leave blank only if the source provides no descriptive term — do not invent one.
- `features_raw` must be preserved exactly as discovered. No categorization or
  vocabulary matching occurs during discovery.
- `difficulty_raw` and `accessibility_raw` must only be populated if explicitly
  stated by an authoritative source. No inference is permitted.
- `url_primary_raw` and `urls_raw` must be preserved exactly as discovered,
  including tracking parameters.
- `identity_notes_raw` must be preserved exactly as discovered.
- `last_verified_date` is populated with today's date at discovery time.
- `field_verified` is always false at discovery.

------------------------------------------------------------
# 5. ORGANIZATIONAL METADATA

```yaml
organizational:
  ownership_raw:        # string, optional
  governance_raw:       # string, optional
  partner_agencies_raw: # string, optional
  coordination_raw:     # string, optional
```

Rules:

- All organizational fields must be preserved exactly as discovered.
- No normalization, no inference, and no deduplication are permitted.
- `ownership_raw` represents legal title only.
- `governance_raw` represents operational control only. Must contain only the
  managing organization's name — never GIS park type labels or tier labels.
- `partner_agencies_raw` represents formal, documented co-operator organizations.
- `coordination_raw` represents informal, community-based, or volunteer partners.
- `partner_agencies_raw` must not duplicate `ownership_raw` or `governance_raw`.
- All organizational fields may appear for any entity type if discovered.
- Conflicts must be recorded in the Conflict Metadata block (§10).
- Organizational fields must never be inferred from context, logos, or implied
  relationships.

------------------------------------------------------------
# 6. TIER METADATA

```yaml
tiers:
  discovered_in: []   # list of tier identifiers, required
  primary_tier:       # tier identifier, required
```

Rules:

- `discovered_in` lists all tiers where the entity appeared.
- `primary_tier` is the lowest-numbered tier where the entity was discovered.
- Tier-0 Baseline uses `"baseline"` as its identifier.
- Tier metadata must reflect the actual discovery workflow, not inferred or
  corrected values.

------------------------------------------------------------
# 7. SOURCE METADATA

```yaml
sources:
  urls: []        # list of URLs, required if available
  datasets: []    # list of dataset names, optional
  documents: []   # list of document filenames from source_documents/, optional
  gis_layers: []  # list of GIS layer names or identifiers, optional
```

Rules:

- All sources must be preserved exactly as discovered.
- No source may be discarded.
- URLs must be stored exactly as discovered — no normalization, no tracking
  parameter removal.
- `documents` lists filenames of downloaded source documents logged in
  `{county}_document_log.yaml` (the Document Collection System). Reference
  the filename only — the document log carries full provenance (URL, date,
  type, description). If a document was the source of entity data, list it
  here.
- GIS layers must be recorded if used. Include the layer name or dataset
  identifier (e.g., MORPC Hub layer ID, ODNR Lake Map ArcGIS Experience ID).
- Dataset and document names must be preserved exactly as encountered.

------------------------------------------------------------
# 8. PROVENANCE METADATA

```yaml
provenance:
  extraction_method:  # string, required — see allowed values below
  source_detail:      # string, optional — specific URL, filename, or endpoint used
  harvested_at:       # timestamp, required — ISO 8601
  discovery_run_id:   # string, required — unique identifier for this discovery run
  discovery_path: []  # list of URLs, required — ordered chain leading to this entity
  parent_url:         # string, optional — URL from which this entity was recursively found
```

### Allowed `extraction_method` values

- `"agency_website"` — information read from an official agency or organization
  website; the primary discovery method for most entities. Use for any standard
  web page that does not require browser interaction to render its content.

- `"browser"` — Claude in Chrome was used to navigate a JavaScript-rendered page,
  ArcGIS Experience viewer, interactive GIS portal, county AuditorMap, or any
  other source requiring browser interaction. Use when the data is not accessible
  via a simple web fetch.

- `"gis_download"` — entity data or coordinates extracted from a downloaded GIS
  dataset. Examples: MORPC Parks & Open Space layer, ODNR Ohio Lake Map Resource,
  SORP parcel CSV, county GIS shapefile export. The dataset name should appear
  in `sources.gis_layers` or `sources.datasets`.

- `"document"` — entity data extracted from a downloaded document: PDF map,
  park brochure, management plan, GPX/KML file, trail guide, or similar. The
  document filename should appear in `sources.documents` and in the county
  document log.

- `"baseline"` — entity seeded from the Tier-0 county baseline spreadsheet.
  `parent_url` must be blank for baseline entities.

- `"human_assist"` — the user provided information directly: a coordinate pair,
  a source page URL, a name confirmation, or other data that automated methods
  could not resolve. Record what the user provided in `source_detail`.

Rules:

- `extraction_method` must reflect the actual method used, not an inferred or
  corrected value.
- `source_detail` records the specific URL, file path, or endpoint used — the
  precise source within the broader method category.
- `harvested_at` must reflect the actual timestamp of extraction.
- `discovery_run_id` must uniquely identify the discovery run.
- `discovery_path` records the full ordered chain of URLs that led to the entity.
  No URL may be removed, normalized, or rewritten.
- `parent_url` records the URL from which this entity was discovered during
  recursive propagation. Blank for directly enumerated entities and for baseline
  seeds.

------------------------------------------------------------
# 9. LINEAGE METADATA

```yaml
lineage:
  parent_entity_id:   # string or null — raw identifier of entity that spawned this discovery
  parent_entity_type: # string or null — one of four v6.x entity types
  lineage_notes:      # string, optional
```

Rules:

- Lineage metadata records the discovery hierarchy — which entity's page or
  document led to the discovery of this entity during recursive propagation.
- `parent_entity_id` must reference the raw identifier discovered during
  extraction, not the normalized entity ID assigned by the upsert engine.
- `parent_entity_type` must be one of: `Site`, `Trailthing`, `Site Network`,
  `Access Point`.
- `lineage_notes` may record ambiguous or conflicting lineage information.
- Lineage must not be inferred from URL structure alone.
- Lineage must not be inferred from naming conventions.
- Lineage must not be inferred from GIS boundaries.
- **Trailthing multi-parent detail** (parent Trailthing, Site parent, Site Network
  parent) is captured in the raw fields (`parent_id_raw`, `site_parent_raw`,
  `parent_site_network_raw`) — not here. Lineage metadata records the discovery
  chain, not the full entity parent model.

------------------------------------------------------------
# 10. CONFLICT METADATA

```yaml
conflicts:
  name_conflicts: []
  counties_conflicts: []
  category_conflicts: []
  subtype_conflicts: []
  designation_conflicts: []
  status_conflicts: []
  ownership_conflicts: []
  governance_conflicts: []
  partner_agencies_conflicts: []
  coordination_conflicts: []
  acres_conflicts: []
  gps_conflicts: []
  features_conflicts: []
  source_term_conflicts: []
  url_conflicts: []
  notes_conflicts: []
```

Rules:

- All conflicts must be preserved exactly as discovered.
- No conflict may be resolved during discovery.
- Conflicts must be recorded even if values differ only in punctuation or
  formatting.
- `gps_conflicts` must record coordinate pairs exactly as discovered.
- `partner_agencies_conflicts` must record all conflicting lists, even if
  differences are minor.
- `source_term_conflicts` records cases where different authoritative sources
  use different terms to describe the same Trailthing entity.
- Conflicts must not be deduplicated or normalized.

------------------------------------------------------------
# 11. UNCERTAINTY METADATA

```yaml
uncertainty:
  missing_fields: []       # fields expected for entity type but not discovered
  ambiguous_fields: []     # fields with unclear or contradictory values
  partial_fields: []       # fields where extraction was incomplete
  extraction_warnings: []  # issues encountered during extraction
```

Rules:

- `missing_fields` lists fields expected for the entity type but not discovered.
- `ambiguous_fields` lists fields with unclear or contradictory values.
- `partial_fields` lists fields where extraction was incomplete.
- `extraction_warnings` records any issues encountered during extraction.
- Uncertainty metadata must not be inferred or corrected.
- Uncertainty metadata must be preserved exactly as generated by the extraction
  process.

------------------------------------------------------------
# 12. PARENT METADATA (ACCESS POINTS ONLY)

```yaml
parent:
  parent_sites_raw: []         # list of site names — Sites that are identity parents
  parent_trailthings_raw: []   # list of Trailthing names — Trailthings that are identity parents
  parent_site_conflicts: []    # conflicting parent site names
  parent_trailthing_conflicts: [] # conflicting parent Trailthing names
```

Rules:

- `parent_sites_raw` must be preserved exactly as discovered. Lists all Sites
  documented as identity parents of this Access Point.
- `parent_trailthings_raw` must be preserved exactly as discovered. Lists all
  Trailthings documented as identity parents of this Access Point.
- An Access Point must have at least one parent — either a Site, a Trailthing,
  or both. An AP with neither is an identity error.
- `parent_site_conflicts` and `parent_trailthing_conflicts` must record all
  conflicting parent names across sources.
- No inference of parent entity is permitted.
- No GIS-based inference is permitted.
- No inference from URL structure is permitted.

------------------------------------------------------------
# 13. BASELINE METADATA

```yaml
baseline:
  seeded_from_baseline: # boolean, required
  baseline_id:          # string, optional — row identifier from baseline spreadsheet
  baseline_notes:       # string, optional — discrepancies between baseline and discovery
```

Rules:

- `seeded_from_baseline` indicates whether the entity originated from Tier-0
  Baseline.
- `baseline_id` must reference the baseline identifier exactly as stored in the
  baseline dataset.
- `baseline_notes` may record discrepancies between baseline and discovered values.
- Baseline values must never override authoritative discovery values.
- Baseline metadata must be preserved even when discovery provides more complete
  information.
- Baseline trail-type entries seed as Trailthings per County Baseline Module
  v6.x §7.8.

------------------------------------------------------------
# 14. NOTES

```yaml
notes:
  general_notes:    # string, optional
  extraction_notes: # string, optional
  review_notes:     # string, optional
```

Rules:

- `notes` fields may contain any additional information relevant to the discovery
  process.
- `general_notes` may include contextual information not captured elsewhere.
- `extraction_notes` may include tool-level or parser-level observations.
- `review_notes` may include human review comments.
- Notes must never override or reinterpret raw fields or metadata fields.

------------------------------------------------------------
# 15. RAW FIELD PRESERVATION RULES

Raw Field Preservation Rules define how all raw fields must be handled during
discovery. Rules apply to all entity types unless explicitly restricted.

General rules:

- All raw fields must be preserved exactly as discovered.
- No normalization, inference, correction, or vocabulary matching is permitted.
- Malformed values must be preserved.
- Missing values must remain blank.
- Conflicts must be recorded in Conflict Metadata (§10).
- GIS-derived fields (`township_raw`, `municipality_raw`) must remain blank
  during discovery.
- Raw fields must appear in the Raw Discovery Record even if blank.

------------------------------------------------------------
## 15.1 SITE RAW FIELDS (ALPHABETICAL)

### `access_notes_raw`
- Preserve exactly as discovered.
- Captures seasonal restrictions, permit requirements, hours, and access caveats.
- Must not contain narrative description — that belongs in `description_raw`.

### `acres_raw`
- Preserve exactly as discovered.
- No unit conversion or numeric normalization.
- Malformed values must be preserved.

### `boundary_document_raw`
- Filename (relative to `source_documents/`) of a downloaded boundary file for
  this entity (shapefile, KMZ, GeoJSON, georeferenced PDF, etc.).
- Blank if no boundary document was downloaded.
- Must not be populated with a URL — only the local filename.
- The document log entry in `{county}_document_log.yaml` carries full provenance.

### `category_raw`
- Preserve exactly as discovered.
- No vocabulary matching during discovery.

### `coordination_raw`
- Preserve exactly as discovered.

### `counties_raw`
- Preserve exactly as discovered.
- No alphabetical sorting during discovery.
- No normalization of county names.

### `description_raw`
- Preserve exactly as discovered.
- Must be narrative prose — not an amenity list.
- No summarization or rewriting.

### `designation_raw`
- Preserve exactly as discovered.
- No vocabulary matching.

### `features_raw`
- Preserve exactly as discovered.
- Must be an amenity list (bullets, icons, facilities) — not narrative sentences.
- No categorization or vocabulary matching.

### `governance_raw`
- Preserve exactly as discovered.
- Must represent operational control only.
- Must not contain GIS park type labels or tier labels.

### `gps_lat_raw`
- May be populated only when explicitly provided by an authoritative source.
- No inference or derivation.

### `gps_lon_raw`
- Same rules as `gps_lat_raw`.

### `habitat_type_raw`
- Preserve exactly as discovered.
- Captures ecological or natural character language from the source.
- No normalization — open vocabulary in v6.x.
- Must not contain amenity or governance content.

### `identity_notes_raw`
- Preserve exactly as discovered.
- Use for: identity flags, disambiguation notes, cross-tier notes,
  CROSS_COUNTY_CANDIDATE, child site relationship notes.

### `location_raw`
- Preserve exactly as discovered.
- No GIS substitution or inference.

### `name_raw`
- Preserve exactly as discovered.
- No title-case correction or punctuation normalization.

### `ownership_raw`
- Preserve exactly as discovered.
- Must represent legal title only.

### `partner_agencies_raw`
- Preserve exactly as discovered.
- Must represent formal, documented co-operators.
- Must not duplicate `ownership_raw` or `governance_raw`.

### `status_raw`
- Preserve exactly as discovered.
- No vocabulary matching.

### `subtype_raw`
- Preserve exactly as discovered.
- No vocabulary matching.

### `url_primary_raw`
- Preserve exactly as discovered.
- No removal of tracking parameters.

### `urls_raw`
- Preserve exactly as discovered.
- Order must not be changed.

### `ebird_hotspot_id`
- Sites only. Optional. Blank if no eBird hotspot exists for this site.
- Format: eBird L-code — `L` followed by digits (e.g., `L123456`).
- Captured at discovery time; not normalized — pass through verbatim.
- Check on [ebird.org/explore](https://ebird.org/explore) by site name or GPS location.
- Do not populate with personal eBird location IDs — only official shared hotspots.

------------------------------------------------------------
## 15.2 TRAILTHING RAW FIELDS (ALPHABETICAL)

### `accessibility_raw`
- Preserve exactly as discovered.
- Populate only when explicitly stated by an authoritative source.

### `coordination_raw`
- Preserve exactly as discovered.

### `counties_raw`
- Preserve exactly as discovered.
- No alphabetical sorting or normalization.

### `description_raw`
- Preserve exactly as discovered.
- Priority: physical and ecological character — not amenity inventory.
- No summarization or rewriting.

### `difficulty_raw`
- Populate only when explicitly stated by an authoritative source.
- No inference from surface type or use type.

### `governance_raw`
- Preserve exactly as discovered.

### `identity_notes_raw`
- Preserve exactly as discovered.
- Use for: TRAIL_HIERARCHY_UNCERTAIN, PARTIAL MEMBERSHIP, and other flags.

### `maps_raw`
- Preserve exactly as discovered.
- Semicolon-delimited URL list.

### `member_trailthing_names_raw`
- Preserve exactly as discovered.
- Records names of member Trailthings when this entity is a container.

### `name_raw`
- Preserve exactly as discovered.

### `org_type_raw`
- Preserve exactly as discovered.
- No vocabulary matching.

### `origin_type_raw`
- Preserve exactly as discovered.
- No vocabulary matching.

### `ownership_raw`
- Preserve exactly as discovered.

### `parent_id_raw`
- Preserve exactly as discovered.
- The name or raw ID of the parent Trailthing when the source explicitly frames
  this entity as a component of another Trailthing.
- Must not be inferred.

### `parent_site_network_raw`
- Preserve exactly as discovered.
- The name of the parent Site Network when the source explicitly frames this
  Trailthing as a member of a Site Network.
- Must not be inferred.

### `partner_agencies_raw`
- Preserve exactly as discovered.

### `site_parent_raw`
- Preserve exactly as discovered.
- The name of the containing Site when the source explicitly frames this
  Trailthing as contained within and access-dependent on a specific Site.
- Must not be inferred from proximity or governance.

### `source_hierarchy_context_raw`
- Preserve exactly as discovered (verbatim or close paraphrase from source).
- Blank if the source provides no hierarchical context.

### `source_term_raw`
- Preserve verbatim from source. Required — do not invent a term.
- The exact word or phrase the source uses to describe what kind of entity
  this is ("trail system," "greenway," "water trail," "connector," etc.).

### `states_included_raw`
- Preserve exactly as discovered.
- Blank for Ohio-only Trailthings.

### `status_raw`
- Preserve exactly as discovered.
- No vocabulary matching.

### `total_length_raw`
- Preserve exactly as discovered.
- No unit conversion.

### `trail_history_raw`
- Preserve exactly as discovered.

### `url_primary_raw`
- Preserve exactly as discovered.

### `urls_raw`
- Preserve exactly as discovered.

### `use_type_raw`
- Preserve exactly as discovered.
- No vocabulary matching.

------------------------------------------------------------
## 15.3 SITE NETWORK RAW FIELDS (ALPHABETICAL)

### `coordination_raw`
- Preserve exactly as discovered.

### `counties_raw`
- Preserve exactly as discovered.

### `description_raw`
- Preserve exactly as discovered.
- Priority: character and mission — not site-level details.

### `governance_raw`
- Preserve exactly as discovered.

### `identity_notes_raw`
- Preserve exactly as discovered.
- Use for: SITE_NETWORK_PROVISIONAL, SITE_NETWORK_UNCERTAIN flags.

### `member_count_raw`
- Preserve exactly as discovered.
- No normalization.

### `member_site_names_raw`
- Preserve exactly as discovered.
- List of member site names if provided by the source.

### `name_raw`
- Preserve exactly as discovered.

### `network_type_raw`
- Preserve exactly as discovered.
- No vocabulary matching.

### `org_type_raw`
- Preserve exactly as discovered.
- No vocabulary matching.

### `ownership_raw`
- Preserve exactly as discovered.

### `partner_agencies_raw`
- Preserve exactly as discovered.

### `states_included_raw`
- Preserve exactly as discovered.

### `status_raw`
- Preserve exactly as discovered.

### `url_primary_raw`
- Preserve exactly as discovered.

### `urls_raw`
- Preserve exactly as discovered.

------------------------------------------------------------
## 15.4 ACCESS POINT RAW FIELDS (ALPHABETICAL)

### `accessibility_raw`
- Preserve exactly as discovered.

### `counties_raw`
- Preserve exactly as discovered.
- Access Points resolve to a single primary county — but preserve multi-county
  raw values if discovered.

### `description_raw`
- Preserve exactly as discovered.
- Operational access detail — not narrative about the parent entity.

### `features_raw`
- Preserve exactly as discovered.
- Amenity list for the access point itself.

### `governance_raw`
- Preserve exactly as discovered.

### `gps_lat_raw`
- May be populated only when explicitly provided by an authoritative source.

### `gps_lon_raw`
- Same rules as `gps_lat_raw`.

### `identity_notes_raw`
- Preserve exactly as discovered.
- Use for: RECLASSIFICATION_CANDIDATE flag (IMP-114), disambiguation notes.

### `location_raw`
- Preserve exactly as discovered.

### `name_raw`
- Preserve exactly as discovered.

### `parent_sites_raw`
- Preserve exactly as discovered.
- List of Site names that are identity parents of this Access Point.

### `parent_trailthings_raw`
- Preserve exactly as discovered.
- List of Trailthing names that are identity parents of this Access Point.

### `status_raw`
- Preserve exactly as discovered.

### `url_primary_raw`
- Preserve exactly as discovered.

### `urls_raw`
- Preserve exactly as discovered.

------------------------------------------------------------
# 16. COMPLETE METADATA OBJECT (TEMPLATE)

```yaml
metadata:
  identity:
    name_raw:
    entity_type:                    # Site | Trailthing | Site Network | Access Point
    counties_raw: []
    township_raw:                   # BLANK — GIS-derived only
    municipality_raw:               # BLANK — GIS-derived only
    parent_site_raw:                # child Sites only
    category_raw:                   # Sites only
    subtype_raw:                    # Sites only
    designation_raw:                # Sites only
    status_raw:
    description_raw:
    location_raw:                   # Sites and Access Points
    acres_raw:                      # Sites only
    habitat_type_raw:               # Sites only
    access_notes_raw:               # Sites only
    boundary_document_raw:          # Sites only; filename in source_documents/
    gps_lat_raw:
    gps_lon_raw:
    features_raw:                   # Sites and Access Points
    source_term_raw:                # Trailthings — REQUIRED
    source_hierarchy_context_raw:   # Trailthings only
    difficulty_raw:                 # Trailthings only
    accessibility_raw:              # Trailthings only
    url_primary_raw:
    urls_raw: []
    ebird_hotspot_id:              # Sites only; eBird L-code if hotspot exists
    identity_notes_raw:
    last_verified_date:
    field_verified:

  organizational:
    ownership_raw:
    governance_raw:
    partner_agencies_raw:
    coordination_raw:

  tiers:
    discovered_in: []
    primary_tier:

  sources:
    urls: []
    datasets: []
    documents: []
    gis_layers: []

  provenance:
    extraction_method:              # agency_website | browser | gis_download | document | baseline | human_assist
    source_detail:
    harvested_at:
    discovery_run_id:
    discovery_path: []
    parent_url:

  lineage:
    parent_entity_id:
    parent_entity_type:             # Site | Trailthing | Site Network | Access Point
    lineage_notes:

  conflicts:
    name_conflicts: []
    counties_conflicts: []
    category_conflicts: []
    subtype_conflicts: []
    designation_conflicts: []
    status_conflicts: []
    ownership_conflicts: []
    governance_conflicts: []
    partner_agencies_conflicts: []
    coordination_conflicts: []
    acres_conflicts: []
    gps_conflicts: []
    features_conflicts: []
    source_term_conflicts: []
    url_conflicts: []
    notes_conflicts: []

  uncertainty:
    missing_fields: []
    ambiguous_fields: []
    partial_fields: []
    extraction_warnings: []

  parent:                           # Access Points only
    parent_sites_raw: []
    parent_trailthings_raw: []
    parent_site_conflicts: []
    parent_trailthing_conflicts: []

  baseline:
    seeded_from_baseline:
    baseline_id:
    baseline_notes:

  notes:
    general_notes:
    extraction_notes:
    review_notes:
```

------------------------------------------------------------
# 17. INTEGRATION POINTS

This module integrates with:

- Discovery Protocol Module v6.x
- Discovery Orchestration Module v6.x
- All Tier Sub-Procedures v6.x
- All Entity Discovery Sub-Procedures v6.x
- Resolution Engine v6.x
- Normalization Engine v6.x
- Audit & Logging Module v6.x

Metadata must be passed unchanged through all downstream modules until Resolution.

------------------------------------------------------------
# 18. MODULE DEPENDENCIES

This module depends on:

- Site Schema Module v6.0
- Trailthing Schema Module v6.0
- Site Network Schema Module v6.0
- Access Point Schema Module v6.0
- All Entity Discovery Sub-Procedures v6.x
- Discovery Protocol Module v6.x
- Discovery Orchestration Module v6.x
- Resolution Engine v6.x
- Normalization Engine v6.x
- Audit & Logging Module v6.x

------------------------------------------------------------
# END OF DISCOVERY METADATA SPECIFICATION v6.0
