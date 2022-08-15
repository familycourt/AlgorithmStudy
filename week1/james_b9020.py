from sys import stdin


def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


n = int(stdin.readline().strip())

for _ in range(n):
    x = int(stdin.readline().strip())

    for i in range(int(x / 2), x):
        if is_prime(i) and is_prime(x - i):
            print(x - i, i)
            break
