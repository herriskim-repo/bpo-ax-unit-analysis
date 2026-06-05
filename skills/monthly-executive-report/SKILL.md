---
name: monthly-executive-report
description: Generate monthly executive KPI report for BPO UNIT operation.
---

# Monthly Executive Report Skill

## 목적

월별 운영 데이터를 기반으로 경영진용 Executive Report를 생성한다.

---

# 입력 데이터

Expected columns:

- month
- division
- unit
- client_id
- revenue
- labor_cost

---

# KPI 규칙

인건비율 = labor_cost / revenue

KPI 기준 = 62% 이하

---

# 수행 작업

1. UNIT별 인건비율 계산
2. KPI 초과 UNIT 탐지
3. 사업부별 요약 생성
4. 위험 고객사 탐지
5. Executive Narrative 생성
6. 추천 Action 생성
7. AI 적용 가능 영역 제안

---

# 출력 형식

Markdown Executive Report

구성:

1. 핵심 요약
2. KPI 초과 UNIT
3. 사업부별 운영 현황
4. 위험 고객사 후보
5. 원인 추정
6. 추천 Action
7. AI 적용 검토 가능 영역

---

# Reporting Style

- 경영진 중심
- 간결
- Action oriented
- Technical jargon 최소화

---

# Important Rules

- 실제 데이터 사용 금지
- 샘플 데이터만 사용
- 비개발자 기준 설명 유지
