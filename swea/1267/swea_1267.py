# SWEA 1267 문제 풀이
import sys

# 로컬 테스트용 파일 입력 설정
sys.stdin = open('sample_input.txt', 'r', encoding='utf-8')

"""
[문제 설명]
사전작업이 필요한 간선 그래프가 주어진다
정점의 갯수와, 간선의 갯수가 주어진다

[입력]
1. 정점의 갯수, 간선의 갯수
2. 연결 정보

[출력]
1. 작업 순서

[알고리즘]
1. 정점 dict 생성, 자신을 잇는 간선 정보를 넣는다
2. dict item이 없는거부터 dfs 돌림
3. item이 visited에 없다면 백트래킹

[복잡도]

"""


def dfs_topological_sort(graph, node, visited, result):
    visited[node] = True

    # 현재 노드의 다음 노드(자식 노드)들을 순회
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs_topological_sort(graph, next_node, visited, result)

    # 모든 자식 노드 방문 후, 현재 노드를 결과 리스트의 맨 앞에 추가
    result.append(node)


def solve():
    T = 10
    for test_case in range(1, T + 1):
        V, E = map(int, sys.stdin.readline().strip().split())
        edges = list(map(int, sys.stdin.readline().strip().split()))

        # 1. 그래프 구성
        graph = {i: [] for i in range(1, V + 1)}

        for i in range(0, E * 2, 2):
            u, v = edges[i], edges[i + 1]
            graph[u].append(v)  # u -> v 관계를 그래프에 저장
        # print(graph)

        # 2. 진입 차수 계산
        in_degree = {i: 0 for i in range(1, V + 1)}
        for node in graph:
            for neighbor in graph[node]:
                in_degree[neighbor] += 1
        print(in_degree)

        # 3. 위상 정렬 실행
        visited = {i: False for i in range(1, V + 1)}
        result = []

        # 진입 차수가 0인 노드부터 DFS 시작
        for node in range(1, V + 1):
            if in_degree[node] == 0 and not visited[node]:
                dfs_topological_sort(graph, node, visited, result)

        # DFS로 구한 순서는 역순이므로, 뒤집어서 출력
        result.reverse()

        # print(f"#{test_case} {' '.join(map(str, result))}")


solve()
