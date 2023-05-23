N=int(input())
dp=['x','SK','CY','SK','SK','SK']
for i in range(6, N+1):
    if dp[i-1]=='CY' or dp[i-3]=='CY' or dp[i-4]=='CY':
        dp.append('SK')
    else:
        dp.append('CY')
print(dp[N])