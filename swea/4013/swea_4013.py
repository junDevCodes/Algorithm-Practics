# SWEA 4013 문제 풀이
# import sys
# from pathlib import Path
#
# # 로컬 테스트용 파일 입력 설정
# BASE_DIR = Path(__file__).resolve().parent
# sys.stdin = (BASE_DIR / 'sample_input.txt').open('r', encoding='utf-8')

"""
[문제 설명]
자석이 1칸 회전할때 붙어 이씨는 날의 자성과 다른 경우 반대방향으로 1칸 회전한다.
모든 회전이 끝난 후 점수를 구하시오
자석의 회전방향은 시계: 1, 반시계: -1이 주어진다
날의 자성은 N극: 0, S극: 1로 주어진다
자석의 정보는 빨간색 화살표 위치부터 시계 방향대로 주어진다

[입력]
0.TC
1. rt_num
2. mag_info
3. rt_info


[출력]
2**(자석번호-1) * S극 여부

[알고리즘]
1. BFS 태우기 
2. 자신의 앞뒤 자석 2, 6번 확인
3. 

[복잡도]
- 시간: O()
- 공간: O()
"""
from collections import deque

# T = int(sys.stdin.readline().strip())
T = int(input())


def bfs():
    global mag_num

    while queue:
        info = queue.pop()
        magnet, direction = info[0], info[1]

        if 0 < magnet - 1 and not visited[magnet-1]:  # 좌측에 자석이 있을 때
            n_mag = magnet - 1
            n_rt = -direction
            if mag_info[magnet][6] != mag_info[n_mag][2]:
                queue.append((n_mag, n_rt))
        if magnet + 1 <= mag_num and not visited[magnet+1]:  # 우측에 자석이 있을 때
            n_mag = magnet + 1
            n_rt = -direction
            if mag_info[magnet][2] != mag_info[n_mag][6]:
                queue.append((n_mag, n_rt))

        mag_info[magnet].rotate(direction)
        visited[magnet] = True


for test_case in range(1, T + 1):
    # 입력
    # rt_num = int(sys.stdin.readline().strip())
    rt_num = int(input())

    mag_num = 4 # 자석 4개
    # 자성 정보
    # mag_info = [deque([])] + [deque(list(map(int, sys.stdin.readline().strip().split()))) for _ in range(mag_num)]
    mag_info = [deque([])] + [deque(list(map(int, input().split()))) for _ in range(mag_num)]

    # 회전 정보
    # rt_info = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(rt_num)]
    rt_info = [tuple(map(int, input().split())) for _ in range(rt_num)]

    # print(mag_info)

    for rt_mag, rt_direction in rt_info:
        queue = deque([])
        visited = [False] * (mag_num+1)

        queue.append((rt_mag, rt_direction))
        visited[rt_mag] = True
        bfs()

    score = 0
    for idx in range(1, mag_num+1):
        score += 2**(idx-1) * mag_info[idx][0]
    
    # 출력 (SWEA 형식)
    print(f"#{test_case} {score}")
