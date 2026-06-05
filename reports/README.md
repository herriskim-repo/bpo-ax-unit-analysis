BPO AX Executive Reporting

이 repository는 BPO 운영분석 AX(Agent Transformation) 파일럿 프로젝트입니다.

목표는 기존 Looker Studio 기반 단순 시각화 보고를 넘어,
운영 데이터를 기반으로 AI Executive Reporting 체계를 구축하는 것입니다.

주요 목표
UNIT별 인건비율 자동 분석
KPI 초과 UNIT 자동 탐지
경영진용 Executive Narrative 생성
운영 규칙의 조직 지식화
반복 보고 업무 자동화
핵심 KPI

인건비율 = labor_cost / revenue

KPI 목표 = 62% 이하

데이터 구조

주요 컬럼:

month
division
unit
client_id
revenue
labor_cost
보안 원칙
실제 회사 데이터는 GitHub에 업로드하지 않음
csv/xlsx 원본 파일 commit 금지
GitHub에는 코드와 문서만 저장
실제 데이터는 Google Workspace 내 관리
주요 구성 요소
Python KPI 분석
Codex Narrative 생성
Markdown Executive Report
AGENTS.md 기반 작업 규칙
Skill 기반 반복 업무 자동화
목표 방향

개인 경험
→ 운영 규칙
→ AGENTS.md / Skills
→ 조직 지식

구조로 전환하는 것이 목표이다.
