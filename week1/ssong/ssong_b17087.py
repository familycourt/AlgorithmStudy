# 숨바꼭질 6

import sys
import math
# N은 동생 명수, S는 수빈이의 위치
N, S = [int(x) for x in sys.stdin.readline().split()]

# 동생들의 위치
arr_A = [int(x) for x in sys.stdin.readline().split()]

minus_data_array = [abs(S - x) for x in arr_A]

minus_data_array.sort()

result = minus_data_array[0]

for i in minus_data_array:
    result = math.gcd(result, i)

print(result)
# 좀 더 깊은 이해 필요
