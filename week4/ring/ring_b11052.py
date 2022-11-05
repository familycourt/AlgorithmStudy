import sys
input = sys.stdin.readline

N = int(input().strip())
P = [0] + list(map(int, input().strip().split()))
price = [0 for _ in range(N+1)]

price[1] = P[1]
for i in range(2, N+1) :
    price[i] = P[i]
    for j in range(1, i//2+1) :
        price[i] = max(price[j]+price[i-j], price[i])
    
print(price[N])