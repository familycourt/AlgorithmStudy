import heapq
import sys
input = sys.stdin.readline

queue = []
N = int(input().strip())
for _ in range(N) :
    x = int(input().strip())
    
    if x == 0 :
        if queue :
            print(heapq.heappop(queue))
        else :
            print(0)
    else :
        heapq.heappush(queue, x)