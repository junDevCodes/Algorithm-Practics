# import sys
# from pathlib import Path
#
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')

"""
[문제]
크기가 N x N 인 단어 퍼즐
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리수를 출력

[입력]
1. TC
2. map_size, len_word
3. map_info_list

[출력]
len_word가 들어갈 수 있는 자리 수 count

[로직]
col 별 low 별 len count
1일 때는 count += 1
0을 만나면 초기화
한줄에 두개의 1이 있는경우 대비 초기화 전 배열에 저장

[예시 입력]
10
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
5 3
1 0 0 1 0
1 1 0 1 1
1 0 1 1 1
0 1 1 0 1
0 1 1 1 0

[예시 출력]
#1 2
#2 6
"""

# T = int(sys.stdin.readline().strip())
T = int(input())

for test_case in range(1, T + 1):
    # map_size, len_word = map(int, sys.stdin.readline().strip().split())
    map_size, len_word = map(int, input().split())
    # print(map_size, len_word)

    # map_info_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(map_size)]
    map_info_list = [list(map(int, input().split())) for _ in range(map_size)]
    # print(map_info_list)

    rotate_map_info_list = list(zip(*map_info_list))
    # print(rotate_map_info_list)

    count_map_list = []
    for col in range(map_size):
        count = 0
        rotate_count = 0
        for row in range(map_size):
            if map_info_list[col][row] == 1:
                count += 1
            elif map_info_list[col][row] == 0:
                if count:
                    count_map_list.append(count)
                count = 0

            if rotate_map_info_list[col][row] == 1:
                rotate_count += 1
            elif rotate_map_info_list[col][row] == 0:
                if rotate_count:
                    count_map_list.append(rotate_count)
                rotate_count = 0

        if count:
            count_map_list.append(count)
        if rotate_count:
            count_map_list.append(rotate_count)

    total_count = 0
    for val in count_map_list:
        if val == len_word:
            total_count += 1

    print(f"#{test_case} {total_count}")