import sys
from itertools import permutations

n, m = [int(x) for x in sys.stdin.readline().strip().split()]
[print(*a) for a in list(permutations([x for x in range(1, n + 1)], m))]
