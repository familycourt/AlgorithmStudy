# 골드바흐의 추측

import sys

N = int(sys.stdin.readline())

a = []
for i in range(N):
    a.append(int(sys.stdin.readline()))

# TODO: 반 나눠서 소수 찾기?
# TODO: half 부터 거꾸로 찾기?


def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


for i in a:
    half_input = i // 2
    for j in range(half_input, 1, -1):
        if is_prime(j) == True:  # 소수일 때
            if is_prime(i - j) == True:
                print(j, i - j)
                break
