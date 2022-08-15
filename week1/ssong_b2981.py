# 검문

import sys

N = int(sys.stdin.readline())

list_a = []
for i in range(N):
    list_a.append(int(sys.stdin.readline()))

# M이 될 수 있는 최대 최소


max_M = max(list_a)
min_M = min(list_a)


# TODO: i 바뀔 때 마다 나머지 초기화 필요
# TODO: 출력 마지막 공백 제거 필요
# TODO: reaminder 0이면 탐색 종료
remainder = 0
output = []
for i in range(2, max_M + 1):
    for index, a in enumerate(list_a):
        if index == 0:
            remainder = a % i
        else:
            if a % i != remainder:
                break
            elif index == N - 1:
                output.append(i)

print(' '.join(map(str, output)))