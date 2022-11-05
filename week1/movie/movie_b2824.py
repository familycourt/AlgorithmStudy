from functools import reduce
import sys


def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


N = int(sys.stdin.readline())
ADivisors = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
BDivisors = list(map(int, sys.stdin.readline().split()))

A = reduce(lambda x, y: x * y, ADivisors)
B = reduce(lambda x, y: x * y, BDivisors)

print(str(gcd(*((A, B) if A > B else (B, A))))[-9:])
