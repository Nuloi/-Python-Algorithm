import sys

n = [True] * 10001
n[0] = n[1] = False
for i in range(2, 101):
    if n[i]:
        for j in range(i * i, 10001, i):
            n[j] = False

def get_goldbach_partition(n):
    mins = sys.maxsize
    for p in range(2, n):
        if n[p]:
            if n[n - p]:
                if abs(p - (n - p)) < mins:
                    mins = abs(p - (n - p))
                    part = (p, n - p)
    return part

t = int(input())
for _ in range(t):
    n = int(input())
    part = get_goldbach_partition(n)
    print(part[0], part[1])
