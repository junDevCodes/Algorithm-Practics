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


def cell_simulation(cell_live, end_time):
    d_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cell_dead = set()

    for _ in range(end_time):
        cell_new = defaultdict(list)
        cell_die = set()

        for key, value in list(cell_live.items()):
            inact, act, life = value

            if inact > 0 :
                cell_live[key][0] -= 1
                continue

            if inact == 0:
                r, c = key
                for dr, dc in d_list:
                    n_key = (r + dr, c + dc)

                    if n_key in cell_live or n_key in cell_dead: continue

                    if n_key in cell_new:
                        if cell_new[n_key][2] < life:
                            cell_new[n_key] = [life, life, life]
                    else:
                        cell_new[n_key] = [life, life, life]

                cell_live[key][0] = -1
                cell_live[key][1] -= 1
            else: # inact = -1
                cell_live[key][1] -= 1

            if cell_live[key][1] == 0:
                cell_die.add(key)

        for d_cell in cell_die:
            cell_dead.add(d_cell)
            del cell_live[d_cell]

        for n_cell_key, n_cell_value in list(cell_new.items()):
            if n_cell_key not in cell_dead:
                cell_live[n_cell_key] = n_cell_value

    return len(cell_live)


def solve():
    T = int(input())
    for tc in range(1, T + 1):
        N, M, K = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(N)]
        cell_live = defaultdict(list)

        for r in range(N):
            for c in range(M):
                life = board[r][c]
                if life > 0:
                    cell_live[(r, c)] = [life, life, life]

        result = cell_simulation(cell_live, K)

        print(f"#{tc} {result}")


solve()
