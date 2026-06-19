# NATURAL AREAS PROJECT
# MODULE MANIFEST v6.0
(Authoritative Inventory, Structure, and Cross-Module Dependencies
for the v6.x Architecture)

This manifest defines the authoritative module inventory, directory
structure, and dependency graph for the Natural Areas Project v6.x
architecture.

The manifest is authoritative for:
- Module presence
- Module purpose
- Module location
- Current version of every module
- Cross-module dependencies
- Repository structure

The manifest lists the **current canonical filename** (including specific version
number) for each module. Update the manifest whenever a module is versioned up.

## Versioning and Reference Convention (IMP-109)

- **Filenames** include the version number: `na_module_name_v6.N.md`
- **Document internal headers** include the version number
- **Inter-module and intra-module references** use the bare document title
  only — no version suffix. Example: `na_resolution_engine.md §5`, never
  `na_resolution_engine_v6.x.md §5`. Section citations follow the same rule.
- **This manifest** is the single authoritative source for current version
  numbers. When a module is versioned up, update this manifest. No other
  documents require changes to their cross-references.

## About the v6.x Architecture

v6.x is an incremental refactor of v5.x. Documents are added here as they
are revised. Until a v5.x document is superseded by a v6.x equivalent, the
v5.x version in the Natural Areas Project v5 folder remains authoritative
for that module.

**Do not mix v5 and v6 document paths within a single county run.** When
beginning a new county under v6.x, confirm with the manifest which modules
have v6.x equivalents and read those; fall back to v5.x only for modules
not yet revised.

------------------------------------------------------------
# CHANGELOG

v6.0 (2026-05-31 update #29):
- na_discovery_protocol_v6.0.md added:
  - Supersedes Discovery Protocol Module v5.9
  - Entity types: 6 → 4; §4.2–4.4 (Trail, Trail Segment, Trail Network) →
    §4.2 Trailthing; §4.5 Site Network → §4.3; §4.6 AP → §4.4
  - §7 entity sub-procedure list updated to 4 entity + 8 tier sub-procedures v6.0;
    entity type sequence (Sites → Trailthings → Site Networks → APs) added
  - §8 Cross-Entity Relationships updated: Trailthing triple-parent (parent
    Trailthing, parent Site, external parent); AP parents = Sites + Trailthings
  - §18 Cross-Tier Trail → Cross-Tier Trailthing; scope extended to all Trailthings
  - §19a Trailthing No-Classification Mandate added (IMP-009): discoverers never
    classify as trail vs. trail network vs. trail segment; source_term_raw
    REQUIRED; variation goes in notes_raw not new records
  - §24 Map and Asset File Preservation replaced with reference to Document
    Collection System (Discovery Orchestration Module v6.0 §4)
  - §11 What Discovery Must Never Do: no-classification mandate added
  - All v5.9 rules carried forward: IMP-013, IMP-014, IMP-015, IMP-016, IMP-022,
    IMP-024, IMP-025, IMP-001, IMP-006, IMP-008, IMP-011/018

v6.0 (2026-05-31 update #28):
- na_audit_and_logging_v6.0.md added:
  - Supersedes Audit & Logging Module v5.1
  - Entity types: 6 → 4 throughout
  - Derived Label removed throughout (was retired in v5.x but still referenced)
  - §3.11 Document Collection Log added: tracks downloaded documents,
    {county}_document_log.yaml, download failures, URL-only entries
  - §3.9 Normalization Log updated: source_term_raw verbatim pass-through,
    habitat_type/access_notes/last_verified_date/field_verified entries, cross-entity
    reference pairing validation, Trailthing parent resolution outcomes
  - §3.10 Delimiter-Integrity Log updated: v6.0 delimiter counts, pairing anomaly,
    source_term blank warning, member list count mismatch
  - §3.1 Run Metadata updated to v6.0 module list (4 schemas/vocab/contracts/specs)
  - §4.15 added (Document Collection Must Be Logged)
  - §4.16 added (Cross-Entity Reference Pairings Must Be Validated)
  - §5 User Surfacing updated: vocabulary expansion candidates, document collection
    summary, pairing anomalies added
  - §6.5 added: document log is cumulative county artifact
  - §10 Visit Planning Query Template added (IMP-018): 6 SQL queries covering
    field verification candidates, GPS-missing entities, staleness threshold
    filter, RECLASSIFICATION_CANDIDATE flag, combined priority list

v6.0 (2026-06-01 update #38):
- na_site_schema_v6.0.md updated:
  - §3.31 eBird Hotspot ID added (IMP-021): optional text field; eBird L-code format;
    enables linking Site records to eBird sighting data in external systems
  - Field count: 30 → 31
- na_tsv_output_site_v6.0.md updated:
  - Field 31 ebird_hotspot_id added; field count 30 → 31; tab delimiters 29 → 30
- na_tsv_integrity_check_v6.0.md updated:
  - Site field count and delimiter counts updated to 31/30 throughout
- Raw discovery record templates updated (CLAUDE.md, na-discovery skill, na-bootstrap skill)
- Count references updated: na-entities skill, na-pipeline skill, na-quality skill,
  processing orchestration, audit module, CONTRIBUTING_v6.0.md

v6.0 (2026-05-31 update #37):
- na_entity_upsert_engine_v6.0.md added to /normalization:
  - Supersedes Entity Upsert Engine v5.2
  - Entity types: 6 → 4; trailthings table for v6.x entities; legacy trail
    tables retained for existing DB records with explicit note
  - Relationship tables: trailthing_hierarchy replaces trail_to_segment/
    trail_to_network/trail_parents for v6.x entities; legacy tables retained
  - parent_site_network_id replaces external_parent_id/external_parent_type (§6.4)
  - New Site fields: habitat_type, access_notes, last_verified_date, field_verified
  - Trailthing core table rules: source_term and source_hierarchy_context pass
    through verbatim; no GPS/Plus Code/township/municipality
  - Held entity child rule (§8.3): Trailthing parent_id holds added; Site Network
    exempt from automatic hold (unresolved_member_ids is explicit, not automatic)
  - AP parent types: Site + Trailthing only (Trail/Trail Segment removed)
  - All eight canonical hold_reason values documented in §8.2 table
  - §13 DDL table groups: all four groups documented; legacy tables noted
  - run_metadata INSERT columns documented (IMP-101): state must be full name;
    resolution_provenance uses resolution_run not resolution_action
  - All v5.2 core logic carried forward

v6.0 (2026-05-31 update #36):
- na_resolution_rules_v6.0.md added to /processing:
  - Supersedes Resolution Rules Module v5.3
  - Entity types: 6 → 4; Trailthing replaces Trail/Trail Segment/Trail Network
  - §4.12 Trailthing Classification Prohibition added: Resolution Engine must
    not classify Trailthings as trail/segment/network; source_term passes through
    verbatim (IMP-007)
  - §5.2 Trailthing identity anchor: single anchor (name + county) replaces three
    separate trail/segment/network anchors; no GPS proximity component
  - §5.3 AP identity anchor: GPS proximity bucket removed; anchor is now parent
    entity ID + name + county; IMP-019 AP deduplication audit added to tracker
  - §6.2 Trailthing identity signature: source term similarity added as weighted
    component (15 points); informs future classification, not a blocking criterion
  - §6.3 AP identity signature: GPS distance removed; parent match weight raised
    to 50; name similarity raised to 30
  - §10 Trailthing rules section added: no-classification mandate, source term
    not identity, hierarchy rules, variation-in-notes rule, Trailthings-not-Sites
  - §11 Network rules simplified: Trail Network rules removed; Site Network rules
    retained with threshold rule reference
  - §13.4 Sequence gaps rule added (IMP-117)
  - Discovery Output Specification reference removed (module retired in v6)
  - All v5.3 core identity principles carried forward
- IMP-019 added to improvement tracker: AP deduplication audit after 10 v6
  county runs to verify GPS proximity removal does not allow duplicates through

v6.0 (2026-05-31 update #35):
- na_cross_county_resolution_v6.0.md added to /processing:
  - Supersedes Cross-County Resolution Protocol v5.2
  - Entity types updated: T/TS/TN → TT (Trailthing) throughout; SQL queries
    updated to trailthings table for v6.x entities
  - Legacy type codes (T, TR, TS, TN, SI) retained with explanation: coexistence
    with TT is intentional pending Trailthing experiment reclassification (IMP-007)
  - Relationship table updates split: trailthing_hierarchy for v6.x entities;
    legacy trail tables for existing DB entities
  - Migration history removed from module — moved to na_db_migration_log.md
  - Held entity snapshot removed — DB is authoritative; bootstrap query surfaces it
  - IMP-117 sequence gap note added to anti-patterns
  - All v5.2 core protocol rules carried forward unchanged
- na_db_migration_log.md added to project root:
  - Historical record of IMP-104 and IMP-107 DB migrations
  - Specific entity migration tables and records
  - Category 2 deletion rule documentation
  - Held entity snapshot (dated 2026-05-12, noted as stale)
  - Not a rules or protocol document — historical record only

v6.0 (2026-05-31 update #34):
- na_discovery_output_spec: NOT carried forward to v6.x — retired.
  Rationale: all four entity types have complete raw discovery record templates
  in their own entity discovery sub-procedures. Raw value rules are stated in
  the Discovery Protocol Module. The output spec was redundant. All v6 module
  references updated to point to Discovery Metadata Specification v6.0 or the
  entity sub-procedures directly.

v6.0 (2026-05-31 update #33):
- na_discovery_metadata_spec_v6.0.md added to /discovery:
  - Supersedes Discovery Metadata Specification v5.3
  - Entity types: 6 → 4 throughout; entity_type allowed values updated
  - Boundary metadata block dropped; replaced with boundary_document_raw on Site
    raw record — presence = boundary document captured; blank = none found
  - Document collection added to Source Metadata §7 as named source type
    referencing {county}_document_log.yaml
  - Extraction method values renamed to describe tool/method used: agency_website,
    browser, gis_download, document, baseline, human_assist
  - AP Parent Metadata expanded: parent_sites_raw + parent_trailthings_raw
    (v5 had only parent_site_raw)
  - Lineage retained as single parent pointer; Trailthing multi-parent detail
    lives in raw fields
  - §15 raw field preservation: all four entity types now complete (v5 had
    Trail/Trail Segment/Trail Network/Site Network/AP all marked "pending")
  - New Site raw fields: habitat_type_raw, access_notes_raw, boundary_document_raw
  - New Trailthing raw fields: source_term_raw, source_hierarchy_context_raw,
    parent_id_raw, site_parent_raw, parent_site_network_raw, member_trailthing_names_raw
  - parent_site_network_raw replaces external_parent_raw/external_parent_type_raw
    throughout (consistent with rename in all other v6 modules)
  - Complete metadata template updated for all changes

v6.0 (2026-05-31 update #32):
- na_processing_orchestration_v6.0.md added to /processing:
  - Supersedes Processing Orchestration Module v5.5
  - Entity types: 6 → 4 throughout; TSV output: 6 files → 4 files
  - Resolution Pass 2 eliminated: single resolution pass; GPS has no identity
    feedback loop in v6.x
  - Two GPS gates (v5.5 Stage 5.5a/5.5b) collapsed into single GPS Gate (Stage 4c)
    covering Sites and APs; Trailthings and Site Networks not gated
  - GPS Acquisition (Stage 4b): single pass all entity types; browser and human
    assist named as primary methods; ranked method list documented
  - Stage 8 upsert: DDL table groups updated (trailthings replaces trail/trail_segment/
    trail_network; trailthing_hierarchy replaces trail_to_segment/trail_network_members)
  - Stage 9 relationship validation: updated for Trailthing hierarchy and cross-entity
    parent relationships
  - IMP-PENDING added: skill label cross-reference column retained but flagged for
    validation against na-pipeline skill after v6.x skills are finalized
  - IMP-106 pipeline coding conventions carried forward unchanged
  - All v5.5 core principles carried forward

v6.0 (2026-05-31 update #31):
- na_county_baseline_v6.0.md added to /processing:
  - Supersedes County Baseline Module v5.1
  - §3 entity types updated to four v6.x types; trail-type entries noted as Trailthings
  - §7.8 Trailthing seeding rule added: all trail-type baseline rows seed as Trailthings;
    source_term populated from authoritative source at discovery, not from baseline row
  - §9 Unconfirmed Baseline Seeds: hold_reason = "unconfirmed_baseline_seed" formally
    documented with definition, hold behavior, required documentation, three resolution
    paths, and prohibition on using as a substitute for discovery work
  - §8 pipeline integration updated: single-pass GPS acquisition, Resolution Pass 2
    eliminated, references updated to v6.x
  - All v5.1 rules carried forward: baseline origin, structure, field interpretation,
    multi-county rules, identity rules, conflict rules, metadata requirements
  - Module dependencies updated to v6.0

v6.0 (2026-05-31 update #30):
- na_child_site_rules_v6.0.md added to /processing:
  - Supersedes Child Site Rules Module v5.4
  - §4 Trailthing Prohibition added: trail-related entities are always Trailthings,
    never child Sites, regardless of location, governance, or naming
  - §5 Relationship Boundary Table added: distinguishes child site (parent_site_id),
    Trailthing-in-Site (site_parent_id), and Site Network membership — mutually
    exclusive patterns governed by separate modules
  - §6 Child Site capabilities clarified: a child Site is a full Site entity with
    its own Trailthings, child Sites, APs, and Site Network memberships
  - All v5.4 rules carried forward: identity rules, evidence requirements, boundary
    rules, county inheritance, multi-level hierarchy, circularity, discovery and
    normalization rules
  - Module dependencies updated to v6.0

v6.0 (2026-05-31 update #27):
- na_resolution_engine_v6.0.md added:
  - Supersedes Resolution Engine v5.5
  - Entity types: 6 → 4 (Trail/Trail Segment/Trail Network → Trailthing)
  - §9.5 Field Model: Trailthing fields (source_term_raw REQUIRED, parent_id_raw,
    site_parent_raw, parent_site_network_raw, member_trailthing_names_raw);
    Site new fields (habitat_type_raw, access_notes_raw); AP new field
    (parent_trailthings_raw replaces parent_trails_raw + parent_trail_segments_raw)
  - §11.3 Field Strategy Assignment: full Trailthing strategy table;
    last_verified_date (choose — most recent), field_verified (choose — true if any)
  - §11.8 renamed Cross-Tier Trailthing Canonicalization; scope extended from
    Trail-only to all Trailthings; source_term_raw conflict triggers review set
  - §12.3 Parent Resolution: Trailthing triple-parent (parent Trailthing, Site,
    external); AP dual-parent (Sites + Trailthings)
  - §12.6 Resolved Entity Structure: entity_type is one of four; entity-specific
    payloads documented for all four types
  - Design Principle 4.8 added: no classification of Trailthings
  - All v5.5 five-phase pipeline structure carried forward

v6.0 (2026-05-31 update #26):
- na_tsv_integrity_check_v6.0.md added:
  - Supersedes TSV Integrity Check Module v5.3
  - Entity types reduced from six to four: Trail/Trail Segment/Trail Network
    sections removed; §6.3 Trailthing added
  - Field counts updated: Site 25→30/29tabs, Trailthing 32/31tabs (new),
    Site Network 15→18/17tabs, Access Point 17→20/19tabs
  - §6a Cross-entity reference pairing validation added: every ID field must
    be paired with a name field; mismatch is an integrity failure; member list
    count parity rule for Site Network
  - Step 6a added to validation algorithm; Step 11a added for v6 new fields
    (last_verified_date format, field_verified boolean, source_term blank warn,
    parent_site_network_id / parent_site_network_name pairing)
  - Provenance field exclusion (§7a, IMP-030) field counts updated
  - Access Point County single-value rule added to §7 error conditions
  - All v5.3 rules carried forward

v6.0 (2026-05-31 update #25):
- All four TSV output specs updated with cross-entity name pairing rule:
  every field that references another entity by ID is immediately followed
  by the referenced entity's human-readable name. TSV output must be
  human-readable without requiring ID lookups. Changes per spec:
  - na_tsv_output_site_v6.0.md: parent_site_name added (pos 28);
    field count 29 → 30; tab delimiters 28 → 29
  - na_tsv_output_trailthing_v6.0.md: parent_name (pos 6),
    site_parent_name (pos 8), parent_site_network_name (pos 10) added;
    field count 29 → 32; tab delimiters 28 → 31
  - na_tsv_output_site_network_v6.0.md: member_site_names (pos 13) added;
    field count 17 → 18; tab delimiters 16 → 17
  - na_tsv_output_access_point_v6.0.md: identity_parent_entity_name (pos 6)
    added; field count 19 → 20; tab delimiters 18 → 19

v6.0 (2026-05-31 update #24):
- na_tsv_output_access_point_v6.0.md added:
  - Supersedes Access Point TSV Output Specification v5.1
  - Identity Parent Entity Type: "Trail" and "Trail Segment" removed;
    "Trailthing" added
  - Both Identity Parent Entity ID and Name included (ID for joins; Name for
    human readability)
  - last_verified_date and field_verified added (IMP-013)
  - Field count: 17 → 19 (before name pairing update); final count 20

v6.0 (2026-05-31 update #23):
- na_tsv_output_site_network_v6.0.md added:
  - Supersedes Site Network TSV Output Specification v5.1
  - Org Type (position 3) added — was in v5 schema but absent from v5.1 TSV
  - Coordination (position 8) added (IMP-135)
  - member_site_names paired with member_site_ids (same-order parallel list)
  - SITE_NETWORK_PROVISIONAL flag preservation noted in Identity Notes field
  - Field count: 15 → 17 (before name pairing update); final count 18

v6.0 (2026-05-31 update #22):
- na_tsv_output_trailthing_v6.0.md added:
  - New specification — no v5 equivalent covers the unified Trailthing
  - Supersedes Trail v5.1, Trail Segment v5.1, Trail Network v5.1 (all retired)
  - source_term required (WARN if blank); source_hierarchy_context optional
  - parent_id/name, site_parent_id/name, parent_site_network_id/name pairs
  - Maps field serialization (semicolon-delimited URL list)
  - No GPS, Plus Code, township, or municipality (multi-location entity)
  - Field count: 32; tab delimiters: 31

v6.0 (2026-05-31 update #21):
- na_tsv_output_site_v6.0.md added:
  - Supersedes Site TSV Output Specification v5.2
  - Four new fields: habitat_type (pos 11), access_notes (pos 13),
    last_verified_date (pos 25), field_verified (pos 26)
  - parent_site_id / parent_site_name pair added
  - Field order updated to match Site Schema Module v6.0 canonical order
  - Field count: 30; tab delimiters: 29
  - site_id remains DB-only (excluded from TSV)

v6.0 (2026-05-31 update #21):
- na_access_point_normalization_v6.0.md added:
  - Supersedes Access Point Normalization Contract v5.3
  - parent_trails_raw + parent_trail_segments_raw → parent_trailthings_raw
  - Allowed identity parent types: Site + Trailthing (was Site + Trail + Trail Segment)
  - last_verified_date and field_verified normalization rules added (IMP-013)
  - IMP-014 notes provenance prohibition added to §5.16
  - Trail Schema and Trail Segment Schema dependencies removed; Trailthing Schema added
  - All v5.3 rules carried forward: IMP-114, IMP-100, IMP-084, GPS/GIS handling

v6.0 (2026-05-31 update #20):
- na_site_network_normalization_v6.0.md added:
  - Supersedes Site Network Normalization Contract v5.3
  - coordination_raw added to inputs; §5.6a Coordination added to field rules
  - IMP-014 notes provenance prohibition added to §5.13
  - IMP-015 description character and mission priority added to §5.11
  - SITE_NETWORK_PROVISIONAL flag preservation added (§10.8)
  - All v5.3 rules carried forward: IMP-105, IMP-102, IMP-100, empty string
    enforcement, member Site ID resolution, member count derivation

v6.0 (2026-05-31 update #19):
- na_trailthing_normalization_v6.0.md added:
  - New from scratch — no v5 equivalent covers Trailthing as unified type
  - Supersedes Trail Normalization v5.3, Trail Segment Normalization v5.1,
    Trail Network Normalization v5.2 (all retired for normalization purposes)
  - No-classification mandate: normalization never classifies as trail vs. trail
    network vs. trail segment
  - source_term_raw and source_hierarchy_context_raw: pass through verbatim (§5.2, §5.3)
  - use_type, surface_type, origin_type, status, difficulty: vocabulary (optional)
  - IMP-021 explicit use/surface fields; difficulty only from authoritative source
  - Parent Trailthing validation with hold on unresolved parent (§5.20)
  - Parent Site validation (warning-only, not blocking) (§5.21)
  - Member Trailthing name resolution (warning-only) (§5.22)
  - last_verified_date and field_verified (IMP-013) (§5.23, §5.24)
  - IMP-014 notes provenance prohibition
  - IMP-015 description ecological/physical character priority
  - No GPS, Plus Code, township, or municipality (multi-location entity)

v6.0 (2026-05-31 update #18):
- na_site_normalization_v6.0.md added:
  - Supersedes Site Normalization Contract v5.11
  - Four new fields: habitat_type (§5.22), access_notes (§5.23),
    last_verified_date (§5.24), field_verified (§5.25) — IMP-011, IMP-012, IMP-013
  - IMP-014 notes provenance prohibition added to §5.19
  - IMP-015 description ecological/physical character priority added to §5.10
  - All v5.11 rules carried forward: IMP-063–069, IMP-049–053, IMP-054–055,
    IMP-060–061, IMP-116

v6.0 (2026-05-31 update #17):
- na_normalization_engine_v6.0.md added:
  - Supersedes Normalization Engine v5.8
  - Entity type list updated: 6 types → 4 (Site, Trailthing, Site Network, AP)
  - §5.2–5.4 (Trails, Trail Segments, Trail Networks) consolidated into §5.2
    (Trailthings); §5.5 Site Networks renumbered §5.3; §5.6 APs renumbered §5.4
  - §4.7 County Normalization: multi-location entities updated to Trailthings +
    Site Networks
  - §4.10 Parent/Child Validation: AP allowed parents updated to Site + Trailthing;
    Trailthing self-referential parent hierarchy added
  - hold_reason unresolved_member_ids: scope updated from Trail Networks to Site
    Networks
  - All v5.8 cross-entity rules carried forward

v6.0 (2026-05-30 update #16):
- na_private_discovery_subproc_v6.0.md added:
  - Supersedes Private & Organization-Based Discovery Sub-Procedure v5.7
  - Entity type consolidation throughout: Trail/Trail Segment/Trail Network → Trailthing
  - §7.3–7.5 consolidated into §7.3 (Trailthing Creation)
  - Document collection §6.3 added
  - All v5.7 rules carried forward: IMP-111 (GNIS cemetery enumeration), IMP-110
    (All golf courses in scope), IMP-099, IMP-029, IMP-030, OBS-026, OBS-027,
    OBS-030, OBS-031

v6.0 (2026-05-30 update #15):
- na_conservancy_discovery_subproc_v6.0.md added:
  - Supersedes Conservancy & Land Trust Discovery Sub-Procedure v5.6
  - Entity type consolidation throughout: Trail/Trail Segment/Trail Network → Trailthing
  - §7.3–7.5 consolidated into §7.3 (Trailthing Creation)
  - Document collection §6.3 added
  - All v5.6 rules carried forward: IMP-134 (Cardinal Land Conservancy), IMP-130
    (Known Organizations inventory), IMP-029, IMP-030, OBS-024, OBS-025, URL-10

v6.0 (2026-05-30 update #14):
- na_municipal_discovery_subproc_v6.0.md added:
  - Supersedes Municipal Lands Discovery Sub-Procedure v5.12
  - Entity type consolidation throughout: Trail/Trail Segment/Trail Network → Trailthing
  - §8.3–8.5 consolidated into §8.3 (Trailthing Creation)
  - Document collection §7.3 added
  - All v5.12 rules carried forward: IMP-099, IMP-032, IMP-029, IMP-030, IMP-031,
    IMP-001, IMP-027, IMP-028, IMP-013, IMP-015, IMP-017, IMP-011

v6.0 (2026-05-30 update #13):
- na_township_discovery_subproc_v6.0.md added:
  - Supersedes Township Lands Discovery Sub-Procedure v5.6
  - Entity type consolidation throughout: Trail/Trail Segment/Trail Network → Trailthing
  - §7.3–7.5 consolidated into §7.3 (Trailthing Creation)
  - §7.1 exclusion list corrected: "Cemeteries" removed (contradicted §5.6 mandatory
    cemetery enumeration)
  - Document collection §6.4 added
  - All v5.6 rules carried forward: IMP-099, IMP-029, IMP-030, IMP-005 (OTA roster,
    defunct handling), IMP-012 (Wrong-county website verification)
  - Township cemetery search added to §10 "What Not To Do" list

v6.0 (2026-05-30 update #12):
- na_county_discovery_subproc_v6.0.md added:
  - Supersedes County Lands Discovery Sub-Procedure v5.5
  - Entity type consolidation throughout: Trail/Trail Segment/Trail Network → Trailthing
  - §6.3–6.5 consolidated into §6.3 (Trailthing Creation)
  - Document collection §5.4 added
  - All v5.5 rules carried forward: IMP-099, IMP-029, IMP-030, OBS-011, OBS-012,
    OBS-013, OBS-014, OBS-028, OBS-029

v6.0 (2026-05-30 update #11):
- na_district_discovery_subproc_v6.0.md added:
  - Supersedes District-Level Public Landholders Discovery Sub-Procedure v5.7
  - Entity type consolidation throughout: Trail/Trail Segment/Trail Network → Trailthing
  - §6.3–6.5 consolidated into §6.3 (Trailthing Creation)
  - Document collection §5.4 added
  - All v5.7 rules carried forward: IMP-072 (Ohio Auditor pre-enumeration), IMP-029,
    IMP-030, OBS-016 (Government conservancy vs. nonprofit), IMP-011 (Cross-tier
    greenway Trailthings), IMP-004 (SWCD tier assignment)

v6.0 (2026-05-30 update #10):
- na_state_discovery_subproc_v6.0.md added:
  - Supersedes State Lands Discovery Sub-Procedure v5.7
  - Entity type consolidation throughout: Trail/Trail Segment/Trail Network → Trailthing
  - §6.3–6.5 (Trail, Trail Segment, Trail Network creation) consolidated into
    §6.3 (Trailthing Creation)
  - §4.2 ODOT: dog trails → Trailthing record
  - §4.6 Water Trail Tier Assignment: Trailthing entity; status_raw or
    identity_notes_raw replaces designation field reference
  - Document collection §5.4 added (T2-specific priorities: ODNR maps emphasized)
  - Download instructions added to §3.3 mandatory sources
  - Section numbering corrected: v5.7 had 4.6 before 4.5; v6.0 renumbered to
    4.1 OHC, 4.2 ODOT, 4.3 EPA/DEFA, 4.4 ODA, 4.5 OTIC, 4.6 Water Trail,
    4.7 Public Universities
  - All v5.7 rules carried forward: IMP-132, IMP-133, IMP-029, IMP-030,
    IMP-003, IMP-008, IMP-009, OBS-006

v6.0 (2026-05-30 update #9):
- na_fed_tribal_discovery_subproc_v6.0.md added:
  - Supersedes Federal & Tribal Lands Discovery Sub-Procedure v5.5
  - Entity type consolidation throughout: Trail/Trail Segment/Trail Network → Trailthing
  - §6.3–6.5 (Trail, Trail Segment, Trail Network creation) consolidated into
    §6.3 (Trailthing Creation)
  - Document collection §5.4 added (T1-specific priorities: Wayne NF, NPS, USFWS
    maps emphasized)
  - Section numbering corrected: v5.5 had 4.6 (NHA) before 4.5; v6.0 renumbered
    to 4.1 Tribal Trust, 4.2 Tribal Reservations, 4.3 Tribal Fee-Simple, 4.4
    Tribal Cultural Sites, 4.5 NHA, 4.6 USACE-ODNR
  - All v5.5 rules carried forward: IMP-111 (VA NCA), IMP-029, IMP-030,
    IMP-007 (NHA), OBS-004 (USACE-ODNR), OBS-005 (NRHP)

v6.0 (2026-05-30 update #8):
- na_discovery_orchestration_v6.0.md added:
  - Supersedes Discovery Orchestration Module v5.3
  - Document Collection System added (§4): source_documents/ folder and
    {county}_document_log.yaml are required session artifacts; maps, brochures,
    PDFs, GPX/KML, GIS exports downloaded and logged at time of encounter
  - Document log format defined: local_file, url, document_type, date_accessed,
    title, description, tier, entities (optional/informal)
  - Filename convention defined: {date}_{tier}_{short-descriptor}.{ext}
  - Document type vocabulary defined (§4.5): 11 values covering PDF maps,
    brochures, guides, plans, GPX, KML, GIS exports, interactive viewers,
    ArcGIS endpoints, kiosk documentation, Other
  - URL-only logging defined for interactive viewers and REST endpoints
  - Entity track execution order updated: Sites → Trailthings → Site Networks
    → Access Points (Trail/Trail Segment/Trail Network tracks removed)
  - Sub-procedure list updated to v6.0 entity sub-procedures
  - County folder structure at discovery completion documented (§17)
  - All v5.3 orchestration rules carried forward unchanged

v6.0 (2026-05-30 update #7):
- na_access_point_discovery_subproc_v6.0.md added:
  - Supersedes Access Point Discovery Sub-Procedure v5.2
  - Identity Parent Entity Type updated: parent_trails_raw +
    parent_trail_segments_raw → parent_trailthings_raw; Site and Trailthing
    are the only valid parent types
  - last_verified_date (populate with today's date) and field_verified
    (always false at discovery) added (IMP-013)
  - Notes_raw provenance prohibition formalized (IMP-014): operational
    access detail scope confirmed; no separate access_notes field needed
  - AP-to-Site reclassification candidate flagging added (IMP-114):
    RECLASSIFICATION_CANDIDATE flag in identity_notes_raw
  - Hazard Portage identity rule (§11) and co-location handling documented
  - Compound type handling (§10) documented
  - Site-as-Destination rule (§5.2) documented
  - IMP-045/IMP-047 water trail dual-layer methodology carried forward
    with Trailthing references updated
  - Three discovery strategy options carried forward (§9); Opportunistic
    remains recommended
  - Complete raw discovery record template with blank-field list

v6.0 (2026-05-30 update #6):
- na_site_network_discovery_subproc_v6.0.md added:
  - Supersedes Site Network Discovery Sub-Procedure v5.1
  - Broadened Site Network definition carried forward from schema v6.0 (IMP-135)
  - Four threshold rules (§3.2–3.5) replace old system-level identity test;
    keyed on network_type_raw and org_type_raw
  - SITE_NETWORK_PROVISIONAL pattern documented (§3.6): create provisional
    record at first member site; remove flag when threshold is met
  - SITE_NETWORK_UNCERTAIN narrowed (§3.7): genuine ambiguity about org_type
    or network_type only; not a substitute for PROVISIONAL
  - coordination_raw field added (consistent with v6.x entity model)
  - IMP-014 notes_raw provenance prohibition added
  - IMP-015 description_raw character/mission priority added
  - Site Network vs. Trailthing distinction documented (§6.3): dual-identity
    greenway example added; Trail Network references replaced with Trailthing
  - Entity type sequence updated: Sites → Trailthings → Site Networks → APs
  - Common cases section added (§12) with 6 worked examples

v6.0 (2026-05-30 update #5):
- na_trailthing_discovery_subproc_v6.0.md added:
  - Supersedes Trail, Trail Segment, and Trail Network discovery sub-procedures
  - No-classification mandate: discoverer does not classify trail vs. trail
    network vs. trail segment; source_term_raw and source_hierarchy_context_raw
    capture source framing verbatim
  - parent_id_raw, site_parent_raw, parent_site_network_raw
    added for documented parent relationships (only when explicitly stated)
  - member_trailthing_names_raw replaces member_trail_names_raw
  - Surface/status/governance variation rule: unnamed variation documented in
    notes_raw, not by creating additional Trailthing records
  - IMP-010 generic name qualification carried forward
  - IMP-021 explicit use/surface fields carried forward (no embedding in
    accessibility_raw)
  - IMP-046 multi-county protocol carried forward (PARTIAL MEMBERSHIP pattern)
  - IMP-014 notes_raw provenance prohibition added
  - IMP-015 description_raw ecological/physical character priority added
  - Complete raw discovery record template with all Trailthing fields
  - Entity type sequence: Sites → Trailthings → Site Networks → Access Points

v6.0 (2026-05-30 update #4):
- na_site_discovery_subproc_v6.0.md added:
  - All v5.10 rules carried forward (IMP-002, IMP-016, IMP-027, IMP-032, IMP-049,
    IMP-050, IMP-051, IMP-052, IMP-068, IMP-073)
  - §7.4 Habitat Type raw field guidance added (IMP-011): what to capture, what not
    to capture, relationship to description_raw and features_raw
  - §7.5 Access Notes raw field guidance added (IMP-012): what to capture, relationship
    to notes_raw and status_raw
  - §7.11 Verification fields guidance added (IMP-013): last_verified_date populated
    at discovery; field_verified always false at discovery
  - §7.8 Notes_raw: provenance prohibition added (IMP-014)
  - §7.3 Description: ecological/physical character priority added (IMP-015)
  - Entity type references updated throughout: Trail/Trail Segment/Trail Network → Trailthing
  - Complete raw discovery record template updated with all new fields
  - Entity type sequence updated: Sites → Trailthings → Site Networks → Access Points

v6.0 (2026-05-30 update #3):
- na_access_point_schema_v6.0.md added:
  - Identity Parent Entity Type updated: Trail/Trail Segment → Trailthing
  - last_verified_date and field_verified added (IMP-013); field count 17 → 19
  - Notes field scope tightened (IMP-014): customer-facing; no provenance artifacts
  - access_notes not added: AP Notes field already correctly scoped to operational
    access detail; no gap to fill
  - Field-by-field rules expanded from v5.2 minimal style
  - Site-as-Destination rule and AP-to-Site reclassification rule (IMP-114) documented
- na_access_point_vocabulary_v6.0.md added:
  - All v5.3 controlled vocabularies carried forward unchanged
  - Identity Parent type references updated throughout (Trail/Trail Segment → Trailthing)
  - Last Verified Date / Field Verified guidance added (§5)
  - Notes field guidance tightened (§6): provenance prohibition added
  - Normalization rules reorganized into tables (§8); ambiguous cases table added

v6.0 (2026-05-30 update #2):
- na_site_vocabulary_v6.0.md added:
  - All v5.6 controlled vocabularies carried forward unchanged (Category,
    Subtype, Designation, Status, Features)
  - Habitat Type free-text guidance added (§8): open vocabulary; ecological/
    natural character field; examples and what-not-to-capture rules
  - Access Notes free-text guidance added (§9): seasonal/public access; relationship
    to Status field documented with usage table
  - Last Verified Date / Field Verified guidance added (§10)
  - Notes field guidance added (§11): customer-facing; no provenance artifacts
  - Description field guidance added (§12): ecological/physical character priority
  - Normalization rules §13 expanded from v5.6 §7 with additional table structure

v6.0 (2026-05-30 update):
- na_site_schema_v6.0.md added (IMP-011, IMP-012, IMP-013, IMP-014, IMP-015):
  - Four new fields: habitat_type (open vocabulary, ecological character),
    access_notes (seasonal/public access caveats), last_verified_date (DATE),
    field_verified (boolean, default false); field count 26 → 30
  - Description mandate tightened: ecological/physical character priority;
    amenity inventory belongs in Features
  - Notes scope tightened: customer-facing; no provenance artifacts
  - Field-by-field rules substantially expanded from v5.4 thin definitions
  - Discovery raw record template updated with new fields
  - Field scope boundary quick-reference table added (§7)
- na_trailthing_schema_v6.0.md updated (IMP-014, IMP-015):
  - §3.23 Description: ecological/physical character priority added
  - §3.26 Notes: customer-facing provenance prohibition added
- na_site_network_schema_v6.0.md updated (IMP-014, IMP-015):
  - §3.13 Description: character and mission priority added
  - §3.15 Notes: customer-facing provenance prohibition added
- na_site_network_vocabulary_v6.0.md updated (IMP-014):
  - §9.3 Notes: provenance prohibition added

v6.0 (2026-05-28):
- Initial manifest. v6 folder and directory structure created.
- na_site_network_schema_v6.0.md added (IMP-135):
  - Broadened Site Network definition: named org/designation + 2+ member
    sites; prior "system-level branding" test removed
  - Four threshold rules in §4 keyed on network_type and org_type
  - SITE_NETWORK_PROVISIONAL flag added; SITE_NETWORK_UNCERTAIN narrowed
  - coordination field added (position 8); field count 16 → 17
- na_trailthing_schema_v6.0.md added (IMP-009):
  - Trail Network, Trail, and Trail Segment unified into single interim entity
    type "Trailthing" (working name, no hierarchical connotation)
  - 29 fields; self-referential parent_id for trail hierarchy; site_parent_id
    and parent_site_network_id for Site Network parent relationships
  - source_term and source_hierarchy_context capture how authoritative sources
    describe the entity — primary input for future hierarchy pattern analysis
  - Trail hierarchy classification deferred to after 30 v6 county runs (IMP-007)
  - na_trail_network_schema_v6.0.md superseded; retained as reference
- na_trail_network_schema_v6.0.md added (IMP-008) — superseded by Trailthing:
  - org_type field added (position 3); descriptive only, no threshold
    function for Trail Networks
  - coordination field added (position 8); field count 17 → 19
  - Identity rules rewritten: system-identity-first, all-conditions test
  - Org-portfolio Trail Networks clarified: named system required, mere
    management insufficient
  - Trail Networks and trail_site_relationships distinguished in §5.4

------------------------------------------------------------
# 1. REPOSITORY STRUCTURE (v6.x MODULES ONLY)

Modules listed here have been revised for v6.x. For all other modules,
use the v5.x equivalents in the Natural Areas Project v5 folder.

- /schemas
  - na_site_schema_v6.0.md
  - na_access_point_schema_v6.0.md
  - na_site_network_schema_v6.0.md
  - na_trailthing_schema_v6.0.md
  - na_trail_network_schema_v6.0.md  *(superseded by na_trailthing_schema_v6.0.md — retained as reference)*

- /vocabularies
  - na_site_vocabulary_v6.0.md
  - na_access_point_vocabulary_v6.0.md
  - na_site_network_vocabulary_v6.0.md
  - na_trailthing_vocabulary_v6.0.md

- /normalization
  - na_normalization_engine_v6.0.md
  - na_site_normalization_v6.0.md
  - na_trailthing_normalization_v6.0.md
  - na_site_network_normalization_v6.0.md
  - na_access_point_normalization_v6.0.md
  - na_entity_upsert_engine_v6.0.md

- /output
  - na_tsv_output_site_v6.0.md
  - na_tsv_output_trailthing_v6.0.md
  - na_tsv_output_site_network_v6.0.md
  - na_tsv_output_access_point_v6.0.md
  - na_tsv_integrity_check_v6.0.md

- /discovery
  - na_discovery_protocol_v6.0.md
  - na_gps_acquisition_v6.0.md
  - na_discovery_orchestration_v6.0.md
  - na_discovery_metadata_spec_v6.0.md
  - na_fed_tribal_discovery_subproc_v6.0.md
  - na_state_discovery_subproc_v6.0.md
  - na_district_discovery_subproc_v6.0.md
  - na_county_discovery_subproc_v6.0.md
  - na_township_discovery_subproc_v6.0.md
  - na_municipal_discovery_subproc_v6.0.md
  - na_conservancy_discovery_subproc_v6.0.md
  - na_private_discovery_subproc_v6.0.md
  - na_site_discovery_subproc_v6.0.md
  - na_trailthing_discovery_subproc_v6.0.md
  - na_site_network_discovery_subproc_v6.0.md
  - na_access_point_discovery_subproc_v6.0.md

- /processing
  - na_processing_orchestration_v6.0.md
  - na_resolution_engine_v6.0.md
  - na_resolution_rules_v6.0.md
  - na_cross_county_resolution_v6.0.md
  - na_child_site_rules_v6.0.md
  - na_county_baseline_v6.0.md

- /audit
  - na_audit_and_logging_v6.0.md

------------------------------------------------------------
# END OF MODULE MANIFEST v6.0
