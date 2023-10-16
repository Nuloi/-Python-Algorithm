import sys

n, m = map(int, sys.stdin.readline().split())

graph = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1


for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k]>0 and graph[k][j]:
                if graph[i][j]==0:
                    graph[i][j]=graph[i][k]+ graph[k][j]
                else:
                    graph[i][j]=min(graph[i][j],graph[i][k]+ graph[k][j])

mini = float('inf')
low = 0

for i in range(n):
    graph[i][i] = 0
    row_sum = sum(graph[i])
    
    if row_sum < mini:
        low = i
        mini = row_sum

print(low + 1)
