# SWEA 1974 문제 풀이
# import sys
# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')
# T = int(sys.stdin.readline().strip("\n"))
"""
검사 리스트 생성 [1~9]
sudoku_map의 가로줄 검사 후 검사 리스트의 모든 값이 1이어야함
세로줄 검사 후 검사 리스트의 값이 모두 1이어야함
target_idx 생성 후 union 통해 리스트 비교
"""
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # sudoku_map = [list(map(int, sys.stdin.readline().strip("\n").split())) for _ in range(9)]
    sudoku_map = [list(map(int, input().split())) for _ in range(9)]
    # print(sudoku_map)

    check_list = [i for i in range(1, 10)]
    # print(check_list)

    check_row = 0
    check_col = 0
    check_small_map = 0
    check_map = 0

    for line in sudoku_map: # 가로줄 검사
        if sorted(line) == check_list:
            check_row += 1

    for item in zip(*sudoku_map): # 세로줄 검사
        if sorted(list(item)) == check_list:
            check_col += 1

    """
    00, 03, 06
    30, 33, 36
    60, 63, 66
    """
    target_idx = [
        (0, 0), (0, 3), (0, 6),
        (3, 0), (3, 3), (3, 6),
        (6, 0), (6, 3), (6, 6)
    ]

    for real_idx_col, real_idx_row in target_idx:
        small_map_list = []
        for idx in range(3):
            small_map_list += sudoku_map[real_idx_col+idx][real_idx_row:real_idx_row+3]
        if sorted(small_map_list) == check_list:
            check_small_map += 1

    check_map = int(all(x == 9 for x in [check_row, check_col, check_small_map]))

    print(f"#{test_case} {check_map}")
