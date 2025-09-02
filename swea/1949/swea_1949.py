# import sys
import copy

# sys.stdin = open('sample_input.txt', 'r', encoding='utf-8')

# 전역 변수 설정
max_length = 0
delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def dfs(map_info, current_row, current_col, can_dig, max_dig, map_size, visited, length):
    global max_length
    max_length = max(max_length, length)

    visited[current_row][current_col] = True

    for d_row, d_col in delta:
        next_row, next_col = current_row + d_row, current_col + d_col

        if 0 <= next_row < map_size and 0 <= next_col < map_size and not visited[next_row][next_col]:

            if map_info[next_row][next_col] < map_info[current_row][current_col]:
                dfs(map_info, next_row, next_col, can_dig, max_dig, map_size, visited, length + 1)

            elif can_dig:
                for dig in range(1, max_dig + 1):

                    if map_info[next_row][next_col] - dig < map_info[current_row][current_col]:

                        temp_map = copy.deepcopy(map_info)
                        temp_map[next_row][next_col] -= dig

                        dfs(temp_map, next_row, next_col, False, max_dig, map_size, visited, length + 1)

    visited[current_row][current_col] = False


def solve():
    # T = int(sys.stdin.readline().strip())
    T = int(input())

    for tc in range(1, T + 1):
        # mnt_size, max_dig = map(int, sys.stdin.readline().strip().split())
        mnt_size, max_dig = map(int, input().split())
        # mnt_info = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(mnt_size)]
        mnt_info = [list(map(int, input().split())) for _ in range(mnt_size)]

        max_val = 0
        for mnt in mnt_info:
            max_val = max(max_val, max(mnt))

        high_loc = []
        for row in range(mnt_size):
            for col in range(mnt_size):
                if mnt_info[row][col] == max_val:
                    high_loc.append((row, col))

        global max_length
        max_length = 0

        for current_row, current_col in high_loc:
            visited = [[False] * mnt_size for _ in range(mnt_size)]
            dfs(mnt_info, current_row, current_col, True, max_dig, mnt_size, visited, 1)

        print(f"#{tc} {max_length}")


solve()
