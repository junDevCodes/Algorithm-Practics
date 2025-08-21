# SWEA 1225 문제 풀이
# import sys
# from pathlib import Path
#
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')

"""
[문제 설명]
8자리의 암호를 생성한다

8개의 숫자를 입력받고
첫번째 숫자를 1 감소 시킨 후 맨뒤로 보낸다
다음 첫번째 숫자는 2 감소 시킨 후 맨 뒤로 보낸다
숫자가 감소할 때 0 이하로 감소되는 경우 0으로 유지되고 프로그램이 종료된다.

[입력]
TC = 10
1. test_case_num
2. 숫자 8개

[출력]
1. #{tc} {최종 완성된 8자리의 암호}

[로직]
deque로 rotate와 turn에 따라 감소되도록

[예시 입력]
1
9550 9556 9550 9553 9558 9551 9551 9551
2
2419 2418 2423 2415 2422 2419 2420 2415

[예시 출력]
#1 6 2 2 9 4 1 3 0
#2 9 7 9 5 4 3 8 0

"""

from collections import deque

T = 10  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    # tc = int(sys.stdin.readline().strip())
    tc = int(input())
    # num_list = deque(list(map(int, sys.stdin.readline().strip().split())))
    num_list = deque(list(map(int, input().split())))

    turn = 0
    while 1:
        num_list[0] -= (turn % 5) + 1
        num_list.rotate(-1)
        turn += 1
        if num_list[-1] <= 0:
            num_list[-1] = 0
            break

    print(f"#{test_case} {' '.join(map(str, num_list))}")
