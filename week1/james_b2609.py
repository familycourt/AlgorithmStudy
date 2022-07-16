import sys
n, m = [int(n) for n in sys.stdin.readline().strip().split()]

gcf = min(n, m)
for i in range(1, min(n, m) + 1):
    if n % i == 0 and m % i == 0:
        gcf = i

print(gcf)
print(int(n * m / gcf))
