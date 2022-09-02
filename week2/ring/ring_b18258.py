# pop 명령어를 pop(0)으로 해결하면 시간초과 
## 해결 1. head를 사용해서 1씩 늘려주기
## 해결 2. dequeue 사용

import sys
input = sys.stdin.readline
from collections import deque

queue = deque([])

N = int(input().strip())
for i in range(N) :
    command = input().strip().split()
    
    if command[0] == 'push' :
        queue.append(command[1])
    elif command[0] == 'pop' :
        if not queue:
            print(-1)
        else :
            print(queue.popleft())
    elif command[0] == 'size' :
        print(len(queue))
    elif command[0] == 'empty' :
        if not queue:
            print(1)
        else : print(0)
    elif command[0] == 'front' :
        if not queue:
            print(-1)
        else : 
            print(queue[0])
    elif command[0] == 'back' :
        if not queue:
            print(-1)
        else : 
            print(queue[-1])