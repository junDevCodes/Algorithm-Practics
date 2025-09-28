# SWEA 1949 문제 풀이
# import sys
# import time
#
# # 로컬 테스트용 파일 입력 설정
# sys.stdin = open('sample_input.txt', 'r', encoding='utf-8')

"""
[문제 설명]
가장 긴 등산로를 찾아서 그 길이를 출력하도록
가장 높은 봉우리에서 시작
가로 세로 방향으로 연결되어야 한다, 높이가 같거나 낮은곳, 대각선 연결 불가
딱 한곳을 정해 최대 K만큼 지형을 깎을 수 있다

[입력]
0. TC
1. map_size, dig_once
2. map_info

[출력]
1. 최대 길이

[알고리즘]
dfs

[복잡도]
- 시간: O()
- 공간: O()
"""

d_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(c_row, c_col, is_dig, road):
    global max_road

    max_road = max(max_road, road + 1)
    visited[c_row][c_col] = True

    for d_row, d_col in d_list:
        n_row, n_col = c_row + d_row, c_col + d_col

        if 0 <= n_row < map_size and 0 <= n_col < map_size and not visited[n_row][n_col]:
            c_height = map_info[c_row][c_col]
            n_height = map_info[n_row][n_col]

            if n_height < c_height:
                dfs(n_row, n_col, is_dig, road+1)
            elif not is_dig and n_height-dig_once < c_height:
                map_info[n_row][n_col] = c_height-1
                dfs(n_row, n_col, True, road+1)
                map_info[n_row][n_col] = n_height

    visited[c_row][c_col] = False


# T = int(sys.stdin.readline().strip())
T = int(input())

for tc in range(1, T + 1):
    # map_size, dig_once = map(int, sys.stdin.readline().strip().split())
    map_size, dig_once = map(int, input().split())

    # map_info = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(map_size)]
    map_info = [list(map(int, input().split())) for _ in range(map_size)]
    visited = [[False] * map_size for _ in range(map_size)]

    start_loc = []
    max_val = 0
    for row in range(map_size):

        if max(map_info[row]) < max_val:
            continue

        for col in range(map_size):
            if max_val < map_info[row][col]:
                max_val = map_info[row][col]
                start_loc = [(row, col)]
            elif max_val == map_info[row][col]:
                start_loc.append((row, col))
    # print(start_loc)

    max_road = 0
    for row, col in start_loc:
        dfs(row, col, False, 1)

    print(f"#{tc} {max_road}")
