# BOJ 17070 문제 풀이
# import sys
# from pathlib import Path
#
# # 파일 입력 설정 (로컬 테스트용)
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')

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

memo = {}
map_info = []
map_size = 0

def dfs_memo(e_row, e_col, direction):
    global map_size, map_info

    if (e_row, e_col, direction) in memo:
        return memo[(e_row, e_col, direction)]

    if e_row == map_size-1 and e_col == map_size-1:
        return 1

    count = 0

    # 가로 이동 (현재 가로 또는 대각선 상태에서 가능)
    if direction == 0 or direction == 2:
        if e_col + 1 < map_size and not map_info[e_row][e_col + 1]:
            count += dfs_memo(e_row, e_col + 1, 0)

    # 세로 이동 (현재 세로 또는 대각선 상태에서 가능)
    if direction == 1 or direction == 2:
        if e_row + 1 < map_size and not map_info[e_row + 1][e_col]:
            count += dfs_memo(e_row + 1, e_col, 1)

    # 대각선 이동 (모든 상태에서 가능)
    if e_col + 1 < map_size and e_row + 1 < map_size and \
            not map_info[e_row][e_col + 1] and \
            not map_info[e_row + 1][e_col] and \
            not map_info[e_row + 1][e_col + 1]:
        count += dfs_memo(e_row + 1, e_col + 1, 2)

    memo[(e_row, e_col, direction)] = count
    return count


def solve():
    global map_size, map_info
    # T = int(sys.stdin.readline().strip())

    # for tc in range(1, T + 1):
    count = 0
    # map_size = int(sys.stdin.readline().strip())
    # map_info = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(map_size)]
    map_size = int(input())
    map_info = [list(map(int, input().split())) for _ in range(map_size)]

    if map_info[map_size-1][map_size-1] == 1:
        print(0)
        return

        # 시작 지점 바로 오른쪽에 벽이 있다면 0 반환
    if map_info[0][1] == 1:
        print(0)
        return

    count = dfs_memo(0, 1, 0)
    print(count)

solve()
