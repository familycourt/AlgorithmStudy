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


a = [int(x) for x in stdin.readline().rstrip().split(' ')]
[print(x) for x in range(a[0], a[1]+1) if is_prime(x)]
