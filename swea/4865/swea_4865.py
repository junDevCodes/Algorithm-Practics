# 4865. [파이썬 S/W 문제해결 기본] 1일차 - 글자수 세기

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    string1 = input()
    string2 = input()

    word_dict = {}

    for char in sorted(set(string1)):
        word_dict[char] = string2.count(char)

    print(f'#{test_case} {max(word_dict.values())}')  # Assuming test_case is always 1 as per the original code