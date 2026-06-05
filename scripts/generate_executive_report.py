"""
generate_executive_report.py

목적:
경영진용 Executive Report 초안 생성.

출력 형식:
Markdown
"""

from datetime import datetime


def generate_markdown_report(risk_units):
    """
    KPI 초과 UNIT 기반 Executive Summary 생성
    """

    today = datetime.today().strftime("%Y-%m-%d")

    report = f"# Executive Report ({today})\n\n"

    report += "## 핵심 요약\n\n"
    report += "KPI 초과 UNIT 중심 운영 리스크 점검 필요.\n\n"

    report += "## KPI 초과 UNIT\n\n"

    for _, row in risk_units.iterrows():
        ratio = round(row['labor_ratio'] * 100, 1)

        report += (
            f"- {row['division']} / {row['unit']} "
            f": 인건비율 {ratio}%\n"
        )

    report += "\n## 추천 Action\n\n"
    report += "- Chat Bot 적용 가능 고객 검토\n"
    report += "- UNIT 간 인력 Sharing 검토\n"
    report += "- KPI 초과 UNIT 운영 구조 점검\n"

    return report


if __name__ == "__main__":
    print("generate_executive_report.py 실행 테스트")
