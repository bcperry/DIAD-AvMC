# CSV Schema Contracts

**Phase 1 Output** | **Date**: 2026-04-26 | **Updated**: 2026-04-26

These contracts define the exact CSV file formats that the synthetic data
generator MUST produce. Power BI .pbix solution files depend on these schemas.

---

## Contract 1: `USEngineering/RDWorkload.csv`

**Purpose**: Domestic R&D engineering workload data (replaces VanArsdel US sales)

| Column | Position | Type | Format | Nullable | Example |
|--------|----------|------|--------|----------|---------|
| ProgramID | 1 | Integer | Plain | No | 1001 |
| Date | 2 | Date | YYYY-MM-DD | No | 2023-06-15 |
| LabCode | 3 | Integer | 5-digit zip | No | 35808 |
| ResearchTasks | 4 | Integer | Plain | No | 13 |
| LaborHours | 5 | Decimal | 6 decimal places | No | 1455.820813 |

**Header row**: `ProgramID,Date,LabCode,ResearchTasks,LaborHours`
**Encoding**: UTF-8
**Line ending**: CRLF (Windows)
**Target rows**: ~4,200,000
**Delimiter**: Comma

### Mapping to Original
| Original Column | New Column | Notes |
|----------------|------------|-------|
| ProductID | ProgramID | Same type; FK to R&D program |
| Date | Date | Identical |
| Zip | LabCode | Same type (integer); uses real zip codes for geocoding |
| Units | ResearchTasks | Same type (integer count); discrete R&D tasks |
| Revenue | LaborHours | Same type (decimal); engineering labor hours |

---

## Contract 2: `InternationalPrograms/{Country}.csv`

**Purpose**: Allied nation R&D collaboration data (replaces VanArsdel international sales)
**Files**: Australia.csv, Canada.csv, Germany.csv, Japan.csv, Mexico.csv, SouthKorea.csv

| Column | Position | Type | Format | Nullable | Example |
|--------|----------|------|--------|----------|---------|
| ProgramID | 1 | Integer | Plain | No | 2003 |
| Date | 2 | Date | YYYY-MM-DD | No | 2024-03-01 |
| LabCode | 3 | Integer | Varies by country | No | 2600 |
| ResearchTasks | 4 | Integer | Plain | No | 6 |
| LaborHours | 5 | Decimal | 6 decimal places | No | 783.335831 |
| Country | 6 | String | Full name | No | Australia |

**Header row**: `ProgramID,Date,LabCode,ResearchTasks,LaborHours,Country`
**Encoding**: UTF-8
**Line ending**: CRLF (Windows)
**Delimiter**: Comma

### Target Row Counts per File
| File | Target Rows | Notes |
|------|-------------|-------|
| Australia.csv | ~1,992,000 | Largest partner; FLRAA, ITEP, IFPC |
| Japan.csv | ~527,000 | Hypersonics, THAAD, Patriot |
| SouthKorea.csv | ~205,000 | FLRAA, IFPC, THAAD, Counter-UAS |
| Germany.csv | ~138,000 | IFPC, Patriot, ITEP |
| Mexico.csv | ~129,000 | MOSA Avionics, Aircrew Trainer |
| Canada.csv | ~46,000 | FLRAA, Directed Energy |

### Mapping to Original
| Original Column | New Column | Notes |
|----------------|------------|-------|
| ProductID | ProgramID | Same type; FK to R&D program |
| Date | Date | Identical |
| Zip | LabCode | Same type; partner facility codes |
| Units | ResearchTasks | Same type; discrete R&D tasks |
| Revenue | LaborHours | Same type, same precision |
| Country | Country | Identical |

---

## Contract 3: `Theme/DIADTheme2.json`

**Purpose**: Power BI theme file defining the Army-branded color palette

```json
{
  "name": "DEVCOM AvMC Theme",
  "dataColors": [
    "#C1A875",
    "#4B5320",
    "#2D2926",
    "#6B7A8D",
    "#8B7340",
    "#708238",
    "#D2B48C",
    "#8B0000",
    "#4682B4",
    "#9E9E93",
    "#E8D5A3",
    "#3B4219",
    "#5F8A8B",
    "#BDB76B",
    "#3C3C3C"
  ]
}
```

---

## Contract 4: Image Assets

| Asset | Dimensions | Format | Purpose |
|-------|-----------|--------|---------|
| `AvMC_Logo.png` | ~979×122px | PNG (RGBA) | Report header logo |
| `Background.jpg` | 1280×720px | JPEG | Report background image |

**Note**: `VanArsdel_Logo.png` is replaced by `AvMC_Logo.png`. The filename in .pbix data source references is updated by `rebuild_powerbi_sources.py` during the extract/patch/compile pipeline.
