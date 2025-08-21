# SWEA 1860 문제 풀이
# import sys
# from pathlib import Path
#
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')
#
# T = int(sys.stdin.readline().strip("\n"))
"""
[문제 설명]


[입력]
1. TC
2. 손님 수, 만드는 시간, 만드는 갯수
3. 손님 도착 시간

[출력]
1. 모든 손님이 지연시간 없이 붕어빵을 먹을 수 있는가 여부 출력

[로직]
현재까지의 빵 갯수 : 현재 시간 // 빵굽는 시간 * 빵 갯수
현재까지의 손님 수 : 현재 시간 >= 손님 시간

[예시 입력]
4
2 2 2
3 4
2 2 2
1 2
2 2 1
4 2
2 2 1
3 2

[예시 출력]
#1 Possible
#2 Impossible
#3 Possible
#4 Impossible

"""
from collections import deque

T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    # customer, cook_time, cook_bread = map(int, sys.stdin.readline().strip("\n").split())
    customer_num, cook_time, cook_bread = map(int, input().split())
    # customer_list = deque(sorted(list(map(int, sys.stdin.readline().strip("\n").split()))))
    customer_list = deque(sorted(list(map(int, input().split()))))
    pos = True

    current_customer = 0
    current_bread = 0
    for time in range(max(customer_list) + 1):
        current_bread = time // cook_time * cook_bread
        if customer_list:
            while customer_list and time >= customer_list[0]:
                customer_list.popleft()
                current_customer += 1
        else:
            break
        if current_bread < current_customer:
            pos = False
        # print(f"빵 갯수 : {current_bread}, 손님 수 : {current_customer}")

    print(f"#{test_case} {'Possible' if pos else 'Impossible'}")
