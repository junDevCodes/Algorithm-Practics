T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    num_list = list(map(int, input().split()))
    max_val = max(num_list)
    min_val = min(num_list)
    gap_val = max_val - min_val
    print(f"#{test_case} {gap_val}")
    pass