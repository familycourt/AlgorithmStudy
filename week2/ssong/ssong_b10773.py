# 제로

import sys

K = int(sys.stdin.readline())

result = []
for _ in range(K):
    num = int(sys.stdin.readline())
    if((num == 0) and (len(result) != 0)):  # 0이면서 리스트에 수가 있어서 pop을 수행할 수 있을 때
        result.pop()
    elif((num == 0) and (len(result) == 0)):  # 리스트가 비어있어서 pop을 수행할 수 없을 때
        continue
    else:
        result.append(num)

print(sum(result))
