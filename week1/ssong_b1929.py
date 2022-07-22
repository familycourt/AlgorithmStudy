# 시작 시간 22-07-22 22:25

import sys

from sympy import false, true

M, N = map(int, sys.stdin.readline().split())

def is_prime_num(num):
    for i in range(2, num):
        if num % i == 0:
            return false
        return true

for i in range(M, N):
    if is_prime_num(i) == true:
        print(i)
