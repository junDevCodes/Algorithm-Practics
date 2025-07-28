# SWEA 5097 - 회전
# 문제: 주어진 배열을 왼쪽으로 N번 회전한 후, 첫 번째 원소를 출력하는 문제입니다.
# 입력: 첫 번째 줄에 테스트 케이스의 수 T가 주어지고,   각 테스트 케이스마다 두 개의 정수 seq(배열의 크기)와 goBack(회전 횟수), 그리고 배열의 원소들이 주어집니다.
# 출력: 각 테스트 케이스마다 회전 후 첫 번째 원소를 출력합니다

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    seq, goBack = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(goBack):
        arr.append(arr.pop(0))  # Rotate the array by moving the first element to the end
    print(f"#{test_case} {arr[0]}")  # Output the first element after rotation