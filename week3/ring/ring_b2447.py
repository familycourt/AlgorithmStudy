import sys
input = sys.stdin.readline

N = int(input().strip())
stars = [['*' for _ in range(N)] for _ in range(N)]

def make_blanks(N:int, x:int, y:int) :
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            stars[i][j] = ' '

def make_stars(N:int, x:int, y:int) :
    global stars

    if N==3:
        stars[x+1][y+1] = ' '
        return

    N //= 3
    make_stars(N, x, y)
    make_stars(N, x+N, y)
    make_stars(N, x+2*N, y)
    make_stars(N, x, y+N)
    make_blanks(N, x+N, y+N)
    make_stars(N, x+2*N, y+N)
    make_stars(N, x, y+2*N)
    make_stars(N, x+N, y+2*N)
    make_stars(N, x+2*N, y+2*N)

make_stars(N, 0, 0)

for star in stars :
    print(''.join(star))