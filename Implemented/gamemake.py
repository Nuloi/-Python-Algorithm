a,b=map(int,input().split())
x,y,s=map(int,input().split())
maps=[[0]*a]*b
for i in range(a):
    for j in range(b):
        maps[i].append(input())
print(maps[0][0])
print(maps[0][1])
print(maps[1][0])
print(maps[1][1])