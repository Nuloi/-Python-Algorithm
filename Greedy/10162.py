import math
time=int(input())
a=math.trunc(time/300)
time=time%300
b=math.trunc(time/60)
time=time%60
c=math.trunc(time/10)
time=time%10
if(time==0):
    print(a,b,c)
else:
    print("-1")