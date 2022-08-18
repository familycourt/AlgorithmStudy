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


x = [1 for _ in range(max(a) * 2 + 1)]
i = 2
while i * i <= max(a) * 2 + 1:
    if (is_prime(i)):
        x = [0 if n % i == 0 and n != i else _ for n, _ in enumerate(x)]
    i += 1
x[1] = 0
for n in a:
    print(sum(x[n + 1:n * 2 + 1]))
