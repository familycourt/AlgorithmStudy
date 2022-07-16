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


n = int(stdin.readline().rstrip())
a = [int(x) for x in stdin.readline().rstrip().split(' ')]
print(sum([1 for x in a if is_prime(x)]))
