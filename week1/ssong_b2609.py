# 최대공약수와 최소공배수

import math
import sys
N, M = map(int, sys.stdin.readline().split())

# 최대공약수
greatest_common_divisor = math.gcd(N, M)
# 최소공배수
least_common_multiple = math.lcm(N, M)

print(greatest_common_divisor)
print(least_common_multiple)
