# SWEA 5177 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
항상 완전 이진트리 유지를 위해 마지막 노드 뒤에 새 노드를 추가한다.
부모노드가 새로 추가된 자식노드보다 큰 경우 그 위치를 서로 바꾼다

[입력]
0. tc
1. node_num
2. node_info

[출력]
가장 마지막 노드의 조상 노드에 저장된 정수의 합

[알고리즘]
1. 리스트를 활용한 이진 트리 구현
2. 부모노드와 비교 후 위치 변경

[복잡도]
- 시간: O()
- 공간: O()
"""
from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    node_num = int(input())
    b_tree = [0] * (node_num + 1)

    node_info = deque(list((map(int, input().split()))))
    c_idx = 1

    while node_info:
        c_node = node_info.popleft()
        b_tree[c_idx] = c_node

        temp_idx = c_idx
        while temp_idx > 1:
            p_idx = temp_idx // 2
            if b_tree[p_idx] > b_tree[temp_idx]:
                b_tree[p_idx], b_tree[temp_idx] = b_tree[temp_idx], b_tree[p_idx]
                temp_idx = p_idx
            else:
                break
        c_idx += 1

    r_idx = node_num
    result = 0
    while r_idx > 1:
        r_idx //= 2
        result += b_tree[r_idx]

    print(f"#{test_case} {result}")
