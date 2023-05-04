a,b=map(int,input().split())
if a<=b:print((b+a)*(b+1-a)//2)
else :print((a+b)*(a+1-b)//2)