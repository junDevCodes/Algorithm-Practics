# Gemini Agent Configuration for Algorithms Repository

This document outlines the conventions and guidelines for managing the `algorithms` directory as a dedicated GitHub repository. This information is intended for the Gemini agent to ensure consistent behavior and for future reference by other agents or users.

## 1. Project Goal (프로젝트 목표)
The primary goal is to manage the `C:/Users/jylee/Desktop/workspace/algorithms/` directory as an independent GitHub repository for algorithm problem-solving.

## 2. Directory Structure Convention (디렉토리 구조 규칙)
The repository will follow a `platform/problem_number/` directory structure.
Example: `algorithms/swea/6254/`

## 3. File Naming Convention (파일 이름 규칙)
- **Solution Files (풀이 파일)**: Solution files should be named using the format `platform_problemNumber.py`.
  Example: `swea_6254.py` (instead of `solution.py`)
- **Markdown Files (마크다운 파일)**: A `README.md` file will be created within each problem's directory to document the solution.

## 4. Problem Solution Markdown File (`README.md`) Template (문제 풀이 마크다운 파일 템플릿)
The following template will be used for the `README.md` file generated for each problem.
**Note (참고)**: The sections "잘한 점 (Strengths)" and "개선할 점 / 아쉬운 점 (Areas for Improvement / Regrets)" are to be filled in by the user, as the agent cannot accurately analyze and provide these insights without direct understanding of the user's thought process and problem-solving context.

```markdown
# [플랫폼] [문제 번호] - [문제 제목]

- **플랫폼**: [플랫폼 이름 (예: SWEA, BOJ, Programmers)]
- **문제 번호**: [문제 번호 (예: 6254)]
- **문제 제목**: [문제의 공식 제목]
- **문제 링크**: [문제 페이지 URL]

## 사용한 알고리즘 및 자료구조
- [사용한 알고리즘 (예: BFS, DFS, 다이나믹 프로그래밍, 그리디)]
- [사용한 자료구조 (예: 큐, 스택, 딕셔너리, 리스트)]

## 풀이 설명
[문제 해결을 위한 접근 방식, 핵심 아이디어, 단계별 풀이 과정 등을 상세히 설명합니다.]

## 시간 복잡도 및 공간 복잡도
- **시간 복잡도**: O([시간 복잡도 표기])
- **공간 복잡도**: O([공간 복잡도 표기])

## 잘한 점
[스스로 생각했을 때 이 풀이에서 좋았던 점, 배운 점, 효율적이었던 부분 등을 기록합니다. 이 부분은 사용자님께서 직접 작성해주셔야 합니다.]

## 개선할 점 / 아쉬운 점
[풀이 과정에서 아쉬웠던 점, 더 효율적으로 개선할 수 있는 부분, 놓쳤던 부분 등을 기록합니다. 이 부분은 사용자님께서 직접 작성해주셔야 합니다.]
```