import sys

sys.setrecursionlimit(10**6)
n = int(input())
graph = [[0]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]

for j in range(n):
    input_str = input()
    for i in range(len(input_str)):
        if input_str[i] == "R":
            graph[j][i] = 1
        elif input_str[i] == "G":
            graph[j][i] = 2
        elif input_str[i] == "B":
            graph[j][i] = 3


def dfs(x, y, color):
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if graph[x][y]==color and not visited[x][y]:
        visited[x][y] = True
        dfs(x-1,y,color)
        dfs(x,y-1,color)
        dfs(x+1,y,color)
        dfs(x,y+1,color)
        return True
    return False

count=0
for k in range(1,4):
    for i in range(n):
        for j in range(n):
            if dfs(i,j,k)==True:
                count+=1

print(count,end=" ")
count=0

for j in range(n):
    for i in range(n):
        visited[j][i] = False
        if graph[j][i] == 1:
            graph[j][i] = 2

for k in range(2,4):
    for i in range(n):
        for j in range(n):
            if dfs(i,j,k)==True:
                count+=1

print(count)
