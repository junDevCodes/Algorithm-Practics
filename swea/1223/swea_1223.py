# SWEA 1223 문제 풀이
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
후위 표현식으로 변환 후 계산하는 프로그램 작성
TC = 10

[입력]
1. 계산식 길이
2. 계산식 문자열

[출력]
1. #tc 계산 결과

[로직]
1. 문자는 그대로 result에 추가
2. 연산자인 경우 stack에 push
3. stack top이 push보다 큰 경우 전부 pop후 result에 추가

[예시 입력]
101
9+5*2+1+3*3*7*6*9*1*7+1+8*6+6*1*1*5*2*4*7+4*3*8*2*6+7*8*4*5+3+7+2+6+5+1+7+6+7*3*6+2+6+6*2+4+2*2+4*9*3
79
4+4*3*4*9+2+7*4*7+7*7*9*5*2+8*8+2*6*7*3*7*9*3*4+8+8*9+3+9+6+9+4*1+6*3+5+1+7+5*1

[예시 출력]
#1 28134
#2 195767

"""
T = 10  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
operator_list = {
    '+': 1,
    '*': 2
}
for test_case in range(1, T + 1):
    # len_num = int(sys.stdin.readline().strip("\n"))
    len_num = int(input())
    # print(len_num)

    # string_cal = sys.stdin.readline().strip("\n")
    string_cal = input()
    # print(string_cal)

    stack = []
    postfix = ""

    for char in string_cal:
        if char not in operator_list.keys():
            postfix += char
        else:
            if stack:
                if operator_list[stack[-1]] == operator_list[char]:
                    postfix += stack.pop()
                elif operator_list[stack[-1]] > operator_list[char]:
                    while stack and operator_list[stack[-1]] >= operator_list[char]:
                        postfix += stack.pop()
                stack.append(char)
            else:
                stack.append(char)
    if stack:
        while stack:
            postfix += stack.pop()

    cal_stack = []
    result = 0

    for cal_char in postfix:
        if cal_char not in operator_list.keys():
            cal_stack.append(int(cal_char))
        else:
            val_1 = cal_stack.pop()
            val_2 = cal_stack.pop()
            if operator_list[cal_char] == 1:
                cal_val = val_1 + val_2
            elif operator_list[cal_char] == 2:
                cal_val = val_1 * val_2
            cal_stack.append(cal_val)

    if cal_stack:
        result = cal_stack.pop()
        
    print(f"#{test_case} {result}")
