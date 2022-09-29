from collections import deque
import sys 
input = sys.stdin.readline

N, M = map(int, input().strip().split())
Mlist = [int(x) for x in input().strip().split()]
queue = deque([int(x) for x in range(1,N+1)])

answer = 0
for m in Mlist :
    cnt =0
    while queue[0] != m :
        queue.rotate(1)
        cnt += 1

    if cnt < len(queue) - cnt :
        answer += cnt
    else :
        answer += len(queue) - cnt
    
    queue.popleft()

print(answer)
