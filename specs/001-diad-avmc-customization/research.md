# Research: DIAD AvMC Customization

**Phase 0 Output** | **Date**: 2026-04-26

## R1: Original DIAD Data Schema Mapping

### US Sales (`USSales/Sales.csv`)
- **Columns**: `ProductID, Date, Zip, Units, Revenue`
- **Rows**: ~4.2M
- **Purpose**: Primary dataset for Labs 1–4; teaches data import, modeling, DAX measures, visualizations

### International Sales (`InternationalSales/*.csv`)
- **Columns**: `ProductID, Date, Zip, Units, Revenue, Country`
- **Rows**: ~3M total across 6 country files (AU, CA, DE, JP, MX, NG)
- **Purpose**: Lab 2+ — teaches combining files from a folder, append queries

### Schema Contract Decisions

| Original Column | AvMC Equivalent | Rationale |
|-----------------|-----------------|-----------|
| `ProductID` | `PlatformID` | Numeric FK; maps to weapon system/aircraft platform |
| `Date` | `Date` | Keep as-is; date column for time-intelligence DAX |
| `Zip` | `InstallationCode` | Numeric location code; maps to military installations |
| `Units` | `WorkOrders` | Count metric; work orders / maintenance events |
| `Revenue` | `EngineeringHours` | Continuous metric; hours expended per work order |
| `Country` (intl only) | `Country` | Keep as-is; allied nation for FMS files |

**Decision**: Preserve exact column count and types per file. US file = 5 columns, International files = 6 columns. This ensures lab instructions for import, append, and Power Query steps work with minimal edits.

---

## R2: AvMC Platform & Installation Reference Data

### Platforms (replacing ProductIDs)
Publicly known weapon systems managed or supported by DEVCOM AvMC and AMCOM:

| PlatformID | Platform Name | Category |
|------------|--------------|----------|
| 1001 | AH-64 Apache | Attack Helicopter |
| 1002 | UH-60 Black Hawk | Utility Helicopter |
| 1003 | CH-47 Chinook | Heavy-Lift Helicopter |
| 1004 | UH-72 Lakota | Light Utility Helicopter |
| 1005 | AH-6 Little Bird | Special Ops Helicopter |
| 2001 | GMLRS (Guided MLRS) | Rocket/Missile |
| 2002 | HIMARS | Rocket/Missile Launcher |
| 2003 | THAAD | Missile Defense |
| 2004 | Patriot | Air/Missile Defense |
| 2005 | ATACMS | Tactical Ballistic Missile |
| 2006 | Javelin | Anti-Tank Missile |
| 2007 | Stinger | MANPADS |
| 3001 | MQ-1C Gray Eagle | UAS |
| 3002 | RQ-7 Shadow | UAS |

**Decision**: Use 14 platforms across 3 categories. This provides enough variety for filtering/slicing in labs while staying within publicly known AvMC scope.

### Installations (replacing Zip codes)
Key AMCOM/AvMC-associated installations:

| InstallationCode | Installation Name | State |
|------------------|------------------|-------|
| 35808 | Redstone Arsenal | AL |
| 78419 | Corpus Christi Army Depot | TX |
| 17201 | Letterkenny Army Depot | PA |
| 36362 | Fort Novosel (formerly Rucker) | AL |
| 96859 | Wheeler Army Airfield | HI |
| 98433 | Joint Base Lewis-McChord | WA |
| 31314 | Fort Stewart / Hunter AAF | GA |
| 42223 | Fort Campbell | KY |
| 79916 | Fort Bliss | TX |
| 10996 | West Point (USMA) | NY |
| 28307 | Fort Liberty (formerly Bragg) | NC |
| 80913 | Fort Carson | CO |

**Decision**: Use actual zip codes as InstallationCode values — this allows the original DIAD zip-code-based map visualizations to still function (Power BI can geocode by zip). 12 installations provide adequate geographic spread.

### FMS Partner Nations (replacing international country files)
Allied nations with significant FMS relationships for AvMC platforms:

| Country File | FMS Context |
|-------------|-------------|
| Australia.csv | AH-64E, CH-47F, Javelin |
| Canada.csv | CH-47F, UAS programs |
| Germany.csv | Patriot, CH-47F |
| Japan.csv | AH-64D/E, Patriot, THAAD |
| Mexico.csv | UH-60, light aviation |
| SouthKorea.csv | AH-64E, K-Defense partnerships |

**Decision**: Keep the same 6 country files. Reframe narrative from "consumer sales" to "FMS platform support hours" — the schema stays identical.

---

## R3: Army Brand Colors for Power BI Theme

### Official Army Colors
- **Army Black**: `#2D2926`
- **Army Gold (Star)**: `#C1A875`
- **Army White**: `#FFFFFF`
- **Army Green (uniform)**: `#4B5320`

### Extended Palette for Data Visualization
Power BI needs 10–15 distinguishable data colors. Derived from Army brand with sufficient contrast:

| Swatch | Hex | Usage |
|--------|-----|-------|
| Army Gold | `#C1A875` | Primary series 1 |
| Dark Gold | `#8B7340` | Primary series 2 |
| Army Green | `#4B5320` | Primary series 3 |
| Army Black | `#2D2926` | Primary series 4 |
| Slate Gray | `#6B7A8D` | Neutral series 5 |
| Olive | `#708238` | Accent 1 |
| Sand | `#D2B48C` | Accent 2 |
| Dark Red (alert) | `#8B0000` | Accent 3 / negative |
| Steel Blue | `#4682B4` | Accent 4 |
| Warm Gray | `#9E9E93` | Accent 5 |
| Light Gold | `#E8D5A3` | Background accent |
| Dark Olive | `#3B4219` | Text/border |
| Muted Teal | `#5F8A8B` | Supplemental |
| Khaki | `#BDB76B` | Supplemental |
| Charcoal | `#3C3C3C` | Supplemental |

**Decision**: Use this 15-color palette in the theme JSON, prioritizing Army Gold and Army Green as the lead series colors. This gives strong visual identity while maintaining readability.

---

## R4: DIAD Lab-by-Lab Content Impact

| Lab | Original Focus | Content Requiring Change | Stays As-Is |
|-----|---------------|------------------------|-------------|
| Lab 1 | Connect to data, Power Query | Data source paths, column names in instructions | Power Query concepts, M functions |
| Lab 2 | Data modeling, relationships | Table names, field names, scenario narrative | Star schema concepts, relationship types |
| Lab 3 | DAX measures, calculated columns | Measure names (Revenue → EngineeringHours), narrative | DAX syntax, time intelligence patterns |
| Lab 4 | Visualizations, formatting | Chart titles, labels, logo/background, theme | Chart types, formatting techniques |
| Lab 5 | Power BI Service, sharing | Workspace names, app names if mentioned | Service concepts, RLS, subscriptions |
| Final | End-to-end dashboard | All visual labels, KPI titles, executive summary | Dashboard design principles |

**Decision**: Labs 1–3 require the heaviest edits (data references). Lab 4 requires asset swaps. Lab 5 is mostly tool-generic. All changes are cosmetic/narrative — no structural lab changes needed.

---

## R5: Branding Asset Requirements

| Asset | Current | Replacement Needed |
|-------|---------|-------------------|
| `VanArsdel_Logo.png` (979×122px) | VanArsdel company logo | DEVCOM AvMC logo, similar dimensions |
| `Background.jpg` (1280×720px) | Generic blue business background | Defense/engineering themed background |
| `DIADTheme2.json` | Blue-dominant commercial palette | Army Gold/Green/Black palette |

**Decision**: Logo can be sourced from public DEVCOM AvMC imagery or created as a text-based placeholder. Background should be a subtle dark/textured image compatible with light-colored chart overlays.

---

## Summary of All Decisions

1. **Schema**: Exact column-count preservation; rename semantics only
2. **Platforms**: 14 publicly-known AvMC weapon systems across 3 categories
3. **Locations**: 12 real installations using actual zip codes for geocoding
4. **FMS nations**: Same 6 countries, reframed as FMS support
5. **Colors**: 15-color Army-brand palette led by Gold and Green
6. **Lab impact**: Cosmetic/narrative changes only; lab sequence untouched
7. **Assets**: 3 files to replace (logo, background, theme JSON)
