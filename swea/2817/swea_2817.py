# SWEA 2817 문제 풀이
# import sys
# from pathlib import Path
#
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / 'sample_input.txt'
# sys.stdin = file_path.open('r', encoding='utf-8')
#
# T = int(sys.stdin.readline().strip("\n"))
"""
[문제 설명]
여기에 문제 요약과 요구사항을 작성하세요.

[입력]
- 입력 형식에 대한 설명
- 각 줄별 입력 내용

[출력]
- 출력 형식에 대한 설명

[로직]
- 문제 해결에 필요한 알고리즘

[예시 입력]
예시 입력 내용을 작성

[예시 출력]
예시 출력 내용을 작성
"""
T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    num, target = map(int, input().split())
    num_list = list(map(int, input().split()))

    count = 0
    num_list.sort()

    def solve(idx, current_sum):
        global count

        # **가지치기(Pruning):** 현재 합이 목표 합보다 크면
        # 더 이상 탐색할 필요가 없으므로 즉시 함수를 종료합니다.
        if current_sum > target:
            return

        # **종료 조건:** 모든 숫자를 다 확인했을 때
        if idx == num:
            # 최종 합이 목표 합과 같으면 카운트를 1 증가시킵니다.
            if current_sum == target:
                count += 1
            return

        # 1. 현재 숫자를 합에 포함하는 경우
        solve(idx + 1, current_sum + num_list[idx])

        # 2. 현재 숫자를 합에 포함하지 않는 경우
        solve(idx + 1, current_sum)


    # 0번 인덱스부터 시작하며, 초기 합은 0입니다.
    solve(0, 0)

    print(f"#{test_case} {count}")
