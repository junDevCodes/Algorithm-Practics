# import sys
#
# sys.stdin = open('sample_input.txt', 'r')


def check_rail(rail_list, rail_len, map_size):
    visited = [False] * map_size

    for idx in range(len(rail_list) - 1):
        diff = rail_list[idx] - rail_list[idx + 1]

        if abs(diff) > 1:
            return 0

        if diff == 1: # 내리막길일때
            for check_idx in range(rail_len):
                if (idx + check_idx + 1 >= len(rail_list)) or (rail_list[idx + 1] != rail_list[idx + check_idx + 1]) \
                        or visited[idx + check_idx + 1]:
                    return 0
                visited[idx + check_idx + 1] = True

        if diff == -1: # 오르막길일때
            for check_idx in range(rail_len):
                if idx - check_idx < 0 or rail_list[idx] != rail_list[idx - check_idx] or visited[idx - check_idx]:
                    return 0
                visited[idx - check_idx] = True

    return 1


def solve():
    # T = int(sys.stdin.readline().strip())
    T = int(input())
    for tc in range(1, T + 1):
        # map_size, rail_len = map(int, sys.stdin.readline().strip().split())
        map_size, rail_len = map(int, input().split())
        # map_info = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(map_size)]
        map_info = [list(map(int, input().split())) for _ in range(map_size)]
        map_rotate = list(zip(*map_info))
        total_count = 0

        for row in range(map_size):
            total_count += check_rail(map_info[row], rail_len, map_size)
            total_count += check_rail(map_rotate[row], rail_len, map_size)

        print(f"#{tc} {total_count}")
    pass


solve()
