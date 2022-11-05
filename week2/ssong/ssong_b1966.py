# 프린터 큐

from collections import deque
import sys

test_case_number = int(sys.stdin.readline())

for _ in range(test_case_number):
    N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]
    importancy = deque(int(x) for x in sys.stdin.readline().rstrip().split())
    index = deque(int(i) for i in range(N))
    count = 0
    while M > -1:
        if (importancy[0] == max(importancy)) and (index[0] != M):  # 출력하는 상황
            importancy.popleft()
            index.popleft()
            count += 1
        elif (importancy[0] == max(importancy)) and (index[0] == M):
            M = -1
            count += 1
        else:
            importancy.append(importancy.popleft())
            index.append(index.popleft())
    print(count)
