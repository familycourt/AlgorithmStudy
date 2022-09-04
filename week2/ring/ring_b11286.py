# 코드 참조

import heapq
import sys
input = sys.stdin.readline

arr = []
queue = []
N = int(input().strip())

for _ in range(N) :
    x = int(input().strip())

    if x == 0 :
        if not queue :
            print(0)
        else :
            print(heapq.heappop(queue)[1])
    else :
        heapq.heappush(queue, (abs(x), x))