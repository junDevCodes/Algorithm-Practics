# SWEA 5178 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
완전 이진트리
리프노드에 1000이하의 자연수
리프노드 제외 = 자식 노드의 합 저장

루트가 1번
같은 단계 왼쪽에서 오른 쪽으로 증가
단계가 꽉 차면 다음 단계의 왼쪽
1~N 까지 빠지는 노드 번호 없음
리프 노드의 번호와 저장된 값이 주어지면 나머지 노드에 자식노드 값의 합 저장 후
지정한 노드 번호에 저장된 값 출력

[입력]
0. TC
1. 노드 갯수, 리프노드 갯수, 값 출력 노드 번호

[출력]
1. 해당하는 노드 번호의 값

[알고리즘]
1. 완전이진트리 => 레벨별 최대 갯수 고정
2. 리스트를 통한 공식 사용 왼쪽 자식 노드 = 부모 인덱스 * 2, 오른쪽 자식 노드 = 부모 인덱스 * 2 + 1
3. 리스트는 노드 갯수 + 1로 지정
4. 노드 번호인덱스에 값넣고 //2 한거에 값 + 하는걸로
5. 인덱스 뒤부터 전체 순회하면 겹치지 않고 가능
6. 가지치기는 타겟넘버 나오면 그냥 출력 후 반복 종료

[복잡도]
- 시간: O()
- 공간: O()
"""

# T = int(sys.stdin.readline().strip())
T = int(input())

for test_case in range(1, T + 1):
    # node_num, leaf_node_num, target_node = map(int, sys.stdin.readline().strip().split())
    node_num, leaf_node_num, target_node = map(int, input().split())

    node_list = [0] * (node_num+1)

    for _ in range(leaf_node_num):
        # node_idx, node_val = map(int, sys.stdin.readline().strip().split())
        node_idx, node_val = map(int, input().split())
        node_list[node_idx] = node_val

    result = 0
    for idx in range(node_num, -1, -1):
        if idx == target_node:
            result = node_list[idx]
            break

        node_list[idx//2] += node_list[idx]

    print(f"#{test_case} {result}")
