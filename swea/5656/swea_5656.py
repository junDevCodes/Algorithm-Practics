import sys
from collections import deque
import copy

# 파일 입력 설정 (로컬 테스트용)
# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')

# 전역 변수를 사용하여 최솟값을 추적합니다.
min_bricks = float('inf')


def bfs(board, r, c):
    """BFS를 사용하여 벽돌을 터뜨리고 연쇄 폭발을 시뮬레이션합니다."""
    q = deque([(r, c)])
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 터뜨릴 벽돌의 파워를 저장하고 0으로 만듭니다.
    power = board[r][c]
    board[r][c] = 0

    while q:
        cur_r, cur_c = q.popleft()

        for d in range(4):
            for i in range(1, power):
                next_r, next_c = cur_r + delta[d][0] * i, cur_c + delta[d][1] * i

                if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]) and board[next_r][next_c] > 0:
                    if board[next_r][next_c] > 1:
                        q.append((next_r, next_c))
                    board[next_r][next_c] = 0


def drop(board):
    """벽돌을 아래로 떨어뜨립니다."""
    for c in range(len(board[0])):
        bricks_in_col = []
        for r in range(len(board)):
            if board[r][c] > 0:
                bricks_in_col.append(board[r][c])

        for r in range(len(board) - 1, -1, -1):
            if bricks_in_col:
                board[r][c] = bricks_in_col.pop()
            else:
                board[r][c] = 0


def dfs(board, balls_left):
    """공을 떨어뜨릴 위치를 결정하는 백트래킹 함수입니다."""
    global min_bricks

    if balls_left == 0:
        count = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] > 0:
                    count += 1
        min_bricks = min(min_bricks, count)
        return

    # 가지치기: 남은 벽돌 수가 현재 최솟값보다 크면 더 이상 탐색하지 않습니다.
    current_bricks = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] > 0:
                current_bricks += 1

    if current_bricks == 0:
        min_bricks = 0
        return

    if current_bricks < min_bricks:
        min_bricks = current_bricks

    # 각 열에 공을 떨어뜨려보는 모든 경우의 수 탐색
    for c in range(len(board[0])):
        r = 0
        while r < len(board) and board[r][c] == 0:
            r += 1

        if r == len(board):
            dfs(board, balls_left - 1)
            continue

        temp_board = copy.deepcopy(board)
        bfs(temp_board, r, c)
        drop(temp_board)

        dfs(temp_board, balls_left - 1)


def solve():
    global min_bricks
    T = int(sys.stdin.readline().strip())
    for test_case in range(1, T + 1):
        N, W, H = map(int, sys.stdin.readline().strip().split())
        board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(H)]

        min_bricks = float('inf')
        dfs(board, N)

        print(f"#{test_case} {min_bricks}")


solve()