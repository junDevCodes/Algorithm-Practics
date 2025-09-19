# SWEA 1868 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
지뢰찾기
근처 8방향에 있는 지뢰의 갯수를 표시한다.
다른 모든 칸의 숫자들이 표시되려면 최소 몇번의 클릭을 해야하는지 구하는 프로그램을 작성하시오

[입력]
0. TC
1. map_size
2. map_info

[출력]
1. 최소 클릭 갯수

[알고리즘]
1. bfs
2. 맵에서 별이 아닌것들이 모두 visited되도록 하는 횟수
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""
from collections import deque

d_list = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1), (1, 1)]


def check_bomb(c_row, c_col):
    global map_size

    bomb_count = 0
    for d_row, d_col in d_list:
        n_row, n_col = c_row + d_row, c_col + d_col

        if 0 <= n_row < map_size and 0 <= n_col < map_size:
            if map_info[n_row][n_col] == "*":
                bomb_count += 1

    return bomb_count


def bfs(m_row, m_col):
    global map_size

    queue = deque([(m_row, m_col)])
    visited_map[m_row][m_col] = True

    while queue:
        c_row, c_col = queue.popleft()

        if map_info[c_row][c_col] == 0:
            for d_row, d_col in d_list:
                n_row, n_col = c_row + d_row, c_col + d_col

                if 0 <= n_row < map_size and 0 <= n_col < map_size:
                    if map_info[n_row][n_col] != "*" and not visited_map[n_row][n_col]:
                        visited_map[n_row][n_col] = True
                        if map_info[n_row][n_col] == 0:
                            queue.append((n_row, n_col))


# T = int(sys.stdin.readline().strip())
T = int(input())

for test_case in range(1, T + 1):

    # map_size = int(sys.stdin.readline().strip())
    map_size = int(input())

    # map_info = [list(map(str, sys.stdin.readline().strip())) for _ in range(map_size)]
    map_info = [list(map(str, input())) for _ in range(map_size)]
    visited_map = [[False] * map_size for _ in range(map_size)]

    for row in range(map_size):
        for col in range(map_size):
            if map_info[row][col] != "*":
                map_info[row][col] = check_bomb(row, col)

    # print(map_info)

    count = 0
    for row in range(map_size):
        for col in range(map_size):
            if map_info[row][col] == 0 and not visited_map[row][col]:
                bfs(row, col)
                count += 1

    for row in range(map_size):
        for col in range(map_size):
            if map_info[row][col] != "*" and not visited_map[row][col]:
                visited_map[row][col] = True
                count += 1

    # 출력 (SWEA 형식)
    print(f"#{test_case} {count}")
