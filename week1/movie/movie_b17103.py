import sys


MAX = 1000000
isPrime = [False, False] + [True] * (MAX - 1)

for i in range(2, MAX + 1):
    if isPrime[i]:
        for j in range(2 * i, MAX + 1, i):
            isPrime[j] = False


def getGoldbachPartitionCount(num):
    cnt = 0

    for i in range(num // 2 + 1):
        if isPrime[i] and isPrime[num - i]:
            cnt += 1

    return cnt


T = int(sys.stdin.readline())

for _ in range(T):
    num = int(sys.stdin.readline())
    print(getGoldbachPartitionCount(num))
