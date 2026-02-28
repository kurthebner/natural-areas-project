# REVISED ENTITY DISCOVERY APPROACH

## CHALLENGE IDENTIFIED:
Getting precise GPS coordinates for 92-94 sites via web search is:
- Time-consuming (5-10 searches per site)
- Inconsistent results (some addresses don't return coordinates)
- Would take 10-15 hours of tedious searching

## BETTER APPROACH - MVP FIRST:

### **PHASE 1: Collect What We Have (NOW - 1 hour)**
Create TSV with ALL sites using data from discovery phase:
- ✅ Name, ownership, category (have for all sites)
- ✅ Address (have for ~50% of sites)
- ✅ Acreage (have for ~40% of sites)  
- ✅ Features, descriptions (have from discovery)
- ⚠️ GPS coordinates (SKIP for now - mark as TBD)

**Result:** Complete MVP TSV with 85% of fields populated

### **PHASE 2: GPS Enrichment (LATER - separate task)**
Two options:
1. **Batch geocoding:** Use geocoding API or service to convert all addresses to GPS
2. **Manual maps:** Open Google Maps for each site, copy coordinates
3. **User does it:** Skippy can add GPS coordinates if needed

## RECOMMENDATION:

**Proceed with MVP approach:**
1. Build complete TSV now with all available data
2. Leave GPS/Plus Code blank (or use approximate city-level coordinates)
3. Mark as "entity-level data pending GPS enrichment"
4. Pass to normalization (which can work with missing GPS)
5. Add GPS coordinates later if needed

**Time savings:** 1-2 hours instead of 10-15 hours

**Quality:** Still get 85% complete data, can enrich GPS later

