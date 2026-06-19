# NATURAL AREAS PROJECT
# ACCESS POINT NORMALIZATION CONTRACT v6.0
(Authoritative Field-Level Rules for Normalizing Resolved Access Point Entities)

This module defines the v6.0 normalization rules applied by the Normalization Engine
v6.0 to transform Resolved Access Point entities into Normalized Access Point Objects
ready for insertion into the Entity Graph.

This contract contains no controlled vocabularies.
All vocabularies are defined in the **Access Point Vocabulary Module v6.0**.

This contract is authoritative for Access Point normalization only.

This module supersedes Access Point Normalization Contract v5.3.

------------------------------------------------------------
# CHANGES FROM v5.3 → v6.0

- **Parent field consolidation**: `parent_trails_raw` and
  `parent_trail_segments_raw` replaced by `parent_trailthings_raw` (§2.2 Inputs,
  §5.7 Parent Entity). Allowed identity parent types updated from Site + Trail +
  Trail Segment to Site + Trailthing.

- **Two new fields added** (IMP-013): Normalization rules added for
  `last_verified_date` (§5.19) and `field_verified` (§5.20). Both fields added to
  raw inputs (§2.2) and validation logic (§7).

- **IMP-014 — Notes provenance prohibition added to §5.16**: Notes field is
  customer-facing. Pipeline source references, IMP numbers, and process content
  must not appear.

- **Schema module references updated**: Trail Schema and Trail Segment Schema
  removed from §2.5 dependencies; Trailthing Schema added.

- **All v5.3 rules carried forward**: IMP-114 (AP-to-Site reclassification),
  IMP-100/IMP-084 (ap_type vocabulary enforcement and compound type resolution),
  IMP-100 status enforcement, empty string enforcement (§5.18), GPS handling,
  GIS-derived township/municipality.

------------------------------------------------------------
# 1. PURPOSE

The Access Point Normalization Contract v6.0 defines:

- How a Resolved Access Point becomes a Normalized Access Point
- How Access Point Type is normalized, including compound-type resolution (IMP-084)
- How Status is normalized
- How Features are normalized
- How Identity Notes are surfaced from identity_notes_raw
- How identity parents (Site or Trailthing) are validated
- How last_verified_date and field_verified are normalized
- How County, Township, and Municipality are handled
- How GPS and Plus Code rules are applied
- How normalization interacts with the Normalization Engine v6.0
- How provenance, conflicts, and uncertainties are recorded

Normalization must:
- Never invent data
- Never infer Access Point Type or parent entity
- Never silently correct malformed values
- Always log normalization decisions

------------------------------------------------------------
# 2. INPUTS

## 2.1 Resolved Entity Object
From Resolution Engine v6.x, including:

- resolved identity key
- resolved entity_type = "Access Point"
- resolved access_point_type
- resolved status (if any)
- resolved identity parent (Site or Trailthing)
- resolved additional parent associations (if any)
- resolved county
- resolved conflicts and uncertainties

## 2.2 Raw Discovery Record v6.0
Including:

- access_point_name_raw
- access_point_type_raw
- status_raw
- features_raw
- county_raw
- parent_sites_raw
- parent_trailthings_raw *(replaces parent_trails_raw + parent_trail_segments_raw)*
- gps_lat_raw (string, as found)
- gps_lon_raw (string, as found)
- address_raw
- url_primary_raw
- urls_raw (all URLs including any map URLs)
- identity_notes_raw
- notes_raw
- last_verified_date *(new in v6.0 — populated at discovery with today's date)*
- field_verified *(new in v6.0 — always false at discovery)*
- discovery_tier, discovered_in_tiers
- seeded_from_baseline, baseline_id
- discovery_metadata

**Not in raw discovery (GIS-derived):**
- township — populated by Normalization Engine via GIS spatial lookup
- municipality — populated by Normalization Engine via GIS spatial lookup

## 2.3 Normalization Engine Outputs (Pre-Populated)
Before this contract runs, the Normalization Engine v6.0 has already:

- Parsed gps_lat_raw + gps_lon_raw → gps_lat, gps_lon (numeric)
- Computed plus_code from gps_lat / gps_lon (if GPS present)
- Derived township via GIS spatial lookup
- Derived municipality via GIS spatial lookup

This contract validates those results but does not recompute them.

## 2.4 Vocabulary Modules
- **Access Point Vocabulary Module v6.0** — ap_type, Status; §5.1 normalization
  mapping table; §2.2 compound type rules (IMP-084).
  **Read §5.1 before normalizing ap_type or status.**

## 2.5 Schema Modules v6.0
- Access Point Schema Module v6.0
- Site Schema Module v6.0 (for parent Site validation)
- Trailthing Schema Module v6.0 (for parent Trailthing validation)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A **Normalized Access Point Object v6.0** conforming to the Access Point Schema
  Module v6.0
- A **Normalization Provenance Record**
- A **Validation Result Object** (warnings, errors)
- A normalized entity ready for the **Entity Upsert Engine v6.x**, OR a flagged
  entity routed to the GPS Acquisition Module if GPS is absent

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH-LEVEL)

1.  Receive Resolved Access Point from Normalization Engine v6.0
2.  Validate identity and entity_type = "Access Point"
3.  **Read Access Point Vocabulary Module v6.0 §5.1** (ap_type and status
    mapping tables, compound type rules)
4.  Normalize Name
5.  Normalize Access Point Type (apply §5.1 ap_type mapping; apply IMP-084
    compound type rule)
6.  Normalize Status (apply §5.1 status mapping)
7.  Normalize Features (update features when compound type rule fires)
8.  Resolve and validate identity parent (Site or Trailthing)
9.  Normalize additional parent associations
10. Normalize County
11. Validate Township, Municipality — pre-populated by GIS lookup
12. Validate GPS (gps_lat / gps_lon) — pre-populated by engine
13. Validate Plus Code — pre-populated by engine
14. Normalize Address
15. Normalize Identity Notes
16. Normalize Notes (provenance prohibition)
17. Normalize URL
18. Normalize Last Verified Date (§5.19)
19. Normalize Field Verified (§5.20)
20. Apply §5.18 empty string enforcement across vocabulary fields
21. Check GPS presence → if absent, flag for GPS Acquisition Module
22. Run integrity anchor deduplication check (via Normalization Engine)
23. Validate against Access Point Schema v6.0
24. Emit Normalized Access Point + provenance

If any critical step fails → return error to Normalization Engine v6.0.

------------------------------------------------------------
# 5. FIELD-BY-FIELD NORMALIZATION RULES

## 5.1 Name

- Use name_raw with minimal whitespace cleanup.
- Never invent names.
- Never infer names from amenities, parent entity, or context.
- If unnamed → leave blank.
- Placeholder names (e.g., "Unnamed Trailhead") → preserve; flag for review.

**Provenance:** Log all corrections and conflicts.

---

## 5.2 Access Point Type

**Read Access Point Vocabulary Module v6.0 §5.1 before applying this step.**

- Single value only — compound values are never valid in `ap_type`.
- Never infer type from amenities or GPS alone.

**Normalization procedure:**

1. Check `access_point_type_raw` against the §5.1 ap_type mapping table.
2. If maps to single controlled value → apply; log.
3. **Compound type rule (IMP-084) — Trailhead + Parking:**
   If raw value combines Trailhead with Parking Area (e.g., "Trailhead/Parking",
   "Trailhead & Parking", "Trailhead with Parking"):
   - Assign `ap_type = "Trailhead"`.
   - Ensure `features` contains `"Parking Area"` (add with capacity annotation
     if documented).
   - Log compound raw value and resolution.
4. **Compound type rule — Parking + Trailhead (reverse):**
   If raw value leads with Parking Area as primary function:
   - Assign `ap_type = "Parking Area"`.
   - Add "Trailhead" to `features` only if source explicitly designates it as
     a trailhead.
   - Log resolution.
5. Other compound or ambiguous value → REVIEW; flag in `identity_notes`; leave
   `ap_type` blank until resolved.
6. Unmappable and not compound → null-and-log.
7. Empty string ("") → null; see §5.18.

**Common mappings (non-exhaustive — AP Vocabulary v6.0 §5.1 is authoritative):**
- "trail head" / "trail-head" → "Trailhead"
- "trailhead/parking" → "Trailhead" (+ Parking Area in features)
- "parking lot" / "parking" → "Parking Area"
- "boat launch ramp" → "Boat Ramp"
- "kayak launch" / "canoe access" → "Watercraft Access Point"
- "pulloff" / "pull off" → "Roadside Pull-Off"
- "portage" / "mandatory portage" / "carry" → "Hazard Portage"
- "dam portage" / "dam carry" → "Hazard Portage"

**Provenance:** Log all mappings, compound resolutions, and unmappable values.

---

## 5.3 Access Level — REMOVED IN v5.0

- If present in older resolved records → silently drop.

---

## 5.4 Role — REMOVED IN v5.0

- If present in older resolved records → silently drop.

---

## 5.5 Status

**Read Access Point Vocabulary Module v6.0 §5.1 before applying this step.**

- Optional. Single value only.
- "Closed" = permanently or indefinitely closed.
- "Seasonal" requires season details in Notes.
- Leave blank if status is ambiguous or undocumented.

**Normalization procedure:**

1. Check `status_raw` against the §5.1 status mapping table.
2. "open" / "operational" → "Active"
3. "seasonal access" → "Seasonal"
4. "permanently closed" / "decommissioned" → "Closed"
5. "permit required" → "Restricted"
6. Unmappable → null-and-log.
7. Empty string ("") → null; see §5.18.

---

## 5.6 Features

- Semicolon-delimited list of facilities and amenities at the access point.
- Free-text — no controlled vocabulary.
- Normalize capitalization to title case.
- Metadata in parentheses permitted: "Parking (50 spaces, paved)", "Restrooms (ADA, seasonal)".
- Must describe features of the access point itself, not the parent entity.
- Remove obvious duplicates.
- Leave blank if no features are documented.
- **When compound type rule fires (§5.2):** Ensure "Parking Area" appears in
  features for records where ap_type = "Trailhead" was resolved from a compound.

---

## 5.7 Parent Entity (Identity Parent)

An Access Point must have exactly one identity parent.

**Valid identity parent types in v6.0:**
- Site
- Trailthing

**Not valid as identity parents:**
- Site Networks

**Resolution rules:**
- Identity parent must be a normalized entity in the Entity Graph.
- If multiple parent candidates exist:
  - Prefer Trailthing if the AP is clearly a trail-specific trailhead or portage.
  - Prefer Site if the AP is primarily a site entrance or site-based access point.
  - If ambiguity remains → leave identity parent blank; surface to Resolution
    Engine; log in identity_notes.
- Never infer parent from proximity alone.
- Never assign multiple identity parents.

**Provenance:** Log all parent resolution decisions and conflicts.

---

## 5.8 Additional Parent Associations

- Additional parents (Site or Trailthing) beyond the identity parent may be
  preserved.
- Written to the `access_point_parents` relationship table.
- Must not contradict the identity parent.
- Must be supported by authoritative sources.
- Never infer additional parents from proximity or geometry.

---

## 5.9 County

- Required — single value only.
- Must match official Ohio county name.
- Must represent the county where the Access Point physically resides.
- Omit the word "County."
- Must not be inferred solely from parent entity's county list.

---

## 5.10 Township — GIS-DERIVED

- Populated by Normalization Engine v6.0 via GIS spatial lookup.
- This contract validates that the field is either a recognized civil township
  name or blank.
- Never copy township from discovery records.

---

## 5.11 Municipality — GIS-DERIVED

- Populated by Normalization Engine v6.0 via GIS spatial lookup.
- This contract validates that the field is either a recognized municipality name
  or blank.
- Never copy municipality from discovery records.

---

## 5.12 GPS (gps_lat / gps_lon)

- Both gps_lat and gps_lon must be present, or both must be blank.
- gps_lat in range [-90, 90]; gps_lon in range [-180, 180].
- Both must be numeric (float).
- If validation fails → log error; blank both fields.

**If GPS is absent after normalization:**
- Flag entity for GPS Acquisition Module (Stage 3).
- Preserve all other normalized fields.
- Log GPS absence in provenance.
- Do not reject — GPS Acquisition Module will acquire coordinates.

---

## 5.13 Plus Code

- If gps_lat and gps_lon are present → plus_code must be present and well-formed.
- If GPS is blank → plus_code must be blank.
- Never manually enter a Plus Code.

---

## 5.14 Address

- Preserve with minimal cleanup (trim whitespace, fix encoding issues).
- Never invent or USPS-normalize.
- Partial addresses and road descriptions are valid.
- Leave blank if no authoritative or defensible address exists.

---

## 5.15 Identity Notes

Surfaced from `identity_notes_raw` at discovery stage.

**Use for:**
- Access point type uncertainty flags
- Parent entity assignment uncertainty or conflict
- Disambiguation notes
- REVIEW flags from normalization
- RECLASSIFICATION_CANDIDATE flag (IMP-114) — preserve; do not strip

**Rules:**
- Must not duplicate Notes content
- Preserve uncertainty flags — do not resolve silently

---

## 5.16 Notes

**Customer-facing scope (IMP-014)**: Notes is a customer-facing field. Pipeline
source references, IMP numbers, session identifiers, and process-related content
must not appear. Strip these during normalization.

- Preserve access-related operational notes.
- Use for: gate hours, parking constraints, seasonal conditions, surface/grade
  issues, fees, signage visibility.
- **Alternate names** (IMP-029): `ALT NAME: '[name]' — [source context]` — any name used
  by an authoritative source that differs from the canonical `name` field. Always preserve;
  never discard known alternate names.
- Must not include features (those belong in Features field).
- Must not include identity-defining information.
- Notes may be concatenated from multiple raw sources — log concatenation.
- Leave blank if no relevant notes.

**Pipeline metadata stripping**: Apply the same metadata stripping logic as Site
Normalization Contract v6.0 §5.19.

---

## 5.17 URL

- Full https:// URL to primary authoritative source.
- Semicolon-delimit if multiple authoritative URLs exist.
- Include map URLs as additional semicolon-delimited values.
- Remove tracking parameters.
- Leave blank if no authoritative URL exists.

---

## 5.18 Empty String Enforcement (IMP-100)

**Run after normalizing all vocabulary-controlled fields, before GPS presence
check and integrity anchor validation.**

Applies to: `ap_type`, `status`.

Empty string ("") is a data defect — convert to null; log in provenance.
Do not route to REVIEW — empty string is a mechanical defect.

---

## 5.19 Last Verified Date (IMP-013) *(new in v6.0)*

- Accept `last_verified_date` from the raw discovery record (populated at
  discovery with today's date).
- Validate format: must be ISO 8601 DATE format (YYYY-MM-DD).
- If present and valid → pass through unchanged.
- If format is invalid → attempt to parse and reformat; log WARNING.
- If absent or null → log WARNING; leave blank.
- Never generate or infer a date not present in the raw record.

---

## 5.20 Field Verified (IMP-013) *(new in v6.0)*

- Accept `field_verified` from the raw discovery record (always `false` at
  discovery).
- Validate: must be boolean.
- String "false"/"False" → convert to boolean `false`; log.
- String "true"/"True" → convert to boolean `true`; log.
- Absent or null → default to `false`; log WARNING.
- Other values → null-and-log; flag for REVIEW.

---

## 10a. AP-to-Site Reclassification (IMP-114)

An Access Point may be reclassified as a Site during normalization when
post-normalization evidence indicates site-level identity was not recognized at
discovery.

**Qualifying Criteria (all three must be met):**
1. `acres_raw` contains a numeric value from an authoritative source.
2. `description_raw` contains narrative prose describing the entity as a place.
3. `governance_raw` names an entity that independently manages this location as
   a destination.

**Disqualifying Conditions (any one blocks reclassification):**
- Entity's identity is access-only (entry to a parent trail or site only).
- Acreage is inferred from GIS parcel extent rather than stated by source.
- Governance is the same managing entity as the parent.
- Description_raw describes the access function rather than the place.

**Required Steps:**
1. Remove the entity from AP output.
2. Create a Site record — populate Site schema fields from the AP's raw fields.
3. Update parent references; log the reference update.
4. Log to normalization_provenance with action "ap_to_site_reclassification".
5. Flag for human review at Stage 5.5 Human Review Gate.

**Prohibition**: Never reclassify based on map area or inferred size alone.
When criteria are borderline, retain AP classification and note for future review.

------------------------------------------------------------
# 6. IDENTITY ANCHOR VALIDATION

The integrity anchor for Access Points is:
`entity_type` + `access_point_type` + `identity_parent_entity_type`
+ `identity_parent_entity_id` + `county`

This contract must verify:
- All anchor fields are present (or identity_parent fields are blank with a
  logged reason)
- County is a valid single value
- Identity parent references a valid entity

------------------------------------------------------------
# 7. VALIDATION LOGIC

Normalization must validate:

- Access Point Type maps to valid vocabulary value (per AP Vocabulary v6.0)
- Status maps to valid vocabulary value if present
- No vocabulary-controlled field contains an empty string (§5.18)
- County: single value, "County" stripped, valid Ohio county name
- GPS: both gps_lat and gps_lon present or both blank; values in valid range
- Plus Code: present if GPS present, blank if GPS blank
- Features: semicolon-delimited, no empty segments
- Parent entity: references valid entity in Entity Graph; type must be Site or
  Trailthing (not Site Network)
- **Last verified date** (§5.19): DATE format validation; warn if absent
- **Field verified** (§5.20): boolean validation; default false if absent
- No invented data
- Blank fields are true blanks (null, not empty string)
- No delimiter characters inside field values

------------------------------------------------------------
# 8. DELIMITER INTEGRITY REQUIREMENTS

- Blank fields are true blanks (null, not empty string)
- No spaces between semicolons and values
- No trailing spaces or newlines within fields
- No collapsed delimiters
- No missing delimiters in multi-value fields

All anomalies must be logged.

------------------------------------------------------------
# 9. CONFLICT HANDLING

## 9.1 Conflicting Names
Use the most authoritative source. Log conflict.

## 9.2 Conflicting Access Point Type
Use authoritative documentation. If unclear → leave blank; flag in identity_notes.

## 9.3 Conflicting Parent Entities
Preserve all claims in metadata. Do not assign identity parent until conflict is
resolved. Surface to Resolution Engine; log in identity_notes.

## 9.4 Conflicting GPS
Use most authoritative source (agency GIS preferred). Log conflict and source.

## 9.5 Conflicting County
Use county derived from GPS if available. Otherwise use most authoritative source.

------------------------------------------------------------
# 10. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.
- Never estimate GPS coordinates.
- Never infer Access Point Type from amenities alone.
- Never infer parent entity from proximity alone.
- Never copy township or municipality from discovery records.
- Never populate features not documented in authoritative sources.
- `last_verified_date` is left blank when absent — do not generate a date.
- `field_verified` defaults to false when absent — do not assume verified.

------------------------------------------------------------
# 11. AUDITABILITY REQUIREMENTS

Normalization must record in `normalization_provenance`:

- All sources consulted
- All vocabulary mappings applied (ap_type, status)
- All compound type resolutions (IMP-084): raw value, assigned ap_type,
  features update made
- All null-and-log decisions (field, raw value, reason)
- All REVIEW flags issued (field, raw value, reason)
- All empty string → null conversions (§5.18)
- All parent resolution decisions (identity parent type, entity ID or not-found)
- All GPS parsing results from gps_lat_raw + gps_lon_raw
- GPS absence flag (if routed to GPS Acquisition Module)
- All GIS derivation results (township, municipality)
- All features sources
- Identity Notes content surfaced from identity_notes_raw
- Last verified date and field verified outcomes
- All conflicts detected and how handled
- All fields left blank and why
- All delimiter-integrity corrections
- Identity anchor validation result
- Deduplication check result

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This contract depends on:

- **Access Point Vocabulary Module v6.0** (§5.1 mapping tables, compound type
  rules — IMP-084)
- Access Point Schema Module v6.0
- Site Schema Module v6.0 (parent Site validation)
- Trailthing Schema Module v6.0 (parent Trailthing validation)
- Resolution Engine v6.x
- Normalization Engine v6.0
- GPS Acquisition Module v6.x
- Entity Upsert Engine v6.x
- Audit & Logging Module v6.x

------------------------------------------------------------
# END OF ACCESS POINT NORMALIZATION CONTRACT v6.0
