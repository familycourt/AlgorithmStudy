import sys
import itertools

N, S = map(int, sys.stdin.readline().strip().split())
numbers = [int(x) for x in sys.stdin.readline().strip().split()]

cnt=0
for i in range(1, N+1) :
    result = list(itertools.combinations(numbers, i))
    for j in result :
        if S == sum(j) : cnt+=1

print(cnt)  