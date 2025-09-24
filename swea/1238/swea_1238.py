# SWEA 1238 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
비상연락망 그래프가 주어질 때 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람을 구하는 함수를 작성하시오

[입력]
0. TC = 10
1. data_len, start_node

[출력]
가장 나중에 연락을 받게되는 사람 중 번호가 가장 큰 사람

[알고리즘]
1. 가장 나중에 연락을 받는다 => 연락을 못받는다 / 연락을 늦게 받는다 두가지 경우 존대
2. bfs통해 동시 visited 처리
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""
from collections import defaultdict, deque


def bfs(data, visit, s_node):
    queue = deque([(s_node, 1)])
    visit[s_node] = True

    while queue:
        c_node, rank = queue.popleft()
        for node in data[c_node]:
            if not visit[node]:
                queue.append((node, rank+1))
                visit[node] = rank+1
                last_rank = rank+1

    last_node_list = [node for node, value in visit.items() if value == last_rank]
    last_node_list.sort(reverse=True)
    last_node = last_node_list[0]

    return last_node


T = 10

for test_case in range(1, T + 1):
    # 입력
    data_len, start_node = map(int, input().split())
    # data_len, start_node = map(int, sys.stdin.readline().strip().split())

    date_list = list(map(int, input().split()))
    # date_list = list(map(int, sys.stdin.readline().strip().split()))

    data_set = defaultdict(list)
    visited = defaultdict(int)

    for idx in range(data_len//2):
        data_from = date_list[idx*2]
        data_to = date_list[idx*2 + 1]
        visited[data_from] = False
        visited[data_to] = 0
        data_set[data_from].append(data_to)

    # print(data_set)

    result = bfs(data_set, visited, start_node)
    
    # 출력 (SWEA 형식)
    print(f"#{test_case} {result}")
