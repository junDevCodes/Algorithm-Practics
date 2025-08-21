# SWEA 1946 문제 풀이
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
압축된 문서의 내용을 풀어쓰는 프로그램

[입력]
1. TC
2. 압축 파일 갯수
3. 압축파일 내용

[출력]
압축 해제 파일 내용

[로직]
출력

[예시 입력]
1
3
A 10
B 7
C 5

[예시 출력]
#1
AAAAAAAAAA
BBBBBBBCCC
CC

"""
T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    # package_num = int(sys.stdin.readline().strip("\n"))
    package_num = int(input())

    print(f"#{test_case}")
    cnt = 0
    for idx in range(package_num):
        # word, word_count = map(str, sys.stdin.readline().strip().split())
        word, word_count = map(str, input().split())
        for _ in range(int(word_count)):
            print(word, end="")
            cnt += 1
            if cnt >= 10:
                print("")
                cnt = 0
    print("")