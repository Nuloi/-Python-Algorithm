a=input()
count=0
if(a[1]>'2'):#위로
    if(a[0]>'a'):
        count+=1
    if(a[0]<'h'):
        count+=1
if(a[1]<'7'):#아래로
    if(a[0]>'a'):
        count+=1
    if(a[0]<'h'):
        count+=1
if(a[0]>'b'):
    if(a[1]>'1'):
        count+=1
    if(a[1]<'8'):
        count+=1
if(a[0]<'g'):
    if(a[1]>'1'):
        count+=1
    if(a[1]<'8'):
        count+=1
print(count)