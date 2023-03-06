n,m=map(int,input().split())

graph=[]
visited=[]

for i in range(n):
    graph.append(list(map(int,input())))
    visited.append([False]*m)

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]==0 and not visited[x][y]:
        visited[x][y] = True
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

count=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            count+=1
print(count)
