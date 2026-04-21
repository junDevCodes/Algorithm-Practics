from collections import deque


def count_left_block(grid, W, H):
    return sum(1 for r in range(H) for c in range(W) if grid[r][c] >= 1)


def find_top_block(grid, c, H):
    for r in range(H):
        if grid[r][c] >= 1:
            return r

    return -1


def block_explore(grid, r, c, v, W, H):
    q = deque([(r, c, v)])
    grid[r][c] = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        (cr, cc, cv) = q.popleft()
        for d in range(4):
            for cp in range(1, cv):
                nr, nc = cr + (dr[d] * cp), cc + (dc[d] * cp)
                if nr < 0 or nc < 0 or nr >= H or nc >= W: continue
                nv = grid[nr][nc]
                if nv > 1:
                    q.append((nr, nc, nv))
                grid[nr][nc] = 0


def drop_block(grid, W, H):
    for c in range(W):
        temp = []
        for r in range(H - 1, -1, -1):
            if grid[r][c] > 0:
                temp.append(grid[r][c])
                grid[r][c] = 0

        for r in range(H - 1, H - 1 - len(temp), -1):
            grid[r][c] = temp[H - 1 - r]


def solve(depth, grid, N, W, H):
    global answer

    cnt = count_left_block(grid, W, H)

    if cnt == 0:
        answer = 0
        return

    if depth == N:
        answer = min(cnt, answer)
        return

    if answer == 0:
        return

    for c in range(W):
        top_r = find_top_block(grid, c, H)
        if top_r == -1: continue

        copy_grid = [row[:] for row in grid]
        block_explore(copy_grid, top_r, c, copy_grid[top_r][c], W, H)
        drop_block(copy_grid, W, H)
        solve(depth + 1, copy_grid, N, W, H)


def main():
    global answer
    T = int(input())
    for tc in range(1, T + 1):
        N, W, H = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(H)]
        answer = float("inf")

        solve(0, grid, N, W, H)

        print(f"#{tc} {answer}")


global answer
main()