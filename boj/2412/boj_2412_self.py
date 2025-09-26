from collections import deque


def solve():
    spot_num, top = map(int, input().split())

    spot_list = {}
    for _ in range(spot_num):
        spot_x, spot_y = map(int, input().split())
        if spot_y not in spot_list:
            spot_list[spot_y] = []
        spot_list[spot_y].append(spot_x)
    # print(spot_list)

    queue = deque([(0, 0, 0)])
    visited = set((0, 0))

    while queue:
        cx, cy, time = queue.popleft()

        if cy == top:
            print(time)
            return

        for dy in range(-2, 3):
            ny = cy + dy
            if ny in spot_list:
                for nx in spot_list[ny]:
                    if abs(nx - cx) <= 2 and (nx, ny) not in visited:
                        queue.append((nx, ny, time + 1))
                        visited.add((nx, ny))

    print(-1)
    return


solve()
