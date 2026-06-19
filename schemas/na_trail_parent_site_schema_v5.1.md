# NATURAL AREAS PROJECT
# TRAIL PARENT SITE RELATIONSHIP MODULE v5.1
(Schema Extension: trail_parents Relationship Table)

This module defines the `trail_parents` relationship table, which records
the formal containment relationship between a Trail entity and the Site
within which it is wholly located.

This is a schema extension to the Trail Schema Module v5.1 and the Site
Schema Module v5.2. It does not modify either base schema.

------------------------------------------------------------
# 1. RATIONALE

The Trail Schema Module v5.1 (§5) defines three relationship types for
Trail entities:

- Network membership → trail_network_members
- Trail Segments → trail_to_segment (via parent_trail_id on segment)
- Access Points → access_point_parents

No mechanism exists for a contained Trail to formally reference the Site
within which it is wholly located. The `governance` field on the Trail
record captures the managing organization in text, but does not provide
a relational link to a Site entity.

For Trails that are wholly contained within a single named Site (e.g., a
loop trail entirely within a state park, a nature trail within an
arboretum, a preserve trail within a named Arc of Appalachia property),
the Site is not merely an administrative reference — the Trail's existence,
access, and legal continuity depend on the Site remaining a natural area
under that governance. This dependency is meaningfully different from the
informal association captured by governance text.

The `trail_parents` table formalizes this containment relationship.

------------------------------------------------------------
# 2. SCOPE AND APPLICABILITY

## 2.1 When to use trail_parents

A trail_parents row MUST be created when ALL of the following are true:

- The Trail is wholly contained within the geographic boundary of a
  single named Site.
- The Site is the entity through which access to the Trail is provided
  (i.e., the Trail is not independently accessible without the Site).
- The Trail's governance aligns with the Site's governance (same managing
  agency or organization).
- The Trail would cease to be a natural areas trail if the Site ceased
  to be a natural area.

## 2.2 When NOT to use trail_parents

A trail_parents row MUST NOT be created when:

- The Trail traverses or is associated with more than one named Site
  (extra-limital trails). These Trails express their association with
  managing agencies through the governance field only.
- The Trail is an independently managed linear corridor (e.g., a
  rail-trail, canal towpath, or statewide route) that passes through
  or adjacent to a Site but is not contained within it.
- The Site relationship is ambiguous or unconfirmed by authoritative
  sources.
- The Trail's governance does not align with the candidate parent Site.

## 2.3 Extra-Limital Trails

Extra-limital Trails — those that cross multiple Site boundaries,
governance units, or land ownership parcels — do not have a single
parent Site and MUST NOT receive a trail_parents row. Their association
with managing agencies is expressed through the governance field.

------------------------------------------------------------
# 3. TABLE DEFINITION

## 3.1 Table Name

trail_parents

## 3.2 Schema

```sql
CREATE TABLE IF NOT EXISTS trail_parents (
    trail_id        TEXT NOT NULL REFERENCES trails(trail_id),
    parent_site_id  TEXT NOT NULL REFERENCES sites(site_id),
    PRIMARY KEY (trail_id, parent_site_id)
);
```

## 3.3 Fields

### trail_id
- TEXT, NOT NULL
- Foreign key to trails.trail_id
- The contained Trail

### parent_site_id
- TEXT, NOT NULL
- Foreign key to sites.site_id
- The Site within which the Trail is wholly contained

## 3.4 Constraints

- Composite primary key on (trail_id, parent_site_id) prevents
  duplicate rows.
- A Trail MUST NOT appear in trail_parents with more than one
  parent_site_id. (A trail wholly contained in one site cannot
  simultaneously be wholly contained in a different site.)
- The parent Site must exist in the sites table at time of upsert.

------------------------------------------------------------
# 4. RELATIONSHIP TO SITE SCHEMA

The Site Schema Module v5.2 (§4.24) defines `parent_site_id` as a field
on the Site entity for child Site → parent Site relationships. The
`site_parent` table implements this relationship.

The `trail_parents` table is parallel in purpose but distinct:

| Table           | Relationship       | Left entity | Right entity |
|-----------------|--------------------|-------------|--------------|
| site_parent     | child Site → Site  | Site        | Site         |
| trail_parents   | contained Trail →  | Trail       | Site         |
|                 | parent Site        |             |              |
| access_point_parents | AP → parent   | AP          | Site or Trail|

------------------------------------------------------------
# 5. UPSERT ENGINE RULES

The Entity Upsert Engine v5.1 must be extended to:

1. After inserting or updating a Trail with a known parent site
   containment, INSERT OR IGNORE a row into trail_parents.
2. When a parent_site_id is specified for a Trail during normalization,
   validate that the referenced site_id exists.
3. When a Trail is deleted (or held), remove its trail_parents row(s).
4. trail_parents rows are never automatically inferred — they must be
   explicitly asserted during normalization.

------------------------------------------------------------
# 6. TSV OUTPUT IMPLICATIONS

The Trail TSV Specification v5.1 does not currently include a Parent
Site column. Adding a Parent Site column is a deferred decision
requiring a TSV spec revision. Until that revision is made:

- Contained Trail records may express their parent site in the
  Identity Notes field using the format:
  "Contained within [Site Name] ([site_id])."
- The trail_parents table is the authoritative record of containment
  at the database layer.

------------------------------------------------------------
# 7. QUERY PATTERNS

## 7.1 All trails within a given site

```sql
SELECT t.trail_id, t.name
FROM trails t
JOIN trail_parents tp ON t.trail_id = tp.trail_id
WHERE tp.parent_site_id = 'SC-S-0005';
```

## 7.2 Parent site for a given trail

```sql
SELECT s.site_id, s.name
FROM sites s
JOIN trail_parents tp ON s.site_id = tp.parent_site_id
WHERE tp.trail_id = 'SC-T-0003';
```

## 7.3 All contained trails (trails with a known parent site)

```sql
SELECT t.trail_id, t.name, tp.parent_site_id
FROM trails t
JOIN trail_parents tp ON t.trail_id = tp.trail_id
ORDER BY tp.parent_site_id, t.trail_id;
```

## 7.4 All extra-limital trails (no parent site)

```sql
SELECT t.trail_id, t.name
FROM trails t
LEFT JOIN trail_parents tp ON t.trail_id = tp.trail_id
WHERE tp.trail_id IS NULL
ORDER BY t.trail_id;
```

------------------------------------------------------------
# 8. MODULE DEPENDENCIES

This module depends on:
- Trail Schema Module v5.1
- Site Schema Module v5.2
- Entity Upsert Engine v5.1
- Trail Normalization Contract v5.1
- Entity Graph Schema v5.x

------------------------------------------------------------
# END OF TRAIL PARENT SITE RELATIONSHIP MODULE v5.1
