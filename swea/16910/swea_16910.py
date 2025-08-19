# SWEA 16910 문제 풀이

"""
[문제 설명]
반지름이 N인 원 안에 포함되는 x, y좌표가 모두 정수인 점의 갯수를 구하시오
x^2 + y^2 <= N^2인 격자점의 개수를 구하시오

[입력]
1. TC
2. N

[출력]
1. #{TC} 좌표가 정수인 격좌점의 갯수

[로직]
x, y를 range(N)으로 순회
x^2 + y^2 <= N^2인 경우 추가

[예시 입력]
3
1
10
100

[예시 출력]
#1 5
#2 317
#3 31417
"""
T = int(input())  # 표준 입력 사용 시
# 여러 개의 테스트 케이스를 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())

    cnt = 0
    zero_cnt = 0
    for y in range(0, num + 1):
        for x in range(0, num + 1):
            if x**2 + y**2 <= num**2:
                cnt += 1
                if x == 0 or y == 0:
                    zero_cnt += 1

    cnt *= 4
    cnt -= 3 # 가운데 겹치는 점 제외
    side_cnt = zero_cnt-1
    cnt -= side_cnt * 2

    print(f"#{test_case} {cnt}")
