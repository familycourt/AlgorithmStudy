# N과 M (2)

import sys
import itertools
N, M = map(int, sys.stdin.readline().split())

arr = [int(a + 1) for a in range(N)]
result = list(itertools.combinations(arr, M))

for i in result:
    print(*i)
