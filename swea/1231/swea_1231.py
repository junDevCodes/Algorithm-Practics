# SWEA 1231 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
주어진 트리를 in-order 형식으로 순회했을 때 나오는 단어를 출력하라
완전 이진트리로 주어짐

[입력]
1. 단어 길이
2. 노드 정보

[출력]
1. in-order 방식 단어 출력

[알고리즘]
1. 입력 = 리스트로 받고 len으로 보기
2. in-order 방식으로 단어 리스트 저장

[복잡도]
- 시간: O()
- 공간: O()
"""


def inorder_dfs(tree, node):
    global result_word_list, node_list

    if node not in tree: #리프 노드인 경우 append
        result_word_list.append(node_list[node])
        return

    left_child = tree[node][0]
    inorder_dfs(tree, left_child)

    result_word_list.append(node_list[node])

    if len(tree[node]) > 1:
        right_child = tree[node][1]
        inorder_dfs(tree, right_child)


T = 10

for test_case in range(1, T + 1):
    # word_len = int(sys.stdin.readline().strip())
    word_len = int(input())
    result_word_list = []
    node_list = ["" for _ in range(word_len+1)]
    node_set = {}

    for _ in range(word_len):
        # input_list = list(map(str, sys.stdin.readline().strip().split()))
        input_list = list(map(str, input().split()))

        node_idx = int(input_list[0])
        node_val = input_list[1]

        if len(input_list) > 2:  # 자식 노드가 있을 때
            for child in input_list[2:]:
                if node_idx not in node_set:
                    node_set[node_idx] = []
                node_set[node_idx].append(int(child))

        node_list[node_idx] = node_val

    # print(node_list)
    # print(node_set)
    # 로직
    inorder_dfs(node_set, 1)

    # 출력 (SWEA 형식)
    print(f"#{test_case} {''.join(result_word_list)}")
