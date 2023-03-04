a=str(input())
arr=-1
plus=0
menus=0
s=1
for i in range(len(a)-1):
    if(a[arr]=='+'):
        s=1
    elif(a[arr]=='-'):
        s=1
        menus=plus
        plus=0
    else:
        plus+=(ord(a[arr])-ord('0'))*s
        s*=10
    arr-=1
plus+=(ord(a[0])-ord('0'))*s
print(plus-menus)