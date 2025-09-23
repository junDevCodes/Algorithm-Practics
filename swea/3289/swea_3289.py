# SWEA 3289 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
입력 n, m일때
1 ~ n 이 각각 n개의 집합이 주어지고
m개의 연산이 주어진다
합집합은 0 a b의 형태로 주어지고
두 원소가 같은 집합인지 확인하는 연산은 1 a b 의 형태로 주어진다
각 테스트 케이스마다 1 연산의 결과값을 저장해서 한줄로 연속해 출력시킨다.

[입력]
0. TC
1. set_num, cal_num
2. cal_info

[출력]
1. get_cal_str

[알고리즘]
1. 서로소 구현
2. union 구현
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""
from collections import deque


def find_set(a):
    if a != p_list[a]: # 대표자가 아니면
        p_list[a] = find_set(p_list[a])
    return p_list[a]


def is_same_set(a, b):
    pa = find_set(a)
    pb = find_set(b)

    return int(pa == pb)


def union_set(a, b):
    pa = find_set(a)
    pb = find_set(b)

    if pa != pb:
        if p_rank[pa] > p_rank[pb]:
            p_list[pb] = pa
        elif p_rank[pa] < p_rank[pb]:
            p_list[pa] = pb
        else:
            p_list[pb] = pa
            p_rank[pa] += 1


# T = int(sys.stdin.readline())
T = int(input())

for test_case in range(1, T + 1):
    # set_num, cal_num = map(int, sys.stdin.readline().strip().split())
    set_num, cal_num = map(int, input().split())
    p_list = [i for i in range(set_num + 1)]
    p_rank = [0] * (set_num + 1)

    # order_list = deque([list(map(int, sys.stdin.readline().strip().split())) for _ in range(cal_num)])
    order_list = deque([list(map(int, input().split())) for _ in range(cal_num)])

    result = ""

    while order_list:
        order, set_a, set_b = order_list.popleft()
        if order == 1:
            result += str(is_same_set(set_a, set_b))
        elif order == 0:
            union_set(set_a, set_b)

    # 로직
    
    # 출력 (SWEA 형식)
    print(f"#{test_case} {result}")
