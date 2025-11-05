T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    word = input()
    cut = N // 4
    sentence = word + word

    num_list = set()

    for idx in range(N):
        num_list.add(int(sentence[idx:idx+cut], 16))

    num_list = list(num_list)
    num_list.sort(reverse=True)

    print(f"#{tc} {num_list[K-1]}")

