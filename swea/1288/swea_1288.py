
def check_count(num) :
    count = 1
    check_num = set(range(10))
    
    while True:
        current = num * count
        for digit in map(int, str(current)):
            check_num.discard(digit)
        
        if len(check_num) == 0:
            return current
        
        count += 1

# 입력 처리
T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    result = check_count(num)
    print(f"#{test_case} {result}")