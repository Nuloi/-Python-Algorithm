import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    graph[x][y] = 0
    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, -1, 0, 1, -1, 1, -1, 1]
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
            dfs(nx, ny)

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m )]

cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            cnt += 1

print(cnt)
