import sys


import sys
input = sys.stdin.readline

numbers = []
N = int(input().strip())
for _ in range(N) :
    numbers.append(int(input().strip()))

for number in sorted(numbers) :
    print(number)