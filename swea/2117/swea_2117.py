# SWEA 2117 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
N*N 크기의 도시에 방범 서비스
K 크기의 서비스 영역은 마름모
운영비용 = 2(K * K) - 2K + 1

집은 각각 M의 비용 지불

손해보지 않으면서 가장 많은 집들에 제공하는 서비스 영역
이 때 서비스 받는 집의 갯수

[입력]
0. TC
1. N, M
2. 도시 정보

[출력]
집의 갯수

[알고리즘]
1. 운영비용 < M*집 갯수 일때 최대의 집 갯수 
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""


def check_house_cost(map_info, map_size, service_size, service_cost, total_cost):
    origin_size = service_size - 1

    max_house = 0
    for row in range(map_size):
        for col in range(map_size):
            house = 0
            for d_val in range(-origin_size, origin_size + 1):
                n_row = row + d_val
                if n_row < 0: continue
                if n_row > map_size-1: break
                rem = origin_size - abs(d_val)
                house += sum(map_info[n_row][max(0, col - rem):min(map_size, col + rem + 1)])

            if house * service_cost >= total_cost:
                max_house = max(max_house, house)

    return max_house


T = int(input())

for test_case in range(1, T + 1):
    # 입력
    # map_size, service_cost = map(int, sys.stdin.readline().strip().split())
    map_size, service_cost = map(int, input().split())
    map_info = []
    total_house_count = 0
    for _ in range(map_size):
        # row = list(map(int, sys.stdin.readline().strip().split()))
        row = list(map(int, input().split()))
        map_info.append(row)
        total_house_count += sum(row)

    result = 0
    for service_size in range(1, map_size+2):
        total_cost = service_size**2 + (service_size - 1)**2
        if total_cost > total_house_count * service_cost: ## 모든 집이 다 포함되어도 손해인 경우 break
            break
        check_house_num = check_house_cost(map_info, map_size, service_size, service_cost, total_cost)
        result = max(result, check_house_num)
    
    # 출력 (SWEA 형식)
    print(f"#{test_case} {result}")
