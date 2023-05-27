N,L=map(int,input().split())
pipe=list(map(int,input().split()))
pipe.sort(reverse=1)

count=1
tap=L
for i in range(1,N):
    if (pipe[i-1]-pipe[i]<tap):
        tap-=pipe[i-1]-pipe[i]
    else:
        tap=L
        count+=1
print(count)