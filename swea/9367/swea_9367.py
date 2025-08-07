# SWEA 문제 풀이
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'carrot_sample_in.txt'
sys.stdin = file_path.open('r', encoding='utf-8')
T = int(sys.stdin.readline().strip("\n"))

"""
1. 현재 값 = 0, count = 0
2. 0번 idx부터 순환하며 현재값보다 크면 count += 1 and 현재값 = idx
3. 현재값 보다 작으면 count = 1, 현재값 = idx
4. 출력
"""

# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    carrots = int(sys.stdin.readline().strip("\n"))
    # print(carrots)

    carrot_list = list(map(int, sys.stdin.readline().strip("\n").split()))
    # print(carrot_list)

    current_carrot = 0
    increase_count = 0
    max_count = 0
    for carrot in carrot_list:
        if current_carrot < carrot:
            increase_count += 1
        else:
            increase_count = 1
        max_count = max(max_count, increase_count)
        current_carrot = carrot
    print(f"#{test_case} {max_count}")
