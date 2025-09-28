# SWEA 1226 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
미로의 정보가 주어지고 도달 가능한지 보는 것

[입력]
0. TC = 10
1. TC_num
2. 미로 정보(길 : 0, 벽 : 1, 출발 : 2, 도착 : 3)

[출력]
1. 도착 가능 여부

[알고리즘]
1. dfs 통해 2에서 출발
2. 델타 통해 0인 경우 dfs 넣기
3. visited 넣기
4. 델타 도착인 경우 1 출력 없으면 0

[복잡도]
- 시간: O()
- 공간: O()
"""
from collections import deque


def bfs(s_xy):
    map_size = len(map_info)
    queue = deque([s_xy])
    visited = [s_xy]

    while queue:
        c_row, c_col = queue.popleft()

        for d_row, d_col in d_list:
            n_row, n_col = c_row + d_row, c_col + d_col
            if 0 <= n_row < map_size and 0 <= n_col < map_size:
                n_idx = (n_row, n_col)
                if map_info[n_row][n_col] == 0 and n_idx not in visited:
                    queue.append(n_idx)
                    visited.append(n_idx)
                elif map_info[n_row][n_col] == 3:
                    return 1
    return 0


T = 10
d_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]


for test_case in range(1, T + 1):
    # 입력
    # TC = int(sys.stdin.readline().strip())
    TC = int(input())

    # map_info = [list(map(int, sys.stdin.readline().strip())) for _ in range(16)]
    map_info = [list(map(int, input())) for _ in range(16)]

    for i in range(len(map_info)):
        try:
            j = map_info[i].index(2)
            start_index = (i, j)
            break
        except ValueError:
            continue

    arrive = bfs(start_index)

    # 출력 (SWEA 형식)
    print(f"#{test_case} {arrive}")
