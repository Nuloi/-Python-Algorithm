from collections import deque

def BFS(f, s, g, u, d):
    dq = deque([(s, 0)])
    visited = set([s])
    while dq:
        x, time = dq.popleft()
        if x == g:
            return time
        for nx in [x + u, x - d]:
            if nx != x and 0 < nx <= f and nx not in visited:
                visited.add(nx)
                dq.append((nx, time + 1))
    return "use the stairs"

f, s, g, u, d = map(int, input().split())
result = BFS(f, s, g, u, d)
print(result)
