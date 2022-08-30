# 6:31 ~

def eratos(m) :
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

def gold(n) :
    m = int(n//2)
    eratoslist = eratos(n)

    for i in range(m, n+1) :
        if eratoslist[i] == 0 :
            if eratoslist[n-i] == 0:
                return i, n-i

    return 0,0

import sys

n = int(sys.stdin.readline().strip())
numbers = [int(sys.stdin.readline().strip()) for _ in range(n)]

for number in numbers :
    a,b = gold(number)
    print(b, a)


