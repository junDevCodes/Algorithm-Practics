# SWEA 4831 문제 풀이

# import sys
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'

# sys.stdin = file_path.open('r', encoding='utf-8')

# num = sys.stdin.readline().strip("\n")
# print(num)
# T = int(num)

class bus:
    def __init__(self, current_place: int, charge_val: int, last_stop):
        self.current_place = current_place
        self.charge = charge_val
        self.last_stop = last_stop
        self.charge_count = 0
    
    def move(self, location): # bus의 현재 위치를 location으로 변경
        self.current_place = location
        pass

    def charge_bus(self): # 충전소 들리는 경우 charge_count += 1
        self.charge_count += 1
    
    pass

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # charge_val, last_stop, charge_stop = map(int,sys.stdin.readline().strip("\n").split())
    # charge_stop_list = list(map(int,sys.stdin.readline().strip("\n").split()))
    charge_val, last_stop, charge_stop = map(int, input().split())
    charge_stop_list = list(map(int, input().split()))
    road = [0] * (last_stop+1)
    
    for charge_road in charge_stop_list:
        road[charge_road] = 1

    new_bus = bus(0, charge_val, last_stop) # OOP를 통한 bus 객체 생성
    
    pass_bus = True
    while pass_bus:

        max_reach = min(new_bus.current_place + new_bus.charge, new_bus.last_stop) # 최종 도착지와 (현재위치+1충전간 거리) 중 더 작은 값

        if max_reach >= new_bus.last_stop: # 도착지를 넘어서거나 도착 한 경우
            result = new_bus.charge_count # 이때까지의 충전 횟수 반환
            break

        pass_bus = False # 충전소 검출을 위해 False
        for i in range(max_reach, new_bus.current_place, -1):
            if road[i] == 1: # 현재 위치에서 갈 수 있는 위치 이내의 충전소가 있는 경우
                new_bus.charge_bus() # 충전 횟수 += 1
                new_bus.move(i) # 현재 위치를 해당 충전소로 변경
                pass_bus = True
                break
            
        if pass_bus == False: # 충전소 검출에 실패한 경우
            result = 0
            break
    
    print(f"#{test_case} {result}")