# SWEA 5249 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
노드번호 V 와 간선갯수 E가 주어진다
E개 의 간선과 가중치 정보가 나올때
최소신장트리의 간선 가중치의 합을 구하시오

[입력]
0. TC
1. node_num, edge_num
2. edge_info

[출력]
1. w_sum

[알고리즘]
1. 
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""


class DisjointSet:
    def __init__(self, v):
        self.p = [0] * (len(v) + 1)
        self.rank = [0] * (len(v) + 1)

    def make_set(self, x):
        self.p[x] = x

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
    len_v = len(vertices)
    ds = DisjointSet(vertices)

    for i in range(len_v):
        ds.make_set(i)

    edges.sort(key=lambda x: x[2])

    for edge in edges:
        s, e, w = edge
        if ds.find_set(s) != ds.find_set(e):
            ds.union_set(s, e)
            mst.append(edge)

    return mst


# T = int(sys.stdin.readline())
T = int(input())

for test_case in range(1, T + 1):
    # 입력
    # node_num, edge_num = map(int, sys.stdin.readline().strip().split())
    node_num, edge_num = map(int, input().split())
    node_vertices = [i for i in range(node_num+1)]
    # node_edges = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(edge_num)]
    node_edges = [list(map(int, input().split())) for _ in range(edge_num)]

    # 로직
    result = 0
    for item in mst_kruskal(node_vertices, node_edges):
        result += item[2]
    
    # 출력 (SWEA 형식)
    print(f"#{test_case} {result}")
