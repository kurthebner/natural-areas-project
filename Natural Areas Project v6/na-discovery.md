---
name: na-discovery
description: Executes tier-based discovery of natural areas entities across U.S. counties under v6 protocols. Triggers on discover, find parks, catalog entities, tier discovery, or any mention of searching for natural areas in a location.
---

# Natural Areas Project — Discovery Skill v6.0

## Project Orientation Protocol

**Mandatory first step in every session — new or resumed — before reading any module, touching any data, or beginning any tier work.**

1. **List the v6 project root.** Run `ls` on `Natural Areas Project v6`. Establishes ground truth of what directories exist.

2. **Identify the authoritative module directories:**
   - `/discovery` — tier and entity discovery sub-procedures (v6.x)
   - `/schemas` — entity schemas (v6.x)
   - `/vocabularies` — controlled vocabularies (v6.x)
   - `/normalization` — normalization contracts (v6.x)
   - `/output` — TSV output specifications (v6.x)
   - `/processing` — pipeline and resolution modules (v6.x)
   - `/audit` — audit and logging modules (v6.x)

3. **Read the module manifest.** Read `na_module_manifest_v6.0.md` at the v6 project root. The manifest lists the current canonical filename — including version number — for every module. Use the manifest to determine which exact file to read. Do not use memory, the skill text, or a session summary to determine module filenames.

4. **Never read from non-authoritative locations.** The v5 project folder (`Natural Areas Project v5/`) contains superseded modules. Never use v5 modules as procedure or schema references for v6 work.

5. **Target directories directly. Do not use broad Glob patterns.** The correct workflow is: read the manifest → get the exact filename → read that file from its canonical directory.

---

## Source Authority Hierarchy

1. **Protocol modules and sub-procedures** — authoritative for all rules
2. **The handoff document** — a progress tracker only; records where you are, not what the rules are
3. **Session memory, prior context, and summaries** — have no protocol authority

When any two conflict, the higher-authority source wins without exception.

---

## Resumed Session Protocol

**Before touching any data or staging files in a resumed session:**

0. Execute the Project Orientation Protocol above.
1. Read **Discovery Orchestration Module v6.0 §6** (authoritative tier order)
2. Verify that the current tier label in the handoff matches the canonical tier order
3. If they disagree, the module wins — correct the handoff before proceeding
4. At every tier transition, state explicitly: *"I am about to begin Tier N — [canonical name]."*

---

## Core Rules

**FETCH BEATS SEARCH**: Always web_fetch official pages. Never rely on search snippets alone.
**USE BROWSER WHEN NEEDED**: When a page requires JavaScript rendering, an ArcGIS viewer, or interactive GIS portal, use Claude in Chrome — not just web_fetch.
**VIEW MAPS DIRECTLY**: Open Google Maps and view the location. Do not search for map references.
**EXHAUSTIVE BEATS EFFICIENT**: Complete every tier 100% before advancing.
**DOCUMENT NEGATIVES**: Record "no entities found" with evidence. Never assume.
**STAGING FILE IS THE RECORD**: Append each entity immediately. Chat history is not a record.
**DOCUMENT LOG IS REQUIRED**: Log every downloaded document at download time in `{county}_document_log.yaml`. Do not defer.
**HANDOFF IS THE INTER-SESSION RECORD**: Any structured table from an authoritative source must be written to the handoff's Captured Source Data section at fetch time.

---

## Discovery Is Collection Only

During discovery, collect raw values exactly as found:
- No normalization of names, types, or categories
- No correction of spelling or formatting
- No inference of missing values
- No population of `township` or `municipality` — GIS-derived only
- No invention of GPS coordinates — only record what authoritative sources explicitly state
- **No classification of Trailthings** — capture `source_term_raw` verbatim; never decide if it is a trail, segment, or network

---

## Eight-Tier Sequence

**Mandatory tier-transition checkpoint**: Before beginning any tier, **read (or re-read) the authoritative sub-procedure for that tier**. This is not optional. The sub-procedure contains mandatory steps that are easy to miss from memory.

Execute tiers in order. Complete all four entity types per tier before advancing.

| Tier | Governance Level | Sub-Procedure |
|------|-----------------|---------------|
| 1 | Federal & Tribal | `na_fed_tribal_discovery_subproc_v6.0.md` |
| 2 | State | `na_state_discovery_subproc_v6.0.md` |
| 3 | District (Metroparks, conservancy districts) | `na_district_discovery_subproc_v6.0.md` ⚠️ **Read §3.0 first — Ohio Auditor pre-enumeration is the mandatory first step** |
| 4 | County | `na_county_discovery_subproc_v6.0.md` — **for MORPC-covered counties: cross-reference `Parks_and_Open_Space_*.csv`** |
| 5 | Township | `na_township_discovery_subproc_v6.0.md` — **Ohio: enumerate townships from `Townships_Officials2022-2023.xlsx` first** |
| 6 | Municipal | `na_municipal_discovery_subproc_v6.0.md` — **for MORPC-covered counties: cross-reference `Parks_and_Open_Space_*.csv`** |
| 7 | Conservancy & Land Trust | `na_conservancy_discovery_subproc_v6.0.md` — **check §4 Known Org inventory first** |
| 8 | Private | `na_private_discovery_subproc_v6.0.md` |

---

## Entity Type Sequence Within Each Tier

Discover in this order within each tier:
1. Sites
2. Trailthings
3. Site Networks
4. Access Points

This ordering ensures Sites exist before Trailthings need to reference them as site parents, and both Sites and Trailthings exist before Access Points need to reference them.

**Every entity type requires a documented result before the tier is complete** — either confirmed entities with records, or a confirmed null with evidence and sources checked. Silence is not a null.

---

## Entity Discovery Sub-Procedures

Read each sub-procedure to determine whether that entity type applies:

- `na_site_discovery_subproc_v6.0.md`
- `na_trailthing_discovery_subproc_v6.0.md` — defines what makes a Trailthing; captures source_term verbatim; no classification
- `na_site_network_discovery_subproc_v6.0.md` — defines threshold rules; read §3 before concluding null
- `na_access_point_discovery_subproc_v6.0.md`

---

## Raw Discovery Record — Key Fields (v6.0)

**Sites:**
```yaml
entity_type: Site
name_raw:
counties_raw: []
county_primary:
ownership_raw:
governance_raw:
partner_agencies_raw:
coordination_raw:
description_raw:       # narrative prose; ecological/physical character priority
habitat_type_raw:      # ecological/natural character; open vocabulary; verbatim
features_raw:          # amenity LIST, verbatim (not sentences)
access_notes_raw:      # seasonal restrictions, permit requirements, access caveats
location_raw:
acres_raw:
gps_lat_raw:           # only if explicitly stated by authoritative source
gps_lon_raw:
boundary_document_raw: # filename in source_documents/ if boundary file downloaded
urls_raw: []
ebird_hotspot_id:      # eBird L-code if site has a known hotspot (e.g. L123456); blank if none
identity_notes_raw:
township_raw:          # BLANK — GIS-derived only
municipality_raw:      # BLANK — GIS-derived only
last_verified_date:    # today's date
field_verified:        # false at discovery
discovery_tier:
seeded_from_baseline:
baseline_id:
```

**Trailthings:**
```yaml
entity_type: Trailthing
name_raw:
source_term_raw:              # REQUIRED — verbatim term from source
source_hierarchy_context_raw: # verbatim how source frames this entity relative to others
counties_raw: []
county_primary:
parent_id_raw:                # parent Trailthing name — only if source explicitly states
site_parent_raw:              # parent Site name — only if source explicitly states
parent_site_network_raw:      # parent Site Network name — only if source explicitly states
member_trailthing_names_raw:  # names of member Trailthings if this is a container
ownership_raw:
governance_raw:
partner_agencies_raw:
coordination_raw:
description_raw:
use_type_raw:
surface_type_raw:
origin_type_raw:
status_raw:
difficulty_raw:               # only if explicitly stated
accessibility_raw:
total_length_raw:
urls_raw: []
maps_raw: []
identity_notes_raw:
last_verified_date:
field_verified:
discovery_tier:
seeded_from_baseline:
baseline_id:
```

**Access Points:**
```yaml
entity_type: Access Point
name_raw:
counties_raw: []
county_primary:
parent_sites_raw: []
parent_trailthings_raw: []
governance_raw:
description_raw:
features_raw:
location_raw:
gps_lat_raw:
gps_lon_raw:
urls_raw: []
identity_notes_raw:
last_verified_date:
field_verified:
discovery_tier:
seeded_from_baseline:
baseline_id:
```

---

## Description vs. Features — Required Distinction

**`description_raw`** — Narrative prose. Complete sentences. Ecological/physical character priority.
- ✓ "Griggs Reservoir Park is a 393-acre greenway along the Scioto River."
- ✓ "Protects one of central Ohio's last intact upland oak-hickory forests."
- ✗ "Picnic shelters, restrooms, fishing" ← that's features_raw

**`habitat_type_raw`** — Ecological/natural character. Open vocabulary. Verbatim from source.
- ✓ "Wet prairie remnant", "Oak-hickory woodland", "Riparian corridor", "Emergent wetland"
- ✗ Amenities, governance labels, or category labels

**`features_raw`** — Amenity and facility list. NOT sentences.
- ✓ "Picnic shelter; restrooms; fishing pond; playground"
- ✗ Narrative sentences

**Governance contamination rule**: `governance_raw` must contain only the managing organization's name. GIS park type labels ("Community Park") are NOT governance — record in `category_raw` or `identity_notes_raw`.

---

## Document Collection (v6 new)

When any map, PDF, brochure, GPX/KML, or GIS export is downloaded:
1. Save to `source_documents/` with filename: `{date}_{tier}_{short-descriptor}.{ext}`
2. Log immediately in `{county}_document_log.yaml`
3. If it is a boundary file for a specific Site, populate `boundary_document_raw` on that entity's record

Do not defer document logging to the end of a session. The document log is a required county artifact.

---

## Per-Entity-Type Null Documentation

Before concluding null for Site Networks or Trailthings at any tier:
1. Read the relevant sub-procedure's criteria section
2. Check at least two sources for evidence
3. Record what was checked and why null was concluded

Required null format:
```yaml
entity_type_result:
  tier:
  governance_level:
  entity_type: Trailthing | Site Network
  result: null
  sources_checked:
    - [URL or source description]
  reasoning: [specific evidence for null]
```

---

## Null Tier Results

```yaml
tier_result:
  tier:
  governance_level:
  result: null
  entities_found: 0
  sources_checked: []
  notes:
```

**DEFECT status (IMP-076)**: If a tier was worked under the wrong protocol or with missing mandatory steps, mark it **DEFECT** in the staging file and **PENDING** in the handoff. Never carry a defective tier forward as complete.

---

## Tier Close Verification — Physical File Check (IMP-080)

Before closing any tier, **physically verify** that every result block is present in the staging YAML file. Do not rely on session context or memory.

1. Read or grep the staging YAML file
2. Confirm every entity type has a result block (entities or null evidence) actually in the file
3. "I staged it above" is not a substitute for verifying the content exists on disk

## Cross-County Candidate Flagging (IMP-104)

When closing any tier: if any entity's `counties_raw` lists more than one county, verify that `identity_notes_raw` contains either `CROSS_COUNTY_CANDIDATE` or `KNOWN_MC:{existing_id}`.

## Staging Append Safety — Key-Targeted Writes (IMP-079)

Never append T7/T8 entities by text position using the Edit tool. Always use Python key-targeted writes:

```python
import yaml, pathlib
f = pathlib.Path("county_oh_raw_discovery.yaml")
data = yaml.safe_load(f.read_text())
data.setdefault("records", [])
data["records"].append({ ... })
f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False))
```

---

## GPS During Discovery

**Primary rule**: Only record GPS if an authoritative source explicitly provides coordinates. Never invent or infer GPS.

**Map verification**: When opening a Google Maps entity detail card to confirm an entity's identity, capture the GPS from the URL (`@LAT,LON,ZOOMz` format). Record in `gps_lat_raw` / `gps_lon_raw` with a note in `identity_notes_raw`.

**Browser (Claude in Chrome)**: Use for any source that requires JavaScript rendering, an ArcGIS viewer, or interactive GIS portal. This is a primary GPS acquisition tool, not a fallback.

---

## Supplemental Authorities — Ohio

### `Townships_Officials2022-2023.xlsx`
- **Scope**: All 88 Ohio counties, 1,307 active townships
- **Use in Tier 5**: Filter by County Name. Website column provides trustee/fiscal officer URLs.
- **Defunct detection**: A township absent from this roster is a defunct candidate — follow Township Discovery Subproc §3.1a before closing as defunct.

### `Parks_and_Open_Space_*.csv` — 15-County MORPC GIS Layer
- **Scope**: DEL, FAI, FAY, FRA, HOC, KNO, LIC, LOG, MAD, MAR, MRW, PER, PIC, ROS, UNI
- **Use in Tier 4**: Cross-reference county-managed entities before closing tier
- **Use in Tier 6**: Filter by Jurisdiction as completeness check
- **Limitations**: No GPS. Sub_Type vocabulary differs from NAP — do not map directly.

---

## After All Tiers Complete

Before handing off to the pipeline:
1. Physical file check on the staging YAML — confirm all tiers have result blocks
2. Cross-county candidate scan — verify all multi-county entities are flagged
3. Baseline seed reconciliation — flag any unconfirmed seeds as `unconfirmed_baseline_seed`
4. Document log review — confirm all downloaded documents are logged
5. Update handoff to `DISCOVERY COMPLETE — PIPELINE READY`
6. Run `na-pipeline` skill

---
# END OF NA_DISCOVERY_SKILL
