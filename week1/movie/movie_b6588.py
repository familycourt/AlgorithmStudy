import sys
import math


def isPrime(n):
    cnt = 0

    for i in range(1, math.ceil(math.sqrt(n + 1))):
        if n % i == 0:
            cnt += 1
            if n // i != i:
                cnt += 1

        if cnt > 2:
            return False

    return True


def goldbach(n):
    for i in range(3, n):
        if isPrime(i) and isPrime(n - i):
            print(n, '=', i, '+', n - i)
            return


while(True):
    n = int(sys.stdin.readline())
    goldbach(n)

    if n == 0:
        break
