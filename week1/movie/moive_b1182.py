import sys
from itertools import combinations


N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
count = 0


for numCount in range(1, N + 1):
    cases = list(combinations(nums, numCount))
    for case in cases:
        if sum(case) == S:
            count += 1

print(count)
