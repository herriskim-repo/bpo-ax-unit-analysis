# Executive Report Template

> 본 템플릿은 BPO UNIT 운영현황을 경영진 보고용으로 정리하기 위한 Markdown 보고서 양식입니다.
> 실제 회사 데이터는 GitHub에 저장하지 않고, 실행 시 생성된 결과만 로컬 또는 보안 저장소에 보관합니다.

---

# {{report_month}} BPO 운영현황 Executive Report

## 1. 핵심 요약

- 이번 달 전체 인건비율: {{overall_labor_ratio}}
- KPI 기준: 인건비율 62% 이하
- KPI 초과 UNIT 수: {{breach_unit_count}}
- 주요 위험 UNIT: {{top_risk_units}}
- 우선 검토 Action: {{recommended_action_summary}}

### Executive Summary

{{executive_summary}}

---

## 2. KPI 초과 UNIT

| 사업부 | UNIT | 매출 | 인건비 | 인건비율 | 상태 |
|---|---:|---:|---:|---:|---|
| {{division}} | {{unit}} | {{revenue}} | {{labor_cost}} | {{labor_ratio}} | {{status}} |

### 해석

{{kpi_breach_commentary}}

---

## 3. 사업부별 운영 현황

| 사업부 | 매출 | 인건비 | 인건비율 | KPI 상태 |
|---|---:|---:|---:|---|
| {{division}} | {{division_revenue}} | {{division_labor_cost}} | {{division_labor_ratio}} | {{division_status}} |

### 사업부별 코멘트

{{division_commentary}}

---

## 4. 위험 고객사 후보

| 고객사 ID | 사업부 | UNIT | 매출 | 인건비 | 인건비율 | 위험 사유 |
|---|---|---|---:|---:|---:|---|
| {{client_id}} | {{division}} | {{unit}} | {{revenue}} | {{labor_cost}} | {{labor_ratio}} | {{risk_reason}} |

### 해석

{{risk_client_commentary}}

---

## 5. 원인 추정

다음 원인을 우선 검토합니다.

- 매출 감소 대비 인건비 고정
- UNIT 내 고객사 mix 변화
- 상담원 Sharing 효과 저하 가능성
- 쇼핑몰 CS 반복 문의 증가 가능성
- 특수 고객 운영 부담 가능성

### 자동 생성 원인 요약

{{root_cause_summary}}

---

## 6. 추천 Action

| 우선순위 | Action | 대상 | 기대 효과 |
|---:|---|---|---|
| 1 | {{action_1}} | {{target_1}} | {{expected_effect_1}} |
| 2 | {{action_2}} | {{target_2}} | {{expected_effect_2}} |
| 3 | {{action_3}} | {{target_3}} | {{expected_effect_3}} |

---

## 7. AI 적용 검토 가능 영역

쇼핑몰 CS 고객 비중이 높은 경우 다음 영역을 우선 검토합니다.

- 배송 조회
- 주문 확인
- 교환/반품
- 취소 요청
- 회원/쿠폰/적립금 문의

### AI 적용 후보 코멘트

{{ai_candidate_commentary}}

---

## 8. 다음 단계

- KPI 초과 UNIT 원인 확인
- 위험 고객사 운영 담당자 인터뷰
- Chat Bot / Voice Bot 적용 가능 업무 유형 확인
- 다음 월 보고서 자동화 반복 실행

---

## 부록: 보고서 생성 기준

- 인건비율 = labor_cost / revenue
- KPI 기준 = 62% 이하
- 분석 단위 = 사업부 → UNIT → 고객사
- 본 보고서는 경영진 의사결정 지원용 초안이며, 최종 판단은 운영 담당자가 검증합니다.
