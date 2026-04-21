from collections import deque


def count_left(grid, W, H):
    return sum(1 for r in range(H) for c in range(W) if grid[r][c] > 0)


def top_block(grid, c, H):
    for r in range(H):
        if grid[r][c] > 0:
            return r

    return -1


def block_explore(grid, sr, sc, W, H):
    q = deque([(sr, sc, grid[sr][sc])])
    grid[sr][sc] = 0

    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]

    while q:
        (cr, cc, cp) = q.popleft()
        grid[cr][cc] = 0


        for idx in range(4):
            for np in range(1, cp):
                nr, nc = cr + (dr[idx] * np), cc + (dc[idx] * np)
                if nr < 0 or nc < 0 or nr >= H or nc >= W: continue

                if grid[nr][nc] > 0:
                    q.append((nr, nc, grid[nr][nc]))
                    grid[nr][nc] = 0


def drop_block(grid, W, H):
    stack = deque([])
    for c in range(W):
        window_r = H-1
        for r in range(H-1, -1, -1):
            if grid[r][c] > 0:
                stack.append(grid[r][c])
                grid[r][c] = 0

        while stack:
            grid[window_r][c] = stack.popleft()
            window_r -= 1


def solve(depth, grid, N, W, H):
    global answer

    cnt = count_left(grid, W, H)

    if cnt == 0:
        answer = 0
        return

    if depth == N:
        answer = min(answer, cnt)
        return

    for c in range(W):
        top_r = top_block(grid, c, H)
        if top_r == -1: continue

        copy_grid = [row[:] for row in grid]
        block_explore(copy_grid, top_r, c, W, H)
        drop_block(copy_grid, W, H)
        solve(depth+1, copy_grid, N, W, H)

T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]

    answer = float("inf")
    solve(0, grid, N, W, H)
    print(f"#{tc} {answer}")