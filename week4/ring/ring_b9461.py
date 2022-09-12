import sys
input = sys.stdin.readline

triangles = [0,1,1,1,2,2,3,4,5,7,9]

T = int(input().strip())
for _ in range(T) :
    N = int(input().strip())
    if len(triangles) < N+1 :
        for i in range(len(triangles), N+1) :
            triangles.append(triangles[i-1] + triangles[i-5])
    print(triangles[N])
