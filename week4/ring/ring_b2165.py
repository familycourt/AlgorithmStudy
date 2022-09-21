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
    if cnt == 2 :
        # 차례대로 i(본인), i-1, i-2 뺀 경우 
        tmp0 = drinks[i-1]      
        tmp1 = drinks[i-2]+glasses[i]
        tmp2 = drinks[i-3]+glasses[i-1]+glasses[i]
        
        if tmp0 >= max(tmp1, tmp2) :
            cnt=0
            drinks[i] = tmp0
        elif tmp1 >= tmp2 :
            cnt=1
            drinks[i] = tmp1
        else :
            cnt=2
            drinks[i] = tmp2
    else : 
        drinks[i] += drinks[i-1]
        cnt += 1
        
print(drinks[n])