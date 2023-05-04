from collections import deque

def bfs(n, k):
    q = deque()
    q.append([n, 0])
    visit = [0]*200001
    visit[n] = 1
    dx = [2, -1, 1]
    
    while q:
        x, time = q.popleft()
        
        if x == k:
            return time
        
        for i in range(3):
            if i == 0:
                nx = x * dx[i]
                
                if visit[nx] == 0 and 0 <= nx <= 100000:
                    q.append([nx, time])
                    visit[nx] = 1
            else:
                nx = x + dx[i]
                
                if visit[nx] == 0 and 0 <= nx <= 100000:
                    q.append([nx, time+1])
                    visit[nx] = 1

n, k = map(int, input().split())
print(bfs(n, k))
