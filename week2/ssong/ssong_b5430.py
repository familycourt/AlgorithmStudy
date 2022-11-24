# AC

import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    flag = 1;
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    num_array = deque(sys.stdin.readline().strip()[1:-1].split(','))
    if n == 0:
        num_array = deque()
    for i in p:
        if i == 'R':
            flag *= (-1)
        elif i == 'D':
            if len(num_array) == 0:
                print("error")
                flag = 0
                break
            else:
                if flag == 1:
                    num_array.popleft()
                elif flag == -1:
                    num_array.pop()
    if flag == -1:
        num_array.reverse()
        print("[" + ",".join(num_array) + "]")
    elif flag == 1:
        print("[" + ",".join(num_array) + "]")

