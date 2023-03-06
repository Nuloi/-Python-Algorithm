n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))
def dfs(x, y):
    if x >= n or y >= n or graph[x][y]==0:
        return False
    if graph[x][y]==-1:
        print("HaruHaru")
        exit()
    dfs(x+graph[x][y],y)
    dfs(x,y+graph[x][y])
    
dfs(0, 0)
print("Hing")