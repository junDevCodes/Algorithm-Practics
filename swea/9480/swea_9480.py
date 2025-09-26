# SWEA 9480 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
단어 목록이 주어지고 단어 세트를 만들어야 한다
각 단어세트는 알파벳을 전부 하나씩 포함해야한다
이때 최대로 만들 수 있는 단어 세트의 갯수를 구하시오 

[입력]
0. TC
1. word_num
2. words

[출력]
문자열 세트

[알고리즘]
1. 단어별로 조합을 짠다
2. 이때 알바벳 전부를 채우면 카운트 추가한다 
3. 안겹치는 조합을 했을때 최대 갯수는

[복잡도]
- 시간: O()
- 공간: O()
"""


def dfs(idx, notes):
    global count

    if idx == word_num:
        if len(notes) == 26:
            count += 1
        return

    dfs(idx+1, notes)
    n_notes = notes.copy()

    for alpha in words[idx]:
        n_notes.add(alpha)

    dfs(idx+1, n_notes)


# T = int(sys.stdin.readline())
T = int(input())

for test_case in range(1, T + 1):
    # 입력
    # word_num = int(sys.stdin.readline())
    word_num = int(input())

    # words = list(str(sys.stdin.readline().strip()) for _ in range(word_num))
    words = list(str(input()) for _ in range(word_num))

    count = 0
    alphabet_list = set()
    dfs(0, alphabet_list)
    
    # 로직
    
    # 출력 (SWEA 형식)
    print(f"#{test_case} {count}")
