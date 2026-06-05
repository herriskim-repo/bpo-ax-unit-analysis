"""
load_data.py

목적:
Google Sheet 또는 CSV 기반 운영 데이터를 읽어오는 공통 모듈.

주의:
- 실제 회사 데이터는 GitHub에 저장하지 않는다.
- 샘플 데이터 기준으로만 테스트한다.
"""

import pandas as pd


def load_sample_data(file_path: str) -> pd.DataFrame:
    """
    샘플 KPI 데이터를 로드한다.

    Expected columns:
    - month
    - division
    - unit
    - client_id
    - revenue
    - labor_cost
    """

    df = pd.read_csv(file_path)

    return df


if __name__ == "__main__":
    print("load_data.py 실행 테스트")
