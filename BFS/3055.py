from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    water_queue = deque()

    for i in range(R):
        for j in range(C):        
            if forest[i][j] == '*': 
                water_queue.append((i,j))
                water_visited[i][j] = 0
            elif forest[i][j] == 'S': 
                queue.append((i,j))
                visited[i][j] = True
                forest[i][j] = 0

    while water_queue:
        x,y = water_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and forest[nx][ny] != 'X' and forest[nx][ny] != 'D' and water_visited[nx][ny] == -1:
                water_visited[nx][ny] = water_visited[x][y]+1
                water_queue.append((nx,ny))   
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and forest[nx][ny] == 'D':
                return forest[x][y]+1
            
            if 0 <= nx < R and 0 <= ny < C and forest[nx][ny] != 'X' and (water_visited[nx][ny] > forest[x][y]+1 or water_visited[nx][ny] == -1) and not visited[nx][ny]:
                forest[nx][ny] = forest[x][y]+1
                visited[nx][ny] = True
                queue.append((nx,ny))
                
    return 'KAKTUS'

R, C = map(int, input().split())
forest = [list(input()) for _ in range(R)]
water_visited = [[-1] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]

result = bfs()
print(result)
