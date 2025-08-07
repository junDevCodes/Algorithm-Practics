# SWEA 12712 문제 풀이
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')
T = int(sys.stdin.readline().strip("\n"))

"""
map_list 순회
delta_list 조회해서 값 합산

계산값 = idx
delta_list = 1 ~ spray_size
idx - delta >= 0
idx + delta <= map_size
"""

# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    map_size, spray_size = map(int, sys.stdin.readline().strip("\n").split())
    # print(map_size, spray_size)

    map_list = []
    for _ in range(map_size):
        map_list.append(list(map(int, sys.stdin.readline().strip("\n").split())))
    # print(map_list)

    max_val = 0
    for col in range(map_size):
        for row in range(map_size):
            plus_val = map_list[col][row]
            x_val = map_list[col][row]
            for delta in range(1, spray_size):
                # 직각 합 / 대각 합
                if col - delta >= 0:
                    plus_val += map_list[col-delta][row]
                    if row - delta >= 0:
                        x_val += map_list[col-delta][row-delta]
                    if row + delta < map_size:
                        x_val += map_list[col-delta][row+delta]
                if row - delta >= 0:
                    plus_val += map_list[col][row-delta]
                if col + delta < map_size:
                    plus_val += map_list[col+delta][row]
                    if row - delta >= 0:
                        x_val += map_list[col+delta][row-delta]
                    if row + delta < map_size:
                        x_val += map_list[col+delta][row+delta]
                if row + delta < map_size:
                    plus_val += map_list[col][row+delta]

            max_val = max(max_val, plus_val, x_val)

    print(f"#{test_case} {max_val}")
