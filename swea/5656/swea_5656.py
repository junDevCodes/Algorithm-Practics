# SWEA 5656 문제 풀이
import sys
from pathlib import Path

# 로컬 테스트용 파일 입력 설정
BASE_DIR = Path(__file__).resolve().parent
sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

from collections import deque

min_bricks = float('inf')


def bfs(board, r, c):
    """BFS를 사용하여 벽돌을 터뜨리고 연쇄 폭발을 시뮬레이션합니다."""
    H, W = len(board), len(board[0])
    q = deque([(r, c, board[r][c])])  # (row, col, power) 저장
    board[r][c] = 0
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        cur_r, cur_c, power = q.popleft()  # 각 벽돌의 power 사용

        for dr, dc in delta:
            for i in range(1, power):  # power만큼 범위 확장
                nr, nc = cur_r + dr * i, cur_c + dc * i

                if 0 <= nr < H and 0 <= nc < W and board[nr][nc] > 0:
                    if board[nr][nc] > 1:
                        q.append((nr, nc, board[nr][nc]))
                    board[nr][nc] = 0


def drop(board):
    """벽돌을 아래로 떨어뜨립니다. (최적화)"""
    H, W = len(board), len(board[0])

    for c in range(W):
        # 아래에서부터 채워넣기
        write_idx = H - 1
        for r in range(H - 1, -1, -1):
            if board[r][c] > 0:
                board[write_idx][c] = board[r][c]
                if write_idx != r:
                    board[r][c] = 0
                write_idx -= 1

        # 나머지는 0으로
        while write_idx >= 0:
            board[write_idx][c] = 0
            write_idx -= 1


def count_bricks(board):
    """남은 벽돌 개수를 셉니다."""
    return sum(1 for row in board for cell in row if cell > 0)


def copy_board(board):
    """보드를 복사합니다. (deepcopy보다 빠름)"""
    return [row[:] for row in board]


def dfs(board, balls_left):
    """공을 떨어뜨릴 위치를 결정하는 백트래킹 함수입니다."""
    global min_bricks

    # 종료 조건: 공을 다 사용함
    if balls_left == 0:
        min_bricks = min(min_bricks, count_bricks(board))
        return

    # 가지치기: 현재 벽돌 개수가 이미 최솟값보다 크거나 같으면 중단
    current_bricks = count_bricks(board)
    if current_bricks == 0:
        min_bricks = 0
        return

    if min_bricks == 0:
        return

    W = len(board[0])
    H = len(board)

    # 각 열에 공을 떨어뜨려보는 모든 경우의 수 탐색
    for c in range(W):
        # 해당 열에서 가장 위의 벽돌 찾기
        r = 0
        while r < H and board[r][c] == 0:
            r += 1

        # 빈 열이면 스킵 (불필요한 재귀 방지)
        if r == H:
            continue

        # 보드 복사 및 시뮬레이션
        temp_board = copy_board(board)
        bfs(temp_board, r, c)
        drop(temp_board)

        # 재귀 호출
        dfs(temp_board, balls_left - 1)

        # 조기 종료: 최솟값이 0이면 더 탐색할 필요 없음
        if min_bricks == 0:
            return


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