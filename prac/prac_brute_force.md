## dfs 구현코드 by 이준영
```py
def dfs(list, node=0):
    global visited

    if 종료조건(문제에따라 다름):
        return 문제에따라 다름
    
    if node not in visited:
        visited.append(node)
    
    return 문제에따라 다름 + dfs(list, node+1)

visited = []
```
---
## dfs 구현 코드 템플릿 유형 1. 단순 방문
```py
def dfs(graph, node):
    global visited
    visited[node] = True  # 현재 노드 방문 처리
    print(node, end=' ') # 방문 순서 출력 (예시)

    # 현재 노드와 연결된 모든 이웃 노드를 확인
    for neighbor in graph[node]:
        # 아직 방문하지 않은 이웃 노드라면
        if not visited[neighbor]:
            dfs(graph, neighbor) # 재귀 호출

# 사용 예시 (인접 리스트)
# graph = { 0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2] }
# visited = [False] * 4
# dfs(graph, 0)
```
---
## dfs 구현 코드 템플릿 유형 2. 경로 탐색 & 백트래킹
```py
def dfs(graph, start_node, end_node):
    if start_node == end_node:
        return True # 목표에 도달했으므로 True 반환

    global visited
    visited[start_node] = True

    for neighbor in graph[start_node]:
        if not visited[neighbor]:
            # 재귀 호출 결과가 True이면, 더 이상 탐색하지 않고 True를 반환
            if dfs(graph, neighbor, end_node):
                return True
    
    # 모든 이웃 노드를 탐색했지만 목표에 도달하지 못했을 경우
    return False

# 사용 예시
# graph = ...
# visited = [False] * len(graph)
# if dfs(graph, 0, 3):
#     print("경로를 찾았습니다.")
```
---
## bfs 구현 코드 템플릿
```py
from collections import deque

def bfs(graph, start_node):
    queue = deque([start_node])  # 1. 큐에 시작 노드 삽입
    visited = {start_node}       # 2. 방문 집합에 시작 노드 추가

    while queue:
        current_node = queue.popleft() # 3. 큐에서 노드 추출
        print(current_node, end=' ')   # 노드 처리 (예: 방문)

        # 4. 현재 노드의 이웃 노드들을 확인
        for neighbor in graph[current_node]:
            # 5. 아직 방문하지 않은 노드라면
            if neighbor not in visited:
                visited.add(neighbor)   # 방문 처리
                queue.append(neighbor) # 큐에 삽입
# graph = { 0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2] }
```