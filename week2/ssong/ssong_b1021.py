# 회전하는 큐

from collections import deque
from copy import deepcopy
import sys

N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]

pop_number_index = [int(x) for x in sys.stdin.readline().rstrip().split()]
rounding_queue = deque()

pop_number_index.reverse()

def pop_queue_left(queue):
    queue.popleft()

def move_queue_left(queue):
    tmp = queue.popleft()
    queue.append(tmp)

def move_queue_right(queue):
    tmp = queue.pop()
    queue.appendleft(tmp)

for i in range(1, N + 1):
    rounding_queue.append(i)

# 0에서 가장 가까운 수 찾기
count = 0

while pop_number_index:
    left_count = 0
    right_count = 0
    half_queue_length = len(rounding_queue) // 2
    
    if rounding_queue[0] == pop_number_index[-1]:
        pop_queue_left(rounding_queue)
        pop_number_index.pop()
    else:
        tmp_right_queue = deepcopy(rounding_queue) 
        tmp_left_queue = deepcopy(rounding_queue) 
        while pop_number_index[-1] != tmp_right_queue[0]:
            move_queue_right(tmp_right_queue)
            right_count += 1
        while pop_number_index[-1] != tmp_left_queue[0]:
            move_queue_left(tmp_left_queue)
            left_count += 1
        rounding_queue = deepcopy(tmp_right_queue)
        count += min(left_count, right_count)

print(count)
