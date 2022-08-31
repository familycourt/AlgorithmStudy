import sys
import math

N = int(sys.stdin.readline())
input = []
multipleList = []


def GCD(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def GCDAll(list):
    candidate = list[0]

    for index in range(len(list)):
        candidate = GCD(candidate, list[index])

    return candidate


def getDivisors(num):
    divisors = []

    for n in range(1, math.ceil(math.sqrt(num)) + 1):
        if num % n == 0:
            divisors.append(n)
            if n != num // n:
                divisors.append(num // n)

    return sorted(divisors[1:])


for _ in range(N):
    input.append(int(sys.stdin.readline()))

input.sort()

try:
    for index, num in enumerate(input, start=1):
        multipleList.append(input[index] - num)
except:
    None

gcd = GCDAll(multipleList)

for divisor in getDivisors(gcd):
    print(divisor, end=' ')
