# 절댓값 힙

import sys
import heapq

N = int(sys.stdin.readline().rstrip())
queue = []

for i in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x != 0:
        heapq.heappush(queue, (abs(x), x))
    else:
        if not queue:
            print(0)
        else:
            print(heapq.heappop(queue)[1])
