# SWEA 1222 문제 풀이
# import sys
# from pathlib import Path
#
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')
#
# T = 10
"""
[문제 설명]
문자열로 이루어진 계산식을 받아
후위 표기식으로 변환 후 계산하는 프로그램 작성
TC = 10

[입력]
1. 문자열의 길이
2. 계산식 문자열

[출력]
1. #tc cal_val

[로직]
1. 숫자가 나오면 후위 문자열에 추가
2. 연산자가 나오면 stack에 push
3. 연산자가 두개면 pop 후 후위 문자열에 추가
4. 문자열 끝나면 연산자 pop 후 후위 문자열에 추가

1. 후위 문자열을 순서대로 추가 연산자가 들어오면 pop 2번 후 연산
[예시 입력]
101
9+8+5+9+2+4+1+8+3+9+3+8+7+8+6+8+9+4+1+1+7+6+1+5+8+7+6+9+6+3+1+3+1+7+5+9+2+8+4+3+7+3+4+7+3+4+8+3+2+6+6
83
7+4+8+3+4+8+5+5+3+6+7+1+2+5+6+5+5+6+1+6+7+8+6+4+7+4+3+1+6+1+2+1+6+8+6+9+2+7+4+3+2+3

[예시 출력]
#1 267
#2 197
"""
T = 10 # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    # len_str = int(sys.stdin.readline().strip("\n"))
    len_str = int(input())
    # print(len_str)

    # string = sys.stdin.readline().strip("\n")
    string = input()
    # print(string)

    operator_list = {'+'}
    postfix = ""
    stack = []

    for char in string:
        if char not in operator_list:
            postfix += char
        else:
            if stack:
                postfix += stack.pop()
            stack.append(char)
    if stack:
        postfix += stack.pop()

    cal_stack = []
    cal_val = 0

    for char in postfix:
        if char not in operator_list:
            cal_stack.append(char)
        else:
            if cal_stack:
                val_1 = cal_stack.pop()
                val_2 = cal_stack.pop()
                cal_val = int(val_1) + int(val_2)
                cal_stack.append(cal_val)

    print(f"#{test_case} {cal_val}")
