# SWEA 25028 문제 풀이
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'input_internal.txt'
sys.stdin = file_path.open('r', encoding='utf-8')

T = int(sys.stdin.readline().strip("\n"))
"""
[문제 설명]
과목 N개
1~N번까지 과목이 주어진다


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
# T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    task = int(sys.stdin.readline().strip("\n"))
    # print(task)

    task_list = [list(map(int, sys.stdin.readline().strip("\n").split())) for _ in range(task)]
    # print(task_list)

    result = 1
    max_val = 1
    for col in task_list:
        if sorted(col) == list(set(col)):
            max_val = max(max_val, max(col))
            result = max_val
        else:
            result = -1
            break
    print(f"#{test_case} {result}")
