n, m = map(int, input().split()) 
first = set()

for i in range(n):
    name = input().strip()
    first.add(name)

count = 0  
names = [] 

for i in range(m):
    name = input().strip()
    if name in first: 
        count += 1
        names.append(name)

names.sort()
print(count)
for name in names:
    print(name)