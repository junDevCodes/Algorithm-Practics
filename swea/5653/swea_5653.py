import sys
from collections import deque
import copy


def solve():
    T = int(sys.stdin.readline().strip())
    for test_case in range(1, T + 1):
        N, M, K = map(int, sys.stdin.readline().strip().split())

        initial_map = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

        # 딕셔너리를 사용하여 세포 상태 관리 (무한 그리드 구현)
        # key: (row, col) 좌표
        # value: [생명력(X), 비활성화 시간, 활성화 시간]
        cells = {}

        start_row = K  # 시작 위치를 K만큼 이동
        start_col = K

        for r in range(N):
            for c in range(M):
                if initial_map[r][c] > 0:
                    life = initial_map[r][c]
                    # 초기 세포의 좌표를 옮겨서 번식 공간을 미리 확보
                    cells[(start_row + r, start_col + c)] = [life, life, life]

        # 시뮬레이션 시작
        for t in range(1, K + 1):
            next_generation = {}

            # 현재 모든 세포의 상태를 업데이트
            dead_cells = []
            for (r, c), state in cells.items():
                life, inactive_time, active_time = state

                # 비활성 상태
                if inactive_time > 0:
                    state[1] -= 1
                    # 비활성 시간이 끝나면 활성 상태로 전환
                    if state[1] == 0:
                        state[2] = life
                # 활성 상태 (번식 시작)
                elif active_time > 0:
                    state[2] -= 1

                    # 활성화된 첫 1시간 동안만 번식
                    if active_time == life - 1:
                        delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]

                        for dr, dc in delta:
                            new_r, new_c = r + dr, c + dc

                            # 빈 공간에만 번식
                            if (new_r, new_c) not in cells:
                                if (new_r, new_c) not in next_generation or next_generation[(new_r, new_c)][0] < life:
                                    # 생명력이 더 높은 세포가 우선권을 가짐
                                    next_generation[(new_r, new_c)] = [life, life, life]

                # 활성 시간 종료 -> 세포 죽음
                if state[1] == 0 and state[2] == 0:
                    dead_cells.append((r, c))

            # 다음 세대 세포들을 현재 세포 목록에 추가
            for loc, state in next_generation.items():
                cells[loc] = state

            # 죽은 세포 제거
            for loc in dead_cells:
                del cells[loc]

        # K시간 후 살아있는 세포의 수 계산
        alive_count = len(cells)
        print(f"#{test_case} {alive_count}")


solve()