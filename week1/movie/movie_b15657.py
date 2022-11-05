import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

for case in combinations_with_replacement(nums, M):
    print(*case)
