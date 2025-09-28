# SWEA 4008 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
숫자 정보가 주어지고 연산자 갯수가 주어진다
연산자는 + - * / 순서이며
숫자의 순서를 변경하지 않고 연산자의 배치를 수정하여 최대 계산 값을 출력하시오

[입력]
0. TC
1. num
2. op_info
3. num_info

[출력]
1. 최대 계산 값

[알고리즘]
1. dfs
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""


def dfs(index, cal_val, plus_cnt, minus_cnt, mul_cnt, div_cnt):
    global max_val, min_val

    if index == num:
        max_val = max(max_val, cal_val)
        min_val = min(min_val, cal_val)
        return

    next_num = num_info[index]

    if plus_cnt > 0:
        dfs(index + 1, cal_val + next_num, plus_cnt - 1, minus_cnt, mul_cnt, div_cnt)

    if minus_cnt > 0:
        dfs(index + 1, cal_val - next_num, plus_cnt, minus_cnt - 1, mul_cnt, div_cnt)

    if mul_cnt > 0:
        dfs(index + 1, cal_val * next_num, plus_cnt, minus_cnt, mul_cnt - 1, div_cnt)

    if div_cnt > 0:
        dfs(index + 1, int(cal_val / next_num), plus_cnt, minus_cnt, mul_cnt, div_cnt - 1)


# T = int(sys.stdin.readline().strip())
T = int(input())

for test_case in range(1, T + 1):
    # 입력
    # num = int(sys.stdin.readline().strip())
    # op_list = list(map(int, sys.stdin.readline().strip().split()))
    # num_info = list(map(int, sys.stdin.readline().strip().split()))
    num = int(input())
    op_info = list(map(int, input().split()))
    num_info = list(map(int, input().split()))

    # print(op_info)

    # 로직
    max_val = float('-inf')
    min_val = float('inf')

    dfs(1, num_info[0], op_info[0], op_info[1], op_info[2], op_info[3])

    result = max_val - min_val

    # 출력 (SWEA 형식)
    print(f"#{test_case} {result}")
