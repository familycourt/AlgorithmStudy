import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input().strip())
graph = []
visited=[]

def DFS(x:int) :
    if x not in visited:
        visited.append(x)
        numbers.remove(x)
        DFS(graph[x]) 

for _ in range(T) :
    
    N = int(input().strip())
    graph = [0] + list(map(int, input().strip().split()))
    numbers = [int(x) for x in range(1, N+1)]
    
    cnt=0
    visited=[]
    while numbers :
        DFS(numbers[0])
        cnt+=1
        
    print(cnt)