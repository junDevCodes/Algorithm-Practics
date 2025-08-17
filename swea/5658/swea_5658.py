# import sys
# from pathlib import Path
from collections import deque

# BASE_DIR = Path(__file__).parent.resolve()
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')

"""
[문제]
숫자가 마름모 모양으로 각변마다 N개씩 묶어져 있다
한번 돌릴 때 마다 시계방향으로 한 칸씩 회전한다.
적힌 수로 만들 수 있는 모든 수 중 K번째로 큰 수를 10진수로 출력

N은 4의 배수
[입력]
1. TC
2. 숫자갯수, N번째 비밀번호
3. 숫자 정보

[출력]
만들 수 있는 숫자 조합 중 N번째 비밀번호를 10진수 변환한 것

[로직]
먼저 원형 큐에 숫자들을 담고, 숫자갯수 / 4 칸씩 분리해서 set리스트에 담기

set의 갯수가 늘어나면 진행 set의 갯수가 늘어나지 않으면 더이상 반복되지 않음으로 종료

이후 set을 정렬 후 N번째 리스트 값 출력

[예시 입력]
5
12 10
1B3B3B81F75E
16 2
F53586D76286B2D8

[예시 출력]
#1 503
#2 55541
#3 334454
#4 5667473
#5 182189737

"""

# T = int(sys.stdin.readline().strip())
T = int(input())

for test_case in range(1, T + 1):
    # num, target_idx = map(int, sys.stdin.readline().strip().split())
    num, target_idx = map(int, input().split())
    rotate_num = int(num / 4)
    # print(num, target_idx, rotate_num)

    # num_queue = deque(list(sys.stdin.readline().strip()))
    num_queue = deque(list(input()))
    # print(num_queue)

    set_list = set({})
    for _ in range(rotate_num):
        result = ""
        for idx in range(1, num+1):
            result += num_queue[idx-1]
            if idx % rotate_num == 0:
                set_list.add(result)
                result = ""
        num_queue.rotate(1)

    num_list = []
    for item in set_list:
        num_list.append(int(item, 16))

    num_list.sort(reverse=True)
    # print(num_list)

    print(f"#{test_case} {num_list[target_idx-1]}")