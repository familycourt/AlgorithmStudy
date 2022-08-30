# 약수
import sys

number_real_divisor = int(sys.stdin.readline())

arr_real_divisor = [int(x) for x in sys.stdin.readline().split()]

if number_real_divisor == 1:
    print(arr_real_divisor[0] * arr_real_divisor[0])
else:
    print(max(arr_real_divisor) * min(arr_real_divisor))
