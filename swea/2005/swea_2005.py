# SWEA 2005 문제 풀이
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
크기가 N인 파스칼의 삼각형 만들기
1. 첫 번째 줄은 항상 숫자 1이다.
2. 두번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

[입력]
1. TC
2. 파스칼 삼각형의 크기

[출력]
#TC
파스칼의 삼각형

[로직]
시작 배열 = 1
추가 배열 = 
처음과 끝에 1
사이 값은 이전 배열 len - 1
값 = 이전 배열의 동일 인덱스 + 이전 인덱스 값  

[예시 입력]
1
4

[예시 출력]#1
1
1 1
1 2 1
1 3 3 1
"""
T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    # pascal_num = int(sys.stdin.readline().strip("\n"))
    pascal_num = int(input())

    pascal_triangle_list = [] # 초기 배열
    # 원하는 추가 배열 형식 [[1], [1, 1], [1, 2, 1]]

    for col in range(pascal_num):
        add_list = []
        for row in range(col + 1):
            if row == 0 or row == col:
                add_list.append(1)
            else:
                same_index_val = pascal_triangle_list[col-1][row]
                before_index_val = pascal_triangle_list[col-1][row-1]
                add_list.append(same_index_val + before_index_val)

        pascal_triangle_list.append(add_list)

    print(f"#{test_case}")
    for triangle in pascal_triangle_list: # 파스칼 삼각형 크기만큼 반복하며 출력
        print(" ".join(map(str, triangle)))


