from collections import deque

n, m = map(int, input().split())
grid = []
for i in range(n):
    row = list(map(int, input().strip()))
    grid.append(row)

x, y = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            x, y = i, j

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dq = deque([(x, y, 0)]) 
visited = [[False] * m for _ in range(n)]
visited[x][y] = True 

distance = [float('inf')] * 4

while dq:
    x, y, dist = dq.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if grid[nx][ny] == 1 or visited[nx][ny]:
            continue
        visited[nx][ny] = True
        if grid[nx][ny] >= 2 and grid[nx][ny] <= 5:
            idx = grid[nx][ny] - 2
            distance[idx] = dist + 1
        dq.append((nx, ny, dist + 1))

if min(distance) == float('inf'):
    print("NIE")
else:
    print("TAK")
    print(min(distance))
