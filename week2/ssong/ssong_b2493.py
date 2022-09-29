# 탑

import sys

N = int(sys.stdin.readline().rstrip())

tower = [int(x) for x in sys.stdin.readline().rstrip().split()]

# 본인보다 더 큰 수가 나올 때 pop
# 스택을 만들어본다
# 스택을 순회하는게 낫겠지?

stack = []
output = []
tmp = 0

for i in range(N):

    while stack:
        if stack[-1][1] > tower[i]:
            output.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        output.append(0)
    stack.append([i, tower[i]])

print(' '.join(map(str, output)))
