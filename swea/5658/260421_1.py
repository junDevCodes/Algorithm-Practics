T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    word = input()
    cut = N // 4

    text = word * 2

    word_set = set()

    for idx in range(N):
        word_set.add(int(text[idx:idx+cut], 16))

    word_list = []

    for item in word_set:
        word_list.append(item)

    word_list.sort(reverse=True)
    answer = word_list[K-1]

    print(f"#{tc} {answer}")
