def dfs(graph, node, visited, orders):

    visited.append(node)

    if len(visited) == n:
        orders.append(list(visited))
    
    for neighbor in sorted(graph[node]):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, orders)
    
n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

given_order = list(map(int, input().split()))

orders = []
dfs(graph, 1, [], orders)

print("orders:", orders)
print("given_order:", given_order)

if given_order in orders:
    print(1)
else:
    print(0)