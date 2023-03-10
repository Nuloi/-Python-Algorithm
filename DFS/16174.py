n = int(input())

chekpoint = [] 

for i in range(n):
    bigmap = list(map(int, input().split()))
    chekpoint.append(bigmap)

visited = [[False]*n for _ in range(n)]

def dfs(x, y):
    if x == n-1 and y == n-1: 
        return True
    
    visited[x][y] = True 
    k = chekpoint[x][y] 
    
    if x+k < n and not visited[x+k][y]: 
        if dfs(x+k, y):
            return True
    if y+k < n and not visited[x][y+k]: 
        if dfs(x, y+k):
            return True
    return False

if dfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")