import sys
input = sys.stdin.readline

N= int(input().strip())
tops = [int(x) for x in input().strip().split()]
stack = []
index = []
answers = ['']*N

while tops :
    top = tops.pop()

    if not stack :
        stack.append(top)
    else :
        while stack :
            if stack[-1] < top :
                stack.pop()
                answers[index.pop()] = str(N)
            else : break
        stack.append(top)
    
    N -= 1
    index.append(N)

while stack :
    stack.pop()
    answers[index.pop()] = str(N)

print(' '.join(answers))