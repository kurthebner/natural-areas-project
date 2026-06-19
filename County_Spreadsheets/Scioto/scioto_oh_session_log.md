# Scioto County, Ohio — Session Log
# Bootstrap: 2026-03-28

---

## County Context

- **County:** Scioto County, Ohio
- **FIPS:** 39145
- **County seat:** Portsmouth
- **Major municipalities:** Portsmouth (city ~18,000), New Boston (village), Lucasville (unincorporated CDP), Minford, McDermott, Wheelersburg, Otway, West Portsmouth, Sciotoville (annexed into Portsmouth)
- **Major waterways:** Scioto River (Ohio River confluence at Portsmouth), Ohio River (southern/eastern border with Kentucky/WV), Scioto Brush Creek, Little Scioto River
- **Park district:** None known — no Scioto County Park District
- **Metropark affiliation:** None — outside MORPC 15-county GPS coverage area
- **Cross-county entities to watch:** Shawnee State Forest (may touch Adams County); Arc of Appalachia preserves (multi-county org, all Scioto seeds appear fully within county); Ohio River border (Lawrence County OH / Greenup/Lewis Counties KY)
- **MORPC GPS layer:** Not applicable — Scioto County is outside coverage; GPS acquisition will require authoritative pages, geocoding, or manual verification

---

## Baseline Pre-Analysis (2026-03-28)

36 seeds read. Tier distribution and flags noted before discovery begins.

### Seeds Requiring Pre-Discovery Judgment

**1. GNIS Pillar features — INCLUDE with full detail**
- Alum Rock (row 4) — GNIS feature type "Pillar" (natural rock formation)
- High Rock (row 15) — same
- Decision 2026-03-28: Include both. Capture all available GNIS and web data (location, elevation, geology, any managing entity). Research during Tier 1/2 pass.

**2. Otway Covered Bridge — assess for historic site status**
- Bridge ID 35-73-15; located in or near Otway, OH
- Covered bridges can be on NRHP and managed as county or township historic sites
- Check Scioto County Engineer / ODNR / NRHP for management and public access status

**3. Millbrook Park (New Boston) — verify current status**
- Described as "formerly an amusement park"; current use unclear
- New Boston is a village — Tier 6 if it's a village park
- Check Village of New Boston

**4. MSPIB entities — sort city park vs. independent**
- Main Street Portsmouth in Bloom (MSPIB) is a civic beautification nonprofit
- "535 On Second" — owned AND managed by MSPIB → potential Tier 8 entity
- "Adopted by MSPIB" parks (Alexandria Park, Roy Rogers Esplanade, York Park, Tracy Park) — likely Portsmouth city parks (Tier 6) with MSPIB as stewardship partner, not owner
- Resolve during Tier 6 Portsmouth pass

**5. Three Bridges Park / Boneyfiddle Project**
- Boneyfiddle is a historic neighborhood in downtown Portsmouth
- The Boneyfiddle Project is a neighborhood revitalization effort
- Determine if Three Bridges Park is a Portsmouth city park or independently managed

**6. Gladys Riley — dual entries (state SNP + Arc of Appalachia preserve)**
- Gladys Riley Golden-star State Nature Preserve (186 ac, ODNR-designated, managed by Arc of Appalachia) — Tier 2
- Gladys Riley Golden Star Lily Preserve (230 ac, Arc of Appalachia) — Tier 8
- These are NOT duplicates: the state designates a subset (186 ac) as a State Nature Preserve; Arc of Appalachia owns the larger parcel (230 ac). Create both records with a parent/child or overlay note. The 44-acre difference likely represents buffer/additional preserve land outside the SNP boundary.
- Acreage discrepancy flag: 230 ac (Arc) vs 186 ac (ODNR) — document both, note in identity_notes

**7. ODNR Historic Sites within Shawnee State Forest**
- CCC Memorial to Company 1545 (Ohio Historic Site #50)
- Copperhead Fire Tower (Ohio Historic Site #6, Ohio's first fire tower, 1924)
- Both located within Shawnee State Forest/Park
- These are child sites of Shawnee State Forest (SC-S-0001 or similar) — create as Sites with parent = Shawnee State Forest
- ODNR "Ohio Historic Site" designation = state-managed historic feature

**8. Clark Planetarium (Shawnee State University)**
- A university building, not a natural area — unlikely to qualify as a Site
- Note during Tier 2 SSU pass; exclude with rationale unless public access/conservation function found

**9. Shawnee State University Campus trails**
- Campus has trails for tree viewing (arboretum function?)
- If formal campus trail system exists, capture as Trail entities under Tier 2 SSU
- URL provided: https://www.shawnee.edu/campus-life/trees/campus-trails

**10. Scioto Bend Preserve (Appalachia Ohio Alliance)**
- Appalachia Ohio Alliance is a separate conservancy from Arc of Appalachia
- No acreage or location in baseline — needs research during Tier 8 pass

---

## Tier Progress

| Tier | Name | Sites | Trails | Segs | TN | SN | APs | Status |
|------|------|-------|--------|------|----|----|-----|--------|
| 1 | Federal | 3 | 0* | 0 | 0 | 0 | 0 | Complete (*WNF trails PENDING) |
| 2 | State | 9 | 13 | 0 | 1 | 0 | 3 | Complete + GPS pass complete |
| 3 | District | - | - | - | - | - | - | Not started |
| 4 | County | - | - | - | - | - | - | Not started |
| 5 | Township | - | - | - | - | - | - | Not started |
| 6 | Municipal | - | - | - | - | - | - | Not started |
| 7 | Conservancy | - | - | - | - | - | - | Not started |
| 8 | Private | - | - | - | - | - | - | Not started |

---

## Baseline Seed Confirmation Tracker

| Seed | Type | Tier | Status | SC-ID |
|------|------|------|--------|-------|
| 535 On Second | MSPIB Park | 8 (or 6) | Pending | — |
| Alexandria Park | Portsmouth City Park | 6 | Pending | — |
| Alum Rock | GNIS Pillar | — | Confirmed (Tier 1, INCLUDE with full detail) — SC-S-0002 pending | SC-S-0002 |
| Bannon Park | Portsmouth City Park | 6 | Pending | — |
| Buckeye Park | Portsmouth City Park | 6 | Pending | — |
| Camp Oyo | BSA camp | 8 | Pending | — |
| CCC Memorial to Company 1545 | ODNR Historic Site | 2 (child) | Confirmed — SC-S-0009 pending | SC-S-0009 |
| Clark Planetarium | SSU property | 2? | Excluded — university building, no conservation function confirmed | — |
| Copperhead Fire Tower | ODNR Historic Site | 2 (child) | Confirmed — SC-S-0010 pending | SC-S-0010 |
| Cyndee Secrest Park | Portsmouth City Park | 6 | Pending | — |
| Earl Thomas Conley Park | Portsmouth City Park | 6 | Pending | — |
| Gladys Riley Golden Star Lily Preserve | Arc of Appalachia | 8 | Pending (Tier 8) | — |
| Gladys Riley Golden-star SNP | State Nature Preserve | 2 | Confirmed — SC-S-0006 pending | SC-S-0006 |
| High Rock | GNIS Pillar | — | Confirmed (Tier 1) — SC-S-0003 pending | SC-S-0003 |
| Labold Ball Fields | Portsmouth City Park | 6 | Pending | — |
| Martha Burton Park | Portsmouth City Park | 6 | Pending | — |
| Millbrook Park | (New Boston) | 6? | Pending | — |
| Mound Park | Portsmouth City Park | 6 | Pending | — |
| Ohio Hanging Rock | Arc of Appalachia | 8 | Pending | — |
| Otway Covered Bridge | Covered bridge | ? | Pending | — |
| Porter Township Park | Township Park | 5 | Pending | — |
| Raven Rock Nature Preserve | State Nature Preserve | 2 | Confirmed — SC-S-0007 pending | SC-S-0007 |
| Roy Rogers Esplanade | Portsmouth City Park | 6 | Pending | — |
| Scioto Bend Preserve | Appalachia Ohio Alliance | 8 | Pending | — |
| Scioto Brush Creek SNP | State Nature Preserve | 2 | Confirmed — SC-S-0008 pending | SC-S-0008 |
| Sciotoville Community Square | Portsmouth City Park | 6 | Pending | — |
| Shawnee State Forest | State Forest | 2 | Confirmed — SC-S-0004 pending | SC-S-0004 |
| Shawnee State Park | State Park | 2 | Confirmed — SC-S-0005 pending | SC-S-0005 |
| Shawnee State University Campus | SSU property | 2 | Confirmed (Deal Arboretum) — SC-S-0011 pending | SC-S-0011 |
| Simon Woods | Arc of Appalachia | 8 | Pending | — |
| Spock Memorial Dog Park | Portsmouth City Park | 6 | Pending | — |
| Three Bridges Park | Boneyfiddle Project | 6? or 8? | Pending | — |
| Tracy Park | Portsmouth City Park | 6 | Pending | — |
| Tremper Mound | Arc of Appalachia | 8 | Pending | — |
| Weghorst Skate Park | Portsmouth City Park | 6 | Pending | — |
| York Park | Portsmouth City Park | 6 | Pending | — |

---

## Session Entries

---

### Tier 1 — Federal (2026-03-28)

**Sources checked:**
- Web search: NPS units in Ohio / Scioto County
- Web search: Wayne National Forest Ironton Unit Scioto County
- Web search: USFWS National Wildlife Refuge Scioto County Ohio
- Web search: USACE Ohio River Scioto County public lands
- Web search: Tribal / federal trust land Scioto County Ohio
- Web search: Portsmouth Earthworks federal designation / NHL
- Web search: GNIS Alum Rock Scioto County Ohio
- Web search: GNIS High Rock Scioto County Ohio
- Fetch blocked: fs.usda.gov, wikipedia, peakvisor, hometownlocator, mountainzone, USACE, GNIS direct API

**Sites found: 3**

1. **Wayne National Forest - Ironton Unit** (SC-S-0001 pending)
   - USDA Forest Service, Ironton Ranger District
   - 107,090 total acres across Lawrence (>2/3), Gallia, Scioto, Jackson counties
   - Scioto County portion: dispersed non-contiguous parcels; no specific named recreation sites confirmed within Scioto County itself
   - Primary developed sites (Lake Vesuvius, Hanging Rock OHV) are in Lawrence County; Symmes Creek trails in Gallia County
   - WNF website blocked — Scioto County trail inventory flagged PENDING VERIFICATION
   - Not in baseline; first encounter during Tier 1

2. **Alum Rock** (SC-S-0002 pending) — GNIS Pillar
   - GPS not found via web search (GNIS direct access blocked)
   - Ownership/management unknown
   - Seeded from baseline row 4

3. **High Rock** (SC-S-0003 pending) — GNIS Pillar
   - GPS 38.5884126°N, -82.7973891°W; elevation ~781 ft; USGS Greenup quad
   - GNIS feature ID: 1076045
   - Ownership/management unknown; near Ohio River
   - Seeded from baseline row 15

**Trails: 0 confirmed** (WNF Scioto County trail inventory incomplete — website blocked; flagged PENDING)

**Trail Segments, Trail Networks, Site Networks, Access Points: 0**

**Null results with evidence:**
- NPS: No NPS units in Scioto County. Hopewell Culture NHP is in Ross County. Portsmouth Earthworks are on NRHP but NOT a National Historic Landmark and NOT part of 2023 UNESCO World Heritage inscription (those 8 sites are in Ross, Licking, Warren, Highland, Miami, and Union counties). Mound Park handled at Tier 6 (Portsmouth city park).
- USFWS: No National Wildlife Refuges in Scioto County. Ohio River Islands NWR is in WV/PA/KY — does not include Ohio shoreline.
- USACE: Ohio River navigation jurisdiction only; no USACE recreation lands or impoundments in Scioto County.
- BLM: No BLM lands in Ohio.
- Tribal: No federal trust lands in Scioto County. Shawnee tribes relocated to Oklahoma; Eastern Shawnee owns ~50 non-trust acres in Ohio elsewhere.

**Baseline seeds confirmed this tier:** Alum Rock ✓, High Rock ✓
**Baseline seeds remaining:** 34

**Tier 1 Status: COMPLETE** (with WNF trail inventory flagged PENDING VERIFICATION)

| Tier | Name | Sites | Trails | Segs | TN | SN | APs | Status |
|------|------|-------|--------|------|----|----|-----|--------|
| 1 | Federal | 3 | 0* | 0 | 0 | 0 | 0 | Complete (*WNF trails PENDING) |

---

### Tier 2 — State (2026-03-28)

**Sources checked:**
- Web search: Shawnee State Forest Ohio acres trails features
- Web search: Shawnee State Park Ohio trails hiking amenities
- Web search: Shawnee State Park hiking trails Ohio list names
- Web search: Shawnee State Forest Ohio mountain bike trails names locations
- Web search: Raven Rock State Nature Preserve Ohio ODNR acres
- Web search: Gladys Riley Golden-star State Nature Preserve Ohio Arc of Appalachia acres
- Web search: Scioto Brush Creek State Nature Preserve Ohio ODNR acres permit features
- Web search: "Scioto Brush Creek" state nature preserve acres permit features ODNR
- Web search: Shawnee State University Deal Arboretum campus trails Ohio
- Web search: Copperhead Fire Tower Shawnee State Forest Ohio historic site
- Web search: CCC Memorial Company 1545 Shawnee State Forest Ohio
- Fetch blocked: naturepreserves.ohiodnr.gov (multiple SNP pages), forestry.ohiodnr.gov, shawnee.edu, trekohio.com, wikipedia

**Sites found: 9**

1. **Shawnee State Forest** (SC-S-0004 pending)
   - ODNR Division of Forestry; 63,747 acres (Scioto and Adams counties)
   - Ohio's largest state forest; ~8,000-acre wilderness; 60+ mi bridle trails; mountain bike trails (names PENDING); Shawnee Backpack Trail
   - Child historic sites: CCC Memorial (SC-S-0009) and Copperhead Fire Tower (SC-S-0010)
   - Seeded from baseline row 26

2. **Shawnee State Park** (SC-S-0005 pending)
   - ODNR Division of Parks and Watercraft; 1,095 acres (discrepancy with baseline 1,163 noted)
   - 10 hiking trails; Shawnee Lodge (50 rooms); Ohio River marina (72 docks); two lakes (68 ac total); campground opened 2023; Black Bear Disc Golf; mini golf
   - Seeded from baseline row 27

3. **Gladys Riley Golden-star State Nature Preserve** (SC-S-0006 pending)
   - ODNR SNP designation (186 ac); land owned and managed by Arc of Appalachia (230 ac)
   - Golden star lily (Ohio Threatened); floodplain trail + oak-hickory hillside trail; permit-only
   - Seeded from baseline row 12

4. **Raven Rock State Nature Preserve** (SC-S-0007 pending)
   - ODNR DNAP; 98 acres; donated 1993; Mississippian sandstone; three natural arches
   - 500-ft overlook (tallest known in Ohio); 1.25-mi one-way trail; permit-only; NHLR listed
   - Seeded from baseline row 21

5. **Scioto Brush Creek State Nature Preserve** (SC-S-0008 pending)
   - ODNR DNAP; 30 acres; permit-only; ODNR page blocked
   - Protects exceptional aquatic biodiversity (70+ fish species); new facilities added (details unconfirmed)
   - Seeded from baseline row 24

6. **CCC Memorial to Company 1545** (SC-S-0009 pending) — *child of Shawnee State Forest*
   - ODNR Historic Site #50; within Shawnee State Forest
   - Exact location within forest not confirmed; GPS flagged for acquisition
   - Seeded from baseline row 6

7. **Copperhead Fire Tower** (SC-S-0010 pending) — *child of Shawnee State Forest*
   - ODNR Historic Site #6; first fire tower built in Ohio (1924); 60-ft steel
   - Copperhead Hill; elevation >1,200 ft; 360-degree view; restored, climbable at own risk; NHLR listed
   - State Forest Service Road 6, West Portsmouth
   - Seeded from baseline row 9

8. **Shawnee State University — Deal Arboretum and Campus Trails** (SC-S-0011 pending)
   - State university campus; ArbNet Level 2 accredited arboretum; 400+ trees, ~100 species
   - Named after Prof. Robert Deal; four named self-guided tree trails; publicly open
   - GPS approx campus centroid: 38.7398°N, -82.9977°W
   - Seeded from baseline row 28

9. **Scioto Brush Creek State Scenic River** (SC-S-0012 pending) — *not in baseline; discovered during Tier 2*
   - ODNR DNAP; designated Ohio's 17th State Scenic River, November 2025 (post-knowledge-cutoff, confirmed via web search)
   - 25.1 river miles from Adams-Scioto county line to Scioto River confluence
   - Distinct from Scioto Brush Creek SNP (SC-S-0008)

**Trails found: 13**

1. **Shawnee Backpack Trail** (SC-T-0001 pending) — 40+ mi main loop (23-mi North Loop / 17-mi South Loop); orange blaze; Buckeye Trail + NCT overlap; parent: Shawnee State Forest + State Park; multi-county
2. **Lampblack Trail** (SC-T-0002 pending) — 1.5 mi; oak-hickory ridgetop; parent: Shawnee State Park
3. **Park Loop Trail** (SC-T-0003 pending) — 4.1 mi; 538-ft gain; most popular day hike; parent: Shawnee State Park
4. **Knighton Nature Trail** (SC-T-0004 pending) — lodge to Turkey Creek Lake; parent: Shawnee State Park
5. **Lookout Trail** (SC-T-0005 pending) — overlook shelter; multiple overlooks; parent: Shawnee State Park
6. **Campground Loop Trail** (SC-T-0006 pending) — short campground loop; parent: Shawnee State Park
7. **Shawnee Forest Day Hike Trail — East Loop** (SC-T-0007 pending) — 7.2 mi; blue blaze; parent: Shawnee State Forest
8. **Shawnee Forest Day Hike Trail — West Loop** (SC-T-0008 pending) — length unconfirmed; parent: Shawnee State Forest
9. **Copperhead Firetower and Bear Lake Trail** (SC-T-0009 pending) — AllTrails name; access to SC-S-0010; parent: Shawnee State Forest
10. **Appalachian Tree Trail** (SC-T-0010 pending) — SSU Deal Arboretum; self-guided; parent: SSU
11. **Around the World Tree Trail** (SC-T-0011 pending) — SSU Deal Arboretum; self-guided; parent: SSU
12. **Relics of the Past Tree Trail** (SC-T-0012 pending) — SSU Deal Arboretum; self-guided; parent: SSU
13. **Medicinal Tree Trail** (SC-T-0013 pending) — SSU Deal Arboretum; self-guided; parent: SSU

**Trail Networks found: 1**

1. **Shawnee Bridle Trail Network** (SC-TN-0001 pending) — 60+ mi equestrian; parent: Shawnee State Forest; multi-county; individual named segments PENDING VERIFICATION; horsemen's campground (20 sites) near Bear Lake

**Trail Segments, Site Networks, Access Points: 0** *(APs added during GPS acquisition pass — see GPS Pass entry below)*

**Null results with evidence:**
- ODNR Wildlife Areas: No Scioto County-specific wildlife area confirmed. Brush Creek Wildlife Area is in Adams County. No other Scioto County wildlife area found.
- Clark Planetarium (SSU): Excluded per pre-discovery analysis. University building; no public conservation or natural areas function confirmed.
- ODNR mountain bike trail names at Shawnee: Trailforks page confirmed trails exist but named trails not confirmed from web search — flagged PENDING VERIFICATION (noted in SC-S-0004 record).

**Additional finds (not in baseline):**
- Scioto Brush Creek State Scenic River (November 2025 designation): post-cutoff find; confirmed via web search; created SC-S-0012 record
- Scioto County Shawnee Bridge to Bridge Route (36-mi shared-roadway bicycle route, Otway Covered Bridge to Mackletree Bridge): noted in identity_notes for SC-S-0004; not created as separate record pending assessment of managing entity and route type

**Baseline seeds confirmed this tier:** Shawnee State Forest ✓, Shawnee State Park ✓, Gladys Riley Golden-star SNP ✓, Raven Rock SNP ✓, Scioto Brush Creek SNP ✓, CCC Memorial to Company 1545 ✓, Copperhead Fire Tower ✓, Shawnee State University ✓ (8 seeds)

**Baseline seeds excluded this tier:** Clark Planetarium ✗ (excluded — no conservation function; university building)

**Baseline seeds confirmed cumulative:** 10 (Tier 1: 2 + Tier 2: 8)
**Baseline seeds remaining:** 26

**Tier 2 Status: COMPLETE**

| Tier | Name | Sites | Trails | Segs | TN | SN | APs | Status |
|------|------|-------|--------|------|----|----|-----|--------|
| 1 | Federal | 3 | 0* | 0 | 0 | 0 | 0 | Complete (*WNF trails PENDING) |
| 2 | State | 9 | 13 | 0 | 1 | 0 | 3 | Complete + GPS pass complete |

---

### GPS Acquisition Pass — Tiers 1–2 (2026-03-28)

**Method:** Chrome browser navigation to ODNR pages and Google Maps to extract GPS coordinates and physical addresses for Tier 1 and Tier 2 entities. No MORPC GPS layer available for Scioto County — all GPS acquired individually.

**GPS updates applied to existing records:**
- **Raven Rock SNP** (SC-S-0006 pending): 38.7186598°N, -83.0547332°W ✓ — also corrected acres to 95 (from 98) and dedication year to 1996; ODNR URL updated to new format
- **Scioto Brush Creek SNP** (SC-S-0008 pending): 38.8414307°N, -83.0949596°W ✓ — address: Tatman-Coe Rd, McDermott, OH 45652
- **Gladys Riley SNP** (SC-S-0007 pending): 38.8506197°N, -83.2018817°W ✓ — address: Tick Ridge-Koenig Hill Rd, Otway, OH 45657
- **Shawnee State Park** (SC-S-0005 pending): 38.7397953°N, -83.2035869°W ✓ — address: 4404 OH-125, West Portsmouth, OH 45663; phone: (740) 858-6652
- **Shawnee State Forest** (SC-S-0004 pending): 38.7032684°N, -83.0888916°W ✓ (HQ reference) — address: 13291 US-52, West Portsmouth, OH 45663; phone: (740) 858-6685
- **Copperhead Fire Tower** (SC-S-0010 pending): 38.7726088°N, -83.1714841°W ✓ — Copperhead Hill, SFSF Rd 6, West Portsmouth, OH 45663
- **Wayne NF / Ironton Unit** (SC-S-0001): GPS already set (38.5884126, -82.7973891) from Tier 1 — no update needed
- **High Rock** (SC-S-0003): GPS already set (38.7398, -82.9977 approx) from Tier 1 — no update needed
- **Alum Rock** (SC-S-0002): GPS still not confirmed — GNIS coordinates unavailable; flagged for future acquisition
- **CCC Memorial** (SC-S-0009 pending): GPS not confirmed — no ODNR web page; location within Shawnee State Forest not pinned; flagged
- **SSU Arboretum** (SC-S-0011 pending): GPS already set (38.7398, -82.9977 campus centroid) from Tier 2 discovery — no update needed
- **Scioto Brush Creek Scenic River** (SC-S-0012 pending): No GPS centroid — 25.1-mile water corridor; intentionally blank

**Access Point records created:**
- **SC-AP-0001** — Shawnee Backpack Trail / State Park Main Trailhead: 38.740963°N, -83.205171°W; St Forest Rd 2, Blue Creek, OH 45616; ap_type: Trailhead; parents: Shawnee State Park + Shawnee State Forest
- **SC-AP-0002** — Shawnee State Forest Headquarters: 38.7032684°N, -83.0888916°W; 13291 US-52, West Portsmouth, OH 45663; ap_type: Parking Area; parent: Shawnee State Forest
- **SC-AP-0003** — Shawnee State Park Marina: 38.6771559°N, -83.1092679°W; Nile Township, OH 45684; ap_type: Marina; parent: Shawnee State Park

**Notable observations during GPS pass:**
- Simon Woods Preserve visible on Google Maps overview of Shawnee area — Arc of Appalachia Tier 8 entity; noted for future
- Shawnee State Park Nature Center appears as separate Google Maps entity (5.0 stars, (740) 858-6652) — potential child site or AP of Shawnee State Park; assess during pipeline or Tier 8 pass
- ODNR DNAP URLs for Gladys Riley and Scioto Brush Creek SNP still use old naturepreserves.ohiodnr.gov format; new ODNR URL format (ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/) confirmed for Raven Rock but not yet verified for other SNPs

**GPS Pass Status: COMPLETE for Tiers 1–2**
*(Alum Rock and CCC Memorial GPS remain unconfirmed; all other entities have GPS or intentionally blank for corridor/GNIS features)*

---

### Tier 3 — District (2026-03-28)

**Scope:** ORC 1545 park/metro park districts; ORC 6101 conservancy/watershed districts; ORC 1515 Soil & Water Conservation Districts.

**Sub-categories investigated:**

**1. ORC 1545 Park/Metro Park District**
- Scioto County government website reviewed; no statutory park district found.
- "Scioto County Parks" listed at 602 7th St, Portsmouth — confirmed to be a county parks department under county commissioners (Tier 4), NOT a separate statutory park district under ORC 1545.
- Web search for "Scioto County Ohio park district ORC 1545 statutory" returned no matches.
- **Result: NULL — no ORC 1545 park district exists in Scioto County.**

**2. ORC 6101 Conservancy/Watershed Districts**
- Muskingum Watershed Conservancy District (MWCD) covers northeast Ohio Muskingum watershed — not applicable to Scioto County.
- Upper Scioto Drainage & Conservancy District found in web search — confirmed to cover Hardin County (headwaters area), not Scioto County.
- Web search for "Scioto County Ohio watershed conservancy district ORC 6101 flood control recreation land" — no Scioto-specific ORC 6101 district found.
- Miami Conservancy District covers the Great Miami watershed in southwest Ohio — not applicable.
- **Result: NULL — no ORC 6101 conservancy or watershed district operates in Scioto County.**

**3. ORC 1515 Soil & Water Conservation District (SWCD)**
- Scioto SWCD official website (sciotoswcd.org) fetched and reviewed via Chrome.
- Content confirmed: agricultural technical assistance only — soil testing, feed testing, farmland preservation easements (agricultural use only), outreach/education programs.
- Zero named natural areas, restoration sites, demonstration areas, wetland restoration projects, or public access lands found.
- County auditor GIS parcel check not independently performed; SWCD website shows no land ownership claims.
- **Result: NULL — Scioto SWCD does not own or manage any natural area parcels eligible for staging.**

**Sources checked:**
- Scioto County government website (scioto.org / commissioners page)
- sciotoswcd.org (official Scioto SWCD website)
- countyoffice.org parks listing for Scioto County
- Web search: "Scioto County Ohio park district ORC 1545 statutory"
- Web search: "Scioto County Ohio watershed conservancy district ORC 6101 flood control recreation land"
- Web search: "Scioto SWCD natural area restoration site land ownership"
- Cross-check: MWCD, Miami Conservancy District, Upper Scioto Drainage & Conservancy District — all confirmed not applicable to Scioto County

**Tier 3 null result (formal):**

```yaml
tier_result:
  tier: 3
  governance_level: District (Park Districts, Conservancy Districts, SWCDs)
  result: null
  entities_found: 0
  sources_checked:
    - Scioto County government website (scioto.org)
    - sciotoswcd.org (Scioto SWCD official site)
    - countyoffice.org Scioto County parks listing
    - Web search — ORC 1545 park district
    - Web search — ORC 6101 conservancy/watershed district
    - Web search — Scioto SWCD land ownership
    - MWCD, Miami Conservancy District, Upper Scioto Drainage & Conservancy District — confirmed not applicable
  notes: >
    No ORC 1545 park district exists in Scioto County. "Scioto County Parks" is a
    county department under county commissioners (Tier 4). No ORC 6101 conservancy
    or watershed district operates within Scioto County boundaries. Scioto SWCD
    website confirms agricultural technical assistance function only — no natural
    area land holdings documented.
```

**Tier 3 Status: COMPLETE — NULL RESULT**

| Tier | Name | Sites | Trails | Segs | TN | SN | APs | Status |
|------|------|-------|--------|------|----|----|-----|--------|
| 1 | Federal | 3 | 0* | 0 | 0 | 0 | 0 | Complete (*WNF trails PENDING) |
| 2 | State | 9 | 13 | 0 | 1 | 0 | 3 | Complete + GPS pass complete |
| 3 | District | 0 | 0 | 0 | 0 | 0 | 0 | Complete — null result |

---

### Tier 4 — County (2026-03-28)

**Sources checked:**
- Scioto County government website (sciotocountyoh.com/recreation, sciotocountyoh.com/nature)
- Scioto Heritage Trail website (sciotoheritagetrail.com)
- portsmouthohio.org (City of Portsmouth website)
- National Register of Historic Places — Scioto County full listing
- Web searches: "Scioto County county park commissioner managed," "Earl Thomas Conley Park ownership," "Bennett Covered Bridge Scioto County," "Burkes Point boat ramp managing agency," "Brush Creek State Forest Scioto County"
- ODNR property page: Brush Creek State Forest
- fishing.org, marinas.com: Burkes Point Boat Ramp

**Key findings and tier routing:**

**Tier 2 misses discovered during Tier 4 research:**
- **Brush Creek State Forest** — ODNR state forest spanning Adams, Pike, and Scioto counties; 13,000+ acres; established 1928; former HQ on SR-73 near Rarden, Scioto County; currently administered from Pike State Forest; named trails: Stone Quarry Trail (hiking) and Coffee Hollow & Crabtree Cemetery Bridle Trail (equestrian). NOT in baseline, NOT discovered during Tier 2 pass. Staged as Tier 2 record.
- **River Otter Trail** — 1.5-mile loop trail at Scioto Brush Creek State Nature Preserve (Tatman-Coe Road, Union Township); described on Scioto Heritage Trail website. Tier 2 trail miss. Staged as Tier 2 record.

**Tier 4 (county-managed) entities found:**

1. **Earl Thomas Conley Riverside Park** — County park at 15888 US-52, West Portsmouth; 81.2 acres; managed by Scioto County Commissioners / Scioto County Parks Department (confirmed via county commissioner news and Scioto Heritage Trail). Features: Allan W. Eckert Trail, Doug Coleman Memorial Splash Pad, Red Bull Pump Track, frisbee golf, sports courts, picnic shelters. Named after country music legend Earl Thomas Conley, a local native. Baseline seed "Earl Thomas Conley Park" (previously assumed city park) — corrected to county governance.
2. **Allan W. Eckert Trail** — Walking/biking trail at ETC Park along the Scioto/Ohio River confluence; named after Ohio historical author Allan W. Eckert.
3. **Burkes Point Boat Ramp** — Ohio River boat ramp at 75 Riverside Drive, Wheelersburg (Porter Township); GPS 38.68880, -82.87650; managing agency uncertain — staged as Tier 4 Access Point with GOVERNANCE_UNCERTAIN flag.

**Deferred to other tiers:**
- Alexandria Point Park → Tier 6 (Portsmouth city park, maintained by MSPIB per portsmouthohio.org)
- Otway Covered Bridge → Tier 8 (Otway Historical Society owns it per Wikipedia — private nonprofit)
- Bennett Schoolhouse Road Covered Bridge → EXCLUDED (owned by Scioto County Airport Authority; no longer in place per search results)
- Horseshoe Mound (NRHP, within Mound Park) → child Site at Tier 6 (Portsmouth city park)
- All other parks on county recreation page (Mound Park, Bannon Park, York Park, Tracy Park, etc.) → Tier 6 (Portsmouth city parks)
- Porter Township Park → Tier 5

**NRHP check results (42 total Scioto County NRHP listings):**
- Horseshoe Mound: within Mound Park (Tier 6); local owner
- Bennett Schoolhouse Road Covered Bridge: owned by Scioto County Airport Authority; not in place; excluded
- Otway Covered Bridge: private owner (Otway Historical Society); Tier 8
- Feurt Mounds/Village Site: private agricultural land; not a natural area park
- Tremper Mound: private agricultural land; overlaps with Arc of Appalachia seed (Tier 8)
- General US Grant Bridge: state transportation asset; not a natural area
- All other NRHP listings: private dwellings, churches, commercial buildings — not natural areas

**Null results with evidence:**
- No county-owned wildlife areas, conservation lands, or natural reserves beyond ETC Park found
- Scioto County tourism page is a mixed listing of all parks regardless of governance tier
- "Scioto County Parks" at 602 7th St, Portsmouth (phone 740-355-8313) operates ETC Park as the county's primary park; no other county parks identified

**Baseline seeds confirmed this tier:** Earl Thomas Conley Park ✓ (governance corrected from city to county)

**Sites found: 1** (Earl Thomas Conley Riverside Park)
**Trails found: 2** (Allan W. Eckert Trail; River Otter Trail at Scioto Brush Creek SNP — Tier 2 miss)
**Tier 2 sites found: 1** (Brush Creek State Forest — miss)
**Tier 2 trails found: 3** (Stone Quarry Trail, Coffee Hollow Bridle Trail, River Otter Trail)
**Access Points found: 1** (Burkes Point Boat Ramp — governance uncertain)

**Tier 4 Status: COMPLETE**

| Tier | Name | Sites | Trails | Segs | TN | SN | APs | Status |
|------|------|-------|--------|------|----|----|-----|--------|
| 1 | Federal | 3 | 0* | 0 | 0 | 0 | 0 | Complete (*WNF trails PENDING) |
| 2 | State | 9+1 | 13+3 | 0 | 1 | 0 | 3 | Complete + 4 misses added |
| 3 | District | 0 | 0 | 0 | 0 | 0 | 0 | Complete — null result |
| 4 | County | 1 | 1 | 0 | 0 | 0 | 1* | Complete (*Burkes Point governance uncertain) |

---

## Tier 5 — Township Discovery
**Date:** 2026-03-28
**Sub-procedure:** na_township_discovery_subproc_v5.4.md

**Sources checked:**
- OTA Active Township Roster (`Townships_Officials2022-2023.xlsx`) — Scioto County filter
- Scioto County government website townships page (sciotocountyoh.com/townships)
- Porter Township website (portertwp.com) — verified Scioto County
- Nile Township website (niletownship.org) — verified Scioto County
- Valley Township website (valleytownship.us) — verified Scioto County
- Jefferson Township Google Sites (sites.google.com/view/jeffersontownshipscioto) — verified Scioto County
- Vernon Township website (scvernontwp.com) — verified Scioto County
- Harrison Township Facebook page (facebook.com/HarrisonTwpSciotoOh) — verified Scioto County
- Google Maps: Clay Township Park Scioto County, Valley Township Park, Madison Township Park Minford
- Mapcarta (mapcarta.com/W558928341) — Clay Township Park OpenStreetMap entry
- MinfordFalcons.net/MadisonTownship.aspx — Madison Township historical page
- Web searches for each of the 16 townships (individual and comparative)

**OTA Roster cross-reference result:**
The OTA 2022–2023 roster lists exactly **16 active townships** in Scioto County:
Bloom, Brush Creek, Clay, Green, Harrison, Jefferson, Madison, Morgan, Nile, Porter, Rarden, Rush, Union, Valley, Vernon, Washington.
Confirmed by Scioto County government website (sciotocountyoh.com/townships), which lists the same 16.

**Handoff correction:** Prior handoff referenced "12 total" townships including "Scioto Township" — INCORRECT. There are 16 active townships and NO Scioto Township in Scioto County. The sciototownshipohio.com website (which appeared in search results) is **Delaware County's** Scioto Township — wrong county, discarded per §4.2a. OTA roster absence + county government website confirmation = Scioto Township does not exist in Scioto County.

**Wrong-county / wrong-state sites discarded (§4.2a):**
- `claytwp.com` — Clay Township, Lancaster County, **Pennsylvania** (contains "Lititz," "Ephrata," "PA Game Commission" — wrong state)
- `harrisontownship.org` — Harrison Township, **Montgomery County** (Dayton area)
- `harrisontwp.us` — Harrison Township, **Gloucester County, New Jersey** — wrong state
- `greentwp.org` — Green Township, **Hamilton County** (Cincinnati area)
- `washingtontwp.org` — Washington Township, **Montgomery County** (Centerville area)
- `sciototownshipohio.com` — Scioto Township, **Delaware County** — wrong county

**Township-by-township findings:**

| Township | Parks Found | Evidence | Status |
|----------|-------------|----------|--------|
| Bloom | 0 | Web searches returned no township parks; Wayne National Forest (4,008 ac) covers part — already Tier 1. No township website found. | COMPLETE |
| Brush Creek | 0 | Web searches returned no township parks. Brush Creek State Forest (Tier 2 miss) covers much of the area. No township website found. | COMPLETE |
| Clay | 1 — **Clay Township Park** | OpenStreetMap (way 558928341) confirms park at GPS 38.78624°N/82.97119°W near Rosemount CDP. Search snippets reference township fiscal officer (740-666-3014) for shelter reservations. No official Clay Twp website for Scioto County found. | COMPLETE |
| Green | 0 | Southeastern rural township bordering Lawrence County. All "Green Township parks" web results returned wrong-county sites (Hamilton, Mahoning counties). No township website found for Scioto County's Green Township. | COMPLETE |
| Harrison | 0 | Facebook page (facebook.com/HarrisonTwpSciotoOh) is minimal — no parks mentioned. "Minford Community Park" referenced in AI summaries could not be confirmed as a named, township-managed park from authoritative sources. No township website found. | COMPLETE |
| Jefferson | 0 | Google Sites page (sites.google.com/view/jeffersontownshipscioto) has sections for Glendale Rental (community building rental), Fire Department, Cemeteries, History — no Parks section. Glendale Rental is a community building, not a park. News article confirms Lucasville (in Jefferson Township) has "no community park." | COMPLETE |
| Madison | 0 | Madison Township Community Center in Minford confirmed via Facebook (facebook.com/p/Madison-Township-Community-Center-100084889157089) — a rental facility for reunions/parties, not a park. No dedicated park found. No township website. | COMPLETE |
| Morgan | 0 | Web searches returned no township parks. Morgan Township is a small rural township along the Scioto River. No township website found. | COMPLETE |
| Nile | 1 — **Friendship Park** | Nile Township website (niletownship.org/parks.html) documents Friendship Park with 3 picnic shelters, baseball, basketball, tennis/pickleball, swings, playground. Open March–October. | COMPLETE |
| Porter | 1 — **Porter Township Park** | Porter Township website (portertwp.com) confirms park at 12063 Gallia Pike, Wheelersburg. Shelter reservable by residents. Pool and Community Center are separate non-natural-area facilities. | COMPLETE |
| Rarden | 0 | Small rural township in northwest Scioto County (village of Rarden). Web searches returned no township parks. No township website found. | COMPLETE |
| Rush | 0 | Rural township along the Scioto River. Web searches returned no township parks. No township website found. | COMPLETE |
| Union | 0 | Contains Scioto Brush Creek SNP (Tier 2) and River Otter Trail (Tier 2 miss). No township-managed parks found. No township website found. | COMPLETE |
| Valley | 0 | Website (valleytownship.us) is administrative only — no parks section. Google Maps shows "Valley Community Services" (583 Robert Lucas Rd) with one review mentioning "Love that there is a park here now!" — no named entity, no independent identity confirmed. Not staged. News article confirms Lucasville (Valley Township) is working to build its first community park (Growing Lucasville Opportunities group, $100K Kubota grant for amphitheater). | COMPLETE |
| Vernon | 1 — **Vernon Township Community Park** | Vernon Township website (scvernontwp.com/about) confirms park at 4168 Turkey Foot Rd. per Community Facilities section. Homepage references Trunk or Treat at the Park. | COMPLETE |
| Washington | 0 | Shawnee State Forest (Tier 2) covers much of the township. County website confirms no municipalities in the township (West Portsmouth CDP only). No township website found for Scioto County's Washington Township. No township parks found. | COMPLETE |

**Key findings:**

1. **Porter Township Park** — Confirmed baseline seed. 12063 Gallia Pike, Wheelersburg, OH 45694. Shelter reservations via Trustee office.
2. **Friendship Park** — NEW FIND. Nile Township. Friendship community near US 52. Seasonal (March–October). Shelters, ball field, courts, playground.
3. **Clay Township Park** — NEW FIND. Near Rosemount CDP, Clay Township. GPS 38.78624°N/82.97119°W from OpenStreetMap. No township website; confirmed via Mapcarta/OSM.
4. **Vernon Township Community Park** — NEW FIND. 4168 Turkey Foot Rd., Vernon Township. Township website confirms active park for community events.

**Null result townships (12):** Bloom, Brush Creek, Green, Harrison, Jefferson, Madison, Morgan, Rarden, Rush, Union, Valley, Washington — all documented with evidence above.

**"Scioto Township" resolution:** Not a Scioto County township. Entry in prior handoff was an error. The OTA roster and Scioto County government website both confirm exactly 16 townships, none named Scioto. The sciototownshipohio.com website is Delaware County's Scioto Township — wrong county, discarded.

**Baseline seeds confirmed this tier:** Porter Township Park ✓

**Sites found: 4** (Porter Township Park, Friendship Park, Clay Township Park, Vernon Township Community Park)
**Trails found: 0**
**Trail Networks found: 0**
**Access Points found: 0**

**Tier 5 Status: COMPLETE**

| Tier | Name | Sites | Trails | Segs | TN | SN | APs | Status |
|------|------|-------|--------|------|----|----|-----|--------|
| 1 | Federal | 3 | 0* | 0 | 0 | 0 | 0 | Complete (*WNF trails PENDING) |
| 2 | State | 9+1 | 13+3 | 0 | 1 | 0 | 3 | Complete + 4 misses added |
| 3 | District | 0 | 0 | 0 | 0 | 0 | 0 | Complete — null result |
| 4 | County | 1 | 1 | 0 | 0 | 0 | 1* | Complete (*Burkes Point governance uncertain) |
| 5 | Township | 4 | 0 | 0 | 0 | 0 | 0 | Complete |

---

## Tier 6 — Municipal
**Session date:** 2026-03-28
**Status:** COMPLETE

### Discovery Protocol
Executed per `na_municipal_discovery_subproc_v5.9.md`. IMP-015 ordering followed: completed all web discovery for all municipalities before running consolidated map verification pass.

### Municipalities Enumerated
Incorporated municipalities in Scioto County, Ohio:
1. **Portsmouth** (city — county seat)
2. **New Boston** (village)
3. **Otway** (village)
4. **Rarden** (village)
5. **South Webster** (village)

### Web Discovery Results (Steps 2–3)

**Portsmouth:**
- Primary authoritative source: portsmouthohio.org/adopt-a-park/ — official Adopt-a-Park program page confirming City owns and maintains 13 parks.
- Secondary source: mspohio.org/city-parks — Main Street Portsmouth In Bloom (MSPIB) lists parks they adopt/maintain.
- City confirmed: 13 parks total. MSPIB sponsors 3 and maintains additional parks in downtown.
- **Key tier decisions:**
  - 535 On Second → Tier 8 (MSPIB-owned pocket park, private nonprofit)
  - Three Bridges Park → Tier 8 (owned by The Boneyfiddle Project, private nonprofit)
  - Alexandria Park = Alexandria Point Park (same entity at 110 Scioto Street)
  - Roy Rogers Esplanade → confirmed City-owned, MSPIB-maintained → Tier 6 confirmed

**New Boston:**
- Village website checked — no parks page found.
- Millbrook Park confirmed via map verification only.

**Otway:**
- Village website checked — no municipal parks page.
- Map verification confirmed no village-owned park within Otway corporate limits.
- Brush Creek Twp. Community Park (5715 OH-348) is Tier 5 entity (township-owned), not Tier 6.
- Historic Otway Covered Bridge = Tier 8 (Otway Historical Society, private).

**Rarden:**
- No village website found.
- Rarden Community Park confirmed via map verification at 1363 Main St.

**South Webster:**
- southwebsterohio.gov checked — redirected to correct site; no parks page found.
- Map verification confirmed no municipal park within village boundary.
- South Webster Soccer Field (bvjeeps.org, (740) 778-2320) is Bloom-Vernon school district athletic field, NOT a municipal park.
- Result: null.

### Consolidated Map Verification Results (Step 4 per IMP-015)

| Municipality | Result |
|---|---|
| Portsmouth | 13 official parks confirmed on map; 2 new finds (Riverfront Park, Larry Hisle Park) flagged for verification |
| New Boston | Millbrook Park confirmed at Oak St (GPS: 38.759116°N, 82.9286962°W) |
| Otway | No municipal park within village limits confirmed |
| Rarden | Rarden Community Park confirmed at 1363 Main St (GPS: 38.923364°N, 83.2461051°W) |
| South Webster | No municipal park found — Soccer Field is school athletic field, not city park |

**Tier 5 misses discovered during map verification:**
- **Brush Creek Twp. Community Park** — 5715 OH-348, Otway, OH (GPS: 38.8600095°N, 83.1922189°W) — Brush Creek Township, missed during Tier 5 pass
- **Eden Park** — Clay Township, OH 45662 (GPS: 38.7747982°N, 82.9421173°W) — possible 2nd Clay Township park, ~2.5 mi from Clay Township Park at 38.78624°N/82.97119°W

**Rotary Park Rt. 23** ruled out — confirmed in South Shore, KY (out of scope).
**Marvin Webster Memorial Park** (5010 North St W) confirmed in South Bloomfield, Pickaway County — NOT in South Webster, Scioto County.

### Entities Discovered

**Portsmouth city parks (13 baseline seeds confirmed):**
| Name | Address | Baseline Seed |
|---|---|---|
| Alexandria Park | Scioto Street | ✓ confirmed |
| Bannon Park | 15th Street and Robinson Avenue | ✓ confirmed |
| Buckeye Park | Williams Street | ✓ confirmed |
| Cyndee Secrest Park | Glen and Harding Avenue (Sciotoville) | ✓ confirmed |
| Labold Ball Fields | Williams and Boundary Streets | ✓ confirmed |
| Martha Burton Park | Front Street | ✓ confirmed |
| Mound Park | 17th Street and Hutchins Avenue | ✓ confirmed |
| Roy Rogers Esplanade | Gallia Street and Chillicothe Street | ✓ confirmed |
| Sciotoville Community Square | Harding Avenue (Sciotoville) | ✓ confirmed |
| Skate Park | 4th Street and Jefferson Street | ✓ confirmed (seed: Weghorst Skate Park) |
| Spock Memorial Dog Park | 2nd & Vine Streets | ✓ confirmed |
| Tracy Park | 9th Street and Chillicothe Street | ✓ confirmed |
| York Park | Ohio Riverfront | ✓ confirmed |

**Portsmouth child Site:**
| Name | Parent | Notes |
|---|---|---|
| Horseshoe Mound | Mound Park | NRHP-listed Hopewell earthwork; discovered at Tier 4 NRHP review |

**Portsmouth new finds (not on Adopt-a-Park list):**
| Name | Address | Flag |
|---|---|---|
| Riverfront Park | 728 2nd Street | VERIFY_IDENTITY_WITH_YORK_PARK |
| Larry Hisle Park | 2238 Thomas Avenue | MINIMAL_DATA; VERIFY_GOVERNANCE (city vs. housing authority) |

**Other municipalities:**
| Name | Municipality | Status |
|---|---|---|
| Millbrook Park | New Boston | ✓ confirmed baseline seed |
| Rarden Community Park | Rarden | New find |

**Tier 5 misses (staged with discovery_tier: 5):**
| Name | Location | Notes |
|---|---|---|
| Brush Creek Twp. Community Park | 5715 OH-348, Otway, OH | Missed at Tier 5; Brush Creek Township |
| Eden Park | Clay Township, OH 45662 | Missed at Tier 5; possible 2nd Clay Twp. park |

### Baseline Seeds Resolved This Tier
All 13 Portsmouth city parks confirmed. Millbrook Park (New Boston) confirmed.
- **Remaining unresolved baseline seeds:** York Park identity question (Riverfront Park overlap); plus Tier 7 and Tier 8 seeds (Arc, AOA, BSA, MSPIB 535 On Second, Three Bridges, Otway Covered Bridge) — addressed at those tiers.

### Tier 6 Summary

| Municipality | Sites | Trails | APs | Notes |
|---|---|---|---|---|
| Portsmouth | 13 + 2 new finds + 1 child | 0 | 0 | 13 seeds confirmed; Horseshoe Mound child; 2 pending verification |
| New Boston | 1 | 0 | 0 | Millbrook Park |
| Otway | 0 | 0 | 0 | Null — Brush Creek Twp. park is Tier 5 |
| Rarden | 1 | 0 | 0 | Rarden Community Park, new find |
| South Webster | 0 | 0 | 0 | Null — soccer field is school athletic facility |

**Tier 6 Status: COMPLETE**

| Tier | Name | Sites | Trails | Segs | TN | SN | APs | Status |
|------|------|-------|--------|------|----|----|-----|--------|
| 1 | Federal | 3 | 0* | 0 | 0 | 0 | 0 | Complete (*WNF trails PENDING) |
| 2 | State | 9+1 | 13+3 | 0 | 1 | 0 | 3 | Complete + 4 misses added |
| 3 | District | 0 | 0 | 0 | 0 | 0 | 0 | Complete — null result |
| 4 | County | 1 | 1 | 0 | 0 | 0 | 1* | Complete (*Burkes Point governance uncertain) |
| 5 | Township | 4+2 | 0 | 0 | 0 | 0 | 0 | Complete + 2 misses found at T6 |
| 6 | Municipal | 15+2 | 0 | 0 | 0 | 0 | 0 | Complete (2 Portsmouth parks flagged VERIFY) |
