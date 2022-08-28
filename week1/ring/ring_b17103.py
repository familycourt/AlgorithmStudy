# pypy3로 제출하면 시간초과 해결댐 ^^;; 진짜 열받네

import math

def eratos(n : int) :
    eratos_list = [False, False] + [True]*n
    for i in range(2, int(math.sqrt(n))+1) :
        if eratos_list[i] :
                for j in range(2, int(n//i)+1) :
                    eratos_list[i*j] = False

    return eratos_list

import sys 
input = sys.stdin.readline

T = int(input().strip())
testcase = [int(input().strip()) for _ in range(T)]

eratos_list = eratos(max(testcase))

for case in testcase :
    cnt = 0

    for i in range(2, case//2+1) : 
        if eratos_list[i] & eratos_list[case-i] :
            cnt+=1      
    print(cnt)
