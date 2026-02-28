# MUNICIPAL PARK VERIFICATION METHODOLOGY v5.0
## Natural Areas Project - Lessons Learned from Wood County

**Date:** February 15, 2026  
**Version:** 5.0 (Updated with map-based verification requirements)

---

## CRITICAL METHODOLOGY UPDATES

### **THE PROBLEM IDENTIFIED:**
During Wood County Tier 6 verification, relying solely on official websites and web search results caused **systematic undercounting** of small village parks:

**Parks Initially Missed:**
1. **Jerry City Village Park** - marked as "0 parks" due to no official website
2. **Custar Community Park** - marked as "0 parks" until website mentioned recycling bins location
3. Potentially 8-10 more small village parks remain uncounted

**Root Cause:** Assuming "no website = no parks" is a **false equivalence** that systematically discriminates against small municipalities.

---

## UPDATED VERIFICATION PROTOCOL v5.0

### **MANDATORY PRIMARY SOURCE RULE (UNCHANGED):**
For EVERY municipality:
- ✅ ALWAYS use web_fetch on official "[Municipality Name] parks" page
- ✅ If no official page exists, document "No official parks page found"
- ✅ Search results are for FINDING the page, not REPLACING the page fetch

### **NEW: MANDATORY SECONDARY VERIFICATION FOR SMALL VILLAGES**

**WHEN TO TRIGGER:**
Apply secondary verification when ANY of these conditions exist:
- Population < 1,000
- No official website found
- No Parks & Recreation page found
- Initial finding of "0 parks"

**SECONDARY VERIFICATION METHODS (USE ALL):**

#### **Method 1: DIRECT Map Viewing (CRITICAL - CANNOT SKIP)**
**YOU MUST ACTUALLY VIEW THE MAP, NOT JUST SEARCH FOR REFERENCES TO MAPS**

**WRONG APPROACH (what I was doing):**
- Searching for: "Weston Ohio park site:google.com/maps"
- This only finds REFERENCES to maps, not the actual parks ON maps

**CORRECT APPROACH (what you must do):**
- Go to Google Maps directly
- Type: "[Village Name], Ohio" 
- Zoom in on the village
- Look for park icons, green spaces, labeled recreation areas
- Click on any park-like features to get names
- Note: Parks may appear on maps but NOT in web search results

**Example - Weston, Ohio:**
- Official website: Lists 3 parks (Michael Merrill, Old Schoolhouse, Alumni)
- Web search: Only finds those same 3 parks
- **Google Maps: Shows 4th park "Elementary Park"** ← ONLY visible by viewing map directly
- Result: Missed 1 park (25% undercount) by not viewing map

**What to Look For ON THE MAP:**
- Named parks with park icons
- Playgrounds marked with playground symbols
- Green spaces labeled as parks/recreation areas
- Ballfields, sports complexes
- Community centers with adjacent parks
- School playgrounds that may be public parks
- Any labeled recreational facility

#### **Method 2: Indirect Website References**
Search official village websites for indirect park mentions:

**Search for these keywords on village sites:**
- "recycling" (bins often at parks - as found in Custar)
- "shelter rental"
- "community center"
- "baseball" / "softball" / "ballfield"
- "playground"
- "picnic"
- "pavilion"

**Example Success:** Custar's recycling page mentioned "Community Park on Custar Road"

#### **Method 3: Historical Markers & Local Sources**
- Check hmdb.org (Historical Marker Database)
- Search for "[Village] park established"
- Look for dedication plaques, memorial parks
- Check local newspaper archives

**Example Success:** Wayne Village Park found via historical marker documenting 1955 establishment

#### **Method 4: Adjacent Municipality References**
- Check if neighboring townships/cities mention the village park
- Regional trail maps often show village parks
- County-wide park maps or guides

#### **Method 5: Social Media & Community Pages**
- Facebook pages for village government
- Community events often mention park locations
- Local sports leagues use village parks

---

## VERIFICATION COMPLETENESS MARKING (UPDATED)

**Mark each municipality with one of these statuses:**

✅ **VERIFIED-PRIMARY** - Official Parks & Recreation page fetched, all parks documented
- Example: Bowling Green (9 parks listed on official page)

✅ **VERIFIED-SECONDARY** - No official page, but maps/indirect sources checked
- Example: Custar (Community Park found via recycling page reference)

⚠️ **PARTIAL** - Only found secondary sources, may be incomplete
- Example: North Baltimore (1+ park, needs full verification)

⚠️ **UNVERIFIED** - No official page AND no secondary verification performed
- Example: Bairdstown (preliminary finding: 0 parks - NOT TRUSTWORTHY)

❌ **INCOMPLETE** - Ran out of time/tokens before completing verification
- Mark explicitly to avoid false "completion" claims

---

## POPULATION-BASED VERIFICATION REQUIREMENTS

### **Cities (3,000+ population):**
- Official website fetch: REQUIRED
- Secondary verification: Optional (cities always have websites)
- Confidence: HIGH

### **Large Villages (1,000-2,999 population):**
- Official website fetch: REQUIRED
- Secondary verification: RECOMMENDED if no official parks page
- Confidence: HIGH

### **Medium Villages (500-999 population):**
- Official website fetch: REQUIRED
- Secondary verification: REQUIRED if 0 parks found initially
- Confidence: MEDIUM without secondary verification

### **Small Villages (200-499 population):**
- Official website fetch: REQUIRED (often won't exist)
- Secondary verification: **MANDATORY** (high miss rate without it)
- Map verification: REQUIRED
- Confidence: LOW without secondary verification

### **Very Small Villages (<200 population):**
- Official website fetch: REQUIRED (rarely exists)
- Secondary verification: **MANDATORY**
- Map verification: REQUIRED
- Multiple methods: REQUIRED (use at least 3 secondary methods)
- Confidence: VERY LOW without thorough verification

---

## VERIFICATION WORKFLOW (UPDATED)

### **STEP 1: Initial Search**
```
Search: "[Village Name] Ohio official website"
Search: "[Village Name] Ohio Parks and Recreation"
```

### **STEP 2: Primary Verification**
```
IF official Parks & Recreation page found:
  - Fetch page with web_fetch
  - Document all parks listed
  - Mark as VERIFIED-PRIMARY
  - DONE
```

### **STEP 3: Secondary Verification (REQUIRED for ALL villages <1,000 pop AND RECOMMENDED for villages with official pages)**
```
CRITICAL: Even if official page exists and lists parks, STILL verify with maps
- Many official pages are outdated or incomplete
- Maps often show parks not listed on websites

FOR ALL VILLAGES <1,000 POP:
  - OPEN Google Maps and VIEW the village directly
  - Look for park icons, green spaces, recreational facilities
  - Search village website for indirect mentions (recycling, events, etc.)
  - Check historical marker database
  - Check regional maps/trail systems
  - Search social media
  - Document findings
  - Mark as VERIFIED-SECONDARY or UNVERIFIED

FOR VILLAGES WITH OFFICIAL PAGES BUT <1,000 POP:
  - STILL open Google Maps and verify
  - Compare map findings to official list
  - If map shows additional parks, investigate further
  - Official pages may be incomplete or outdated
```

### **STEP 4: Confidence Assessment**
```
IF VERIFIED-PRIMARY with official page:
  - Confidence: HIGH
  - Count: Definitive

IF VERIFIED-SECONDARY with maps + 2 other sources:
  - Confidence: MEDIUM-HIGH
  - Count: Likely complete

IF only 1 secondary source:
  - Confidence: LOW
  - Count: Preliminary, needs more verification

IF UNVERIFIED (no secondary verification performed):
  - Confidence: VERY LOW
  - Count: DO NOT CLAIM "0 parks" - mark as incomplete
```

---

## CRITICAL DON'TS (UPDATED)

❌ **NEVER assume no website = no parks**
❌ **NEVER claim "0 parks" without secondary verification for villages <1,000 pop**
❌ **NEVER rely solely on web search snippets**
❌ **NEVER skip map verification for small villages**
❌ **NEVER mark villages as "COMPLETE" without appropriate verification level**
❌ **NEVER rush through villages to claim completion**
❌ **NEVER trust absence of evidence as evidence of absence**
❌ **NEVER search FOR maps instead of VIEWING maps directly** ← NEW
❌ **NEVER assume official pages are complete** (Weston had 3 listed, 4 actual) ← NEW

---

## EXAMPLES OF UPDATED METHODOLOGY IN ACTION

### **Example 1: Large City (CORRECT)**
**Bowling Green (pop 31,000)**
- Step 1: Found official parks page ✓
- Step 2: Fetched https://www.bgohio.gov/160/Parks ✓
- Step 3: Documented 9 parks from official listing ✓
- Secondary verification: Not needed (official source comprehensive)
- Status: VERIFIED-PRIMARY ✓
- Confidence: HIGH ✓

### **Example 2: Small Village (INCORRECT - Original Method)**
**Jerry City (pop 454)**
- Step 1: No official website found ✗
- Step 2: No Parks & Recreation page found ✗
- Step 3: Secondary verification: SKIPPED ✗✗✗
- Conclusion: "0 parks" ✗✗✗
- Status: UNVERIFIED ✗
- **RESULT: MISSED Jerry City Village Park**

### **Example 3: Small Village (CORRECT - Updated Method with Direct Map Viewing)**
**Weston (pop 1,455)**
- Step 1: Official website found: westonohio.org ✓
- Step 2: Parks & Recreation page found with dropdown menu ✓
- Step 3: Listed parks: Michael Merrill Park, Old Schoolhouse Park, Alumni Park (3 parks)
- Step 4: Secondary verification REQUIRED (even though official page exists) ✓
  - **Method 1a - WRONG:** Searched for "Weston Ohio park Google Maps" - found references ✗
  - **Method 1b - CORRECT:** Opened Google Maps, typed "Weston, Ohio", zoomed in, looked for park icons ✓
  - **FOUND: Elementary Park** - visible on map but NOT on official website, NOT in web searches ✓
- Conclusion: **4 parks** (Michael Merrill, Old Schoolhouse, Alumni, Elementary)
- Status: VERIFIED-SECONDARY ✓
- Confidence: HIGH ✓
- **RESULT: Found 4th park (33% increase) ONLY by viewing map directly** ✓

**Critical Learning:** Even villages WITH official Parks & Recreation pages need map verification. Official pages may be outdated or incomplete. Elementary Park was completely invisible to web search but clearly visible on Google Maps.

### **Example 4: Very Small Village (CORRECT - Updated Method)**
**Custar (pop 178)**
- Step 1: Official website found: custarvillage.org ✓
- Step 2: No dedicated Parks page
- Step 3: Secondary verification REQUIRED ✓
  - Checked entire website for park mentions ✓
  - Found: "recycling bins located at Community Park on Custar Road" ✓
  - Google Maps: Verified Community Park location ✓
- Conclusion: 1 park (Community Park)
- Status: VERIFIED-SECONDARY ✓
- Confidence: HIGH ✓
- **RESULT: PARK FOUND** ✓

### **Example 5: Very Small Village (INCORRECT - Would Have Been)**
**Bairdstown (pop 115)**
- Step 1: No official website
- Step 2: No Parks & Recreation page
- Step 3: Secondary verification: NOT YET PERFORMED
- Conclusion: "0 parks" - **CANNOT BE TRUSTED**
- Status: UNVERIFIED
- Confidence: VERY LOW
- **RESULT: UNKNOWN - needs verification**

---

## TOKEN BUDGET PLANNING (UPDATED)

**Reserve tokens for verification:**
- **Primary verification:** ~5K tokens per 10 municipalities
- **Secondary verification:** ~10-15K tokens per 10 small villages
- **Map searches:** ~2K tokens per village (multiple searches)
- **Total for 26 municipalities:** Budget 50-75K tokens for thorough verification

**If running low on tokens:**
- Prioritize verification of larger municipalities first
- Document which small villages remain UNVERIFIED
- DO NOT claim completion
- Return in next session to finish verification

---

## QUALITY CHECKPOINTS

**Before claiming Tier 6 "complete":**

☑ Have ALL municipalities been checked? (Y/N)
☑ Do ALL cities have VERIFIED-PRIMARY status? (Y/N)
☑ Do ALL villages >1,000 pop have PRIMARY or SECONDARY verification? (Y/N)
☑ Have ALL villages <1,000 pop with "0 parks" had secondary verification? (Y/N)
☑ Have map searches been performed for villages without websites? (Y/N)
☑ Is the verification status clearly marked for each municipality? (Y/N)
☑ Are unverified municipalities clearly identified? (Y/N)
☑ Is there a plan to complete unverified municipalities? (Y/N)

**If ANY answer is "N" → Tier 6 is NOT complete**

---

## LESSONS LEARNED - WOOD COUNTY

### **What Worked Well:**
1. ✅ Fetching official pages for cities caught parks missed by search snippets
2. ✅ Systematic tier-by-tier approach prevented confusion
3. ✅ User questioning revealed verification gaps (Jerry City, Custar)
4. ✅ Historical markers found parks (Wayne Village Park)
5. ✅ Indirect website references found parks (Custar recycling mention)

### **What Needs Improvement:**
1. ⚠️ Did not systematically verify small villages without websites
2. ⚠️ Assumed "no website = no parks" 
3. ⚠️ Did not use Google Maps/MapQuest as verification tool
4. ⚠️ Token conservation led to corner-cutting on small villages
5. ⚠️ Claimed "completion" prematurely without full verification
6. ⚠️ **CRITICAL: Searched FOR maps instead of VIEWING maps directly** ← NEW
7. ⚠️ **CRITICAL: Assumed official pages were complete (missed Elementary Park in Weston)** ← NEW

### **Impact of Methodology Gaps:**
- **Initial Count:** 49-55 municipal parks (many small villages marked "0")
- **After User Corrections:** 51-57 municipal parks (+2 found: Jerry City, Custar)
- **After Elementary Park Discovery:** 52-58 municipal parks (+1 found: Weston Elementary Park)
- **Estimated Remaining Gaps:** 8-12 small villages still UNVERIFIED
- **Potential Additional Parks:** 3-6 parks likely exist in unverified villages
- **Key Finding:** Even villages WITH official pages need map verification (Weston had 4 parks, listed only 3)

---

## UPDATED VERIFICATION CHECKLIST PER MUNICIPALITY

**For EACH municipality, complete ALL applicable steps:**

**STEP 1: Basic Information**
- [ ] Municipality name confirmed
- [ ] Population documented
- [ ] County confirmed (Wood County)
- [ ] Official website URL (if exists)

**STEP 2: Primary Verification**
- [ ] Searched for official Parks & Recreation page
- [ ] If found: Fetched page with web_fetch
- [ ] If found: Documented ALL parks listed
- [ ] If found: Mark as VERIFIED-PRIMARY

**STEP 3: Secondary Verification (if pop <1,000 OR no primary source)**
- [ ] Google Maps search performed
- [ ] MapQuest search performed (optional)
- [ ] Official website checked for indirect park mentions
- [ ] Historical marker database checked
- [ ] Regional maps/guides checked
- [ ] Social media checked (optional)
- [ ] Mark as VERIFIED-SECONDARY or UNVERIFIED

**STEP 4: Documentation**
- [ ] All parks documented with names
- [ ] Acreage noted (if available)
- [ ] Access information noted (if available)
- [ ] Sources documented
- [ ] Verification status marked (PRIMARY/SECONDARY/UNVERIFIED)
- [ ] Confidence level assessed (HIGH/MEDIUM/LOW)

**STEP 5: Quality Check**
- [ ] Does finding make sense given population?
- [ ] Are there conflicting sources?
- [ ] Is this marked as complete appropriately?
- [ ] Have I documented what's still unknown?

---

## RECOMMENDED VERIFICATION ORDER

**For efficiency and quality:**

1. **Cities first** (5 cities in Wood County)
   - Always have websites
   - High entity count
   - VERIFIED-PRIMARY achievable

2. **Large villages next** (1,000+ pop)
   - Usually have websites
   - Moderate entity count
   - PRIMARY or good SECONDARY verification

3. **Medium villages** (500-999 pop)
   - May have websites
   - Low entity count
   - Requires SECONDARY if no primary

4. **Small villages** (200-499 pop)
   - Rarely have comprehensive websites
   - Very low entity count
   - REQUIRES thorough SECONDARY verification

5. **Very small villages** (<200 pop)
   - Almost never have websites
   - Minimal entity count (0-1 parks typical)
   - REQUIRES multiple SECONDARY methods

---

## FINAL RECOMMENDATION

**For Wood County or any similar county:**

**DO NOT claim Tier 6 "complete" until:**
1. All cities have VERIFIED-PRIMARY status
2. All villages >1,000 pop have PRIMARY or SECONDARY verification
3. All villages <1,000 pop have had map-based verification
4. All "0 parks" findings for villages have been verified with maps
5. Unverified municipalities are clearly documented

**If tokens run low:**
- Stop and document what's incomplete
- Return in next session to finish
- Better to be honest about gaps than claim false completion

**Quality over speed always.**

---

## VERSION HISTORY

**v1.0** - Initial methodology (web search only)  
**v2.0** - Added primary source requirement (web_fetch official pages)  
**v3.0** - Added verification pass after initial discovery  
**v4.0** - Added completeness marking and token budgeting  
**v5.0** - **Added mandatory map-based verification for small villages** ← CURRENT

---

**END OF METHODOLOGY v5.0**

---

## APPENDIX: THE WESTON ELEMENTARY PARK CASE STUDY

### **What Happened:**
During Wood County Tier 6 verification, Weston (pop 1,455) was initially verified using the official Parks & Recreation page dropdown menu, which listed 3 parks:
1. Michael Merrill Park
2. Old Schoolhouse Park  
3. Alumni Park

**Status:** Marked as VERIFIED-PRIMARY with 3 parks ✓

### **The Problem:**
User pointed out: "But there are 4 parks (at least) in Weston!"

### **The Discovery:**
**Elementary Park** exists in Weston and is:
- ✅ Visible on Google Maps when viewing Weston, Ohio directly
- ❌ NOT listed on the official village Parks & Recreation page
- ❌ NOT findable via web search queries
- ❌ Completely missed by relying on official page alone

### **Why This Matters:**
This demonstrates that **EVEN VILLAGES WITH OFFICIAL PARKS PAGES CAN HAVE INCOMPLETE LISTINGS**.

### **The Methodology Failure:**
**What I did (WRONG):**
1. Found official page ✓
2. Fetched official page ✓
3. Listed parks from dropdown menu ✓
4. Marked as VERIFIED-PRIMARY ✗ ← STOPPED TOO SOON
5. Did NOT view Google Maps ✗✗✗

**What I should have done (CORRECT):**
1. Found official page ✓
2. Fetched official page ✓
3. Listed parks from dropdown menu ✓
4. **OPENED Google Maps and viewed Weston, Ohio directly** ✓
5. **Compared map findings to official list** ✓
6. **Discovered Elementary Park on map** ✓
7. **Investigated why it's not on official page** ✓
8. Marked as VERIFIED-SECONDARY with 4 parks ✓

### **The Lesson:**
**Official government pages can be:**
- Outdated
- Incomplete  
- Under construction
- Missing newer facilities
- Missing facilities managed by other entities
- Simply incorrect

**Google Maps often shows reality on the ground better than official websites.**

### **The Fix:**
**For ALL municipalities, regardless of official page quality:**
1. Fetch and document official page listings
2. **ALSO view Google Maps directly**
3. Compare findings
4. Investigate discrepancies
5. Use higher count when verified
6. Document methodology used

### **Impact on Weston Count:**
- **Official page:** 3 parks
- **Google Maps:** 4 parks (+Elementary Park)
- **Increase:** +33%
- **New status:** VERIFIED-SECONDARY (both sources used)

### **This Case Validates Methodology v5.0:**
✅ Always use multiple verification methods
✅ Never rely solely on official pages
✅ **Actually VIEW maps, don't just search for them**
✅ Compare findings across sources
✅ Investigate discrepancies
✅ Document verification quality honestly

**Bottom line:** If I had followed v5.0 methodology from the start, I would have found Elementary Park immediately. This is why the methodology was created.

---

**END OF METHODOLOGY v5.0 - UPDATED WITH WESTON CASE STUDY**
