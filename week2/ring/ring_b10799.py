import sys
input = sys.stdin.readline

laser = [x for x in input().strip()]
stack = []
cnt = 0

for x in laser :
    if x == '(' :
        stack.append(1)
    elif x == ')' : 
        if tmp =='(':
            stack.pop()
            cnt += len(stack)          
        else :
            cnt += stack.pop()
    
    tmp = x

print(cnt)