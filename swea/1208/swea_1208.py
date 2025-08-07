# SWEA 1208 문제 풀이
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')
T = 10
"""
dump동안 반복
box_height의 맥스 값에 해당하는 idx를 -1 이후 min값에 해당하는 idx +1
dump 반복 이후 최고점과 최저점 반환
"""
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dump_count = int(sys.stdin.readline().strip("\n"))
    # print(dump)

    box_height = list(map(int,sys.stdin.readline().strip().split()))
    # print(box_height)

    for i in range(dump_count):
        high_val = max(box_height)
        low_val = min(box_height)
        high_idx = box_height.index(high_val)
        low_idx = box_height.index(low_val)
        box_height[high_idx] -= 1
        box_height[low_idx] += 1

    gap_height = max(box_height) - min(box_height)

    print(f"#{test_case} {gap_height}")
