"""
calculate_kpi.py

목적:
UNIT별 인건비율(KPI)을 계산한다.

KPI 정의:
labor_cost_ratio = labor_cost / revenue

목표 KPI:
62% 이하
"""

import pandas as pd


def calculate_labor_ratio(df: pd.DataFrame) -> pd.DataFrame:
    """
    인건비율 계산
    """

    df["labor_ratio"] = df["labor_cost"] / df["revenue"]

    return df


def summarize_by_unit(df: pd.DataFrame) -> pd.DataFrame:
    """
    UNIT별 KPI 요약
    """

    summary = (
        df.groupby(["division", "unit"])
        .agg(
            revenue=("revenue", "sum"),
            labor_cost=("labor_cost", "sum"),
            labor_ratio=("labor_ratio", "mean")
        )
        .reset_index()
    )

    return summary


if __name__ == "__main__":
    print("calculate_kpi.py 실행 테스트")
