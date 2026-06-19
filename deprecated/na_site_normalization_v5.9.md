# NATURAL AREAS PROJECT
# SITE NORMALIZATION CONTRACT v5.9
(Authoritative Field-Level Rules for Normalizing Resolved Site Entities)

This module defines the entity-specific normalization rules applied by the
Normalization Engine v5.x to produce a fully normalized Site entity conforming
to the Site Schema Module v5.x and ready for insertion into the Entity Graph
Schema v5.x.

This contract contains no controlled vocabularies.
All vocabularies are defined in the Site Vocabulary Module v5.x.

This contract is authoritative for Site normalization only.

------------------------------------------------------------
# CHANGES FROM v5.8 → v5.9

- **IMP-063 — Category vocabulary enforcement**: Replaced the sparse §5.2 Category rule with full
  vocabulary validation logic. Invalid values now trigger FATAL REJECT or flag-for-review per the
  mapping table in Site Vocabulary Module v5.5 §7.1. Added cultural institution name-pattern check
  per §7.2 — if recorded category = "Recreation Facility" and name matches a cultural institution
  pattern, flag as CATEGORY MISMATCH for human review.

- **IMP-064 — Subtype vocabulary enforcement**: Replaced the sparse §5.3 Subtype rule with full
  per-category validation logic. Invalid subtype values are mapped or nulled per Site Vocabulary
  Module v5.5 §7.3. Ecological descriptors misplaced in Nature Preserve subtype are nulled and
  routed to description. Features-vocabulary terms misplaced in Recreation Facility subtype are
  nulled and moved to features.

- **IMP-065 — Deterministic subtype inference**: Added §5.3a Deterministic Subtype Inference.
  When subtype is blank after vocabulary validation, name-keyword inference is applied for Nature
  Preserve, Water Site, Recreation Facility, and Campground per Site Vocabulary Module v5.5 §7.4.

- **IMP-066 — Municipality GIS derivation — explicit call specification**: Added explicit GIS
  utility call specification to §5.14. The normalization engine must call
  `na_township_lookup.OhioTownshipLookup.get_both(lat, lon)` and route the result: if
  `(None, municipality)` is returned, populate `municipality` and leave `township` blank; if
  `(township, None)` is returned, populate `township` as "[Name] Township" and leave `municipality`
  blank. If GPS is null, leave both blank.

- **IMP-069 — GPS gate before output**: Added §5.16a GPS Gate. No site may proceed to TSV Output
  (Stage 4) or Database Upsert unless `gps_lat` and `gps_lon` are non-null, OR
  `gps_unresolvable = true` is explicitly set. GPS-null sites with no unresolvable flag are routed
  to `held_entities` with `hold_reason = "gps_missing"`.

------------------------------------------------------------
# CHANGES FROM v5.6 → v5.7

- **IMP-059/IMP-060 — Formula description detection and acreage source mismatch**: Expanded
  §5.10 with explicit REJECT patterns for CRP-style formula descriptions and acreage
  cross-check rule. Added acreage source documentation requirement to §5.12.

------------------------------------------------------------
# CHANGES FROM v5.5 → v5.6

- **IMP-055 — Municipality/Township field validation**: Added explicit blocklist to §5.14
  and §5.15 prohibiting governance/agency names, type labels, and township names from the
  municipality field. Added REJECT condition, cross-field contamination check, and GIS-only
  population rule. Mirrors these rules in §7 Validation Logic and §10 Missing Data Rules.

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
  to §5.19 Notes. Only narrow, meaningless internal pipeline markers are stripped
  (session refs, bare IMP refs, OBJECTID annotations, discovery run labels, staging
  labels, browser retry annotations). All substantive content is preserved — including
  source attribution, GPS approximation notes with location context, external system
  identifiers (MORPC ParkID etc.), operational notes, and identity notes. The `notes`
  field is a content field; IMP-053 targets only machine-generated scaffolding artifacts.

- **IMP-061 — Notes field preservation principle**: Clarified that the `notes` field
  is the primary home for all useful contextual information that does not fit other
  structured fields. This includes: source citations, GPS approximation warnings with
  location detail, address conflicts or verification needs, identity ambiguities, external
  system cross-references (MORPC ParkID, ODNR ID, etc.), acquisition history, operational
  restrictions, and cross-entity relationships. Notes must not be blanked wholesale; only
  verified-meaningless pipeline scaffolding (see IMP-053 strip list) is removed. When in
  doubt, retain the note.

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
4. Normalize Category — vocabulary enforcement (§5.2)
4a. Apply cultural institution name-pattern check (§5.2)
5. Normalize Subtype — vocabulary enforcement (§5.3)
5a. Apply deterministic subtype inference if blank (§5.3a)
6. Normalize Designation, Status
7. Normalize organizational fields:
   ownership → governance → partner_agencies → coordination
8. Normalize Counties
9. Validate GPS (gps_lat / gps_lon)
10. Validate Plus Code
11. Derive Township, Municipality from GPS via GIS lookup (§5.14, §5.15)
12. **GPS Gate** — hold if GPS null and no gps_unresolvable flag (§5.16a)
13. Normalize Location
14. Normalize Acres
15. Normalize Features
16. Normalize Description
17. Normalize Notes
18. Normalize URLs
19. Validate Parent Site relationship
20. Run identity anchor deduplication check
21. Validate against Site Schema v5.x
22. Emit Normalized Site + provenance

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

## 5.2 Category (IMP-063)

**Vocabulary enforcement**: Every `category` value must match one of the 18 allowed values in Site
Vocabulary Module v5.5 §2.1. Apply in this order:

1. **Case normalization**: convert to title case, trim whitespace.
2. **Exact match check**: if the value matches an allowed value exactly → accept.
3. **Mapping table**: if no exact match, apply Site Vocabulary Module v5.5 §7.1 mapping table.
   - Unambiguous mappings (e.g., "nature preserve" → "Nature Preserve") → apply and log.
   - Context-dependent mappings (e.g., "recreation area" → "Park" or "Recreation Facility") →
     flag for **REVIEW** (hold in review queue); do not auto-resolve.
4. **No match, no mapping**: → **FATAL REJECT** (entity cannot proceed to output).
   Log: `"Category '[value]' has no vocabulary mapping. Entity held for manual category assignment."`
5. **Blank category**: allowed only when source documents provide no classification. Log as WARNING.

**Cultural institution name-pattern check (IMP-068)**: After category is set, compare the
normalized site name against Site Vocabulary Module v5.5 §7.2 pattern table. If the recorded
category is "Recreation Facility" but the name matches a cultural institution pattern:
- Flag as **CATEGORY MISMATCH** review item.
- Do NOT auto-correct. Surface for human review with: `"Name '[name]' matches cultural institution
  pattern '[pattern]' but category is 'Recreation Facility'. Expected category: '[expected]'."`

## 5.3 Subtype (IMP-064)

**Vocabulary enforcement**: Every non-blank `subtype` value must appear in the category-specific
list in Site Vocabulary Module v5.5 §3.2. Apply in this order:

1. **Category-specific list check**: if the subtype appears in the list for the entity's category → accept.
2. **Mapping table**: if not in the category list, apply Site Vocabulary Module v5.5 §7.3 mapping table.
   - Ecological descriptors misplaced in Nature Preserve subtype (Bog, Fen, Forest, Wetland, etc.):
     → null the `subtype` field; append ecological character to `description` if not already present.
   - Features vocabulary terms misplaced in Recreation Facility subtype (Gazebo, Pavilion, Splash Pad, etc.):
     → null `subtype`; ensure the Features vocabulary equivalent appears in `features` if physical
     infrastructure is documented.
   - Other mapped values (e.g., "Community Park" → "Neighborhood Park") → apply and log.
   - Unmappable values → **null** the `subtype` field (do not reject the entity; log a WARNING).
3. **Wrong-category subtype**: if the subtype is a valid value but belongs to a different category →
   flag for **REVIEW**. Example: "Botanical Garden" in subtype of a "Recreation Facility" site.

## 5.3a Deterministic Subtype Inference (IMP-065)

Applied **after** §5.3 vocabulary enforcement, **only when `subtype` is still blank**.
Inference is deterministic — never applied if subtype was set or explicitly nulled in §5.3.
Record inference in normalization provenance as `subtype_source = "name_inference"` or
`"description_inference"`.

Apply inference rules from Site Vocabulary Module v5.5 §7.4:
- **Nature Preserve** — designation check → "State Nature Preserve" designation or name keyword → infer; else → "Private Nature Preserve"
- **Water Site** — name keyword match (River/Creek/Stream/Run → "River"; Reservoir → "Reservoir"; Lake → "Lake"; Pond → "Pond"; Harbor → "Harbor"; Marina → "Marina")
- **Recreation Facility** — name keyword match (Golf Course, Pool/Aquatic Center, Tennis, Pickleball, Skate Park, Disc Golf, Ice Rink, BMX, Pump Track, Sports Complex, Athletic Field, Recreation Center)
- **Campground** — description keyword match (cabin/lodge, RV/hookup/electric, primitive, group)

If no inference rule matches → leave `subtype` blank. Do not infer for any other category.

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

**FORMULA DESCRIPTION DETECTION (IMP-059)**: The following patterns indicate a
formula-generated description sourced from a parks database export rather than
genuine descriptive content. REJECT and blank on any match:

- `"[digits]-acre [type] in the [name] community."` — truncated CRP database format
  where the leading "[Name] is a [integer.]" prefix was stripped during extraction
- `"[Name] is a [X]-acre [type] in the [name] community."` — CRP full formula format
- `"[type] in the [name] community."` — CRP formula with acreage also missing
- `"[Name] has [X] acres of parkland."` — acreage restatement only
- `"The site is part of the [governance entity] natural areas network."` — governance
  self-reference with no site-specific content
- `"of [type] in the [name] community."` — CRP fragment with leading text stripped

For any formula description that also contains additional non-formula sentences
(e.g., trail access, named natural features, historical notes), strip only the
formula sentence and retain the remainder if ≥ 20 characters.

**ACQUISITION/ESTABLISHMENT YEAR HANDLING**: If `description_raw` begins with
`"Acquired in [YYYY]"` or `"Established in [YYYY]"`, extract that date note and
append to the `notes` field as `"Acquired in [YYYY]."` or `"Established in [YYYY]."`.
Strip the acquisition clause from description; evaluate remainder per IMP-052 rules.

**ACREAGE IN DESCRIPTION WARNING**: If a description contains an explicit acreage
figure that differs from the `acres` field by more than 10%, log a WARNING:
`"Description acreage ([X]) does not match acres field ([Y]) — likely different source
vintage. Description acreage not authoritative; acres field takes precedence."` Do not
reject the description for this reason alone, but do not use the description acreage
to update the acres field.

Fields that must never appear in `description`: governance, ownership, acreage (unless
contextually embedded in identity content), hours, permits, amenity lists,
administrative community/district names with no geographic bearing on the site itself.

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
- **Source documentation (IMP-060)**: When the `acres` field is populated, record the
  source in the normalization provenance record. Do not use acreage figures extracted
  from `description_raw` to populate this field — description text is typically from
  a different source vintage than the authoritative GIS/auditor acreage and will often
  disagree. If the only available acreage is from description text, leave `acres` blank
  and log: `"Acreage available only from description text — source vintage unknown,
  not written to acres field."`

------------------------------------------------------------
# 5.13 Counties
- Required.
- Alphabetized.
- Semicolon-delimited.
- Must omit the word "County".
- Multi-county Sites remain single entities.

------------------------------------------------------------
# 5.14 Municipality (GIS-derived, IMP-066)

**GIS derivation requirement**: Municipality must be derived from GPS coordinates using
`na_township_lookup.OhioTownshipLookup.get_both(lat, lon)`. This method returns a
`(township_name, municipality_name)` tuple:

- If `township_name` is `None` and `municipality_name` is not `None` → the GPS point falls
  within an **incorporated city or village**. Populate `municipality = municipality_name`.
  Leave `township` blank.
- If `township_name` is not `None` → the GPS point falls within an **unincorporated civil
  township**. Populate `township = "[township_name] Township"`. Leave `municipality` blank.
- If GPS (`gps_lat` / `gps_lon`) is null → leave both `municipality` and `township` blank.
  Do not attempt GIS lookup without valid coordinates.
- If GIS lookup fails (shapefile load error, coordinate out of Ohio bounds) → leave blank and
  log a WARNING with the entity ID and coordinates.

Never populated from discovery fields, source text, address parsing, or any other pipeline stage.
A valid municipality is an incorporated city, village, or borough. It is NOT a township,
county, agency, district, or governance entity.
- Leave blank if the GPS point falls in an unincorporated area (no city or village).

**REJECT with FATAL error if municipality contains any of the following:**
- Any value from the Governance vocabulary (e.g., "Metro Parks", "ODNR", "MORPC",
  "Park District", "Conservation District", "Wildlife Area", "Metro Gardens")
- Any value ending in "Township" or "Twp" (those belong in the Township field only)
- Any bare type label: "Township", "County", "District", "Division", "Authority",
  "Commission", "Reservation", "Preserve", "Area", "Wildlife", "Nature"
- Any abbreviation of a township: "Twp", "Tp"
- Any value matching the Ownership or Governance fields of the same entity

**Cross-field contamination check:** if municipality == township for the same entity,
REJECT both — this pattern indicates governance or type-label contamination.

------------------------------------------------------------
# 5.15 Township (GIS-derived)
- Must be GIS-derived from GPS coordinates via spatial lookup. Never populated from
  discovery fields, source text, or any other pipeline stage.
- A valid township is a civil township name in the form "[Name] Township".
- Leave blank if the GPS point falls outside any civil township, or if GIS lookup fails.

**REJECT with FATAL error if township contains any of the following:**
- Any value from the Governance vocabulary (e.g., "Metro Parks", "ODNR")
- A bare type label without a name: "Township", "Twp", "County"
- Any value matching the Municipality field of the same entity (cross-contamination)

**Normalization:** if township raw value is "[Name] Twp", expand to "[Name] Township".

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
# 5.17a GPS Gate — Pre-Output Hold (IMP-069)

**This gate runs after GPS validation and Plus Code computation, before TSV Output (Stage 4).**

No Site entity may proceed to TSV Output or Database Upsert unless one of the following is true:

**A. GPS is confirmed**: both `gps_lat` and `gps_lon` are non-null, valid numerics.

**B. GPS is explicitly flagged unresolvable**: the entity has `gps_unresolvable = true` set in
its normalization record. This flag must be accompanied by a `notes` entry explaining why GPS
cannot be obtained (e.g., "GPS unresolvable — site is a distributed linear corridor with no
centroid; boundaries described by metes and bounds only."). See GPS Acquisition Module v5.3 §7
for the full `gps_unresolvable` flag definition and qualifying criteria.

**If neither condition is met** (GPS null, no unresolvable flag):
- Route entity to `held_entities` with `hold_reason = "gps_missing"`.
- Log: `"Entity [site_id] held: GPS null and gps_unresolvable not set. Entity must re-enter
  at GPS Acquisition (Stage 3b) before proceeding to output."`
- Entity is not rejected — it will be released when GPS is acquired in a subsequent run.

**Late-addition sites** (sites added outside the normal pipeline discovery-to-normalization flow)
must re-enter at Stage 2 (Normalization) and must pass through Stage 3 (GPS Acquisition) before
they are eligible for Stage 4 output. They must NOT be upserted directly to the database without
going through this gate.

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

**Core principle (IMP-061)**: The `notes` field is a content field. It is the primary
home for all substantive contextual information that does not fit structured fields.
When in doubt, retain the note. A note with too much information is better than a
note that has had useful content stripped.

- Free text; semicolon-delimited when listing multiple distinct notes.
- Must not contradict controlled fields.
- Use for: source citations, GPS approximation warnings with location context,
  address conflicts and verification needs, identity ambiguities, external system
  cross-references, acquisition and establishment history, operational restrictions,
  cross-entity relationships, and any other useful contextual information.

**PIPELINE METADATA CLEANSING (IMP-053)**: Strip only narrow, meaningless machine-
generated scaffolding artifacts — not substantive content. A `notes` value that
contains pipeline markers alongside real information must have the markers stripped
while the real information is preserved intact.

Strip the following patterns (case-insensitive):
- Session references: `Session N:`, `Session N.`, `Session N` (trailing), `Manually assigned Session N`
- Bare IMP references: `(IMP-NNN)`, `(IMP-NNN: description)`, `; IMP-NNN` — strip only
  when the IMP reference is the entire note or an isolated parenthetical; do not strip
  when IMP context is woven into explanatory text
- OBJECTID annotations: `(OBJECTID NNN)`, `OBJECTID NNN,`
- Bare GPS placeholders: `GPS pending verification.` — strip ONLY this exact placeholder;
  do not strip GPS approximation notes that contain substantive location context
  (e.g., `GPS approximate — address unconfirmed; Sale Road vicinity, Clinton Township`)
- Discovery run labels: `Cataloged during [County] County run.`, `Cataloged during [County] County session.`
- Pipeline staging notes: `staged in [file] YAML`, `staged not pipelined`
- Browser retry annotations: `([date] browser retry)`, `(browser JS extraction, [date])`

**Preserve the following** — these are substantive content, never pipeline scaffolding:
- `Source: [source].` lines — attribution and provenance for the note's content
- GPS approximation notes with location detail: `GPS approximate — [location context]`
- External system identifiers: `MORPC ParkID: NNN`, `ODNR ID: NNN`, `ParkID: NNN`
- Operational notes: hours, closures, permit requirements, contact information, shelter rental availability
- Identity notes written in plain prose (child site relationships, alternate names, address conflicts)
- Cross-entity references: `Child site of [Site Name] ([site_id]).`
- Acquisition and establishment history: `Acquired in YYYY.`, `Established in YYYY.`
- Funding and grant notes: `Acquired in part through [Fund Name].`
- Verification flags: `MUST VERIFY [item].`, `field verification needed`, `identity needs field verification`

After stripping, clean up residual punctuation artifacts (double spaces, leading/trailing
semicolons or periods, orphaned conjunctions). Never produce an empty string — if stripping
would leave nothing, write NULL.

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
- **Category vocabulary enforcement** (§5.2, IMP-063): FATAL REJECT on unmappable values; REVIEW flag on context-dependent mappings
- **Cultural institution name-pattern check** (§5.2, IMP-068): CATEGORY MISMATCH flag if Recreation Facility + cultural institution name pattern
- **Subtype vocabulary enforcement** (§5.3, IMP-064): null on unmappable; REVIEW flag on wrong-category subtypes
- **Subtype inference** (§5.3a, IMP-065): applied after §5.3, only when subtype blank
- Organizational field separation:
  ownership vs governance vs partner_agencies vs coordination
- GPS pairing and numeric format
- **GPS Gate** (§5.17a, IMP-069): HOLD in held_entities with hold_reason="gps_missing" if GPS null and gps_unresolvable not set
- Plus Code derivation
- **GIS municipality/township derivation** (§5.14, IMP-066): `get_both()` called after GPS validation
- Acres numeric
- Semicolon formatting
- No invented data
- No placeholders
- No delimiter characters inside fields
- Parent Site validity
- Identity anchor completeness
- Municipality blocklist check (§5.14): REJECT if governance name, type label, or
  township value present in municipality field
- Township blocklist check (§5.15): REJECT if governance name or bare type label present
- Cross-field contamination check: REJECT if municipality == township for same entity

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
- Never set municipality or township to a governance entity name, agency abbreviation,
  type label, or any value not derived from a GIS spatial lookup.
- If GPS is blank, municipality and township must also be blank.
- If GIS lookup fails, leave municipality and township blank — do not substitute
  administrative, ownership, or governance values as proxies.

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