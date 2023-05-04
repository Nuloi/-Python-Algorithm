from collections import deque

def BFS(n,k):
    visited = [-1] * 100001 
    count = [0] * 100001 
    dq = deque()
    dq.append(n)
    visited[n] = 0
    count[n] = 1

    while dq:
        x = dq.popleft()

        for nx in (x-1, x+1, 2*x): 
            if 0 <= nx <= 100000:
                if visited[nx] == -1:
                    visited[nx] = visited[x] + 1
                    count[nx] = count[x]
                    dq.append(nx)
                elif visited[nx] == visited[x] + 1: 
                    count[nx] += count[x]
                    
    print(visited[k])
    print(count[k]) 
    return 0

n,k=map(int,input().split())
BFS(n,k)