# SWEA 1217 문제 풀이
# import sys
# from pathlib import Path
#
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')
#
# T = 10
"""
[문제 설명]
두개의 숫자 N, M이 주어질 때 N의 M 거듭제곱 값을 구하시오
TC = 10

[입력]
1. tc
2. num, power

[출력]
#tc cal_val

[로직]
재귀함수
한번 들어갈때마다 power - 1
power == 0 까지 반복

[예시 입력]
1
9 8
2
2 8

[예시 출력]
#1 43046721
#2 256
"""
T = 10  # 표준 입력 사용 시


def cal_power(n, p):
    if p == 0:
        return 1
    return n * cal_power(n, p-1)


for test_case in range(1, T + 1):
    # tc = int(sys.stdin.readline().strip("\n"))
    tc = int(input())
    # print(tc)

    num, power = map(int, input().split())
    # print(num, power)

    cal_val = cal_power(num, power)

    print(f"#{test_case} {cal_val}")
