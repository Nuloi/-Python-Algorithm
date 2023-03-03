N=int(input())
M=input()
x=1
y=1
for i in range(len(M)):
    if(M[i]=="R" and x<N):
        x+=1
    if(M[i]=="L" and x<1):
        x-=1
    if(M[i]=="U" and y<1 ):
        y-=1
    if(M[i]=="D" and y<N):
        y+=1
print(y, x)