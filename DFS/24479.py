n,m,l=map(int,input().split())

graph = [[] for _ in range(n)]
visited = [False] * (n)
num=[0]*n

for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
for i in range(n):
    graph[i].sort() # 인접 정점을 오름차순으로 정렬

def dfs(graph, v, visited):
    visited[v] = True
    num[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return False

dfs(graph,l-1,visited,num)

for i in range(n):
    print(num[i]*i)
