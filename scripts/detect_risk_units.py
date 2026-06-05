"""
detect_risk_units.py

목적:
KPI 기준(62%)을 초과하는 위험 UNIT 탐지.
"""

KPI_THRESHOLD = 0.62


def detect_risk_units(summary_rows: list[dict]) -> list[dict]:
    """KPI 초과 UNIT 탐지"""

    risk_rows = []

    for row in summary_rows:
        if row["labor_ratio"] > KPI_THRESHOLD:
            risk_rows.append(row)

    risk_rows.sort(
        key=lambda x: x["labor_ratio"],
        reverse=True,
    )

    return risk_rows


if __name__ == "__main__":
    print("detect_risk_units.py 실행 테스트")
