# 부분수열의 합

import sys
import itertools

N, S = map(int, sys.stdin.readline().split())

a = [int(x) for x in sys.stdin.readline().split()]

cnt = 0

for i in range(1, N + 1):
    comb_arr = itertools.combinations(a, i)

    for x in comb_arr:
        if sum(x) == S:
            cnt += 1

print(cnt)
