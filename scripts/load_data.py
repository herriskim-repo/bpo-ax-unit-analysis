"""
load_data.py

목적:
CSV 기반 운영 데이터를 읽어오는 공통 모듈.

주의:
- 외부 패키지(pandas 등)를 사용하지 않는다.
- Python 기본 내장 모듈만 사용한다.
- 실제 회사 데이터는 GitHub에 저장하지 않는다.
- 샘플 데이터 기준으로만 테스트한다.
"""

import csv
from pathlib import Path


REQUIRED_COLUMNS = [
    "month",
    "division",
    "unit",
    "client_id",
    "revenue",
    "labor_cost",
]


def _to_number(value: str) -> float:
    """문자열 숫자를 float로 변환한다. 콤마가 포함된 값도 처리한다."""
    if value is None:
        return 0.0
    clean_value = str(value).replace(",", "").strip()
    if clean_value == "":
        return 0.0
    return float(clean_value)


def load_sample_data(file_path: str | Path) -> list[dict]:
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

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"샘플 데이터 파일을 찾을 수 없습니다: {file_path}")

    rows: list[dict] = []

    with open(file_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)

        missing_columns = [col for col in REQUIRED_COLUMNS if col not in reader.fieldnames]
        if missing_columns:
            raise ValueError(f"필수 컬럼이 없습니다: {missing_columns}")

        for row in reader:
            row["revenue"] = _to_number(row["revenue"])
            row["labor_cost"] = _to_number(row["labor_cost"])
            rows.append(row)

    return rows


if __name__ == "__main__":
    print("load_data.py 실행 테스트")
