# 피보나치 수 5

import sys

n = int(sys.stdin.readline().rstrip())

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibo(n - 1) + fibo(n - 2))

print(fibo(n))