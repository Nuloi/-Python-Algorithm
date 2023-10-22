n = int(input())
maps = []
for i in range(n):
    row = list(map(int, input().split()))
    maps.append(row)

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            a = 0
        else:
            a = maps[i - 1][j - 1]
        if i == j:
            b = 0
        else:
            b = maps[i - 1][j]
        row_max = max(a, b)
        maps[i][j] += row_max

print(max(maps[n - 1]))
