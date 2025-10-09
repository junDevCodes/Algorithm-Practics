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
1. 플로이드 워셜로 전체 비용 계산
2. N -> target -> N의 비용이 제일 큰 정점의 시간 출력

[복잡도]
- 시간: O()
- 공간: O()

[review]
시간복잡도 O(n^3) 때문에 그래프가 커지면 시간이 기하급수적으로 늘어나기 때문에 사용 X
"""
def floyd_warshall(graph):
    v = len(graph)

    for via_node in range(v):
        for start_node in range(v):
            if start_node == via_node: continue

            for end_node in range(v):
                if graph[start_node][via_node] + graph[via_node][end_node] < graph[start_node][end_node]: # 경유해서 가는게 직항보다 짧다면
                    graph[start_node][end_node] = graph[start_node][via_node] + graph[via_node][end_node] # 최소 경로 갱신

    for i in range(v):
        if graph[i][i] < 0: #자기 자신을 가는 경로가 0 이하라면 음수 사이클 검출
            print("음수 사이클 검출")
            break

    return graph
T = int(input())


for test_case in range(1, T + 1):
    node_num, edges_num, target_num = map(int, input().split())
    graph_info = [[float("inf")] * node_num for _ in range(node_num)]
    for idx in range(node_num):
        graph_info[idx][idx] = 0
    for _ in range(edges_num):
        s, e, w = map(int, input().split())
        graph_info[s-1][e-1] = w

    res = floyd_warshall(graph_info)
    max_time = 0
    target_idx = target_num - 1
    for node in range(node_num):
        if node == target_idx: continue
        max_time = max(max_time, res[node][target_idx] + res[target_idx][node])

    print(f"#{test_case} {max_time}")
