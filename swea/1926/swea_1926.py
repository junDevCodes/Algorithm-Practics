num_end = int(input())
num_list = []

for num in range(1, num_end+1): # list에 저장
    num_list.append(str(num))

for num in num_list:
    clap_count = 0
    for char in num: # 각각의 자리수를 순회
        if char in ['3', '6', '9']: # 자리수에 3, 6, 9가 포함되면 clap_count += 1
            clap_count += 1
    if clap_count > 0: # clap_count 존재한다면
        print('-' * clap_count, end=' ') # clap_count 만큼 - 출력
    else:
        print(num, end=' ') # clap_count가 없으면 숫자 그대로 출력
