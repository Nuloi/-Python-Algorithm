n=int(input())
tr=[]
for i in range(n):
    a=int(input())
    tr.append(a)
tr.sort()
n-=1
while(2<=n):
    if tr[n-2]+tr[n-1]>tr[n]:
        print(tr[n-2]+tr[n-1]+tr[n])
        break
    n-=1
if n==1:print("-1")