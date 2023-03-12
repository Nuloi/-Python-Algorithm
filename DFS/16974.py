import sys

sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

visited = [False] * (n + 1)        
graph=[[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) 

order=list(map(int,input().split()))
if order[0]!=1:
    print("0")
    exit()
de=1

def dfs(graph,v):
    tr=0
    global de 
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            if i==order[de]:
                if de==n-1:
                    print("1")
                    exit()
                de=de+1
                tr=1
                dfs(graph,i)
                break
    if tr==1:
        dfs(graph,v)


dfs(graph,1)
print("0")
