#!/usr/bin/env python3
from __future__ import annotations

import csv
import random
from datetime import date
from pathlib import Path

from faker import Faker


ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "Instructor" / "Data"
US_SALES_PATH = DATA_DIR / "USSales" / "Sales.csv"
INTERNATIONAL_DIR = DATA_DIR / "InternationalSales"

START_DATE = date(2021, 1, 1)
END_DATE = date(2025, 12, 31)
RANDOM_SEED = 20260426

US_ROW_COUNT = 4_200_000
INTERNATIONAL_ROW_COUNTS = {
    "Australia": 1_992_000,
    "Japan": 527_000,
    "SouthKorea": 205_000,
    "Germany": 138_000,
    "Mexico": 129_000,
    "Canada": 46_000,
}

PLATFORMS = [
    {"id": 1001, "name": "AH-64 Apache", "category": "Helicopter", "weight": 1.35, "orders": (4, 28), "hours": 88.0},
    {"id": 1002, "name": "UH-60 Black Hawk", "category": "Helicopter", "weight": 1.75, "orders": (5, 35), "hours": 76.0},
    {"id": 1003, "name": "CH-47 Chinook", "category": "Helicopter", "weight": 1.20, "orders": (3, 24), "hours": 102.0},
    {"id": 1004, "name": "UH-72 Lakota", "category": "Helicopter", "weight": 0.78, "orders": (2, 18), "hours": 52.0},
    {"id": 1005, "name": "AH-6 Little Bird", "category": "Helicopter", "weight": 0.38, "orders": (1, 12), "hours": 64.0},
    {"id": 2001, "name": "GMLRS", "category": "Rocket/Missile", "weight": 1.05, "orders": (2, 20), "hours": 43.0},
    {"id": 2002, "name": "HIMARS", "category": "Rocket/Missile Launcher", "weight": 0.92, "orders": (2, 18), "hours": 57.0},
    {"id": 2003, "name": "THAAD", "category": "Missile Defense", "weight": 0.55, "orders": (1, 10), "hours": 136.0},
    {"id": 2004, "name": "Patriot", "category": "Air/Missile Defense", "weight": 0.96, "orders": (2, 16), "hours": 118.0},
    {"id": 2005, "name": "ATACMS", "category": "Tactical Ballistic Missile", "weight": 0.42, "orders": (1, 9), "hours": 71.0},
    {"id": 2006, "name": "Javelin", "category": "Anti-Tank Missile", "weight": 0.88, "orders": (1, 14), "hours": 31.0},
    {"id": 2007, "name": "Stinger", "category": "MANPADS", "weight": 0.46, "orders": (1, 10), "hours": 28.0},
    {"id": 3001, "name": "MQ-1C Gray Eagle", "category": "UAS", "weight": 0.66, "orders": (2, 16), "hours": 67.0},
    {"id": 3002, "name": "RQ-7 Shadow", "category": "UAS", "weight": 0.34, "orders": (1, 11), "hours": 39.0},
]

INSTALLATIONS = [
    {"code": 35808, "name": "Redstone Arsenal", "weight": 2.35},
    {"code": 78419, "name": "Corpus Christi Army Depot", "weight": 1.85},
    {"code": 17201, "name": "Letterkenny Army Depot", "weight": 1.25},
    {"code": 36362, "name": "Fort Novosel", "weight": 1.10},
    {"code": 96859, "name": "Wheeler Army Airfield", "weight": 0.74},
    {"code": 98433, "name": "Joint Base Lewis-McChord", "weight": 0.90},
    {"code": 31314, "name": "Fort Stewart / Hunter AAF", "weight": 0.86},
    {"code": 42223, "name": "Fort Campbell", "weight": 0.98},
    {"code": 79916, "name": "Fort Bliss", "weight": 0.72},
    {"code": 10996, "name": "West Point", "weight": 0.12},
    {"code": 28307, "name": "Fort Liberty", "weight": 0.82},
    {"code": 80913, "name": "Fort Carson", "weight": 0.64},
]

FMS_CONFIG = {
    "Australia": {"platform_ids": [1001, 1003, 2006], "facility_codes": [2600, 4700, 5000, 8107], "growth": 0.04},
    "Japan": {"platform_ids": [1001, 2003, 2004], "facility_codes": [100, 197, 904, 901], "growth": 0.035},
    "SouthKorea": {"platform_ids": [1001, 1002, 2004, 2006], "facility_codes": [412, 140, 406, 503], "growth": 0.09},
    "Germany": {"platform_ids": [1003, 2004, 2007], "facility_codes": [67657, 91522, 92655, 53123], "growth": 0.025},
    "Mexico": {"platform_ids": [1002, 1004], "facility_codes": [11520, 76220, 45659, 66600], "growth": 0.02},
    "Canada": {"platform_ids": [1003, 3001], "facility_codes": [8050, 3155, 3590, 107], "growth": 0.018},
}

PLATFORM_BY_ID = {platform["id"]: platform for platform in PLATFORMS}
CSV_DIALECT = "excel"
CSV_LINE_TERMINATOR = "\r\n"


def weighted_choice(items: list[dict[str, object]], weight_key: str) -> dict[str, object]:
    return random.choices(items, weights=[float(item[weight_key]) for item in items], k=1)[0]


def random_activity_date(country: str | None = None) -> date:
    year_weights = []
    for year in range(START_DATE.year, END_DATE.year + 1):
        years_since_start = year - START_DATE.year
        if country == "SouthKorea":
            year_weights.append(1.0 + (0.22 * years_since_start))
        elif country:
            year_weights.append(1.0 + (FMS_CONFIG[country]["growth"] * years_since_start))
        else:
            year_weights.append(1.0 + (0.04 * years_since_start))

    selected_year = random.choices(range(START_DATE.year, END_DATE.year + 1), weights=year_weights, k=1)[0]
    quarter_months = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (10, 11, 12),
    ]
    selected_quarter = random.choices(quarter_months, weights=[1.18, 0.92, 1.14, 0.96], k=1)[0]
    selected_month = random.choice(selected_quarter)
    selected_day = random.randint(1, 28)
    return date(selected_year, selected_month, selected_day)


def correlated_work_and_hours(platform: dict[str, object], international: bool = False) -> tuple[int, str]:
    min_orders, max_orders = platform["orders"]
    order_ceiling = min(int(max_orders), 20 if international else 50)
    work_orders = random.triangular(int(min_orders), order_ceiling, int(min_orders) + (order_ceiling - int(min_orders)) * 0.42)
    work_order_count = max(1, int(round(work_orders)))

    mean_hours = float(platform["hours"])
    noise = random.uniform(0.82, 1.22)
    complexity = random.choice([0.88, 0.95, 1.00, 1.07, 1.18])
    engineering_hours = work_order_count * mean_hours * noise * complexity
    lower_bound = 25.0 if international else 50.0
    upper_bound = 3000.0 if international else 5000.0
    engineering_hours = min(max(engineering_hours, lower_bound), upper_bound)
    return work_order_count, f"{engineering_hours:.6f}"


def write_csv(path: Path, header: list[str], rows) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.writer(output_file, dialect=CSV_DIALECT, lineterminator=CSV_LINE_TERMINATOR)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)
            count += 1
    return count


def generate_us_rows():
    for _ in range(US_ROW_COUNT):
        platform = weighted_choice(PLATFORMS, "weight")
        installation = weighted_choice(INSTALLATIONS, "weight")
        work_orders, engineering_hours = correlated_work_and_hours(platform)
        yield [
            platform["id"],
            random_activity_date().isoformat(),
            installation["code"],
            work_orders,
            engineering_hours,
        ]


def generate_international_rows(country: str):
    config = FMS_CONFIG[country]
    platform_subset = [PLATFORM_BY_ID[platform_id] for platform_id in config["platform_ids"]]
    for _ in range(INTERNATIONAL_ROW_COUNTS[country]):
        platform = weighted_choice(platform_subset, "weight")
        work_orders, engineering_hours = correlated_work_and_hours(platform, international=True)
        yield [
            platform["id"],
            random_activity_date(country).isoformat(),
            random.choice(config["facility_codes"]),
            work_orders,
            engineering_hours,
            "South Korea" if country == "SouthKorea" else country,
        ]


def generate_us_sales() -> int:
    return write_csv(
        US_SALES_PATH,
        ["PlatformID", "Date", "InstallationCode", "WorkOrders", "EngineeringHours"],
        generate_us_rows(),
    )


def generate_international_sales() -> dict[str, int]:
    row_counts = {}
    old_nigeria_path = INTERNATIONAL_DIR / "Nigeria.csv"
    if old_nigeria_path.exists():
        old_nigeria_path.unlink()
    for country in INTERNATIONAL_ROW_COUNTS:
        row_counts[country] = write_csv(
            INTERNATIONAL_DIR / f"{country}.csv",
            ["PlatformID", "Date", "InstallationCode", "WorkOrders", "EngineeringHours", "Country"],
            generate_international_rows(country),
        )
    return row_counts


def main() -> None:
    random.seed(RANDOM_SEED)
    Faker.seed(RANDOM_SEED)
    Faker()

    print("Generating DEVCOM AvMC synthetic CSV data...")
    us_count = generate_us_sales()
    print(f"USSales/Sales.csv: {us_count:,} rows")

    international_counts = generate_international_sales()
    for country, row_count in international_counts.items():
        print(f"InternationalSales/{country}.csv: {row_count:,} rows")


if __name__ == "__main__":
    main()
