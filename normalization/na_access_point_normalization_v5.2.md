# NATURAL AREAS PROJECT
# ACCESS POINT NORMALIZATION CONTRACT v5.2
(Authoritative Field-Level Rules for Normalizing Resolved Access Point Entities)

This module defines the v5.2 normalization rules applied by the
Normalization Engine v5.x to transform Resolved Access Point entities into
Normalized Access Point Objects ready for insertion into the Entity Graph.

This contract contains no controlled vocabularies.
All vocabularies are defined in the **Access Point Vocabulary Module v5.3**.

This module is authoritative for Access Point normalization only.

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

**IMP-100 — AP vocabulary enforcement hardening.**

- **§5.2 Access Point Type**: Added mandatory read gate for AP Vocabulary
  §5.1 mapping table. Added compound type enforcement rule (IMP-084):
  "Trailhead/Parking" and similar compound values → assign "Trailhead" as
  `ap_type`; parking represented in `features` as "Parking Area". Added
  enforcement language: null-and-log on unmappable values (replacing the
  weaker "leave blank and flag"). Added empty string → null rule (§5.18).

- **§5.5 Status**: Added mandatory read gate for AP Vocabulary §5.1 status
  mapping table. Made "open"/"operational" → "Active" normalization explicit.
  Added enforcement language: null-and-log on unmappable values. Added
  empty string → null rule (§5.18).

- **§5.18 Empty String Enforcement (new)**: Both vocabulary-controlled AP
  fields (`ap_type`, `status`) treat empty string ("") as a data defect —
  convert to null and log. Run after the field-level normalization steps,
  before integrity anchor validation.

- **Module dependency updated**: References now cite Access Point Vocabulary
  Module v5.3 (compound type rule, IMP-084 resolved in v5.3 of that module).

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **identity_notes added**: New normalized field surfaced from
  identity_notes_raw; distinct from notes; used for identity
  clarifications, type uncertainty flags, and parent assignment notes
- **Map URL removed**: map_url_raw no longer a raw input; map URLs
  captured in urls_raw at discovery and url at normalized stage
- **Raw input field renames**:
  - notes_raw → identity_notes_raw (identity clarifications)
  - url_all_raw → urls_raw (all URLs including map URLs)
  - url_primary → url_primary_raw
  - map_url_raw removed
  - gps_raw → gps_lat_raw + gps_lon_raw (split at discovery stage)
- **GPS Hold Workflow removed**: GPS acquisition now handled by GPS
  Acquisition Module (Stage 3 of pipeline), consistent with all entities;
  no separate held_entities batch geocoding process
- **Derived Label removed**: No longer computed or stored at any stage
- **Normalization workflow updated**: Steps revised for removed and
  added fields; GPS hold step replaced with GPS Acquisition Module
  routing note
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- `access_level` removed — field no longer exists
- `role` removed — field no longer exists
- `gps_primary` → `gps_lat` + `gps_lon` — GPS parsing handled by engine
- GPS required before upsert — Access Points without GPS held pending
  acquisition (now handled by GPS Acquisition Module in v5.1)
- `township` and `municipality` — GIS-derived only, not from discovery
- `features` added — semicolon-delimited facilities and amenities
- Parent entity rules updated — Trail added as valid parent

------------------------------------------------------------
# 1. PURPOSE

The Access Point Normalization Contract v5.2 defines:

- How a Resolved Access Point becomes a Normalized Access Point
- How each Access Point Schema v5.x field is validated and normalized
- How Access Point Type is normalized, including compound-type resolution (IMP-084)
- How Status is normalized
- How Features are normalized
- How Identity Notes are surfaced from identity_notes_raw
- How identity parents (Site, Trail, or Trail Segment) are validated
- How additional parent associations are normalized for the Entity Graph
- How County, Township, and Municipality are handled
- How GPS and Plus Code rules are applied
- How normalization interacts with the Normalization Engine v5.x
- How provenance, conflicts, and uncertainties are recorded
- How normalized entities integrate with the Entity Upsert Engine v5.x

Normalization must:
- Never invent data
- Never infer Access Point Type or parent entity
- Never silently correct malformed values
- Always log normalization decisions

------------------------------------------------------------
# 2. INPUTS

## 2.1 Resolved Entity Object
From Resolution Engine v5.x, including:

- resolved identity key
- resolved entity_type = "Access Point"
- resolved access_point_type
- resolved status (if any)
- resolved identity parent (Site, Trail, or Trail Segment)
- resolved additional parent associations (if any)
- resolved county
- resolved conflicts and uncertainties

## 2.2 Raw Discovery Record v5.1
Including:

- access_point_name_raw
- access_point_type_raw
- status_raw
- features_raw
- county_raw
- parent_sites_raw
- parent_trails_raw
- parent_trail_segments_raw
- gps_lat_raw (string, as found)
- gps_lon_raw (string, as found)
- address_raw
- url_primary_raw
- urls_raw (all URLs including any map URLs)
- identity_notes_raw
- discovery_tier, discovered_in_tiers
- seeded_from_baseline, baseline_id
- discovery_metadata
- source_map

**Removed from v5.0 raw inputs:**
- notes_raw — renamed to identity_notes_raw
- url_all_raw — renamed to urls_raw
- map_url_raw — removed; map URLs now in urls_raw
- gps_raw — replaced by gps_lat_raw + gps_lon_raw

**Not in raw discovery (GIS-derived):**
- township — populated by Normalization Engine via GIS spatial lookup
- municipality — populated by Normalization Engine via GIS spatial lookup

**Removed from v4.0 raw inputs:**
- access_level_raw — field no longer exists
- role_raw — field no longer exists

## 2.3 Normalization Engine Outputs (Pre-Populated)
Before this contract runs, the Normalization Engine v5.x has already:

- Parsed gps_lat_raw + gps_lon_raw → gps_lat, gps_lon (numeric)
- Computed plus_code from gps_lat / gps_lon (if GPS present)
- Derived township via GIS spatial lookup
- Derived municipality via GIS spatial lookup

This contract validates those results but does not recompute them.

## 2.4 Vocabulary Modules
- **Access Point Vocabulary Module v5.3** — ap_type, Status;
  §5.1 normalization mapping table; §2.2 compound type rules (IMP-084).
  **Read §5.1 before normalizing ap_type or status.**

## 2.5 Schema Modules v5.x
- Access Point Schema Module v5.x
- Site Schema Module v5.x
- Trail Schema Module v5.x
- Trail Segment Schema Module v5.x

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A **Normalized Access Point Object v5.2** conforming to the Access Point
  Schema Module v5.x
- A **Normalization Provenance Record**
- A **Validation Result Object** (warnings, errors)
- A normalized entity ready for the **Entity Upsert Engine v5.x**,
  OR a flagged entity routed to the GPS Acquisition Module if GPS is absent

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH-LEVEL)

1.  Receive Resolved Access Point from Normalization Engine v5.x
2.  Validate identity and entity_type = "Access Point"
3.  **Read Access Point Vocabulary Module v5.3 §5.1** (ap_type and status
    mapping tables, compound type rules)
4.  Normalize Name
5.  Normalize Access Point Type (apply §5.1 ap_type mapping; apply IMP-084
    compound type rule)
6.  Normalize Status (apply §5.1 status mapping)
7.  Normalize Features (update features when compound type rule fires)
8.  Resolve and validate identity parent (Site, Trail, or Trail Segment)
9.  Normalize additional parent associations
10. Normalize County
11. Validate Township, Municipality — pre-populated by GIS lookup
12. Validate GPS (gps_lat / gps_lon) — pre-populated by engine from
    gps_lat_raw + gps_lon_raw
13. Validate Plus Code — pre-populated by engine
14. Normalize Address
15. Normalize Identity Notes
16. Normalize Notes
17. Normalize URL (including any map URLs from urls_raw)
18. Apply §5.18 empty string enforcement across vocabulary fields
19. Check GPS presence → if absent, flag for GPS Acquisition Module
20. Run integrity anchor deduplication check (via Normalization Engine)
21. Validate against Access Point Schema v5.x
22. Emit Normalized Access Point + provenance

If any critical step fails → return error to Normalization Engine v5.x.

------------------------------------------------------------
# 5. FIELD-BY-FIELD NORMALIZATION RULES

## 5.1 Name

- Use name_raw with minimal whitespace cleanup.
- Never invent names.
- Never infer names from amenities, parent entity, or context.
- If unnamed → leave blank; a name may be constructed from Type +
  parent name during TSV output if needed.
- Placeholder names (e.g., "Unnamed Trailhead") → preserve and flag
  for review.

**Provenance:** Log all corrections and conflicts.

---

## 5.2 Access Point Type

**Read Access Point Vocabulary Module v5.3 §5.1 before applying this step.**

- Single value only — compound values are never valid in `ap_type`.
- Never infer type from amenities or GPS alone.

**Normalization procedure:**

1. Check `access_point_type_raw` against the §5.1 ap_type mapping table.
2. If the raw value maps to a single controlled value → apply the mapping; log.
3. **Compound type rule (IMP-084):** If the raw value combines Trailhead with
   Parking Area (e.g., "Trailhead/Parking", "Trailhead & Parking", "Trailhead
   with Parking"):
   - Assign `ap_type = "Trailhead"` (trail access function takes precedence).
   - Ensure `features` contains `"Parking Area"` (add if not already present;
     annotate with space count if documented, e.g., `"Parking Area (8 spaces)"`).
   - Log the compound raw value and the resolution in `normalization_provenance`.
4. **Compound type rule — Parking + Trailhead (reverse case):** If the raw
   value leads with Parking Area as the primary function and trailhead access
   is secondary:
   - Assign `ap_type = "Parking Area"`.
   - Add `"Trailhead"` to `features` only if the source explicitly designates
     it as a trailhead. Do not add "Trailhead" to features based solely on
     proximity to a trail.
   - Log resolution.
5. If the raw value is any other compound or ambiguous value → route to
   **REVIEW**; flag in `identity_notes`; leave `ap_type` blank until resolved.
6. If the raw value is unmappable and not compound → **null-and-log**: leave
   blank, record the raw value and reason in `normalization_provenance`.
7. Empty string ("") → null; see §5.18.

**Common mappings (non-exhaustive — AP Vocabulary §5.1 is authoritative):**
- "trail head" / "trail-head" → "Trailhead"
- "trailhead/parking" / "trailhead & parking" → "Trailhead" (+ Parking Area in features)
- "parking lot" / "parking" → "Parking Area"
- "boat launch ramp" → "Boat Ramp"
- "kayak launch" / "canoe access" → "Watercraft Access Point"
- "pulloff" / "pull off" → "Roadside Pull-Off"
- "portage" / "mandatory portage" / "carry" → "Hazard Portage"
- "dam portage" / "dam carry" → "Hazard Portage"

**Provenance:** Log all mappings, compound resolutions, and unmappable values.

---

## 5.3 Access Level — REMOVED IN v5.0

- `access_level` is no longer a field.
- If present in older resolved records → silently drop.
- Access restriction information may be preserved in Notes if operationally
  relevant.

---

## 5.4 Role — REMOVED IN v5.0

- `role` is no longer a field.
- If present in older resolved records → silently drop.

---

## 5.5 Status

**Read Access Point Vocabulary Module v5.3 §5.1 before applying this step.**

- Optional. Single value only.
- "Closed" = permanently or indefinitely closed.
- "Seasonal" requires season details in Notes.
- Leave blank if status is ambiguous or undocumented.

**Normalization procedure:**

1. Check `status_raw` against the §5.1 status mapping table.
2. If the raw value maps to a controlled value → apply the mapping; log.
   - "open" / "operational" → "Active"
   - "seasonal access" → "Seasonal"
   - "permanently closed" / "decommissioned" → "Closed"
   - "permit required" → "Restricted"
3. If the raw value is unmappable → **null-and-log**: leave blank, record
   the raw value and reason in `normalization_provenance`.
4. Empty string ("") → null; see §5.18.

---

## 5.6 Features

- Semicolon-delimited list of facilities and amenities at the access point.
- Free-text — no controlled vocabulary.
- Normalize capitalization to title case for consistency.
- Metadata in parentheses is permitted: "Parking (50 spaces, paved)",
  "Restrooms (ADA, seasonal)"
- Must describe features of the access point itself, not the parent entity.
- Remove obvious duplicates.
- Leave blank if no features are documented.
- **When compound type rule fires (§5.2):** Ensure "Parking Area" (with
  any documented capacity annotation) appears in features for records where
  `ap_type = "Trailhead"` was resolved from a compound raw value.

**Examples of valid normalized values:**
- "Restrooms;Water Fountain;Parking (50 spaces, paved, 4 ADA);Bike Racks"
- "Pit Toilet;Gravel Parking (20 spaces);Picnic Table"
- "Seasonal Restrooms;Parking;Boat Ramp;Fishing Pier"

**Provenance:** Log source URL for features if different from primary URL.

---

## 5.7 Parent Entity (Identity Parent)

An Access Point must have exactly one identity parent — the single entity
that primarily defines where this access point belongs.

**Valid identity parent types:**
- Site
- Trail
- Trail Segment

**Not valid as identity parents:**
- Trail Networks
- Site Networks

**Resolution rules:**
- Identity parent must be a normalized entity in the Entity Graph.
- If multiple parent candidates exist:
  - Prefer Trail Segment if the AP is clearly a segment-specific trailhead.
  - Prefer Trail if the AP serves the trail system generally.
  - Prefer Site if the AP is primarily a site entrance.
  - If ambiguity remains → leave identity parent blank, surface to
    Resolution Engine; log in identity_notes.
- Never infer parent from proximity alone.
- Never assign multiple identity parents.

**Provenance:** Log all parent resolution decisions and conflicts.

---

## 5.8 Additional Parent Associations

- Additional parents (Site, Trail, Trail Segment) beyond the identity
  parent may be preserved.
- Written to the `access_point_parents` relationship table.
- Must not contradict the identity parent.
- Must be supported by authoritative sources.
- Never infer additional parents from proximity or geometry.

**Provenance:** Log all additional parent associations.

---

## 5.9 County

- Required — single value only.
- Must match official Ohio county name.
- Must represent the county where the Access Point physically resides.
- Omit the word "County."
- Must not be inferred solely from parent entity's county list.
- Multi-county logic does not apply — Access Points are point locations.

---

## 5.10 Township — GIS-DERIVED

**DO NOT normalize from raw discovery values.**

- Populated by Normalization Engine v5.x via GIS spatial lookup.
- This contract validates that the field is either a recognized civil
  township name (without "Township" appended), or blank.
- Never copy township from discovery records.

---

## 5.11 Municipality — GIS-DERIVED

**DO NOT normalize from raw discovery values.**

- Populated by Normalization Engine v5.x via GIS spatial lookup.
- This contract validates that the field is either a recognized
  municipality name (city or village), or blank.
- Never copy municipality from discovery records.

---

## 5.12 GPS (gps_lat / gps_lon)

**GPS parsing is handled by the Normalization Engine v5.x from
gps_lat_raw + gps_lon_raw.**

This contract validates the result:

- Both gps_lat and gps_lon must be present, or both must be blank.
- gps_lat must be in range [-90, 90].
- gps_lon must be in range [-180, 180].
- Both must be numeric (float).
- Must represent an authoritative coordinate — no placeholders, no
  centroids.
- If validation fails → log error, blank both fields.

**If GPS is absent after normalization:**
- Flag entity for GPS Acquisition Module (Stage 3 of pipeline).
- Preserve all other normalized fields.
- Log GPS absence in normalization provenance.
- Do not reject — GPS Acquisition Module will attempt to acquire
  coordinates from address, map lookup, or other methods.
- Access Points cannot be included in the statewide database without GPS.

---

## 5.13 Plus Code

**Plus Code computation is handled by the Normalization Engine v5.x.**

This contract validates:
- If gps_lat and gps_lon are present → plus_code must be present and
  well-formed.
- If GPS is blank → plus_code must be blank.
- Never manually enter a Plus Code.

---

## 5.14 Address

- Preserve with minimal cleanup (trim whitespace, fix obvious encoding
  issues).
- Never invent or USPS-normalize.
- Partial addresses and road descriptions are valid.
- Leave blank if no authoritative or defensible address exists.

**Valid address forms:**
- "18331 Carter Road, Bowling Green, OH 43402"
- "State Route 6 at Metzger Marsh Road"
- "0.5 miles north of Bowling Green on SR 25"

---

## 5.15 Identity Notes

Surfaced from `identity_notes_raw` at discovery stage.

**Use for:**
- Access point type uncertainty flags
- Parent entity assignment uncertainty or conflict
- Disambiguation notes (e.g., why this is an Access Point vs. a feature)
- Vocabulary type flags (e.g., "source calls this 'boardwalk access' —
  no vocabulary match, flagged for review")
- REVIEW flags from normalization (compound or ambiguous ap_type pending
  resolution)
- Notes added during Resolution or Normalization passes

**Rules:**
- Must not duplicate Notes content
- Must not contain operational or contextual notes (those go in Notes)
- Preserve uncertainty flags — do not resolve silently

---

## 5.16 Notes

- Preserve access-related operational notes.
- Use for: gate hours, parking constraints, seasonal conditions,
  surface/grade issues, fees, signage visibility.
- Must not include features (those belong in Features field).
- Must not include identity-defining information.
- Notes may be concatenated from multiple raw sources — log concatenation.
- Leave blank if no relevant notes.

---

## 5.17 URL

- Full https:// URL to primary authoritative source.
- Semicolon-delimit if multiple authoritative URLs exist.
- Include map URLs (authoritative maps, GIS viewers, PDF maps) as
  additional semicolon-delimited values — no separate Map URL field exists.
- Remove tracking parameters.
- Leave blank if no authoritative URL exists.

---

## 5.18 Empty String Enforcement (IMP-100)

**Run this step after normalizing all vocabulary-controlled fields and before
the GPS presence check and integrity anchor validation step.**

Empty string (`""`) is not a valid blank in any vocabulary-controlled Access
Point field. It is a data defect produced when a raw value was present but
normalization did not assign a controlled value. It must not persist into the
normalized entity.

**Applies to both controlled fields:**
- `ap_type`
- `status`

**Rule:** For each controlled field, if the value is an empty string after the
field-level normalization step:
1. Convert to null (true blank).
2. Log in `normalization_provenance`: `{field}: empty string converted to null`.
3. Do not route to REVIEW — empty string is a mechanical defect, not an
   ambiguous value. (If the original `_raw` field contained a meaningful value
   that could not be mapped, the null-and-log at the field level already
   captured it.)

This rule applies regardless of whether the empty string originated from the
raw record, from a failed mapping attempt, or from any intermediate processing.

------------------------------------------------------------
# 6. IDENTITY ANCHOR VALIDATION

The integrity anchor for Access Points is:
`entity_type` + `access_point_type` + `identity_parent_entity_type`
+ `identity_parent_entity_id` + `county`

This contract must verify:
- All anchor fields are present (or identity_parent fields are blank
  with a logged reason)
- County is a valid single value
- Identity parent references a valid entity

The Normalization Engine v5.x runs the deduplication check after this
validation.

------------------------------------------------------------
# 7. VALIDATION LOGIC

Normalization must validate:

- Access Point Type maps to valid vocabulary value (per AP Vocabulary v5.3)
- Status maps to valid vocabulary value if present (per AP Vocabulary v5.3)
- No vocabulary-controlled field contains an empty string (§5.18)
- County: single value, "County" stripped, valid Ohio county name
- GPS: both gps_lat and gps_lon present or both blank; values in valid
  range
- Plus Code: present if GPS present, blank if GPS blank
- Features: semicolon-delimited, no empty segments
- Parent entity: references valid entity in Entity Graph
- No invented data
- Blank fields are true blanks (null, not empty string)
- No delimiter characters inside field values

If any field fails validation:
- Surface as warning or error (per severity)
- Do not silently correct
- Log in normalization provenance

------------------------------------------------------------
# 8. DELIMITER INTEGRITY REQUIREMENTS

Normalization must ensure:

- Blank fields are true blanks (null, not empty string)
- No spaces between semicolons and values
- No trailing spaces or newlines within fields
- No collapsed delimiters (consecutive semicolons)
- No missing delimiters in multi-value fields

All anomalies must be logged.

------------------------------------------------------------
# 9. CONFLICT HANDLING

### 9.1 Conflicting Names
- Use the most authoritative source.
- Log conflict in normalization provenance.

### 9.2 Conflicting Access Point Type
- Use authoritative documentation.
- If unclear → leave blank, flag in identity_notes.

### 9.3 Conflicting Parent Entities
- Preserve all claims in metadata.
- Do not assign an identity parent until conflict is resolved.
- Surface to Resolution Engine; log in identity_notes.

### 9.4 Conflicting GPS
- Use most authoritative source (agency GIS preferred over third-party).
- Log conflict and source of accepted coordinates.

### 9.5 Conflicting County
- Use county derived from GPS coordinates if available.
- Otherwise use most authoritative source.
- Log conflict.

------------------------------------------------------------
# 10. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.
- Never estimate GPS coordinates.
- Never infer Access Point Type from amenities alone.
- Never infer parent entity from proximity alone.
- Never copy township or municipality from discovery records.
- Never populate features not documented in authoritative sources.

------------------------------------------------------------
# 11. AUDITABILITY REQUIREMENTS

Normalization must record in `normalization_provenance`:

- All sources consulted
- All vocabulary mappings applied (ap_type, status) — field, raw value,
  mapped value, mapping rule applied
- All compound type resolutions (IMP-084): raw value, assigned ap_type,
  features update made
- All null-and-log decisions (field, raw value, reason)
- All REVIEW flags issued (field, raw value, reason)
- All empty string → null conversions (§5.18)
- All parent resolution decisions
- All GPS parsing results (from gps_lat_raw + gps_lon_raw)
- GPS absence flag (if routed to GPS Acquisition Module)
- All GIS derivation results (township, municipality)
- All features sources
- Identity Notes content surfaced from identity_notes_raw
- All conflicts detected and how handled
- All fields left blank and why
- All delimiter-integrity corrections
- Identity anchor validation result
- Deduplication check result

Never overwrite previously logged normalization decisions.

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This contract depends on:

- **Access Point Vocabulary Module v5.3** (§5.1 mapping tables, §2.2
  compound type rules — IMP-084)
- Access Point Schema Module v5.x
- Site Schema Module v5.x
- Trail Schema Module v5.x
- Trail Segment Schema Module v5.x
- Discovery Output Specification v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- GPS Acquisition Module v5.x
- Entity Upsert Engine v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF ACCESS POINT NORMALIZATION CONTRACT v5.2
