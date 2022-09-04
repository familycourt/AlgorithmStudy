# 스택

import sys

calculate_number = int(sys.stdin.readline())

stack = []

def is_empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False

def get_size(stack):
    print(len(stack))

def push(stack, num):
    stack.append(num)

def pop(stack):
    if is_empty(stack): # 스택 비어있다면
        print("-1")
    else:
        print(stack.pop())

def is_empty_stack(stack):
    if is_empty(stack):
        print('1')
    else:
        print('0')

def get_top(stack):
    if is_empty(stack): # 스택 비어있다면
        print('-1')
    else:
        print(stack[-1])

for _ in range(calculate_number):
    menu = [x for x in sys.stdin.readline().split()]
    if(menu[0] == 'push'):
        push(stack, int(menu[1]))
    elif(menu[0] == 'pop'):
        pop(stack)
    elif(menu[0] == 'size'):
        get_size(stack)
    elif(menu[0] == 'empty'):
        is_empty_stack(stack)
    elif(menu[0] == 'top'):
        get_top(stack)