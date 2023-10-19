from collections import deque

def BFS(graph):
    visited = [False] * 101
    dq = deque()
    dq.append((1, 0))

    while dq:
        node, moves = dq.popleft()

        if node == 100:
            return moves

        for dice in range(1, 7):
            if node + dice<=100:
                next_node = graph[node + dice]
                if not visited[next_node]:
                    dq.append((next_node, moves + 1))
                    visited[next_node] = True

n, m = map(int, input().split())
graph = [i for i in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    graph[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    graph[u] = v

result = BFS(graph)
print(result)
