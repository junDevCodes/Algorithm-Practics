T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    box = int(input())

    box_list = list(map(int, input().split()))
    max_val = 0

    for target in range(0, box): # 왼쪽부터 순환
        drop = 0 # sum 초기화   
        for i in range(target+1, box): # 자신 기준 오른쪽부터 순환
            if box_list[target] > box_list[i]: # 자신보다 작으면 반복 
                drop += 1 # 낙차 추가
        if max_val <= drop: # max_val이 sum보다 작거나 같다면
            max_val = drop # max_val = sum

    print(f"#{test_case} {max_val}")