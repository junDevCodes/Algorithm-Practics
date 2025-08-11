# SWEA 4866 문제 풀이
# import sys
# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')
# T = int(sys.stdin.readline().strip("\n"))
"""
input : tc, 문자열
output : 정상 출력 여부 T/F(1, 0)

여는 괄호인 경우 stack
아닌 경우 검사 후 pop 에러 발생 시 0
다 끝내면 1
"""

T = int(input())
parentheses = {
    ')': '(',
    '}': '{',
    ']': '['
}

for test_case in range(1, T + 1):
    stack = []
    string = input()
    result = 1  # 기본값을 1로 설정

    for char in string:
        if char in parentheses.values():
            stack.append(char)
        elif char in parentheses.keys():
            if not stack or stack[-1] != parentheses[char]:
                result = 0
                break
            else:
                stack.pop()

    if stack:
        result = 0

    print(f"#{test_case} {result}")
