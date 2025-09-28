# SWEA 1244 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
숫자판과 회전 횟수가 주어진다 최대 금액을 출력하시오

[입력]
0. TC
1. num, rotate_num

[출력]
최대 금액

[알고리즘]
1. dfs
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""


def dfs(num_list, rotate):
    global max_num

    num_str = "".join(map(str, num_list))

    if (num_str, rotate) in memo:
        return memo[(num_str, rotate)]

    if rotate == 0:
        return int(num_str)

    max_val = 0

    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):  # 중복 방지
            # 교환
            num_list[i], num_list[j] = num_list[j], num_list[i]

            # 재귀 호출해서 결과 받기
            result = dfs(num_list, rotate - 1)
            max_val = max(max_val, result)

            # 되돌리기
            num_list[i], num_list[j] = num_list[j], num_list[i]

        # 결과를 메모에 저장하고 반환
    memo[(num_str, rotate)] = max_val
    return max_val


T = int(input())
memo = {}

for test_case in range(1, T + 1):
    # 입력
    # num, rotate_num = map(int, sys.stdin.readline().strip().split())
    num, rotate_num = map(int, input().split())
    num = list(str(num))

    max_num = dfs(num, rotate_num)
    
    # 출력 (SWEA 형식)
    print(f"#{test_case} {max_num}")
