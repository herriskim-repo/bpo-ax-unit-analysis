"""
run_pipeline.py

목적:
BPO AX Executive Reporting 전체 실행 파이프라인.

실행 흐름:
1. sample KPI 데이터 로드
2. 인건비율 계산
3. KPI 초과 UNIT 탐지
4. Executive Report 생성
5. Markdown 파일 저장
"""

from pathlib import Path
from datetime import datetime

from load_data import load_sample_data
from calculate_kpi import calculate_labor_ratio, summarize_by_unit
from detect_risk_units import detect_risk_units
from generate_executive_report import generate_markdown_report


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "sample" / "sample_kpi_data.csv"
OUTPUT_DIR = BASE_DIR / "reports" / "generated"


def main():
    print("[1] KPI 데이터 로드")

    df = load_sample_data(DATA_PATH)

    print("[2] 인건비율 계산")

    df = calculate_labor_ratio(df)

    print("[3] UNIT KPI 요약")

    summary_df = summarize_by_unit(df)

    print("[4] KPI 초과 UNIT 탐지")

    risk_df = detect_risk_units(summary_df)

    print("[5] Executive Report 생성")

    report = generate_markdown_report(risk_df)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    today = datetime.today().strftime("%Y_%m_%d")

    output_file = OUTPUT_DIR / f"executive_report_{today}.md"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report)

    print("\n=== 실행 완료 ===")
    print(f"Report saved: {output_file}")


if __name__ == "__main__":
    main()
