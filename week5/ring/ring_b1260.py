from collections import deque
import sys
input = sys.stdin.readline   

N, M, V = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]
visited_dfs = []
visited_bfs = []

def DFS(v : int) :
    visited_dfs.append(v)
    for node in graph[v] :
        if node not in visited_dfs :
            DFS(node)
  
def BFS(v :int) :
    queue = deque([v])
    visited_bfs.append(v)
    while queue :
        x = queue.popleft()
        for node in graph[x] :
            if node not in visited_bfs :
                visited_bfs.append(node)
                queue.append(node)          

for _ in range(M) :
    node1, node2 = map(int, input().strip().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# 작은 것부터 방문 할 예정이므로.. sort를 꼬옥 해줘야한다.. !
for i in range(1, N+1) :
    graph[i].sort()    
    
DFS(V)
print(' '.join(list(map(str,visited_dfs))))

BFS(V)
print(' '.join(list(map(str,visited_bfs))))