# SWEA 24973 문제 풀이
# import sys
# from pathlib import Path
#
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')

# T = int(sys.stdin.readline().strip("\n"))
"""
[문제 설명]
2차원 지도 정보
각 칸에 해당하는 고유 높이

가장 높은곳에서 출발
델타 탐색 후 가장 낮은 칸으로만 이동
더이상 이동할 수 없을 때 이동한 총 칸수
시작 지점 포함

[입력]
1. tc
2. map_size
3. mount_list

[출력]
1. #tc, move_count

[로직]
제일 높은 곳에서 지점부터 델타 탐색
델타 탐색 값이 현재 값과 같거나 큰 경우까지
나보다 작은 경우 가장 작은 값의 위치로 이동후 move_count += 1
델타 돌렸는데 자기 자신이 제일 작으면 종료
[예시 입력]3
5
20 19 18 17 16
15 14 13 12 11
4  5  6  7  10
3  2  1  8  9
6  7  8  9  10
4
50 49 48 30
10 12 13 29
11 15 16 28
50 45 46 27
5
40 39 38 37 36
30 25 24 23 35
29 20 10 22 34
28 19 12 18 33
27 26 13 14 32

[예시 출력]
#1 6
#2 3
#3 5
"""


def find_route(mountain, start_x, start_y):
    size = len(mountain)
    start_val = mountain[start_y][start_x]
    min_val = start_val
    count_val = 1

    while 1:
        for delta in delta_list:
            next_y = start_y + delta[0]
            next_x = start_x + delta[1]
            if 0 <= next_y < size and 0 <= next_x < size:
                cal_val = mountain[next_y][next_x]
                if cal_val < min_val:
                    min_val = cal_val
                    min_idx_x = next_x
                    min_idx_y = next_y

        if start_val != min_val:
            start_y = min_idx_y
            start_x = min_idx_x
            count_val += 1
            start_val = min_val
        else:
            break

    return count_val


def find_start(mountain):
    max_val = [0, 0, 0]
    start_x = []
    start_y = []
    for col in range(len(mountain)):
        for row in range(len(mountain[0])):
            if max_val[0] < mountain[col][row]:
                max_val[0] = mountain[col][row]
                max_val[1] = col
                max_val[2] = row

    for col in range(len(mountain)):
        for row in range(len(mountain[0])):
            if max_val[0] == mountain[col][row]:
                start_y.append(col)
                start_x.append(row)

    return start_y, start_x


T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
delta_list = [(0, -1), (0, 1), (-1, 0), (1, 0)]
for test_case in range(1, T + 1):
    # map_size = int(sys.stdin.readline().strip("\n"))
    map_size = int(input())
    # print(map_size)

    # mount_list = [list(map(int, sys.stdin.readline().strip("\n").split())) for _ in range(map_size)]
    mount_list = [list(map(int, input().split())) for _ in range(map_size)]
    # print(mount_list)

    start_y, start_x = find_start(mount_list)

    max_count_step = 0
    for idx in range(len(start_y)):
        count_step = find_route(mount_list, start_x[idx], start_y[idx])
        max_count_step = max(count_step, max_count_step)
    print(f"#{test_case} {max_count_step}")
