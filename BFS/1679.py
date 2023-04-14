import sys
from collections import deque

def bfs(n, k):
    queue = deque([(n, 0)])
    visited = set([n])
    while queue:
        x, time = queue.popleft()
        if x == k:
            return time
        for nx in [x-1, x+1, x*2]:
            if 0 <= nx <= 100000 and nx not in visited:
                visited.add(nx)
                queue.append((nx, time+1))


n, k = map(int, sys.stdin.readline().split())
print(bfs(n, k))

