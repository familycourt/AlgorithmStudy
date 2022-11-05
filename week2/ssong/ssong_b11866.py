# 요세푸스 문제 0

import sys

N, K = [int(x) for x in sys.stdin.readline().rstrip().split()]

round_queue = [int(i) for i in range(1, N + 1)]

delete_order = []
index = 0
while N > 0:
    index += K
    if index > N:
        while index > N:
            index -= N
    tmp = round_queue.pop(index - 1)
    delete_order.append(str(tmp))
    index -= 1
    N -= 1

print("<",end="")
print(', '.join(delete_order), end="")
print(">", end="")
