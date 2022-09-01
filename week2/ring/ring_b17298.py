import sys
input = sys.stdin.readline

N = int(input().strip())
numbers = [int(x) for x in input().strip().split()]
stack = []
index = []
NGE = ['']*N

for i, number in enumerate(numbers) :
    if not stack :
        stack.append(number)
    else :
        while stack :
            if stack[-1] < number :
                stack.pop()
                NGE[index.pop()] = str(number)
            else : break
        stack.append(number)

    index.append(i)

while index :
    NGE[index.pop()] = '-1'

print(' '.join(NGE)) 