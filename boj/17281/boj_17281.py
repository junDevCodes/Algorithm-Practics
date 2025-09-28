# BOJ 17281 문제 풀이
import sys
from pathlib import Path

# 파일 입력 설정 (로컬 테스트용)
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')

"""
[문제 설명]
경기 시작 전 타순을 정하고 경기중에는 변경할 수 없다
9번타자 이후는 1번타자이고 이닝이 변경되어도 순서를 유지한다.

공격은 다음과 같아
안타 : 타자와 모든 주자가 한 루씩 진루
2루타 : 타자와 모든 주자가 두 루씩 진루
3루타 : 타자와 모든 주자가 세 루씩 진루
홈런 : 타자와 모든 주자가 홈까지 진루
아웃 : 모든 주자는 진루하지 못하고, 아웃카운트 증가

1번 타자를 4번 타순에 정했다
나머지 타순을 정해야 한다
각 선수가 각 이닝에서 어떤 결과를 얻는지 미리 알고 있다
가장 많은 득점을 하는 타순에서 그때의 득점을 구하라

안타: 1
2루타: 2
3루타: 3
홈런: 4
아웃: 0

[입력]
1. 이닝
2. 1~9번까지의 선수의 N번 이닝의 결과

[출력]
5~9번의 타순을 조정하여 최대 득점을 구하라

[알고리즘]
dfs
현재 이닝수와 진행 index 기록
3 아웃이면 이닝 넘기기

1234 고정이므로 5~9까지 조합하기

[예시]
2
4 0 0 0 0 0 0 0 0
4 0 0 0 0 0 0 0 0

출력:
1
"""
from collections import deque

innings = 0
innings_info = []
lineup = [0] * 10
player_used = [False] * 10
max_score = 0


def dfs(current_batter_idx):
    global max_score

    # 기저 사례: 9번 타순까지 모두 정해졌다면 경기를 시뮬레이션
    if current_batter_idx == 10:
        max_score = max(max_score, play_game())
        return

    # 1번 타자는 4번 타순에 고정
    if current_batter_idx == 4:
        lineup[current_batter_idx] = 1
        dfs(current_batter_idx + 1)
        return

    # 나머지 8명의 선수로 타순 배치
    for player in range(2, 10):
        if not player_used[player]:
            lineup[current_batter_idx] = player
            player_used[player] = True
            dfs(current_batter_idx + 1)
            player_used[player] = False  # 백트래킹


def play_game():
    global innings, lineup, innings_info
    player_idx = 0
    score = 0
    for inning in range(1, innings+1):
        base = deque([0,0,0,0])
        out_count = 0
        while out_count != 3:
            c_player = innings_info[inning][player_idx]
            if c_player == 0:
                out_count += 1
            else:
                base[0] = player_idx
                for run in range(c_player):
                    base.rotate(1)
                    if base[0] != 0:
                        score += 1
                        base[0] = 0

            if player_idx == 9:
                player_idx = 1
            else:
                player_idx += 1
    return score

def solve():
    global innings, innings_info, lineup, player_used, max_score

    T = int(sys.stdin.readline().strip())
    for tc in range(1, T + 1):
        innings = int(sys.stdin.readline().strip())
        innings_info = [[]]+[[0]+list(map(int, sys.stdin.readline().strip().split())) for _ in range(innings)]

        lineup[4] = 1
        player_used[1] = True

        dfs(1)

        print(max_score)

solve()