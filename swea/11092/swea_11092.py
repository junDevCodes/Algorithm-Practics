T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    pos_num = int(input())

    num_list = list(map(int, input().split()))

    max_val = 0
    min_val = max(num_list) # 초기 최솟값을 최대값으로 설정

    for index, num in enumerate(num_list): # enumerate로 index와 값을 둘다 받아오기
        if max_val <= num: # 최대값의 경우 마지막 인덱스까지
            max_val = num
            max_idx = index
        if num < min_val: # 최소값의 경우 처음 인덱스까지
            min_val = num
            min_idx = index
    
    abs_val = abs(max_idx - min_idx)
    print(f"#{test_case} {abs_val}")