import sys

sys.setrecursionlimit(10000)
z=0
count = []
while True:
    m, n = map(int, input().split())

    if m==0 and n==0 :
        break

    graph=[]
    graph = [list(map(int, input().split())) for _ in range(n)]
    count.append(0)
    
    def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or graph[x][y] == 0:
                return False
            if graph[x][y] == 1:
                graph[x][y] = 0
                dfs(x-1, y)
                dfs(x-1, y+1)
                dfs(x, y-1)
                dfs(x+1, y-1)
                dfs(x+1, y+1)
                dfs(x+1, y)
                dfs(x-1, y-1)
                dfs(x, y+1)
                return True
            return False

    for j in range(n):
        for l in range(m):
            if dfs(j, l):
                count[z] += 1
    z+=1
    graph = None

for i in range(z):
    print(count[i])