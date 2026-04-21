T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    cut = N//4
    num = input()
    num_double = num*2

    set_list = set()
    for n in range(N):
        set_list.add(num_double[n:n+cut])

    num_list = []
    for item in set_list:
        num_list.append(int(item, 16))

    num_list.sort(reverse = True)

    print(f"#{tc} {num_list[K-1]}")