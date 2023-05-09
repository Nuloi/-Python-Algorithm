import math
n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
for i in range(n):
    a[i]-=b
    if a[i]<0:
        a[i]=0
low=n
for i in range(n):
    if a[i]!=0:
        low+=math.ceil(a[i]/c)
print(low)