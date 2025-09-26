# SWEA 1486 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
점원의 키 조합에서 타겟 높이와의 차이가 최소인 경우에서 차이를 구하시오

[입력]
0. TC
1. 점원 수, 타겟 높이
2. 점원 키 리스트

[출력]
1. 최소인 경우 키차이

[알고리즘]
1. dfs
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""


def dfs(index, h_sum):
    global min_height

    if h_sum >= min_height:
        return

    if index == clerk_num:
        if h_sum >= target_height:
            min_height = min(min_height, h_sum)
        return

    dfs(index+1, h_sum + clerk_height_list[index])

    dfs(index+1, h_sum)


# T = int(sys.stdin.readline().strip())
T = int(input())
# T = int(input())

for test_case in range(1, T + 1):
    # 입력
    # clerk_num, target_height = map(int, sys.stdin.readline().strip().split())
    clerk_num, target_height = map(int, input().split())

    # clerk_height_list = list(map(int, sys.stdin.readline().strip().split()))
    clerk_height_list = list(map(int, input().split()))
    
    # 로직
    min_height = float('inf')

    dfs(0, 0)

    # 출력 (SWEA 형식)
    print(f"#{test_case} {min_height - target_height}")
