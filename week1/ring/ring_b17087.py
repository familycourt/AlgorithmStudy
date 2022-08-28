import sys
import math
input = sys.stdin.readline

N, S = map(int, input().strip().split())
locations = [abs(S-int(x)) for x in input().strip().split()]

# gcd 함수에 리스트를 넣는 방법은 없는가..
answer = locations[0]
for x in locations[1:] :
    answer = math.gcd(answer, x)
print(answer)
