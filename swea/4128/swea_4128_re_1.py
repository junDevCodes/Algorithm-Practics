from itertools import combinations

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    min_score = float("inf")
    food_num = set([i for i in range(1, N + 1)])
    food_list = [[0]]+[[0]+list(map(int, input().split())) for _ in range(N)]
    n = N // 2

    comb_list = list(combinations(food_num, n))

    for idx in range(len(comb_list) // 2):
        score_1, score_2 = 0, 0
        comb = comb_list[idx]
        other = list(food_num - set(comb_list[idx]))
        for i in range(n):
            for j in range(n):
                if i != j:
                    score_1 += food_list[comb[i]][comb[j]]
                    score_2 += food_list[other[i]][other[j]]

        min_score = min(min_score, abs(score_1 - score_2))
    print(f"#{tc} {min_score}")