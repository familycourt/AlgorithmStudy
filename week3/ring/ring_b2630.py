# 다른 사람 코드 참고 ... 재귀는 언제나 어렵다.

import sys
input = sys.stdin.readline

papers = []
white, blue = 0, 0

def discrim(n : int, x : int, y : int) :
    global white, blue 
    color = papers[x][y]
    for i in range(x, x+n) :
        for j in range(y, y+n) :
            if color != papers[i][j] :
                discrim(n//2, x, y)
                discrim(n//2, x, y+n//2)
                discrim(n//2, x+n//2, y)
                discrim(n//2, x+n//2, y+n//2)
                return

    if color == 0 :
        white += 1
    else :
        blue += 1

# papers = [list(map(int, input().strip().split())) for _in range(N)]
N = int(input().strip())
for _ in range(N) :
    papers.append([int(x) for x in input().strip().split()])

discrim(N, 0, 0)
print(white)
print(blue)




