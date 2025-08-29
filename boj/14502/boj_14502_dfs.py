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

from collections import deque
import copy


def bfs(lab_map, virus_loc):

    max_row, max_col = len(lab_map), len(lab_map[0])
    queue = deque(virus_loc)
    delta_list = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while queue:
        current_row, current_col = queue.popleft()

        for delta_row, delta_col in delta_list:
            next_row, next_col = current_row + delta_row, current_col + delta_col

            if 0 <= next_row < max_row and 0 <= next_col < max_col and lab_map[next_row][next_col] == 0:
                lab_map[next_row][next_col] = 2
                queue.append((next_row, next_col))

    safe_area_count = 0
    for row in range(max_row):
        for col in range(max_col):
            if lab_map[row][col] == 0:
                safe_area_count += 1

    return safe_area_count


def dfs(lab_map, safe_loc, virus_loc, start_idx, count, max_safe_area):

    if count == 3:
        temp_map = copy.deepcopy(lab_map)
        current_safe_area = bfs(temp_map, virus_loc)
        return max(max_safe_area, current_safe_area)

    current_max = max_safe_area

    for i in range(start_idx, len(safe_loc)):
        row, col = safe_loc[i]

        lab_map[row][col] = 1

        current_max = dfs(lab_map, safe_loc, virus_loc, i + 1, count + 1, current_max)

        lab_map[row][col] = 0

    return current_max


def solve():
    # map_row, map_col = map(int, sys.stdin.readline().strip().split())
    map_row, map_col = map(int, input().split())
    # lab_map = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(map_row)]
    lab_map = [list(map(int, input().split())) for _ in range(map_row)]

    safe_loc = []
    virus_loc = []
    for row in range(map_row):
        for col in range(map_col):
            if lab_map[row][col] == 0:
                safe_loc.append((row, col))
            elif lab_map[row][col] == 2:
                virus_loc.append((row, col))

    result = dfs(lab_map, safe_loc, virus_loc, 0, 0, 0)
    print(result)

    return 0


solve()
