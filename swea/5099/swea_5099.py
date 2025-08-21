# SWEA 5099 문제 풀이
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
피자는 1번 위치에서 넣거나 뺄 수 있다
피자는 1번부터 N번까지 순서대로 굽는다
피자는 1번에서 치즈를 확인하고 다시 넣을 수 있다
M개의 피자에 처음 뿌려진 치즈의 양이 주어진다
화덕을 한바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다
치즈가 모두 녹아 0이 되면 화덕에서 꺼내고 바로 그 자리에 남은 피자를 순서대로 넣는다.

[입력]
1. TC
2. 화덕의 크기, 피자 개수
3. 피자에 뿌려진 치즈 양

[출력]
가장 마지막에 남는 피자 번호

[로직]
- 문제 해결에 필요한 알고리즘

[예시 입력]
3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2

[예시 출력]
#1 4
#2 8
#3 6

"""

from collections import deque

T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    # oven_size, pizza_num = map(int, sys.stdin.readline().strip("\n").split())
    oven_size, pizza_num = map(int, input().split())
    # pizza_list = list(map(int, sys.stdin.readline().strip("\n").split()))
    pizza_list = list(map(int, input().split()))
    oven = deque()

    for idx in range(1, oven_size + 1): # 초기 피자 넣기
        oven.append([idx, pizza_list[idx - 1]])

    current_pizza = oven_size # 다음 넣을 피자 준비
    last_pizza = 0
    while oven:
        oven[0][1] = oven[0][1] // 2 # 한바퀴 돌고 온 피자 치즈 변경
        if oven[0][1] == 0: # 계산 후 0이 된 피자는 뺀다.
            current_pizza += 1
            out_pizza = oven.popleft()
            if current_pizza <= pizza_num:
                oven.appendleft([current_pizza, pizza_list[current_pizza - 1]])
                oven.rotate(-1)
            last_pizza = out_pizza[0]
        else:
            oven.rotate(-1)
    print(f"#{test_case} {last_pizza}")
