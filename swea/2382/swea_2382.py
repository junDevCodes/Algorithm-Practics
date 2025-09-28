# SWEA 2382 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
미생물 군집이 주어진다
row, col 이 0이나 map_size이면 상하좌우반전 & 미생물 수 // 2
같은 칸에 도달하면 미생물 수를 합치고 제일 큰 미생물 군집의 방향을 따라감
N 시간 이후 총 미생물의 수
상: 1, 하: 2, 좌: 3, 우: 4

[입력]
0. TC
1. map_size, target_time, micro_com_num
2. micro_com_info(row, col, micro_com, dir)

[출력]
M시간 후 남아있는 미생물 수의 총 합

[알고리즘]
1. 같은 칸에 도달한 경우 비교 하고 제일 큰 방향을 들고감
2. 상하좌우 반전 & 미생물 수 // 2
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""

from collections import defaultdict

# T = int(sys.stdin.readline().strip())
T = int(input())

d_list = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

for test_case in range(1, T + 1):
    # map_size, target_time, micro_com_num = map(int, sys.stdin.readline().strip().split())
    map_size, target_time, micro_com_num = map(int, input().split())

    micro_info_list = defaultdict(list)
    for micro_idx in range(1, micro_com_num+1):
        # micro_info_list[micro_idx].extend(list(map(int, sys.stdin.readline().strip().split())))
        micro_info_list[micro_idx].extend(list(map(int, input().split())))
    # print(micro_info_list)
    # 로직
    for _ in range(target_time):
        micro_location_list = defaultdict(list)

        for micro_idx, [c_row, c_col, micro_com, dire] in micro_info_list.items():
            n_row, n_col = c_row + d_list[dire][0], c_col + d_list[dire][1]
            if n_row == 0 or n_row == (map_size-1) or n_col == 0 or n_col == (map_size-1):
                micro_com //= 2 # micro_com 의 수 절반으로
                dire = ((dire - 1) ^ 1) + 1 # 비트 연산 XOR로 방향 전환 시키기
            micro_location_list[(n_row, n_col)].append(micro_idx)
            micro_info_list[micro_idx] = [n_row, n_col, micro_com, dire]

        same_indexes = [keys for keys in micro_location_list.values() if len(keys) > 1]
        for same_index in same_indexes:
            micro_com_list = [0]
            dir_list = [0]
            for idx in same_index:
                same_micro = micro_info_list.pop(idx)
                same_n_row, same_n_col = same_micro[0], same_micro[1]
                micro_com_list.append(same_micro[2])
                dir_list.append(same_micro[3])
                max_idx = micro_com_list.index(max(micro_com_list))
            micro_info_list[idx] = [same_n_row, same_n_col, sum(micro_com_list), dir_list[max_idx]]

    result = 0
    for row, col, micro_sum, dire in micro_info_list.values():
        result += micro_sum

    # 출력 (SWEA 형식)
    print(f"#{test_case} {result}")
