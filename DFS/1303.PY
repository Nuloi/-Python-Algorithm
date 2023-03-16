import sys

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [[0]*n for _ in range(m)]
visited = [[False]*n for _ in range(m)]

for i in range(m):
    input_str = input()
    for j in range(len(input_str)):
        if input_str[j] == "B":
            graph[i][j] = 2
        elif input_str[j] == "W":
            graph[i][j] = 1

power=[0,0]

p=0
def dfs(x, y, color):
    global p
    if x<=-1 or x>=m or y<=-1 or y>=n:
        return False
    if graph[x][y]==color and not visited[x][y]:
        visited[x][y] = True
        p+=1
        dfs(x-1,y,color)
        dfs(x,y-1,color)
        dfs(x+1,y,color)
        dfs(x,y+1,color)
        return True
    return False

for k in range(1,3):
    for i in range(m):
        for j in range(n):
            p=0
            if dfs(i,j,k)==True:
                power[k-1]+=p*p

print(power[0],power[1])
