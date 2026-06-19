# NATURAL AREAS PROJECT
# SITE NORMALIZATION CONTRACT v5.5
(Authoritative Field-Level Rules for Normalizing Resolved Site Entities)

This module defines the entity-specific normalization rules applied by the
Normalization Engine v5.x to produce a fully normalized Site entity conforming
to the Site Schema Module v5.x and ready for insertion into the Entity Graph
Schema v5.x.

This contract contains no controlled vocabularies.
All vocabularies are defined in the Site Vocabulary Module v5.x.

This contract is authoritative for Site normalization only.

------------------------------------------------------------
# CHANGES FROM v5.4 → v5.5

- **IMP-049 — Activity detection and mapping in §5.18 Features**: Added activity detection
  rule. Any token in `features_raw` that resolves to a pure activity term (Hiking, Fishing,
  Hunting, Horseback Riding, Mountain Biking, Boating, Paddling, Swimming, Wildlife Viewing,
  etc.) must be dropped or mapped to a physical infrastructure vocabulary term. If a physical
  infrastructure term from the vocabulary represents the activity's enabling infrastructure
  (e.g., Watercraft Access for Paddling; Fishing Area for Fishing), and the source documents
  that physical infrastructure exists at the site, then map to the vocabulary term. If no
  physical infrastructure vocabulary equivalent exists, drop the token entirely.

- **IMP-050 — Operational content detection in §5.18 Features**: Added operational content
  detection rule. Tokens or annotations representing hours, parking, policies, permit
  requirements, seasonal closures, events, or facility sub-detail must be stripped from the
  features token stream before vocabulary mapping. Physical infrastructure terms that carry
  operational annotations are normalized to the bare physical term (e.g., "Picnic Shelter
  (electrical outlets, 50 capacity)" → "Picnic Shelter").

- **IMP-051 — Named entity detection in §5.18 Features**: Strengthened the named entity
  prohibition. Vocabulary mapping must detect and reject tokens that are specific named Trail,
  Access Point, or child Site entities. Detection heuristic: if a token contains a proper noun
  that matches a known Trail, AP, or Site name for this county, or matches the pattern
  "[Proper Name] Trail" / "[Proper Name] Access", it must be dropped. Generic infrastructure
  references that do not name a specific entity ("Hiking Trail", "Bridle Trail") pass through
  to vocabulary mapping normally.

- **IMP-052 — Description redundancy detection in §5.10 Description**: Added explicit
  redundancy detection and stripping rule. If `description_raw` opens with a prohibited
  pattern (acreage+category opener, location opener, name restatement), strip the opener
  and retain any substantive identity remainder. If no substantive identity remainder exists
  after stripping, blank the `description` field. A blank description is preferred over a
  wholly redundant one.

- **IMP-053 — Notes pipeline metadata stripping**: Added pipeline metadata cleansing rule
  to §5.19 Notes. `notes_raw` values containing pipeline provenance markers (tier markers,
  session references, IMP references, OBJECTID annotations, GPS pending notes, discovery
  run labels) must have those markers stripped before writing to `notes`. Legitimate
  operational content and source attribution lines are preserved.

------------------------------------------------------------
# CHANGES FROM v5.3 → v5.4

- Added name suffix normalization rule to §5.1: "Parkland" → "Park" (Columbus-specific CRP naming convention).
  Columbus Recreation & Parks consistently names parcels "X Parkland" in source data while regional sources
  (MORPC, county GIS) use "X Park". This suffix discrepancy causes GPS name-matching failures at Stage 3.
  Normalization must strip the "-land" suffix from "Parkland" names to produce a canonical normalized name.
  Raw name is preserved in name_raw; normalized name is written to name.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.3

- Added normalization rules for new field: partner_agencies
- Updated organizational field cluster to four-tier model:
  ownership, governance, partner_agencies, coordination
- Updated validation rules to reflect new field
- Updated input field model to align with Discovery Output Specification v5.x:
  gps_raw replaced by gps_lat_raw and gps_lon_raw (already split at discovery)
  notes_raw replaced by identity_notes_raw
  url_primary_raw and urls_raw confirmed as canonical raw URL field names
- Discovery Output Specification v5.x retired; all input references now v5.x
- Updated dependencies to v5.x schema
- No changes to identity anchor or identity signature
- No changes to GIS-derived fields or GPS handling
- No changes to discovery expectations

------------------------------------------------------------
# 1. PURPOSE

The Site Normalization Contract v5.3 defines:

- How a Resolved Site is transformed into a Normalized Site
- How each Site Schema v5.x field is validated and normalized
- How Category, Subtype, Designation, Status, and Features are normalized
- How organizational fields (ownership, governance, partner_agencies, coordination) are separated
- How parent-child relationships are validated using the Child Site Rules Module v5.x
- How GPS, Plus Code, Location, and jurisdiction fields are handled
- How normalization interacts with the Normalization Engine v5.x
- How provenance, conflicts, and uncertainties are recorded
- How normalized entities integrate with the Entity Upsert Engine v5.x

Normalization must:

- Never invent data
- Never infer governance, ownership, partner agencies, or identity
- Never silently correct malformed values
- Always log normalization decisions

------------------------------------------------------------
# 2. INPUTS

## 2.1 Resolved Entity Object
From Resolution Engine v5.x, including:

- resolved identity key
- resolved entity_type = "Site"
- resolved parent_site_id (if any)
- resolved county set
- resolved governance, ownership, partner_agencies, coordination
- resolved category, subtype, designation, status
- resolved conflicts and uncertainties

## 2.2 Raw Discovery Record v5.x
Including:

- name_raw
- counties_raw
- ownership_raw
- governance_raw
- partner_agencies_raw (optional; may be absent)
- coordination_raw
- gps_lat_raw
- gps_lon_raw
- location_raw
- url_primary_raw
- urls_raw
- parent_site_raw
- identity_notes_raw
- description_raw
- features_raw
- discovery_metadata

Not in raw discovery (GIS-derived):
- municipality
- township

## 2.3 Normalization Engine Pre-Populated Fields
Before this contract runs, the Normalization Engine v5.x has already:

- Received gps_lat_raw and gps_lon_raw as already-split values from discovery
- Validated gps_lat and gps_lon from gps_lat_raw / gps_lon_raw
- Computed plus_code
- Derived township via GIS spatial lookup
- Derived municipality via GIS spatial lookup

## 2.4 Vocabulary Modules v5.x
- Category, Subtype, Designation, Status, Features

## 2.5 Schema Modules v5.x
- Site Schema Module v5.x
- Child Site Rules Module v5.x

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A Normalized Site Object v5.x conforming to the Site Schema Module v5.x
- A Normalization Provenance Record
- A Validation Result Object
- A normalized entity ready for the Entity Upsert Engine v5.x

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH-LEVEL)

1. Receive Resolved Site
2. Validate identity and entity_type = "Site"
3. Normalize name
4. Normalize Category, Subtype, Designation, Status
5. Normalize organizational fields:
   ownership → governance → partner_agencies → coordination
6. Normalize Counties
7. Validate GPS (gps_lat / gps_lon)
8. Validate Plus Code
9. Validate Township, Municipality
10. Normalize Location
11. Normalize Acres
12. Normalize Features
13. Normalize Description
14. Normalize Notes
15. Normalize URLs
16. Validate Parent Site relationship
17. Run identity anchor deduplication check
18. Validate against Site Schema v5.x
19. Emit Normalized Site + provenance

------------------------------------------------------------
# 5. FIELD-BY-FIELD NORMALIZATION RULES

## 5.1 Name
- Use resolved name or name_raw with minimal whitespace cleanup.
- Never infer from amenities or nearby entities.
- Alternate names → Description or Notes.
- **Columbus CRP "Parkland" suffix normalization**: If name_raw ends with the word "Parkland"
  (case-insensitive, whole-word match), replace the trailing "Parkland" with "Park" to produce
  the normalized name. This is a systematic naming convention used by Columbus Recreation & Parks
  for parcel-level land holdings; regional sources (MORPC, county GIS) consistently omit the
  "-land" suffix. Example: "Amberfield Parkland" → "Amberfield Park".
  Raw name is preserved in name_raw; write normalized form to name only.

## 5.2 Category
- Must match vocabulary.
- Never infer from features or governance.
- Leave blank if ambiguous.

## 5.3 Subtype
- Optional.
- Must match subtype list for chosen Category.
- Leave blank if unclear.

## 5.4 Designation
- Must match vocabulary.
- Semicolon-delimited.
- Never infer from name or category.

## 5.5 Status
- Must match vocabulary.
- "Closed" = permanently closed.
- "Proposed" must be documented.

------------------------------------------------------------
# 5.6 Ownership
- Must contain the exact legal name of the owning entity.
- Must not use generic categories.
- Must not encode governance or partner roles.
- Leave blank if unverifiable.

------------------------------------------------------------
# 5.7 Governance
- Must contain exact names of managing organizations.
- Semicolon-delimited if multiple.
- Must not encode ownership or partner roles.
- If governance = ownership → repeat explicitly.

------------------------------------------------------------
# 5.8 Partner Agencies (NEW IN v5.2)
- Formal, documented co‑operator organizations.
- Must use exact organization names.
- Must not duplicate Ownership or Governance.
- Must not include informal volunteer groups.
- Must be supported by authoritative documentation.
- Leave blank if no formal partners exist.

Examples:
- Ohio Department of Natural Resources (ODNR)
- U.S. Army Corps of Engineers (USACE)
- Metroparks Toledo (when acting as co‑operator)

------------------------------------------------------------
# 5.9 Coordination
- Community-based, volunteer, advisory, or informal partners.
- Must not duplicate Ownership, Governance, or Partner Agencies.
- Must not use generic categories.
- Leave blank if no documented coordination exists.

Examples:
- Friends of Caesar Creek Lake
- Local trail volunteer associations

------------------------------------------------------------
# 5.10 Description
- 1–3 sentences.
- Identity-defining ecological, historical, or physical character.
- Must not include governance, ownership, or amenities.
- Must not contradict controlled fields.

**REDUNDANCY DETECTION AND STRIPPING (IMP-052)**: Before writing to `description`,
apply the following stripping pass to `description_raw`:

1. Detect prohibited openers using these patterns (case-insensitive):
   - `A [N]-acre [category word] ...` — strip the entire opener clause
   - `Located in [place] ...` — strip if nothing substantive follows
   - `[Site name] is a [category] ...` — strip if remainder is only location/governance
   - `A [N]-acre [category] located in [place] ...` — strip the entire combined opener

2. After stripping the opener, evaluate the remainder:
   - If the remainder contains identity-defining content (ecology, history, physical character,
     programmatic distinctiveness, named natural features, cultural significance) → write the
     remainder to `description`
   - If the remainder is only additional location, governance, acreage, or category restatement
     → blank `description`

3. If `description_raw` consists entirely of prohibited opener patterns with no
   substantive remainder, write blank to `description`. Do not log blank descriptions
   as errors — a blank description is the correct normalization outcome when the source
   offers no distinctive identity content.

Fields that must never appear in `description`: governance, ownership, acreage (unless
contextually embedded in identity content), hours, permits, amenity lists.

------------------------------------------------------------
# 5.11 Location
- Full address OR general geographic description.
- Never invent street numbers.
- Must not include county names.
- Must not encode governance or access rules.

------------------------------------------------------------
# 5.12 Acres
- Numeric only.
- Never estimate or average.
- Use most authoritative source.

------------------------------------------------------------
# 5.13 Counties
- Required.
- Alphabetized.
- Semicolon-delimited.
- Must omit the word "County".
- Multi-county Sites remain single entities.

------------------------------------------------------------
# 5.14 Municipality (GIS-derived)
- Must be GIS-derived.
- Must be a valid municipality name or blank.
- Never use discovery values.

------------------------------------------------------------
# 5.15 Township (GIS-derived)
- Must be GIS-derived.
- Must be a valid township name or blank.
- Never use discovery values.

------------------------------------------------------------
# 5.16 GPS (gps_lat / gps_lon)
- Both present or both blank.
- Must be numeric.
- Must be authoritative.
- If invalid → blank both fields.

------------------------------------------------------------
# 5.17 Plus Code
- Must be present if GPS present.
- Must be blank if GPS blank.
- Never manually entered.

------------------------------------------------------------
# 5.18 Features
- Semicolon-delimited.
- Must match vocabulary (Site Vocabulary Module v5.x §6.2).
- Alphabetical order required.
- Metadata in parentheses allowed only for quantity or location disambiguation (e.g., "Picnic Shelter (3)").
- Trails, Trail Segments, Access Points, and child Sites are never Features.

**FEATURES NORMALIZATION SEQUENCE (IMP-049, IMP-050, IMP-051)**:

Apply in this order to each token in `features_raw`:

**Step 1 — Activity detection (IMP-049)**: If the token is a pure activity term, apply the mapping:
- Paddling / Canoeing / Kayaking / Boating → map to "Watercraft Access" if a watercraft launch or access point is documented for the site; otherwise drop
- Fishing → map to "Fishing Area" if a designated fishing area is documented; otherwise drop
- Hunting → map to "Hunting Area" if a designated hunting zone is documented; otherwise drop
- Mountain Biking → map to "Mountain Bike Trail" if a mountain bike trail is documented; otherwise drop
- Horseback Riding → map to "Bridle Trail" if a bridle trail is documented; otherwise drop
- Hiking / Walking / Running → drop entirely (generic trail use is not a physical feature)
- Swimming / Wading → map to "Swimming Area" or "Spray Park" if the physical infrastructure is documented; otherwise drop
- All other activity terms (Wildlife Viewing, Birdwatching, Geocaching, Photography, Mushroom Foraging, Nature Study, Wildflower Study, etc.) → drop entirely

**Step 2 — Operational content stripping (IMP-050)**: Strip any token or annotation that represents:
- Hours of operation (any time or date pattern)
- Parking description or count
- Access policy ("dogs permitted", "no bikes", "permit required")
- Seasonal closure
- Event listing
- Facility sub-detail annotation within parentheses (e.g., "(electrical outlets, 50 capacity)")
Physical feature terms that carry operational annotations are retained with the annotation stripped (e.g., "Picnic Shelter (permit required on weekends)" → "Picnic Shelter").

**Step 3 — Named entity detection (IMP-051)**: If a token names a specific Trail, Access Point, or child Site entity (proper noun + "Trail" / "Access" / "Path" / site name), drop the token. Generic infrastructure references not naming a specific entity pass through to vocabulary mapping.

**Step 4 — Vocabulary mapping**: Map remaining tokens to vocabulary terms per Site Vocabulary Module §6.2. Tokens that do not map to any vocabulary term are dropped (not written to `features`). After mapping, alphabetize and semicolon-delimit.

------------------------------------------------------------
# 5.19 Notes
- Free text.
- Must not contradict controlled fields.
- Use for temporary closures, access nuance, historical context, parcel IDs, citations.

**PIPELINE METADATA CLEANSING (IMP-053)**: Before writing `notes_raw` to `notes`, strip
all pipeline provenance metadata. The `notes` field is a public-facing operational field;
pipeline metadata belongs in `identity_notes` or provenance tables only.

Strip the following patterns (case-insensitive):
- Session references: `Session N:`, `Session N.`, `Session N` (trailing), `Manually assigned Session N`
- IMP references: `(IMP-NNN)`, `(IMP-NNN: description)`, `; IMP-NNN`
- OBJECTID annotations: `(OBJECTID NNN)`, `OBJECTID NNN,`
- GPS provenance notes: `GPS pending verification.`
- Discovery run labels: `Cataloged during [County] County run.`, `Cataloged during [County] County session.`
- Pipeline staging notes: `staged in [file] YAML`, `staged not pipelined`
- Browser retry annotations: `([date] browser retry)`, `(browser JS extraction, [date])`

**Preserve the following** — these are legitimate operational content, not pipeline metadata:
- `Source: [source name] ([date]).` lines — these are attribution and provenance for the note's content
- Operational notes: hours, closures, permit requirements, contact information
- Identity notes written in plain prose (child site relationships, alternate names, GPS rationale)
- Cross-entity references written in plain prose ("Child site of [Site Name] ([site_id]).")

After stripping, clean up residual punctuation artifacts (double spaces, leading/trailing semicolons or periods, orphaned conjunctions).

------------------------------------------------------------
# 5.20 URLs
url_primary:
- Single authoritative URL.
- Must be full https:// URL.

urls:
- Semicolon-delimited list of additional URLs (sourced from urls_raw).
- Remove duplicates.
- Full https:// URLs only.

------------------------------------------------------------
# 5.21 Parent Site
- Blank for top-level Sites.
- Must reference a valid parent_site_id.
- Must follow Child Site Rules Module v5.x.
- Must not be inferred from signage or layout.

------------------------------------------------------------
# 6. IDENTITY ANCHOR VALIDATION

Top-level Sites:
- entity_type + name + counties

Child Sites:
- entity_type + name + counties + parent_site_id

Normalization must verify:
- All anchor fields present
- Counties valid and alphabetized
- Parent Site ID valid if present

------------------------------------------------------------
# 7. VALIDATION LOGIC

Normalization must validate:

- Vocabulary-controlled fields
- Organizational field separation:
  ownership vs governance vs partner_agencies vs coordination
- GPS pairing and numeric format
- Plus Code derivation
- Acres numeric
- Semicolon formatting
- No invented data
- No placeholders
- No delimiter characters inside fields
- Parent Site validity
- Identity anchor completeness

------------------------------------------------------------
# 8. DELIMITER INTEGRITY REQUIREMENTS

- Blank fields must be true blanks.
- No trailing spaces.
- No collapsed semicolons.
- No missing delimiters in multi-value fields.

------------------------------------------------------------
# 9. CONFLICT HANDLING

- Conflicting names → use most authoritative; log alternates.
- Conflicting ownership → flag; never infer.
- Conflicting acreage → use highest-authority source; log conflict.
- Conflicting category → leave blank; log conflict.

------------------------------------------------------------
# 10. MISSING DATA RULES

- Leave blank if unverifiable.
- Never estimate acres.
- Never infer ownership, governance, partner agencies, or designation.
- Never generate GPS without authoritative source.
- Never copy municipality or township from discovery.

------------------------------------------------------------
# 11. AUDITABILITY REQUIREMENTS

Normalization must record:

- All sources consulted
- All vocabulary mappings
- All conflicts
- All blank-field decisions
- All GPS parsing results
- All GIS derivations
- All delimiter corrections
- Identity anchor validation
- Deduplication check results

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This contract depends on:

- Site Vocabulary Module v5.x
- Site Schema Module v5.x
- Child Site Rules Module v5.x
- Discovery Output Specification v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- Entity Graph Schema v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF SITE NORMALIZATION CONTRACT v5.4