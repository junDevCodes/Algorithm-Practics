T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = int(input())

    num_list = []
    num_len = 100

    for y in range(num_len):
        num_low = list(map(int, input().split()))
        num_list.append(num_low)

    diag_forword_sum = 0
    diag_reverse_sum = 0
    max_val = 0
    for y in range(num_len):
        low_sum = sum(num_list[y])
        col_sum = sum(num_list[i][y] for i in range(num_len))
        diag_forword_sum += num_list[y][y]
        diag_reverse_sum += num_list[y][num_len-1-y]
        
        max_val = max(max_val, low_sum, col_sum)
    max_val = max(max_val, diag_forword_sum, diag_reverse_sum)

    print(f"#{tc} {max_val}")