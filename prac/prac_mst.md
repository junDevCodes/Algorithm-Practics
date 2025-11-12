# MST

---
## 정의

- 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리

---
## 구현 알고리즘
### 1. **Kruskal**
#### 탐욕기법: 모든 간선 중에 가중치가 작은 간선을 선택하다보면 MST가 구현되겠지
- 간선을 하나씩 선택해서 MST를 찾는 알고리즘
- 간선을 가중치에 따라 오름차순으로 정렬
- 가중치가 가장 낮은 간선부터 선택
    1. 두 대표자가 다르다면 최소 비용 집합에 추가
    2. 두 대표자가 같다면 사이클이 생성되므로 무시
- n-1개의 간선이 선택될 때까지 2번 과정을 반복
### 2. **Prim**
#### 탐욕기법: 정점이 가지고 있는 간선중에 가중치가 작은 간선을 선택하다보면 MST가 구현되겠지 
- 임의 정점 하나를 선택해서 시작
- 우선순위 큐를 사용하여 간선의 가중치가 가장 작은 간선 선택
- 이 간선이 연결하는 정점이 이미 방문한 정점이 아니라면 최소 신장트리 추가, 방문 표시
- 우선순위 큐가 빌 때까지 반복
---
## Kruskal 구현
```python
class DisjointSet:
    def __init__(self, v):
        # 부모 노드를 저장하는 배열
        self.p = [0] * (len(v) + 1)
        # 트리의 높이(rank)를 저장하는 배열 (Union by Rank 최적화)
        self.rank = [0] * (len(v) + 1) 
    
    def make_set(self, x):
        # 각 원소를 개별 집합으로 초기화
        self.p[x] = x
        self.rank[x] = 0
    
    def find_set(self, x):
      # x가 속한 집합의 대표자(루트)를 찾음 (경로 압축 최적화)
        if x != self.p[x]:
            # 재귀적으로 루트를 찾으면서 경로상의 모든 노드를 루트에 직접 연결
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union_set(self, x, y):
        # x와 y가 속한 두 집합을 합침 (Union by Rank)
        # 각 원소의 루트(대표자) 찾기
        px = self.find_set(x)
        py = self.find_set(y)
        
        # 이미 같은 집합이면 union 불필요
        if px != py:
          # rank가 작은 트리를 큰 트리 아래에 붙임
          if self.rank[px] < self.rank[py]:
              self.p[px] = py
          elif self.rank[px] > self.rank[py]:
              self.p[py] = px
          else: # rank가 같으면 한쪽을 다른 쪽 아래에 붙이고 높이 1 증가
              self.p[py] = px
              self.rank[px] += 1

def mst_kruskal(vertices, edges):
    mst = [] # 최소 신장 트리를 구성할 간선들을 저장
    n = len(vertices)
    ds = DisjointSet(vertices)

    # 모든 정점을 개별 집합으로 초기화
    for i in range(n+1):
        ds.make_set(i)

    # 간선을 가중치 기준 오름차순 정렬 (탐욕 알고리즘의 핵심)
    edges.sort(key=lambda x: x[2])

    # 간선을 하나씩 확인하며 MST 구성
    for edge in edges:
        s, e, w = edge
        # 두 정점이 다른 집합에 속해있으면 (사이클이 생기지 않으면)
        if ds.find_set(s) != ds.find_set(e):
            ds.union_set(s, e) # 두 집합을 합침
            mst.append(edge) # MST에 간선 추가
            
    return mst

# edge = [시작정점, 도착정점, 가중치]
# edges = [[edge1], [edge2]]
# vertices = [node1, node2, node2]
# mst_kruskal(vertices, edges) = [[mst_edge1], [mst_edge2]]
```
---
## Prim 구현
```python
import heapq

def prim(vertices, edges):
    mst = [] # 최소 신장 트리를 구성할 간선들을 저장

    # 인접 리스트 생성: 각 정점에 연결된 (도착정점, 가중치) 쌍을 저장
    adj_list = {v: [] for v in vertices}
    for s, e, w in edges:
        adj_list[s].append((e, w)) # 무방향 그래프이므로
        adj_list[e].append((s, w)) # 양쪽 방향 모두 추가

    # 방문한 정점을 추적
    visited = set()
    
    # 시작 정점 선택 (임의로 첫 번째 정점 선택)
    init_vertex = vertices[0]
    visited.add(init_vertex) # 시작 정점을 방문 처리

    # 시작 정점과 연결된 모든 간선을 우선순위 큐에 추가
    # [가중치, 시작정점, 도착정점] 형태로 저장 (가중치 기준으로 최소 힙)
    min_heap = [[w, init_vertex, e] for e, w in adj_list[init_vertex]]
    heapq.heapify(min_heap)
    
    # 우선순위 큐가 빌 때까지 반복
    while min_heap:
        # 가중치가 가장 작은 간선 선택 (탐욕 알고리즘의 핵심)
        w, s, e = heapq.heappop(min_heap)
        
        # 이미 방문한 정점이면 건너뜀 (사이클 방지)
        if e in visited: continue
        
        # 새로운 정점 방문 처리
        visited.add(e)
        mst.append((s, e, w)) # MST에 간선 추가
        
        # 새로 추가된 정점과 연결된 모든 간선을 우선순위 큐에 추가
        for adj_v, adj_w in adj_list[e]:
            # 방문하지 않은 정점으로 가는 간선만 추가
            if adj_v in visited: continue
            heapq.heappush(min_heap, [adj_w, e, adj_v])
            
    return mst

# edge = [시작정점, 도착정점, 가중치]
# edges = [[edge1], [edge2]]
# vertices = [node1, node2, node2]
# mst_kruskal(vertices, edges) = [[mst_edge1], [mst_edge2]]
```