# SWEA 5201 문제 풀이
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'sample_input.txt'
sys.stdin = file_path.open('r', encoding='utf-8')
T = int(sys.stdin.readline().strip("\n"))

"""
container_weight와 truck_weight를 크기순으로 정렬
트럭 무게 & 컨테이너 무게 역순 조회
트럭 무게 >= 컨테이너 무게 -> 둘다 pop 컨테이너 무게는 총 무게에 합산
트럭 무게 < 컨테이너 무게 시 컨테이너만 pop 후 다시 비교
트럭/컨테이너 둘 중 하나의 원소가 0 이 되면 종료 후 총 무게 반환
"""

# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    container, truck = map(int, sys.stdin.readline().strip("\n").split())
    # print(container, truck)

    container_weight = list(map(int, sys.stdin.readline().strip("\n").split()))
    truck_weight = list(map(int, sys.stdin.readline().strip("\n").split()))
    # print(container_weight)
    # print(truck_weight)

    container_weight.sort()
    truck_weight.sort()

    total_weight = 0
    while truck_weight and container_weight:
        if truck_weight[-1] >= container_weight[-1]:
            truck_weight.pop()
            total_weight += container_weight.pop()
        else:
            container_weight.pop()

    print(f"#{test_case} {total_weight}")
