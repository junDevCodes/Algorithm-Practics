# SWEA 1859 문제 풀이
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')
T = int(sys.stdin.readline().strip("\n"))
"""
input : tc, opportunity, sale_price
output : max_price

logic : 
1. 최대 값을 기준으로 list를 나눈다.
2. list마다 최대 값이 맨 뒤에 오도록 한다.
3. 최대 값보다 작은 값만 list에 추가한다.
4. 최대 값과의 차이 값을 종합해서 계산

개선 로직 :
뒤에서 부터 순회하며 이전 값 보다 큰 경우 max_price
max_price 보다 작은 경우 차이를 price_total += 차이
max_price 보다 큰 경우 max_price 교체 
"""
# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    opportunity = int(sys.stdin.readline().strip("\n"))
    # opportunity = int(input())
    # print(opportunity)

    sale_price = list(map(int, sys.stdin.readline().strip("\n").split()))
    # sale_price = list(map(int, input().split()))
    # print(sale_price)

    stack = []
    divide_price = []

    price_copy = sale_price.copy() # 데이터 무결성 위한 copy

    while 1:
        max_idx = price_copy.index(max(price_copy)) # 현재 리스트에서 가장 큰 값의 index 위치

        if max_idx == (len(price_copy) -1): # 가장 큰 값이 맨 뒤인 경우 추가 후 break
            top_val = len(price_copy[:max_idx]) * price_copy[max_idx]
            sum_others = sum(price_copy[:max_idx])
            divide_price.append([top_val, sum_others])
            break

        top_val = len(price_copy[:max_idx]) * price_copy[max_idx]
        sum_others = sum(price_copy[:max_idx])
        divide_price.append([top_val, sum_others])

        price_copy = price_copy[max_idx+1:] # 분할 후 나머지 부분 저장

    price_total = 0

    for part in divide_price:
        price_total += part[0] - part[1]

    print(f"#{test_case} {price_total}")