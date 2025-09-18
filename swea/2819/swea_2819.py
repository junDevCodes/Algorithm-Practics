
  # SWEA 2819 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
4x4 격자판에서 동서남북 네 방향으로 이동하며
서로 다른 7개의 숫자열의 갯수

[입력]
0. TC
1. 격자판

[출력]
1. 서로 다른 7개의 숫자열의 갯수

[알고리즘]
1. DFS
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""


def dfs(c_row, c_col, str_lst):

    if len(str_lst) == 7:
        num_set.add("".join(map(str, str_lst)))
        return

    str_lst.append(map_info[c_row][c_col])

    for d_row, d_col in delta_list:
        n_row, n_col = c_row + d_row, c_col + d_col
        if 0 <= n_row < 4 and 0 <= n_col < 4:
            dfs(n_row, n_col, str_lst)
    str_lst.pop()


# T = int(sys.stdin.readline().strip())
T = int(input())

delta_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for test_case in range(1, T + 1):
    # 입력
    # map_info = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(4)]
    map_info = [list(map(int, input().split())) for _ in range(4)]

    num_set = set()
    for row in range(4):
        for col in range(4):
            word = []
            dfs(row, col, word)

    # 로직
    result = len(num_set)
    
    # 출력 (SWEA 형식)
    print(f"#{test_case} {result}")
