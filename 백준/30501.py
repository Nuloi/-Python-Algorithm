N = int(input())
name = [input() for _ in range(N)]

for i in range(N):
    if 'S' in name[i]:
        print(name[i])
