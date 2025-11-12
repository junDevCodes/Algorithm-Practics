# SWEA 1234 문제 풀이
import sys
from pathlib import Path

# 로컬 테스트용 파일 입력 설정
BASE_DIR = Path(__file__).resolve().parent
sys.stdin = (BASE_DIR / "sample_input.txt").open("r", encoding="utf-8")

"""
[문제 설명]


[조건]


[입력]


[출력]


[알고리즘]
1. 
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""


def solve():
    T = int(input())

    for test_case in range(1, T + 1):

        print(f"#{test_case}")


solve()
