# SWEA 24991 문제 풀이
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')

T = int(sys.stdin.readline().strip("\n"))
"""
[문제 설명]
학생 키 비교
좌측 < 우측
자신의 키가 몇번째인지 아는 사람의 명 수

[입력]
1. TC
2. N명 학생 수 / M번 키 비교
3. 키 비교 결과 

[출력]
1. #tc 자신의 키를 아는 사람의 명 수

[로직]
연결 리스트
모두와 연결된 경우 알 수 있다

[예시 입력]
3
6 6
1 5
3 4
5 4
4 2
4 6
5 2
6 7
1 3
1 5
3 4
5 4
4 2
4 6
5 2
6 3
1 2
2 3
4 5

[예시 출력]
#1 1
#2 2
#3 0
"""
# T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    student, comparison = map(int, sys.stdin.readline().strip("\n").split())
    # print(student, comparison)

    for i in range(comparison):
        small, big = map(int, sys.stdin.readline().strip("\n").split())
        # print(small, big)
    print(f"#{test_case}")
