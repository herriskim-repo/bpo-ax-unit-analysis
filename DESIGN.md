# DESIGN.md

# BPO AX Executive Reporting Architecture

## 프로젝트 목적

이 프로젝트의 목적은 기존 Looker Studio 기반 단순 시각화 보고를 넘어, BPO 운영 데이터를 기반으로 AI Executive Reporting 체계를 구축하는 것이다.

---

# 핵심 목표

- KPI 위험 탐지
- 위험 UNIT 탐지
- 원인 추정
- Executive Narrative 생성
- Action 제안
- AI Agent 적용 후보 탐지

---

# 시스템 구조

Google Sheet
↓
Python KPI Analysis
↓
Codex Narrative Generation
↓
Executive Report
↓
Markdown / PDF / PPT

---

# 역할 정의

## Google Sheet

운영 데이터 저장

## Python

KPI 계산 및 데이터 가공

## Codex

Narrative 생성 및 보고서 작성

## AGENTS.md

운영 규칙 및 작업 정책 정의

## Skills

반복 업무 절차 표준화

---

# Executive Reporting 방향

목표는 단순 차트 생성이 아니다.

다음을 자동화하는 것이 핵심이다.

- KPI 위험 탐지
- 원인 추정
- Action 제안
- AI 적용 후보 탐지

---

# 조직 구조

사업부
→ UNIT
→ 고객사

현재 운영은 UNIT 중심으로 이루어진다.

---

# 보안 원칙

- 실제 데이터는 GitHub에 저장하지 않는다.
- GitHub에는 코드와 문서만 저장한다.
- 샘플 데이터는 익명화한다.

---

# AX 방향

이 프로젝트의 핵심은 AI가 운영을 판단하는 것이 아니다.

운영 담당자의 경험과 운영 규칙을 조직 자산으로 축적하는 것이다.

즉,

개인 경험
↓
운영 규칙
↓
AGENTS.md / Skills
↓
조직 지식

구조로 전환하는 것이 목표이다.
