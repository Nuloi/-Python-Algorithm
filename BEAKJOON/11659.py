n,m=map(int,input().split())
arr=list(map(int, input().split()))

sumarr=[0]
i_j_list=[]
total=0

for z in range(m):
    i_j = list(map(int,input().split()))
    i_j_list.append(i_j)

for number in arr:
    total += number
    sumarr.append(total)

for i_j in i_j_list:
    i , j = i_j[0], i_j[1]
    print(sumarr[j] - sumarr[i-1])