def dfs(c, n, jum, vis):
    count = 1
    for d in [c-jum, c+jum]:
        if 0 <  d <= n and not vis[d]:
            vis[d] = True
            count += dfs(d, n, ai[d], vis)
    return count

n = int(input())
ai = list(map(int, input().split()))
c = int(input())
ai.insert(0,0)
vis = [False] * (n + 1)
vis[c] = True

print(dfs(c, n, ai[c], vis))
