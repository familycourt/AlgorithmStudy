from collections import deque
import sys
input = sys.stdin.readline

N = int(input().strip())
queue = deque([int(x) for x in range(1,N+1)])

while len(queue) > 1 :
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])