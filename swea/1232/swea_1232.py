# SWEA 1232 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
사직연산 표현을 이진트리로 한것
임의의 정점에 연산자가 있다면 해당 트리의 왼쪽 서브트리 결과와 오른쪽 서브트리 결과를 연산하는것
총 계산 결과 출력 소수점 없이 정수로

[입력]
정점이 정수면 정점 번호와 양의 정수
정점이 연산자면 정점 번호, 연산자, 해당 정점의 왼쪽, 오른쪽 자식의 정점번호 주어짐
루트 정점은 항상 1

[출력]


[알고리즘]
1. 
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""


def dfs_cal(tree, node):
    global node_list

    if node not in tree: # 리프노드면 값 반환
        return node_list[node]

    if node_list[node] == '+':
        return dfs_cal(tree, tree[node][0]) + dfs_cal(tree, tree[node][1])
    elif node_list[node] == '-':
        return dfs_cal(tree, tree[node][0]) - dfs_cal(tree, tree[node][1])
    elif node_list[node] == '*':
        return dfs_cal(tree, tree[node][0]) * dfs_cal(tree, tree[node][1])
    elif node_list[node] == '/':
        return dfs_cal(tree, tree[node][0]) // dfs_cal(tree, tree[node][1])


T = 10

for test_case in range(1, T + 1):
    # node_num = int(sys.stdin.readline().strip())
    node_num = int(input())
    node_list = [0] * (node_num + 1)
    node_set = {}

    for _ in range(node_num):
        # input_list = list(map(str, sys.stdin.readline().strip().split()))
        input_list = list(map(str, input().split()))

        node_idx = int(input_list[0])
        if len(input_list) > 2: # 연산자 입력이라면
            node_val = input_list[1]
            left_child_idx, right_child_idx = input_list[2], input_list[3]
            node_set[node_idx] = [int(left_child_idx), int(right_child_idx)]
        else:
            node_val = int(input_list[1])

        node_list[node_idx] = node_val

    result = dfs_cal(node_set, 1)

    print(f"#{test_case} {result}")
    # print(node_list)
    # print(node_set)
