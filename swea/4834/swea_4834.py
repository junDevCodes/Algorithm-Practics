T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    repeat = int(input())
    card_list = {}
    card = input()
    
    for num in card:
        if num in card_list:
            card_list[num] += 1
        else:
            card_list[num] = 1
    
    sorted_card = list(sorted(card_list.items(), key= lambda card: (card[1], card[0]), reverse=True))
    max_val = sorted_card[0][0]
    count = sorted_card[0][1]
    print(f"#{test_case} {max_val} {count}")
    pass