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

print(max_val)
pass
