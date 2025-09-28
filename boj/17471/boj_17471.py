import sys
from collections import deque
from itertools import combinations


def check_connection(selected_areas, area_info, people_in_area):
    if not selected_areas:
        return False, 0

    start_node = list(selected_areas)[0]
    queue = deque([start_node])
    visited = {start_node}
    count = 1
    total_people = people_in_area[start_node]

    while queue:
        current_node = queue.popleft()

        for neighbor in area_info[current_node]:
            if neighbor in selected_areas and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                count += 1
                total_people += people_in_area[neighbor]

    return count == len(selected_areas), total_people


def solve():
    area_num = int(sys.stdin.readline().strip())
    people_list = list(map(int, sys.stdin.readline().strip().split()))
    people_in_area = {i: people_list[i - 1] for i in range(1, area_num + 1)}

    area_info = {i: [] for i in range(1, area_num + 1)}
    for idx in range(1, area_num + 1):
        neighbor_info = list(map(int, sys.stdin.readline().strip().split()))
        area_info[idx] = neighbor_info[1:]

    min_diff = float('inf')
    all_areas = set(range(1, area_num + 1))
    # print(all_areas)

    # itertools.combinations를 사용하여 모든 조합 생성
    for i in range(1, area_num // 2 + 1):
        for group_A in combinations(all_areas, i):
            group_A = set(group_A)
            group_B = all_areas - group_A
            print(group_A, group_B)

            is_A_connected, people_A = check_connection(group_A, area_info, people_in_area)
            # print(f"A: {is_A_connected, people_A}")
            is_B_connected, people_B = check_connection(group_B, area_info, people_in_area)
            # print(f"B: {is_B_connected, people_B}")

            if is_A_connected and is_B_connected:
                diff = abs(people_A - people_B)
                min_diff = min(min_diff, diff)

    if min_diff == float('inf'):
        print(-1)
    else:
        print(min_diff)


solve()