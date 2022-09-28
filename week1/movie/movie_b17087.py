import sys


def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def gcdAll(list):
    candidate = list[0]

    for index in range(1, len(list)):
        candidate = gcd(candidate, list[index])

    return candidate


N, S = map(int, sys.stdin.readline().split())
brothers = list(map(int, sys.stdin.readline().split()))

diff = list(map(lambda x: x - S if x > S else S - x, brothers))


print(gcdAll(diff))
