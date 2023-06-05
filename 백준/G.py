import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input().rstrip())
dirs = input().rstrip()
K = int(input().rstrip())
coords = [tuple(map(int, input().split())) for _ in range(K)]

x, y, z = [0], [0], [0]
for dir in dirs:
    if dir == 'R':
        x.append(x[-1]+1)
        y.append(y[-1])
        z.append(z[-1]+1)
    elif dir == 'U':
        x.append(x[-1])
        y.append(y[-1]+1)
        z.append(z[-1]+1)
    else:
        x.append(x[-1]+1)
        y.append(y[-1]+1)
        z.append(z[-1])

coords.sort(key=lambda t: (t[0]+t[1], t[1]))
visitables = sorted((x[i]+y[i], y[i]) for i in range(len(x)))

answer = 0
for x, y in coords:
    idx = bisect_left(visitables, (x+y, y))
    if idx != len(visitables) and visitables[idx] == (x+y, y):
        answer += 1

print(answer)
    