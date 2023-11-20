n = int(input())
m = int(input())

friend = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

invited = set()
if friend[1]:
    for i in friend[1]:
        invited.add(i)
        if friend[i]:
            for j in friend[i]:
                invited.add(j)

if len(invited) == 0:
    print(0)
else:
    print(len(invited)-1)
