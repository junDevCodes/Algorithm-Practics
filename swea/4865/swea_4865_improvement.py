# 4865. [파이썬 S/W 문제해결 기본] 1일차 - 글자수 세기
import sys
from collections import Counter
sys.stdin = open("sample_input.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    string1 = input()
    string2 = input()

    freq_map = Counter(string2) # 글자의 빈도수를 hash map 형태로 미리 생성

    max_count = 0

    for char in set(string1):
        count = freq_map.get(char, 0) #
        max_count = max(max_count, count)

    print(f'#{test_case} {max_count}')