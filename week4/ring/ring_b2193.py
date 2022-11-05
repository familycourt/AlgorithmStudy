# i-2번째에 01을 붙이고 i-1번째에 0을 합쳐 만드는 방식으로 ~

import sys
input = sys.stdin.readline

N = int(input().strip())
Nlist = [0,1,1]
for i in range(3, N+1) :
    Nlist.append(Nlist[i-1] + Nlist[i-2])

print(Nlist[N])