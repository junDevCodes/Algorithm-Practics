import sys
sys.stdin = open("sample_input.txt", "r")

def view_light(house_lst):
    end_len = len(house_lst)-2
    search_list = [-2, -1, 1, 2]
    sum_val = 0

    for house in range(2, end_len):
        min_val = 255
        for find_sector in search_list:
            house_val = house_lst[house] - house_lst[house + find_sector]
            if house_val > 0:
                if house_val <= min_val:
                    min_val = house_val
            else:
                break
        else:  # break 없이 끝났을 때만 더함
            sum_val += min_val
    return sum_val

for test_case in range(1, 11):
    repeat = int(sys.stdin.readline().strip("\n"))
    
    count_house = 0
    house_list = list(map(int, sys.stdin.readline().split()))

    count_house = view_light(house_list)

    print(f"#{test_case} {count_house}")