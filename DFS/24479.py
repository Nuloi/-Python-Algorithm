import sys

n, m, l = map(int, input().split())

visited = set()
num = []
graph = [[] for _ in range(n+1)]

for j in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    for i in graph[v]:
        if i not in visited:
            visited.add(i)
            num.append(i)
            dfs(i)

visited.add(l)
num.append(l)
dfs(l)

num.extend([0]*(n-len(num)))

for i in range(n):
    print(num[i])
