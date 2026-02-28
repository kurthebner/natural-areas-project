# ENTITY-SPECIFIC DISCOVERY DATA COLLECTION TEMPLATE v4.0

**Purpose:** Collect structured entity-level data for Sites during discovery phase  
**Aligned With:** Site Schema Module v4.0, Site TSV Output Specification v4.0  
**Date Created:** February 16, 2026

---

## FIELD COLLECTION PRIORITY

### **TIER 1: REQUIRED FIELDS** (Must collect for every site)
These fields are absolutely required for valid TSV output:

1. **name** - Official site name (string, required)
2. **county_list** - County/counties (semicolon-delimited, alphabetized, required)

### **TIER 2: HIGH-PRIORITY FIELDS** (Collect whenever available)
These fields are critical for site identification and usability:

3. **category** - Site type classification (from vocabulary)
4. **ownership** - Legal owner (exact entity name, not category)
5. **gps_primary** - GPS coordinates (lat,lon format)
6. **address** - Full street address
7. **acres** - Acreage (numeric)
8. **url_primary** - Primary official URL

### **TIER 3: MEDIUM-PRIORITY FIELDS** (Collect when readily available)
These fields enhance data quality but aren't critical:

9. **subtype** - Category-specific subtype (from vocabulary)
10. **governance** - Managing entity (if different from owner)
11. **description** - Brief site description
12. **features** - Amenities/features (semicolon-delimited, from vocabulary)
13. **plus_code** - Google Plus Code
14. **designation** - Formal legal/administrative status (semicolon-delimited)

### **TIER 4: OPTIONAL FIELDS** (Collect if easily accessible)
Nice to have but not essential:

15. **coordination** - Partner organizations (semicolon-delimited)
16. **network_affiliation** - Formal network membership
17. **municipality** - City/village name (semicolon-delimited)
18. **township** - Township name (semicolon-delimited)
19. **location** - Human-readable location description
20. **notes** - Additional notes/context
21. **status** - Current operational status (from vocabulary)
22. **parent_site_id** - Parent site reference (for child sites)

### **TIER 5: PROVENANCE FIELDS** (Auto-collected)
Automatically captured during discovery:

23. **source_primary** - Primary source URL/reference
24. **source_all** - All sources (semicolon-delimited)
25. **discovery_tier** - Which tier discovered (1-8)
26. **discovered_date** - Date of discovery

---

## DATA COLLECTION SPREADSHEET STRUCTURE

### **Column Headers** (in order for CSV/TSV)

```
name	category	subtype	ownership	governance	address	acres	gps_lat	gps_lon	plus_code	county_list	municipality	township	description	features	designation	status	url_primary	notes	parent_site_id	source_primary	discovery_tier
```

### **Field-by-Field Collection Guide**

#### **1. name** (REQUIRED)
- **What:** Official published site name
- **How:** From official website, signage, or authoritative source
- **Format:** Exact official name, title case
- **Examples:** 
  - ✅ "Mary Jane Thurston State Park"
  - ✅ "Carter Historic Farm"
  - ❌ "The Carter Farm" (if official name is "Carter Historic Farm")
  - ❌ "WINTERGARDEN PARK" (should be title case)

#### **2. category** (HIGH PRIORITY)
- **What:** Highest-level site classification
- **How:** Classify using Site Category Vocabulary
- **Format:** Single value from controlled vocabulary
- **Common Values:** 
  - State Park, County Park, Municipal Park
  - Nature Preserve, Wildlife Area
  - Historic Site, Recreation Area
- **Where to find:** Usually in site description or official designation

#### **3. subtype** (MEDIUM PRIORITY)
- **What:** Category-specific refinement
- **How:** Based on category, use appropriate subtype vocabulary
- **Format:** Single value, category-dependent
- **Examples:**
  - Category: "County Park" → Subtype: "Historic Farm"
  - Category: "State Park" → Subtype: "Day Use"

#### **4. ownership** (HIGH PRIORITY)
- **What:** Legal title holder (exact entity name)
- **How:** From official sources, property records, or authoritative documentation
- **Format:** Exact legal name, not generic category
- **Examples:**
  - ✅ "State of Ohio"
  - ✅ "Wood County Park District"
  - ✅ "City of Bowling Green"
  - ✅ "Black Swamp Conservancy"
  - ❌ "State Government" (too generic)
  - ❌ "County" (too generic)

#### **5. governance** (MEDIUM PRIORITY)
- **What:** Operational manager (if different from owner)
- **How:** From official sources
- **Format:** Exact organization name
- **Examples:**
  - Owner: "State of Ohio" / Governance: "Wood County Park District" (leased operation)
  - Owner: "City of Bowling Green" / Governance: "City of Bowling Green" (same - can leave blank)

#### **6. address** (HIGH PRIORITY)
- **What:** Full street address
- **How:** From official website, Google Maps, or signage
- **Format:** Street address, City, State ZIP
- **Examples:**
  - ✅ "18331 Carter Road, Bowling Green, OH 43402"
  - ✅ "26940 Lime City Rd, Perrysburg, OH 43551"
  - ⚠️ "Bowling Green, OH" (acceptable if no street address available)

#### **7. acres** (HIGH PRIORITY)
- **What:** Site acreage
- **How:** From official sources (website, master plan, park district)
- **Format:** Numeric value (no "acres" text)
- **Examples:**
  - ✅ 104
  - ✅ 44.5
  - ✅ 0.5
  - ❌ "104 acres" (remove text)
  - ⚠️ Leave blank if only estimate available (document in notes: "~100 acres estimated")

#### **8-9. gps_lat / gps_lon** (HIGH PRIORITY)
- **What:** GPS coordinates in decimal degrees
- **How:** From Google Maps, official site, or geocoding
- **Format:** Decimal degrees, 6 decimal places, lat/lon separate columns
- **Examples:**
  - ✅ Lat: 41.374800  Lon: -83.651300
  - ✅ Lat: 41.5000    Lon: -83.6500
  - ❌ 41°22'29.3"N (convert to decimal)
  - ❌ Combined: "41.3748,-83.6513" (split into two columns)

**How to get from Google Maps:**
1. Search for site name or address
2. Right-click on location
3. Click first item (coordinates)
4. Copy coordinates (format: 41.374800, -83.651300)
5. Split: first number = lat, second = lon (make negative for West)

#### **10. plus_code** (MEDIUM PRIORITY)
- **What:** Google Plus Code
- **How:** From Google Maps
- **Format:** Plus code string
- **Example:** "9274+8F Bowling Green, Ohio"

**How to get:**
1. In Google Maps, click on location
2. Plus code appears below coordinates
3. Copy full code

#### **11. county_list** (REQUIRED)
- **What:** County or counties
- **How:** Geographic verification
- **Format:** Semicolon-delimited, alphabetized, no "County" suffix
- **Examples:**
  - ✅ "Wood"
  - ✅ "Fulton;Wood" (multi-county, alphabetized)
  - ❌ "Wood County" (remove "County")
  - ❌ "Wood;Fulton" (not alphabetized)

#### **12. municipality** (OPTIONAL)
- **What:** Incorporated city/village
- **How:** From address or geographic verification
- **Format:** City/village name, semicolon-delimited if multiple
- **Examples:**
  - ✅ "Bowling Green"
  - ✅ "Perrysburg"
  - Leave blank if in unincorporated area

#### **13. township** (OPTIONAL)
- **What:** Township name
- **How:** From address or geographic verification  
- **Format:** Township name, semicolon-delimited if multiple
- **Examples:**
  - ✅ "Perrysburg Township"
  - ✅ "Lake Township"

#### **14. description** (MEDIUM PRIORITY)
- **What:** Brief site description (1-3 sentences)
- **How:** From official website or brochure
- **Format:** Plain text, concise
- **Example:** "120-acre nature preserve featuring wetlands, mature forest, and 5+ miles of hiking trails. Includes observation tower and environmental education center."

#### **15. features** (MEDIUM PRIORITY)
- **What:** Amenities and features
- **How:** From official website, visit, or park map
- **Format:** Semicolon-delimited list from Features Vocabulary
- **Examples:**
  - ✅ "Hiking Trails;Fishing;Playground;Picnic Area"
  - ✅ "Nature Trails;Wildlife Viewing;Education Center"
  - ❌ "Has trails and playground" (use controlled terms, semicolon-delimited)

**Common Features:** (from vocabulary)
- Hiking Trails, Biking Trails, Nature Trails
- Fishing, Boating, Swimming
- Playground, Picnic Area, Shelter
- Restrooms, Parking
- Wildlife Viewing, Bird Watching
- Education Center, Visitor Center

#### **16. designation** (MEDIUM PRIORITY)
- **What:** Formal legal/administrative status
- **How:** From official sources, must be formally documented
- **Format:** Semicolon-delimited from Designation Vocabulary
- **Examples:**
  - ✅ "State Nature Preserve"
  - ✅ "National Register of Historic Places"
  - ✅ "Conservation Easement"
  - ❌ "Beautiful Park" (not a formal designation)

#### **17. status** (OPTIONAL)
- **What:** Current operational status
- **How:** From official sources
- **Format:** Single value from Status Vocabulary
- **Values:** Open, Closed, Seasonal, Under Development, Planned

#### **18. url_primary** (HIGH PRIORITY)
- **What:** Primary official URL
- **How:** Official park/site website
- **Format:** Full URL
- **Examples:**
  - ✅ "https://wcparks.org/carter-historic-farm"
  - ✅ "https://parks.ohiodnr.gov/maryjane thurston"

#### **19. notes** (OPTIONAL)
- **What:** Additional context, uncertainties, or special notes
- **Format:** Free text
- **Examples:**
  - "Acreage estimate only - official count not published"
  - "Operates under lease from State of Ohio to WCPD"
  - "Tri-county site - main entrance in Wood County"

#### **20. parent_site_id** (OPTIONAL)
- **What:** Reference to parent site (for child sites)
- **How:** If site is part of a larger site system
- **Format:** Will be resolved during normalization
- **Examples:**
  - Site: "City Park Pool" → Parent: "City Park"
  - Leave blank for most sites

#### **21. source_primary** (AUTO-COLLECTED)
- **What:** Primary authoritative source
- **How:** URL of main source used for discovery
- **Format:** Full URL
- **Auto-populated:** From discovery process

#### **22. discovery_tier** (AUTO-COLLECTED)
- **What:** Which tier discovered site
- **How:** Automatically assigned
- **Format:** 1-8
- **Auto-populated:** During discovery

---

## COLLECTION WORKFLOW

### **For Each Site:**

**STEP 1: Navigate to Official Page or Google Maps**
- Official website preferred
- Google Maps as fallback

**STEP 2: Collect REQUIRED Fields First**
- name
- county_list

**STEP 3: Collect HIGH-PRIORITY Fields**
- category
- ownership
- gps_lat, gps_lon
- address
- acres
- url_primary

**STEP 4: Collect MEDIUM-PRIORITY Fields (if visible)**
- subtype
- governance
- description
- features
- plus_code

**STEP 5: Collect OPTIONAL Fields (if easy)**
- municipality
- township
- designation
- notes

**STEP 6: Document Source**
- source_primary (URL used)

**STEP 7: Quality Check**
- Name spelled correctly?
- GPS coordinates have negative longitude?
- Acreage is numeric only?
- County list alphabetized if multiple?

---

## COLLECTION TOOLS

### **Primary Tools:**
1. **Official Website** - Best source for name, ownership, description, features
2. **Google Maps** - GPS, Plus Code, address verification
3. **Park District Master Plans** - Acreage, features, management
4. **Discovery Documentation** - Already have name, ownership, tier

### **Lookup Sequences:**

**For County Parks:**
1. WCPD website → Park page
2. Copy: name, description, features, acreage
3. Google Maps → GPS, Plus Code, address
4. Record ownership: "Wood County Park District"
5. Record category: "County Park"

**For Municipal Parks:**
1. City website → Parks page
2. Copy: name, description, features
3. Google Maps → GPS, Plus Code, address, acreage estimate
4. Record ownership: "City of [Name]"
5. Record category: "Municipal Park"

**For State/Private:**
1. Official website → All available data
2. Google Maps → GPS, Plus Code
3. Document ownership, governance from official sources

---

## QUALITY STANDARDS

### **Minimum Acceptable Record:**
- ✅ name (required)
- ✅ county_list (required)
- ✅ category (highly recommended)
- ✅ ownership (highly recommended)
- ⚠️ GPS coordinates (should have, but can proceed without)

### **Target Quality Record:**
- ✅ All Tier 1 + Tier 2 fields
- ✅ 50%+ of Tier 3 fields
- ✅ Source documented

### **Gold Standard Record:**
- ✅ All Tier 1-3 fields
- ✅ Some Tier 4 fields
- ✅ Multiple sources verified

---

## VOCABULARY QUICK REFERENCE

### **Category** (most common)
- State Park
- County Park  
- Municipal Park
- Nature Preserve
- Wildlife Area
- Historic Site
- Recreation Area
- Campground

### **Features** (most common)
- Hiking Trails
- Biking Trails
- Fishing
- Playground
- Picnic Area
- Restrooms
- Parking
- Wildlife Viewing

*Full vocabularies: See Site Vocabulary Module v4.0*

---

## EXAMPLE COMPLETED RECORDS

### **Example 1: State Park**
```
name: Mary Jane Thurston State Park
category: State Park
subtype: Day Use
ownership: State of Ohio
governance: Wood County Park District
address: 1466 State Route 65, Bowling Green, OH 43402
acres: 104
gps_lat: 41.3748
gps_lon: -83.6513
plus_code: 9274+8F Bowling Green, Ohio
county_list: Fulton;Wood
municipality: 
township: 
description: 104-acre state park along the Maumee River featuring hiking trails, fishing, canoeing access, and historic canal lock remains.
features: Hiking Trails;Fishing;Canoeing;Historic Site;Picnic Area;Restrooms;Parking
designation: 
status: Open
url_primary: https://parks.ohiodnr.gov/maryjane thurston
notes: Multi-county park shared with Fulton County. Operated under lease by WCPD.
parent_site_id: 
source_primary: https://parks.ohiodnr.gov/maryjane thurston
discovery_tier: 1
```

### **Example 2: County Park**
```
name: Carter Historic Farm
category: County Park
subtype: Historic Farm
ownership: Wood County Park District
governance: 
address: 18331 Carter Road, Bowling Green, OH 43402
acres: 60
gps_lat: 41.3401
gps_lon: -83.7145
plus_code: 87QP+MX Bowling Green, Ohio
county_list: Wood
municipality: 
township: Lake Township
description: 60-acre working historic farm featuring 1920s farmstead, antique farm equipment, animals, and agricultural education programs.
features: Historic Site;Education Center;Nature Trails;Parking;Picnic Area
designation: Conservation Easement
status: Open
url_primary: https://wcparks.org/carter-historic-farm
notes: BSC holds conservation easement. Restored wetlands added 2019.
parent_site_id: 
source_primary: https://wcparks.org/carter-historic-farm
discovery_tier: 3
```

### **Example 3: Municipal Park (Minimal Data)**
```
name: Jerry City Village Park
category: Municipal Park
subtype: 
ownership: Village of Jerry City
governance: 
address: Jerry City, OH 43437
acres: 
gps_lat: 41.2456
gps_lon: -83.6892
plus_code: 
county_list: Wood
municipality: Jerry City
township: 
description: 
features: Playground;Picnic Area
designation: 
status: Open
url_primary: 
notes: Discovered via Google Maps verification - not on official village website. Acreage unknown.
parent_site_id: 
source_primary: Google Maps
discovery_tier: 6
```

---

## FILE FORMAT

### **Recommended: Google Sheets or CSV**
- Tab-separated values (TSV) for export
- UTF-8 encoding
- One row per site
- Header row with field names
- Empty cells for missing data (don't use "N/A" or "-")

### **Naming Convention:**
`wood-county-entity-discovery-YYYYMMDD.csv`

Example: `wood-county-entity-discovery-20260216.csv`

---

## NEXT STEPS AFTER COLLECTION

1. **Complete entity discovery for all tiers**
2. **Review for completeness**
3. **Export as TSV**
4. **Pass to Normalization Engine**
5. **Normalization applies vocabularies and formatting**
6. **Generate final Sites.tsv output**

---

**Template Version:** 4.0  
**Last Updated:** February 16, 2026  
**Status:** Ready for Wood County Entity Discovery
