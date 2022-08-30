import sys
input = sys.stdin.readline

num_list = []

K = int(input().strip())
for i in range(K) :
    N = int(input().strip())
    if N != 0 :
        num_list.append(N)
    else :
        num_list.pop()

print(sum(num_list))