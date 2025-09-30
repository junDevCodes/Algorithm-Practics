# SWEA 5189 문제 풀이
# import sys
# from pathlib import Path
#
# # 파일 입력 설정 (로컬 테스트용)
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')

"""
[문제 설명]
인접행렬로 주어진다
1번은 사무실
2~N번까지는 관리 구역이다
모든 관리구역을 다 순회하고 사무실로 돌아오는 최소 배터리 사용량을 구하시오 

[입력]
0. TC
1. sector_num
2. map_info

[출력]
1. 최소 배터리 사용량

[알고리즘]
dfs 백트래킹 사용
visited를 통해 관리구역 순회 관리
s_idx, e_idx 관리 통해 dfs 관리
"""
def dfs(c_sector, c_val, visit):
    global sector_num, min_battery

    if visit == sector_num:
        c_val += map_info[c_sector][0]
        min_battery = min(min_battery, c_val)
        return

    if c_val > min_battery:
        return

    for n_sector in range(1, sector_num):
        if c_sector == n_sector: continue
        if visited[n_sector]: continue

        visited[n_sector] = True
        dfs(n_sector, c_val + map_info[c_sector][n_sector], visit + 1)
        visited[n_sector] = False

# SWEA 테스트 케이스 처리 템플릿
# T = int(sys.stdin.readline())
T = int(input())

for test_case in range(1, T + 1):
    # 입력 처리
    # sector_num = int(sys.stdin.readline())
    sector_num = int(input())

    # map_info = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(sector_num)]
    map_info = [list(map(int, input().split())) for _ in range(sector_num)]
    visited = [False] * sector_num

    min_battery = float("inf")

    dfs(0, 0, 1)
    
    # 출력 (SWEA 형식)
    print(f"#{test_case} {min_battery}")
