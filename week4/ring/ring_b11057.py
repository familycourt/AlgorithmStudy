import sys
input = sys.stdin.readline


N = int(input().strip())
numbers = [[1 for _ in range(10)]] + [[0 for _ in range(10)] for _ in range(N-1)]

for i in range(1, N) :
    tmp = 0
    for j in range(10) :
        tmp += numbers[i-1][j]
        numbers[i][j] = tmp

print(sum(numbers[N-1])%10007)

