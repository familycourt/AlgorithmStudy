# 그냥 피보나치 쓰면 시간초과 남..

import sys
input = sys.stdin.readline

fibonacci = [[1,0], [0,1]]

T = int(input().strip())
for _ in range(T) :
    N = int(input().strip())

    if len(fibonacci) < N+1 :
         for i in range(len(fibonacci), N+1) :
            fibonacci.append([fibonacci[i-2][0]+fibonacci[i-1][0], fibonacci[i-2][1]+fibonacci[i-1][1]])
    
    print(fibonacci[N][0], fibonacci[N][1])


