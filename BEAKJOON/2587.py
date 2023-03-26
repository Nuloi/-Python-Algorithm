a=[]
for i in range(5):
    a.append(int(input()))
mid=sum(a)/5
a.sort()
print(round(mid))
print(a[2])