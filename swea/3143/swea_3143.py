# SWEA 3143 문제 풀이
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
A 문자을 타이핑 하는데 걸리는 횟수
A 문자열 내부에 B 문자열이 있다면 B 문자열 만큼을 1회로 한다.

[입력]
1. TC
2. string, inner_string

[출력]
1. #tc type_count

[로직]
1. string 길이를 구한다
2. len_inner_string = inner_string 포함 횟수 * len(inner_string)
3. len(string) - len_inner_string + inner_string 포함 횟수
=> type_count = len(string) - (len(inner_string)-1) * inner_string 포함횟수

[예시 입력]
2
banana bana
asakusa sa	//Test Case의 개수
//A=”banana”, B=”bana”
//A=”asakusa”, B=”sa”

[예시 출력]
#1 3
#2 5	//Test Case 1번의 답
//Test Case 2번의 답
"""
T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    # string, inner_string = map(str, sys.stdin.readline().strip("\n").split())
    string, inner_string = map(str, input().split())

    include_string = string.count(inner_string)

    type_count = len(string) - (len(inner_string)-1) * include_string

    print(f"#{test_case} {type_count}")