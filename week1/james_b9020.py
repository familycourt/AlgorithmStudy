from sys import stdin

n = int(stdin.readline().strip())

factor = 2
while n != 1:
    if n % factor == 0:
        print(factor)
        n = int(n / factor)
        factor = 2
    else:
        factor += 1
