# SWEA 6019 문제 풀이
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
두 기차가 N 마일 떨어져 있고
기차 A는 시속 A 마일, 기차 B는 시속 B 마일로 달린다
파리는 시속 F 마일로 기차 A에서 B로 날아간다.
파리가 기차 B에 도착하면 바로 A 기차를 향해 날아간다.

기차끼리 충돌하면 파리가 죽는다.

[입력]
1. TC
2. 기차간 거리, A의 속력, B의 속력, 파리의 속력

[출력]
1. 파리가 움직인 총 길이

[로직]
(거리 / (A + B)) * 파리 속력

[예시 입력]
예시 입력 내용을 작성

[예시 출력]
예시 출력 내용을 작성
"""
T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    train_distance, train_A_speed, train_B_speed, fly_speed = map(int, input().split())
    result = (train_distance / (train_A_speed + train_B_speed)) * fly_speed
    print(f"#{test_case} {result:.10f}")
