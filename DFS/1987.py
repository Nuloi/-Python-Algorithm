dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    global result
    result = max(result, cnt)
    alphabet = board[x][y]
    visited[ord(alphabet) - ord('A')] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >= c or visited[ord(board[nx][ny]) - ord('A')]:
            continue
        dfs(nx, ny, cnt+1)
    visited[ord(alphabet) - ord('A')] = False

r, c = map(int, input().split())
board = [input() for _ in range(r)]

visited = [False] * 26
visited[ord(board[0][0]) - ord('A')] = True
result = 1
dfs(0, 0, 1)

print(result)