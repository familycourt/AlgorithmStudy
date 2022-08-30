import math
from sys import stdin

n = int(stdin.readline().strip())
str = stdin.readline().strip()
list = str.split()

# n까지 검사할 필요가 없다 ~ 왜냐? 앞에서 이미 검사한거기 때문이다 ~
def is_prime(n):
  if(n==1):
    return 0

  m = math.sqrt(n)
  for i in range(2, n+1):
    if(i > m):
      return 1
    if n%i  == 0:
      return 0
  return -1
    
cnt=0
for i in list:
  n = int(i)
  cnt += int(is_prime(n))

print(cnt)