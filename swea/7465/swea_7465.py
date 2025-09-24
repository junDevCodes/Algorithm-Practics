# SWEA 7465 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
창용 마을 무리의 갯수를 구하라
1~N번까지 번호가 붙여져있고
서로를 아는 관계이거나 몇 사람을 거쳐서 아는 관계라면 하나의 무리라고 한다

[입력]
0. TC
1. p_num, r_num
2. r_info

[출력]
1. 무리의 갯수

[알고리즘]
1. get union 처리
2. p 리스트의 갯수를 구하기
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""


def find_set(x):
    if x != p_list[x]:
        p_list[x] = find_set(p_list[x])
    return p_list[x]


def union_set(x, y):
    px = find_set(x)
    py = find_set(y)

    if px != py:
        if px < py:
            p_list[px] = py
        elif px > py:
            p_list[py] = px
        else:
            p_list[py] = px
            p_rank[px] += 1


# T = int(sys.stdin.readline())
T = int(input())

for test_case in range(1, T + 1):
    # 입력
    # p_num, r_num = map(int, sys.stdin.readline().strip().split())
    p_num, r_num = map(int, input().split())

    p_list = [i for i in range(p_num + 1)]
    p_rank = [0] * (p_num+1)

    for _ in range(r_num):
        # set_a, set_b = map(int, sys.stdin.readline().strip().split())
        set_a, set_b = map(int, input().split())

        union_set(set_a, set_b)

    group = set()
    for idx in range(1, p_num+1):
        p_list[idx] = find_set(idx)
        group.add(p_list[idx])

    # 로직
    result = len(group)
    
    # 출력 (SWEA 형식)
    print(f"#{test_case} {result}")
