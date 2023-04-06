from collections import deque

def bfs(start, campus, visited):
    q = deque([start])
    visited[start[0]][start[1]] = True
    people_count = 0

    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if campus[nx][ny] == 'P':
                    people_count += 1
                    q.append((nx, ny))
                elif campus[nx][ny] == 'O':
                    q.append((nx, ny))

    return people_count

n, m = map(int, input().split())
campus = [input().strip() for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':#도현이 위치
            start = (i, j)

result = bfs(start, campus, visited)

if result == 0:
    print("TT")
else:
    print(result)
