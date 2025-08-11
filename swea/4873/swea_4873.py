# SWEA 4873 문제 풀이
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')
T = int(sys.stdin.readline().strip("\n"))
"""
input : tc, 문자열
output : 반복 문자 제거 후 남은 문자 수

stack 비워져있다면 추가
채워져있다면 top과 char 비교
같다면 pop / not append
다르다면 append char

모든 문자열이 다 끝났다면 len(stack) 반환
"""
# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    string = list(sys.stdin.readline().strip("\n"))
    stack = []
    for char in string:
        if stack:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)
    result = len(stack)

    print(f"#{test_case} {result}")
