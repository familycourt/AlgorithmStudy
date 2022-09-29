# N과 M (8)

import sys
import itertools

N, M = [int(x) for x in sys.stdin.readline().split()]

a = [int(x) for x in sys.stdin.readline().split()]
a.sort()
result = list(itertools.combinations_with_replacement(a, M))


for i in sorted(set(result)):
    print(*i)
