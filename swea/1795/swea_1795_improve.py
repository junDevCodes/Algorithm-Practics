# SWEA 1795 문제 풀이
import sys
from pathlib import Path

# 로컬 테스트용 파일 입력 설정
BASE_DIR = Path(__file__).resolve().parent
sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

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

import heapq


def dijkstra(start, graph):
    distances = [INF] * (node_num + 1)
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        dist, cur = heapq.heappop(queue)
        if distances[cur] < dist:
            continue
        for nbr, nbr_dist in graph[cur]:
            next_dist = dist + nbr_dist
            if distances[nbr] > next_dist:
                distances[nbr] = next_dist
                heapq.heappush(queue, (next_dist, nbr))
    return distances


INF = float('inf')

T = int(input())
for t in range(1, T+1):
    node_num, edges_num, target_num = map(int, input().split())

    graph = {i: [] for i in range(1, node_num + 1)}
    reversed_graph = {i: [] for i in range(1, node_num + 1)}

    for _ in range(edges_num):
        x, y, c = map(int, input().split())
        graph[x].append((y, c))
        reversed_graph[y].append((x, c))

    res_dist = dijkstra(target_num, graph)
    reversed_dist = dijkstra(target_num, reversed_graph)
    print(f'#{t}', max([res_dist[i] + reversed_dist[i] for i in range(1, node_num + 1)]))
