# WOOD COUNTY NORMALIZATION WORKFLOW PLAN

**Project:** Natural Areas Discovery v4.0  
**County:** Wood County, Ohio  
**Phase:** Normalization  
**Date:** February 16, 2026  
**Status:** Planning

---

## CURRENT STATE ASSESSMENT

### What We Have
- ✅ Discovery documentation (8 tiers complete)
- ✅ Master discovery summary (92-94 sites)
- ✅ Source documentation and verification
- ✅ Tier-by-tier summaries

### What We Need
- ⏭️ Structured entity records (Sites, Trails, Access Points)
- ⏭️ Entity-level data (names, addresses, coordinates, ownership)
- ⏭️ Normalized fields ready for TSV output

---

## NORMALIZATION CHALLENGE

**Problem:** Our discovery phase produced narrative documentation, not structured data records.

**Example:** 
- **Have:** "Bowling Green has 15+ parks including Wintergarden/St. John's Nature Preserve (120+ acres)"
- **Need:** Structured record with Site_ID, Site_Name, County, Ownership, Acreage, etc.

**Solution:** We need a **Data Extraction** phase before normalization

---

## REVISED WORKFLOW

### Phase 1: DATA EXTRACTION (New - Required)
Extract structured entity data from discovery documentation

**Process:**
1. Review each tier's discovery documentation
2. Extract individual site records
3. Create structured entity records with available fields
4. Document what data is available vs. missing

**Output:** Structured entity list with known fields populated

---

### Phase 2: DATA ENRICHMENT (Optional)
Fill in missing required fields through additional research

**Common Missing Fields:**
- Exact acreage (many sites show "15+ parks" not individual acres)
- GPS coordinates (not systematically collected during discovery)
- Full addresses (some sites only have city/township)
- Plus codes (not collected during discovery)
- Detailed feature lists

**Decision Point:** How complete does normalization data need to be?

**Options:**
A. **Minimal Viable**: Normalize only what we have, mark rest as NULL/TBD
B. **Enriched**: Research missing fields before normalization
C. **Iterative**: Normalize what we have, enrich in future passes

---

### Phase 3: NORMALIZATION (Standard Process)
Apply normalization engine to structured data

**Process:**
1. Load Site Schema & Vocabulary
2. Apply normalization rules
3. Validate required fields
4. Map vocabularies
5. Format fields
6. Compute derived labels
7. Validate integrity

---

### Phase 4: TSV OUTPUT
Generate standardized output files

---

## RECOMMENDED APPROACH

### **OPTION: Iterative Minimal Viable Product (MVP)**

**Rationale:**
- Discovery documentation is comprehensive but not entity-detailed
- Full field enrichment would require weeks of additional research
- Better to produce working TSV with known data than delay for perfection
- Can enrich in future iterations

**MVP Process:**

1. **Extract Core Site Data** (~2-3 hours)
   - Site names from discovery docs
   - Ownership (tier = ownership indicator)
   - County (all Wood County)
   - Discovery tier
   - Source URLs where available
   - Mark detailed fields as TBD

2. **Normalize MVP Data** (~1 hour)
   - Apply site name normalization
   - Map tiers to ownership categories
   - Validate required fields
   - Mark optional fields as NULL

3. **Generate MVP TSV** (~30 min)
   - Sites.tsv with core fields
   - Document what's complete vs. TBD
   - Create enhancement roadmap

4. **Quality Audit** (~30 min)
   - Validate TSV integrity
   - Check referential integrity
   - Document gaps

**Total Time:** ~4-5 hours for MVP normalization

---

## SAMPLE ENTITY EXTRACTION

### From Discovery Docs:

**Tier 1: State**
```
Site_Name: Mary Jane Thurston State Park
County: Wood (shared with Fulton)
Ownership: State of Ohio (ODNR)
Category: State Park
Acreage: 104 (total, shared)
Source: https://parks.ohiodnr.gov/maryjane thurston
Discovery_Tier: 1
```

**Tier 3: County**
```
Site_Name: Carter Historic Farm
County: Wood
Ownership: Wood County Park District
Category: County Park
Acreage: 60+ (estimated from sources)
Source: https://wcparks.org/carter-historic-farm
Discovery_Tier: 3
```

**Tier 6: Municipal**
```
Site_Name: Wintergarden / St. John's Nature Preserve
County: Wood
Ownership: City of Bowling Green
Category: Municipal Park / Nature Preserve
Acreage: 120+ 
Source: https://www.bgohio.org/
Discovery_Tier: 6
```

---

## REQUIRED vs. AVAILABLE FIELDS

### Site Schema Required Fields:
- ✅ Site_ID (can generate)
- ✅ Site_Name (have from discovery)
- ✅ County (all Wood County)
- ✅ State (all Ohio)
- ✅ Ownership (can infer from tier)
- ⚠️ Site_Type (need to classify each)
- ❌ GPS_Lat / GPS_Lon (not systematically collected)
- ❌ Plus_Code (not collected)
- ⚠️ Acreage (have estimates, not precise)
- ⚠️ Address (partial - city/township only for many)

### Conclusion:
**We can produce a valid MVP TSV** with required fields populated from available data, marking detailed fields as TBD for future enrichment.

---

## NEXT STEPS - USER DECISION REQUIRED

### Question 1: Scope
**Which approach for normalization?**

A. **MVP Fast Track** (4-5 hours)
   - Extract and normalize what we have
   - Mark missing fields as NULL/TBD
   - Produce working TSV quickly
   - Document enhancement roadmap

B. **Full Enrichment** (2-3 weeks)
   - Research each site individually
   - Collect GPS, acreage, addresses
   - Full feature cataloging
   - Complete all optional fields

C. **Hybrid** (1 week)
   - Extract what we have
   - Enrich tier 1-3 (high priority sites)
   - Leave tier 6-8 as MVP
   - Progressive enhancement

### Question 2: Entity Types
**Which entities to normalize first?**

A. **Sites Only** (primary entities)
B. **Sites + Trails** (if trail data available)
C. **Sites + Trails + Access Points** (full system)

---

## RECOMMENDATION

**Start with MVP Fast Track - Sites Only**

**Why:**
1. Proves the normalization workflow works
2. Produces usable output quickly
3. Identifies what data we actually need
4. Can iterate and enrich later
5. Validates TSV output process

**Next Session:**
1. User approves MVP approach
2. Begin extracting site data from discovery docs
3. Create structured entity records
4. Apply normalization engine
5. Generate Sites.tsv
6. Quality audit

---

**File Status:** Normalization planning complete  
**Awaiting:** User decision on approach
