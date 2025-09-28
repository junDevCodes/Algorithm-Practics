# SWEA 4871 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
V개 이내의 노드를, E개의 간선으로 연결한 방향성 그래프
특정한 두 개의 노드가 경로에 존재하는지 확인하는 프로그램

[입력]
0. TC
1. vertex_num, edge_num
2. edge_info_list
3. target_edge

[출력]
1. connected

[알고리즘]
1. 
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""

from collections import defaultdict


def dfs(graph, node, target_v):
    global connected

    visited.add(node)

    if node == target_v:
        connected = 1
        return

    if node in graph:
        for next_node in graph[node]:
            if next_node in visited: continue
            if not connected:
                dfs(graph, next_node, target_v)


# T = int(sys.stdin.readline().strip())
T = int(input())

for test_case in range(1, T + 1):
    # 입력
    # v_num, e_num = map(int, sys.stdin.readline().strip().split())
    v_num, e_num = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(e_num):
        # s_v, e_v = map(int, sys.stdin.readline().strip().split())
        s_v, e_v = map(int, input().split())
        graph[s_v].append(e_v)
    # print(graph)

    # target_s_v, target_e_v = map(int, sys.stdin.readline().strip().split())
    target_s_v, target_e_v = map(int, input().split())
    # 로직
    connected = 0
    visited = set()
    dfs(graph, target_s_v, target_e_v)
    
    # 출력 (SWEA 형식)
    print(f"#{test_case} {connected}")
