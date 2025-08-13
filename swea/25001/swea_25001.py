# SWEA 25001 문제 풀이
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
홀수 쨋날에 물을 준 경우 키가 1이 자라고
짝수 쨋날에 물을 준 경우 키가 2가 자란다

하루에 나무 하나만 물을 줄 수 있다
물을 주지 않을 수 도 있다

가장 키가 컸던 나무와 모든 나무가 키가 같아지도록 할 수 있는 최소 날짜 수

[입력]
1. TC
2. 나무 그루 수
3. 나무 정보

[출력]
모든 나무 높이가 같아지는 최소 날짜 수

[로직]
최대 높이를 구한다
각 나무마다 높이 차이가 얼마나는지 구한다

홀수로 나는 경우 홀수 날을 무조건 거쳐야 함
짝수로 나는 경우 안주는 선택지 고려 가능

+ 0, 1, 2 가능


[예시 입력]
3
2
5 5
4
2 3 10 5
4
1 2 3 4

[예시 출력]
#1 0
#2 14
#3 4
"""
T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    # tree = int(sys.stdin.readline().strip("\n"))
    tree = int(input())
    # print(tree)

    # tree_list = list(map(int, sys.stdin.readline().strip("\n").split()))
    tree_list = list(map(int, input().split()))
    # print(tree_list)

    max_height = max(tree_list)
    # print(max_height)

    gap_count = 0
    for height in tree_list:
        gap_count += max_height - height
    # print(gap_count)

    day_count = 0
    while 0 < gap_count:
        day_count += 1
        if day_count % 2 == 1:
            gap_count -= 1
        elif day_count % 2 == 0:
            gap_count -= 2

    print(f"#{test_case} {day_count}")
