from sys import stdin
from itertools import combinations

a = []
while True:
    line = [x for x in stdin.readline().strip().split()]
    a.append(line)
    if line[0] == '0':
        break

for pool in a:
    [print(' '.join(case)) for case in combinations(pool[1:], 6)]
    print()
