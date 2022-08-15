import sys
a = [int(n) for n in sys.stdin.read().splitlines()][:-1]


def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


for num in a:
    flag = True
    for i in range(3, num):
        if is_prime(i) and is_prime(num - i):
            flag = False
            print('{} = {} + {}'.format(num, i, num - i))
            break
    if flag:
        print("Goldbach's conjecture is wrong.")
