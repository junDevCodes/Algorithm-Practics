# SWEA 4206 문제 풀이
import sys
from pathlib import Path

# 파일 입력 설정 (로컬 테스트용)
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')

"""
[문제 설명]
여기에 문제 요약과 요구사항을 작성하세요.

[입력]
- 입력 형식에 대한 설명
- 각 줄별 입력 내용

[출력]
- 출력 형식에 대한 설명

[알고리즘]
1. 문제 해결 단계
2. 필요한 자료구조/알고리즘
3. 시간복잡도 고려사항

[예시]
입력:
예시 입력 내용

출력:
예시 출력 내용
"""

# SWEA 테스트 케이스 처리 템플릿
T = int(input())

for test_case in range(1, T + 1):
    # 입력 처리
    n = int(input())
    # arr = list(map(int, input().split()))
    
    # 문제 해결 로직
    result = n  # 실제 로직으로 교체
    
    # 출력 (SWEA 형식)
    print(f"#{test_case} {result}")
