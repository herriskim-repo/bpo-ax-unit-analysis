"""
detect_risk_units.py

목적:
KPI 기준(62%)을 초과하는 위험 UNIT 탐지.
"""

import pandas as pd


KPI_THRESHOLD = 0.62


def detect_risk_units(summary_df: pd.DataFrame) -> pd.DataFrame:
    """
    KPI 초과 UNIT 탐지
    """

    risk_df = summary_df[
        summary_df["labor_ratio"] > KPI_THRESHOLD
    ].copy()

    risk_df = risk_df.sort_values(
        by="labor_ratio",
        ascending=False
    )

    return risk_df


if __name__ == "__main__":
    print("detect_risk_units.py 실행 테스트")
