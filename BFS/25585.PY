from collections import deque
import sys

def bfs(start, visited, grid, N):
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, -1, 1]
    
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    
    while queue:
        r, c, cnt = queue.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
                visited[nr][nc] = cnt + 1
                queue.append((nr, nc, cnt + 1))
                
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    return nr, nc, visited[nr][nc]

    return -1, -1, sys.maxsize

def solve(grid, N):
    targets = []
    start = None

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                targets.append((i, j))
            elif grid[i][j] == 2:
                start = (i, j, 0)

    total_distance = 0
    while targets:
        visited = [[-1] * N for _ in range(N)]
        r, c, dist = bfs(start, visited, grid, N)

        if r == -1:
            return "Shorei", -1

        total_distance += dist
        start = (r, c, 0)
        targets.remove((r, c))

    return "Undertaker", total_distance

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

result, distance = solve(grid, N)
print(result)
if distance != -1:
    print(distance)
