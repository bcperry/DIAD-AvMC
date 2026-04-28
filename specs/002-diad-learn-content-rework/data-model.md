# Data Model: DIAD AvMC Customization

**Phase 1 Output** | **Date**: 2026-04-26 | **Updated**: 2026-04-26

**Theme**: *R&D Engineering Workload (TDD + S3I focus)* — Track research and development engineering effort across AvMC's technology portfolio.

## Entities

### Program (dimension — replaces Product)
R&D programs aligned to the Army's six modernization priorities.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| ProgramID | Integer | Primary key; unique identifier | 1001 |
| Program | String | Display name of R&D program | FLRAA (V-280 Valor) |
| Category | String | Modernization grouping | Future Vertical Lift |
| DirectorateID | Integer | FK to Directorate dimension | 7 |

**Categories**: Future Vertical Lift, Long Range Precision Fires, Air & Missile Defense, Modeling & Simulation, Emerging Technology

**Relationships**: `ProgramID` → `RDWorkload.ProgramID`, `InternationalPrograms.ProgramID`

**bi_dimensions.xlsx format**: Category and Program are stored pipe-delimited (`Category|Program`) in the Product sheet, matching the original DIAD split-by-delimiter exercise.

### Lab (dimension — replaces Geography)
AvMC test and research facility locations using real zip codes for Power BI geocoding.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| LabCode | Integer | Zip code of facility (acts as PK) | 35808 |
| Lab | String | Human-readable facility name | Redstone Arsenal (HQ/TDD/S3I) |
| State | String | Two-letter state code | AL |
| Country | String | Country (for LabCodeCountry join) | USA |

**Relationships**: `LabCode` → `RDWorkload.LabCode` (via `LabCodeCountry` composite key, same pattern as original `ZipCountry`)

### Directorate (dimension — replaces Manufacturer)
Army organizations involved in R&D engineering work.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| DirectorateID | Integer | Primary key | 7 |
| Directorate | String | Organization name | DEVCOM AvMC |
| Logo | String | URL to organization logo image | (Image URL) |

**Key mapping**: DirectorateID 7 = DEVCOM AvMC (the "us" organization, replacing VanArsdel)

### RDWorkload (fact — replaces Sales / USSales/Sales.csv)
Domestic R&D engineering workload data. Core transactional table.

| Field | Type | Description | Range |
|-------|------|-------------|-------|
| ProgramID | Integer | FK to Program | 1001–3002 |
| Date | Date | Activity date | 2021-01-01 to 2025-12-31 |
| LabCode | Integer | Zip code of lab facility | See Lab table |
| ResearchTasks | Integer | Discrete R&D tasks (prototype builds, test events) | 1–35 |
| LaborHours | Decimal | Engineering labor hours per task period | 25.00–5000.00 (6 decimal places) |

**Row count target**: ~4,200,000 rows (matches original Sales.csv)
**File**: `USEngineering/RDWorkload.csv`
**Header**: `ProgramID,Date,LabCode,ResearchTasks,LaborHours`

### InternationalPrograms (fact — replaces InternationalSales/*.csv)
Allied nation R&D collaboration data (Five Eyes, NATO partners).

| Field | Type | Description | Range |
|-------|------|-------------|-------|
| ProgramID | Integer | FK to Program | Subset per country |
| Date | Date | Activity date | 2021-01-01 to 2025-12-31 |
| LabCode | Integer | Partner nation facility code | Varies by country |
| ResearchTasks | Integer | Discrete R&D tasks | 1–20 |
| LaborHours | Decimal | Engineering labor hours | 25.00–3000.00 (6 decimal places) |
| Country | String | Partner nation name | Australia, Canada, etc. |

**Row count targets**: ~3M total across 6 files
**Folder**: `InternationalPrograms/`
**Header**: `ProgramID,Date,LabCode,ResearchTasks,LaborHours,Country`

| File | Target Rows |
|------|-------------|
| Australia.csv | ~1,992,000 |
| Japan.csv | ~527,000 |
| SouthKorea.csv | ~205,000 |
| Germany.csv | ~138,000 |
| Mexico.csv | ~129,000 |
| Canada.csv | ~46,000 |

## Star Schema

```
                  ┌──────────────────┐
                  │    Directorate   │
                  │   (dimension)    │
                  └────────┬─────────┘
                           │ DirectorateID
                  ┌────────▼─────────┐
                  │     Program      │
                  │   (dimension)    │
                  └────────┬─────────┘
                           │ ProgramID
              ┌────────────┼─────────────────┐
              │            │                 │
     ┌────────▼────────┐   │   ┌─────────────▼──────────┐
     │   RDWorkload    │   │   │  InternationalPrograms  │
     │     (fact)      │   │   │         (fact)          │
     └────────┬────────┘   │   └─────────────────────────┘
              │            │
              │ LabCodeCountry (composite key)
              │
     ┌────────▼────────┐
     │      Lab        │
     │   (dimension)   │
     └─────────────────┘
```

This mirrors the original DIAD star schema:
- Program↔Directorate via DirectorateID (same as Product↔Manufacturer via ManufacturerID)
- RDWorkload↔Program via ProgramID (same as Sales↔Product via ProductID)
- RDWorkload↔Lab via LabCodeCountry composite key (same as Sales↔Geography via ZipCountry)
- InternationalPrograms appended into RDWorkload during Power Query (same as International Sales→Sales append)

## Calculated Columns & Measures

| Name | Type | DAX Pattern | Original |
|------|------|-------------|----------|
| LabCodeCountry | Calculated column | `RDWorkload[LabCode] & "," & RDWorkload[Country]` | ZipCountry |
| PY Labor Hours | Measure | `CALCULATE(SUM(RDWorkload[LaborHours]), SAMEPERIODLASTYEAR('Date'[Date]))` | PY Sales |
| % Growth | Measure | `DIVIDE(SUM(RDWorkload[LaborHours])-[PY Labor Hours],[PY Labor Hours])` | % Growth |
| Total Labor Hours | Measure | `SUM(RDWorkload[LaborHours])` | Sales |
| DEVCOM AvMC Labor Hours | Measure | Filtered to DirectorateID=7 | VanArsdel Sales |
| Effort Share | Measure | Division of AvMC hours by total | Market Share |

## Validation Rules

- `ProgramID` must exist in Program table (referential integrity)
- `Date` must be a valid date in YYYY-MM-DD format
- `ResearchTasks` must be a positive integer ≥ 1
- `LaborHours` must be a positive decimal > 0 with 6 decimal places
- `Country` must be one of: Australia, Canada, Germany, Japan, Mexico, South Korea
- `LabCode` for US data must be a valid 5-digit zip code from the Lab table

## Date Range Decision

**Original DIAD**: 2014–2021 data (7 years)
**AvMC version**: 2021–2025 (5 years)

Rationale: More recent dates feel current for the AvMC audience. 5 years supports all time-intelligence DAX patterns taught in the labs (YoY, QoQ, MTD, YTD). The DAX Date table uses `CALENDAR(DATE(2020,1,1), DATE(2026,12,31))` to provide padding around the data range.

## Design Notes

**Why Option C (R&D Workload)?** Captures the technology development side of AvMC's mission. Maps naturally to the Army's six modernization priorities. The TDD (Technology Development Directorate) and S3I (Software, Simulation, Systems Engineering & Integration) directorates at Redstone Arsenal are the primary audience.

**Addressed downside — lab count**: The original concern about "only ~6 lab locations" weakening map visualizations was addressed by expanding to 12 labs across the US (AL, CA, VA, TX, CO, NM, AZ, MD, HI, FL).
