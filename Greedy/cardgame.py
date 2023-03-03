
a,b=map(int,input().split())
high=int(0)
for i in range(a):
    num=list(map(int,input().split()))
    num.sort()
    mn=num[0]
    high=max(high,mn)
print(high)