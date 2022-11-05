# 큐

from collections import deque
import sys

calculate_number = int(sys.stdin.readline().rstrip())
# list로 큐 구현하면 insert함수에서 시간초과
# insert는 O(n)
queue = deque()


def is_empty(queue):
    if len(queue) == 0:
        return True
    else:
        return False


def get_size(queue):
    print(len(queue))


def push(queue, num):
    queue.appendleft(num)


def pop(queue):
    if is_empty(queue):  # 스택 비어있다면
        print("-1")
    else:
        print(queue.pop())


def is_empty_queue(queue):
    if is_empty(queue):
        print('1')
    else:
        print('0')


def front(queue):
    if is_empty(queue):
        print('-1')
    else:
        print(queue[-1])


def back(queue):
    if is_empty(queue):
        print('-1')
    else:
        print(queue[0])


for _ in range(calculate_number):
    menu = [x for x in sys.stdin.readline().split()]
    if(menu[0] == 'push'):
        push(queue, int(menu[1]))
    elif(menu[0] == 'pop'):
        pop(queue)
    elif(menu[0] == 'size'):
        get_size(queue)
    elif(menu[0] == 'empty'):
        is_empty_queue(queue)
    elif(menu[0] == 'front'):
        front(queue)
    elif(menu[0] == 'back'):
        back(queue)
