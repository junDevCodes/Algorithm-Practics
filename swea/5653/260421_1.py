def simulate(occupation, cells, time):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for step in range(time):
        temp_cells = []

        for cell in cells:
            [cr, cc, value, age] = cell

            # 활성 상태 - 번식 리스트 넣기
            if age == value:
                for d in range(4):
                    nr, nc = cr + dr[d], cc + dc[d]
                    # 기존 세포칸 내부에 존재하면 pass
                    if (nr, nc) in occupation: continue
                    temp_cells.append([nr, nc, value])

            # 나이 추가 (직접 참조)
            cell[3] += 1
        # value 기준 내림차순
        temp_cells.sort(key=lambda x: -x[2])
        # age가 value * 2 이하인 경우만 남겨두기
        cells = [cell for cell in cells if cell[3] < cell[2] * 2]
        # temp 저장된 cell들 적재
        for [tr, tc, tv] in temp_cells:
            if (tr, tc) in occupation: continue
            occupation.add((tr, tc))
            cells.append([tr, tc, tv, 0])

    return len(cells)

def main():
    T = int(input())

    for tc  in range(1, T + 1):
        H, W, K = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(H)]

        occupation_init = set()
        cells_init = list()

        for r in range(H):
            for c in range(W):
                X = grid[r][c]
                if X > 0:
                    occupation_init.add((r, c))
                    cells_init.append([r, c, X, 0])

        answer = simulate(occupation_init, cells_init, K)

        print(f"#{tc} {answer}")

main()