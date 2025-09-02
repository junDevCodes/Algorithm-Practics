# SWEA 1953 문제 풀이
import sys
from pathlib import Path

# 로컬 테스트용 파일 입력 설정
sys.stdin = open('sample_input.txt', 'r', encoding='utf-8')

"""
[문제 설명]
탈주범이 최대로 갈 수 있는 좌표 갯수를 구하라

[입력]
1. TC
2. map_row, map_col, start_row, start_col, escape_time
3. map_info

1, 2, 3, 4, 5, 6, 7
1: 상하좌우
2: 상하
3: 좌우
4: 상우
5: 하우
6: 하좌
7: 상좌

[출력]
최대로 갈 수 있는 범위

[알고리즘]
bfs visited

[복잡도]
- 시간: O()
- 공간: O()
"""
from collections import deque


delta_list = {
    1: [(-1, 0), (1, 0), (0, 1), (0, -1)],
    2: [(1, 0), (-1, 0)],
    3: [(0, 1), (0, -1)],
    4: [(-1, 0), (0, 1)],
    5: [(1, 0), (0, 1)],
    6: [(1, 0), (0, -1)],
    7: [(-1, 0), (0, -1)]
}


def is_valid_connection(pipe_type, dr, dc, next_pipe_type):
    # 현재 터널의 이동 방향과 다음 터널의 연결 방향이 일치하는지 확인

    # 현재 터널이 위쪽으로 이동할 때 (dr=-1, dc=0)
    if (dr, dc) == (-1, 0) and next_pipe_type in [1, 2, 5, 6]:
        return True
    # 현재 터널이 아래쪽으로 이동할 때 (dr=1, dc=0)
    if (dr, dc) == (1, 0) and next_pipe_type in [1, 2, 4, 7]:
        return True
    # 현재 터널이 왼쪽으로 이동할 때 (dr=0, dc=-1)
    if (dr, dc) == (0, -1) and next_pipe_type in [1, 3, 4, 5]:
        return True
    # 현재 터널이 오른쪽으로 이동할 때 (dr=0, dc=1)
    if (dr, dc) == (0, 1) and next_pipe_type in [1, 3, 6, 7]:
        return True

    return False


def bfs(map_info, sr, sc, R, C, L):
    visited = [[False] * C for _ in range(R)]
    queue = deque([(sr, sc, 1)])
    visited[sr][sc] = True
    count = 1

    while queue:
        cr, cc, time = queue.popleft()

        if time == L:
            continue

        pipe_type = map_info[cr][cc]

        for dr, dc in delta_list[pipe_type]:
            nr, nc = cr + dr, cc + dc

            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and map_info[nr][nc] != 0:
                next_pipe_type = map_info[nr][nc]
                if is_valid_connection(pipe_type, dr, dc, next_pipe_type):
                    visited[nr][nc] = True
                    queue.append((nr, nc, time + 1))
                    count += 1

    return count


def solve():
    # T = int(input())
    T = int(sys.stdin.readline().strip())

    for test_case in range(1, T + 1):
        map_row, map_col, start_row, start_col, escape_time = map(int, sys.stdin.readline().strip().split())
        map_info = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(map_row)]

        result = bfs(map_info, start_row, start_col, map_row, map_col, escape_time)

        # 출력 (SWEA 형식)
        print(f"#{test_case} {result}")


solve()
