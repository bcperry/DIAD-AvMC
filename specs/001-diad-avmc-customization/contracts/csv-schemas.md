# CSV Schema Contracts

**Phase 1 Output** | **Date**: 2026-04-26

These contracts define the exact CSV file formats that the synthetic data
generator MUST produce. Power BI .pbix solution files depend on these schemas.

---

## Contract 1: `USSales/Sales.csv`

**Purpose**: Domestic platform sustainment data (replaces VanArsdel US sales)

| Column | Position | Type | Format | Nullable | Example |
|--------|----------|------|--------|----------|---------|
| PlatformID | 1 | Integer | Plain | No | 1001 |
| Date | 2 | Date | YYYY-MM-DD | No | 2023-06-15 |
| InstallationCode | 3 | Integer | 5-digit zip | No | 35808 |
| WorkOrders | 4 | Integer | Plain | No | 3 |
| EngineeringHours | 5 | Decimal | 6 decimal places | No | 254.572500 |

**Header row**: `PlatformID,Date,InstallationCode,WorkOrders,EngineeringHours`
**Encoding**: UTF-8
**Line ending**: CRLF (Windows)
**Target rows**: ~4,200,000
**Delimiter**: Comma

### Mapping to Original
| Original Column | New Column | Notes |
|----------------|------------|-------|
| ProductID | PlatformID | Same type, different semantic |
| Date | Date | Identical |
| Zip | InstallationCode | Same type (integer); uses real zip codes |
| Units | WorkOrders | Same type (integer count) |
| Revenue | EngineeringHours | Same type (decimal); same precision |

---

## Contract 2: `InternationalSales/{Country}.csv`

**Purpose**: FMS partner nation support data (replaces VanArsdel international sales)
**Files**: Australia.csv, Canada.csv, Germany.csv, Japan.csv, Mexico.csv, SouthKorea.csv

| Column | Position | Type | Format | Nullable | Example |
|--------|----------|------|--------|----------|---------|
| PlatformID | 1 | Integer | Plain | No | 2003 |
| Date | 2 | Date | YYYY-MM-DD | No | 2024-03-01 |
| InstallationCode | 3 | Integer | Varies by country | No | 6837 |
| WorkOrders | 4 | Integer | Plain | No | 1 |
| EngineeringHours | 5 | Decimal | 6 decimal places | No | 403.987500 |
| Country | 6 | String | Full name | No | Australia |

**Header row**: `PlatformID,Date,InstallationCode,WorkOrders,EngineeringHours,Country`
**Encoding**: UTF-8
**Line ending**: CRLF (Windows)
**Delimiter**: Comma

### Target Row Counts per File
| File | Target Rows | Notes |
|------|-------------|-------|
| Australia.csv | ~1,992,000 | Largest FMS partner file |
| Japan.csv | ~527,000 | |
| SouthKorea.csv | ~205,000 | |
| Germany.csv | ~138,000 | |
| Mexico.csv | ~129,000 | |
| Canada.csv | ~46,000 | Smallest FMS partner file |

### Mapping to Original
| Original Column | New Column | Notes |
|----------------|------------|-------|
| ProductID | PlatformID | Same type, different semantic |
| Date | Date | Identical |
| Zip | InstallationCode | Same type |
| Units | WorkOrders | Same type |
| Revenue | EngineeringHours | Same type, same precision |
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

**Note**: `VanArsdel_Logo.png` will be replaced by `AvMC_Logo.png`. The filename in .pbix data source references will need updating in each solution file.
