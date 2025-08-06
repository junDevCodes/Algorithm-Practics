# SWEA 2001 문제 풀이
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')
T = int(sys.stdin.readline().strip("\n"))

# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    size, flap = map(int, sys.stdin.readline().strip("\n").split())

    fly_list = []
    for _ in range(size):
        fly_list.append(list(map(int, sys.stdin.readline().strip("\n").split())))

    find_fly = size-flap+1
    max_val = 0

    for y in range(find_fly):
        for x in range(find_fly):
            cal_val = 0
            for delta_y in range(flap):
                for delta_x in range(flap):
                    cal_val += fly_list[y+delta_y][x+delta_x]
            max_val = max(max_val, cal_val)

    print(f"#{test_case} {max_val}")