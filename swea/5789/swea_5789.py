T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    box, repeat = map(int, input().split()) # box 갯수, 반복 횟수

    box_list = [0] * box # 값이 0 인 box 갯수만큼의 리스트 생성

    for i in range(1, repeat+1):
        L, R = map(int, input().split())

        for idx in range(L-1,R): # L에서 R까지 box_list 조회
            box_list[idx] = i # 해당 idx에 L 값으로 변경
    
    box_str = " ".join(map(str, box_list)) # box_list는 int이기 때문에 str로 변경 후 join
    print(f"#{test_case} {box_str}")