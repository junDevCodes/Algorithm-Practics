import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
file_path = BASE_DIR / 'sample_input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')

"""
[문제]
각 변에 16진수 숫자
시계방향 회전
각 변에 동일한 갯수의 숫자

K번째로 큰 수를 10진수로 만든 수

N은 4의 배수

[입력]
0. TC
1. N, K
2. num_info

[출력]
K번째 16진수 -> 10진수

[로직]
deque

"""

from heapq import nlargest

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    s = input().strip().upper()

    L = N // 4
    s2 = s + s  # 회전 없이 원형 처리
    uniq = set()

    # 시작 오프셋 r만 바꾸면 4변이 자동 생성됨
    for r in range(L):
        base = r
        for j in range(4):
            start = base + j * L
            hex_str = s2[start:start+L]
            uniq.add(int(hex_str, 16))

    # 전체 정렬 대신 상위 K개만 추출
    topk = nlargest(K, uniq)
    ans = topk[-1]
    print(f"#{tc} {ans}")