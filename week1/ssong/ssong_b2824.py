# 최대공약수

import sys
import math

N = int(sys.stdin.readline())
arr_N = [int(x) for x in sys.stdin.readline().split()]

M = int(sys.stdin.readline())

arr_M = [int(x) for x in sys.stdin.readline().split()]

total_N = 1
total_M = 1
for num in arr_N:
    total_N *= num
for num in arr_M:
    total_M *= num

result = math.gcd(total_N, total_M)
print(str(result)[-9:])  # 자리수 절삭 좋은방법 생각 필요
