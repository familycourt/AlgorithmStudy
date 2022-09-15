import sys
input = sys.stdin.readline

N = int(input().strip())
Alist = list(map(int, input().strip().split()))
Sumlist = [0 for _ in range(N)]

for i in range(N) :
    tmp = []
    for j in range(i) :
        if Alist[i] > Alist[j]:
            tmp.append(Sumlist[j])
    
    if tmp : 
        Sumlist[i] = max(tmp)
    Sumlist[i] += Alist[i]

print(max(Sumlist))


