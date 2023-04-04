from collections import deque

def bfs(m, n, box):
    queue = deque()
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))

    max_day = 0
    for row in box:
        max_day = max(max_day, max(row))

    return max_day - 1

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

result = bfs(m, n, box)

for row in box:
    if 0 in row:
        print(-1)
        exit(0)

print(result)
