import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())


for case in combinations([num for num in range(1, N + 1)], M):
    print(' '.join(map(str, case)))
