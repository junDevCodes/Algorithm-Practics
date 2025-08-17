# import sys
# from pathlib import Path

import itertools

# BASE_DIR = Path(__file__).parent.resolve()
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')

"""
[문제]
두개의 음식 시너지가 최소가 되는 식재료 조합을 찾아라
2개를 뽑은 후 점수 계산 나머지 2개의 점수 계산
합이 최소가 되는 조합 출력

[입력]
1. TC
2. 재료의 종류
3. 재료간 조합 점수표

[출력]
1. 가장 최소의 음식 점수 차

[로직]
종류 / 2로 조합 갯수 정하기
조합 돌리기
조합 점수, 조합 반대편 점수 계산
조합 반대편과 차이가 제일 적은 점수 계산

[예시 입력]
10
4
0 5 3 8
4 0 4 1
2 5 0 3
7 2 3 0

[예시 출력]
#1 2
#2 1
#3 38
#4 15
#5 4
#6 0
#7 51
#8 23
#9 13
#10 11
"""

# T = int(sys.stdin.readline().strip()) # TC
T = int(input()) # TC

for test_case in range(1, T + 1):
    # ingredients = int(sys.stdin.readline().strip()) # 재료 종류 수
    ingredients = int(input()) # 재료 종류 수
    # print(ingredients)

    # ingredients_combo = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(ingredients)] # 조합 점수표
    ingredients_combo = [list(map(int, input().split())) for _ in range(ingredients)] # 조합 점수표
    # print(ingredients_combo)

    ingredients_list = set([i for i in range(ingredients)]) # 조합 인덱스 번호표
    # print(ingredients_list)

    combo_list = list(itertools.combinations(ingredients_list, ingredients // 2)) # 인덱스로 조합 계산
    # print(combo_list)

    gap_combo = -1
    for combo in combo_list: # 각 조합별 계산
        other_combo = tuple(ingredients_list - set(combo)) # 나머지 인덱스 번호
        combo_cal = list(itertools.permutations(combo, 2)) # 점수 계산을 위해 2개씩 묶어 순열 생성
        other_combo_cal = list(itertools.permutations(other_combo, 2)) # 반대 점수 계산을 위해 2개씩 묶어 순열 생성

        combo_sum = 0
        other_combo_sum = 0
        cal_gap = 0
        for idx in range(len(combo_cal)):
            combo_sum += ingredients_combo[combo_cal[idx][0]][combo_cal[idx][1]] # 점수 계산
            other_combo_sum += ingredients_combo[other_combo_cal[idx][0]][other_combo_cal[idx][1]] # 반대 점수 계산
            cal_gap = abs(combo_sum - other_combo_sum)

        if gap_combo < 0:
            gap_combo = cal_gap
        else:
            gap_combo = min(gap_combo, cal_gap)

    print(f"#{test_case} {gap_combo}")
