import sys

n, m = map(int, input().split())

name_num = {}
num_name = {}
for i in range(1, n+1):
    name = sys.stdin.readline().rstrip()
    name_num[name] = i
    num_name[i] = name

for i in range(m):
    q = sys.stdin.readline().rstrip()
    if q.isdigit(): 
        num = int(q)
        print(num_name[num])
    else: 
        name = q
        print(name_num[name])
