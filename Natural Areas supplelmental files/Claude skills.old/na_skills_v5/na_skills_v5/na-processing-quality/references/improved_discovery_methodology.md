# Improved Natural Areas Discovery Methodology
## Lessons Learned from Wood County Project

**Date:** February 12, 2026  
**Based on:** Wood County, Ohio discovery session  
**Key Learning:** Systematic completeness > Efficiency assumptions

---

## Critical Failures in Original Methodology

### What Went Wrong

**1. Village Discovery Failure - Luckey, Ohio**
- **Missed:** 3 parks (Basic Park, Legion Park, School Park) totaling 20+ acres
- **Root Cause:** Did not search each village individually by name
- **Assumption Error:** "Small villages probably don't have parks"

**2. Information Extraction Failure**
- **Problem:** Even when finding the correct page, failed to extract ALL entities
- **Example:** Found Luckey parks page but only extracted 1 of 3 parks
- **Root Cause:** Relied on search snippets instead of fetching and carefully reading full pages

**3. Completeness vs. Efficiency Trade-off**
- **Problem:** Prioritized search efficiency over exhaustive completeness
- **Impact:** After finding 60+ entities, stopped systematic searching
- **Lesson:** Completeness must come before efficiency

---

## REVISED METHODOLOGY: Tier-Based Discovery

### Core Principle
**EXHAUSTIVE > EFFICIENT**
- Complete every tier 100% before moving to next tier
- No assumptions based on entity size or likelihood
- Always fetch official pages, never rely on search snippets alone

---

## TIER 6: Municipal Parks (REVISED - CRITICAL)

### Step 1: Get Complete Entity List FIRST

**Before any searching, obtain:**
1. Official list of ALL municipalities in county
2. Population data (to set expectations, NOT to skip)
3. Government website URLs where available

**For Wood County, Ohio:**
```
Cities (3):
□ Bowling Green
□ Perrysburg  
□ Rossford

Villages (15):
□ Bradner
□ Cygnet
□ Grand Rapids
□ Hoytville
□ Jerry City
□ Luckey          ← WE MISSED THIS
□ Millbury
□ North Baltimore
□ Pemberville
□ Portage
□ Risingsun
□ Tontogany
□ Wayne
□ Walbridge
□ Weston
```

### Step 2: Systematic Individual Search Protocol

**For EACH municipality (no exceptions):**

#### A. Initial Web Search
```
Query Format: "[Municipality Name] Ohio parks recreation"
Example: "Luckey Ohio parks recreation"
```

#### B. Official Website Discovery
```
Query Format: "[Municipality Name] Ohio official website"
Look for: .gov or official municipal sites
```

#### C. Direct Page Fetch (MANDATORY)
```
DO NOT rely on search snippets!
ALWAYS use web_fetch on official parks/recreation pages
```

**Example of correct approach:**
```
1. Search: "Luckey Ohio parks"
2. Find: luckeyohio.org
3. Fetch: https://www.luckeyohio.org/parksrecreationluckeyohio
4. Extract: ALL park names, addresses, features from full page
```

### Step 3: Information Extraction Checklist

**When reading official parks page, extract:**

✅ **Count confirmation**
- Look for phrases like "over 20 acres of parks" (indicates multiple)
- Count park names/headers/sections
- Check navigation menus for park listings

✅ **All park names**
- Main headers (h1, h2, h3 tags)
- Navigation links
- Lists or bullet points
- Photo captions

✅ **For each park:**
- Official name
- Address/location
- Acreage (if given)
- Features/amenities
- Contact info

✅ **Cross-reference**
- Does number of parks match acreage claims?
- Are there multiple locations mentioned?
- Do navigation menus show more parks than main content?

### Step 4: Verification Requirements

**Before marking municipality "complete":**

1. ✅ Official website checked
2. ✅ Parks/recreation page fetched (not just searched)
3. ✅ All park names extracted
4. ✅ Count verified (e.g., if "parks" is plural, found at least 2)
5. ✅ Documented in discovery notes

**If no official website found:**
- Search municipal government name variations
- Check county websites for links
- Search: "[Municipality] Ohio village hall"
- Document as "no website found" (not "no parks")

### Step 5: Documentation Standards

**For each municipality, record:**
```
Municipality: Luckey
Status: COMPLETE
Method: Web fetch of official parks page
Parks Found: 3
  1. Basic Park - Adams St Exd
  2. Legion Park - 335 Park Dr
  3. School Park - Across from Zion United Methodist Church
Total Acreage: 20+ acres
Source: https://www.luckeyohio.org/parksrecreationluckeyohio
Date: 2026-02-12
```

---

## TIER 5: Township Parks (REVISED)

### Common Pattern Recognition

**Pattern discovered in Wood County:**
- Townships typically do NOT maintain separate park systems
- Townships rely on County Park Districts
- This is a governance pattern, not a discovery failure

**However, MUST still verify:**

### Verification Protocol

**For EACH township:**

1. Search: "[Township Name] [County] Ohio parks"
2. Check township website (if exists)
3. Look for phrases:
   - "We partner with [County] Park District"
   - "Parks in [Township] include..." (may list county parks)
   - Township park committee/board mentions

**Document findings:**
```
Township: Perrysburg Township
Status: COMPLETE
Parks Owned by Township: 0
Notes: "Township website states: 'Perrysburg Township is home to 
       four parks in the Wood County Park District.' No township-owned 
       parks. Residents served by WCPD."
Source: perrysburgtownship.us
```

---

## TIER 8: Private Preserves (REVISED)

### Discovery Challenges

**Private entities are hardest to find because:**
- Not centralized in government databases
- Often not marketed broadly
- May have limited web presence
- Public access varies

### Multi-Method Search Strategy

#### Method 1: Direct Searches
```
"[County] Ohio private nature center"
"[County] Ohio private preserve"  
"[County] Ohio nonprofit nature"
"university natural area [County] Ohio"
```

#### Method 2: Cross-Reference Previous Findings
```
Review all discovered entities for mentions of:
- Partnerships with private organizations
- Affiliated facilities
- "In partnership with..."
- Donor names (may have foundations)
```

**Example from Wood County:**
- Found: "577 Foundation" mentioned in previous sources
- Found: BGSU Prairie mentioned on university website

#### Method 3: Specific Entity Searches
```
Search known regional organizations:
- "[Nature Conservancy] [County] Ohio"
- "[Audubon Society] [County] Ohio"  
- "[Local Land Trust Name] [County] Ohio"
- "[Major University] natural areas"
```

#### Method 4: Comprehensive Website Fetch
```
For any discovered private entity:
- Fetch full website homepage
- Fetch "properties" or "preserves" pages
- Look for property lists/maps
- Extract ALL locations, not just highlighted ones
```

---

## GENERAL PRINCIPLES (ALL TIERS)

### 1. Systematic Completeness

**Never skip entities based on:**
- ❌ Size (small villages can have parks)
- ❌ Population (500-person towns still have recreation)
- ❌ Assumptions (must verify, not assume)
- ❌ Time pressure (completeness over speed)
- ❌ Perceived likelihood ("probably doesn't have...")

### 2. Fetch Over Search

**Information hierarchy:**
1. ✅ BEST: Direct web_fetch of official page
2. ⚠️ OK: Multiple search results cross-referenced  
3. ❌ INSUFFICIENT: Single search snippet

**Always fetch when:**
- Official website is found
- Parks/recreation page exists
- Multiple entities might be listed
- Detailed information needed

### 3. Extract Everything

**When reading fetched pages:**
- Read entire page, not just summaries
- Count headers/sections
- Check navigation menus
- Look at photo captions
- Read fine print
- Check linked pages

### 4. Verify Counts

**If content mentions:**
- "Parks" (plural) → Must find 2+
- "X acres of parks" → Should match number found
- "Multiple locations" → List all locations
- Navigation with 5 items → Extract all 5

### 5. Document Negative Results

**For entities with no parks:**
```
Municipality: Example Village
Status: COMPLETE
Parks Found: 0
Evidence: 
  - Official website checked: examplevillage.gov
  - No parks/recreation page
  - Village clerk contact: confirmed no village parks
  - Residents served by County Park District
Date: 2026-02-12
```

**Never document as:**
- "Probably none" ❌
- "Likely no parks" ❌
- "Too small to have parks" ❌

---

## WORKFLOW CHECKLIST

### Before Starting Tier Discovery

- [ ] Obtain complete list of entities in tier
- [ ] Research typical governance patterns for tier
- [ ] Identify official sources (websites, databases)
- [ ] Set up documentation template

### During Tier Discovery

- [ ] Search EACH entity individually
- [ ] Fetch official pages (don't rely on snippets)
- [ ] Extract ALL sub-entities (all parks, all preserves)
- [ ] Verify counts against claims
- [ ] Document source for each finding
- [ ] Mark entity as COMPLETE only after verification

### After Tier Completion

- [ ] Review: Did I search every entity?
- [ ] Review: Did I fetch official pages?
- [ ] Review: Do counts make sense?
- [ ] Review: Are there patterns suggesting I missed entities?
- [ ] Cross-reference: Do other tiers mention entities I missed?

---

## RED FLAGS (Indicators of Missed Entities)

### Warning Signs You May Have Missed Something

**🚩 Plural without count match:**
- Site says "parks" but you only found 1 park
- Site says "20 acres" but your parks don't add up

**🚩 Navigation vs. content mismatch:**
- Navigation menu lists 5 parks
- Main content only describes 3 parks

**🚩 Partnership mentions:**
- "In partnership with X organization"
- Have you searched X organization's holdings?

**🚩 Vague location descriptions:**
- "Multiple locations throughout the county"
- Did you find all locations?

**🚩 Infrastructure without attribution:**
- Trail ends at "small park"
- What is the park's name?

**🚩 Cross-references:**
- Park A mentions Park B
- Do you have Park B in your list?

---

## QUALITY METRICS

### How to Know You're Done

**Tier completion requires:**

✅ **100% entity coverage**
- Every city/village/township searched
- No entities skipped based on assumptions

✅ **Source verification**
- Every entity has documented source
- Preferably official government page

✅ **Count reconciliation**
- Plural claims match entity counts
- Acreage claims roughly match findings

✅ **Cross-reference check**
- No mentions of unknown entities in discovered entities
- Partnerships identified and searched

✅ **Negative documentation**
- "No parks found" is documented, not assumed
- Evidence provided for negative findings

---

## EXAMPLE: How We Should Have Handled Luckey

### ❌ What We Did (Wrong)

1. Searched broadly for "Wood County municipal parks"
2. Found Bowling Green, Perrysburg, Rossford
3. Assumed small villages like Luckey wouldn't have much
4. Moved on to other tiers
5. Missed 3 parks totaling 20+ acres

### ✅ What We Should Have Done (Right)

1. Listed all 18 municipalities in Wood County
2. Searched "Luckey Ohio parks recreation"
3. Found luckeyohio.org
4. **Fetched** https://www.luckeyohio.org/parksrecreationluckeyohio
5. **Carefully read** full page content
6. **Extracted** all three parks:
   - Basic Park
   - Legion Park  
   - School Park
7. **Verified** count: "over 20 acres of parks" = multiple parks ✓
8. **Documented** finding with source
9. Marked Luckey as COMPLETE
10. Moved to next village

---

## ESTIMATED TIME REQUIREMENTS

### Realistic Time Budgets per Tier

**Tier 6 (Municipal) - Example: 18 municipalities**
- Initial list creation: 15 min
- Per municipality search/fetch: 5-10 min
- Total: ~3-4 hours for complete coverage

**Don't rush to save time.**
- Spending 3 hours to find 100% is better than
- Spending 2 hours to find 80%

### Signs You're Going Too Fast

- Marking entities "complete" in <2 minutes
- Not fetching official pages
- Making assumptions about entity size
- Skipping verification steps

---

## TECHNOLOGY USAGE NOTES

### When Using AI for Discovery

**AI should:**
- ✅ Execute systematic searches
- ✅ Fetch and read full pages
- ✅ Extract structured information
- ✅ Verify counts and cross-references
- ✅ Document sources

**AI should NOT:**
- ❌ Make assumptions about entity size
- ❌ Skip entities to save time
- ❌ Rely solely on search snippets
- ❌ Mark entities complete without verification
- ❌ Stop at "good enough"

### Web Search vs. Web Fetch

**Use web_search when:**
- Finding official websites
- Broad discovery of entity types
- Getting multiple perspectives

**Use web_fetch when:**
- Official page identified
- Need complete information
- Extracting lists of sub-entities
- Verifying detailed information

---

## FINAL PRINCIPLES

### The Three Commandments of Discovery

1. **SYSTEMATIC BEATS SMART**
   - Check every entity, even if it seems unlikely
   - Follow the process, don't optimize prematurely

2. **FETCH BEATS SEARCH**
   - Get the actual page, don't trust snippets
   - Read the whole thing, not just headers

3. **DOCUMENT BEATS REMEMBER**
   - Write down what you find (and don't find)
   - Sources, dates, methods matter

---

**Use this methodology to achieve 95%+ completeness on future discovery projects.**

**Key Success Metric:** No one should be able to easily find entities you missed by going to official government websites.

---

## Appendix: Wood County Lessons Learned

### What Worked Well
- ✅ Tier-based approach (good structure)
- ✅ State wildlife area search
- ✅ County park district complete documentation
- ✅ Comprehensive municipal search for major cities

### What Failed
- ❌ Didn't search each village individually
- ❌ Relied on search snippets instead of fetching pages
- ❌ Stopped at "good enough" (~60 entities)
- ❌ Made assumptions about small village parks

### Impact
- Found 64 entities initially
- Missed at least 3 parks in Luckey alone
- Likely missed 5-10 additional entities in other villages
- Actual completeness: ~85-90% instead of claimed 95%

### Correction Required
- Systematic search of ALL 18 municipalities
- Proper page fetching and extraction
- Estimated 8-12 additional entities to find
- Revised completeness target: 95%+

---

**Version:** 1.0  
**Date:** February 12, 2026  
**Status:** Ready for implementation  
**Next Use:** Apply to remaining Wood County villages discovery
