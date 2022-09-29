# 다른 사람 코드  참고 - > 진차 참신하네..

import sys
input = sys.stdin.readline

N = int(input().strip())
numbers = [0]*10001

for _ in range(N) :
    numbers[int(input().strip())] +=1

for i in range(10001) :
    if numbers[i] > 0 :
        for j in range(numbers[i]) :
            print(i)