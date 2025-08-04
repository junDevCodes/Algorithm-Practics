T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    len_num = int(input())
    num_seq = input()
    num_len = 0
    max_len = 0
    
    for num in num_seq:
        if int(num) == 1:
            num_len += 1
        elif int(num) == 0:
            if max_len <= num_len:
                max_len = num_len
            num_len = 0
    if max_len <= num_len:
        max_len = num_len
    print(f"#{test_case} {max_len}")