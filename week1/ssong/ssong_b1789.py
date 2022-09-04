# 수들의 합

import sys

# 서로다른 자연수 N갸의 합 S
S = int(sys.stdin.readline())

# 더하는 갯수가 가장 많을 때를 구해라
# TODO: 빼고 난 결과가 다음 수보다 작다면 빼지 않고 다음 수로 넘어감
cnt = 0
for i in range(1, S + 1):
    if(S == i):
        cnt += 1
        break
    if ((S - i) < i + 1):
        continue
    S = S - i
    cnt += 1


# 뺀 다음수보다 S가 작다면 다음수가 마지막 수이다
print(cnt)
