# SWEA 5650 문제 풀이
import sys
from pathlib import Path

# 로컬 테스트용 파일 입력 설정
BASE_DIR = Path(__file__).resolve().parent
sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
N x N 크기의 핀볼 게임판
총 5가지 형태의 블럭
웜홀과 블랙홀 존재

블럭 형태
1: |\ : 상 -> 하, 하 -> 우, 좌 -> 상, 우 -> 좌
2: |/ : 상 -> 우, 하 -> 상, 좌 -> 하, 우 -> 좌
3: \| : 상 -> 좌, 하 -> 상, 좌 -> 우, 우 -> 하
4: /| : 상 -> 하, 하 -> 좌, 좌 -> 우, 우 -> 상
5: 정사각형 : 좌 <-> 우, 상 <-> 하

웜홀에 빠지면 동일한 숫자를 가진 반대편 웜홀로 이동하며 진행방향은 그대로 유지된다

핀볼이 블랙홀을 만나게 되며 핀볼이 사라지게 되어 게임이 끝난다

핀볼이 출발위치로 돌아오거나 블랙홀에 빠질 때 끝나며 점수는 벽이나 블럭에 부딪힌 횟수가 된다.
최대 점수를 구하시오

[입력]
0. TC
1. N
2. board

[출력]
1. 최대 점수를 구하시오

[알고리즘]
1. 최대 점수 -> 출발 위치 기준 4방향 전부 탐색
2. 반복문 통해 시뮬레이션
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""
<<<<<<< HEAD
max_score = 0
# 0: 상, 1: 하, 2: 좌, 3: 우
d_way = {0: (-1, 0),
         1: (1, 0),
         2: (0, -1),
         3: (0, 1)}


def ball_simulation(board, start_way, start_coord, next_coord):
    global max_score

    c_score = 0
    cur_r, cur_c = next_coord
    while board[cur_r][cur_c] != -1 or (cur_r, cur_c) != start_coord:


def solve():
    global max_score

    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        board = [list(map(int, input().split())) for _ in range(N)]

        for r in range(N):
            for c in range(N):
                if board[r][c] == 0:
                    for way, d_val in list(d_way.items()):
                        dr, dc = d_val
                        nr, nc = r + dr, c + dc

                        if nr < 0 or nc < 0 or nr >= N or nc >= N: continue

                        if board[nr][nc] != 0: continue
                        ball_simulation(board, way, (r, c), (nr, nc))

        print(f"#{test_case} {max_score}")
=======
# 0: 상, 1: 하, 2: 좌, 3: 우
d_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
block_reflect = {
    1: {0: 1, 1: 3, 2: 0, 3: 2},
    2: {0: 3, 1: 0, 2: 1, 3: 2},
    3: {0: 2, 1: 0, 2: 3, 3: 1},
    4: {0: 1, 1: 2, 2: 3, 3: 0},
    5: {0: 1, 1: 0, 2: 3, 3: 2}
}
max_value = 0
wormhole = {}


def ball_simulation(board, start_way, start_coord):
    global max_value, block_reflect, d_list, wormhole

    N = len(board)
    c_count = 0
    c_way = start_way
    cr, cc = start_coord

    while True:
        dr, dc = d_list[c_way]
        nr, nc = cr + dr, cc + dc

        if nr < 0 or nc < 0 or nr >= N or nc >= N:
            c_way = block_reflect[5][c_way]
            c_count += 1
            dr, dc = d_list[c_way]
            nr, nc = nr + dr, nc + dc

        cr, cc = nr, nc

        if (cr, cc) == start_coord or board[cr][cc] == -1:
            max_value = max(max_value, c_count)
            return

        if board[cr][cc] == 0: continue

        if board[cr][cc] > 5:
            cr, cc = wormhole[(cr, cc)]
            continue

        c_way = block_reflect[board[cr][cc]][c_way]
        c_count += 1


def solve():
    global max_value, d_list, wormhole

    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        board = [list(map(int, input().split())) for _ in range(N)]

        wormhole = {}
        wormhole_check = [tuple()] * 11
        max_value = 0

        for r in range(N):
            for c in range(N):
                if board[r][c] > 5:
                    w_val = board[r][c]
                    if not wormhole_check[w_val]:
                        wormhole_check[w_val] = (r, c)
                        continue

                    wormhole[(r, c)] = wormhole_check[w_val]
                    wormhole[wormhole_check[w_val]] = (r, c)

        for r in range(N):
            for c in range(N):
                if board[r][c] == 0:
                    start_coord = (r, c)
                    for way, dxy in enumerate(d_list):
                        ball_simulation(board, way, start_coord)

        print(f"#{tc} {max_value}")
>>>>>>> afd27d6f726ba58c27b63fbddc6a0622a93bc9fc


solve()
