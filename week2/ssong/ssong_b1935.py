# 후위 표기식2

import sys

N = int(sys.stdin.readline())

postfix = str(sys.stdin.readline())

operand = []  # 피연산자
for _ in range(N):
    operand.append(int(sys.stdin.readline()))

diff_tmp = ord('A')
stack = []

for i in range(len(postfix)):
    if(postfix[i] >= 'A' and postfix[i] <= 'Z'):
        stack.append(operand[ord(postfix[i]) - diff_tmp])
    else:
        if(postfix[i] == '+'):
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif(postfix[i] == '-'):
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif(postfix[i] == '*'):
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif(postfix[i] == '/'):
            b = stack.pop()
            a = stack.pop()
            stack.append(a / b)

print(f'{stack.pop():.2f}')
