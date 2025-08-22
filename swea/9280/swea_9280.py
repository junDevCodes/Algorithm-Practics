# SWEA 9280 문제 풀이
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
차 도착 시 빈공간 탐색
없다면 입구에서 대기
있다면 주차 시킴, 주차 가능 공간 중 번호가 가장 작은 주차 공간
차들은 차례대로 기다림

주차 요금 = 차량의 무게와 주차공간마다 책정된 단위 무게당 금액을 곱한 가격

총 수입을 계산하는 프로그램

[입력]
1. TC
2. 단위 무게 수, 차량 갯수
3. 단위 무게당 요금 정보
4. 차량 무게 정보
5. 차량의 출입 여부 = 2 * 차량 갯수 : 음수면 출, 양수면 입 

[출력]
1. #{TC} {총 수입}

[로직]
딕셔너리를 통해 주차 타워 생성
주차타워 순회하며 빈자리 있으면 낮은 순서대로 채워넣기

[예시 입력]
2
3 4
2
3
5
2
1
3
8
3
2
-3
1
4
-4
-2
-1
2 4
5
2
100
500
1000
2000
3
1
2
4
-1
-3
-2
-4

[예시 출력]
#1 53
#2 16200

"""

import heapq
from collections import deque

T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    # rate_n, car_n = map(int, sys.stdin.readline().strip().split())
    rate_n, car_n = map(int, input().split())

    free_slot = [i for i in range(rate_n)] # 주차장 키
    # rate = [int(sys.stdin.readline().strip()) for _ in range(rate_n)] # 무게 가중치
    rate = [int(input()) for _ in range(rate_n)] # 무게 가중치
    # weight = [int(sys.stdin.readline().strip()) for _ in range(car_n)] # 차 무게
    weight = [int(input()) for _ in range(car_n)] # 차 무게
    car_pos = [-1] * car_n # 차량 현재 위치
    car_pos.insert(0, -1)
    weight.insert(0, -1)
    wait_q = deque() # 대기 줄
    heapq.heapify(free_slot) # 힙큐 변환
    total_fee = 0
    # print(free_slot, rate, weight, car_pos)

    for _ in range(2*car_n):
        # event = int(sys.stdin.readline().strip()) # 이벤트 받기
        event = int(input()) # 이벤트 받기
        if event > 0: # 입차
            if free_slot: # 받을 수 있는 키가 남아있으면
                slot = heapq.heappop(free_slot) # 남아있는 주차장 키 빼서
                car_pos[event] = slot # 차한테 주고
                total_fee += rate[slot] * weight[event] # 총 가격 추가
                # print(total_fee)
            else: # 키가 남아 있지 않으면
                wait_q.append(event) # 대기줄에 올리기
        else: # 출차
            event *= -1 # 음수이기 때문에 이벤트 값 변환
            slot = car_pos[event] # 현재 차 위치에서 slot 반환
            heapq.heappush(free_slot, slot) # 주차장 키 반환
            car_pos[event] = -1 # 차량 위치 초기화
            if wait_q:
                slot = heapq.heappop(free_slot) # 남아있는 주차장 키 빼서
                left_car = wait_q.popleft()
                car_pos[left_car] = slot # 차한테 주고
                total_fee += rate[slot] * weight[left_car] # 총 가격 추가

    print(f"#{test_case} {total_fee}")