# import sys
# from pathlib import Path
#
# # 파일 입력 설정 (로컬 테스트용)
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')

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
import sys
from itertools import permutations
innings = int(sys.stdin.readline())
game_data = [[]] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(innings)]
# 조건
# 1. 한 이닝에 3아웃이 발생하면 이닝 종료
# 2. 9번 타자까지 공을 쳤는데 3아웃이 발생하지 않으면 이닝 종료하지않음
# 3. 1번 이닝에서 6번 타자가 마지막이면 2번 이닝은 7번 타자부터 시작
# 4. 경기가 시작하기 전에 타순을 정해줘야함, 단 4번타자는 고정 1번 선수
order = [i for i in range(2, 10)] # 고정된 4번타자 제외하고 순서를 정해주자.
result = float('-inf')
for x in permutations(order, 8): # 8명의 순서의 조합을 따져본다.
    batter = [0] + list(x) # 4번 조건. 1~3번 타자(랜덤 3명) / 1번 선수 (1번 선수) / 4~8번 타자(랜덤 5명)
    batter.insert(4, 1)
    number, point = 1, 0 # 타수와 점수
    for inning in range(1, innings+1): # 각 이닝에 대해
        out = 0 #이닝이 돌면 out은 0으로 초기화
        p1 = p2 = p3 = 0 # 1~3루의 현재 상태
        while out < 3: # 1번, 2번 조건. out이 3번이 되기 전까지 반복
            #여기서부터 야구 룰
            if game_data[inning][batter[number]] == 0:
                out += 1
            elif game_data[inning][batter[number]] == 1:
                point += p3
                p1, p2, p3 = 1, p1, p2
            elif game_data[inning][batter[number]] == 2:
                point += p2 + p3
                p1, p2, p3 = 0, 1, p1
            elif game_data[inning][batter[number]] == 3:
                point += p1 + p2 + p3
                p1, p2, p3 = 0, 0, 1
            elif game_data[inning][batter[number]] == 4:
                point += p1 + p2 + p3 + 1
                p1, p2, p3 = 0, 0, 0
            number += 1 # 타순 증가
            if number == 10: #타순이 9가 되면
                number = 1 #다시 0으로 초기화
    # 3번 조건. 이닝이 끝나도 number을 초기화 하지 않으므로 다음이닝에 타순 유지
    result = max(result, point)
print(result)
