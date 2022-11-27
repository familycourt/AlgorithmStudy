# 하노이 탑 이동 순서

import sys
# 원판의 개수 N
N =  int(sys.stdin.readline().rstrip())

# N 홀수일 때 3에 먼저 올려야함
# N 짝수일 때 2에 먼저 올려야함

def hanoi(N, a, b, c):
    if N == 1:
        print(a, c, sep = " ")
    else:
        hanoi(N - 1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(N - 1, b, a, c)

print(2**N - 1)
if(N <= 20):
    hanoi(N, 1, 2, 3)
