n=int(input())
roooooood=list(map(int,input().split()))
prices=list(map(int,input().split()))

mincost = prices[0]
cost = 0
for i in range(n-1):
    if mincost > prices[i]:
        mincost = prices[i]
    cost += roooooood[i] * mincost
    print(roooooood)
print(cost)
