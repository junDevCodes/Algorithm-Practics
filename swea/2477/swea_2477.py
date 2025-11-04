# SWEA 2477 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
1~N개 접수 창구
1~M개 정비 창구
접수 창구마다 걸리는 시간 i
정비 창구마다 걸리는 시간 j

방문한 고객 1~K명
고객 도착시간 k

지갑 두고간 고객이 사용한 접수창구 A, 정비창구 B

A와 B를 이용한 고객들의 고객번호의 합
없는 경우 -1 출력

접수 창구
여러 고객이 기다리고 있는 경우 고객번호 낮은 순서대로 접수 heapq
빈창구가 여러개이면 접수 창구번호 작은곳으로 간다

정비 창구
먼저 기다리는 고객 우선 queue
두명 이상 고객이 동시 접수 완료하고 정비창구 이동시 접수 창구 작은 고객이 우선
빈 창구가 여러곳인 경우 정비 창구번호 작은 곳으로 간다.

[조건]
1. 1 <= N, M <= 9
2. 1 <= i, j <= 20
3. 2 <= K <= 1000
4.  0 <= k <= 1000

[입력]
0. TC
1. N, M, K, A, B
2. i
3. j
4. k

[출력]
지갑을 두고간 창구를 거쳐간 고객 번호의 합

[알고리즘]
1. 시뮬레이션 with queue, heapq
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""
from collections import deque
import heapq


def solve():
    T = int(input())
    
    for test_case in range(1, T + 1):
        N, M, K, A, B = map(int, input().split())
        counter = [[] for _ in range(N + 1)]
        garage = [[] for _ in range(M + 1)]
        counter_time = [0] + list(map(int, input().split()))
        garage_time = [0] + list(map(int, input().split()))
        customer = [0] + list(map(int, input().split()))

        customer_idx = 1
        c_time = 0
        customer_line = []
        garage_line = deque([])
        visited = [0] * (K + 1)
        done = 0
        result = 0

        while done != K:
            while customer_idx <= K and customer[customer_idx] == c_time: # 현재 시간 기준 도착한 손님은 접수 대기줄에 넣기 접수 번호 작은 순 정렬
                heapq.heappush(customer_line, customer_idx)
                customer_idx += 1

            for counter_idx in range(1, N + 1): # 대기줄이 있을때 카운터가 비어있다면 손님을 카운터에 넣고 0 초로 설정
                if customer_line:
                    if not counter[counter_idx]:
                        next_customer = heapq.heappop(customer_line)
                        counter[counter_idx] = [next_customer, 0]
                        if counter_idx == A: # 사용한 카운터가 카드 분실이면 고객 번호 추가
                            visited[counter[counter_idx][0]] += 1

            for counter_idx in range(1, N + 1):
                if counter[counter_idx]: # 모든 창구의 시간을 1씩 추가
                    counter[counter_idx][1] += 1
                    if counter[counter_idx][1] == counter_time[counter_idx]: # 카운터 상담 시간이 지나면 해당 카운터를 비우고 정비 줄로 넘기기
                        garage_line.append(counter[counter_idx][0])
                        counter[counter_idx] = []

            for garage_idx in range(1, M + 1): # 대기 줄이 있을 때 정비소가 비어있다면 정비소에 넣고 0초 설정
                if garage_line:
                    if not garage[garage_idx]:
                        next_garage = garage_line.popleft()
                        garage[garage_idx] = [next_garage, 0]
                        if garage_idx == B: # 사용한 카운터가 카드 분실이면 고객 번호 추가
                            visited[garage[garage_idx][0]] += 1

            for garage_idx in range(1, M + 1):
                if garage[garage_idx]: # 모든 정비소의 시간을 1씩 추가
                    garage[garage_idx][1] += 1
                    if garage[garage_idx][1] == garage_time[garage_idx]: # 정비소 작업이 지나면 정비소 비우기
                        garage[garage_idx] = []
                        done += 1

            c_time += 1

        for idx, res in enumerate(visited):
            if res == 2:
                result += idx

        if result == 0:
            result = -1

        print(f"#{test_case} {result}")


solve()

