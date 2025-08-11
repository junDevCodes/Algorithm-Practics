# SWEA 10804 문제 풀이
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')
T = int(sys.stdin.readline().strip("\n"))
"""
"""
# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
pair = {
    'b' : 'd',
    'd' : 'b',
    'q' : 'p',
    'p' : 'q'
}
for test_case in range(1, T + 1):
    string = list(sys.stdin.readline().strip("\n"))
    result = ""
    while string:
        result += pair[string.pop()]
    print(f"#{test_case} {result}")
