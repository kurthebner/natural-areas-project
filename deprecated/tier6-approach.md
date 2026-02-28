# TIER 6 ENTITY DISCOVERY APPROACH

## CHALLENGE:
Tier 6 has 62+ individual parks across 28 municipalities.
Detailed park-by-park lists are in discovery transcripts but not in structured format.

## TWO OPTIONS:

### OPTION A: Extract All 62+ Parks Now (Time: 2-3 hours)
- Go through all Tier 6 discovery documents
- Extract every park name, address, features
- Build complete TSV with all 62 rows
- Pros: Complete data
- Cons: Time-intensive extraction from narrative docs

### OPTION B: Create Municipal Summary + Detail Later (Time: 20 minutes)
- Create TSV with municipal-level summaries (28 rows for municipalities)
- OR create placeholder rows for major systems (Bowling Green, Perrysburg, etc.)
- Note: "Detailed park inventory pending entity-level extraction"
- Pros: Fast, gets structure done
- Cons: Not complete individual park list

### OPTION C: Focus on Major Systems Only (Time: 1 hour)
- Extract detailed parks for top 4 cities (Bowling Green, Perrysburg, Rossford, Northwood)
- These represent ~50 of the 62 parks
- Leave small villages as summary entries
- Pros: Gets 80% of parks with 33% of effort
- Cons: Missing ~12 village parks

## RECOMMENDATION:
**Option C** - Extract major city parks (50 parks), summarize small villages (12 parks).
Balances completeness with efficiency.

