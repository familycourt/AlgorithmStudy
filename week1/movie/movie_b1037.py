import sys


N = int(sys.stdin.readline())
divisors = list(map(int, sys.stdin.readline().split()))

print(min(divisors) * max(divisors))
