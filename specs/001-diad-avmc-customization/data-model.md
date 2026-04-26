# Data Model: DIAD AvMC Customization

**Phase 1 Output** | **Date**: 2026-04-26

## Entities

### Platform (dimension)
Replaces the original DIAD "Product" concept.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| PlatformID | Integer | Primary key; unique identifier | 1001 |
| PlatformName | String | Display name of weapon system | AH-64 Apache |
| Category | String | Grouping: Helicopter, Rocket/Missile, UAS | Helicopter |
| Manufacturer | String | Prime contractor | Boeing |
| ServiceBranch | String | Primary using branch | Army |

**Relationships**: `PlatformID` → `USSustainment.PlatformID`, `FMSSupport.PlatformID`

### Installation (dimension)
Replaces zip-code-only geography in original DIAD.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| InstallationCode | Integer | Zip code of installation (acts as PK) | 35808 |
| InstallationName | String | Human-readable name | Redstone Arsenal |
| State | String | Two-letter state code | AL |
| Command | String | Parent command (AMCOM, DEVCOM, FORSCOM) | AMCOM |

**Relationships**: `InstallationCode` → `USSustainment.InstallationCode`

### USSustainment (fact — replaces USSales/Sales.csv)
Core transactional table for domestic platform sustainment work.

| Field | Type | Description | Range |
|-------|------|-------------|-------|
| PlatformID | Integer | FK to Platform | 1001–3002 |
| Date | Date | Work order date | 2021-01-01 to 2025-12-31 |
| InstallationCode | Integer | Zip code of installation | See Installation table |
| WorkOrders | Integer | Number of work orders | 1–50 |
| EngineeringHours | Decimal | Total engineering hours | 50.00–5000.00 |

**Row count target**: ~4.2M rows (matches original Sales.csv)

### FMSSupport (fact — replaces InternationalSales/*.csv)
Allied nation Foreign Military Sales support data.

| Field | Type | Description | Range |
|-------|------|-------------|-------|
| PlatformID | Integer | FK to Platform | 1001–3002 |
| Date | Date | Support activity date | 2021-01-01 to 2025-12-31 |
| InstallationCode | Integer | Partner nation facility code | Varies by country |
| WorkOrders | Integer | Number of support events | 1–20 |
| EngineeringHours | Decimal | Total support hours | 25.00–3000.00 |
| Country | String | Partner nation name | Australia, Canada, etc. |

**Row count targets**: ~3M total across 6 files

## Star Schema

```
                    ┌──────────────┐
                    │   Platform   │
                    │  (dimension) │
                    └──────┬───────┘
                           │ PlatformID
              ┌────────────┼────────────┐
              │            │            │
     ┌────────▼───────┐   │   ┌────────▼───────┐
     │ USSustainment  │   │   │  FMSSupport    │
     │    (fact)      │   │   │    (fact)      │
     └────────┬───────┘   │   └────────────────┘
              │            │
              │ InstallationCode
              │
     ┌────────▼───────┐
     │  Installation  │
     │  (dimension)   │
     └────────────────┘
```

This mirrors the original DIAD model where Products relate to both US and International Sales via ProductID, and geography is resolved via Zip.

## Validation Rules

- `PlatformID` must exist in Platform table (referential integrity)
- `Date` must be a valid date in YYYY-MM-DD format
- `WorkOrders` must be a positive integer ≥ 1
- `EngineeringHours` must be a positive decimal ≥ 0
- `Country` must be one of: Australia, Canada, Germany, Japan, Mexico, South Korea
- `InstallationCode` for US data must be a valid 5-digit zip code

## Date Range Decision

**Original DIAD**: 2015 data
**AvMC version**: 2021–2025 (5-year range)

Rationale: More recent dates feel current for the audience. 5 years supports all time-intelligence DAX patterns taught in the labs (YoY, QoQ, MTD, YTD).
