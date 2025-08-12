# SWEA 22167 문제 풀이
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
문자열 뒤집기

[입력]
1. TC
2. 문자열

[출력]
뒤집은 문자열 출력

[로직]
stack 기본기 사용
append -> pop 하며 join

[예시 입력]
3
hello
python
algorithm

[예시 출력]
olleh
nohtyp
mhtirogla
"""
T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    # string = sys.stdin.readline().strip("\n")
    string = input()

    stack = []
    for char in string:
        stack.append(char)

    result = ""
    for _ in string:
        result += stack.pop()

    print(f"{result}")
