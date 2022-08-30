import math
from sys import stdin

# 문자열.split('구분자') -> 리스트로 만들어줌 허거덩~
str = stdin.readline().strip()
list = str.split()

a,b = int(list[0]), int(list[1])

# n까지 검사할 필요가 없다 ~ 왜냐? 앞에서 이미 검사한거기 때문이다 ~
def is_prime(n):
  m = math.sqrt(n)
  for i in range(2, n+1):
    if(i > m):
      print(n)
      break
    if n%i  == 0:
      break
    

for i in range(a, b+1):
  is_prime(i)