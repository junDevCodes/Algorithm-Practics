# BOJ 17070 문제 풀이
import sys
from pathlib import Path

# 파일 입력 설정 (로컬 테스트용)
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')

"""
[문제 설명]
집은 N*N 크기의 격자판
초기 파이프는 (1, 1), (1, 2)를 차지하고 있고 방향은 가로이다
파이프는 가로, 대각, 세로 상태가 있고
밀 수 있는 방향은 가로인 경우 2가지, 세로인 경우 2가지, 대각인 경우 3가지가 있다.
파이프의 한쪽 끝을 (N, N)으로 이동시키는 방법의 갯수를 구해보자
이동 시킬 수 없는 경우 0 을 출력한다. 

[입력]
0. TC
1. 방의 총 사이즈이자 최종 위치

[출력]
N, N으로 이동시키는 방법의 수를 출력한다
이동 시킬 수 없는 경우 0을 출력한다.

[알고리즘]
DFS
1. 두 좌표의 상태를 받는다
2. row가 같은 경우 가로, col이 같은 경우 세로, 각각의 가로, 세로가 1씩 차이나면 대각으로 판단하고
모든 상황에 대해 DFS 실행 두 좌표 중 하나가 N, N에 도달 시 return후 count 추가
3. 벽은 1로 주어지고 1이 있는경우 그 방형은 갈 수 없다.

[예시]
3
0 0 0
0 0 0
0 0 0

출력:
1
"""


count = 0

def dfs(start_pipe, end_pipe, target_idx, map_info):
    global count

    s_row, s_col = start_pipe[0], start_pipe[1]
    e_row, e_col = end_pipe[0], end_pipe[1]

    if (e_row, e_col) == (target_idx, target_idx):
        count += 1
        return

    n_s_pipe = (e_row, e_col)

    if s_row == e_row:  # 가로 상태
        if e_col + 1 <= target_idx and not map_info[e_row][e_col+1]: # 맵 밖으로 나가지 않고 벽이 아니라면
            dfs(n_s_pipe, (e_row, e_col+1), target_idx, map_info) # 가로로 한번 더

        if e_col + 1 <= target_idx and e_row + 1 <= target_idx \
            and not map_info[e_row][e_col+1] \
            and not map_info[e_row+1][e_col] \
            and not map_info[e_row+1][e_col+1]: # 맵 밖으로 나가지 않고 벽이 아니라면
            dfs(n_s_pipe, (e_row+1, e_col+1), target_idx, map_info) # 대각으로 한번 더

    elif s_col == e_col:  # 세로 상태
        if e_row + 1 <= target_idx and not map_info[e_row+1][e_col]: # 맵 밖으로 나가지 않고 벽이 아니라면
            dfs(n_s_pipe, (e_row+1, e_col), target_idx, map_info) # 세로로 한번 더

        if e_col + 1 <= target_idx and e_row + 1 <= target_idx \
            and not map_info[e_row][e_col+1] \
            and not map_info[e_row+1][e_col] \
            and not map_info[e_row+1][e_col+1]: # 맵 밖으로 나가지 않고 벽이 아니라면
            dfs(n_s_pipe, (e_row+1, e_col+1), target_idx, map_info) # 대각으로 한번 더

    else:  # 대각 상태
        if e_col + 1 <= target_idx and not map_info[e_row][e_col+1]: # 맵 밖으로 나가지 않고 벽이 아니라면
            dfs(n_s_pipe, (e_row, e_col+1), target_idx, map_info) # 가로로 한번 더

        if e_row + 1 <= target_idx and not map_info[e_row+1][e_col]: # 맵 밖으로 나가지 않고 벽이 아니라면
            dfs(n_s_pipe, (e_row+1, e_col), target_idx, map_info) # 세로로 한번 더

        if e_col + 1 <= target_idx and e_row + 1 <= target_idx \
            and not map_info[e_row][e_col+1] \
            and not map_info[e_row+1][e_col] \
            and not map_info[e_row+1][e_col+1]: # 맵 밖으로 나가지 않고 벽이 아니라면
            dfs(n_s_pipe, (e_row+1, e_col+1), target_idx, map_info) # 대각으로 한번 더
        


def solve():
    global count
    T = int(sys.stdin.readline().strip())

    for tc in range(1, T + 1):
        count = 0
        map_size = int(sys.stdin.readline().strip())
        map_info = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(map_size)]

        start_pipe = (0, 0)
        end_pipe = (0, 1)

        dfs(start_pipe, end_pipe, map_size-1, map_info)

        print(count)

solve()
