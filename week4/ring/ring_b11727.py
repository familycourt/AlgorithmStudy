# combination으로 풀면 무적권 시간 초과 
# 11726의 원리를 이해하면 이것도 자동으로 풀 수 있다.

import sys
input = sys.stdin.readline


n = int(input().strip())
rectangles = [0, 1, 3] + [0 for _ in range(3, n+1)]

for i in range(3, n+1) :
    rectangles[i] = rectangles[i-2]*2 + rectangles[i-1]

print(rectangles[n]%10007)


