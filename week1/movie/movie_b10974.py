import sys
from itertools import permutations

N = int(sys.stdin.readline())

for case in permutations([_ for _ in range(1, N + 1)], N):
    print(*case)
