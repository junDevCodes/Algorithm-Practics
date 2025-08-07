# SWEA 4861 문제 풀이
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')
T = int(sys.stdin.readline().strip("\n"))
"""
size * size 글자판
문자 순회
idx부터 word_len칸 문자열
뒤집고 비교
찾으면 break
"""
# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    size, word_len = map(int, sys.stdin.readline().strip().split())
    word_list = [list(sys.stdin.readline().strip()) for _ in range(size)]
    rotate_word_list = list(zip(*word_list))  # 열 방향 처리

    result = ""

    # 가로 탐색
    for row in word_list:
        for idx in range(size - word_len + 1):
            sentence = row[idx:idx + word_len]
            if sentence == sentence[::-1]:
                result = ''.join(sentence)
                break
        if result:
            break

    # 세로 탐색
    if not result:
        for col in rotate_word_list:
            for idx in range(size - word_len + 1):
                sentence = col[idx:idx + word_len]
                if sentence == sentence[::-1]:
                    result = ''.join(sentence)
                    break
            if result:
                break

    print(f"#{test_case} {result}")
