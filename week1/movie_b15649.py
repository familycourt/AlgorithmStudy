import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())


num = [_ for _ in range(1, N + 1)]


for case in permutations(num, M):
    for element in case:
        print(element, end=' ')
    print()
