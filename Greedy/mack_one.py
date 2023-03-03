#어떤 수 N이 1이 될때 까지 다음 두 과정중 하나를 반복적으로 선택하여 수행하려고한다
#1. N에서 1을 뺸다 2. N에서 K로 나눈다.
N,K=map(int, input().split())
count=int(0)
while(N!=1):
    if(N%K==0):
        N/=K
    else:
        N-=1        
    count+=1
print(count)