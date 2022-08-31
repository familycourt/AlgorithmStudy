# 다른 사람 코드 참고
 
import sys 
input = sys.stdin.readline

stack1 = [x for x in input().strip()]
stack2 = []
M = int(input().strip())

for i in range(M) :
    command = input().strip().split()
    if command[0] == 'L' and stack1 :
        stack2.append(stack1.pop())
    elif command[0] == 'D' and stack2 :
        stack1.append(stack2.pop())
    elif command[0] == 'B' and stack1 :
        stack1.pop()
    elif command[0] == 'P' :
        stack1.append(command[1])

stack1.extend(reversed(stack2))
print(''.join(stack1))