# SWEA 4615 문제 풀이
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')

T = int(sys.stdin.readline().strip("\n"))
"""
[문제 설명]
오셀로 게임 규칙 :
    4, 6, 8보드 중 하나를 골라
    돌을 놓는다 돌의 기본 배치는 보드 정중앙에 아래와 같이 둔다
    ---------
    | W | B |
    |-------|
    | B | W |
    ---------
    자신이 놓을 돌의 위치와 자신의 돌 사이에 상대방의 돌이 있는 경우에만 그 곳에 돌을 놓을 수 있고,
    그 때 상대방의 돌을 자신의 돌로 만들 수 있다.
    
    만약 돌을 놓을 곳이 없다면 상대방이 다시 돌을 놓는다

승리조건 : 
    보드에 빈 곳이 없거나 양 플레이어 모두 돌을 놓을 곳이 없으면 게임이 끝난다.
    그 때 보드에 있는 돌의 개수가 많은 플레이어가 승리하게 된다.

[입력]
1. TC
2. 보드 사이즈, 돌을 놓는 횟수
3. X, Y, 돌 색(B : 1, 2 : W)

[출력]
#TC (흑, 백) 돌 개수

[로직]
초반 정가운데 돌 놓기

돌 놓게되면 델타 탐색으로 방향 찾기
방향으로 스택에 담기
ex) BWWWB인 경우 닫히게 되면 종료 전부 B로 반환하며 역방향으로 다시 채우기

이후 맵 전체 순회 이후 각각 COUNT 

[예시 입력]
1
4 12
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2

[예시 출력]
#1 0 16
"""
# T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
delta_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
color_stone = {
    1: "B",
    2: "W"
}


def check_delta(othello_map, col, row):
    result = ""
    for delta in delta_list:
        if 0 <= col+delta[0] < len(othello_map) and 0 <= row+delta[1] < len(othello_map[0]):
            if othello_map[col+delta[0]][row+delta[1]] == 0:
                result = "zero---------------------------------------------"
            elif othello_map[col][row] != othello_map[col+delta[0]][row+delta[1]]:
                result = "different----------------------------------------"
            elif othello_map[col][row] == othello_map[col+delta[0]][row+delta[1]]:
                result = "same---------------------------------------------"
    pass

for test_case in range(1, T + 1):
    map_size, total_turn = map(int, sys.stdin.readline().strip("\n").split())
    print(map_size, total_turn)

    othello_map = [([0] * map_size) for i in range(map_size)] # map_size * map_size 의 othello_map 선언

    for col in range(((map_size//2)-1), ((map_size//2)+1)): # 정가운데를 순회
        for row in range(((map_size//2)-1), ((map_size//2)+1)):
            if col == row:
                othello_map[col][row] = "W" # 정대각선에 W
            elif (map_size-1) - col == row:
                othello_map[col][row] = "B" # 역대각선에 B
    print(othello_map)

    for turn in range(total_turn):
        turn_y, turn_x, turn_color = map(int, sys.stdin.readline().strip("\n").split()) # 돌 놓기 입력 받기

        othello_map[turn_y-1][turn_x-1] = color_stone[turn_color] # 돌 놓기

        check_delta(othello_map, turn_y-1, turn_x-1)

    print(f"#{test_case}")
    print(othello_map)

