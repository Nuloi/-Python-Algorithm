import heapq

inf = 10 ** 11

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[i] = [inf] * (N + 1)
    graph[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

start, end = map(int, input().split())

def dijkstra(graph, start):
    distances = [inf] * (N + 1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, node = heapq.heappop(queue)
        
        if distances[node] < dist:
            continue
        
        for i in range(1, N + 1):
            cost = dist + graph[node][i]
            if cost < distances[i]:
                distances[i] = cost
                heapq.heappush(queue, (cost, i))
    
    return distances

result = dijkstra(graph, start)

print(result[end])
