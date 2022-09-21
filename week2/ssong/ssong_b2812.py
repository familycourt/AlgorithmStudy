# 크게 만들기

import sys

N, K = [int(x) for x in sys.stdin.readline().rstrip().split()]

num = list(sys.stdin.readline().rstrip())
stack = []
delete_count = K

for i in range(N):
    while delete_count and stack:
        if stack[-1] < num[i]:
            stack.pop()
            delete_count -= 1
        else:
            break
    stack.append(num[i])

print(''.join(stack[:N-K]))
