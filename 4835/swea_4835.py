T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num_len, sector = map(int, input().split()) # 숫자 갯수와 구간 수

    num_list = list(map(int, input().split())) # 구간합 리스트 생성 전 일반 리스트
    
    total = 0
    sum_num_list = []
    for idx in range(num_len): # 구간합 리스트 생성
        total += num_list[idx]
        sum_num_list.append(total)

    max_val = 0
    start_sector = sector-1 # 구간합 시작 index = sector - 1
    for idx in range(start_sector, num_len): # 구간합 계산 횟수 = start_sector ~ num_len
        cal_val = 0
            
        if idx == start_sector: # 초기 시작의 경우 구간합 필요 없음
            cal_val = sum_num_list[idx]
            min_val = cal_val
        else:# 이후에는 구간합 공식 적용
            cal_val = sum_num_list[idx] - sum_num_list[idx - sector] #구간 index - 구간 제외 index

        if max_val <= cal_val:
            max_val = cal_val
        
        if min_val >= cal_val:
            min_val = cal_val

    cal_gap = max_val - min_val
    print(f"#{test_case} {cal_gap}")
