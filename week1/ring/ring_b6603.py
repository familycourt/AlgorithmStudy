# 9:28 ~ 9:41

import sys
import itertools

n =[]
while True:
    m = [int(x) for x in sys.stdin.readline().strip().split()]
    n.append(m)
    if m[0]==0 : break

for x in n : 
    y = x[1:]

    result = list(itertools.combinations(y, 6))
    for j in result :
        print(*j)
    print()
