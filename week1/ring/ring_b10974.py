import sys 
import itertools

N = int(sys.stdin.readline().strip())
Nlist = [x for x in range(1, N+1)]

answers = list(itertools.permutations(Nlist))
for answer in answers :
    print(*answer)