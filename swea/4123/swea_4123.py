# SWEA 4123 문제 풀이
# import sys
#
# sys.stdin = open('sample_input.txt', 'r', encoding='utf-8')

"""
[문제 설명]
고정된 숫자 배치에
연산자를 배치하여
최대 수식의 계산 결과 - 최소 수식의 계산결과

[입력]
1. tc
2. num_len
3. 연산자의 갯수 +, -, *, /
4. 수식 숫자

[출력]
최대 - 최소

[알고리즘]
dfs를 통한 완탐 혹은 iter tools 조합
"""


def dfs(idx, current_val, op_list, nums):
    global min_val, max_val

    if idx == len(nums):
        max_val = max(max_val, current_val)
        min_val = min(min_val, current_val)
        return

    for op_idx in range(4):
        if op_list[op_idx] > 0:
            op_list[op_idx] -= 1

            next_val = 0
            if op_idx == 0:
                next_val = current_val + nums[idx]
            elif op_idx == 1:
                next_val = current_val - nums[idx]
            elif op_idx == 2:
                next_val = current_val * nums[idx]
            elif op_idx == 3:
                if current_val < 0:
                    next_val = -(-current_val // nums[idx])
                else:
                    next_val = current_val // nums[idx]

            dfs(idx + 1, next_val, op_list, nums)

            op_list[op_idx] += 1


def solve():
    global min_val, max_val
    T = int(input())
    # T = int(sys.stdin.readline().strip())

    for test_case in range(1, T + 1):
        # num_len = int(sys.stdin.readline().strip())
        num_len = int(input())
        # operator_list = list(map(int, sys.stdin.readline().strip().split()))
        operator_list = list(map(int, input().split()))
        # num_list = list(map(int, sys.stdin.readline().strip().split()))
        num_list = list(map(int, input().split()))

        min_val = float('inf')
        max_val = float('-inf')

        dfs(1, num_list[0], operator_list, num_list)

        result = max_val - min_val
        print(f"#{test_case} {result}")


solve()
