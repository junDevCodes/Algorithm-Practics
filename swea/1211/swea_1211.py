# import sys
# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')

"""
첫 줄 탐색 1 검출
index_list 생성

min_count = (count, index)
"""

delta_list = [(-1, 0, 0), (1, 0, 1), (0, 1, 2)]

def check_side(map, x, y):
    for delta in delta_list:
        dx = delta[0]
        dy = delta[1]
        flag = delta[2]

        if 0 <= x + dx < len(map[0]) and 0 <= y + dy < len(map):
            if map[y + dy][x + dx] == 1:
                return flag
    return 2

def find_route(map, idx):
    current_x = idx
    current_y = 0
    way_flag = 0
    count = 0

    while current_y < len(map) - 1:
        if way_flag == 2:
            way_flag = check_side(map, current_x, current_y)
        
        # 다음 이동할 위치 계산
        next_x = current_x + delta_list[way_flag][0]
        next_y = current_y + delta_list[way_flag][1]
        
        # 반드시 경계 체크 먼저!
        if (0 <= next_x < len(map[0]) and 
            0 <= next_y < len(map) and 
            map[next_y][next_x] == 1):
            # 경계 안이고 길이 있으면 이동
            current_x = next_x
            current_y = next_y
            count += 1
        else:
            # 경계 밖이거나 길이 없으면 아래로 이동
            way_flag = 2
            current_x += delta_list[2][0]  # 아래로 (x는 그대로)
            current_y += delta_list[2][1]  # 아래로 (y+1)
            count += 1
    
    return count

T = 10


for test_case in range(1, T + 1):
    
    min_count = {
        "count" : -1,
        "idx": 0
    }

    # tc = int(sys.stdin.readline().strip("\n"))
    tc = int(input().strip("\n"))

    # ladder_list = [list(map(int, sys.stdin.readline().strip("\n").split())) for _ in range(100)]
    ladder_list = [list(map(int, input().split())) for _ in range(100)]

    for idx, value in enumerate(ladder_list[0]):
        if value == 1:
            route_val = find_route(ladder_list, idx)

            if min_count['count'] < 0:
                min_count['idx'] = idx
                min_count['count'] = route_val
            else :
                if route_val < min_count['count']:
                    min_count['idx'] = idx
                    min_count['count'] = route_val

    print(f"#{test_case} {min_count['idx']}")