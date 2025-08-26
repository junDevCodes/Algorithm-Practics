# BOJ 14502 문제 풀이
# import sys
# from pathlib import Path
#
# # 파일 입력 설정 (로컬 테스트용)
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')

"""
[문제 설명]
바이러스는 상하좌우 인접한 빈 칸으로 퍼져나갈 수 있다.
벽의 갯수는 꼭 3개를 세워야 한다
0 : 빈칸
1 : 벽
2 : 바이러스

벽을 3개 세운 후 바이러스가 퍼질 수 없는 영역 크기의 최댓값을 구하시오

[입력]
1. map_col, map_row
2. map_info

[출력]
1. 벽 3개를 세운 후 바이러스가 퍼질 수 없는 영역 크기의 최댓값

[알고리즘]
1. 조합을 통해 벽 3개를 세우는 경우의 수를 찾는다
2. 세운 상태에서 bfs를 통해 델타탐색으로 구현
3. 가지치기 early return을 통해 과도한 계산 방지
    바이러스의 갯수를 카운트해서 min값 넘어가면 return
4. 가장 min 바이러스 갯수인 경우 남은 안전지대 갯수 카운팅

[예시]
입력:
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

출력:
27
"""

import itertools
from collections import deque
from copy import deepcopy

delta_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(map_list):
    queue = deque(virus_index_list)
    visited = {*virus_index_list}
    while queue:
        current_col, current_row = queue.popleft()
        for dt_col, dt_row in delta_list:
            next_col, next_row = current_col + dt_col, current_row + dt_row
            if 0 <= next_col < map_col and 0 <= next_row < map_row:
                if map_list[next_col][next_row] != 1 and (next_col, next_row) not in visited:
                    map_list[next_col][next_row] = 2
                    queue.append((next_col, next_row))
                    visited.add((next_col, next_row))

    sum_safe_place = 0
    for col_idx in range(map_col):
        for row_idx in range(map_row):
            if map_list[col_idx][row_idx] == 0:
                sum_safe_place += 1
    return sum_safe_place


# map_col, map_row = map(int, sys.stdin.readline().strip().split())
map_col, map_row = map(int, input().split())
# print(map_col, map_row)

# map_info = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(map_col)]
map_info = [list(map(int, input().split())) for _ in range(map_col)]
# print(map_info)

empty_index_list = []
virus_index_list = []
for col in range(map_col):
    for row in range(map_row):
        if map_info[col][row] == 0:
            empty_index_list.append((col, row))
        elif map_info[col][row] == 2:
            virus_index_list.append((col, row))
# print(empty_index_list)

wall_list = list(itertools.combinations(empty_index_list, 3))
# print(wall_list)

safe_place = 0
max_safe_place = 0
for wall in wall_list:
    copy_map_info = deepcopy(map_info)

    for wall_col, wall_row in wall:
        copy_map_info[wall_col][wall_row] = 1

    safe_place = bfs(copy_map_info)

    max_safe_place = max(max_safe_place, safe_place)

print(max_safe_place)