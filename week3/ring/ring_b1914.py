# 하노이탑은 빠르게 포기..
## 원리 : A->C 로 원판을 보내는데 B를 거점으로 이용한다. 

import sys
input = sys.stdin.readline

answers = []

def hanoi(n : int, a:int, b: int, c:int) :
    # 종료 조건 : 1개 남으면 A -> C
    if n == 1 :
        print(a, c)
        return

    # 출발점 A -> 거점 B로 원판 n-1개 이동
    hanoi(n-1, a, c, b)
    # n-1 개 이동하고 맨 아래에 남은 가장 큰 원판은 바로 도착점 C로 보냄 
    print(a, c)
    # 거점 B -> 도착점 C로 원판 n-1개 이동
    hanoi(n-1, b, a, c)


N =int(input().strip())
print(2**N-1)
if N<= 20 :
    hanoi(N, 1, 2, 3)