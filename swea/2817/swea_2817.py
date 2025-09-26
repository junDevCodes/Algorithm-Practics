# SWEA 2817 문제 풀이
# import sys
# from pathlib import Path
#
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')

"""
[문제 설명]
N개의 자연수 수열 A가 주어지고
부분 수열의 합이 K가 되는 경우의 수를 출력하시오

[입력]
0. TC
1. seq_num, sum_target
2. seq_info

[출력]
1. 부분 수열 합의 K가 되는 경우의 수 

[로직]
dfs를 통한 완탐과 백트래킹

[예시 입력]
1
4 3
1 2 1 2

[예시 출력]
#1 4

"""


def dfs(start_idx, c_val):
    global seq_num, sum_target, count

    if c_val == sum_target:
        count += 1
        return

    if c_val > sum_target:
        return

    for c_idx in range(start_idx, seq_num):
        dfs(c_idx+1, c_val + seq_info[c_idx])
    return 0


# T = int(sys.stdin.readline())
T = int(input())

# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    # seq_num, sum_target = map(int, sys.stdin.readline().strip().split())
    seq_num, sum_target = map(int, input().split())

    # seq_info = list(map(int, sys.stdin.readline().strip().split()))
    seq_info = list(map(int, input().split()))

    count = 0
    dfs(0, 0)

    print(f"#{test_case} {count}")
