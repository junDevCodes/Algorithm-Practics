# SWEA 5174 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
노드 N을 루트로 하는 서브트리에 속한 노드의 개수 알아내는 프로그램

[입력]
0. TC
1. 간선 갯수, 타겟 노드
2. 간선 정보

[출력]
타겟 노드 하위 서브트리에 속한 노드 갯수

[알고리즘]
1. 노드 set 만들기
2. dfs를 통해 갯수 찾기 => 백트래킹

[복잡도]
- 시간: O()
- 공간: O()
"""


def dfs(tree, node):
    if node not in tree: #리프 노드 도달 시 1반환
        return 1

    count = 1
    for next_node in tree[node]:
        count += dfs(tree, next_node)

    return count


# T = int(sys.stdin.readline().strip())
T = int(input())

for test_case in range(1, T + 1):
    # edge_num, target_node = map(int, sys.stdin.readline().strip().split())
    edge_num, target_node = map(int, input().split())

    # edge_list = list(map(int, sys.stdin.readline().strip().split()))
    edge_list = list(map(int, input().split()))

    node_set = {}
    for idx in range(0, len(edge_list), 2):
        parent_node = edge_list[idx]
        child_node = edge_list[idx+1]
        if parent_node not in node_set:
            node_set[parent_node] = [child_node]
        else:
            node_set[parent_node].append(child_node)

    # print(node_set)
    # 로직
    result = dfs(node_set, target_node)

    # 출력 (SWEA 형식)
    print(f"#{test_case} {result}")
