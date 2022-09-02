# N과 M (9)

import sys
import itertools

N, M = [int(x) for x in sys.stdin.readline().split()]

array_N = [int(x) for x in sys.stdin.readline().split()]

result = list(itertools.permutations(array_N, M))
result = sorted(set(result))

for i in result:
    print(*i)
