# 소인수분해

import sys
import math

N = int(sys.stdin.readline())

# 에라토스테네스의 체


def eratosthenes_sieve(N):
    # 전체 체 초기화 : 모두 소수로 가정
    sieve = [True] * (N + 1)

    m = int(N ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i * 2, N + 1, i):  # (시작범위, 마지막 범위, range 간격)
                sieve[j] = False

    true_count = sum(sieve) - 1

    return [i for i in range(2, N+1) if sieve[i] == True]


a = eratosthenes_sieve(N)

while True:  # 소인수 분해 끝날 때까지 while문 돌아감
    if N == 1:
        break
    else:
        for i in a:
            if N % i == 0:  # 나눠진다면
                N = N / i
                print(i)
                break
