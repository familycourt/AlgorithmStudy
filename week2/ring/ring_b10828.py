import sys
input = sys.stdin.readline

stack = []

N = int(input().strip())
for i in range(N) :
    command = input().strip().split()

    if command[0] == 'push' :
        stack.append(command[1])
    elif command[0] == 'pop' :
        if not stack :
            print(-1)
        else :
            print(stack.pop())
    elif command[0] == 'size' :
        print(len(stack))
    elif command[0] == 'empty' :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    elif command[0] == 'top' :
        if not stack :
            print(-1)
        else :
            print(stack[-1])
