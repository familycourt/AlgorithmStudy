# 재경 : 이게 시간초과 안나면 자기코드가 더 우수하다 -> 시간초과 남 ㅎ
# 결국 stack으로 푸는게 맞았다.. 후
# 다른 사람 코드 참조

import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
numbers = [int(x) for x in input().strip()]
k = K
stack = []

for number in numbers :
    while stack and k>0 and stack[-1] < number :
            stack.pop()
            k -= 1
    stack.append(number)

stack = map(str, stack[:N-K])
print(''.join(stack))
