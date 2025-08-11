# SWEA 4866 문제 풀이
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')
T = int(sys.stdin.readline().strip("\n"))
"""
input : tc, 문자열
output : 정상 출력 여부 T/F(1, 0)

input 에서 괄호만 stack
반대 괄호인 경우 pop
"""
# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
parentheses = {
    ')' : '(',
    '}' : '{',
    ']' : '['
}
for test_case in range(1, T + 1):
    stack = []
    string = list(sys.stdin.readline().strip("\n"))

    for char in string:
        if char in parentheses.values():
            stack.append(char)
        if char in parentheses.keys():
            if stack[-1] == parentheses[char]:
                stack.pop()
    if not stack:
        result = 1
    else:
        result = 0

    print(f"#{test_case} {result}")
