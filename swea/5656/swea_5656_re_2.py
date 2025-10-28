# SWEA 5656 문제 풀이
import sys
from pathlib import Path

# 로컬 테스트용 파일 입력 설정
BASE_DIR = Path(__file__).resolve().parent
sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
N: 구슬 발사 횟수
W: 맵 가로(넓이)
H: 맵 세로(높이)

발사 횟수를 전부 소진했을 경우 남아있는 블럭이 가장 작은 경우

[입력]
0. TC
1. N, W, H
2. board_info

[출력]
남아있는 블럭 갯수

[알고리즘]
dfs 위에서 공 떨어트리기
bfs 연쇄 폭발
drop 함수 구현

[복잡도]

"""

from collections import deque

min_block = float("inf")


def sum_check(board):
    return sum(1 for row in board for cell in row if cell > 0)


def copy_board(board):
    return [row[:] for row in board]


def drop(board):
    W = len(board[0])
    H = len(board)

    for c_col in range(W):
        write = H - 1
        for c_row in range(H - 1, -1, -1):
            if board[c_row][c_col] > 0:
                board[write][c_col] = board[c_row][c_col]
                if write != c_row:
                    board[c_row][c_col] = 0
                write -= 1

        while write >= 0:
            board[write][c_col] = 0
            write -= 1


def bfs(board, c_row, c_col):
    W = len(board[0])
    H = len(board)

    d_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([(c_row, c_col, board[c_row][c_col])])
    board[c_row][c_col] = 0

    while queue:
        cr, cc, power = queue.popleft()
        if power < 2: continue

        for cp in range(1, power):
            for dr, dc in d_list:
                nr, nc = cr + (dr * cp), cc + (dc * cp)

                if nr < 0 or nc < 0 or nr >= H or nc >= W: continue

                if board[nr][nc] > 1:
                    queue.append((nr, nc, board[nr][nc]))
                board[nr][nc] = 0


def dfs(board, N_left):
    global min_block

    W = len(board[0])
    H = len(board)

    if N_left == 0:
        min_block = min(min_block, sum_check(board))
        return

    c_block = sum_check(board)
    if c_block == 0:
        min_block = 0
        return

    if min_block == 0:
        return

    for c_col in range(W):
        c_row = 0
        while c_row < H and board[c_row][c_col] == 0:
            c_row += 1

        if c_row == H: continue

        temp_board = copy_board(board)
        bfs(temp_board, c_row, c_col)
        drop(temp_board)
        dfs(temp_board, N_left - 1)


def solve():
    global min_block

    T = int(input())

    for tc in range(1, T + 1):
        N, W, H = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(H)]
        min_block = float("inf")

        dfs(board, N)

        print(f"#{tc} {min_block}")


solve()
