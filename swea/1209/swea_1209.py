T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = int(input())

    num_list = []
    num_len = 100 # 배열 길이

    for y in range(num_len): # 2차원 배열에 한줄씩 담기
        num_low = list(map(int, input().split()))
        num_list.append(num_low)

    diag_forword_sum = 0
    diag_reverse_sum = 0
    max_val = 0
    for y in range(num_len):
        low_sum = sum(num_list[y]) # 행의 합
        col_sum = sum(num_list[i][y] for i in range(num_len)) # 2중 for문을 통해 열의 합을 담는다
        diag_forword_sum += num_list[y][y] # 대각선 정방향 전체 배열을 순회하며 총 하나의 값을 낸다.
        diag_reverse_sum += num_list[y][num_len-1-y] # 대각선 역방향 전체 배열을 순회하며 총 하나의 값을 낸다
        
        max_val = max(max_val, low_sum, col_sum) # 현재 max_val, low_sum, col_sum 중 가장 큰 값
    max_val = max(max_val, diag_forword_sum, diag_reverse_sum) # 최종 max_val 대각선 정,역 방향 중 가장 큰 값

    print(f"#{tc} {max_val}")