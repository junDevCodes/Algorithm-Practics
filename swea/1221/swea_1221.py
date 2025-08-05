T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc, num_len = map(str, input().split())
    num_len = int(num_len)

    # 변화나 가능한 str_list
    num_system = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    # 문자열로 주어진 리스트
    num_list_str = list(map(str, input().split()))

    num_list = []

    # 문자열로 주어진 리스트를 정수 리스트로 변환
    for num in num_list_str:
        if num in num_system:
            num_list.append(num_system.index(num))

    # 정수 리스트 정렬
    num_list.sort()

    print(tc)
    # 정렬된 정수리스트를 str_list index 에 넣어 출력
    for num in num_list:
        print(num_system[num], end=" ")
    
