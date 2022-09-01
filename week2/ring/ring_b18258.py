# pop 명령어를 pop(0)으로 해결하면 시간초과 
## 해결 1. head를 사용해서 1씩 늘려주기
## 해결 2. dequeue 사용

import sys
input = sys.stdin.readline

head = 0
queue = []

N = int(input().strip())
for i in range(N) :
    command = input().strip().split()
    
    if command[0] == 'push' :
        queue.append(command[1])
    elif command[0] == 'pop' :
        if head == len(queue):
            print(-1)
        else :
            print(queue[head])
            head += 1
    elif command[0] == 'size' :
        print(len(queue)-head)
    elif command[0] == 'empty' :
        if head == len(queue):
            print(1)
        else : print(0)
    elif command[0] == 'front' :
        if head == len(queue):
            print(-1)
        else : 
            print(queue[head])
    elif command[0] == 'back' :
        if head == len(queue):
            print(-1)
        else : 
            print(queue[-1])