# SWEA 22380 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
기초 다익스트라
한 지점에서 다른 한 지점까지 이동하는 최소 비용을 제작해야한다
정점은 0 ~ node-1 번까지 존재한다

[입력]
0. TC
1. node_num, edges_num
2. edges_info(s, e, w)

[출력]
최소 비용 / impossible

[알고리즘]
1. 
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""
from collections import defaultdict
import heapq, math


def dijkstra(graph, start):
    distances = {v: math.inf for v in range(node_num)}
    distances[start] = 0
    min_heap = []
    heapq.heappush(min_heap, [0, start])

    while min_heap:
        c_distance, c_node = heapq.heappop(min_heap)

        if distances[c_node] < c_distance: continue

        for adj, weight in graph[c_node].items():
            distance = c_distance + weight
            if distance < distances[adj]:
                distances[adj] = distance
                heapq.heappush(min_heap, [distance, adj])

    return distances

T = int(input())

for test_case in range(1, T + 1):
    node_num, edges_num = map(int, input().split())
    edges_info = defaultdict(dict)
    for _ in range(edges_num):
        s, e, w = map(int, input().split())
        edges_info[s][e] = w

    result = dijkstra(edges_info, 0)
    if result[node_num-1] != math.inf:
        print(f"#{test_case} {result[node_num-1]}")
    else:
        print(f"#{test_case} impossible")
