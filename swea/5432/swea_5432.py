# SWEA 5432 문제 풀이
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')

T = int(sys.stdin.readline().strip("\n"))
"""
[문제 설명]
쇠막대기를 겹친 후 레이저를 수직으로 발사하여 자른다

쇠막대기와 레이저의 배치 조건
- 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.
- 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
- 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
- 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.

- 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 ()으로 표시된다. 모든 ()는 반드시 레이저를 표현한다.
- 쇠 막대기의 왼쪽 끝은 ( 여는 괄호, 오른쪽 끝은 ) 닫는 괄호로 표현된다

[입력]
1. TC
2. 괄호 표현

[출력]
1. #TC 잘려진 조각 갯수

[로직]


[예시 입력]
2
()(((()())(())()))(())
(((()(()()))(())()))(()())

[예시 출력]
#1 17
#2 24
"""
# T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    num = int(sys.stdin.readline().strip("\n"))
    print(num)
    print(f"#{test_case}")
