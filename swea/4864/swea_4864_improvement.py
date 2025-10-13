# SWEA 4864 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
문자열 매치 알고리즘
두개의 문자열 str1, str2가 주어질 때 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램
존재하면 1, 존재하지 않으면 0 출력

[입력]
0. tc
1. str1
2. str2

[출력]
0. 존재 유무 1 / 0

[알고리즘]
1. kmp 알고리즘 구현
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""
# 1단계: LPS 배열 생성 함수
def get_lps(pattern):
    M = len(pattern)
    lps = [0] * M
    length = 0  # 현재까지 찾은 접두사=접미사의 길이
    i = 1       # LPS 배열을 계산할 패턴의 인덱스

    while i < M:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # LPS 배열을 이용하여 j를 되돌림 (i는 그대로)
                length = lps[length - 1]
            else:
                # length가 0이면, 더 이상 되돌릴 곳이 없음
                lps[i] = 0
                i += 1
    return lps


# 2단계: KMP 매칭 함수
def kmp(text, pattern):
    M = len(pattern)
    N = len(text)
    lps = get_lps(pattern)

    i = 0  # text 포인터
    j = 0  # pattern 포인터
    find_pattern = 0

    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        # [중요]: 패턴 전체를 찾았을 경우
        if j == M:
            # 패턴을 찾았으므로 1을 반환하고 종료
            # 만약 모든 위치를 찾고 싶다면: j = lps[j - 1] (다음 탐색 위치로 이동)
            j = lps[j - 1]
            find_pattern += 1

            # 불일치 발생 시 (pattern[j] != text[i])
        elif i < N and pattern[j] != text[i]:
            if j != 0:
                # 텍스트 포인터(i)를 유지하고, 패턴 포인터(j)만 되돌림
                j = lps[j - 1]
            else:
                # j가 0이면 패턴의 첫 글자부터 불일치 -> 텍스트 포인터(i)만 1 증가
                i += 1

    # 하나이상 찾았으면 1 반환 아니면 0 반환
    return 1 if find_pattern != 0 else 0


T = int(input())

for test_case in range(1, T + 1):
    pattern = input()
    text = input()
    result = kmp(text, pattern)
    print(f"#{test_case} {result}")
