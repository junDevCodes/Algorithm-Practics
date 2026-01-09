"""
[문제]
서로 다른 N개의 물건
일부 물건 쌍에 대해 양팔 저울 측정 결과표
각 물건에 대해 비교 결과를 알 수 없는 물건의 개수를 출력하는 프로그램

[입력]
1. 물건의 개수
2. 물건 측정 쌍의 개수
3. 측정 결과표

[출력]
1. 1 ~ N까지의 물건마다 비교 결과를 알 수 없는 물건의 개수

[로직]
1. dfs_heavy, dfs_light로 분리
2. 각각의 dfs를 돌며 자기 제외 노드 갯수 세기
3. 전체 물건 수 - dfs_heavy + dfs_light

[예시 입력]
6
5
1 2
2 3
3 4
5 4
6 5

[예시 출력]
2
2
2
0
3
3
"""


def dfs(graph, start_node, visited):
    count = 1  # 시작 노드 자신을 포함하여 1로 시작
    visited[start_node] = True

    for next_node in graph[start_node]:
        if not visited[next_node]:
            count += dfs(graph, next_node, visited)
    return count


item_num = int(input()) # 전체 물건의 개수
compare_num = int(input()) # 측정 쌍의 개수

heavier_graph = [[] for _ in range(item_num + 1)]
lighter_graph = [[] for _ in range(item_num + 1)]

for _ in range(compare_num):
    a, b = map(int, input().split())
    heavier_graph[a].append(b)  # a는 b보다 무겁다
    lighter_graph[b].append(a)  # b는 a보다 가볍다

for i in range(1, item_num + 1):
    visited_heavy = [False] * (item_num + 1)
    heavier_count = dfs(lighter_graph, i, visited_heavy) - 1  # -1은 자기 자신 제외

    visited_light = [False] * (item_num + 1)
    lighter_count = dfs(heavier_graph, i, visited_light) - 1  # -1은 자기 자신 제외

    total_known = heavier_count + lighter_count

    unknown_count = (item_num - 1) - total_known
    print(unknown_count)