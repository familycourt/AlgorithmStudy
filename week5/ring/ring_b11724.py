import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]

visited=[]
nodes = [int(x) for x in range(1, N+1)]
def BFS(x: int) :
    visited.append(x)
    nodes.remove(x)
    
    if not graph[x] : return
    
    for y in graph[x] :
        if y not in visited :
            BFS(y)

for _ in range(M) :
    node1, node2 = map(int, input().strip().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    
cnt=0
while nodes :
    cnt += 1
    BFS(nodes[0])

print(cnt)