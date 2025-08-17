# import sys
# from pathlib import Path
from collections import deque

# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / "sample_input.txt"
# sys.stdin = file_path.open('r', encoding='utf-8')

"""
[문제]
4개의 자석이 돌아간다

하나의 자석이 1칸 회전 할 때 맞닿은 부분의 극성이 반대인 경우에만 반대로 회전한다

빨간색 화살표의 위치가 N극이면 1점 S극이면 자석의 번호에 따라 점수를 1, 2, 4, 8점 획득한다.

4개 자석의 자성 정보와 회전 횟수를 주고
회전 이후 획득하는 점수의 총 합을 구하시오

자석은 총 4개 각 자석은 8개의 날
시계 방향 : 1 / 반시계 방향 : -1
N극 : 0 / S극 : 1
빨간색 화살표 위치의 날 기준 시계 방향으로 주어진다.

[입력]
1. TC
2. 회전 횟수
3. 자석 정보
4. 회전 자석과 방향

[출력]
회전 이후 최종 점수

[로직]
2번 6번을 비교 후 회전 여부 결정
원형 큐 사용

[예시 입력]
10
2
0 0 1 0 0 1 0 0
1 0 0 1 1 1 0 1
0 0 1 0 1 1 0 0
0 0 1 0 1 1 0 1
1 1
3 -1

[예시 출력]
#1 10
#2 14
#3 3
#4 13
#5 15
#6 10
#7 2
#8 6
#9 5
#10 4
"""

# T = int(sys.stdin.readline().strip()) # TC
T = int(input()) # TC

for test_case in range(1, T + 1):
    # rt_cnt = int(sys.stdin.readline().strip()) # 회전 횟수
    rt_cnt = int(input()) # 회전 횟수
    # print(rt_cnt)

    # magnet_list = [deque(map(int, sys.stdin.readline().strip().split())) for _ in range(4)] # 자석 정보
    magnet_list = [deque(map(int, input().split())) for _ in range(4)] # 자석 정보
    # print(magnet_list)

    # rt_queue = deque(tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(rt_cnt)) # 회전 자석과 방향
    rt_queue = deque(tuple(map(int, input().split())) for _ in range(rt_cnt)) # 회전 자석과 방향
    # print(rt_queue)

    while rt_queue:
        cm, cr = rt_queue.popleft() # 스텝별 회전 정보
        # print(cm, cr)

        rotate_info = [False] * 4 # 회전 정보 리스트 초기화
        queue = deque([(cm, cr)]) # 회전 큐
        rotate_info[cm-1] = cr # 회전 정보 방문 큐
        # print(queue)
        # print(rotate_info)

        delta_list = (-1, 1) # 델타 리스트
        while queue: # BFS
            current_magnet, current_rotate = queue.popleft() # 현재 기준 회전 시작
            current_magnet_idx = current_magnet - 1

            for delta in delta_list: # 델타 탐색
                next_magnet_idx = current_magnet_idx + delta
                if 0 <= next_magnet_idx < 4: # 델타 탐색이 범위 내 라면
                    if not rotate_info[next_magnet_idx]: # 방문 정보 확인
                        if current_magnet_idx < next_magnet_idx: # 현재 기준 오른쪽 자석과 비교
                            if magnet_list[current_magnet_idx][2] != magnet_list[next_magnet_idx][6]: # 오른쪽 자석과 연결 노드비교
                                rotate_info[next_magnet_idx] = current_rotate * -1 # 다르다면 반대방향 회전
                                queue.append((next_magnet_idx + 1, rotate_info[next_magnet_idx])) # 회전 큐에 다음 자석 정보와 회전 정보 추가
                        elif next_magnet_idx < current_magnet_idx: # 현재 기준 왼쪽 자석과 비교
                            if magnet_list[current_magnet_idx][6] != magnet_list[next_magnet_idx][2]: # 오른쪽 자석과 연결 노드비교
                                rotate_info[next_magnet_idx] = current_rotate * -1 # 다르다면 반대방향 회전
                                queue.append((next_magnet_idx + 1, rotate_info[next_magnet_idx])) # 회전 큐에 다음 자석 정보와 회전 정보 추가

        # print(rotate_info)
        for rotate in range(4):
            magnet_list[rotate].rotate(rotate_info[rotate])

        # print(magnet_list)
    sum = 0
    cal_list = [1, 2, 4, 8]
    for idx in range(4):
        sum += magnet_list[idx][0] * cal_list[idx]
    print(f"#{test_case} {sum}")