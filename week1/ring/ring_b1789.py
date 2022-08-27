import math

def getsum(S : int) :
    sqrt = int(math.sqrt(2*S))

    # n-1 부터 0까지 (0부터 n-1까지를 reverse 했다고 생각하자)
    for x in reversed(range(sqrt+2)) :
        if x*(x+1) == 2*S :
            return x
        elif x*(x+1) < 2*S :
            return x

import sys

S = int(sys.stdin.readline().strip())
print(getsum(S))