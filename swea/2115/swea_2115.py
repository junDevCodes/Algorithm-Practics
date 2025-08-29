# SWEA 2115 문제 풀이
# import sys
# from pathlib import Path
#
# # 파일 입력 설정 (로컬 테스트용)
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')

"""
[문제 설명]
map_size * map_size 정사각형 벌통
각 칸에는 벌통에 있는 꿀의 양

두명의 일꾼이 있다.
벌통의 수 beehive_num
서로 겹치면 안된다

두 일꾼이 한 통에서 채취할 수 있는 꿀의 최대양 max_honey
만약 초과하는 경우 둘중 하나를 선택해서 꿀을 채취해야 한다.

채취한 꿀은 각 항목마다 용기에 담기며 그 값을 제곱하여 합해 수익이 생긴다
ex) 6, 1, 8
6*6 + 1*1 + 8*8 = 101
수익이 최대가 되는 경우를 찾고 그때의 수익을 출력하시오

[입력]
1. TC
2. map_size, beehive_num, max_honey
3. honey_info

[출력]
1. #tc 최대 수익

[예시]
입력:
10
4 2 13
6 1 9 7    
9 8 5 8
3 4 5 3
8 2 6 7
3 3 10
7 2 9
6 6 6
5 5 7

출력:
#1 174
#2 131
#3 145
#4 155
#5 166
#6 239
#7 166
#8 172
#9 291
#10 464

[알고리즘]
일꾼 두명 고정
가로 탐색 고정

전체 길이 - 벌통 길이 => 인덱스 로테이트
돌면서 일꾼 한명의 시작 인덱스 찾고 beehive_num만큼 한 통으로 묶기
visited a 에 넣고
한번더 인덱스 로테이트 후 visited a 아닌 인덱스를 찾고

visited combo((ay, ax, by, bx))찾고

visited combo 아닌것만 순회 계산

combo에서 한 그룹의 max_honey를 넘는 경우
조합 돌려서 조합의 합이 max_honey보다 작고 max인 값 찾기
각각의 유닛을 제곱 후 합하기
이 값이 제일 큰 걸 고르기

"""


def get_max_profit(honey_list, limit):
    max_val = 0
    beehive_num = len(honey_list)

    for i in range(1, 1 << beehive_num):
        total_honey = 0
        total_profit = 0
        for j in range(beehive_num):
            if i & (1 << j):
                total_honey += honey_list[j]
                total_profit += honey_list[j] ** 2

        if total_honey <= limit:
            max_val = max(max_val, total_profit)

    return max_val


def solve():
    max_profit = 0

    # map_size, beehive_num, max_honey = map(int, sys.stdin.readline().strip().split())
    map_size, beehive_num, max_honey = map(int, input().split())

    # honey_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(map_size)]
    honey_list = [list(map(int, input().split())) for _ in range(map_size)]

    for row_1 in range(map_size):
        for col_1 in range(map_size - beehive_num + 1):
            honey_1 = honey_list[row_1][col_1:col_1 + beehive_num]
            profit_1 = get_max_profit(honey_1, max_honey)

            for row_2 in range(row_1, map_size):
                start_col_2 = 0

                if row_1 == row_2:
                    start_col_2 = col_1 + beehive_num

                for col_2 in range(start_col_2, map_size - beehive_num + 1):
                    honey_2 = honey_list[row_2][col_2:col_2 + beehive_num]
                    profit_2 = get_max_profit(honey_2, max_honey)

                    max_profit = max(max_profit, profit_1 + profit_2)

    return max_profit


# SWEA 테스트 케이스 처리 템플릿
# T = int(sys.stdin.readline().strip())
T = int(input())
for test_case in range(1, T + 1):
    result = solve()

    # 출력 (SWEA 형식)
    print(f"#{test_case} {result}")
