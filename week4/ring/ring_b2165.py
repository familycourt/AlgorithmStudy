# 내 코드가 통과는 했지만 굉장히 잘못됐음을 직감하고 참고하여 다시 작성

import sys 
import copy
input = sys.stdin.readline

n = int(input().strip())
glasses = [0]
for _ in range(n) :
    glasses.append(int(input().strip()))

cnt=2    
drinks = copy.deepcopy(glasses)
if n!=1 : drinks[2] += drinks[1]  

for i in range(3, n+1) :
    drinks[i] = max(drinks[i-1], drinks[i-2]+glasses[i], drinks[i-3]+glasses[i-1]+glasses[i])
    
print(drinks[n])