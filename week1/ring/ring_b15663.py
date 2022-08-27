import sys
import itertools

N, M = sys.stdin.readline().strip().split()
N, M = int(N), int(M)

Nlist = [int(x) for x in sys.stdin.readline().strip().split()]
answers = [x for x in itertools.permutations(Nlist, M)]
for answer in sorted(set(answers)) :
    print(*answer)