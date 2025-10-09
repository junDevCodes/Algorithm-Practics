# SWEA 5251 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
기본 다익스트라

[입력]
0. TC
1. node_num, vertex_num
2. graph_info(s, e, w)

[출력]
0 ~ node_num 까지의 최소 비용

[알고리즘]
1. 다익스트라
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""
from collections import defaultdict
import heapq, math


def dijkstra(graph, start):
    distances = {v: math.inf for v in range(node_num + 1)}
    distances[start] = 0
    min_heap = []
    heapq.heappush(min_heap, (0, start))

    while min_heap:
        c_distance, c_node = heapq.heappop(min_heap)

        if distances[c_node] < c_distance: continue

        for adj, weight in graph[c_node].items():
            distance = c_distance + weight
            if distance < distances[adj]:
                distances[adj] = distance
                heapq.heappush(min_heap, (distance, adj))

    return distances

T = int(input())

for test_case in range(1, T + 1):
    node_num, vertex_num = map(int, input().split())
    graph_info = defaultdict(dict)
    for _ in range(vertex_num):
        s, e, w = map(int, input().split())
        graph_info[s][e] = w

    res = dijkstra(graph_info, 0)

    print(f"#{test_case} {res[node_num]}")
