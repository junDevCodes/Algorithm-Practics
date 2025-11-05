import sys
sys.stdin = open("sample_input.txt", encoding="utf-8")

from collections import deque

T = 10

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    order = list(map(int, input().split())) # 명령 리스트

    V_info = {i: [] for i in range(1, V + 1)} # 노드 자식 정보 담기
    V_reverse = {i: [] for i in range(1, V + 1)} # 노드 부모 정보 담기
    for idx in range(E):
        p = order[idx * 2]
        c = order[idx * 2 + 1]

        V_info[p].append(c)
        V_reverse[c].append(p)

    indeg = [0] * (V + 1)
    for v in range(1, V + 1): # 노드 부모 갯수 카운트
        indeg[v] = len(V_reverse[v])

    q = deque()
    for v in range(1, V + 1): # 노드 부모 갯수가 0인 초기 노드들 q에 삽입
        if indeg[v] == 0:
            q.append(v)

    work = []
    while q:
        cur = q.popleft()
        work.append(cur)
        for nxt in V_info[cur]: # 자식 조회
            indeg[nxt] -= 1 # 부모가 해결됐으므로 자식의 부모갯수 -= 1
            if indeg[nxt] == 0: # 모든 부모가 해결된 노드는 q에 추가
                q.append(nxt)

    print(f"#{tc}", *work)
