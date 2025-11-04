# SWEA 2117 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
N: 도시크기, M: 하나의 집이 지불 할 수 있는 비용
N * N 도시의 홈 방범 서비스
마름모 모양의 영역 제공

운영 비용 공식: K * K + (K - 1) * (K - 1)

손해를 보지 않으면서 홈 방범 서비스를 가장 많은 집들에게 제공하는 서비스 영역을 찾고
그때 홈 방법 서비스를 제공 받는 집들의 수를 출력하는 프로그램을 작성하라

[조건]
테스트 케이스 50개
5 <= N <= 20
1 <= M <= 10
운영 비용은 서비스 면적과 동일
집이 있는 위치는 1 나머지는 0

[입력]
0. TC
1. N, M
2. board

[출력]
손해보지 않는 선에서 최대 집 갯수

[알고리즘]
1. 
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""
total_house = 0
max_house = 0

def cal_fee(size):
    return size * size + (size - 1) * (size - 1)


def sum_house_count(board):
    return sum(sum(row) for row in board)


def find_max_house(board, size, M, fee):
    global max_house

    N = len(board)

    for r in range(N):
        for c in range(N):
            house_count = find_house(board, (r, c), size)
            if fee <= (house_count * M):
                max_house = max(house_count, max_house)


def find_house(board, cur_coord, size):
    N = len(board)

    house = 0
    cr, cc = cur_coord

    for r in range(max(0, cr - size), min(cr + size + 1, N)):
        for c in range(max(0, cc - size), min(cc + size + 1, N)):
            if (abs(cr - r) + abs(cc - c)) < size and board[r][c] == 1:
                house += 1

    return house


def solve():
    global total_house, max_house

    T = int(input())

    for test_case in range(1, T + 1):
        N, M = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(N)]
        max_house = 0

        total_house = sum_house_count(board)

        for size in range(N+1, 0, -1):
            fee = cal_fee(size)

            if fee > total_house * M: continue

            find_max_house(board, size, M, fee)

        print(f"#{test_case} {max_house}")


solve()
