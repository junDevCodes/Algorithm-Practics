# SWEA 1215 문제 풀이
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
8 x 8 글자판에서 제시된 길이를 가진 회문의 갯수 구하기
문자의 종류 : 'A', 'B', 'C'
오직 직선인 경우만 인정
TC = 10

[입력]
1. 찾아야 할 회문의 길이
2. 8 x 8 글자판의 배치

[출력]
#TC 회문의 갯수

[로직]
8 * (8 - 회문의 길이)만큼 반복
슬라이싱 통해 reverse와 똑같은 경우 palindrome_count += 1

zip 통해 90도 회전 생성
8 * (8 - 회문의 길이)만큼 반복
슬라이싱 통해 reverse와 똑같은 경우 palindrome_count += 1

[예시 입력]
4
CBBCBAAB
CCCBABCB
CAAAACAB
BACCCCAC
AABCBBAC
ACAACABC
BCCBAABC
ABBBCCAA

[예시 출력]
#1 12
"""
T = 10  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    # len_palindrome = int(sys.stdin.readline().strip("\n"))
    len_palindrome = int(input())
    # print(len_palindrome)

    # palindrome_list = [sys.stdin.readline().strip("\n") for _ in range(8)]
    palindrome_list = [input() for _ in range(8)]
    # print(palindrome_list)

    rotate_palindrome_list = list(map("".join, zip(*palindrome_list)))
    # print(rotate_palindrome_list)

    palindrome_count = 0
    for col in range(8):
        for row in range(9-len_palindrome):
            if palindrome_list[col][row:row+len_palindrome] == palindrome_list[col][row:row+len_palindrome][::-1]:
                palindrome_count += 1
            if rotate_palindrome_list[col][row:row+len_palindrome] == rotate_palindrome_list[col][row:row+len_palindrome][::-1]:
                palindrome_count += 1

    print(f"#{test_case} {palindrome_count}")
