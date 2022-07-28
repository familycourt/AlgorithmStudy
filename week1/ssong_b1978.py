import sys
import math

N = int(sys.stdin.readline())

def is_prime_num(num):
    if num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

a = [int(x) for x in sys.stdin.readline().strip().split()]

cnt = 0
for i in range(N):
    if is_prime_num(a[i]) == True:
        cnt += 1

print(cnt)