# 골드바흐 파티션

import sys
import math

# 소수판별 제곱근으로 하면 시간초과


def eratosthenes_sieve(N):
    # 전체 체 초기화 : 모두 소수로 가정
    sieve = [True] * (N + 1)

    m = int(N ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i * 2, N + 1, i):  # (시작범위, 마지막 범위, range 간격)
                sieve[j] = False

    return sieve


def find_goldbach_partition(num, arr):
    half_num = num // 2
    count = 0
    for i in range(1, half_num + 1):
        if arr[i] == True and arr[num - i] == True:  # 소수라면
            count += 1

    return count


number_test_case = int(sys.stdin.readline())

arr = eratosthenes_sieve(1000000)
arr[0] = False
arr[1] = False

for i in range(number_test_case):
    num = int(sys.stdin.readline())
    print(find_goldbach_partition(num, arr))
