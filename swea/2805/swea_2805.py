# SWEA 2805 문제 풀이
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
여기에 문제 요약과 요구사항을 작성하세요.

[입력]
- 입력 형식에 대한 설명
- 각 줄별 입력 내용

[출력]
- 출력 형식에 대한 설명

[로직]
- 문제 해결에 필요한 알고리즘

[예시 입력]
예시 입력 내용을 작성

[예시 출력]
예시 출력 내용을 작성
"""
T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    # map_size = int(sys.stdin.readline().strip("\n"))
    map_size = int(input())
    # map_list = [list(sys.stdin.readline().strip("\n")) for _ in range(map_size)]
    map_list = [list(input()) for _ in range(map_size)]
    # print(map_list)

    square_delta_list = []
    cnt_even = 0
    even_list = []
    for i in range(1, map_size + 1):
        if i % 2 == 1:
            square_delta_list.append(i)
        else:
            even_list.append(cnt_even)
            cnt_even += 1

    even_list.sort(reverse=True)
    for idx in even_list:
        square_delta_list.append(square_delta_list[idx])

    sum = 0
    for col in range(map_size):
        cnt_idx = square_delta_list[col]
        sum_idx = (map_size - cnt_idx) // 2
        for plus_row in range(cnt_idx):
            sum += int(map_list[col][sum_idx + plus_row])

    print(f"#{test_case} {sum}")
