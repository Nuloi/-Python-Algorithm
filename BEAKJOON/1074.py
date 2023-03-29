n,r,c=map(int,input().split())
def ess(n,y,x):
    line = (2 ** (n - 1))
    graph = line ** 2
    if n==1:
        if 1<=y and 1<=x:
            return 3
    
        if 1<=y and 1>x:
            return 2
    
        if 1>y and 1<=x:
            return 1
        
        else:
            return 0
        
    if line<=y and line<=x:
        return graph*3+ess(n-1,y-line,x-line)
    
    if line<=y and line>x:
        return graph*2+ess(n-1,y-line,x)
    
    if line>y and line<=x:
        return graph*1+ess(n-1,y,x-line)
        
    if line>y and line>x:
        return graph*0+ess(n-1,y,x)
    
print(ess(n,r,c))