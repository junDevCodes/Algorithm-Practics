# SWEA 2105 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
숫자는 디저트 카페의 디저트 종류이고
대각선으로 움직일 수 있는 길들이 있다
사각형을 그려 돌아와야한다

해당 지역을 벗어나면 안되고
순회 중 같은 숫자를 조회하면 안된다
한 곳만 조회할 수 없고
왔던 길을 되돌아 갈 수 없다.

가장 많이 먹을 수 있는 경로를 찾고 그 때의 디저트 수를 구하시오

불가능한 경우 -1을 반환한다.

[입력]
0. TC
1. map_size
2. map_info

[출력]
1. 가장 많이 먹을 수 있는 디저트 수

[알고리즘]
1. 한 지점 기준 방향을 정하고
2. 얼마나 갈지 정하고, 얼마나 돌아올지 정한다
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""


def dfs(c_row, c_col, move, c_way):
    global map_size, max_dessert

    d_row, d_col = d_list[c_way]
    n_row, n_col = c_row + d_row, c_col + d_col

    if 0 <= n_row < map_size and 0 <= n_col < map_size:
        if c_way == 3 and (n_row, n_col) == start_idx:
            max_dessert = max(max_dessert, move)
            return
        if not visited[map_info[n_row][n_col]]:
            visited[map_info[n_row][n_col]] = True
            dfs(n_row, n_col, move+1, c_way)
            if c_way < 3:
                dfs(n_row, n_col, move+1, c_way+1)
            visited[map_info[n_row][n_col]] = False


d_list = [(1, 1), (1, -1), (-1, -1), (-1, 1)] # 0: 우하, 1: 좌하, 2: 좌상, 3: 우상

T = int(input())

for test_case in range(1, T + 1):
    map_size = int(input())
    map_info = [list(map(int, input().split())) for _ in range(map_size)]

    max_dessert = -1

    for row in range(map_size-2):
        for col in range(1, map_size-1):
            visited = [False] * 101
            start_idx = (row, col)
            visited[map_info[row][col]] = True
            dfs(row, col, 1, 0)
    
    print(f"#{test_case} {max_dessert}")
