# SWEA 4751 문제 풀이
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
문자열 장식하기

[입력]
1. TC
2. 문자열

[출력]
다이아몬드 장식으로 꾸민 문자열

[로직]
- 문제 해결에 필요한 알고리즘

[예시 입력]
2
D
APPLE

[예시 출력]
..#..
.#.#.
#.D.#
.#.#.
..#..
..#...#...#...#...#..
.#.#.#.#.#.#.#.#.#.#.
#.A.#.P.#.P.#.L.#.E.#
.#.#.#.#.#.#.#.#.#.#.
..#...#...#...#...#..

"""
T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    l15 = "..#."
    l24 = ".#.#"
    # string = sys.stdin.readline().strip()
    string = input()
    print(l15 * len(string) + ".")
    print(l24 * len(string) + ".")
    for char in string:
        print(f"#.{char}.", end="")
    print("#")
    print(l24 * len(string) + ".")
    print(l15 * len(string) + ".")
