# SWEA 5250 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
추가 가중치가 있는 다익스트라

[입력]
0. tc
1. map_size
2. map_info

[출력]
1. (0, 0) -> (map_size-1, map_size-1) 까지의 최소 비용

[알고리즘]
1.상하좌우로만 이동 가능
2. 일단 기존 distance를 map 형식으로 관리 현재 위치까지 도착하는데 드는 비용 갱신
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""
from collections import defaultdict
import heapq, math


d_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dijkstra(graph, s_row, s_col):
    distances = [[math.inf] * map_size for _ in range(map_size)]
    distances[s_row][s_col] = 0
    min_heap = []
    heapq.heappush(min_heap, (0, s_row, s_col))

    while min_heap:
        c_distance, c_row, c_col = heapq.heappop(min_heap)

        if distances[c_row][c_col] < c_distance: continue #현재 거리가 기존 거리보다 길면 다음꺼 탐색

        c_height = graph[c_row][c_col]
        for d_row, d_col in d_list: # 델타 탐색
            weight = 1
            n_row, n_col = c_row + d_row, c_col + d_col
            if n_row < 0 or n_col < 0 or n_row >= map_size or n_col >= map_size: continue # 맵 범위 밖이면 다음꺼 탐색

            n_height = graph[n_row][n_col]

            if c_height < n_height: # 다음 지역이 더 높은 경우 높이 차이만큼 가중치 추가
                weight += n_height - c_height

            distance = c_distance + weight
            if distance < distances[n_row][n_col]:
                distances[n_row][n_col] = distance
                heapq.heappush(min_heap, (distance, n_row, n_col))

    return distances


T = int(input())

for test_case in range(1, T + 1):
    map_size = int(input())
    map_info = [list(map(int, input().split())) for _ in range(map_size)]
    # print(map_info)

    res = dijkstra(map_info, 0, 0)

    print(f"#{test_case} {res[map_size-1][map_size-1]}")
