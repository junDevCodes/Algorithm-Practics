# SWEA 6485 문제 풀이
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')
T = int(sys.stdin.readline().strip("\n"))
"""
bus_line의 범위 내에 몇개의 bus_stop이 해당되는지
i 번쨰의 bus_line start~end, bus_stop이 해당되면 += 1
"""
# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    bus_line = int(sys.stdin.readline().strip("\n"))
    # print(bus_line)

    bus_line_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(bus_line)]
    # print(bus_line_list)

    bus_stop = int(sys.stdin.readline().strip("\n"))
    # print(bus_stop)

    bus_stop_list = {str(sys.stdin.readline().strip()):0 for _ in range(bus_stop)}
    # print(bus_stop_list)

    for bus in bus_line_list:
        for idx in range(bus[0], bus[1]+1):
            bus_stop_list[str(idx)] += 1

    result = " ".join(map(str, bus_stop_list.values()))
    print(f"#{test_case} {result}")
