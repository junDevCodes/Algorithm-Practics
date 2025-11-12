# SWEA 2105 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
한 변의 길이 N

원 안의 숫자는 디저트의 종류

카페는 대각선으로 이동

같은 종류 디저트 안됨

왔던길 되돌아가는거 안됨

원점으로 돌아올 때 가장 많이 먹을 수 있는 경로 찾기, 그때의 디저트 수 출력
못먹으면 -1 출력

[조건]


[입력]


[출력]


[알고리즘]
1. dfs 직진 or 회전
2. set 디저트 종류
3. visited

[복잡도]
- 시간: O()
- 공간: O()
"""
max_len_dessert = 0
d_list = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def dfs(board, r, c, start_coord, dessert, visited, way):
    global max_len_dessert, d_list

    N = len(board)

    if (r, c) == start_coord and way == 3: # 시작지점으로 돌아오게되면 정상 종료
        max_len_dessert = max(max_len_dessert, sum(dessert))

    if dessert[board[r][c]] == 1: # 이미 같은 종류의 디저트가 있으면 비정상 종료
        return

    if visited[r][c] == 1: # 이미 방문한적이 있다면 비정상 종료
        return
    else:
        visited[r][c]= 1
        dessert[board[r][c]] = 1

    dr, dc = d_list[way]
    if 0 <= r + dr < N and 0 <= c + dc < N:
        dfs(board, r + dr, c + dc, start_coord, dessert, visited, way)

    if way < 3:
        rt_dr, rt_dc = d_list[way + 1]
        if 0 <= r + rt_dr < N and 0 <= c + rt_dc < N:
            dfs(board, r + rt_dr, c + rt_dc, start_coord, dessert, visited, way + 1)

    visited[r][c] = 0
    dessert[board[r][c]] = 0

    return


def solve():
    global max_len_dessert

    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        board = [list(map(int, input().split())) for _ in range(N)]

        max_len_dessert = 0
        dessert = [0] * 101
        for r in range(N-2):
            for c in range(1, N-1):
                visited = [[0] * N for _ in range(N)] # 대각선 한칸 아래로 시작
                dfs(board, r, c, (r, c), dessert, visited, 0)

        if max_len_dessert == 0:
            max_len_dessert = -1
        print(f"#{test_case} {max_len_dessert}")
        

solve()

