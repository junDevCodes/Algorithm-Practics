from collections import deque

near_list = {
    2: 6
}

T = int(input())

for tc in range(1, T + 1):

    K = int(input())
    mag_num = 4

    mag_list = [deque([])]+[deque(map(int, input().split())) for _ in range(mag_num)]

    for idx in range(K):
        m, r = map(int, input().split())
        queue = deque([(m, r)])

        visited = [0] * (mag_num + 1)
        visited[m] = 1
        while queue:
            mag, rt = queue.popleft()

            for key, near_mag_key in near_list.items():
                if mag_list[mag][key] != mag_list[min(mag + 1, mag_num)][near_mag_key]:
                    if not visited[min(mag + 1, mag_num)]:
                        queue.append((min(mag + 1, mag_num), (rt * -1)))
                        visited[min(mag + 1, mag_num)] = 1
                if mag_list[max(mag - 1, 1)][key] != mag_list[mag][near_mag_key]:
                    if not visited[max(mag - 1, 1)]:
                        queue.append((max(mag - 1, 1), (rt * -1)))
                        visited[max(mag - 1, 1)] = 1

            mag_list[mag].rotate(rt)

    result = 0
    for idx in range(1, mag_num + 1):
        if mag_list[idx][0]:
            result += 2 ** (idx-1)

    print(f"#{tc} {result}")