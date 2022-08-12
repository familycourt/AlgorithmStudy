# 시작 시간 22-07-22 22:25

import sys
import math

M, N = map(int, sys.stdin.readline().split())

b = 0

for i in range(M, N):
    for j in range(2, int(math.sqrt(i) + 1)):
        #print(num, i)
        if i % j == 0:
            b = 1
    
    if b == 0:
        print(i)
    b = 0

