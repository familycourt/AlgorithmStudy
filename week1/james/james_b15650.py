from sys import stdin
from itertools import combinations

N, M = [int(x) for x in stdin.readline().strip().split()]

[print(*case) for case in combinations(range(1, N + 1), M)]
