import sys
input = sys.stdin.readline

n = int(input().strip())
nlist = list(map(int, input().strip().split()))
sumlist = [0 for _ in range(n)]

sumlist[0] = nlist[0]
for i in range(1, n) :
    if sumlist[i-1] > 0 :
        sumlist[i] += sumlist[i-1]
    sumlist [i] += nlist[i]

print(max(sumlist))

