# SWEA 5653 문제 풀이
import sys
from pathlib import Path

# 로컬 테스트용 파일 입력 설정
BASE_DIR = Path(__file__).resolve().parent
sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
N: 세로크기
M: 가로크기
K: 시간

X시간동안 비활성화
이후 X 시간동안 활성화
이후 사망

사망할때는 죽은 상태로 셀을 차지하고 있음
활성화된 세포는 첫 1시간 동안 상하좌우 네 방향으로 번식을 함

[입력]
0. TC
1. N, M, K
2. map_info

[출력]
1. 활성, 비활성 세포의 갯수

[알고리즘]
1. 셀 위치로 default dict 사용, 활성, 비활성, 사망 상태 저장
2. bfs queue 전부 소진을 1타임으로 상태 변경, 확장까지
3. 시간이 지났을때 queue 강제 종료 queue에 남아있는 작업의 갯수 = 살아있는 세포 갯수

0: 사망 1: 비활성 2: 활성

[복잡도]
- 시간: O()
- 공간: O()
"""
from collections import defaultdict


<<<<<<< HEAD
<<<<<<< HEAD
def bfs(board, cell_list, max_time):
    d_list = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    N = len(board)
    M = len(board[0])

    queue = deque([*cell_list.keys()])
    cur_time = 1

    while cur_time <= max_time: # 현재 시간이 타겟 시간인 경우
        to_add = {}

        while queue:
            key = queue.popleft()
            active_time, status, cell_time = cell_list[key]
            r, c = key

            if active_time == cell_time: # 활성, 비활성 시간에 도달한 경우
                status = (status + 1) % 3 # 상태 변경 비활성 -> 활성 -> 사망
                cell_list[key] = [active_time, status, 1] # 셀 업데이트
                continue

            if status == 0: continue

            if status == 2 and cell_time == 1:
                for dr, dc in d_list:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nc < 0 or nr >= N or nc >= M: continue
                    to_add[(r, c)] = max(to_add.get((nr, nc), 0), active_time)

            cell_list[key][2] += 1

        for add_key, add_value in to_add.items():
            cell_list[add_key] = cell_list.get(add_key, [add_value, 1, 1])
        cur_time += 1

    print(cell_list)
    return 1
=======
=======
>>>>>>> afd27d6f726ba58c27b63fbddc6a0622a93bc9fc
def cell_simulation(cell_list, end_time):
    d_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dead = set()

    for _ in range(end_time):
        new_cell = defaultdict(list)
        die = set()

        for key, value in list(cell_list.items()):
            inact, act, life = value

            if inact > 0:
                cell_list[key][0] -= 1
                continue

            if inact == 0:
                r, c = key
                for dr, dc in d_list:
                    n_key = (r + dr, c + dc)

                    if n_key in cell_list or n_key in dead: continue

                    if n_key in new_cell:
                        if new_cell[n_key][2] < life:
                            new_cell[n_key] = [life, life, life]
                    else:
                        new_cell[n_key] = [life, life, life]
                cell_list[key][0] = -1
                cell_list[key][1] -= 1
            else:
                cell_list[key][1] -= 1

            if cell_list[key][1] == 0:
                die.add(key)

        for d_cell in die:
            dead.add(d_cell)
            del cell_list[d_cell]

        for n_key, val in new_cell.items():
            if n_key not in dead:
                cell_list[n_key] = val

                act -= 1

    return len(cell_list)
>>>>>>> ca29d6b6dc1899471413107467559e5126a67021


def solve():
    T = int(input())

    for test_case in range(1, T + 1):
        N, M, K = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(N)]

        cell_list = defaultdict(list)

        for row in range(N):
            if sum(board[row]) == 0: continue

            for col in range(M):
                if board[row][col] > 0:
                    cell_list[(row, col)] = [board[row][col], board[row][col], board[row][col]]
                    #비활성 시간 타이머, 활성 시간 타이머, 생명값

        result = cell_simulation(cell_list, K)

        print(f"#{test_case} {result}")


solve()