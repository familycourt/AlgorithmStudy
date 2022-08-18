# 검문

import sys
import math

N = int(sys.stdin.readline())

list_a = []
for i in range(N):
    list_a.append(int(sys.stdin.readline()))

diff_a = []
for i in range(N - 1):
    diff_a.append(abs(list_a[i + 1] - list_a[i]))

# M이 될 수 있는 최대 최소


max_M = max(list_a)
min_M = min(list_a)


# TODO: i 바뀔 때 마다 나머지 초기화 필요
# TODO: 출력 마지막 공백 제거 필요
# TODO: reaminder 1이면 탐색 종료
# 시간을 줄이는 방법 : 2중 for문 없애기?
# 힌트: a를 m으로 나눈 나머지와 b를 m으로 나눈 나머지가 같다면
# (a-b)는 m의 배수가 됩니다.

# 순회하면서 최대공약수 업데이트
remainder = diff_a[0]
for i in range(1, N - 1):
    remainder = math.gcd(remainder, diff_a[i])

output = []
for i in range(2, int(math.sqrt(remainder)) + 1):
    if remainder % i == 0:
        output.append(i)
        output.append(remainder // i)
output.append(remainder)
output = list(set(output))
output.sort()
print(' '.join(map(str, output)))
