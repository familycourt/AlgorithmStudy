import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))


for case in sorted(set(permutations(nums, M))):
    print(*case)
