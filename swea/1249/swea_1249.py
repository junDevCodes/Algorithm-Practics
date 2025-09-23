# SWEA 1249 문제 풀이
import sys
from pathlib import Path

# 로컬 테스트용 파일 입력 설정
BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]


[입력]


[출력]


[알고리즘]
1. 
2. 
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""

T = int(input())

for test_case in range(1, T + 1):
    # 입력
    n = int(input())
    
    # 로직
    result = n
    
    # 출력 (SWEA 형식)
    print(f"#{test_case} {result}")
