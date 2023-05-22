from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def shortest_path(N, M, grid):
    # 방문 여부와 벽을 뚫었는지 여부를 저장하는 배열
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    start = (0, 0, 0, 0)  # (x, y, 벽 부순 횟수, 이동 횟수)

    queue = deque()
    queue.append(start)
    visited[0][0][0] = True
    
    while queue:
        x, y, walls, count = queue.popleft()
        
        if x == N - 1 and y == M - 1:
            return count + 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                # 벽을 만났을 때
                if grid[nx][ny] == 1:
                    # 벽을 부술 기회가 있는 경우
                    if walls == 0 and not visited[nx][ny][1]:
                        queue.append((nx, ny, 1, count + 1))
                        visited[nx][ny][1] = True
                # 이동 가능한 공간인 경우
                elif not visited[nx][ny][walls]:
                    queue.append((nx, ny, walls, count + 1))
                    visited[nx][ny][walls] = True
    
    return -1

N, M = map(int, input().split())
grid = []
for i in range(N):
    row = list(map(int, input().rstrip()))
    grid.append(row)
if N==1 and M==1:
    print("-1")
    exit(0)
result = shortest_path(N, M, grid)
print(result)
