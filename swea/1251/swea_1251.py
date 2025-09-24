# SWEA 1251 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
N개의 섬을 연결하는 교통 시스템
각 이동은 환경부담 세율(E)와 해저터널길이(L) 제곱의 곱
가중치 = E * L**2

최소 가중치로 N개의 섬을 연결하는 방법

[입력]
0. TC
1. island_num
2. island_x, island_y
3. fee


[출력]
1. 최소 환경 부담금

[알고리즘]
1. 
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""
from itertools import combinations


class DisjointSet:
    def __init__(self, v):
        self.p = [0] * (len(v) + 1)
        self.rank = [0] * (len(v) + 1)

    def make_set(self, x):
        self.p[x] = x
        self.rank[x] = 0

    def find_set(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union_set(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        if px != py:
            if self.rank[px] < self.rank[py]:
                self.p[px] = py
            elif self.rank[px] > self.rank[py]:
                self.p[py] = px
            else:
                self.p[py] = px
                self.rank[px] += 1


def mst_kruskal(vertices, edges):
    mst = []
    n = len(vertices)
    ds = DisjointSet(vertices)

    for i in range(n+1):
        ds.make_set(i)

    edges.sort(key=lambda x: x[2])
    for edge in edges:
        s, e, w = edge
        if ds.find_set(s) != ds.find_set(e):
            ds.union_set(s, e)
            mst.append(edge)
    return mst


# T = int(sys.stdin.readline().strip())
T = int(input())

for test_case in range(1, T + 1):
    # 입력
    # island_num = int(sys.stdin.readline().strip())
    island_num = int(input())
    island_vertices = [i for i in range(1, island_num + 1)]
    # island_x = [0] + list(map(int, sys.stdin.readline().strip().split()))
    # island_y = [0] + list(map(int, sys.stdin.readline().strip().split()))
    island_x = [0] + list(map(int, input().split()))
    island_y = [0] + list(map(int, input().split()))
    # fee = float(sys.stdin.readline().strip())
    fee = float(input())
    island_edges = list(combinations(island_vertices, 2))

    for edge_idx in range(len(island_edges)):
        start_e = island_edges[edge_idx][0]
        end_e = island_edges[edge_idx][1]
        island_len = abs(island_x[start_e] - island_x[end_e])**2 + abs(island_y[start_e] - island_y[end_e])**2
        island_edges[edge_idx] = list(island_edges[edge_idx]) + [island_len * fee]

    # 로직
    result = 0
    for item in mst_kruskal(island_vertices, island_edges):
        result += item[2]
    
    # 출력 (SWEA 형식)
    print(f"#{test_case} {round(result)}")
