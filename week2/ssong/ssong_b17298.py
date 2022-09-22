# 오큰수

import sys
from collections import deque

N = int(sys.stdin.readline())

A = [int(x) for x in sys.stdin.readline().rstrip().split()]
# list insert 함수 O(N)
# deque appendleft함수 O(1)
stack = []
answer = deque()
for i in range(N - 1, -1, -1):
    while stack:
        if stack[-1] > A[i]:
            answer.appendleft(stack[-1])
            break
        else:
            stack.pop()
    if not stack:
        answer.appendleft(-1)
    stack.append(A[i])
print(' '.join(map(str, answer)))
