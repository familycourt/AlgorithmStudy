# 골드바흐의 추측2

import sys
import math


def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    check_exception = True
    half_n = n // 2
    for i in range(3, half_n + 1):
        if is_prime(i) == True and is_prime(n - i) == True:  # 소수일 때
            print(f"{n} = {i} + {n - i}")
            check_exception = False
            break
    if check_exception == True:
        print("Goldbach's conjecture is wrong.")
