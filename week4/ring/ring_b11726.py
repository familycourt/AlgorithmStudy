# 규칙을 찾긴했는데.. 왜 이건지는 모르겠다.. 

import sys
input = sys.stdin.readline 

n = int(input().strip())
rectangles = [0, 1, 2, 3] + [0 for _ in range(4, n+1)]

for i in range(4, n+1) :
    rectangles[i] = rectangles[i-1] + rectangles[i-2]

print(rectangles[n]%1007)