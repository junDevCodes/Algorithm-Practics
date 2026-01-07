# BOJ 15686 문제 풀이
# import sys
# from pathlib import Path

# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
N x N 지도가 주어진다
집에서 가장 가까운 치킨집의 거리를 치킨 거리라고 하고
모든 집의 치킨 거리의 합을 도시의 치킨 거리라고 한다

치킨 가게를 M개 없앨 때

도시의 치킨 거리의 최솟값을 구하시오

[조건]
2 <= N <= 50
1 <= M <= 13
1 <= H <= 2N
M <= C <= 13

[입력]
N, M
map_info

[출력]
도시의 치킨 거리의 최소값

[알고리즘]
1. 모든 집의 좌표를 저장, 모든 치킨집의 좌표를 저장
2. 치킨집 제거 Combination
3. 조합 별 치킨거리 구하고 최솟값 출력

[복잡도]
- 시간: O()
- 공간: O()
"""
from itertools import combinations

# T = int(sys.stdin.readline())

# for tc in range(1, T + 1):
N, M = map(int, input().split())

houses = list()
chickens = list()

for i in range(N):
    row = list(map(int, input().split()))  # 한 줄씩 입력받기
    for j in range(N):
        if row[j] == 1:
            houses.append((i, j))
        elif row[j] == 2:
            chickens.append((i, j))


comb_list = list(combinations(chickens, M))

min_dist = float("inf")

for C_list in comb_list:
    temp_dist = 0
    for Home in houses:
        home_x, home_y = Home
        home_dist = float("inf")
        for Chicken in C_list:
            chicken_x, chicken_y = Chicken
            home_dist = min(home_dist, abs(home_x - chicken_x) + abs(home_y - chicken_y))
        temp_dist += home_dist
    min_dist = min(min_dist, temp_dist)

# check_result = int(input()) 

# if min_dist == check_result:
#     corr = "정답입니다."
# else:
#     corr = "오답입니다."
# 출력
print(min_dist)
    # print(f"{tc}번: {corr}")