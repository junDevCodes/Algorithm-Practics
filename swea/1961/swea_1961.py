# SWEA 1961 문제 풀이
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'input.txt'

sys.stdin = file_path.open('r', encoding='utf-8')
T = int(sys.stdin.readline().strip("\n"))

# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    size = int(sys.stdin.readline().strip("\n"))
    # print(size)

    num_list = []
    for _ in range(size):
        num_list.append(list(map(int, sys.stdin.readline().strip("\n").split())))
    # print(num_list)

    rotate_90_num_list = list(zip(*reversed(num_list)))
    rotate_180_num_list = list(zip(*reversed(rotate_90_num_list)))
    rotate_270_num_list = list(reversed([*zip(*num_list)]))

    print(f"#{test_case}")
    for idx in range(size):
        rt_90 = "".join(map(str,rotate_90_num_list[idx]))
        rt_180 = "".join(map(str,rotate_180_num_list[idx]))
        rt_270 = "".join(map(str,rotate_270_num_list[idx]))
        print(f"{rt_90} {rt_180} {rt_270}")
