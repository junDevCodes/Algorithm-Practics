# SWEA 1979 문제 풀이

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'input.txt'

sys.stdin = file_path.open('r', encoding='utf-8')
T = int(sys.stdin.readline().strip("\n"))

"""
리스트 전체 순환

1을 만나면 이전 인덱스 조회 열/행 -1 인덱스 조회
이전 인덱스가 있으면 해당 열/행 조회 X

우측 혹은 하단만 확장 +n
0을 만나거나 size까지 count += 1

계산 중 count가 word보다 커지면 break

계산 종료 후 count가 word와 같으면 word_count += 1
"""

def check_row_col(word_map, col, row): # 이전 인덱스 조회
    check_col = True
    check_row = True
    if col - 1 >= 0:
        try:
            if word_map[col-1][row] == 1:
                check_col = False
        except:
            pass
    if row - 1 >= 0:
        try:
            if word_map[col][row-1] == 1:
                check_row = False
        except:
            pass

    return [check_col, check_row]

def check_word_len(word_map, word, col, row, hor_ver): # 칸수 측정
    size_count = 1
    if hor_ver == 0: # 수직
        for delta in range(1, len(word_map)-col):
            if word_map[col+delta][row] == 1:
                size_count += 1
            else:
                return size_count
            if size_count > word:
                size_count = 0
                return size_count
        return size_count
    elif hor_ver == 1: # 수평
        for delta in range(1, len(word_map)-row):
            if word_map[col][row+delta] == 1:
                size_count += 1
            else:
                return size_count
            if size_count > word:
                size_count = 0
                return size_count
        return size_count

# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    size, word = map(int, sys.stdin.readline().strip("\n").split())
    # size, word = map(int, input().split())
    # print(size, word)

    word_map = []
    for _ in range(size):
        word_map.append(list(map(int, sys.stdin.readline().strip("\n").split())))
        # word_map.append(list(map(int, input().split())))
    # print(word_map)

    word_count = 0
    for col in range(size): # 전체 리스트 조회
        for row in range(size):
            if word_map[col][row] == 1: # 1 검출 시 
                check = check_row_col(word_map, col, row) # 이전 인덱스 검출
                if check[0]:
                    hor_word = check_word_len(word_map, word, col, row, hor_ver=0) # 수평 칸수 확인
                    if hor_word == word:
                        word_count += 1
                if check[1]:
                    ver_word = check_word_len(word_map, word, col, row, hor_ver=1) #수직 칸수 확인
                    if ver_word == word:
                        word_count += 1


    print(f"#{test_case} {word_count}")
