# 11:51 ~ 11:56

import sys 
import itertools

N, M = map(int, sys.stdin.readline().strip().split())
numbers = [i for i in range(1, N+1)]
answers = list(itertools.combinations(numbers, M))

for answer in answers :
    print(*answer)