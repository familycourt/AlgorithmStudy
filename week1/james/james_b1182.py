from sys import stdin
from itertools import combinations

_, num = [int(x) for x in stdin.readline().strip().split(' ')]

a = [int(x) for x in stdin.readline().strip().split(' ')]


x = [list(combinations(a, i)) for i in range(1, len(a) + 1)]

cnt = 0

for i in x:
    for case in i:
        if sum(case) == num:
            cnt += 1

print(cnt)
