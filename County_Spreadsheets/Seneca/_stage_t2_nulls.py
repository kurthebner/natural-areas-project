import yaml, pathlib

f = pathlib.Path(r"D:\users\user1\Documents\CP Projects\Natural Areas Project v5\County_Spreadsheets\Seneca\seneca_ohio_raw_discovery.yaml")
data = yaml.safe_load(f.read_text(encoding="utf-8"))
data.setdefault("tier_nulls", [])

t2_nulls = [
    {
        "tier": 2,
        "governance_level": "ODNR Division of Parks and Watercraft (State Parks)",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://parks.ohiodnr.gov/",
            "https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property",
        ],
        "reasoning": (
            "No ODNR state park is located in Seneca County. Web search for 'Ohio state parks Seneca County' "
            "returned only Seneca County Park District (county-level) results, not any ODNR Division of Parks "
            "and Watercraft facility. No ODNR boating access or state park waterway in Seneca County found."
        ),
    },
    {
        "tier": 2,
        "governance_level": "ODNR Division of Forestry (State Forests)",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://en.wikipedia.org/wiki/List_of_Ohio_state_forests",
            "https://dam.assets.ohio.gov/image/upload/ohiodnr.gov/documents/forestry/maps/State_Forest_Guide_Update_10082024.pdf",
        ],
        "reasoning": (
            "Ohio has 22-24 state forests, all located in southeastern/southern/eastern Ohio. "
            "Wikipedia's complete list of Ohio state forests confirms none are in Seneca County. "
            "Seneca County is in the northwest Ohio glaciated plain — no state forest in this region."
        ),
    },
    {
        "tier": 2,
        "governance_level": "Ohio History Connection (OHC)",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://www.ohiohistory.org/preserve/state-historic-sites-and-museums/",
        ],
        "reasoning": (
            "Ohio History Connection does not manage any historic sites or natural areas in Seneca County. "
            "Note: Hayes Presidential Library & Museums (Rutherford B. Hayes) is in Fremont, Sandusky County — "
            "confirmed not in Seneca County. The baseline seed for Hayes Library is a baseline error. "
            "(Confirmed in prior session.)"
        ),
    },
    {
        "tier": 2,
        "governance_level": "Ohio Department of Transportation (ODOT) — scenic byways, rest areas, bikeway corridors",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://www.scenicoh.com/scenic-byways-1",
            "https://www.ohiodnr.gov/",
        ],
        "reasoning": (
            "No ODOT-designated scenic byway with formal recreation facilities found in Seneca County. "
            "No ODOT rest areas with nature trails or bikeway corridors confirmed in Seneca County. "
            "Ohio's 27 scenic byways primarily run through scenic/hilly regions; none identified in "
            "Seneca County's flat agricultural terrain."
        ),
    },
    {
        "tier": 2,
        "governance_level": "Public Universities (Tier 2 — state-funded, Ohio)",
        "entity_type": "All",
        "result": "null",
        "sources_checked": [
            "https://en.wikipedia.org/wiki/Heidelberg_University_(Ohio)",
            "https://www.tiffin.edu/",
        ],
        "reasoning": (
            "Seneca County has two universities: Heidelberg University and Tiffin University. "
            "Both are PRIVATE universities — neither is a state/public institution. "
            "Heidelberg University (110 acres, Tiffin) has campus woodlands/arboretum but is private — Tier 8. "
            "Tiffin University Nature Preserve is managed by the Seneca County Park District — Tier 4. "
            "No public university natural areas in Seneca County."
        ),
    },
    {
        "tier": 2,
        "governance_level": "ODNR Division of Wildlife — Wildlife Production Areas (WPA)",
        "entity_type": "All",
        "result": "null (unresolved baseline seeds)",
        "sources_checked": [
            "https://codes.ohio.gov/ohio-administrative-code/rule-1501:31-15-04",
            "https://www.law.cornell.edu/regulations/ohio/Ohio-Admin-Code-1501-31-15-06",
        ],
        "reasoning": (
            "Baseline lists 'Wildlife Production Area 64' (88.31 acres) and 'Lake Lepomis Wildlife Area' "
            "as state wildlife areas. Neither appears in OAC Rule 1501:31-15-04 (state hunting areas) "
            "or any ODNR web source. WPA 64 naming convention (Pittman-Robertson numbered parcels) "
            "is not separately enumerated in Ohio administrative code. "
            "Both staged as unresolved_baseline_seed held entities — cannot confirm from authoritative sources. "
            "NOTE: NCIT (North Coast Inland Trail, OH-MC-T-0110) confirmed to NOT extend into Seneca County "
            "— trail documented only in Erie/Huron/Ottawa/Sandusky counties."
        ),
    },
    {
        "tier": 2,
        "governance_level": "Ohio EPA / Village of Attica — Attica Upground Reservoirs",
        "entity_type": "Site",
        "result": "null (unresolved baseline seeds — likely non-qualifying water supply infrastructure)",
        "sources_checked": [
            "https://www.wikidata.org/wiki/Q35695787",
            "https://senecahealthdept.org/attica-water-supply-remains-safe-after-derailment/",
            "https://dam.assets.ohio.gov/image/upload/epa.ohio.gov/Portals/29/public%20comment%20docs/Attica-Regionalization-LER_FNSI.pdf",
        ],
        "reasoning": (
            "Baseline lists 'Attica Upground Reservoir' and 'Attica Upground Reservoir #2' as Ohio EPA water "
            "supply reservoirs in Seneca County. These are public water supply infrastructure operated by the "
            "Village of Attica (Reservoir #2 holds ~49.6 million gallons). "
            "No formal ODNR or state management for recreation confirmed. "
            "Informal birding access noted (eBird hotspot L3625317) but no managed natural area designation. "
            "Staged as unresolved_baseline_seed — flagged for human verification of recreation access status."
        ),
    },
    {
        "tier": 2,
        "governance_level": "ODNR Division of Wildlife — Clinton Nature Preserve (ODNR-owned, deferred)",
        "entity_type": "Site",
        "result": "deferred_to_tier_4",
        "sources_checked": [
            "https://www.senecacountyparks.com/places/clinton-nature-preserve",
        ],
        "reasoning": (
            "Clinton Nature Preserve (33 acres, 400 East TR 132, Tiffin) is ODNR-owned land leased to and "
            "managed by the Seneca County Park District. Per NAP governance tier protocol, "
            "management tier governs for discovery. SCPD is the managing entity → Tier 4. "
            "Will be staged as a Tier 4 entity (Seneca County Park District) during Tier 4 discovery."
        ),
    },
]

for null in t2_nulls:
    data["tier_nulls"].append(null)

data["current_tier"] = 3
data["discovery_status"] = "IN_PROGRESS"

f.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
print(f"Added {len(t2_nulls)} T2 null blocks. Total tier_nulls: {len(data['tier_nulls'])}")
print(f"Total records: {len(data['records'])}")
