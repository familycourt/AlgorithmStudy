from collections import deque
import sys
input = sys.stdin.readline

P = int(input().strip())
for i in range(P) :
    N, M = map(int, input().strip().split())
    imp = [int(x) for x in input().strip().split()]
    idx = deque([int(x) for x in range(N)])


    
    cnt = 0
    while M > -1 :
        if imp[idx[0]] < max(imp) :
            idx.rotate(-1)
        else :
            if idx[0] == M :
                M = -1
            cnt+=1
            imp[idx[0]] = -1
            idx.popleft()
        
    print(cnt)