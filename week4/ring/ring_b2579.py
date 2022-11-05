# 다른 사람 코드 참조

import sys
input = sys.stdin.readline

stairs = []
N = int(input().strip())
for _ in range(N) :
    stairs.append(int(input().strip()))

scores = [0 for _ in range(N)]
scores[0] = stairs[0]
if N >1 :
    scores[1] = stairs[0] + stairs[1]
if N >2 :
    scores[2] = max(stairs[1]+stairs[2], stairs[0]+stairs[2])

for i in range(3, N) :
    scores[i] = max(scores[i-3] + stairs[i-1]+ stairs[i], scores[i-2]+stairs[i])

print(scores[N-1])