# 덱

from collections import deque
import sys

_deque = deque()

calculate_number = int(sys.stdin.readline())


def is_empty(_deque):
    if len(_deque) == 0:
        return True
    else:
        return False


def get_size(_deque):
    print(len(_deque))


def push_front(_deque, num):
    _deque.appendleft(num)


def push_back(_deque, num):
    _deque.append(num)


def pop_front(_deque):
    if is_empty(_deque):  # 스택 비어있다면
        print("-1")
    else:
        print(_deque.popleft())


def pop_back(_deque):
    if is_empty(_deque):  # 스택 비어있다면
        print("-1")
    else:
        print(_deque.pop())


def is_empty_deque(_deque):
    if is_empty(_deque):
        print('1')
    else:
        print('0')


def front(_deque):
    if is_empty(_deque):
        print('-1')
    else:
        print(_deque[0])


def back(_deque):
    if is_empty(_deque):
        print('-1')
    else:
        print(_deque[-1])


for _ in range(calculate_number):
    menu = [x for x in sys.stdin.readline().split()]
    if(menu[0] == 'push_front'):
        push_front(_deque, int(menu[1]))
    elif(menu[0] == 'push_back'):
        push_back(_deque, int(menu[1]))
    elif(menu[0] == 'pop_front'):
        pop_front(_deque)
    elif(menu[0] == 'pop_back'):
        pop_back(_deque)
    elif(menu[0] == 'size'):
        get_size(_deque)
    elif(menu[0] == 'empty'):
        is_empty_deque(_deque)
    elif(menu[0] == 'front'):
        front(_deque)
    elif(menu[0] == 'back'):
        back(_deque)
