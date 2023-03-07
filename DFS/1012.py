import sys

sys.setrecursionlimit(10000)  # 최대 재귀 깊이를 10000으로 설정
testcase = int(input())
count = []

for i in range(testcase):
    m, n, o = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    count.append(0)

    for j in range(o):
        a, b = map(int, input().split())
        graph[b][a] = 1  # 입력값과 맞게 좌표를 바꿔줍니다.

    def dfs(x, y):
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
            return True
        return False

    for j in range(n):
        for l in range(m):
            if dfs(j, l):
                count[i] += 1

for i in range(testcase):
    print(count[i])
