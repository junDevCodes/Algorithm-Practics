# SWEA 5644 문제 풀이
import sys
from pathlib import Path

# 로컬 테스트용 파일 입력 설정
BASE_DIR = Path(__file__).resolve().parent
sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
무선 충전 시 최적의 BC 선택 알고리즘

[조건]
1. 지도 가로세로 = 10
2. 사용자 총 2명 (1, 1), (10, 10) 고정
3. 총 이동시간 20~100
4. BC 갯수 1~8 / BC 성능 10~500 (짝수)
5. 초기 위치 충전 가능
6. 같은 위치 BC 없음, A, B 동시 같은 지점 이동 가능, 사용자 지도 밖 이동 없음

[입력]
0. TC
1. M: 총 이동 시간, A: BC 갯수
2. A 의 이동정보
3. B 의 이동정보
4. BC 갯수만큼 BC 정보 coord: (row, col), C: 충전 범위, P: 충전량

[출력]


[알고리즘]
1. 
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""
from collections import defaultdict


Charger = defaultdict(dict)
# 이동 방향 0: 정지, 1: 상, 2: 우, 3: 하, 4: 좌
d_list = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]


def charger_area(board, row, col, c, charge_id):
    for i in range(max(0, row - c), min(11, row + c + 1)):
        for j in range(max(0, col - c), min(11, col + c + 1)):
            if abs(i - row) + abs(j - col) <= c:
                board[i][j].append(charge_id)
                if 0 in board[i][j]:
                    board[i][j].remove(0)


def best_score(a_list, b_list):
    global Charger

    best = 0

    for a in a_list:
        for b in b_list:
            if a == 0 and b == 0:
                cand = 0
            elif a == b:
                cand = Charger[a]["power"]
            else:
                cand = 0
                if a != 0:
                    cand += Charger[a]["power"]
                if b != 0:
                    cand += Charger[b]["power"]
            best = max(best, cand)

    return best


def move_simulation(board, time, move_A, move_B):
    global d_list

    total_val = best_score(board[1][1], board[10][10])

    A_cr, A_cc = [1, 1]
    B_cr, B_cc = [10, 10]

    for c_time in range(1, time + 1):
        A_dr, A_dc = d_list[move_A[c_time]]
        B_dr, B_dc = d_list[move_B[c_time]]

        A_cr += A_dr
        A_cc += A_dc
        B_cr += B_dr
        B_cc += B_dc

        val_list_A = board[A_cr][A_cc]
        val_list_B = board[B_cr][B_cc]

        total_val += best_score(val_list_A, val_list_B)

    return total_val


def solve():
    global Charger

    T = int(input())

    for test_case in range(1, T + 1):
        M, A = map(int, input().split())
        board = [[[0] for _ in range(11)] for _ in range(11)]
        Charger = defaultdict(dict)

        move_A = [0] + list(map(int, input().split()))
        move_B = [0] + list(map(int, input().split()))

        for charger in range(1, A + 1):
            col, row, C, P = map(int, input().split())
            Charger[charger] = {"coord": (row, col), "area": C, "power": P}
            charger_area(board, row, col, C, charger)

        result = move_simulation(board, M, move_A, move_B)

        print(f"#{test_case} {result}")


solve()
