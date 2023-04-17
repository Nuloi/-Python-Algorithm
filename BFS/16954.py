from collections import deque
       
a,b=map(int,input().split())

def BFS(a,b):
    queue = deque([(a, 1)])
    visited = set([a])
    while queue:
        x, time = queue.popleft()
        if x == b:
            return time
        for nx in [x*2,(x*10)+1]:
            if 0 <= nx <= 1000000000 and nx not in visited:
                visited.add(nx)
                queue.append((nx, time+1))
                
if None==BFS(a,b):
    print(-1)
else:
    print(BFS(a,b))
