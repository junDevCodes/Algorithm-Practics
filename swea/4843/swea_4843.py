T = int(input())

for test_case in range(1, T + 1):
    num_len = int(input())
    num_list = list(map(int, input().split()))

    sorted_num_list = sorted(num_list)

    result = []

    left = 0
    right = num_len - 1

    while left <= right: # 좌우가 줄어들며 서로 지나가기 전까지
        if right >= left:
            result.append(sorted_num_list[right])  # 큰 수
            right -= 1
        if left <= right:
            result.append(sorted_num_list[left])   # 작은 수
            left += 1

    result = result[:10]

    print(f"#{test_case} {' '.join(map(str, result))}")
