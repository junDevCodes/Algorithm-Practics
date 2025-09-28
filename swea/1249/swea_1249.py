# SWEA 1249 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
bfs를 통해 최소 값을 가지는 경로 탐색

[입력]
0. TC
1. map_size
2. map_info

[출력]
경로상 최소 복구 시간.

[알고리즘]
1. bfs
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""
import heapq


def dijkstra():
    N = len(map_info)
    # 각 칸까지의 최소 비용 기록
    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = map_info[0][0]

    # (비용, 행, 열)
    heap = [(map_info[0][0], 0, 0)]

    while heap:
        c_cost, r, c = heapq.heappop(heap)

        # 이미 더 짧은 경로로 처리된 경우 패스
        if c_cost > dist[r][c]:
            continue

        # 상하좌우 탐색
        for dr, dc in d_list:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N:
                n_cost = c_cost + map_info[nr][nc]
                if n_cost < dist[nr][nc]:
                    dist[nr][nc] = n_cost
                    heapq.heappush(heap, (n_cost, nr, nc))

    return dist[N-1][N-1]


d_list = [(0, 1), (1, 0), (-1, 0), (0, -1)]


# T = int(sys.stdin.readline())
T = int(input())

for test_case in range(1, T + 1):
    # 입력
    # map_size = int(sys.stdin.readline())
    map_size = int(input())

    # map_info = [list(map(int, sys.stdin.readline().strip())) for _ in range(map_size)]
    map_info = [list(map(int, input())) for _ in range(map_size)]

    # 로직
    result = dijkstra()
    
    # 출력 (SWEA 형식)
    print(f"#{test_case} {result}")
