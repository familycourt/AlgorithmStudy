# 최대공약수와 최소공배수

import sys

N, M = map(int, sys.stdin.readline().split())

# 시간 초과

# # 최대공약수
# for i in range(min(N, M), 0, -1):
#     if (N % i == 0) and (M % i == 0):
#         print(i)
#         break

# # 최소공배수
# for i in range(max(N, M), (N * M) + 1):
#     if((i % N == 0) and (i % M == 0)):
#         print(i)
#         break


def gcd(N, M):
    while True:
        r = N % M
        if r == 0:
            break
        N = M
        M = r

    return M


print(gcd(N, M))


def lcm(N, M):
    result = N * M // gcd(N, M)
    return result


print(lcm(N, M))
