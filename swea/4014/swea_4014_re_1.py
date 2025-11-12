import sys
sys.stdin = open("sample_input.txt", encoding="utf-8")


def check(line):
    """한 줄이 활주로 건설 가능한지 체크"""
    installed = [False] * len(line)

    for i in range(len(line) - 1):
        diff = line[i] - line[i + 1]

        # 평지
        if diff == 0:
            continue

        # 높이 차이가 2 이상
        if abs(diff) > 1:
            return 0

        # 내리막 (다음이 낮음)
        if diff == 1:
            for j in range(i + 1, i + 1 + X):
                if j >= len(line) or line[j] != line[i + 1] or installed[j]:
                    return 0
                installed[j] = True

        # 오르막 (다음이 높음)
        else:
            for j in range(i, i - X, -1):
                if j < 0 or line[j] != line[i] or installed[j]:
                    return 0
                installed[j] = True

    return 1


T = int(input())

for tc in range(1, T + 1):
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    rotate_board = list(map(list, zip(*board)))
    result = 0

    for r in range(N):
        result += check(board[r]) + check(rotate_board[r])
    print(f"#{tc} {result}")
