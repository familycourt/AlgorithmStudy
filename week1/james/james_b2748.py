import sys

x = [0, 1]
for _ in range(int(sys.stdin.readline().strip()) - 1):
    x.append(x[-1] + x[-2])
print(x[-1])
