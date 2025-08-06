# SWEA 4836 문제 풀이
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'

sys.stdin = file_path.open('r', encoding='utf-8')
T = int(sys.stdin.readline().strip("\n"))

# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    paint = int(sys.stdin.readline().strip("\n"))
    num_list = [[0]*10 for _ in range(10)]
    color_list = []

    for _ in range(paint):
        start_col, start_row, end_col, end_row, color = map(int, sys.stdin.readline().strip("\n").split())
        for col in range(start_col, end_col+1):
            for row in range(start_row, end_row+1):
                num_list[col][row] += color

    count = 0
    for line in num_list:
        for element in line:
            if element == 3:
                count += 1

    print(f"#{test_case} {count}")
