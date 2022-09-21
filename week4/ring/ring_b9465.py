import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T) :
    n = int(input().strip())
    stickers = []
    stickers.append(list(map(int, input().strip().split())))
    stickers.append(list(map(int, input().strip().split())))
    
    if n==1:
        print(max(stickers[0][0], stickers[1][0]))
        continue
    
    stickers[0][1] += stickers[1][0]
    stickers[1][1] += stickers[0][0]
    
    for i in range(2, n) :
        stickers[0][i] += max(stickers[0][i-2], stickers[1][i-2], stickers[1][i-1])
        stickers[1][i] += max(stickers[1][i-2], stickers[0][i-2], stickers[0][i-1])
        
    print(max(stickers[0][n-2], stickers[0][n-1], stickers[1][n-2], stickers[1][n-1]))