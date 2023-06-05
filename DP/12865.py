N =int(input())
weights = []
values = []

for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)
dp = [[0] * (K + 1) for _ in range(N + 1)]
    
for i in range(1, N + 1):
    weight = weights[i - 1]
    value = values[i - 1]
    
    for j in range(1, K + 1):
        if weight > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[N][K])

