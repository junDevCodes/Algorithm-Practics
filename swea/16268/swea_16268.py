# SWEA 16268 문제 풀이
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')
T = int(sys.stdin.readline().strip("\n"))
"""
전체 순환하며 delta 탐색 적용된 꽃가루 합산
"""
# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    col, row = map(int, sys.stdin.readline().strip("\n").split())
    # col, row = map(int, input().split())
    # print(col, row)

    num_list = []
    for _ in range(col):
        num_list.append(list(map(int, sys.stdin.readline().strip("\n").split())))
        # num_list.append(list(map(int, input().split())))
    # print(num_list)

    delta_list = [-1, 1]
    max_val = 0
    for y in range(col):
        for x in range(row):
            cal_val = num_list[y][x]
            for delta in delta_list:
                if 0 <= y+delta < col:
                    cal_val += num_list[y+delta][x]
                if 0 <= x+delta < row:
                    cal_val += num_list[y][x+delta]
            max_val = max(max_val, cal_val)

    print(f"#{test_case} {max_val}")
