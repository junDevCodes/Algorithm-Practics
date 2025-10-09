# SWEA 1795 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
N개의 집이 있다
1~N번까지의 번호를 붙일때 각 집에서 X번 집으로 모인다
각 집 -> X -> 각 집 의 비용이 최대인 집의 시간을 구하시오

[입력]
0. tc
1. node_num, edges_num, target_num
2. graph_info(s, e, w)

[출력]
1. N -> target_num -> N이 최대인 경우의 시간


[알고리즘]
1. 다익스트라로 해결 N -> T -> N 인경우마다 최대 시간 갱신

[복잡도]
- 시간: O()
- 공간: O()
"""
from collections import defaultdict
import heapq, math


def dijkstra(graph, start):
    distances[start][start] = 0
    min_heap = []
    heapq.heappush(min_heap, (0, start))

    while min_heap:
        c_distance, c_node = heapq.heappop(min_heap)
        if distances[start][c_node] < c_distance: continue

        for adj, weight in graph[c_node].items():
            distance = c_distance + weight
            if distance < distances[start][adj]:
                distances[start][adj] = distance
                heapq.heappush(min_heap, (distance, adj))

    return

T = int(input())

for test_case in range(1, T + 1):
    node_num, edges_num, target_num = map(int, input().split())
    graph_info = defaultdict(dict)
    distances = [[math.inf] * (node_num + 1) for _ in range(node_num + 1)]
    for _ in range(edges_num):
        s, e, w = map(int, input().split())
        graph_info[s][e] = w

    for node in range(1, node_num+1):
        dijkstra(graph_info, node)

    max_time = 0
    for s_node in range(1, node_num+1):
        time = distances[s_node][target_num] + distances[target_num][s_node]
        max_time = max(max_time, time)
    print(f"#{test_case} {max_time}")
