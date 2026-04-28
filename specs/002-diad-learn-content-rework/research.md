# Research: DIAD AvMC Customization

**Phase 0 Output** | **Date**: 2026-04-26 | **Updated**: 2026-04-26

## R1: Original DIAD Data Schema Mapping

### US Sales (`USSales/Sales.csv`)
- **Columns**: `ProductID, Date, Zip, Units, Revenue`
- **Rows**: ~4.2M
- **Purpose**: Primary dataset for Labs 1–4; teaches data import, modeling, DAX measures, visualizations

### International Sales (`InternationalSales/*.csv`)
- **Columns**: `ProductID, Date, Zip, Units, Revenue, Country`
- **Rows**: ~3M total across 6 country files (AU, CA, DE, JP, MX, NG)
- **Purpose**: Lab 2+ — teaches combining files from a folder, append queries

### Schema Contract Decisions (Final — Option C)

| Original Column | AvMC Equivalent | Rationale |
|-----------------|-----------------|-----------|
| `ProductID` | `ProgramID` | Numeric FK; maps to R&D program (FLRAA, FARA, PrSM, etc.) |
| `Date` | `Date` | Keep as-is; date column for time-intelligence DAX |
| `Zip` | `LabCode` | Numeric location code; maps to test/research labs (uses real zip codes) |
| `Units` | `ResearchTasks` | Count metric; discrete tasks completed per work period |
| `Revenue` | `LaborHours` | Continuous metric; engineering hours expended |
| `Country` (intl only) | `Country` | Keep as-is; allied nation for FMS/international program files |

### Folder / File Renames

| Original | AvMC Version |
|----------|-------------|
| `USSales/` | `USEngineering/` |
| `Sales.csv` | `RDWorkload.csv` |
| `InternationalSales/` | `InternationalPrograms/` |
| `Nigeria.csv` | `SouthKorea.csv` |

### Table Renames (Power BI model)

| Original Table | AvMC Table | Rationale |
|---------------|-----------|-----------|
| Sales | RDWorkload | R&D engineering workload fact table |
| Product | Program | R&D programs (FLRAA, PrSM, THAAD, etc.) |
| Manufacturer | Directorate | Army organizations (DEVCOM AvMC, PEO M&S, etc.) |
| Geography | Lab | Test/research facility locations |

**Decision**: Preserve exact column count and types per file. US file = 5 columns, International files = 6 columns. This ensures lab instructions for import, append, and Power Query steps work with minimal rewiring.

---

## R2: AvMC R&D Programs & Lab Reference Data

### Programs (replacing Products via bi_dimensions.xlsx)

14 programs across 4 categories reflecting DEVCOM AvMC's mission areas:

| ProgramID | Program Name | Category |
|-----------|-------------|----------|
| 1001 | FLRAA (V-280 Valor) | Future Vertical Lift |
| 1002 | FARA | Future Vertical Lift |
| 1003 | ITEP (T901 Engine) | Future Vertical Lift |
| 1004 | MOSA Avionics | Future Vertical Lift |
| 1005 | Black Hawk Aircrew Trainer | Modeling & Simulation |
| 2001 | PrSM (Precision Strike Missile) | Long Range Precision Fires |
| 2002 | HIMARS Modernization | Long Range Precision Fires |
| 2003 | Hypersonic Weapon Components | Long Range Precision Fires |
| 2004 | LRPF Next-Gen Propulsion | Long Range Precision Fires |
| 2005 | IFPC (Indirect Fire Protection) | Air & Missile Defense |
| 2006 | THAAD Modernization | Air & Missile Defense |
| 2007 | Patriot Next-Gen Radar | Air & Missile Defense |
| 3001 | Directed Energy Weapons | Emerging Technology |
| 3002 | Counter-UAS Systems | Emerging Technology |

**Decision**: 14 programs across 4 categories. High-volume programs (FLRAA, FARA, ITEP) have higher activity weights. Programs use pipe-delimited Category|Program format in bi_dimensions.xlsx matching original DIAD Product table structure.

### Labs (replacing Geography zip codes)

12 labs using actual zip codes for Power BI geocoding:

| LabCode | Lab Name | State |
|---------|---------|-------|
| 35808 | Redstone Arsenal (HQ/TDD/S3I) | AL |
| 94035 | Moffett Field / NASA Ames | CA |
| 23604 | JB Langley-Eustis (Aviation Dev) | VA |
| 78419 | Corpus Christi (Sustainment Eng) | TX |
| 80913 | Colorado Springs (S3I Software) | CO |
| 88002 | White Sands Missile Range | NM |
| 85365 | Yuma Proving Ground | AZ |
| 21005 | Aberdeen Proving Ground (DEVCOM HQ) | MD |
| 96857 | Wheeler Army Airfield | HI |
| 35898 | Redstone Test Center | AL |
| 32542 | Eglin AFB (Joint Test) | FL |
| 87117 | Kirtland AFB (Directed Energy) | NM |

**Decision**: Real zip codes as LabCode values for geocoding. 12 labs across the US. Redstone Arsenal dominates activity volume (weight 2.80) as AvMC headquarters.

### Directorates (replacing Manufacturers)

| DirectorateID | Directorate Name | Role |
|--------------|-----------------|------|
| 7 | DEVCOM AvMC | "Us" — the protagonist organization |
| (others) | PEO Missiles & Space | Partner (replaces Fabrikam) |
| | SMDC | Partner (replaces Tailwind Traders) |
| | DEVCOM ARL | Partner (replaces Nod Publishers) |
| | Industry Partners | Partner (replaces Wide World Importers) |

### FMS Partner Nations (replacing international country files)

| Country File | FMS Context | Mapped Programs |
|-------------|-------------|----------------|
| Australia.csv | FLRAA, ITEP, IFPC partnerships | 1001, 1003, 2005 |
| Japan.csv | Hypersonics, THAAD, Patriot support | 2003, 2006, 2007 |
| SouthKorea.csv | FLRAA, IFPC, THAAD, Counter-UAS | 1001, 2005, 2006, 3002 |
| Germany.csv | IFPC, Patriot, ITEP | 2005, 2007, 1003 |
| Mexico.csv | MOSA Avionics, Aircrew Trainer | 1004, 1005 |
| Canada.csv | FLRAA, Directed Energy | 1001, 3001 |

**Decision**: Keep 6 country files. Replace Nigeria with SouthKorea. Each country gets a realistic subset of programs.

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
| Module 2 (Lab 1) | Connect to data, Power Query | Data source paths (`USEngineering/RDWorkload.csv`), column names in instructions, scenario text | Power Query concepts, M functions |
| Module 3 (Lab 2) | Data modeling, relationships | Table names (Program, Lab, Directorate, RDWorkload), field names, ZipCountry→LabCodeCountry, scenario narrative | Star schema concepts, relationship types |
| Module 4 (Lab 3) | DAX measures, hierarchies | Measure names (`LaborHours` not `Revenue`), `PY Labor Hours`, `% Growth`, hierarchy names (Program Hierarchy) | DAX syntax, time intelligence patterns |
| Module 5 (Lab 4) | Visualizations, formatting | Chart titles, labels, logo/background swap, theme application, slicer references | Chart types, formatting techniques |
| Lab 5+ | Power BI Service, sharing | Workspace names, app names if mentioned | Service concepts, RLS, subscriptions |
| Final | End-to-end dashboard | All visual labels, KPI titles, executive summary | Dashboard design principles |

**Decision**: Modules 2–3 require the heaviest edits (data references). Module 4–5 require asset swaps and label changes. All changes are cosmetic/narrative — no structural lab changes needed.

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

1. **Schema**: Exact column-count preservation; Option C naming (ProgramID, LabCode, ResearchTasks, LaborHours)
2. **Programs**: 14 DEVCOM AvMC R&D programs across 4 categories (FVL, LRPF, AMD, Emerging Tech)
3. **Labs**: 12 real facilities using actual zip codes for geocoding
4. **Directorates**: DEVCOM AvMC + 4 partner organizations
5. **FMS nations**: Same 6 countries (Nigeria→SouthKorea), reframed as international programs
6. **Colors**: 15-color Army-brand palette led by Gold and Green
7. **Lab impact**: Cosmetic/narrative changes only; lab sequence untouched
8. **Assets**: 3 files to replace (logo, background, theme JSON)
9. **Learn content**: Module-by-module rework of dashboard-in-a-day.md preserving structure
