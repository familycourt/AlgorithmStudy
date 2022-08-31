# 조합

import sys

n, m = map(int, sys.stdin.readline().split())

if n == m:
    result = 1
else:
    total = 1
    for i in range(1, n + 1):
        total *= i
        if i == (n - m):
            factorial_n_minus_m = total
        elif i ==  m:
            factorial_m = total
    result = total // (factorial_m * factorial_n_minus_m)

print(result)