import sys

def getcom(n : int, m : int):
    result = 1
    for x in range(n-m+1, n+1) :
        result *= x
    for x in range(2, m+1) :
        result //= x

    return result 


N, M = sys.stdin.readline().strip().split()
N, M = int(N), int(M)

if N-M < M :
    print(getcom(N, N-M))
else :
    print(getcom(N, M))