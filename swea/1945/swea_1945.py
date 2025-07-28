def cal_prime_factorization(num):
    prime_list = {
        "2": 0,
        "3": 0,
        "5": 0,
        "7": 0,
        "11": 0
    }
    answer_list = []
    
    for target_num in prime_list.keys():
        while num % int(target_num) == 0 :
            prime_list[target_num] += 1
            num = num // int(target_num)
        answer_list.append(prime_list[target_num])

    return answer_list

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    result = " ".join(map(str, cal_prime_factorization(num)))
    print(f"#{test_case} {result}")