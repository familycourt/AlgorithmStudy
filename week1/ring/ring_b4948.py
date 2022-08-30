# 5:31 ~ 

import math
from sys import stdin

# n까지 소수인지 확인하는 함수 eratos
def eratos(n) :
    m = 2*n
    eratos_list = [0 for i in range(m+1)]
    for i in range(2,m+1) :
        if eratos_list[i] == 1 :
            continue
        else :
            j=2
            tmp_i = i
            while True :
                tmp_i = i*j
                j+=1

                if tmp_i > m :
                    break

                eratos_list[tmp_i] = 1

    return eratos_list

x = []
while True:
  n = int(stdin.readline())
  if n == 0 :
    break
  else:
    x.append(n)
m = max(x)

eratoslist  = eratos(m)

for y in x :
    answer=[]
    for i in range(y+1, 2*y+1) :
        if eratoslist[i] == 0 :
            answer.append(i)
    print(len(answer))







 
        