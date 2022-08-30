# 유클리드로 gcd 안짜면 runtime error

import sys
import math

N = int(sys.stdin.readline().strip())
Alist = [int(x) for x in sys.stdin.readline().strip().split()]
M = int(sys.stdin.readline().strip())
Blist = [int(x) for x in sys.stdin.readline().strip().split()]

a = math.prod(Alist)
b = math.prod(Blist)
answer = math.gcd(a, b)

print(str(answer)[-9:])