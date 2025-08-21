# SWEA 21772 문제 풀이
from collections import deque

# import sys
# from pathlib import Path
#
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')
#
# T = int(sys.stdin.readline().strip("\n"))
"""
[문제 설명]
여기에 문제 요약과 요구사항을 작성하세요.

[입력]
- 입력 형식에 대한 설명
- 각 줄별 입력 내용

[출력]
- 출력 형식에 대한 설명

[로직]
- 문제 해결에 필요한 알고리즘

[예시 입력]
예시 입력 내용을 작성

[예시 출력]
예시 출력 내용을 작성
"""
T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    # num, rotate = map(int, sys.stdin.readline().strip("\n").split())
    num, rotate = map(int, input().split())

    # num_list = deque(list(map(int, sys.stdin.readline().strip("\n").split())))
    num_list = deque(list(map(int, input().split())))
    for _ in range(rotate):
        num_list.rotate(-1)
    print(f"#{test_case} {num_list[0]}")
