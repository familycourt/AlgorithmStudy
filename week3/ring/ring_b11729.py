# 이거 1914번과 동일 !

import sys
input = sys.stdin.readline

def hanoi(n:int, x:int, y:int, z:int) :
    if n==1 :
        print(x, z)
        return

    hanoi(n-1, x, z, y)
    print(x, z)
    hanoi(n-1, y, x, z)

N = int(input().strip())
K = 2**N-1

if N<=20 : hanoi(N, 1, 2, 3)