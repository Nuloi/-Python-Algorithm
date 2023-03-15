import sys

sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0]  
dy = [0, 1, 0, -1]  

def dfs(x, y):
    visited[x][y] = True 
    for i in range(4):  
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < h and ny >= 0 and ny < w:  
            if not visited[nx][ny] and grid[nx][ny] == '#': 
                dfs(nx, ny) 


t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(input())
    visited = [[False] * w for _ in range(h)] 
    count = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and grid[i][j] == '#': 
                dfs(i, j)  
                count += 1 
    print(count) 
