# import sys
# from pathlib import Path
#
# BASE_DIR = Path(__file__).parent.resolve()
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')

"""
[문제]
각 변에 16진수 숫자
시계방향 회전
각 변에 동일한 갯수의 숫자

K번째로 큰 수를 10진수로 만든 수

N은 4의 배수

[입력]
0. TC
1. N, K
2. num_info

[출력]
K번째 16진수 -> 10진수

[로직]
deque

"""

from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    num_info = list(map(str, input()))

    len_word = N // 4
    result = 0
    num_set = set()

    num_queue = deque(num_info)
    for idx in range(len_word):
        c_num_info = list(num_queue)
        num_set.add("".join(c_num_info[len_word*0:len_word]))
        num_set.add("".join(c_num_info[len_word*1:len_word*2]))
        num_set.add("".join(c_num_info[len_word*2:len_word*3]))
        num_set.add("".join(c_num_info[len_word*3:len_word*4]))
        num_queue.rotate(1)

    num_list = []
    for item in num_set:
        num_list.append(int(item, 16))

    num_list.sort(reverse=True)

    result = num_list[K-1]

    print(f"#{tc} {result}")