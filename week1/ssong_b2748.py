import sys

# def fibo(N):
#     if N == 1:
#         return 0
#     elif N == 2:
#         return 1
#     else:
#         return fibo(N-1) + fibo(N-2)
# 재귀로 하면 시간초과

N = int(sys.stdin.readline())

alist = [0, 1]

for i in range(N-1):
    alist.append(alist[i] + alist[i+1])

print(alist[N])
