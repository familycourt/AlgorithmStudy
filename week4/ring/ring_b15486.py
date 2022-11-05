# 다른 사람 코드 참고

import sys
input = sys.stdin.readline

N = int(input().strip())
T = []
P = []
for _ in range(N) :
    t, p = map(int, input().strip().split())
    T.append(t)
    P.append(p)
    
answers = [0 for _ in range(N+1)]

tmp = 0
for i in range(N) :
    tmp = max(tmp, answers[i]) 
    if i+T[i] > N :
        continue
    answers[i+T[i]] = max(answers[i+T[i]], tmp+P[i])
            
print(max(answers))