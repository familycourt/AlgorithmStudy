# 모든 순열

import sys
import itertools

N = int(sys.stdin.readline())

a = [int(x) for x in range(1, N + 1)]

result = list(itertools.permutations(a, N))

for i in result:
    print(*i)
