import sys
import math

def gcd(n, m):
    if n%m == 0 : return m
    else : return gcd(m, n%m)

N = int(sys.stdin.readline().strip())
M = [int(sys.stdin.readline().strip()) for _ in range(N)]
M.sort()

numbers = [M[m]-M[m-1] for m in range(1,N)]

gcd_num = numbers[0]
for number in numbers[1:] :
   gcd_num = gcd(gcd_num, number)

answer = []
for i in range(2,int(math.sqrt(gcd_num))+1) :
    if gcd_num%i==0:
        answer.append(i)
        answer.append(gcd_num//i)
answer.append(gcd_num)

# 중복제거
answer = list(set(answer))

answer.sort()
print(*answer)