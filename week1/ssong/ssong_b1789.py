# 수들의 합

import sys

# 서로다른 자연수 N갸의 합 S
S = int(sys.stdin.readline())

# 더하는 갯수가 가장 많을 때를 구해라
cnt = 0
for i in range(S):
    S = S - (i + 1)
    if(S < i):
        break
    print(S, i + 1)
    cnt += 1
cnt -= 1
print(cnt)