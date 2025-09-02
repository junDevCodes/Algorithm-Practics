# BOJ 2412 문제 풀이
"""
[문제 설명]
암벽 홈
각각의 홈 좌표(x, y)
abs(a-x) <= 2 and abs(b-y) <= 2인 경우 a, b로 이동 가능
y = T까지 올라가려한다
0, 0에서 이동회수를 최소로 하면서 정상에 오르려 한다
x 좌표는 상관 없음

[입력]
1. spot_num, top
2. spot_info


[출력]
1. 최소 이동 회수 / 불가능 시 -1

[알고리즘]
완탐
최소 횟수


[복잡도]
"""
import sys
from collections import deque


def solve():
    spot_num, top = map(int, sys.stdin.readline().split())

    # 딕셔너리로 홈을 y 좌표 기준으로 정리
    spots = {}
    for _ in range(spot_num):
        x, y = map(int, sys.stdin.readline().split())
        if y not in spots:
            spots[y] = []
        spots[y].append(x)

    # 0,0에서 시작
    queue = deque([(0, 0, 0)])
    visited = set([(0, 0)])

    while queue:
        x, y, step = queue.popleft()

        # 정상에 도달하면 단계 반환
        if y == top:
            print(step)
            return

        # y좌표 +-2 범위의 홈들만 탐색
        for dy in range(-2, 3):
            next_y = y + dy
            if next_y in spots:
                # 다음 y 좌표에 있는 모든 x 좌표를 탐색
                for next_x in spots[next_y]:
                    # x 좌표도 +-2 범위에 있는지 확인
                    if abs(next_x - x) <= 2:
                        if (next_x, next_y) not in visited:
                            visited.add((next_x, next_y))
                            queue.append((next_x, next_y, step + 1))

    print(-1)


solve()