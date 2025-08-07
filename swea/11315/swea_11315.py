# SWEA 11315 문제 풀이
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')
T = int(sys.stdin.readline().strip("\n"))

"""
전체 리스트 순회
o 발견 시 4가지 케이스 ㅡ, ㅣ, /, \ 에 대해서 5칸을 조회
하나라도 연속한 부분이 있으면 YES, 아니면 NO
"""

# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    size = int(sys.stdin.readline().strip("\n"))
    # size = int(input())
    # print(size)

    map_list = []
    for _ in range(size):
        map_list.append(list(sys.stdin.readline().strip("\n")))
        # map_list.append(list(input()))
    # print(map_list)

    result = "NO"
    for col in range(size):
        for row in range(size):
            cnt_list = [0] * 4  # 각각 ㅣ,\,ㅡ,/
            if map_list[col][row] == 'o':
                for delta in range(5):
                    if max(cnt_list) != delta:
                        break
                    if col + delta < size:
                        if map_list[col+delta][row] == 'o':
                            cnt_list[0] += 1
                        if row + delta < size:
                            if map_list[col+delta][row+delta] == 'o':
                                cnt_list[1] += 1
                    if row + delta < size:
                        if map_list[col][row+delta] == 'o':
                            cnt_list[2] += 1
                        if col - delta >= 0:
                            if map_list[col-delta][row+delta] == 'o':
                                cnt_list[3] += 1
                if max(cnt_list) >= 5:
                    result = "YES"
                    break
            if result == "YES":
                break
        if result == "YES":
            break

    print(f"#{test_case} {result}")
