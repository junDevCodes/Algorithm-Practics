# SWEA 18581 문제 풀이
# import sys
# from pathlib import Path

# 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
트리 노드의 총 수 V
V-1개의 간선이 나열된다
항상 부모 - 자식

[입력]
1. 노드 총 수
2. 간선 정보

[출력]
1. 전위 순회 정점 번호
2. 중위 순회 정점 번호
3. 후위 순회 정점 번호

[알고리즘]
1. dictionary 통한 인접리스트
2. dfs 로직으로 출력

[복잡도]
- 시간: O()
- 공간: O()
"""


def preOrder(tree, node):
    if node not in tree:
        print(node, end=" ")
        return

    print(node, end=" ")

    left_node = tree[node][0]
    preOrder(tree, left_node)

    if len(tree[node]) > 1:
        right_node = tree[node][1]
        preOrder(tree, right_node)


def inOrder(tree, node):
    if node not in tree:
        print(node, end=" ")
        return

    left_node = tree[node][0]
    inOrder(tree, left_node)

    print(node, end=" ")

    if len(tree[node]) > 1:
        right_node = tree[node][1]
        inOrder(tree, right_node)


def postOrder(tree, node):
    if node not in tree:
        print(node, end=" ")
        return

    left_node = tree[node][0]
    postOrder(tree, left_node)

    if len(tree[node]) > 1:
        right_node = tree[node][1]
        postOrder(tree, right_node)

    print(node, end=" ")


# 입력
node_num = int(input())
edge_list = list(map(int, input().split()))

node_dict = {}
isParent = set([])

for idx in range(0, len(edge_list), 2):
    parent_node = edge_list[idx]
    child_node = edge_list[idx+1]
    if parent_node not in node_dict:
        node_dict[parent_node] = [child_node]
    else:
        node_dict[parent_node].append(child_node)
    if child_node not in isParent:
        isParent.add(child_node)
# print(node_dict)
# print(isParent)

for root in range(1, node_num):
    if root not in isParent:
        root_node = root
        break

preOrder(node_dict, root_node)
print("")
inOrder(node_dict, root_node)
print("")
postOrder(node_dict, root_node)

