#!/usr/bin/env python3
from __future__ import annotations

import csv
import random
from datetime import date
from pathlib import Path

from faker import Faker


ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "Instructor" / "Data"
US_DATA_PATH = DATA_DIR / "USEngineering" / "RDWorkload.csv"
INTERNATIONAL_DIR = DATA_DIR / "InternationalPrograms"

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

PROGRAMS = [
    {"id": 1001, "name": "FLRAA (V-280 Valor)", "category": "Future Vertical Lift", "weight": 1.75, "tasks": (5, 35), "hours": 96.0},
    {"id": 1002, "name": "FARA", "category": "Future Vertical Lift", "weight": 1.35, "tasks": (4, 28), "hours": 88.0},
    {"id": 1003, "name": "ITEP (T901 Engine)", "category": "Future Vertical Lift", "weight": 1.20, "tasks": (3, 24), "hours": 102.0},
    {"id": 1004, "name": "MOSA Avionics", "category": "Future Vertical Lift", "weight": 0.78, "tasks": (2, 18), "hours": 64.0},
    {"id": 1005, "name": "Black Hawk Aircrew Trainer", "category": "Modeling & Simulation", "weight": 0.66, "tasks": (2, 16), "hours": 52.0},
    {"id": 2001, "name": "PrSM (Precision Strike Missile)", "category": "Long Range Precision Fires", "weight": 1.05, "tasks": (2, 20), "hours": 71.0},
    {"id": 2002, "name": "HIMARS Modernization", "category": "Long Range Precision Fires", "weight": 0.92, "tasks": (2, 18), "hours": 57.0},
    {"id": 2003, "name": "Hypersonic Weapon Components", "category": "Long Range Precision Fires", "weight": 0.55, "tasks": (1, 10), "hours": 136.0},
    {"id": 2004, "name": "LRPF Next-Gen Propulsion", "category": "Long Range Precision Fires", "weight": 0.42, "tasks": (1, 9), "hours": 118.0},
    {"id": 2005, "name": "IFPC (Indirect Fire Protection)", "category": "Air & Missile Defense", "weight": 0.96, "tasks": (2, 16), "hours": 76.0},
    {"id": 2006, "name": "THAAD Modernization", "category": "Air & Missile Defense", "weight": 0.88, "tasks": (1, 14), "hours": 43.0},
    {"id": 2007, "name": "Patriot Next-Gen Radar", "category": "Air & Missile Defense", "weight": 0.46, "tasks": (1, 10), "hours": 31.0},
    {"id": 3001, "name": "Directed Energy Weapons", "category": "Emerging Technology", "weight": 0.38, "tasks": (1, 12), "hours": 67.0},
    {"id": 3002, "name": "Counter-UAS Systems", "category": "Emerging Technology", "weight": 0.34, "tasks": (1, 11), "hours": 39.0},
]

LABS = [
    {"code": 35808, "name": "Redstone Arsenal (HQ/TDD/S3I)", "weight": 2.80},
    {"code": 94035, "name": "Moffett Field / NASA Ames", "weight": 1.45},
    {"code": 23604, "name": "JB Langley-Eustis (Aviation Dev)", "weight": 1.30},
    {"code": 78419, "name": "Corpus Christi (Sustainment Eng)", "weight": 1.10},
    {"code": 80913, "name": "Colorado Springs (S3I Software)", "weight": 0.92},
    {"code": 88002, "name": "White Sands Missile Range", "weight": 1.05},
    {"code": 85365, "name": "Yuma Proving Ground", "weight": 0.86},
    {"code": 21005, "name": "Aberdeen Proving Ground (DEVCOM HQ)", "weight": 0.74},
    {"code": 96857, "name": "Wheeler Army Airfield", "weight": 0.48},
    {"code": 35898, "name": "Redstone Test Center", "weight": 0.72},
    {"code": 32542, "name": "Eglin AFB (Joint Test)", "weight": 0.56},
    {"code": 87117, "name": "Kirtland AFB (Directed Energy)", "weight": 0.38},
]

FMS_CONFIG = {
    "Australia": {"program_ids": [1001, 1003, 2005], "facility_codes": [2600, 4700, 5000, 8107], "growth": 0.04},
    "Japan": {"program_ids": [2003, 2006, 2007], "facility_codes": [100, 197, 904, 901], "growth": 0.035},
    "SouthKorea": {"program_ids": [1001, 2005, 2006, 3002], "facility_codes": [412, 140, 406, 503], "growth": 0.09},
    "Germany": {"program_ids": [2005, 2007, 1003], "facility_codes": [67657, 91522, 92655, 53123], "growth": 0.025},
    "Mexico": {"program_ids": [1004, 1005], "facility_codes": [11520, 76220, 45659, 66600], "growth": 0.02},
    "Canada": {"program_ids": [1001, 3001], "facility_codes": [8050, 3155, 3590, 107], "growth": 0.018},
}

PROGRAM_BY_ID = {program["id"]: program for program in PROGRAMS}
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


def correlated_tasks_and_hours(program: dict[str, object], international: bool = False) -> tuple[int, str]:
    min_tasks, max_tasks = program["tasks"]
    task_ceiling = min(int(max_tasks), 20 if international else 50)
    tasks = random.triangular(int(min_tasks), task_ceiling, int(min_tasks) + (task_ceiling - int(min_tasks)) * 0.42)
    task_count = max(1, int(round(tasks)))

    mean_hours = float(program["hours"])
    noise = random.uniform(0.82, 1.22)
    complexity = random.choice([0.88, 0.95, 1.00, 1.07, 1.18])
    labor_hours = task_count * mean_hours * noise * complexity
    lower_bound = 25.0 if international else 50.0
    upper_bound = 3000.0 if international else 5000.0
    labor_hours = min(max(labor_hours, lower_bound), upper_bound)
    return task_count, f"{labor_hours:.6f}"


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
        program = weighted_choice(PROGRAMS, "weight")
        lab = weighted_choice(LABS, "weight")
        research_tasks, labor_hours = correlated_tasks_and_hours(program)
        yield [
            program["id"],
            random_activity_date().isoformat(),
            lab["code"],
            research_tasks,
            labor_hours,
        ]


def generate_international_rows(country: str):
    config = FMS_CONFIG[country]
    program_subset = [PROGRAM_BY_ID[program_id] for program_id in config["program_ids"]]
    for _ in range(INTERNATIONAL_ROW_COUNTS[country]):
        program = weighted_choice(program_subset, "weight")
        research_tasks, labor_hours = correlated_tasks_and_hours(program, international=True)
        yield [
            program["id"],
            random_activity_date(country).isoformat(),
            random.choice(config["facility_codes"]),
            research_tasks,
            labor_hours,
            "South Korea" if country == "SouthKorea" else country,
        ]


def generate_us_sales() -> int:
    return write_csv(
        US_DATA_PATH,
        ["ProgramID", "Date", "LabCode", "ResearchTasks", "LaborHours"],
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
            ["ProgramID", "Date", "LabCode", "ResearchTasks", "LaborHours", "Country"],
            generate_international_rows(country),
        )
    return row_counts


def main() -> None:
    random.seed(RANDOM_SEED)
    Faker.seed(RANDOM_SEED)
    Faker()

    print("Generating DEVCOM AvMC synthetic CSV data...")
    us_count = generate_us_sales()
    print(f"USEngineering/RDWorkload.csv: {us_count:,} rows")

    international_counts = generate_international_sales()
    for country, row_count in international_counts.items():
        print(f"InternationalPrograms/{country}.csv: {row_count:,} rows")


if __name__ == "__main__":
    main()
