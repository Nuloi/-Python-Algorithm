t = int(input())
k = int(input())  

coins = []  
for i in range(k):
    p, n = map(int, input().split())
    coins.append((p, n))

dp = [0] * (t+1) 
dp[0] = 1 

for p, n in coins:
    for i in range(t, p-1, -1):
        for j in range(1, n+1):
            if i < j*p:
                break
            dp[i] += dp[i-j*p]

print(dp[t])
