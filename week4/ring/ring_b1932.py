import sys
input = sys.stdin.readline

nlist = []
n = int(input().strip())

for _ in range(n) :
    nlist.append(list(map(int, input().strip().split())))

for i in range(1, len(nlist)) :
    for j in range(len(nlist[i])) :
        if j==0 :
            nlist[i][j] += nlist[i-1][j]
        elif j == len(nlist[i])-1 :
            nlist[i][j] += nlist[i-1][j-1]
        else :
            nlist[i][j] += max(nlist[i-1][j-1], nlist[i-1][j])
            
print(max(nlist[-1]))
        