# 다른 사람 코드 참고 

import sys
input = sys.stdin.readline

N = int(input().strip())

numbers = [[0 for _ in range(10)] for _ in range(N+1)]
numbers[1][0] = 0
for i in range(1,10) :
    numbers[1][i] = 1

for i in range(2, N+1) :
    numbers[i][0] = numbers[i-1][1]
    for j in range(1, 9) :
        numbers[i][j] = numbers[i-1][j-1] + numbers[i-1][j+1]
    numbers[i][9] = numbers[i-1][8]

print(sum(numbers[N])%1000000000)
    