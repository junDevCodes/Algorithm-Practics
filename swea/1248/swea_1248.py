# SWEA 1248 문제 풀이
import sys
from pathlib import Path

# 로컬 테스트용 파일 입력 설정
BASE_DIR = Path(__file__).resolve().parent
sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
공통 조상 찾고 서브트리 갯수 구하기

[조건]
10 <= V <= 10000

[입력]
T
V, E, 8, 13
E개 간선 리스트

[출력]


[알고리즘]
1. 
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""


def lca(parent, a, b):
    anc = set()
    x = a
    while x != 0:
        anc.add(x)
        x = parent[x]

    y = b
    while y not in anc:
        y = parent[y]

    return y


def subtree_size(childern, root):
    stack = [root]
    cnt = 0

    while stack:
        node = stack.pop()
        cnt += 1
        for item in childern[node]:
            stack.append(item)

    return cnt


def solve():
    T = int(input())
    
    for test_case in range(1, T + 1):
        V, E, t1, t2 = map(int, input().split())
        parent = [0] * (V + 1)
        children = [[] for _ in range(V + 1)]
        order = list(map(int, input().split()))

        for idx in range(E):
            p = order[idx*2]
            c = order[idx*2 + 1]
            parent[c] = p
            children[p].append(c)

        father = lca(parent, t1, t2)
        sub_size = subtree_size(children, father)

        print(f"#{test_case} {father} {sub_size}")
        

solve()
