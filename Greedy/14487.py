n=int(input())
i=list(map(int,input().split()))
i.sort()
print(sum(i)-i[-1])