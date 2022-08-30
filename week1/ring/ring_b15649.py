# 6:11 ~ 
import sys
import itertools 

a, b = map(int, sys.stdin.readline().strip().split())
list_a = [i for i in range(1, a+1)]

answer = list(itertools.permutations(list_a,b))

for i in answer :
    print(*i)