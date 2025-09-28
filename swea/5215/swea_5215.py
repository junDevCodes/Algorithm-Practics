# SWEA 5215 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
재료 갯수, 제한 칼로리
칼로리 제한중 최대 점수를 출력하라

[입력]
0. TC
1. ingredient_num, max_calorie
2. ingredient_score, ingredient_calorie

[출력]
1. 주어진 제한 칼로리 이하의 조합 중 가장 점수가 높은 조합의 점수

[알고리즘]
1. dfs
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""


def dfs(index, c_sum, s_sum):
    global result

    if c_sum > max_c:
        return

    if index == i_num:
        result = max(s_sum, result)
        return

    dfs(index+1, c_sum+i_info[index][0], s_sum+i_info[index][1])

    dfs(index+1, c_sum, s_sum)


from collections import defaultdict

# T = int(sys.stdin.readline().strip())
T = int(input())

for test_case in range(1, T + 1):
    # 입력
    # i_num, max_c = map(int, sys.stdin.readline().strip().split())
    i_num, max_c = map(int, input().split())

    i_info = defaultdict(list)

    for idx in range(i_num):
        # i_score, i_calorie = map(int, sys.stdin.readline().strip().split())
        i_score, i_calorie = map(int, input().split())
        i_info[idx].extend([i_calorie, i_score])

    result = 0
    dfs(0, 0, 0)
    
    # 출력 (SWEA 형식)
    print(f"#{test_case} {result}")
