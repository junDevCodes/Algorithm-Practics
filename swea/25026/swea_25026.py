# SWEA 25026 문제 풀이
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
실력 편차가 K이내인 팀 중 가장 많은 인원수의 팀

[입력]
1. TC
2. player, gap
3. player_list

[출력]
가장 많은 인원수

[로직]
리스트 순회 차이 나면 count list 담기
max_count 출력

[예시 입력]
3
4 2
6 4 2 3
4 1
1 3 7 5
10 4
12 7 3 2 12 20 5 20 2 7

[예시 출력]
#1 3
#2 1
#3 4
"""
T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    # player, gap = map(int, sys.stdin.readline().strip("\n").split())
    player, gap = map(int, input().split())
    # print(player, gap)

    # player_list = list(map(int, sys.stdin.readline().strip("\n").split()))
    player_list = list(map(int, input().split()))
    player_list.sort(reverse=True)
    # print(player_list)

    count_list = []

    for standard_player in range(player):
        count = 0
        for compare_idx in range(standard_player, player):
            if 0 <= (player_list[standard_player] - player_list[compare_idx]) <= gap:
                count += 1
        count_list.append(count)

    # print(count_list)

    print(f"#{test_case} {max(count_list)}")
