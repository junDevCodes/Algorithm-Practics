import sys
from pathlib import Path
from collections import deque

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')

"""
[문제]
자석 1칸을 K번 회전할 때 붙어있는 자석은 서로 붙어있는 날의 자성과 다를경우 반대방향 1칸 회전

모든 자석 N극 0점
1번 자석 S극 1점
2번 자석 S극 2점
3번 자석 S극 4점
4번 자석 S극 8점

회전 방향은 시계 1, 반시계 -1

자성은 N극 0, S극 1로 주어짐

0~7번까지 톱날이 주어지고
화살표는 7번 톱날을 가르킴


[입력]
1. TC
2. 회전 횟수
3. 1~4번 자석 자성정보

[출력]
1. #TC 0번의 점수

[로직]
deque pop left

saw[0][1] != saw[1][5]
각 톱니의 1번과 5번이 다르게 되면 돌리는 방향 반대로 움직이기


[예시 입력]
10

2

0 0 1 0 0 1 0 0

1 0 0 1 1 1 0 1

0 0 1 0 1 1 0 0

0 0 1 0 1 1 0 1

1 1

3 -1

[예시 출력]
#1 10
"""

T = int(sys.stdin.readline().strip())

for test_case in range(1, T + 1):
    rotate_count = int(sys.stdin.readline().strip())
    print(rotate_count)

    saw_tooth_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(4)]
    print(saw_tooth_list)

    rotate_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(rotate_count)]
    print(rotate_list)



    print(f"#{test_case}")