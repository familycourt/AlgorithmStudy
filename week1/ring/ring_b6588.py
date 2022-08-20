# 8:20 ~ 8:44

import math 

def is_prime(n):
  if(n==1):
    return False

  m = math.sqrt(n)
  for i in range(2, n+1):
    if(i > m):
      return True
    if n%i  == 0:
      return False
  return False

def gold(n) :
    for i in range(3, int(n//2)+1, 2) :
        if is_prime(i) & is_prime(n-i) & n-i%2!=0:
            return i, n-i
    return 0,0
            

import sys

numbers=[]
while True:    
    n = int(sys.stdin.readline().strip())
    if n==0 :
        break
    else : 
        numbers.append(n)

for number in numbers :
    a,b = gold(number)
    if a ==0 :
        print('Goldbach\'s conjecture is wrong.')
    else :
        print(number , '=' , a , '+' , b)