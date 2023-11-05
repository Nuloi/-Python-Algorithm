import sys
from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph)
    order = [0] * len(graph)  

    queue = deque()
    queue.append(start)
    visited[start] = True
    order[start] = 1  

    counter = 2 

    while queue:
        node = queue.popleft()

        for j in sorted(graph[node]):
            if not visited[j]:
                queue.append(j)
                visited[j] = True
                order[j] = counter
                counter += 1

    return order

N, M, R = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

order = bfs(graph, R - 1) 

for i in range(N):
    print(order[i])
