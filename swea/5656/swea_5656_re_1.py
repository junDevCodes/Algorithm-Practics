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

def check_block(board):
    return sum(1 for row in board for cell in row if cell > 0)


def copy_board(board):
    return [row[:] for row in board]


def bfs(board, r, c):
    queue = deque([(r, c, board[r][c])])
    board[r][c] = 0

    d_list = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while queue:
        c_row, c_col, power = queue.popleft()

        if power <= 0: continue # 확장하지 않는 경우 다음 셀 탐색

        for d_row, d_col in d_list: # 상하좌우 방향별 탐색
            for c_power in range(1, power): # 최대 power별 탐색

                n_row, n_col = c_row + d_row * c_power, c_col + d_col * c_power

                if n_row < 0 or n_col < 0 or n_row >= len(board) or n_col >= len(board[0]):
                    # 맵 범위를 넘어간 경우 이상 power 모두 처리 불가
                    break
                if board[n_row][n_col] > 1:
                    queue.append((n_row, n_col, board[n_row][n_col]))  # 맵 내부인 경우 queue append
                board[n_row][n_col] = 0 # 맵 초기화



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


def dfs(board, ball_left):
    global min_block

    if ball_left == 0: # 남은 공 횟수가 없으면 최소 블럭 반환
        min_block = min(min_block, check_block(board))
        return

    current_block = check_block(board)
    if current_block == 0: # 남아있는 블럭이 없으면 최소 블럭 반환
        min_block = 0
        return

    if min_block == 0: # 이미 최소 블럭이 0이라면 반환
        return

    W = len(board[0])
    H = len(board)

    for c in range(W): # 세로줄 먼저 탐색
        r = 0
        while r < H and board[r][c] == 0:
            # board 범위 벗어나지 않으면서 0인 경우를 제외하고
            r += 1

        if r == H: continue # board 끝에 다다른 경우 다음 세로줄 탐색

        # 여기까지 통과 된 경우 board 끝이 아니고 값이 0이 아닌 가장 위의 값
        temp_board = copy_board(board)
        bfs(temp_board, r, c)
        drop(temp_board)

        dfs(temp_board, ball_left-1)


def solve():
    global min_block

    T = int(input())

    for test_case in range(1, T + 1):
        N, W, H = map(int, input().split())

        board = [list(map(int, input().split())) for _ in range(H)]
        min_block = float("inf")

        dfs(board, N)

        print(f"#{test_case} {min_block}")


solve()
