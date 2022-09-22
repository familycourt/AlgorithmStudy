# 카드2

from collections import deque
import sys

N = int(sys.stdin.readline())

card = deque()

for i in range(N):
    card.append(i + 1)

while len(card) > 1:
    card.popleft()
    tmp = card.popleft()
    card.append(tmp)

print(*card)
