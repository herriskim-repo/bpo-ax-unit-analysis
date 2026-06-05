"""
calculate_kpi.py

목적:
UNIT별 인건비율(KPI)을 계산한다.

KPI 정의:
labor_cost_ratio = labor_cost / revenue

목표 KPI:
62% 이하
"""

from collections import defaultdict


KPI_THRESHOLD = 0.62


def calculate_labor_ratio(rows: list[dict]) -> list[dict]:
    """각 row에 labor_ratio 계산 결과를 추가한다."""

    for row in rows:
        revenue = row.get("revenue", 0)
        labor_cost = row.get("labor_cost", 0)

        if revenue == 0:
            labor_ratio = 0
        else:
            labor_ratio = labor_cost / revenue

        row["labor_ratio"] = labor_ratio

    return rows


def summarize_by_unit(rows: list[dict]) -> list[dict]:
    """UNIT별 KPI 요약"""

    grouped = defaultdict(lambda: {
        "division": "",
        "unit": "",
        "revenue": 0,
        "labor_cost": 0,
    })

    for row in rows:
        key = (row["division"], row["unit"])

        grouped[key]["division"] = row["division"]
        grouped[key]["unit"] = row["unit"]
        grouped[key]["revenue"] += row["revenue"]
        grouped[key]["labor_cost"] += row["labor_cost"]

    summary_rows = []

    for value in grouped.values():
        revenue = value["revenue"]
        labor_cost = value["labor_cost"]

        if revenue == 0:
            labor_ratio = 0
        else:
            labor_ratio = labor_cost / revenue

        summary_rows.append({
            "division": value["division"],
            "unit": value["unit"],
            "revenue": revenue,
            "labor_cost": labor_cost,
            "labor_ratio": labor_ratio,
            "status": "RISK" if labor_ratio > KPI_THRESHOLD else "NORMAL",
        })

    return summary_rows


if __name__ == "__main__":
    print("calculate_kpi.py 실행 테스트")
