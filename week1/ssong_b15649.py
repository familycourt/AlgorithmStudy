# N과 M (1)

import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
# 내장함수 활용하기
[print(*a) for a in list(itertools.permutations([x for x in range(1, N + 1)], M))]
