import sys
import itertools

N, M = sys.stdin.readline().strip().split()
N, M = int(N), int(M)

Nlist = [int(x) for x in sys.stdin.readline().strip().split()]
Nlist.sort()
answers = [x for x in itertools.combinations_with_replacement(Nlist, M)]

for answer in sorted(set(answers)) :
    print(*answer)