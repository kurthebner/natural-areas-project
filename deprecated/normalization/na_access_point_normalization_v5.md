# NATURAL AREAS PROJECT
# ACCESS POINT NORMALIZATION CONTRACT v5.0
(Authoritative Field-Level Rules for Normalizing Resolved Access Point Entities)

This module defines the v5.0 normalization rules applied by the
Normalization Engine v5.0 to transform Resolved Access Point entities into
Normalized Access Point Objects v5.0 ready for insertion into the
Entity Graph Schema v5.0.

This contract contains no controlled vocabularies.
All vocabularies are defined in the Access Point Vocabulary Module v5.0.

This module is authoritative for Access Point normalization only.

------------------------------------------------------------
# CHANGES FROM v4.0

- **`access_level` removed**: No longer a field in the Access Point schema
- **`role` removed**: No longer a field in the Access Point schema
- **`gps_primary` → `gps_lat` + `gps_lon`**: GPS parsing handled by Normalization Engine v5.0; this contract validates the result
- **GPS is required before upsert**: Access Points without GPS are held, not rejected
- **`township` and `municipality`**: Now GIS-derived by Normalization Engine v5.0 — not normalized from raw discovery values
- **`features` added**: Semicolon-delimited list of facilities and amenities at the access point
- **Parent entity rules updated**: Trail added as valid parent alongside Site and Trail Segment
- Updated all version references to v5.0

------------------------------------------------------------
# 1. PURPOSE

The Access Point Normalization Contract v5.0 defines:

- How a Resolved Access Point becomes a Normalized Access Point
- How each Access Point Schema v5.0 field is validated and normalized
- How Access Point Type and Status are normalized
- How Features are normalized
- How identity parents (Site, Trail, or Trail Segment) are validated
- How additional parent associations are normalized for the Entity Graph
- How County, Township, and Municipality are handled
- How GPS, Plus Code, and Address rules are applied
- How normalization interacts with the Normalization Engine v5.0
- How provenance, conflicts, and uncertainties are recorded
- How normalized entities integrate with the Entity Upsert Engine v5.0

Normalization must:
- Never invent data
- Never infer Access Point Type or parent entity
- Never silently correct malformed values
- Always log normalization decisions

Derived Label is not computed here.
It is computed only during TSV output.

------------------------------------------------------------
# 2. INPUTS

## 2.1 Resolved Entity Object
From Resolution Engine v5.0, including:

- resolved identity key
- resolved entity_type = "Access Point"
- resolved access_point_type
- resolved status (if any)
- resolved identity parent (Site, Trail, or Trail Segment)
- resolved additional parent associations (if any)
- resolved county
- resolved conflicts and uncertainties

## 2.2 Raw Discovery Record v5.0
Including:

- access_point_name_raw
- access_point_type_raw
- status_raw
- features_raw
- county_raw
- parent_sites_raw
- parent_trails_raw
- parent_trail_segments_raw
- gps_raw (string "lat,lon" — parsed by Normalization Engine)
- address_raw
- url_primary_raw, url_all_raw
- notes_raw
- map_url_raw
- discovery_tier, discovered_in_tiers
- seeded_from_baseline, baseline_id
- discovery_metadata
- source_map

**Not in raw discovery (GIS-derived):**
- township — populated by Normalization Engine via GIS spatial lookup
- municipality — populated by Normalization Engine via GIS spatial lookup

**Removed from v4.0 raw inputs:**
- access_level_raw — field no longer exists
- role_raw — field no longer exists

## 2.3 Normalization Engine Outputs (Pre-Populated)
Before this contract runs, the Normalization Engine v5.0 has already:

- Parsed gps_raw → gps_lat, gps_lon (numeric)
- Computed plus_code from gps_lat / gps_lon
- Derived township via GIS spatial lookup
- Derived municipality via GIS spatial lookup

This contract validates those results but does not recompute them.

## 2.4 Vocabulary Modules v5.0
- Access Point Vocabulary Module v5.0 (Type, Status)

## 2.5 Schema Modules v5.0
- Access Point Schema Module v5.0
- Site Schema Module v5.0
- Trail Schema Module v5.0
- Trail Segment Schema Module v5.0

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A Normalized Access Point Object v5.0 conforming to the Access Point Schema Module v5.0
- A Normalization Provenance Record
- A Validation Result Object (warnings, errors)
- A normalized entity ready for the Entity Upsert Engine v5.0
  — OR — a held entity record if GPS is missing

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH-LEVEL)

1. Receive Resolved Access Point from Normalization Engine v5.0
2. Validate identity and entity_type = "Access Point"
3. Normalize name
4. Normalize Access Point Type
5. Normalize Status
6. Normalize Features
7. Resolve and validate identity parent (Site, Trail, or Trail Segment)
8. Normalize additional parent associations
9. Normalize County
10. Validate Township, Municipality — pre-populated by GIS lookup
11. Validate GPS (gps_lat / gps_lon) — pre-populated by engine
12. Validate Plus Code — pre-populated by engine
13. Normalize Address
14. Normalize Notes
15. Normalize URLs and Map URL
16. Check GPS presence → if missing, route to held entities
17. Run integrity anchor deduplication check (via Normalization Engine)
18. Validate against Access Point Schema v5.0
19. Emit Normalized Access Point + provenance (or held entity record)

Derived Label is not constructed here.
It is computed only during TSV output.

If any critical step fails → return error to Normalization Engine v5.0.

------------------------------------------------------------
# 5. FIELD-BY-FIELD NORMALIZATION RULES

## 5.1 Name

- Use name_raw with minimal whitespace cleanup.
- Never invent names.
- Never infer names from amenities, parent entity, or context.
- If unnamed → leave blank; normalization constructs a Derived Label from Type + parent name at TSV output time.
- Placeholder names (e.g., "Unnamed Trailhead") → preserve and flag for review.

**Provenance:** Log all corrections and conflicts.

---

## 5.2 Access Point Type

- Must match a controlled value from Access Point Vocabulary Module v5.0.
- Known synonyms must be mapped to canonical values — log all mappings.
- If unmappable → leave blank and flag uncertainty.
- Never infer type from amenities alone.

**Common normalization mappings:**
- "trail head", "trail-head" → "Trailhead"
- "parking lot", "parking" → "Parking Area"
- "boat launch ramp" → "Boat Ramp"
- "kayak launch", "canoe access" → "Watercraft Access Point"
- See Access Point Vocabulary Module v5.0 Section 4 for full mapping table.

**Provenance:** Log all mappings and unmappable values.

---

## 5.3 Access Level ✨ REMOVED IN v5.0

- `access_level` is no longer a field in the Access Point schema.
- If access level values are present in resolved records from older discovery runs → silently drop.
- Do not migrate to any other field.
- Access restriction information may be preserved in Notes if operationally relevant.

---

## 5.4 Role ✨ REMOVED IN v5.0

- `role` is no longer a field in the Access Point schema.
- If role values are present in resolved records from older discovery runs → silently drop.
- Do not migrate to any other field.

---

## 5.5 Status

- Must match a controlled value from Access Point Vocabulary Module v5.0.
- If unmappable → leave blank and flag uncertainty.
- "Closed" = permanently or indefinitely closed.
- "Seasonal" requires season details in Notes.
- Leave blank if status is ambiguous or undocumented.

**Common normalization mappings:**
- "open", "operational" → "Active"
- "seasonal access" → "Seasonal"
- "permanently closed" → "Closed"
- "permit required" → "Restricted"

---

## 5.6 Features ✨ NEW IN v5.0

- Semicolon-delimited list of facilities and amenities at the access point.
- Free-text — no controlled vocabulary.
- Normalize capitalization to title case for consistency.
- Metadata in parentheses is permitted: "parking (50 spaces, paved)", "restrooms (ADA, seasonal)"
- Must describe features of the access point itself, not the parent entity.
- Remove obvious duplicates.
- Leave blank if no features are documented.

**Examples of valid normalized values:**
- "restrooms;water fountain;parking (50 spaces, paved, 4 ADA);bike racks"
- "pit toilet;gravel parking (20 spaces);picnic table"
- "seasonal restrooms;parking;boat ramp;fishing pier"

**What NOT to include:**
- Features of the parent Site, Trail, or Trail Segment
- Inferred amenities

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
  - If ambiguity remains → leave identity parent blank, surface to Resolution Engine.
- Never infer parent from proximity alone.
- Never assign multiple identity parents.

**Provenance:** Log all parent resolution decisions and conflicts.

---

## 5.8 Additional Parent Associations

- Additional parents (Site, Trail, Trail Segment) beyond the identity parent may be preserved.
- Written to the `access_point_parents` relationship table.
- Must not contradict the identity parent.
- Must be supported by authoritative sources.
- Never infer additional parents from proximity or geometry.

**Examples:**
- A trailhead at the junction of two trails may have both trails as parents.
- A parking area serving both a site and a trailhead may have both as parents.

**Provenance:** Log all additional parent associations.

---

## 5.9 County

- Required — single value only.
- Must match official Ohio county name.
- Must represent the county where the Access Point physically resides.
- Omit the word "County" (e.g., "Wood County" → "Wood").
- Must not be inferred solely from parent entity's county list.
- Multi-county logic does not apply — Access Points are point locations.

---

## 5.10 Township ✨ GIS-DERIVED IN v5.0

**DO NOT normalize from raw discovery values.**

- Populated by Normalization Engine v5.0 via GIS spatial lookup.
- This contract validates that the field is either:
  - A recognized civil township name (without "Township" appended), or
  - Blank (GIS lookup failed or GPS unavailable)
- Never copy township_raw from discovery records.

---

## 5.11 Municipality ✨ GIS-DERIVED IN v5.0

**DO NOT normalize from raw discovery values.**

- Populated by Normalization Engine v5.0 via GIS spatial lookup.
- This contract validates that the field is either:
  - A recognized municipality name (city or village), or
  - Blank (access point is outside any municipality boundary)
- Never copy municipality_raw from discovery records.

---

## 5.12 GPS (gps_lat / gps_lon) ✨ UPDATED FROM v4.0

**GPS parsing is handled by the Normalization Engine v5.0.**
This contract validates the result:

- Both gps_lat and gps_lon must be present, or both must be blank.
- gps_lat must be in range [-90, 90].
- gps_lon must be in range [-180, 180].
- Both must be numeric (float).
- Must represent an authoritative coordinate — no placeholders, no centroids.
- If validation fails → log error, blank both fields.

**GPS is required before upsert:**
- If gps_lat and gps_lon are blank after normalization → route to **held entities** with `hold_reason = missing_gps`.
- Do not reject — hold pending GPS acquisition.
- Access Points cannot be included in the statewide database without GPS.

---

## 5.13 Plus Code ✨ UPDATED FROM v4.0

**Plus Code computation is handled by the Normalization Engine v5.0.**
This contract validates:

- If gps_lat and gps_lon are present → plus_code must be present and well-formed.
- If GPS is blank → plus_code must be blank.
- Never manually enter a Plus Code.

---

## 5.14 Address

- Preserve with minimal cleanup (trim whitespace, fix obvious encoding issues).
- Never invent or USPS-normalize.
- Partial addresses and road descriptions are valid.
- Leave blank if no authoritative or defensible address exists.

**Valid address forms:**
- "18331 Carter Road, Bowling Green, OH 43402"
- "State Route 6 at Metzger Marsh Road"
- "0.5 miles north of Bowling Green on SR 25"

---

## 5.15 Notes

- Preserve access-related operational notes.
- Use for: gate hours, parking constraints, seasonal conditions, surface/grade issues, fees, signage visibility.
- Must not include features (those belong in Features field).
- Must not include identity-defining information.
- Notes may be concatenated from multiple raw sources — log concatenation.
- Leave blank if no relevant notes.

---

## 5.16 URLs

**`url_primary`:**
- Full https:// URL to primary authoritative source.
- Single value.
- Remove tracking parameters.

**`url_all` (additional URLs):**
- Semicolon-delimited.
- Full https:// URLs only.
- Remove duplicates.
- Remove tracking parameters.

---

## 5.17 Map URL

- Full https:// URL to a map showing this access point.
- Semicolon-delimited if multiple.
- May include PDF maps, interactive viewers, GIS layers.
- Leave blank if none.

------------------------------------------------------------
# 6. GPS HOLD WORKFLOW

Access Points without GPS after normalization are not rejected — they are held.

**Hold trigger:** gps_lat and gps_lon are both blank after normalization.

**Hold process:**
1. Route entity to `held_entities` table with `hold_reason = missing_gps`.
2. Preserve all other normalized fields.
3. Log hold in normalization provenance.

**Release trigger:**
- On subsequent normalization runs, if GPS has been acquired (via batch geocoding or manual entry) → release and upsert.
- See Entity Upsert Engine v5.0 Section 8 for held entity release workflow.

**Note:** GPS acquisition for held Access Points is a separate workflow — batch geocoding from address, manual GPS assignment from map tools, or field verification. This contract does not define that workflow.

------------------------------------------------------------
# 7. IDENTITY ANCHOR VALIDATION

The integrity anchor for Access Points is:
`entity_type` + `access_point_type` + `identity_parent_entity_type` + `identity_parent_entity_id` + `county`

This contract must verify:
- All anchor fields are present (or identity_parent fields are blank with a logged reason)
- County is a valid single value
- Identity parent references a valid entity

The Normalization Engine v5.0 runs the deduplication check after this validation.

------------------------------------------------------------
# 8. VALIDATION LOGIC

Normalization must validate:

- Access Point Type maps to valid vocabulary value
- Status maps to valid vocabulary value (if present)
- County: single value, "County" stripped, valid Ohio county name
- GPS: both gps_lat and gps_lon present or both blank; values in valid range
- Plus Code: present if GPS present, blank if GPS blank
- Features: semicolon-delimited, no empty segments
- Parent entity: references valid entity in Entity Graph
- No invented data
- Blank fields are true blanks
- No delimiter characters inside field values

If any field fails validation:
- Surface as warning or error (per severity)
- Do not silently correct
- Log in normalization provenance

------------------------------------------------------------
# 9. DELIMITER INTEGRITY REQUIREMENTS

Normalization must ensure:

- Blank fields are true blanks
- No spaces between semicolons and values
- No trailing spaces or newlines within fields
- No collapsed delimiters (consecutive semicolons)
- No missing delimiters in multi-value fields

All anomalies must be logged.

------------------------------------------------------------
# 10. CONFLICT HANDLING

### 10.1 Conflicting Names
- Use the most authoritative source.
- Log conflict in normalization provenance.

### 10.2 Conflicting Access Point Type
- Use authoritative documentation.
- If unclear → leave blank, flag uncertainty.

### 10.3 Conflicting Parent Entities
- Preserve all claims in metadata.
- Do not assign an identity parent until conflict is resolved.
- Surface to Resolution Engine.

### 10.4 Conflicting GPS
- Use most authoritative source (agency GIS preferred over third-party).
- Log conflict and source of accepted coordinates.

### 10.5 Conflicting County
- Use county derived from GPS coordinates if available.
- Otherwise use most authoritative source.
- Log conflict.

------------------------------------------------------------
# 11. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.
- Never estimate GPS coordinates.
- Never infer Access Point Type from amenities alone.
- Never infer parent entity from proximity alone.
- Never copy township or municipality from discovery records.
- Never populate features not documented in authoritative sources.

------------------------------------------------------------
# 12. AUDITABILITY REQUIREMENTS

Normalization must record in `normalization_provenance`:

- All sources consulted
- All vocabulary mappings applied (Type, Status)
- All parent resolution decisions
- All GPS parsing results
- All GIS derivation results (township, municipality)
- All features sources
- GPS hold decisions (if triggered)
- All conflicts detected and how handled
- All fields left blank and why
- All delimiter-integrity corrections
- Identity anchor validation result
- Deduplication check result

Never overwrite previously logged normalization decisions.

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This contract depends on:

- Access Point Vocabulary Module v5.0
- Access Point Schema Module v5.0
- Site Schema Module v5.0
- Trail Schema Module v5.0
- Trail Segment Schema Module v5.0
- Discovery Output Specification v5.0
- Resolution Engine v5.0
- Normalization Engine v5.0
- Entity Graph Schema v5.0
- Audit & Logging Module v5.0

------------------------------------------------------------
# END OF ACCESS POINT NORMALIZATION CONTRACT v5.0
