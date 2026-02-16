from collections import deque


def check_board(board):
    return sum(1 for row in board for cell in row if cell > 0)


def copy_board(board):
    return [row[:] for row in board]


def bfs(r, c, board):
    W, H = len(board[0]), len(board)
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 하, 우, 상, 좌

    q = deque([(r, c, board[r][c])])
    board[r][c] = 0

    while q:
        cur_r, cur_c, cur_val = q.popleft()
        board[cur_r][cur_c] = 0

        if cur_val <= 1:
            continue

        for dx, dy in dxy:
            for val in range(1, cur_val):
                nx = cur_c + (dx * val)
                ny = cur_r + (dy * val)

                if nx < 0 or nx >= W or ny < 0 or ny >= H:
                    continue

                if board[ny][nx] > 1:
                    q.append([ny, nx, board[ny][nx]])
                board[ny][nx] = 0


def drop(board):
    W, H = len(board[0]), len(board)

    for c in range(W):
        cur = H - 1
        for r in range(H - 1, -1, -1):
            if board[r][c] > 0:
                board[cur][c] = board[r][c]
                cur -= 1

        while cur >= 0:
            board[cur][c] = 0
            cur -= 1


def dfs(board, ball_left):
    global min_block
    W, H = len(board[0]), len(board)
    cur_block = check_board(board)

    if ball_left == 0:
        min_block = min(min_block, cur_block)
        return

    if cur_block == 0:
        min_block = min(min_block, cur_block)
        return

    for c in range(W):
        for r in range(H):
            if board[r][c] <= 0:
                continue

            temp_board = copy_board(board)
            bfs(r, c, temp_board)
            drop(temp_board)
            dfs(temp_board, ball_left - 1)
            break

    return


def solve():
    global min_block
    T = int(input())
    for tc in range(1, T + 1):

        N, W, H = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(H)]

        min_block = float("inf")

        dfs(board, N)

        print(f"#{tc} {min_block}")
    return


solve()
