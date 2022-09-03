from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
people = deque([int(x)+1 for x in range(N)])
answer = []

while people : 
    for i in range(K-1) :
        people.rotate(-1)
    answer.append(str(people.popleft()))

print('<', end='')
print(', '.join(answer), end='')
print('>')