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
1. i_num, c_max
2. i_score, i_cal
i_info - dict

[출력]
1. 주어진 제한 칼로리 이하의 조합 중 가장 점수가 높은 조합의 점수

[알고리즘]
1. dfs 선택 비선택 분기
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""
def dfs(c_idx, c_cal, c_score):
    global i_num, c_max, high_score

    if c_idx == i_num:
        if c_cal <= c_max:
            high_score = max(high_score, c_score)
        return

    key = key_list[c_idx]
    value = item_list[c_idx]
    dfs(c_idx+1, c_cal + value, c_score + key) # 선택
    dfs(c_idx+1, c_cal, c_score) # 미선택


# T = int(sys.stdin.readline())
T = int(input())

for tc in range(1, T + 1):

    # i_num, c_max = map(int, sys.stdin.readline().strip().split())
    i_num, c_max = map(int, input().split())

    key_list = [0] * i_num
    item_list = [0] * i_num
    for idx in range(i_num):
        # i_score, i_cal = map(int, sys.stdin.readline().strip().split())
        i_score, i_cal = map(int, input().split())
        key_list[idx] = i_score
        item_list[idx] = i_cal

    high_score = float("-inf")

    dfs(0, 0, 0)

    print(f"#{tc} {high_score}")