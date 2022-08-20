# 6:50 ~ 7:01

import sys
import math

n = int(sys.stdin.readline().strip())
m = int(math.sqrt(n))

i=2

while i <= m:
    while True :
        if n%i != 0 :
            break
        print(i)
        n = n//i
    i+=1

if n!= 1 : print(n)

    