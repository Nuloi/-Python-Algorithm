a=[]
for i in range(7):
    int(input(a[i]))
a.sort()
t=0
low=0
su=0
for i in range(7):
    if(a[i]%2!=0):
        if(t==0):
            low=a[i]
    su+=a[i]
if su==0:
    print("-1")
else:
    print(su)
    print(low)
