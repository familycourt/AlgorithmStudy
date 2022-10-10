import sys
input = sys.stdin.readline
# 런타임에러 = 재귀에러 발생하므로 재귀 허용치를 늘림 
sys.setrecursionlimit(10000)

N, M = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]

visited=[]
def DFS(x:int) :
    visited.append(x)
    for y in graph[x] :
        if y not in visited :
            DFS(y)

for _ in range(M) :
    node1, node2 = map(int, input().strip().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    
cnt=0
while len(visited) != N :
    for i in range(1,N+1) :
        if i not in visited :
            cnt+=1
            DFS(i)

print(cnt)